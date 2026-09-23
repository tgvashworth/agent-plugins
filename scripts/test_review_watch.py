"""Watcher regressions with a fake gh executable; no network or GitHub writes."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


WATCH = Path(__file__).resolve().parents[1] / "utils/skills/review-agent/scripts/watch.sh"
FAKE_GH = r'''
import json, os, pathlib, sys
root = pathlib.Path(os.environ["WATCH_FIXTURE"])
fixture = json.loads((root / "fixture.json").read_text())
counts_path = root / "counts.json"
counts = json.loads(counts_path.read_text()) if counts_path.exists() else {}
args = sys.argv[1:]
def next_value(key, default):
    i = counts.get(key, 0)
    counts[key] = i + 1
    counts_path.write_text(json.dumps(counts))
    values = fixture.get(key, [default])
    return values[min(i, len(values) - 1)]
if args[:2] == ["repo", "view"]:
    print("owner/repo")
elif args[:2] == ["pr", "view"]:
    print("author" if "author" in args else next_value("lifecycle", "CLOSED"))
elif args[:2] == ["pr", "checks"]:
    value = next_value("checks", {"data": []})
    print(value.get("raw", json.dumps(value.get("data"))))
    sys.exit(value.get("exit", 0))
elif args[0] == "api":
    key = "issues" if "/issues/" in args[1] else "reviews" if args[1].endswith("/reviews") else "comments"
    value = next_value(key, {"messages": []})
    if value.get("exit"):
        sys.exit(value["exit"])
    for message in value["messages"]:
        print(message["id"] if args[-1] == ".[] | .id" else str(message["id"]) + "\t" + message["line"])
else:
    raise AssertionError(args)
'''


def checks(bucket, exit_code=0):
    return {"data": [{"name": "build", "bucket": bucket, "state": bucket, "link": "https://example.test/build"}], "exit": exit_code}


class WatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="review-watch-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "gh").write_text("#!" + sys.executable + "\n" + FAKE_GH)
        (self.root / "sleep").write_text("#!/bin/sh\nexit 0\n")
        for name in ("gh", "sleep"):
            (self.root / name).chmod(0o755)

    def run_watch(self, **fixture):
        (self.root / "fixture.json").write_text(json.dumps(fixture))
        (self.root / "counts.json").write_text("{}")
        env = dict(os.environ, PATH=str(self.root) + os.pathsep + os.environ["PATH"],
                   WATCH_FIXTURE=str(self.root), REVIEW_AGENT_STATE_DIR=str(self.root / "state"))
        result = subprocess.run(["bash", str(WATCH), "42", "0"], env=env, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        lines = result.stdout.splitlines()
        self.assertEqual(lines[-1], "[watch] PR #42 closed — stopping")
        return lines[:-1]

    def test_green_start_and_restart_are_silent(self):
        fixture = dict(checks=[checks("pass")], lifecycle=["OPEN", "OPEN", "CLOSED"])
        self.assertEqual(self.run_watch(**fixture), [])
        self.assertEqual(self.run_watch(**fixture), [])

    def test_nonzero_failure_seed_is_valid_and_not_repeated(self):
        self.assertEqual(self.run_watch(checks=[checks("fail", 1)], lifecycle=["OPEN", "CLOSED"]), [])
        self.assertEqual(self.run_watch(checks=[checks("pass")], lifecycle=["OPEN", "OPEN", "CLOSED"]),
                         ["CHECK all 1 checks passed"])

    def test_changes_emit_once_including_after_a_restart_gap(self):
        self.assertEqual(self.run_watch(checks=[checks("pending", 8)], lifecycle=["OPEN", "CLOSED"]), [])
        self.assertEqual(self.run_watch(checks=[checks("fail", 1), checks("fail", 1), checks("pass")],
                                        lifecycle=["OPEN", "OPEN", "OPEN", "CLOSED"]),
                         ["CHECK build: fail https://example.test/build", "CHECK all 1 checks passed"])

    def test_initial_fetch_error_does_not_turn_baseline_into_an_event(self):
        self.assertEqual(self.run_watch(checks=[{"raw": "", "exit": 1}, checks("pass"), checks("pass")],
                                        lifecycle=["OPEN", "OPEN", "CLOSED"]), [])

    def test_comments_arriving_during_restart_gap_are_delivered(self):
        old = {"id": 1, "line": "COMMENT-HUMAN reviewer: Old comment"}
        new = {"id": 2, "line": "COMMENT-HUMAN reviewer: New blocker"}
        self.assertEqual(self.run_watch(checks=[checks("pass")], issues=[{"messages": [old]}],
                                        lifecycle=["OPEN", "CLOSED"]), [])
        self.assertEqual(self.run_watch(checks=[checks("pass")], issues=[{"messages": [old, new]}],
                                        lifecycle=["OPEN", "OPEN", "CLOSED"]), [new["line"]])

    def test_failed_comment_seed_retries_without_replaying_history(self):
        old = {"id": 1, "line": "COMMENT-HUMAN reviewer: Old comment"}
        new = {"id": 2, "line": "COMMENT-HUMAN reviewer: New blocker"}
        self.assertEqual(self.run_watch(checks=[checks("pass")],
                                        issues=[{"exit": 1}, {"messages": [old]}, {"messages": [old, new]}],
                                        lifecycle=["OPEN", "OPEN", "CLOSED"]), [new["line"]])


if __name__ == "__main__":
    unittest.main()

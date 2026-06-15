#!/usr/bin/env bash
# read-comment.sh — fetch the full body of a PR comment by URL.
#
# Each event line emitted by watch.sh ends with a comment/review URL. The body
# in the event line is truncated to 300 chars — when you need the full thing
# (a bot's detailed analysis, a reviewer's full rationale, etc.), pass the URL
# here. Handles:
#   - issue / PR-level comments  (.../#issuecomment-<id>)
#   - inline review comments     (.../#discussion_r<id>)
#   - review summaries           (.../#pullrequestreview-<id>)
#
# Usage: read-comment.sh <url>

set -uo pipefail

URL="${1:-}"
if [[ -z "$URL" ]]; then
  echo "usage: read-comment.sh <comment-url>" >&2
  exit 2
fi

if [[ ! "$URL" =~ ^https://github\.com/([^/]+)/([^/]+)/(pull|issues)/([0-9]+)#(.+)$ ]]; then
  echo "[read-comment] not a GitHub PR/issue comment URL: $URL" >&2
  exit 2
fi
owner="${BASH_REMATCH[1]}"
repo="${BASH_REMATCH[2]}"
pr="${BASH_REMATCH[4]}"
frag="${BASH_REMATCH[5]}"

case "$frag" in
  issuecomment-*)
    id="${frag#issuecomment-}"
    gh api "repos/$owner/$repo/issues/comments/$id" --jq .body
    ;;
  discussion_r*)
    id="${frag#discussion_r}"
    gh api "repos/$owner/$repo/pulls/comments/$id" --jq .body
    ;;
  pullrequestreview-*)
    id="${frag#pullrequestreview-}"
    gh api "repos/$owner/$repo/pulls/$pr/reviews/$id" --jq .body
    ;;
  *)
    echo "[read-comment] unrecognised URL fragment: #$frag" >&2
    exit 2
    ;;
esac

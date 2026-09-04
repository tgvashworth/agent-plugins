#!/usr/bin/env python3
"""Validate the portable skill and dual-host plugin packaging."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DIRS = (ROOT / "playbook-dev", ROOT / "utils")
ALLOWED_SKILL_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    # Claude extensions that Codex also accepts. Explicit-only behavior is
    # represented in agents/openai.yaml because Codex rejects
    # disable-model-invocation: true.
    "argument-hint",
    "model",
    "user-invocable",
    "version",
}
PROHIBITED_SKILL_TEXT = {
    "${CLAUDE_PLUGIN_ROOT}": "Claude-only plugin-root interpolation",
    "$ARGUMENTS": "Claude-only command arguments",
    "AskUserQuestion": "host-specific question tool",
    "TodoWrite": "host-specific progress tool",
    "Agent(": "host-specific worker call syntax",
    "Monitor(": "host-specific process call syntax",
}


def load_json(path: Path, errors: list[str]) -> dict[str, object] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{path.relative_to(ROOT)}: missing file")
        return None
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)}:{exc.lineno}: invalid JSON: {exc.msg}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)}: expected a JSON object")
        return None
    return value


def _plain_scalar(value: str, path: Path, line_number: int, errors: list[str]) -> str | None:
    """Validate the small YAML scalar subset used by skill frontmatter."""
    value = value.strip()
    if not value:
        return ""
    if value in {"null", "Null", "NULL", "~"}:
        return ""
    if value[0] in "[{&*!|>@`" or value.startswith(("- ", "? ", ": ")):
        errors.append(
            f"{path.relative_to(ROOT)}:{line_number}: unsupported YAML scalar syntax"
        )
        return None
    if value[0] in "'\"":
        quote = value[0]
        if len(value) < 2 or value[-1] != quote:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: unterminated quoted scalar"
            )
            return None
        return value[1:-1]
    if ": " in value:
        errors.append(
            f"{path.relative_to(ROOT)}:{line_number}: quote scalars containing ': '"
        )
        return None
    return value


def _nested_block(
    lines: list[str], path: Path, first_line: int, errors: list[str]
) -> bool:
    """Validate indented mappings and lists without pretending to parse all YAML."""
    valid = True
    for offset, line in enumerate(lines):
        if not line.strip():
            continue
        line_number = first_line + offset
        if "\t" in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: tabs are not valid indentation"
            )
            valid = False
            continue
        if not line.startswith("  "):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: nested YAML must be indented"
            )
            valid = False
            continue
        item = line.strip()
        if item == "-":
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: empty list item is unsupported"
            )
            valid = False
            continue
        is_list_item = item.startswith("- ")
        if is_list_item:
            item = item[2:].strip()
        mapping = re.match(r"^[A-Za-z][A-Za-z0-9_-]*:\s*(.*)$", item)
        if not is_list_item and not mapping:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: expected a nested mapping or list item"
            )
            valid = False
            continue
        value = mapping.group(1) if mapping else item
        if _plain_scalar(value, path, line_number, errors) is None:
            valid = False
    return valid


def _block_scalar(
    lines: list[str], path: Path, first_line: int, errors: list[str]
) -> str | None:
    """Validate indentation while treating block-scalar content as plain text."""
    for offset, line in enumerate(lines):
        if not line.strip():
            continue
        line_number = first_line + offset
        if "\t" in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: tabs are not valid indentation"
            )
            return None
        if not line.startswith("  "):
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: block scalar must be indented"
            )
            return None
    return "\n".join(part.strip() for part in lines).strip()


def frontmatter(text: str, path: Path, errors: list[str]) -> tuple[dict[str, str], str] | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: missing or malformed YAML frontmatter")
        return None

    lines = match.group(1).splitlines()
    fields: dict[str, str] = {}
    valid = True
    index = 0
    while index < len(lines):
        line = lines[index]
        line_number = index + 2
        if not line.strip():
            index += 1
            continue
        if "\t" in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: tabs are not valid indentation"
            )
            valid = False
            index += 1
            continue
        key_match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not key_match:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: unsupported YAML syntax"
            )
            valid = False
            index += 1
            continue

        key = key_match.group(1)
        if key in fields:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: duplicate frontmatter key {key!r}"
            )
            valid = False

        raw_value = (key_match.group(2) or "").strip()
        index += 1
        block_start = index
        while index < len(lines) and (not lines[index].strip() or lines[index][0].isspace()):
            index += 1
        block = lines[block_start:index]

        if raw_value in {"|", ">"}:
            if not block or not any(part.strip() for part in block):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number}: empty block scalar for {key!r}"
                )
                valid = False
                value = ""
            else:
                parsed_block = _block_scalar(block, path, block_start + 2, errors)
                if parsed_block is None:
                    valid = False
                    value = ""
                else:
                    value = parsed_block
        elif raw_value:
            if block:
                errors.append(
                    f"{path.relative_to(ROOT)}:{block_start + 2}: unexpected indented content"
                )
                valid = False
            parsed_scalar = _plain_scalar(raw_value, path, line_number, errors)
            if parsed_scalar is None:
                valid = False
                value = ""
            else:
                value = parsed_scalar
        elif block:
            if not _nested_block(block, path, block_start + 2, errors):
                valid = False
            value = "<nested>" if any(part.strip() for part in block) else ""
        else:
            value = ""

        fields[key] = value

    if not valid:
        return None
    return fields, text[match.end() :]


def check_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or "://" in target or target.startswith(("#", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link: {target}")


def check_skills(errors: list[str]) -> None:
    seen: dict[str, Path] = {}
    for plugin_dir in PLUGIN_DIRS:
        for path in sorted((plugin_dir / "skills").glob("*/SKILL.md")):
            text = path.read_text(encoding="utf-8")
            parsed = frontmatter(text, path, errors)
            if parsed is None:
                continue
            fields, body = parsed
            unknown = set(fields) - ALLOWED_SKILL_KEYS
            if unknown:
                errors.append(
                    f"{path.relative_to(ROOT)}: unsupported frontmatter: "
                    + ", ".join(sorted(unknown))
                )
            name = fields.get("name")
            if not name:
                errors.append(f"{path.relative_to(ROOT)}: missing name")
            elif name != path.parent.name:
                errors.append(
                    f"{path.relative_to(ROOT)}: name {name!r} does not match directory"
                )
            elif name in seen:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate skill name also used by "
                    f"{seen[name].relative_to(ROOT)}"
                )
            else:
                seen[name] = path
            if not fields.get("description"):
                errors.append(f"{path.relative_to(ROOT)}: missing or empty description")
            for token, reason in PROHIBITED_SKILL_TEXT.items():
                if token in body:
                    errors.append(f"{path.relative_to(ROOT)}: {reason}: {token}")
            for markdown_path in path.parent.rglob("*.md"):
                check_markdown_links(
                    markdown_path,
                    markdown_path.read_text(encoding="utf-8"),
                    errors,
                )


def check_plugins(errors: list[str]) -> None:
    for plugin_dir in PLUGIN_DIRS:
        claude_path = plugin_dir / ".claude-plugin" / "plugin.json"
        codex_path = plugin_dir / ".codex-plugin" / "plugin.json"
        claude = load_json(claude_path, errors)
        codex = load_json(codex_path, errors)
        if claude is None or codex is None:
            continue
        for key in ("name", "version", "description"):
            if not codex.get(key):
                errors.append(f"{codex_path.relative_to(ROOT)}: missing {key}")
        if claude.get("name") != codex.get("name"):
            errors.append(f"{plugin_dir.name}: Claude and Codex plugin names differ")
        if claude.get("version") != codex.get("version"):
            errors.append(f"{plugin_dir.name}: Claude and Codex plugin versions differ")
        if codex.get("skills") != "./skills/":
            errors.append(f"{codex_path.relative_to(ROOT)}: skills must be ./skills/")


def check_marketplace(errors: list[str]) -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    marketplace = load_json(path, errors)
    if marketplace is None:
        return
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        errors.append(f"{path.relative_to(ROOT)}: plugins must be an array")
        return
    expected = {"u", "playbook-dev"}
    found: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append(f"{path.relative_to(ROOT)}: plugin entry must be an object")
            continue
        name = entry.get("name")
        if isinstance(name, str):
            found.add(name)
        source = entry.get("source")
        source_path = source.get("path") if isinstance(source, dict) else None
        if not isinstance(source_path, str) or not (ROOT / source_path).is_dir():
            errors.append(f"{path.relative_to(ROOT)}: invalid source for {name!r}")
        policy = entry.get("policy")
        if not isinstance(policy, dict) or not {
            "installation",
            "authentication",
        }.issubset(policy):
            errors.append(f"{path.relative_to(ROOT)}: incomplete policy for {name!r}")
        if not entry.get("category"):
            errors.append(f"{path.relative_to(ROOT)}: missing category for {name!r}")
    if found != expected:
        errors.append(
            f"{path.relative_to(ROOT)}: expected plugins {sorted(expected)}, got {sorted(found)}"
        )


def check_shell_scripts(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("**/*.sh")):
        result = subprocess.run(
            ["bash", "-n", str(path)], capture_output=True, text=True, check=False
        )
        if result.returncode:
            errors.append(
                f"{path.relative_to(ROOT)}: bash syntax error: {result.stderr.strip()}"
            )


def main() -> int:
    errors: list[str] = []
    check_skills(errors)
    check_plugins(errors)
    check_marketplace(errors)
    check_shell_scripts(errors)
    for path in ROOT.glob("**/.DS_Store"):
        errors.append(f"{path.relative_to(ROOT)}: remove generated macOS metadata")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill_count = sum(1 for plugin in PLUGIN_DIRS for _ in (plugin / "skills").glob("*/SKILL.md"))
    print(f"Validation passed: {skill_count} skills and {len(PLUGIN_DIRS)} plugins")
    return 0


if __name__ == "__main__":
    sys.exit(main())

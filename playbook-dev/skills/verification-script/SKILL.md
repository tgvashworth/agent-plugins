---
name: verification-script
description: This skill should be used when the user asks to "create verification script", "build completion checker", "generate validation script", "check stage completion", "verify output files", or needs scripts to validate playbook outputs.
version: 0.1.0
---

# Verification Script

Generate scripts that check file existence, size thresholds, and completion status.

## Purpose of Verification Scripts

Verification scripts provide automated checks for:
- Stage completion status
- Output file existence
- Content size thresholds
- Format validation

## Script Types

### Completion Checker

Check if all expected outputs exist:

```bash
#!/bin/bash
# verify-stage1.sh - Check Stage 1 completion

set -e

ITEMS_DIR="${1:-.}"
REQUIRED_FILES=("diagnosis.md" "evidence-assessment.md" "capability-gaps.md")

total=0
complete=0
incomplete=()

for item_dir in "$ITEMS_DIR"/*/; do
    if [ -d "$item_dir" ]; then
        ((total++))
        all_present=true

        for file in "${REQUIRED_FILES[@]}"; do
            if [ ! -f "$item_dir/analysis/$file" ]; then
                all_present=false
                break
            fi
        done

        if [ "$all_present" = true ]; then
            ((complete++))
        else
            incomplete+=("$(basename "$item_dir")")
        fi
    fi
done

echo "Completion: $complete / $total ($(( complete * 100 / total ))%)"

if [ ${#incomplete[@]} -gt 0 ]; then
    echo "Incomplete items:"
    printf '  - %s\n' "${incomplete[@]}"
    exit 1
fi

exit 0
```

### Size Threshold Checker

Verify files are non-trivial:

```bash
#!/bin/bash
# verify-sizes.sh - Check file sizes

MIN_SIZE=500  # bytes

for file in "$@"; do
    if [ -f "$file" ]; then
        size=$(wc -c < "$file")
        if [ "$size" -lt "$MIN_SIZE" ]; then
            echo "WARN: $file is only $size bytes (min: $MIN_SIZE)"
        fi
    else
        echo "MISSING: $file"
    fi
done
```

### Progress Reporter

Show completion status in simple format:

```bash
#!/bin/bash
# verify-progress.sh - Show progress

ITEMS_DIR="${1:-.}"

echo "Stage 1 Progress:"
echo "================"

for item_dir in "$ITEMS_DIR"/*/; do
    name=$(basename "$item_dir")
    if [ -d "$item_dir/analysis" ] && [ "$(ls -A "$item_dir/analysis" 2>/dev/null)" ]; then
        echo "[DONE] $name"
    else
        echo "[TODO] $name"
    fi
done
```

## Script Structure

### Standard Script Template

```bash
#!/bin/bash
# Script: {name}
# Purpose: {description}
# Usage: {how to run}

set -e  # Exit on error

# Configuration
MIN_SIZE=500
REQUIRED_FILES=("file1.md" "file2.md")

# Functions
check_file() {
    local file="$1"
    if [ ! -f "$file" ]; then
        return 1
    fi
    local size=$(wc -c < "$file")
    [ "$size" -ge "$MIN_SIZE" ]
}

# Main logic
main() {
    local target="${1:-.}"
    local errors=0

    # Perform checks
    # ...

    # Report results
    if [ "$errors" -gt 0 ]; then
        echo "FAILED: $errors errors found"
        exit 1
    else
        echo "PASSED: All checks successful"
        exit 0
    fi
}

main "$@"
```

## Check Types

### File Existence

```bash
check_exists() {
    local file="$1"
    if [ -f "$file" ]; then
        echo "OK: $file exists"
        return 0
    else
        echo "MISSING: $file"
        return 1
    fi
}
```

### Directory Structure

```bash
check_structure() {
    local base="$1"
    local required_dirs=("stages" "templates" "reference")

    for dir in "${required_dirs[@]}"; do
        if [ ! -d "$base/$dir" ]; then
            echo "MISSING DIR: $base/$dir"
            return 1
        fi
    done
    return 0
}
```

### Content Size

```bash
check_size() {
    local file="$1"
    local min_size="${2:-500}"

    if [ ! -f "$file" ]; then
        return 1
    fi

    local size=$(wc -c < "$file")
    if [ "$size" -ge "$min_size" ]; then
        return 0
    else
        echo "TOO SMALL: $file ($size bytes, min: $min_size)"
        return 1
    fi
}
```

### Content Validation

```bash
check_content() {
    local file="$1"
    local pattern="$2"

    if grep -q "$pattern" "$file" 2>/dev/null; then
        return 0
    else
        echo "MISSING CONTENT: $pattern in $file"
        return 1
    fi
}
```

## Output Formats

### Detailed Report

```bash
echo "=== Verification Report ==="
echo "Date: $(date)"
echo "Target: $TARGET"
echo ""
echo "Results:"
echo "  Total items: $total"
echo "  Complete: $complete"
echo "  Incomplete: $incomplete"
echo "  Completion: $(( complete * 100 / total ))%"
echo ""
if [ ${#errors[@]} -gt 0 ]; then
    echo "Issues:"
    for error in "${errors[@]}"; do
        echo "  - $error"
    done
fi
```

### Progress Format

```bash
echo "Stage 1: [DONE] 45/50 (90%)"
echo "Stage 2: [TODO] 0/1"
echo "Stage 3: [----] Not started"
```

### Machine-Readable

```bash
# JSON output
echo "{\"stage\": 1, \"total\": $total, \"complete\": $complete, \"percent\": $(( complete * 100 / total ))}"
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Complete (100%) or substantially complete (≥95%) |
| 1 | Incomplete (<95%) |
| 2 | Critical error (missing required files) |

## Integration with Playbook

### Verification Points

Call verification scripts at key points:

```markdown
## Stage Transitions

### After Stage 1
```bash
./bin/verify-stage1 items/
```

### After Stage 2
```bash
./bin/verify-stage2 cohort-analysis/
```

### Before Stage 4
```bash
./bin/verify-all
```
```

### Automated Retry

```bash
# Retry incomplete items
incomplete=$(./bin/verify-stage1 items/ --list-incomplete)
for item in $incomplete; do
    # Re-launch analysis for item
done
```

## Script Locations

Place verification scripts in:

```
playbook/
└── bin/
    ├── verify-stage1.sh
    ├── verify-stage2.sh
    ├── verify-all.sh
    └── verify-progress.sh
```

Or at analysis root:

```
analysis/
├── bin/
│   └── verify-analysis.sh
└── playbook/
```

## Validation Checklist

Before finalizing script:

- [ ] Checks all required files
- [ ] Validates size thresholds
- [ ] Has clear output format
- [ ] Uses appropriate exit codes
- [ ] Handles edge cases (empty dirs, missing files)
- [ ] Is documented with usage instructions

## Additional Resources

For verification patterns:
- **`${CLAUDE_PLUGIN_ROOT}/references/playbook-pattern.md`** - Section 4.13

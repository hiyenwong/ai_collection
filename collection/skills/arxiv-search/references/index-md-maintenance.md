# INDEX.md Maintenance Guide

The file `~/ai_github/ai_collection/INDEX.md` is a sequential log of research entries prepended by cron jobs. It has accumulated structural quirks.

## Line-Number Prefix Formatting

INDEX.md entries use a **line-number prefix format** where each line starts with `     N|` (space-padded line number + pipe). This is a historical artifact from repeated prepend operations where content was inserted at the top with prepended counters.

Example:
```
    60|  - **Activation**: untrained CNN V1 alignment
    61|
    62|### Riemannian geometry meets fMRI (arXiv:2605.22334)
    63|- [[skill-name]] - Description...
```

## Inserting New Entries

**DO NOT use `sed`** to insert entries — the line-number prefixes and special characters (parentheses, single quotes in names like "Parkinson's", pipe characters) cause shell escaping failures.

**Use Python `readlines`/`writelines` instead** — this is the most reliable approach:

```python
# Read the file
with open('/path/to/INDEX.md', 'r') as f:
    lines = f.readlines()

# Find insertion point by line content
insert_idx = -1
for i, line in enumerate(lines):
    if 'target anchor string' in line:
        insert_idx = i
        break

# New lines must match the line-number prefix format
new_lines = [
    '    32|\n',  # blank separator
    '    33|### Paper Title (arXiv:2605.XXXXX)\n',
    '    34|- [[skill-name]] - Description...\n',
    # ...
    '    39|  - **Activation**: keyword1, keyword2\n',
]

# Insert after the anchor
result = lines[:insert_idx+1] + new_lines + lines[insert_idx+1:]

# Write back
with open('/path/to/INDEX.md', 'w') as f:
    f.writelines(result)
```

## Finding the Correct Insertion Point

Use `grep -n` to find the exact line number before inserting:

```bash
grep -n "activation anchor phrase" ~/ai_github/ai_collection/INDEX.md
```

The line number output tells you where to insert. The line numbers in the file may NOT match the prefix numbers — trust `grep -n` output over the prefix counts.

## Index Structure

The file is organized top-to-bottom most-recent-first:
- Entries at the TOP are from the current day
- Older entries scroll down (older days) or stay at bottom
- Each date has a `## YYYY-MM-DD - Topic (Cron Job)` heading
- Subsections for individual papers use `### Title (arXiv:ID)`
- Entries use `- [[skill-name]] - Description...` format with bullet points

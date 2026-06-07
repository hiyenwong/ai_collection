## INDEX.md Multi-Section Insertion Pitfall

INDEX.md accumulates multiple same-date sections from repeated cron runs (e.g., multiple `## 2026-05-24` sections). **Do NOT** simply append to the end or use `cat >> INDEX.md` — this buries entries and creates duplicates.

### Correct Insertion Strategy

```python
with open('INDEX.md', 'r') as f:
    lines = f.read().split('\n')

# Find the FIRST line that starts a DIFFERENT date (i.e., not today)
today_prefix = '## 2026-05-24'  # adjust for current date
insert_pos = None
for i, line in enumerate(lines):
    if line.startswith('## ') and today_prefix not in line:
        insert_pos = i
        break

if insert_pos is None:
    # No older date found — append at end
    insert_pos = len(lines)

# Insert before insert_pos
new_lines = lines[:insert_pos] + new_entries.split('\n') + lines[insert_pos:]
```

This ensures today's entries always sit at the top (chronologically newest), grouped with other same-date sections, never buried at the bottom.

### Same-Day Multi-Run Edge Case

When **all** section headers share today's date (common with repeated hourly cron runs), the "find first different date" strategy falls through to "append at end" — creating a duplicate same-date section. This is correct behavior (the file already starts with today's sections) but means entries may appear as a separate `## YYYY-MM-DD - Topic (Cron Job)` section at the bottom.

To mitigate: after insertion, the INDEX.md should be read back and any same-date sections with the **same topic** should be merged. This is a known limitation; the background curator consolidates these at scale. For now, prefer appending a new section rather than trying to find-and-inject into an existing same-date section (risk of format corruption is higher than the cost of a duplicate section header).

### Duplicate Prevention

Before inserting, grep for the arXiv IDs in the new entries:
```python
existing = open('INDEX.md', 'r').read()
for entry in new_entries_list:
    if entry['arxiv_id'] in existing:
        print(f'Skip duplicate: {entry["arxiv_id"]}')
        continue
```

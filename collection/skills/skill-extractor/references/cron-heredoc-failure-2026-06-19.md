# Cron Job Operational Patterns - 2026-06-19 Update

## Heredoc Append Failure in Cron Mode (CONFIRMED 2026-06-19)

**Failure pattern**: `cat >> file << 'MARKER'` heredoc appends fail with:
- Exit code: -1
- Error: "Foreground command uses '&' backgrounding. Use terminal(background=true) for long-lived processes..."
- This occurs even for simple text appends that shouldn't trigger background detection

**Root cause**: The `<<` heredoc syntax in terminal foreground mode triggers the background process detection heuristic, causing the command to be rejected.

**Reliable alternatives** (confirmed working):

### Python file append (RECOMMENDED)
```python
python3 -c "
with open('/path/to/file.md', 'a') as f:
    f.write('New content here\n')
print('Done')
"
```

### Why this matters
INDEX.md updates and daily report writes commonly use heredoc appends in bash scripts. In cron mode, these silently fail. Python's `open(path, 'a')` is the reliable pattern for all file append operations.

## Previous Patterns (from cron-kg-ops-update-2026-06-17.md)

- `kg_tool import-paper` ✅
- `kg_tool pagerank` ✅
- `kg_tool communities` ✅
- `kg_tool search` ✅
- `kg_tool generate-embeddings` ❌ (persistent datatype mismatch)
- Duplicate prevention via `grep` for arXiv ID before skill creation
- Saturated domain rule: >70% saturation → enhance existing skills, don't create new ones
- Python string split-and-insert for INDEX.md (not heredoc append, not patch mode)

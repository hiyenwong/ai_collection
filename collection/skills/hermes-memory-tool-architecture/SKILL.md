---
name: hermes-memory-tool-architecture
description: "Hermes Agent memory tool architecture reference — complete design patterns for TypeScript replication. Covers frozen snapshot injection, atomic file writes, security scanning, file locking, flush lifecycle, and dual-store (memory/user) design."
triggers:
  - memory tool
  - persistent memory
  - frozen snapshot
  - memory architecture
  - memory store design
---

# Hermes Memory Tool Architecture

Source: `hermes-agent/tools/memory_tool.py` (584 lines)

## Core Architecture

```
System Prompt (frozen at session start)
  ├── MEMORY block (agent notes, 2200 char limit)
  └── USER block (user profile, 1375 char limit)
        ↕ tool calls during session
MemoryStore (live state, mutable)
  ├── add / replace / remove actions
  ├── Security scanning (injection + invisible chars)
  ├── File locking (cross-process safety)
  └── Atomic writes (tmp + fsync + rename)
        ↕ file I/O
~/.hermes/memories/MEMORY.md
~/.hermes/memories/USER.md
```

## Key Constants

- `MEMORY_CHAR_LIMIT = 2200` — agent notes limit
- `USER_CHAR_LIMIT = 1375` — user profile limit
- `ENTRY_DELIMITER = "\n§\n"` — separator between entries
- `MEMORY_NUDGE_INTERVAL = 10` — turns between nudge reminders
- `MEMORY_FLUSH_MIN_TURNS = 6` — min turns before session-end flush

## Design Pattern: Frozen Snapshot

`load_from_disk()` reads files, deduplicates, then **freezes** the rendered block in `_system_prompt_snapshot`. Mid-session writes DO NOT update this snapshot. This keeps the system prompt stable across all turns, preserving prefix cache.

```python
# In __init__:
self._system_prompt_snapshot = {}

# In load_from_disk():
self._system_prompt_snapshot = {
    "memory": self._render_block("memory", self.memory_entries),
    "user":   self._render_block("user",   self.user_entries),
}

# In format_for_system_prompt():
def format_for_system_prompt(self, target: str) -> Optional[str]:
    block = self._system_prompt_snapshot.get(target, "")
    return block if block else None
```

## Design Pattern: Atomic Writes

Never use direct `open("w")` — it truncates before lock acquisition, creating a race window where concurrent readers see an empty file.

```python
def _write_file(path, entries):
    content = ENTRY_DELIMITER.join(entries) if entries else ""
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp", prefix=".mem_")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, str(path))  # atomic on same filesystem
```

## Design Pattern: File Locking

Cross-process safety via `fcntl.flock(LOCK_EX)` (Unix) / `msvcrt.locking(LK_LOCK)` (Windows). Lock file is `{target}.md.lock`.

```python
@contextmanager
def _file_lock(self, path):
    lock_path = str(path) + ".lock"
    # Unix: fcntl.flock(fd, fcntl.LOCK_EX)
    # Windows: msvcrt.locking(fd, msvcrt.LK_LOCK, ...)
```

## Design Pattern: Security Scanning

Two-phase scan before accepting any content:

1. **Invisible character detection** — 10 Unicode chars (U+200B/C/D, U+2060, U+FEFF, U+202A-E)
2. **Threat pattern matching** — 12 regex patterns:
   - prompt_injection, role_hijack, deception_hide, sys_prompt_override
   - disregard_rules, bypass_restrictions
   - exfil_curl, exfil_wget, read_secrets
   - ssh_backdoor, ssh_access, hermes_env

## Design Pattern: Flush on Session End

Triggered when `_memory_flush_min_turns != 0`, memory tool exists, user turns >= threshold, messages >= 3.

1. Constructs a synthetic user message: `"[System: The session is being compressed. Save anything worth remembering...]"`
2. Sends only the `MEMORY_SCHEMA` tool to an auxiliary LLM client (temperature 0.3)
3. Uses a sentinel ID (`__flush_{id}_{monotonic}`) to identify and clean up flush messages
4. Failures are silently handled

## System Prompt Injection

In `run_agent.py` (lines 4128-4140):
```python
if self._memory_enabled:
    block = self.memory_store.format_for_system_prompt("memory")
    if block:
        prompt_parts.append(block)
if self._user_profile_enabled:
    block = self.memory_store.format_for_system_prompt("user")
    if block:
        prompt_parts.append(block)
```

## Render Block Format (for system prompt display)

```
════════════════════════════════════════════════
MEMORY (your personal notes) [99% — 2,195/2,200 chars]
════════════════════════════════════════════════
entry1 text
§
entry2 text
§
entry3 text
```

Note: Header/separator only in system prompt rendering. File storage is pure §-delimited entries.

## Tool Schema (MEMORY_SCHEMA)

- **name**: `"memory"`
- **actions**: add, replace, remove
- **targets**: `"memory"` (agent notes), `"user"` (user profile)
- **parameters**: action (required), target (required), content (for add/replace), old_text (for replace/remove)
- **old_text matching**: fuzzy substring match; rejects if multiple distinct entries match

## Key Design Rationale

| Decision | Why |
|----------|-----|
| Frozen snapshot | Stable system prompt → prefix cache works |
| Atomic write | Concurrent readers never see partial state |
| File lock | Multi-session concurrent writes (multiple agents) |
| § delimiter | Lightweight vs JSON/YAML parsing |
| Security scan | Prevent prompt injection via persisted memory |
| Char limits | Prevent memory bloat consuming context window |
| Flush lifecycle | Rescue important info before context compression |
| Fuzzy old_text | LLMs can't always produce exact matches |
| Multi-match rejection | Prevent accidental modification of wrong entry |

## TypeScript Porting Notes

- **File locking**: Node.js has no built-in flock. Use `proper-lockfile` or `fs-ext`
- **Atomic rename**: `fs.renameSync()` is atomic on same filesystem (POSIX)
- **fsync**: `fs.fsyncSync(fd)` after write
- **Encoding**: UTF-8 throughout
- **The rest**: Direct 1:1 translation possible

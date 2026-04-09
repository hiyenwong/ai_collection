---
name: codex-session-manager
description: 'Monitor and manage OpenAI Codex CLI sessions. List history, view session content, resume via ACP, track statistics. Use when user asks about Codex sessions, wants to check progress, or resume previous work.'
metadata:
  {
    "openclaw":
      {
        "emoji": "📜",
        "requires": { "anyBins": ["codex"] },
      },
  }
---

# Codex Session Manager

Manage OpenAI Codex CLI sessions from OpenClaw.

## Session Storage

Codex sessions are stored in `~/.codex/sessions/`:

```
~/.codex/sessions/
└── 2026/
    └── 04/
        ├── 04/
        │   └── rollout-2026-04-04T22-43-49-xxx.jsonl
        ├── 05/
        │   └── rollout-2026-04-05T08-31-04-xxx.jsonl
        └── ...
```

Each `.jsonl` file contains the full transcript of a Codex session.

## Commands

### List Sessions

```bash
# List all sessions (latest first)
find ~/.codex/sessions -type f -name "*.jsonl" | sort -r | head -20

# List sessions from specific date
find ~/.codex/sessions/2026/04/09 -type f -name "*.jsonl"
```

### View Session Summary

```bash
# Quick summary: count messages, extract key info
python3 << 'EOF'
import json
session_file = "/path/to/session.jsonl"
messages = []
with open(session_file) as f:
    for line in f:
        msg = json.loads(line)
        messages.append(msg)

print(f"Session: {session_file.split('/')[-1]}")
print(f"Total messages: {len(messages)}")
print(f"Messages breakdown:")
for msg in messages[:5]:
    role = msg.get('role', 'unknown')
    content_preview = str(msg.get('content', ''))[:100]
    print(f"  [{role}] {content_preview}...")
EOF
```

### Session Statistics

```bash
# Aggregate stats across all sessions
python3 << 'EOF'
import json
import os
from pathlib import Path
from datetime import datetime

sessions_dir = Path.home() / ".codex" / "sessions"
stats = {
    'total': 0,
    'by_date': {},
    'avg_messages': 0,
    'message_counts': []
}

for jsonl in sessions_dir.rglob("*.jsonl"):
    try:
        with open(jsonl) as f:
            count = sum(1 for _ in f)
        stats['total'] += 1
        stats['message_counts'].append(count)
        
        # Extract date from filename
        filename = jsonl.name
        date_str = filename.split('T')[0].replace('rollout-', '')
        stats['by_date'][date_str] = stats['by_date'].get(date_str, 0) + 1
    except:
        pass

if stats['message_counts']:
    stats['avg_messages'] = sum(stats['message_counts']) / len(stats['message_counts'])

print(f"Total sessions: {stats['total']}")
print(f"Average messages: {stats['avg_messages']:.1f}")
print(f"Sessions by date:")
for date, count in sorted(stats['by_date'].items(), reverse=True)[:10]:
    print(f"  {date}: {count} sessions")
EOF
```

### Find Session by Content

```bash
# Search sessions for specific content
grep -r "your keyword" ~/.codex/sessions/*.jsonl | head -10
```

## Resume Session via ACP

Use `sessions_spawn` with `resumeSessionId` to continue a Codex session:

```json
{
  "runtime": "acp",
  "agentId": "codex",
  "resumeSessionId": "<session-uuid-from-jsonl>",
  "task": "Continue from where we left off..."
}
```

### Extract Session UUID

```bash
# Get session ID from first message
python3 << 'EOF'
import json
session_file = "/path/to/session.jsonl"
with open(session_file) as f:
    first_msg = json.loads(f.readline())
    session_id = first_msg.get('session_id', 'unknown')
    print(f"Session UUID: {session_id}")
EOF
```

## Integration with OpenClaw

### From Chat Command

When user asks:
- "show me Codex sessions" → list sessions
- "what was in session X" → view summary
- "resume Codex session" → ACP spawn with resumeSessionId
- "Codex statistics" → aggregate stats

### ACP Resume Pattern

```python
# Step 1: Find session
sessions = find_codex_sessions(date="2026-04-09")

# Step 2: Extract UUID
session_id = extract_session_uuid(sessions[0])

# Step 3: Resume via ACP
sessions_spawn(
    runtime="acp",
    agentId="codex",
    resumeSessionId=session_id,
    task="Continue the previous task"
)
```

## Session JSONL Format

Each line is a JSON object:

```json
{
  "role": "user|assistant|system",
  "content": "...",
  "session_id": "uuid",
  "timestamp": "ISO8601",
  "tool_calls": [...],  // if any
  "tool_results": [...]  // if any
}
```

## Monitoring Running Sessions

Check if Codex is currently running:

```bash
# Check running Codex processes
ps aux | grep codex | grep -v grep

# Check via process tool
process action:list
```

## Workflow

1. **List** → Find relevant session
2. **View** → Understand what happened
3. **Resume** → Continue work via ACP
4. **Monitor** → Track progress with process tool

---

*Related: coding-agent skill, acp-router skill*
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

Codex uses a structured event format:

```json
{
  "timestamp": "2026-04-07T14:14:09.273Z",
  "type": "session_meta|event_msg|response_item",
  "payload": {
    // type-specific content
  }
}
```

### Event Types

| Type | Description | Key Payload Fields |
|------|-------------|---------------------|
| `session_meta` | Session initialization | `id` (session UUID), `cwd`, `cli_version`, `model_provider`, `git.branch`, `git.commit_hash` |
| `event_msg` | Events like task_started | `type` (event type), `turn_id` |
| `response_item` | Messages | `type` ("message"), `role` ("developer"|"user"|"assistant"), `content` (array of input_text) |

### Extract Session Info

```python
import json
from pathlib import Path

def parse_codex_session(jsonl_path):
    """Parse Codex session and extract key info."""
    with open(jsonl_path) as f:
        lines = [json.loads(line) for line in f]
    
    # Find session_meta
    meta = next((l for l in lines if l.get('type') == 'session_meta'), None)
    
    # Find all response_items
    messages = [l for l in lines if l.get('type') == 'response_item']
    
    # Count by role
    roles = {}
    for msg in messages:
        role = msg.get('payload', {}).get('role', 'unknown')
        roles[role] = roles.get(role, 0) + 1
    
    return {
        'session_id': meta.get('payload', {}).get('id', 'unknown') if meta else 'unknown',
        'cwd': meta.get('payload', {}).get('cwd', 'unknown') if meta else 'unknown',
        'branch': meta.get('payload', {}).get('git', {}).get('branch', 'unknown') if meta else 'unknown',
        'cli_version': meta.get('payload', {}).get('cli_version', 'unknown') if meta else 'unknown',
        'total_events': len(lines),
        'message_count': len(messages),
        'roles': roles,
        'filename': jsonl_path.name,
        'date': jsonl_path.name.split('T')[0].replace('rollout-', ''),
        'time': jsonl_path.name.split('T')[1].split('-')[0] if 'T' in jsonl_path.name else ''
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

## Activation Keywords

- codex session
- openai codex
- codex manager
- codex CLI
- session monitor

## Tools Used

- exec
- read
- write

## Instructions for Agents

Use this skill to manage and monitor OpenAI Codex CLI sessions. Read session logs in JSONL format, track session state, and provide status summaries.

## Examples

User: Help me with Codex Session Manager
Agent: [Activates codex-session-manager skill and follows the instructions above]

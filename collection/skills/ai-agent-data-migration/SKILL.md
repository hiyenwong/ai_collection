---
name: ai-agent-data-migration
description: Systematic migration of data between AI agent systems (e.g., OpenClaw to Hermes, profile migration, backup/restore). Use when migrating memories, skills, configurations, cron jobs, or other agent state between systems.
triggers:
  - "migrate from"
  - "migration"
  - "import from"
  - "export to"
  - "backup agent"
  - "restore agent"
  - "move to hermes"
  - "transfer data"
---

# AI Agent Data Migration

Systematic approach for migrating data between AI agent systems or creating backup/restore workflows.

## Migration Workflow

### Phase 1: Discovery & Inventory

1. **Identify source system structure**
   ```bash
   # Find all relevant directories
   find ~/.source-agent -type d -maxdepth 2 | head -30
   
   # List configuration files
   ls -la ~/.source-agent/
   ```

2. **Catalog data categories**
   - **Memories**: Daily notes, long-term memory files
   - **Skills**: Custom skills and their metadata
   - **Configurations**: Agent personality, user preferences, tool settings
   - **Scheduled Tasks**: Cron jobs, heartbeats, recurring tasks
   - **State**: Session data, caches, authentication
   - **Projects**: Workspace directories, code, documents

3. **Check target system compatibility**
   - Verify target system directory structure
   - Identify mapping between source and target formats
   - Note any incompatibilities or required transformations

### Phase 2: Migration Planning

Create a todo list for the migration:

```python
# Example migration tasks
tasks = [
    {"id": "1", "content": "Migrate memory files", "status": "pending"},
    {"id": "2", "content": "Migrate skills with categorization", "status": "pending"},
    {"id": "3", "content": "Recreate cron jobs in target system", "status": "pending"},
    {"id": "4", "content": "Migrate agent configurations", "status": "pending"},
    {"id": "5", "content": "Migrate additional state/data", "status": "pending"},
    {"id": "6", "content": "Verify migration completeness", "status": "pending"}
]
```

### Phase 3: Execute Migration

#### Memory Files
```python
import shutil
import os

# Migrate memory files
source_memories = os.path.expanduser("~/.source-agent/memories")
target_memories = os.path.expanduser("~/.target-agent/memories")

os.makedirs(target_memories, exist_ok=True)

for filename in os.listdir(source_memories):
    if filename.endswith('.md'):
        src = os.path.join(source_memories, filename)
        dst = os.path.join(target_memories, filename)
        
        # Backup if exists
        if os.path.exists(dst):
            shutil.copy2(dst, dst + '.backup')
        
        shutil.copy2(src, dst)
```

#### Skills
```python
# Migrate skills with proper categorization
source_skills = os.path.expanduser("~/.source-agent/skills")
target_skills = os.path.expanduser("~/.target-agent/skills")

for skill_name in os.listdir(source_skills):
    skill_path = os.path.join(source_skills, skill_name)
    if os.path.isdir(skill_path):
        # Determine category from skill content or name
        category = infer_category(skill_name, skill_path)
        
        target_path = os.path.join(target_skills, category, skill_name)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # Backup existing
        if os.path.exists(target_path):
            shutil.move(target_path, target_path + '_backup')
        
        shutil.copytree(skill_path, target_path)
```

#### Cron Jobs
```python
# For Hermes target, use cronjob tool
# For other systems, use appropriate API

# Example: Recreate cron job in Hermes
cronjob(
    action="create",
    name="task-name",
    schedule="0 22 * * *",
    prompt="Task description and instructions",
    deliver="origin"
)
```

#### Configurations
```python
# Migrate agent configuration files
config_files = ['SOUL.md', 'AGENTS.md', 'USER.md', 'TOOLS.md']

for config in config_files:
    src = os.path.join(source_dir, config)
    if os.path.exists(src):
        # Save with prefix to avoid conflicts
        dst = os.path.join(target_memories, f'source_{config.lower()}')
        shutil.copy2(src, dst)
```

### Phase 4: Verification

```python
def verify_migration():
    checks = []
    
    # Check memories
    memory_count = len([f for f in os.listdir(target_memories) if f.endswith('.md')])
    checks.append(("Memories", memory_count >= expected_count))
    
    # Check skills
    skill_count = count_skills(target_skills)
    checks.append(("Skills", skill_count >= expected_skill_count))
    
    # Check cron jobs
    cron_jobs = cronjob(action="list")
    checks.append(("Cron jobs", len(cron_jobs.get('jobs', [])) >= expected_cron_count))
    
    # Report
    for name, passed in checks:
        status = "✅" if passed else "❌"
        print(f"{status} {name}")
    
    return all(passed for _, passed in checks)
```

### Phase 5: Documentation

Generate a migration report:

```python
manifest = {
    "migration_date": datetime.now().isoformat(),
    "source": "SourceSystem",
    "target": "TargetSystem",
    "migrated_items": {
        "memory_files": count,
        "skills": count,
        "cron_jobs": count,
        "config_files": count
    },
    "manual_steps_required": [
        "Merge SOUL.md files",
        "Reconfigure API credentials",
        "Verify model settings"
    ]
}
```

## Common Migration Scenarios

### OpenClaw → Hermes

| OpenClaw Path | Hermes Path | Notes |
|--------------|-------------|-------|
| `~/.openclaw/workspace/memory/` | `~/.hermes/memories/` | Direct copy |
| `~/.openclaw/workspace/skills/` | `~/.hermes/skills/openclaw-imports/` | Create category |
| `~/.openclaw/cron/jobs.json` | Use `cronjob` tool | Recreate jobs |
| `~/.openclaw/workspace/SOUL.md` | `~/.hermes/SOUL.md` | Manual merge |

### Profile Migration (Hermes)

```bash
# Export profile
hermes profile export <profile-name>

# Import to new system
hermes profile import <backup-file>
```

### Backup/Restore Workflow

```bash
# Create timestamped backup
backup_dir="~/.hermes/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p $backup_dir
cp -r ~/.hermes/memories $backup_dir/
cp -r ~/.hermes/skills $backup_dir/
cp ~/.hermes/config.yaml $backup_dir/
```

## Best Practices

1. **Always backup before migrating** - Keep original data until verified
2. **Migrate incrementally** - Do one category at a time
3. **Verify after each phase** - Don't proceed until current phase is confirmed
4. **Document manual steps** - Some things can't be automated (API keys, OAuth)
5. **Test functionality** - After migration, test that skills and tasks work
6. **Keep migration log** - Save manifest for future reference

## Pitfalls to Avoid

- **Don't overwrite without backup** - Always backup existing target files
- **Don't migrate credentials** - Reconfigure auth manually for security
- **Don't assume compatibility** - Check format differences between systems
- **Don't forget verification** - Untested migration is incomplete
- **Don't delete source until confirmed** - Keep backup until everything works

## When to Use This Skill

- Migrating from OpenClaw, Claude Desktop, or other AI agent systems to Hermes
- Moving between Hermes profiles
- Creating comprehensive backups
- Restoring from backups
- Consolidating multiple agent workspaces

## Activation Keywords

- "ai-agent-data-migration"
- "ai agent data migration"
- "use ai agent data migration"
- "ai agent data migration help"
- "ai agent data migration tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Ai Agent Data Migration usage
```
User: "Help me with ai agent data migration"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed ai agent data migration assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```

# INDEX.md Integrity Check Pattern

**Discovered**: 2026-06-02 (Tuesday cron job)

## The Gap

Skills can exist in `ai_collection/collection/skills/{name}/` with valid SKILL.md and kg.db entries, yet have **no INDEX.md entry**. This creates a silent orphaning problem where the skill is functionally usable but invisible in the knowledge index.

**Confirmed case**: `quantum-control-pulse-software` (arXiv:2605.21286)
- ✅ SKILL.md exists in ai_collection
- ✅ Entity indexed in kg.db  
- ❌ Missing from INDEX.md entirely

## Three-Way Sync Requirement

When a skill is created or discovered, these three locations must ALL be in sync:

| Location | Purpose | Check Command |
|----------|---------|---------------|
| `~/.hermes/skills/ai_collection/{name}/SKILL.md` | Hermes runtime | `ls ~/.hermes/skills/ai_collection/{name}/SKILL.md` |
| `~/ai_github/ai_collection/collection/skills/{name}/SKILL.md` | Git project copy | `ls ~/ai_github/ai_collection/collection/skills/{name}/SKILL.md` |
| `~/ai_github/ai_collection/INDEX.md` | Knowledge index | `grep "{name}" ~/ai_github/ai_collection/INDEX.md` |

## Fix Pattern

### Step 1: Identify missing INDEX.md entries

```bash
# For each skill in ai_collection, check INDEX.md
for skill in ~/ai_github/ai_collection/collection/skills/*/; do
  name=$(basename "$skill")
  if ! grep -q "$name" ~/ai_github/ai_collection/INDEX.md; then
    echo "MISSING: $name"
  fi
done
```

### Step 2: Add structured entry to INDEX.md

Format for each entry:
```markdown
### {Paper Topic Title}
- [[{skill-name}]] - One-sentence description (arXiv: {id})
  - Key point 1
  - Key point 2
  - **Activation**: keyword1, keyword2, keyword3
```

### Step 3: Git commit

```bash
cd ~/ai_github/ai_collection
git add INDEX.md
git commit -m "fix: add INDEX.md entry for {skill-name} (arXiv: {id})"
git -c http.proxy=http://127.0.0.1:7890 -c https.proxy=http://127.0.0.1:7890 push
```

## Prevention

Always run the 4-level duplicate + integrity check during cron research sessions:
1. `ls ~/.hermes/skills/*/{name}*` - check .hermes/skills
2. `grep -r "{arxiv_id}" ~/.hermes/skills/*/SKILL.md` - check all SKILL.md files
3. `grep -r "{arxiv_id}" ~/ai_github/ai_collection/collection/skills/*/SKILL.md` - check ai_collection
4. `grep "{name}" ~/ai_github/ai_collection/INDEX.md` - verify INDEX.md entry (NEW)

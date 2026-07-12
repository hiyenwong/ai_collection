# Domain Saturation Workflow

**Pattern**: Detect existing skill coverage before creating new skills from research papers.

## Problem

Automated research workflows (cron jobs) repeatedly process papers from the same domains. Without saturation detection, this creates:
- Duplicate skills for the same paper
- Multiple narrow skills where a synthesis umbrella would be better
- Wasted effort re-creating what already exists

## Detection Workflow

**When triggered**: Before Step 3 (skill initialization) in automated arXiv research pipelines.

### Step 1: Pre-Search Check

Search existing skills for each discovered paper:

```bash
# For each arXiv ID in the batch
for id in 2606.07336 2606.06647; do
  grep -rl "$id" ~/.hermes/skills/*/SKILL.md ~/.hermes/skills/ai_collection/*/SKILL.md
done
```

If ANY paper has existing skills → proceed to saturation check.

### Step 2: Saturation Assessment

Count coverage ratio:

- **Full saturation**: All papers in batch have existing skills (≥1 skill per paper)
- **Partial saturation**: Some papers have skills, some don't
- **No saturation**: No papers have existing skills

### Step 3: Workflow Branching

Based on saturation level:

**Full saturation** (all papers covered):
- ❌ Do NOT create new narrow skills
- ✅ Pivot to validation workflow:
  1. Verify existing SKILL.md content is current
  2. Check cross-system sync (ai_collection repo, INDEX.md)
  3. Verify Git commit history includes the paper
  4. Update downstream systems (Obsidian notes, kg.db) if missing
  5. Report: "Papers already have skills, validated sync state"

**Partial saturation** (some covered):
- Create skills for uncovered papers
- Consider synthesis umbrella for entire set (see skill-creator SKILL.md synthesis section)

**No saturation** (none covered):
- Proceed with standard skill creation workflow

## Validation Workflow (Full Saturation Case)

When all papers already have skills, verify completeness:

### Sync Verification Checklist

1. **ai_collection repo sync**:
   ```bash
   ls -la ~/ai_github/ai_collection/collection/skills/{skill-name}/
   # Compare file sizes with ~/.hermes/skills/ai_collection/{skill-name}/
   ```

2. **INDEX.md presence**:
   ```bash
   grep -A5 "{arxiv-id}" ~/ai_github/ai_collection/INDEX.md
   ```

3. **Git commit history**:
   ```bash
   cd ~/ai_github/ai_collection && git log --oneline -10
   # Look for commit mentioning the arxiv ID
   ```

4. **Obsidian notes** (if workflow requires):
   ```bash
   ls ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/
   # Check for date-appropriate research notes
   ```

5. **Knowledge graph** (if workflow requires):
   ```bash
   sqlite3 ~/.hermes/kg.db "SELECT id FROM kg_entities WHERE url LIKE '%{arxiv-id}'"
   ```

### Resolution Patterns

- **Missing in ai_collection**: Copy from `~/.hermes/skills/ai_collection/`, update INDEX.md, git commit
- **Missing in INDEX.md**: Prepend entry, git commit
- **Missing Git commit**: Already committed but unpushed → verify with `git status`, push if clean
- **Missing Obsidian**: Create learning note with paper summary + skill pointers
- **Missing kg.db**: Insert paper entity + skill relationships (see automated-research-workflow.md)

## Benefits

1. **Prevents duplicates**: Stops creating 3+ narrow skills per paper
2. **Saves compute**: Validation is faster than skill creation + packaging
3. **Improves quality**: Validates existing skills are synced across systems
4. **Enables synthesis**: When all papers have narrow skills, consider creating unified framework

## Session Examples

**2026-06-20 economics/quantum cron (NEW PATTERN — synthesis pivot)**:
- Discovered: arXiv 2604.08180 (134-page quantum finance review) + 4 other quantum finance papers
- Pre-search: Found 8+ existing quantum finance skills
- Decision: **Full saturation → synthesis pivot** → created umbrella skill `quantum-finance-computation-stack` from the comprehensive review paper (already in kg.db but had no skill)
- Result: **Synthesis umbrella created instead of narrow skill**

**Synthesis pivot pattern (NEW, 2026-06-20)**: When domain saturation is detected but a paper in the batch is a comprehensive review/survey that lacks a dedicated skill, create a **class-level umbrella skill** rather than a narrow paper-specific skill or doing nothing.

## Known Duplicate Skill Groups (2026-07-11 catalog)

The following groups cover identical papers and need curator consolidation:

| arXiv ID | Keep (canonical) | Delete (duplicates) |
|----------|-----------------|---------------------|
| 2607.02283 | `dendritic-in-context-learning-snn` | `dendritic-icl-snn`, `dendricl-icl-single-layer-snn` |
| 2607.07077 | `hyperbolic-learning-brain-graphs` (ai_collection) | `hlbg-hyperbolic-learning-brain-graphs` (neuroscience/) |
| 2607.06456 | `hardware-aware-mixed-signal-snn-framework` | `hardware-aware-snn-design-space-exploration` |
| 2607.03890 | `sound-localization-equilibrium-dynamics` | `equilibrium-dynamics-sound-localization` |
| 2607.08561 | `contravariance-theory-strong-alignment-minimal` | `contravariance-theory-strong-alignment` |
| 2606.30319 | `brainjanus-unified-brain-model` | `brainjanus-unified-brain-vision-language` |
| 2607.07373 | `dynamic-neural-manifolds-snn-control` | `dynamic-neural-manifold-snn-control` |
| 2607.05652 | `pathwise-metastability-galves-locherbach-models` | `pathwise-metastability-galves-locherbach` |

**Ghost entries** (INDEX.md listed but no skill exists):
- `brainjanus-unified-brain` — no local SKILL.md, no repo directory

**See**: `references/cron-session-log-2026-07-11.md` for full session details

## Integration Points

- See `references/automated-research-workflow.md` for complete pipeline including kg.db schema
- See skill-creator SKILL.md synthesis section for creating unified frameworks from saturated domains
- See skill-creator SKILL.md pitfalls section for git split index issues (use `git add -A`)

## Activation

This workflow activates automatically in:
- Automated research cron jobs
- Session reviews that discover duplicate skills
- Domain-specific paper processing (neuroscience, quantum, etc.)

Keyword triggers: "domain saturation", "paper already has skill", "duplicate skill detection", "validate existing skills"
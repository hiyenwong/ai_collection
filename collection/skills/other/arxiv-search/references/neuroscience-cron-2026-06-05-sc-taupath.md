# Neuroscience Cron Session — SC-TauPath Workflow (2026-06-05)

## Session Overview

- **Paper**: arXiv:2606.04066 — "SC-TauPath: A Structural Connectivity Attribution Framework for Mapping Alzheimer's Tau Propagation Pathways"
- **Authors**: Jing Zhang et al.
- **Submitted**: 2026-06-02
- **Categories**: q-bio.NC, cs.LG
- **Skill created**: `sc-taupath-alzheimer-tau-propagation`

## Workflow Steps Executed

1. **Paper discovery**: browser_navigate → `https://arxiv.org/list/q-bio.NC/recent`
2. **Paper selection**: Dual-keyword scoring (9 neuroscience keywords)
3. **Skill creation**: skill_manage → neuroscience category
4. **Sync to ai_collection**: cp skill directory → git workflow
5. **Obsidian note**: write_file to `~/obsidian/科技/论文/神经科学/`
6. **Knowledge graph**: INSERT to `kg.db` papers table

## Key Pitfalls Discovered

### 1. YAML Title Quoting Required

**Problem**: Paper titles containing colons cause YAML parse errors when unquoted in SKILL.md frontmatter.

**Failure example**:
```yaml
paper_title: SC-TauPath: A Structural Connectivity Attribution Framework
```
**Error**: YAML parse error at line 2 (colon triggers key: value parsing)

**Fix**: Always quote the `paper_title` field:
```yaml
paper_title: "SC-TauPath: A Structural Connectivity Attribution Framework"
```

**Verification**: skill_manage(action='create') succeeds after quoting.

### 2. ai_collection Repository Push Blocked

**Problem**: Direct push to `main` branch blocked by GitHub repository rules requiring PR-based contributions.

**Error message**:
```
remote: error: GH006: Protected branch update failed for refs/heads/main
remote: error: Required status checks are expected
```

**Fix pattern**:
```bash
cd ~/ai_github/ai_collection
git checkout -b neuroscience/sc-taupath-2606.04066
git push origin neuroscience/sc-taupath-2606.04066
gh pr create --title "feat: add sc-taupath from arXiv 2606.04066" --body "..."
# PR URL: https://github.com/hiyenwong/ai_collection/pull/14
git checkout main  # Return to main branch
```

**Result**: Branch created → pushed → PR #14 created → returned to main with staged changes.

### 3. Directory Size Exceeds GitHub Display Limit

**Problem**: Three directories in `collection/skills/` exceed GitHub's 1000-file display limit:
- `neuroscience`: 1149 files
- `quantum`: 1077 files  
- `other`: 1283 files

**Impact**: Files beyond position 1000 invisible in GitHub web UI, limiting review/PR verification.

**Mitigation options**:
1. Sub-categorize: `neuroscience/cortical/`, `neuroscience/synaptic/`, `neuroscience/clinical/`
2. Date-based subdirectories: `neuroscience/2026-06/`
3. Periodic cleanup of obsolete skills
4. Use `git ls-tree -r HEAD --name-only | grep neuroscience | wc -l` to count via CLI

**Current status**: Not blocking operations, but limiting UI visibility.

## Knowledge Graph Import

**Schema verified**: `kg_entities.id` is INTEGER PRIMARY KEY (auto-increment), NOT TEXT.

**Insert pattern**:
```sql
INSERT INTO kg_entities (title, url, content, authors, published_date, category, source)
VALUES ('SC-TauPath: A Structural Connectivity Attribution Framework...',
        'https://arxiv.org/abs/2606.04066',
        '...',
        'Jing Zhang, ...',
        '2026-06-02',
        'neuroscience',
        'arxiv');
-- Use cur.lastrowid to get assigned ID
```

**Tags added**: tau-propagation, alzheimer, structural-connectivity, attribution, network-diffusion, Braak-staging, DTI, PET, pathway-mapping, interpretability (10 tags)

## Working Tree State After Session

- **Branch**: `main` (switched from feature branch after PR creation)
- **Modified on main**: `INDEX.md` (uncommitted)
- **Staged on main**: `collection/skills/sc-taupath-alzheimer-tau-propagation/SKILL.md` (uncommitted)
- **Branch ahead**: main is 2 commits ahead of origin/main (from previous work)
- **PR status**: #14 pending merge on branch `neuroscience/sc-taupath-2606.04066`

## Lessons for Future Sessions

1. **Always quote paper_title in YAML** when creating neuroscience skills
2. **Use branch + PR workflow** for ai_collection contributions (direct push blocked)
3. **Verify kg.db schema** before INSERT (id is auto-increment INTEGER)
4. **Return to main branch** after PR creation to leave clean working tree
5. **Use targeted git add** (not `git add -A`) to avoid capturing sibling session cleanup

## SC-TauPath Core Methodology

- **NDM-augmented MLP**: Network diffusion model integrated with multi-layer perceptron
- **Gradient×input attribution**: Edge contribution scoring via backpropagation gradients
- **Validation**: ADNI 234 participants, Braak staging anatomy confirmed
- **Key contribution**: Maps tau propagation pathways via structural connectivity edge scoring

## Related Skills

- `stp-stabilizes-goal-conditioned-dynamics` (arXiv:2606.03481)
- `discrete-signaling-chaotic-regularization-rnn` (arXiv:2606.04426)
- `sc-taupath-alzheimer-tau-propagation` (arXiv:2606.04066) — this session

## Session Date

2026-06-05 Thursday — Cron job executed at scheduled time.
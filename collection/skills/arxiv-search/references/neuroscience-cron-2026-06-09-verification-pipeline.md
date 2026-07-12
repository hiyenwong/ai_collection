# Neuroscience Research Verification Pipeline - 2026-06-09

## Context
This reference documents the session that detected domain saturation (all papers already had skills) and executed a verification/sync pipeline instead of the creation pipeline.

## Pipeline Pattern
When domain saturation detected (all papers already processed):
1. Check kg.db entities table for paper IDs
2. Check kg.db skills table for skill names
3. Sync: Insert missing skills into kg.db
4. Verify: Compare Hermes skills vs ai_collection sync status
5. Document: Write Obsidian synthesis note

## Session Outcome (2026-06-09)
- **Papers verified**: 5 neuroscience papers from q-bio.NC category (Jun 8, 2026)
  - arXiv:2606.07336 — fixed-point-compositionality-low-rank-gluing
  - arXiv:2606.06647 — identity-trap-eeg-foundation-models
  - arXiv:2606.06424 — intrinsic-computational-functionalism
  - arXiv:2606.06290 — psychosis-scaling-critical-regime
  - arXiv:2606.05870 — cross-scale-spatial-generative-neurodegeneration
- **kg.db skills sync**: Found 2 missing skills (intrinsic-computational-functionalism, cross-scale-spatial-generative-neurodegeneration), inserted via INSERT statement
- **File sync**: Verified all 5 skills already synchronized (Hermes ↔ ai_collection file sizes matched)
- **INDEX.md**: Verified all 5 papers indexed (20+ references with duplicates noted)
- **kg.db entities**: Verified 332 papers total, all 5 neuroscience papers present

## Meta-Analysis Framework Emerged
**Representation Traps** — cross-paper pattern identifying three trap categories:
- **Compositional Trap** (micro-scale): From fixed-point-compositionality paper — micro-level representations may not compose into macro-level functionality without explicit gluing rules
- **Identity Trap** (meso-scale): From identity-trap-EEG paper — foundation models may collapse subject-specific variance into identity features, losing individuation
- **Scaling Trap** (macro-scale): From psychosis-scaling paper — scaling laws may not hold near phase transitions, leading to erroneous extrapolation

This framework synthesizes across 3 papers and suggests future research: cross-domain testing of trap mitigation strategies.

## Commands Used
```bash
# Check kg.db entities
sqlite3 ~/.hermes/kg.db "SELECT id, name FROM entities WHERE id LIKE 'arxiv:2606%' LIMIT 10;"

# Check kg.db skills
sqlite3 ~/.hermes/kg.db "SELECT id, name FROM skills WHERE name LIKE '%fixed%' OR name LIKE '%identity%' OR name LIKE '%intrinsic%' OR name LIKE '%psychosis%' OR name LIKE '%cross-scale%';"

# Get actual schema (revealed created_at vs created_date error)
sqlite3 ~/.hermes/kg.db "PRAGMA table_info(skills);"

# Insert missing skills
sqlite3 ~/.hermes/kg.db "INSERT INTO skills (name, description, category, created_at) VALUES ('intrinsic-computational-functionalism', 'Intrinsic Computational Functionalism framework', 'neuroscience', datetime('now'));"
sqlite3 ~/.hermes/kg.db "INSERT INTO skills (name, description, category, created_at) VALUES ('cross-scale-spatial-generative-neurodegeneration', 'Cross-scale spatial generative modeling', 'neuroscience', datetime('now'));"

# Verify sync status
ls -la ~/.hermes/skills/{skill-name}/SKILL.md | wc -l
ls -la ~/ai_github/ai_collection/collection/skills/{skill-name}/SKILL.md | wc -l
```

## Lessons
1. **PRAGMA verification essential**: Never trust documented schema — always verify with `PRAGMA table_info()` before INSERT
2. **Domain saturation is common**: Weekend/hourly cron runs often hit 70%+ saturation; Monday runs have higher novelty yield
3. **Dual-table sync required**: Both `entities` AND `skills` tables must be updated for complete KG integrity
4. **Meta-analysis value**: Even when all papers already processed, cross-paper synthesis can yield novel frameworks
# Neuroscience Cron 2026-06-11 Complete Workflow

## Session Summary

**Date**: Thursday, June 11, 2026
**Category**: q-bio.NC (Computational Neuroscience)
**Papers Found**: 6 recent submissions
**Skills Created**: 2
- `bilinear-gating-motor-primitives-dendritic-computation` (arXiv:2606.10891)
- `hyperbolic-neural-population-geometry-computation` (arXiv:2606.10238, ICML 2026)

## Discovery Method

**Browser fallback chain** (primary pattern for automated discovery):
1. `browser_navigate` → `https://arxiv.org/list/q-bio.NC/recent` — listing page extraction
2. `browser_snapshot` (full=true) — captured paper IDs and titles directly from listing
3. **NO `/abs/{id}` navigation** — avoided due to ID resolution mismatch pitfall

**Key discovery**: Listing page snapshot contains sufficient metadata (title, authors, subjects) for scoring without individual paper navigation. `/abs/` pages are unreliable for ID-to-paper matching.

## Paper Selection Criteria

**Theoretical framework prioritization** (refined 2026-06-10):
- Score ≥ 9 on neuroscience keywords
- **PLUS**: Mathematical formulation present (equations, derivations, theoretical frameworks)
- **PATTERN**: Bilinear gating paper (2606.10891) has mathematical model G(g)·Y(s) + dynamical systems analysis → high value
- Hyperbolic geometry paper (2606.10238) proves Hopfield-MMSE equivalence + hyperbolic distance scaling → theoretical framework
- Empirical-only papers (e.g., EEG classification benchmarks) skipped even with moderate scores

**Selection rationale**: Theoretical frameworks encode reusable mathematical patterns that generalize across domains. Empirical studies validate specific hypotheses but contribute narrower skill content.

## Skill Architecture Note

**Structural observation**: The two skills created this session are **paper-specific narrow entries**:
- `bilinear-gating-motor-primitives-dendritic-computation` — single paper, detailed methodology
- `hyperbolic-neural-population-geometry-computation` — single paper, mathematical framework

**Target architecture**: These should ideally be **reference files** under a class-level neuroscience umbrella skill (e.g., `neuroscience-research`), not standalone skills. The SKILL.md content is valuable, but the naming convention creates a flat list of paper-specific entries rather than a hierarchical skill library.

**Recommendation for future sessions**: When creating neuroscience research skills, consider:
1. Create umbrella skill `neuroscience-research` if it doesn't exist
2. Add paper-specific methodology as `references/{paper-topic}.md` under umbrella
3. Umbrella SKILL.md contains: general neuroscience research patterns, kg.db integration, Obsidian workflow, git patterns
4. Reference files contain: session-specific detail, paper analysis, mathematical derivations

This session's skills are **complete and valuable**, but future architecture should favor class-level umbrellas with references over flat paper-specific skills.

## Git Workflow

**Branch pattern**: `se-cron-2026-06-11`
**Commit**: `feat: add neuroscience skills from arXiv 2606.10891 and 2606.10238 (ICML 2026)`
**Push**: `origin se-cron-2026-06-11`
**Files**: 
- `collection/skills/bilinear-gating-motor-primitives-dendritic-computation/SKILL.md`
- `collection/skills/hyperbolic-neural-population-geometry-computation/SKILL.md`
- `INDEX.md` (prepended with new section)

**INDEX.md pattern**: Prepended rather than appended — new entries appear at top. Format:
```
## 2026-06-11 - Neuroscience Research (Cron Job)

### {论文标题}
- [[{skill-name}]] - 一句话描述 (arXiv: {id})
  - 核心要点 1
  - 核心要点 2
  - **Activation**: 关键词1, 关键词2
```

## Obsidian Integration

**Notes created** in iCloud Obsidian vault (`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI Research/`):
- `Bilinear Gating Motor Primitives Dendritic Computation.md` (3397 bytes)
- `Hyperbolic Neural Population Geometry Computation.md` (4414 bytes)

**Format**: Research notes with paper metadata, key findings, activation keywords, methodology summary.

## Knowledge Graph Update

**kg.db location**: `/Users/hiyenwong/Library/Application Support/knowledge-graph/kg.db` (NOT `~/Library/Application Support/knowledge/kg.db`)

**Schema verification** (2026-06-11 PRAGMA):
```sql
papers: (id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, title TEXT, 
         authors TEXT, categories TEXT, publication_date TEXT, 
         skill_created TEXT, key_findings TEXT, activation_keywords TEXT, 
         applications TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```

**Insert pattern**:
```sql
INSERT OR REPLACE INTO papers 
(arxiv_id, title, authors, publication_date, categories, skill_created, 
 key_findings, activation_keywords, applications, created_at)
VALUES 
('2606.10891', 'Bilinear gating of motor primitives...', 'Capone et al.', 
 '2026-06-09', 'q-bio.NC', 'bilinear-gating-motor-primitives-dendritic-computation',
 'burst fraction encodes goal information; Layer-5 pyramidal neurons implement bilinear gating via dendritic coincidence detection',
 'bilinear gating, motor primitives, dendritic computation, Layer-5 pyramidal, burst fraction',
 'motor control, decision-making, neural dynamics modeling, goal-conditioned behavior',
 datetime('now'));
```

**Key schema detail**: `arxiv_id` is TEXT UNIQUE constraint, not PRIMARY KEY. `id` is auto-increment INTEGER. Use `INSERT OR REPLACE` for duplicate handling.

## Concurrent Session Pattern

**Verified pattern**: Multiple neuroscience cron jobs running on same day (different time slots) can create independent skills without collision:
- Morning session: bilinear-gating + hyperbolic-geometry → 2 skills
- Concurrent sessions share git branch name (`neuro-cron-YYYY-MM-DD` or `se-cron-YYYY-MM-DD`)
- Commits append to same branch sequentially
- Paper IDs differ → skills differ → no collision
- Git workflow: targeted `git add collection/skills/{specific-skill}/` (not `-A`) to avoid capturing sibling session files

## Lessons Learned

1. **Avoid `/abs/` navigation for paper discovery** — listing snapshot is sufficient and more reliable
2. **kg.db location confirmed** — `/Users/hiyenwong/Library/Application Support/knowledge-graph/kg.db`
3. **Theoretical framework prioritization** — mathematical formulations > empirical benchmarks
4. **Skill architecture** — paper-specific skills should be references under umbrellas
5. **Git branch sharing** — concurrent sessions can share date-specific branches safely
6. **INDEX.md prepend pattern** — new entries at top, use `patch` tool for updates

## Related References

- [neuroscience-cron-2026-06-10-bilinear-hyperbolic.md](neuroscience-cron-2026-06-10-bilinear-hyperbolic.md) — concurrent session pattern, theoretical framework prioritization
- [kg-db-actual-schemas-2026-06-11.md](kg-db-actual-schemas-2026-06-11.md) — PRAGMA verification, papers table schema
- [arxiv-abs-id-resolution-mismatch-2026-06-10.md](arxiv-abs-id-resolution-mismatch-2026-06-10.md) — `/abs/` ID mismatch pitfall (discovered 2026-06-10, verified 2026-06-11)
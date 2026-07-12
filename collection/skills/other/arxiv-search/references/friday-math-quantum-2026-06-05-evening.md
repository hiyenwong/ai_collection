# Friday Math+Quantum Cron — 2026-06-05 Evening Run

## Discovery
- Feeds: quant-ph (106) + math.NT (29) + stat.ME (49) + math.PR (35) + math.ST (31) = **250 items**
- Cross-domain matches (math+quantum): **125**
- Math-only: 108, Quantum-only: 10

## Top Papers
| arXiv | Title | Math | Quantum | Total |
|-------|-------|------|---------|-------|
| 2606.06362 | Quantum thermalisation in free fermions | 6 | 6 | 12 |
| 2605.29732 | Exact Geometric Typicality and Bipartite Entanglement | 8 | 4 | 12 |
| 2606.06426 | Robust Framework for Model Order Selection (CES Noise) | 11 | 0 | 11 |
| 2606.05992 | GKP Boson Sampling ML Surrogate | 4 | 6 | 10 |
| 2507.06232 | Error Exponents for Quantum Packing | 6 | 4 | 10 |

## Skills Created
1. `quantum-thermalisation-fermions` (2606.06362) — Closed-system thermalisation, Mpemba effect, covariance matrix methods
2. `gkp-boson-sampling-ml-surrogate` (2606.05992) — Two-stage ML surrogate for GBS circuit screening

## KG Import
- 7 papers → kg.db entities (rowid 154-160), 7 vector embeddings in kg_vectors
- 1 paper already existed (2606.05387)

## Schema Clarification
- `entities.id` = TEXT (arxiv ID), `entities.rowid` = INTEGER (auto-increment)
- `kg_vectors.entity_id` → `entities.rowid` (INTEGER), NOT `entities.id`
- `kg_vectors.vector_data` = BLOB (stores JSON-encoded float arrays)

## Git Sync
- Branch: `friday-math-quantum-2026-06-05`, Commit: `f0901050`
- `patch` tool works reliably for INDEX.md updates — avoids truncation pitfall

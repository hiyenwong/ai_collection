# Friday Math+Quantum Cron — 2026-06-06 (Batch 2)

## Papers Discovered (Second Wave)

| arXiv | Title | Category | Score | Notes |
|-------|-------|----------|-------|-------|
| 2606.06455 | Breakeven demonstration of quantum low-density parity-check codes | quant-ph; cs.IT | 5 | qLDPC breakeven on trapped-ion, OMG architecture, 4→18 qubits |
| 2606.06365 | A framework for low-overhead quantum fault tolerance via spacetime lifting | quant-ph | 4 | Homological algebra, symmetry-reduced products, almost-linear scaling |
| 2606.06179 | Diffusion Models Observe Only Gradients: A Geometric Perspective on Score Matching Errors | stat.ML; cs.LG | 5 | Helmholtz-Hodge decomposition, Fokker-Planck, KL divergence, Sobolev identity |

## Skills Created

1. **quantum-ldpc-breakeven** — Trapped-ion qLDPC breakeven, OMG architecture, multi-code testing
2. **spacetime-lifting-quantum-fault-tolerance** — Homological fault complexes, spacetime lifting, measurement-based interpretation
3. **score-matching-gradient-decomposition** — Helmholtz-Hodge decomposition, solenoidal invisibility, dual Sobolev estimator

## Discovery Sources

- `https://arxiv.org/list/quant-ph/recent` → 65 entries (Fri Jun 5-6)
- `https://arxiv.org/list/stat.ML/recent` → 41 entries
- Broad search: quantum AND (number theory OR statistics OR probability OR matrix OR estimation OR eigenvalue OR linear algebra) → 2,070 results

## KG Import Details

- 3 papers imported to kg.db entities 2260-2262
- 3 vector embeddings generated (kg_vectors table, `vector_data` BLOB column, 384-dim)
- kg_vectors schema: (id INTEGER PK, entity_id INTEGER, vector_data BLOB, created_at TIMESTAMP)

## Sync

- Committed to branch: `neuro-cron-2026-06-05`
- Commit: `a7225259`
- 4 files: 3 SKILL.md + INDEX.md

## Pitfall Confirmed

- **kg_vectors column name**: Must use `vector_data` NOT `embedding`. The column holds JSON-encoded float arrays as BLOB. `PRAGMA table_info(kg_vectors)` confirms: `0|id|INTEGER|0||1`, `1|entity_id|INTEGER|0||0`, `2|vector_data|BLOB|0||0`, `3|created_at|TIMESTAMP|0|CURRENT_TIMESTAMP|0`.
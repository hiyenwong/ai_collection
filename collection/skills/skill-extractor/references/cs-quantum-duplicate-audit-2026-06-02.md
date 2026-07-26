# CS+Quantum Skill Duplicate Audit — 2026-06-02

## Context

2026-06-02 Tuesday cron job scan of kg.db for recent CS+Quantum papers (arXiv IDs from rowid 1888-1918).

## Papers Scanned & Existing Skill Matches

| arXiv ID | Paper Title | Existing Skill(s) | Status |
|----------|------------|-------------------|--------|
| 2605.31493 | Progressive Swapping to the Middle | `progressive-swapping-quantum-network-protocol`, `psm-quantum-memory-distribution` | **DUPLICATE** — 2 skills for same paper |
| 2605.31449 | Support Vector Machine with Scalable Quantum Kernel | `hamming-quantum-kernel-svm`, `quantum-ml-patterns` | Overlapping |
| 2605.31006 | Quantum State Preparation via Neural Network Encoding | `nn-quantum-state-encoding` | ✅ |
| 2605.30866 | Generative Quantum Data Embeddings | `generative-quantum-embeddings` | ✅ |
| 2605.30429 | Attention-based optimizer for symmetry finding | `attention-quantum-symmetry` | ✅ |
| 2605.27278 | Optimal quantum locally differentially private mechanisms | `quantum-local-differential-privacy` | ✅ |

## Known Duplicates Requiring Consolidation

1. **2605.31493**: `psm-quantum-memory-distribution` AND `progressive-swapping-quantum-network-protocol` — same paper
2. **2605.30866**: `generative-quantum-embedding` (singular) vs `generative-quantum-embeddings` (plural) — same paper
3. **2511.11609**: `stochastic-quantum-neural-networks` (malformed name) vs `stochastic-quantum-neural-network-ai` — same paper

## Saturation Metrics

- 6 papers scanned → all 6 had at least one corresponding skill
- 2 papers had duplicate skills (2 skills for same paper)
- Net new skills needed: **0**
- Saturation rate: **100%** (vs ~85-90% estimate)

## Implication

The skill library is approaching full saturation for CS+Quantum papers. Future cron jobs should:
1. Prioritize skill enhancement over creation
2. Focus on cross-domain synthesis (CS+Quantum+Medical, CS+Quantum+Econ)
3. Flag duplicates for curator consolidation

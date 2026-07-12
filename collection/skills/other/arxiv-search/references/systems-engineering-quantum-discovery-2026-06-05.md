# Systems Engineering + Quantum Discovery (2026-06-05 Thursday)

## RSS Feed Yields

| Feed | Items | Cross-Domain Matches |
|------|-------|---------------------|
| quant-ph+cs.SY+eess.SY+cs.DC | 179 | 102 |

Consistent with 2026-06-04 yield (102 matches from 4 combined feeds).

## Top Papers by Dual-Keyword Score

| Score | arXiv | Title |
|-------|-------|-------|
| 10 (6+4) | 2604.13643 | Quantum secret sharing in tripartite superconducting network |
| 10 (6+4) | 2604.21472 | LightStim: QEC Protocol Evaluation with Automated DEM |
| 10 (8+2) | 2511.23462 | Arbitrary control of temporal waveform of photons |
| 9 (6+3) | 2606.04312 | Characterization of errors in photon-heralded quantum operations |
| 9 (6+3) | 2606.05060 | High-fidelity neutral atom gates via low-rank Hessian optimization |

## Skills Created

1. **lightstim-qec-protocol-evaluation** (arXiv: 2604.21472) - QEC protocol evaluation framework
2. **low-rank-hessian-quantum-gate-calibration** (arXiv: 2606.05060) - Gate calibration methodology

## Parallel Session Duplicate (IMPORTANT)

A sibling cron session running concurrently already created entries in INDEX.md for both papers:
- `low-rank-hessian-quantum-control` was already in INDEX.md (line 86-90)
- `lightstim-qec-protocol-evaluation` was already in INDEX.md (line 123-128)

**Lesson**: Before creating new INDEX.md entries, always `grep` for the arXiv ID first.
If an entry exists, PATCH it with more detail instead of creating a duplicate.

## KG Tool Path Mismatch

- `kg_tool` binary reports: `DB path: /Users/hiyenwong/wiki/kg.db`
- Cron job uses: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- These are TWO separate databases with different schemas
- Use the workspace kg.db for cron workflows (arxiv_papers, kg_entities, kg_relations)
- kg_tool binary operates on the wiki kg.db (entities, relationships, pagerank, kg_vectors)

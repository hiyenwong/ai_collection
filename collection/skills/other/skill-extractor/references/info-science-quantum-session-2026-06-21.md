# Information Science + Quantum — Session Notes 2026-06-21

## arXiv API Status (RECONFIRMED 2026-06-21)
- `urllib.request` with proxy `http://127.0.0.1:7890` ✅ works during cron jobs
- `curl` with HTTPS ✅ works
- `web_search` (Firecrawl) ❌ returns NoneType errors for arXiv
- `web_extract` ❌ blocks arxiv.org URLs
- **Working query patterns**: `cat:quant-ph+AND+all:information+theory` or `cat:quant-ph+AND+(all:privacy+OR+all:security+OR+all:communication)`

## New Skills Created (3)
1. `passive-user-loop-back-qkd` (2606.19551) — Bell-state Loop-Back QKD for passive users
2. `vine-codes-qldpc` (2606.20263) — qLDPC codes on planar square grids
3. `qpu-scale-randomized-benchmarking` (2606.20123) — MQA protocol for whole-QPU benchmarking

## Additional Papers Discovered (all existing skills, no new skill needed)
- 2606.20003 — Optimal Shadow Estimation → `optimal-shadow-estimation` (verified sync)
- 2606.20513 — Frontier Decoder qLDPC → `frontier-qldpc-decoder` (verified sync)
- 2606.19486 — Ansatz-free Hamiltonian Learning → `optimal-ansatz-free-hamiltonian-learning` (verified sync)
- 2606.19196 — Blind Symmetry Matching → `blind-symmetry-matching-quantum` (verified sync)
- 2606.17268 — Coset-based qLDPC → `coset-based-qldpc-codes` (verified sync)
- 2606.19493 — Ricci flow Bures-Helstrom metric → `ricci-flow-bures-helstrom-qubit-metric`
- 2606.18666 — Covert Blockwise Coding → `covert-bosonic-sequential-detection`
- 2606.15996 — Sharma-Mittal entropy gravity → `sharma-mittal-entropy-gravity` (NEW)

## New Skill Created (1 additional)
4. `sharma-mittal-entropy-gravity` (2606.15996) — SM entropy bridging info theory to infrared gravity, derives MOND-like regime from generalized entropy parameters

## Domain Saturation (Updated)
- Information Science + Quantum: ~65% (14 papers → 8 existing, 3 new, 3 skipped)
- qLDPC subdomain: ~70% (construction + decoding + benchmarking all covered)
- QKD/Communication: ~80%+ (well-covered)
- Shadow Estimation: ~90% (optimal-shadow-estimation, classical-shadow-unitary-channel-estimation, classical-shadow-estimation)

## KG Update
- Added 3 entities (2606.20513, 2606.19486, 2606.17268) to workspace kg.db
- Generated vectors for new entities
- Total entities: 2731
- Total vectors: 7219

## Overlap Alert
- qLDPC codes cluster: `vine-codes-qldpc`, `frontier-qldpc-decoder`, `coset-based-qldpc-codes`, `sparse-mamba-qec-decoder`, `qldpc-breakeven-evaluation` → consider `quantum-ldpc-codes` umbrella
- Benchmarking cluster: `qpu-scale-randomized-benchmarking`, `quantum-fault-tolerance-benchmark`, `application-level-quantum-benchmarking` → consider `quantum-benchmarking` umbrella

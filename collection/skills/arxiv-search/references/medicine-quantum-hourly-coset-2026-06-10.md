# 2026-06-10 Medicine + Quantum Hourly — Coset Ensemble Decoder

## Discovery
- arXiv API via proxy: `curl -x http://127.0.0.1:7890 https://export.arxiv.org/api/query`
- Three queries: (1) quantum medicine/healthcare, (2) quantum computing + neural network, (3) cat:quant-ph recent
- 61 new quant-ph entries scanned

## Paper Selected
- **2606.11076**: Coset Ensemble Decoder for QEC with Algorithm-Hardware Co-Design
- **Key results**: 8.2x FPGA LUT reduction; better accuracy-latency than MWPM/UF; tunable candidate number
- **Implementation**: github.com/IMSeonL/coset-ensemble-decoder

## Git Rebase Pitfall (CRITICAL)
- ai_collection main had pending rebase (158 commits remaining) when `git pull` was attempted
- `git pull` → merge conflicts in INDEX.md + 10+ SKILL.md modify/delete conflicts
- `git rebase --continue` failed due to dumb terminal + unset EDITOR
- **Fix**: `git rebase --abort` then work on existing branch without pulling
- **Lesson**: Before pulling in ai_collection, always `git status` first. If rebase in progress, abort or skip pull.

## INDEX.md Conflict Resolution
- File contained `<<<<<<< HEAD` markers after failed merge
- Existing entry at arXiv 2606.10777 referenced same skill name but different paper
- Updated entry to 2606.11076 with correct FPGA co-design details

## Pattern: QEC Hardware-Software Co-Design
Three skills from today's sessions all illustrate this theme:
1. coset-ensemble-decoder-qec — FPGA co-design for QEC decoding
2. jacobian-geometry-robustness-qnn — noise-aware training with hardware calibration
3. analog-quantum-event-gnn — native Rydberg Hamiltonian implementation
Medical implication: quantum ML for healthcare must account for NISQ hardware constraints from design phase.

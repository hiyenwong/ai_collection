# Information Science + Quantum — 2026-06-14 Sunday

## Browser Discovery
- **Source**: `https://arxiv.org/list/cs.IT/recent` → 107 entries
- **Cross-domain matches** (info_score > 0 AND quantum_score > 0):
  - 2605.25692 (score 5): Homomorphic Quantum Error Correction — QHE+QEC algebraic compatibility ✅ NEW skill
  - 2606.12301 (score 4): Iterative Ising decoder for QEC — ❌ existing skill (iterative-ising-qec-decoder)
  - 2606.11580 (score 3): Superspace Concentration & Adversarial Robustness — ✅ NEW skill
  - 2606.13286 (score 3): Quantum Communication with Phase-squeezed M-PSK — ⏭️ skipped
  - 2606.12445 (score 2): SAT/MaxSAT/SMT for QLDPC Distance — ✅ NEW skill
  - 2606.11468 (score 3): Entanglement-Assisted QLDPC Encoder Circuits — ⏭️ skipped

## Novel Patterns Found
1. **Homomorphic QEC**: Bridges quantum cryptography (QHE) with error correction — code-space preservation during encrypted cloud computation
2. **Superspace Focus Measure**: F(ρ) = λ_max(ρ_super) as resource-theoretic monotone for adversarial robustness; 74% better resilience threshold vs fidelity
3. **Solver Architecture > Problem Structure**: For QLDPC distance, branch-and-bound MaxSAT dominates unsat-core MaxSAT despite XOR-rich parity checks

## kg.db State After Session
- papers: 178 (+3)
- kg_entities: 2,388 (+3)
- kg_vectors: 5,075 (+3)
- Domain saturation: ~60%

## Confirmed Patterns
- cs.IT listing pages remain PRIMARY source for info-science + quantum papers (30% cross-domain rate)
- browser_console extraction with dual-keyword scoring works reliably
- git branch pattern (info-science-cron-YYYY-MM-DD) works without conflicts

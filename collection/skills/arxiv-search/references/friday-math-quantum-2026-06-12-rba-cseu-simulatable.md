# Friday Math+Quantum 2026-06-12: RBA, CSEU, Simulatable Processes

## Session Summary
Today's weekly topic: **Number Theory, Statistics, Advanced Mathematics** + daily **Quantum Mechanics**.

## Top 3 Papers (all cross-domain math+quantum)

### 1. arXiv:2606.13457 — Reduced Basis Algorithm for Nonlinear ODEs/PDEs on Quantum Computers
- **Math score**: 9 (numerical analysis, ODE, PDE, algorithm, linear algebra)
- **Quantum score**: 6 (quantum, qubits, block-encoding, Pauli decomposition)
- **Categories**: math.NA, quant-ph
- **Key methodology**: Lifts polynomial nonlinear dynamics into linear quantum-accessible operators via monomial basis composition. Logarithmic qubit scaling in grid size.
- **Skill created**: `reduced-basis-quantum-ode-solver`
- **Note**: Already existed in ai_collection from previous session — Hermes version was richer, updated it during sync.

### 2. arXiv:2606.13638 — Classical Shadow Estimation of Unitary Channels at Heisenberg Limit
- **Math score**: 7 (statistics, estimation, matrix, eigenvalue)
- **Quantum score**: 8 (quantum, unitary, measurement, tomography, Hamiltonian)
- **Categories**: quant-ph
- **Key methodology**: Parallel non-adaptive CSEU protocol achieving O(d/epsilon) Heisenberg-limit query complexity with matching lower bound.
- **Skill created**: `classical-shadow-unitary-channel-estimation`

### 3. arXiv:2606.13576 — Learning with Simulators (COLT 2026)
- **Statistics score**: 8 (machine learning, statistics, VC dimension, Kolmogorov complexity)
- **Categories**: cs.LG, cs.CC, cs.DS, stat.ML
- **Key methodology**: Simulator access replaces independence assumption in PAC learning; universal algorithm with regret bounded by time-bounded Kolmogorov complexity.
- **Skill created**: `simulatable-process-learning-theory`

## Domain Saturation: ~60-65%
Improvement from previous Friday evening run (55%). Math+quantum cross-domain continues producing high-value skills at a steady rate.

## INDEX.md Prepend Pattern
When INDEX.md is too large for read_file (>100K chars) and patch fails due to duplicate headings:
```bash
python3 -c "
import re
with open('/tmp/new_entries.md', 'r') as f: new = f.read()
with open('INDEX.md', 'r') as f: content = f.read()
new_content = re.sub(r'(# AI Collection Index\n\n)', r'\1' + new + '\n', content, count=1)
with open('INDEX.md', 'w') as f: f.write(new_content)
"
```
This avoids read_file size limits and patch ambiguity on recurring date headings.

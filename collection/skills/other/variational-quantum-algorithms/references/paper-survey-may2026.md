# Paper Survey — Variational Quantum Algorithms (May 2026)

Source papers collected during 2026-05-05 research session.

## 2605.00807 — CVQE with Trapezoidal Guiding States

**Authors:** Yi-Hua Lai, John P.T. Stenger, Gloria Bazargan, Igor V. Schweigert, Daniel Gunlynde
**Key insight:** CVQE eliminates iterative quantum-classical communication of conventional VQE. The choice of guiding state is critical — trapezoidal-state preparation enables accurate many-electron ground-state solutions with minimal resources.
**Method:** Analyze state probability distributions at each CVQE stage to determine optimal guiding-state parameters.
**Validation:** Tested on prototypical bimolecular reaction H₂ + H₂ → H₂ + H₂ using NISQ computing.

## 2605.00747 — QIBP Certified QNN Training

**Authors:** Emma Andrews, Nahyeon Kim, Prabhat Mishra
**Key insight:** Interval Bound Propagation (IBP), successful in classical ML for adversarial robustness, extended to quantum domain as QIBP.
**Method:** Track lower/upper bounds through QNN circuit; implement with both interval arithmetic (tighter bounds) and affine arithmetic (faster).
**Result:** Certified models guarantee correct predictions for samples within trained adversarial robustness bounds.

## 2605.00739 — Resource-Efficient VQE for TSP

**Authors:** Yuefeng Lin, Chao Zheng, Cong Guo
**Key insight:** Standard one-hot TSP encoding requires O(n²) qubits; compact binary encoding reduces to O(n log n).
**Components:**
- Compact binary-register encoding
- Permutation-preserving problem-inspired ansatz
- Divide-and-conquer execution strategy (each subsystem fits available hardware)
**Results:** 4-city: 100%, 5-city: 100%, 6-city: 95.5% success rates. Tested on SpinQ Gemini Pro and Triangulum II NMR quantum computers.

## Related Papers (same date)

| arXiv | Title | Relevance |
|-------|-------|-----------|
| 2605.00794 | Quantum Simulation of DAEs | Quantum algorithms for differential equations |
| 2605.00772 | Entanglement capacity from quantum walks | Network entanglement analysis |
| 2605.00770 | Topological QFI protection | Quantum metrology |
| 2605.00745 | Nanographene simulation + Trotter cancellation | Error mitigation |

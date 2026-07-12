# Neuroscience + Quantum Cron Scan — 2026-06-08

## Papers Scanned

| arXiv | Title | Skill Status |
|-------|-------|-------------|
| 2606.07376 | Measurement circuit ansatz: Naimark vs QNN measurements | Existing: naimark-qnn-measurement-circuits |
| 2606.03517 | Scalable On-Hardware Training of QNNs for Clinical Data | Existing: scalable-on-hardware-qnn-training |
| 2605.29557 | Quantum Subliminal Learning | Existing: quantum-subliminal-learning |
| 2605.28879 | Meta-Quantum Ensemble for Network Intrusion Detection | Existing: meta-quantum-ensemble |
| 2605.25768 | Rethinking Expressibility-Trainability Trade-off in HQNNs | Existing: hqnn-expressibility-trainability-nas |
| 2605.30724 | Research Progress on QNNs and QML | Survey paper, no skill needed |
| 2605.22097 | Q-PhotoNAS: Hybrid Quantum NAS on Photonics | Existing: q-photonas-hybrid-arch-search |

## Key Methodology Additions

### HQNN Expressibility-Trainability Decoupling (2605.25768)
- Pure PQCs: weak, regime-dependent trade-off between expressibility and trainability
- Full hybrid end-to-end training: **eliminates** the trade-off
- Classical components reshape the optimization landscape
- Multi-objective NAS reveals different Pareto-optimal solutions

### Scalable QNN Hardware Training (2606.03517)
- Butterfly circuit architecture: O(n log n) parameters, logarithmic depth
- Layer-wise training: confines optimization to one small layer at a time
- Parallelized parameter-shift: exploits commuting structure
- Validated: IonQ Forte Enterprise 16-qubit training, 32-qubit inference
- Application: MIMIC-III clinical data imputation

### Quantum Subliminal Learning Security (2605.29557)
- QNNs retain hidden-task signal through public-task interface (unlike classical NNs)
- Unified geometric picture: teacher drift magnitude controls transmission
- Security concern for quantum model supply chains

### Q-PhotoNAS on Photonic Devices (2605.22097)
- GA-based NAS for hybrid photonic quantum-classical models
- 19 hyperparameters across 6 gene groups
- 99.44% accuracy on Digits, 98.78% on MNIST
- 67 ms single-image inference projected on Quandela Ascella

## Domain Saturation
Neuroscience+Quantum ~80% saturated. All papers mapped to existing skills.

## Critical Update (2026-06-08)
**scalable-on-hardware-qnn-training** skill was found to describe WRONG methodology — it said "block encoding + Hadamard test" for gradient reduction, but arXiv:2606.03517 actually uses Butterfly circuits + layer-wise training + parallelized parameter-shift rule, reducing from O(n²) to O(log n). The skill was corrected. **Lesson**: Always verify skill methodology against the source paper abstract, not just memory or previous descriptions.

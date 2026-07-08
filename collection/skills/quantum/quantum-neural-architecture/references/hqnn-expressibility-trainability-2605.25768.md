# HQNN Expressibility-Trainability Trade-off Analysis (arXiv: 2605.25768)

## Paper Summary
**Title**: Rethinking Expressibility-Trainability Trade-off in Hybrid Quantum Neural Networks  
**Authors**: Muhammad Kashif, Muhammad Shafique  
**Date**: 2026-05-25

## Key Findings
- **Pure PQCs**: Only weak, regime-dependent expressibility-trainability trade-off
- **Hybrid (quantum-only training)**: Moderate trade-off
- **Hybrid (end-to-end training)**: Trade-off increasingly disrupted and can be eliminated
- **Mechanism**: Classical components reshape the optimization landscape, decoupling trainability from PQC expressibility
- **Multi-objective NAS**: Framework jointly optimizes expressibility, trainability, and task performance across combined classical-quantum design space

## Reusable Patterns

### Training Configuration Comparison Protocol
Always test 3 configurations on the same problem:
1. Pure PQC (quantum-only model, no classical layers)
2. Hybrid with quantum-only training (classical layers frozen)
3. Hybrid with end-to-end training (all parameters trainable)

### Design Space for HQNN NAS
- Circuit depth (2-20 layers), qubit count (4-20), entanglement topology
- Classical layer sizes (32-512 neurons), layer count (1-5), activation functions

### Key Insight
Hybridization is not just an implementation detail — it's a **defining factor** in the performance of quantum machine learning models.

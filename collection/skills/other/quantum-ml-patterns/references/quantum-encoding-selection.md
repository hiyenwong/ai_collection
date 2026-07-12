# Quantum Encoding Selection Framework (arXiv:2606.05387)

**Author**: Vincenzo Sammartino
**Survey**: 66 primary works (2017-2026) via PRISMA-adapted protocol

## Three-Axis Taxonomy

All encoding families classified along:

1. **Cost**: gate depth, qubit count, classical preprocessing
2. **Expressivity**: Fourier expressivity, feature map rank, kernel richness  
3. **Robustness**: noise resilience, barren plateau resistance, kernel concentration

## Encoding Families

| Encoding | Qubits | Depth | Expressivity | NISQ Viable |
|----------|--------|-------|-------------|-------------|
| Basis | D | O(1) | Low | Yes |
| Angle | n | O(n) | Medium | Yes |
| Dense-Angle | n | O(n) | Medium-High | Yes |
| Amplitude | log₂(D) | O(D) | High | Only if p < 10⁻³ |
| Data Re-uploading | n | O(n×L) | Very High | Limited |
| IQP | n | O(n²) | High | Limited |

## Critical Threshold

**p* ~ 10⁻³** gate-error rate: below which amplitude encoding is viable.
For p ≥ 10⁻³ (current NISQ reality), **shallow angle-based encodings consistently outperform amplitude encoding** despite exponential qubit advantage.

## Five-Regime Decision Framework

Map (D, n, p, τ) → encoding recommendation:
1. Low-D, High-p → Basis encoding
2. Medium-D, Medium-p → Angle/dense-angle encoding  
3. High-D, Low-p (< 10⁻³) → Amplitude encoding
4. Complex features, Any-p → Data re-uploading
5. Hardware-aware → IQP encoding when connectivity permits

## Trainability Analysis

Unified treatment: barren plateau onset, quantum kernel concentration, Fourier spectrum gaps — all as functions of encoding circuit.

## Neural Network State Preparation (arXiv:2605.31006)

Complementary approach: train classical NN to map input data → quantum circuit parameters directly.
- **0.992 fidelity** on unseen images
- **5000x runtime reduction** per data instance
- Avoids per-instance variational optimization entirely

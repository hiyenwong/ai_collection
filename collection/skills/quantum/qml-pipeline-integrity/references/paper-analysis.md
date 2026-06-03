# QML-PipeGuard Paper Analysis (arXiv:2605.25066)

## Paper Metadata
- **Title**: QML-PipeGuard: Drift-Aware Behavioral Fingerprinting for Quantum Machine Learning Pipeline Integrity
- **Author**: Esra Yeniaras
- **Date**: May 24, 2026
- **Categories**: quant-ph, cs.CR, cs.LG
- **Pages**: 54 pages, 12 Tables, 5 figures

## Key Contributions

1. **Pipeline-composition treatment** of encoder-ansatz-measurement channel
2. **QML-specific threat model** with tight frame-bound analysis
3. **Finite-shot sample-complexity bound** for practical deployment
4. **Tolerance decomposition** separating adversarial and natural-drift contributions
5. **End-to-end validation** on IBM Heron r2 processor

## Technical Details

### Threat Model
- Adversary controls execution environment
- Can substitute declared quantum channel with behaviorally similar alternative
- Not covered by existing QML verification (pulse noise, input drift, device identity)

### Measurement Family
- Tomographically structured
- Single-qubit: Pauli {X, Y, Z} with frame-bound C=√3
- n-qubit: tensor products
- Informationally complete for channel substitution detection

### Sample Complexity
- ~1.4×10⁴ shots for 2-qubit pipeline
- Fits in single batched job on IBM Heron
- Validated on noise-matched simulator

### Results
- Sneaky channel detected with wide safety margin
- Evades weak (non-informationally-complete) contracts
- Typical hardware drift within tolerance

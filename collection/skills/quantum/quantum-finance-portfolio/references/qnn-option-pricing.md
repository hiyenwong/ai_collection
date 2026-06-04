# QNN Option Pricing on NISQ Hardware — Cross-Platform Benchmark Notes

**Paper**: arXiv:2604.19832 (Zając & Pracht, 2026)
**Title**: Option Pricing on Noisy Intermediate-Scale Quantum Computers: A Quantum Neural Network Approach

## Key Findings

### Architecture
- 2-qubit QNN for BSM option pricing function approximation
- Compact circuit design suitable for current NISQ constraints
- Parameters optimized via hybrid classical-quantum training loop

### Hardware Platforms Tested
| Processor | Type | Key Characteristics |
|-----------|------|---------------------|
| IBM Fez | Superconducting | Falcon-family processor |
| IQM Garnet | Superconducting | European QPU vendor |
| IonQ Forte | Trapped-ion | High connectivity, longer coherence |
| Rigetti Ankaa-3 | Superconducting | Ankaa architecture |

### Results Summary
- **All platforms achieved accurate BSM pricing approximations** despite NISQ noise
- **Hardware-dependent performance**: each platform showed distinct error characteristics
- **Cross-platform consistency**: pricing accuracy maintained across all four devices
- **Viability proven**: QNN approach works for derivative pricing on current hardware

### Extension Potential
- Local volatility models
- Stochastic volatility (Heston framework)
- Interest rate models
- Path-dependent options (Asian, barrier, lookback)
- Multi-asset derivatives

### Implementation Notes
- Loss: MSE between QNN output and true BSM price
- Classical optimizer updates circuit parameters between quantum evaluations
- Encoding maps financial parameters to qubit rotation angles
- Limited shot counts are the primary accuracy bottleneck on NISQ devices

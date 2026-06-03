---
name: qaoa-landscape-audit
description: "QAOA variational landscape audit methodology using Landscape Span Compression (LSC) metric to quantify hardware noise impact on optimization quality and detect barren plateaus in constrained quantum optimization."
---

# QAOA Landscape Audit Methodology

## Description
Systematic methodology for auditing the variational energy landscape of QAOA (Quantum Approximate Optimization Algorithm) under real hardware noise. Uses Landscape Span Compression (LSC) metric to quantify noise-induced landscape flattening, enabling practitioners to diagnose when QAOA will fail before running expensive quantum experiments.

Based on paper: "Noise-Induced Landscape Distortion in QAOA for Constrained Binary Optimization" (arXiv:2604.19426) — empirically validates LSC as a device-agnostic metric on IBM quantum hardware for constrained QUBO problems.

## Activation Keywords
- qaoa landscape audit, qaoa noise analysis, landscape span compression
- qaoa barren plateau detection, quantum noise audit
- variational landscape distortion, QAOA hardware noise
- 量子优化景观审计, QAOA噪声分析, 景观压缩
- qaoa quality assessment, quantum hardware noise impact

## Core Concepts

### Landscape Span Compression (LSC)
```
LSC = 1 - (Observed_Landscape_Span / Ideal_Landscape_Span)
```
- **LSC → 0**: Landscape is intact, noise has minimal impact
- **LSC → 1**: Landscape is flattened, approaching barren plateau
- **Practical threshold**: LSC > 0.7 indicates QAOA likely to fail

### Key Finding from arXiv:2604.19426
- LSC is **device-agnostic** — works across different quantum hardware platforms
- Empirically validated on IBM's `ibm_fez` for three constrained QUBO problems
- Provides **early warning** before running expensive optimization: measure LSC first, skip if too high
- Noise doesn't just add error — it **systematically distorts** the energy landscape geometry

## Tools Used
- exec: Run QAOA circuits, compute LSC metric, benchmark on hardware
- read: Read hardware calibration data, noise profiles
- write: Generate audit reports, landscape visualizations

## Usage Patterns

### Pattern 1: Pre-Run Landscape Audit
Before running QAOA optimization, compute LSC to predict success probability.

### Pattern 2: Hardware Comparison
Compare LSC across different quantum devices to select the best hardware for a given problem.

### Pattern 3: Noise Characterization
Use LSC as a diagnostic tool to understand how specific noise channels affect optimization.

## Instructions for Agents

### Phase 1: Landscape Span Measurement
1. **Define the problem Hamiltonian**: Express the QUBO/constrained optimization as H_C
2. **Sample the landscape**: Evaluate energy at random parameter configurations (θ, γ)
3. **Compute ideal span**: Maximum energy range in noise-free simulation
4. **Compute observed span**: Maximum energy range on actual hardware
5. **Calculate LSC**: `LSC = 1 - (observed_span / ideal_span)`

### Phase 2: Interpretation
| LSC Range | Interpretation | Recommendation |
|-----------|---------------|----------------|
| 0.0 - 0.3 | Landscape intact | Proceed with QAOA optimization |
| 0.3 - 0.7 | Moderate distortion | Use error mitigation, increase shots |
| 0.7 - 0.9 | Severe distortion | Consider classical alternative |
| 0.9 - 1.0 | Near barren plateau | QAOA will likely fail, use classical solver |

### Phase 3: Mitigation Strategies
1. **Error mitigation**: Apply zero-noise extrapolation, readout error correction
2. **Ansatz modification**: Reduce circuit depth, use noise-robust mixing operators
3. **Problem reformulation**: Change constraint encoding to reduce hardware sensitivity
4. **Hardware selection**: Choose device with lowest LSC for the problem class

## Error Handling

### Noisy Calibration Data
- Hardware calibration data changes frequently; use most recent calibration
- If calibration is stale (>24h), re-run small test circuits to estimate current noise level

### LSC Computation Expensive
- Use subsampling: evaluate landscape at O(100) random points instead of full grid
- Classical simulation for ideal span, hardware runs for observed span

## Resources
- arXiv:2604.19426 - "Noise-Induced Landscape Distortion in QAOA for Constrained Binary Optimization"
- IBM Quantum calibration API
- Qiskit Runtime primitives for efficient circuit execution

## Related Skills
- qaoa-xy-mixers-portfolio
- quantum-hybrid-audit
- quantum-neural-barren-plateau
- qbalance-quantum-workflow-optimization

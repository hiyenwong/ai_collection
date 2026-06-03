# QAOA Landscape Audit - Research Notes

## Source Paper
**Title**: Noise-Induced Landscape Distortion in QAOA for Constrained Binary Optimization: Empirical Characterization on IBM Quantum Hardware
**arXiv**: 2604.19426
**Categories**: quant-ph, cs.ET
**Date**: 2026-04-26

## Key Findings

### Landscape Span Compression (LSC)
- **Definition**: LSC = 1 - (Observed_Landscape_Span / Ideal_Landscape_Span)
- **Property**: Device-agnostic metric for quantifying hardware noise impact
- **Intuition**: Measures how much noise flattens the energy landscape
- **LSC → 1**: Landscape collapses toward barren plateau

### Experimental Validation
- **Hardware**: IBM's `ibm_fez` quantum processor
- **Problems**: Three constrained QUBO instances
- **Method**: Compare energy landscape on hardware vs noise-free simulation
- **Result**: LSC reliably predicts QAOA optimization success/failure

### Practical Impact
1. **Pre-run diagnostic**: Compute LSC before expensive QAOA optimization runs
2. **Hardware selection**: Choose device with lowest LSC for problem class
3. **Resource saving**: Skip runs where LSC > 0.7 (high failure probability)
4. **Noise characterization**: Understand which noise channels distort landscape most

## Connection to Portfolio Optimization
- QAOA is used for portfolio optimization (see arXiv:2605.06858, 2605.17623)
- LSC audit can predict when QAOA-based portfolio optimization will fail on real hardware
- Complements the hybrid audit methodology (quantum-hybrid-audit skill)

## Related Papers
- arXiv:2605.06858 - Constrained Counterdiabatic QAOA for Portfolio Optimization
- arXiv:2605.17623 - Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- arXiv:2605.02465 - Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution

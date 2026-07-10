# CVaR Portfolio Optimization on NISQ: Benchmark Patterns (arXiv: 2606.07727)

## Paper Summary
**Title**: Benchmarking Quantum Algorithmic Resilience for CVaR Portfolio Optimization: The Expressibility-Coherence Trade-off  
**Authors**: Prashik N. Somkuwar, K. Srinivasan, G. Raghavan  
**Date**: 2026-06-05

## Key Findings
- **SWAP Tax**: WS-QAOA provides exact theoretical mapping but suffers catastrophic hardware decoherence due to exponential nonlocal gate overhead on IBM heavy hex topology
- **HE-VQNN**: Preserves hardware coherence but lacks mathematical expressibility to capture dense tail risk asset correlations
- **Novel Technique**: Classical-quantum hybrid proxy matrix to bypass CVaR auxiliary qubit bottleneck
- **Scale**: Maps up to 16 assets from NIFTY 50 onto IBM heavy hex processor
- **Fundamental Limitation**: NISQ computers without all-to-all connectivity face nonviable choice between algorithmic inexpressibility and hardware decoherence

## Reusable Patterns

### 1. CVaR Proxy Matrix Pattern
Instead of encoding all CVaR auxiliary variables on quantum hardware (which requires extra qubits), compute tail-risk correlations classically and use as proxy input to QPU.

### 2. SWAP Tax Quantification Protocol
Count required SWAP operations for target circuit on given hardware topology, estimate decoherence impact as additional depth / T1 time ratio.

### 3. Expressibility-Coherence Trade-off Analysis
Measure both algorithmic expressibility (Hilbert space coverage) and hardware coherence consumption (circuit depth × gate count / T1) to predict whether an algorithm is viable on target hardware.

## Pitfalls
- WS-QAOA may produce meaningless results on NISQ due to decoherence
- HE-VQNN may miss important tail-risk correlations in dense covariance matrices
- Heavy hex topology significantly limits which asset pairs can be directly coupled
- Current NISQ devices cannot outperform classical solvers for this problem class

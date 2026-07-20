# 2026-06-06 Quantum Finance Session Notes

## arXiv Papers Reviewed

### 2604.08180 - Quantum Computing for Financial Transformation: A Review
- 134-page comprehensive review across five domains
- Proposes unified evaluation framework: bottleneck → quantum primitive → classical benchmark → realistic constraints
- Key finding: hybrid workflows strongest near-term case, not blanket quantum advantage
- Post-quantum cryptography must be deployed NOW for financial infrastructure

### 2510.11153 - Hot-Starting Quantum Portfolio Optimization
- Restricts search to discrete solutions near continuous optimum via compact Hilbert space
- Reduces qubit requirements, improves solution quality
- Outperforms SOTA on D-Wave Advantage annealer
- Works with smooth convex objective + integer trading constraints

### 2510.05475 - From Classical Rationality to Contextual Reasoning: Quantum Logic for AI in Finance
- Quantum logic applications in financial AI modeling
- Advocates quantum-inspired neural networks for finance

### 2602.21350 - The Inverse Born Rule Fallacy
- Naive amplitude encoding (psi=sqrt(P)) makes representations phase-deaf
- Advocates Dynamical Hamiltonian Encoding (DHE) for non-commutative data evolution

### 2604.25644 - Efficient Complex-Valued State Preparation on Bucket Brigade QRAM
- O(log²(MN)) BBQRAM query complexity for complex-valued matrices
- Reduces QPU to retrievals + controlled-rotation cascades

## Key New Patterns

1. **Five-Domain Stack**: Evaluate quantum finance across unified stack, not isolated demos
2. **Hot-Starting**: Compact Hilbert space near continuous optimum reduces qubit count
3. **Amplitude Encoding Trap**: sqrt(P) encoding loses non-commutative structure needed for advantage
4. **Hybrid Workflow**: Classical pre → quantum refine → classical post is the winning pattern

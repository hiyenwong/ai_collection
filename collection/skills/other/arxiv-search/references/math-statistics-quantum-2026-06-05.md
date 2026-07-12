# Math + Statistics + Quantum Dual-Keyword Scoring (Verified 2026-06-05 — Friday)

## Session Summary
- RSS Feed: `quant-ph+stat.ME+stat.ML+math.NT+math.PR+math.ST`
- Total papers parsed: 276
- Dual-keyword scoring: math_score + 2×quantum_score
- High-score papers (≥10): 12
- Newly imported to kg.db: 6
- New skills created: 3

## Keyword Sets (Verified 2026-06-05)

### Math Keywords (43 terms)
```
number theory, statistics, probability, matrix, lattice, optimization, estimation,
distribution, algorithm, theorem, conjecture, bound, random matrix, bayesian, gaussian,
entropy, linear algebra, eigenvalue, eigenvector, topological, homology, tensor,
coding theory, information theory, persistent homology, betti number, stochastic,
markovian, calculus, algebra, geometry, analysis, convergence, polynomial, spectral,
approximation, kernel, inference, variance, covariance, regression, classification,
prime, factorization, shor, modular form, diophantine
```

### Quantum Keywords (28 terms)
```
quantum, qubit, entanglement, superposition, hamiltonian, gate, fidelity, decoherence,
phonon, fermionic, boson, bosonic, fermion, spin, operator, eigenstate, wavefunction,
density matrix, trace, measurement
```

## Top Papers by Score (2026-06-05)
| Score | arXiv ID | Title | Math | Quantum |
|-------|----------|-------|------|---------|
| 18 | 2606.05066 | Fermionic non-Gaussianity via Bell sampling | 6 | 6 |
| 15 | 2605.29242 | Hybrid Gaussian-exponential ZNE | 5 | 5 |
| 14 | 2606.04786 | ADAPT-VQE operator selection | 2 | 6 |
| 14 | 2606.05060 | Low-rank Hessian optimization | 2 | 6 |
| 13 | 2606.04353 | Spectral Fusion spin chains | 5 | 4 |
| 13 | 2412.19119 | Multiparameter estimation SU(2)/SU(1,1) | 1 | 6 |
| 12 | 2606.04070 | Quantum circuit partition maze | 4 | 4 |
| 12 | 2606.04794 | Monitored chaotic scattering | 4 | 4 |

## Skills Created
1. `hybrid-qnz-zero-noise-extrapolation` (2605.29242) - NISQ error mitigation
2. `spectral-fusion-quantum-state-transfer` (2606.04353) - Spin chain state transfer
3. `monitored-chaotic-scattering-rmt` (2606.04794) - RMT monitored scattering

## Parser Notes
- RSS XML uses `<description>` tag with "Abstract:" prefix for abstract text
- Extract via regex: `r'Abstract:\s*(.*)'`
- Categories from `<category>` tags (multiple per item possible)
- Authors from `<dc:creator>` tag
- arXiv ID from `<link>` via regex: `r'arxiv\.org/abs/([^\s/]+)'`
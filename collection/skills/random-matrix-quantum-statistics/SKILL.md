---
name: random-matrix-quantum-statistics
description: |
  Random matrix theory (RMT) methodology for analyzing quantum impurity models and
  disordered quantum systems. Uses ensemble statistics (GOE, GUE, GSE) to derive
  charge distributions, spectral properties, and universal power-law behaviors.
  Triggers: random matrix theory, quantum impurity, disordered quantum, GOE, GUE,
  Gaussian orthogonal ensemble, charge distribution, spectral statistics, universal
  power-law, 随机矩阵理论, 量子杂质模型
---

# Random Matrix Theory for Quantum Statistics

## Core Framework

### Quantum Impurity Models

Hybridize a localized electronic level with a bath of random fermions:
```
H = epsilon * d†d + sum_k epsilon_k * c†_k c_k + sum_k (V_k * d†c_k + h.c.)
```

### Statistical Ensembles

- **GOE** (Gaussian Orthogonal Ensemble): Time-reversal symmetric systems
- **GUE** (Gaussian Unitary Ensemble): Broken time-reversal symmetry
- **GSE** (Gaussian Symplectic Ensemble): Time-reversal + spin-rotation symmetry

### Key Findings from arXiv:2507.22586

1. **Crossover Behavior**:
   - Large hybridization -> Gaussian charge distribution (centered at 1/2)
   - Small hybridization -> Bimodal distribution (peaks at 0 and 1)

2. **Universal Power-Law**:
   - Bimodal regime exhibits (-3/2) power-law behavior
   - Derivable from single random electron level approximation

3. **Exact Results**:
   - Functional integral for general PDF of eigenvalues/eigenstates
   - Exact RMT solution in N->infinity limit for Gaussian regime

## Methodology

### Numerical Sampling
1. Generate random matrix ensemble
2. Compute hybridization spectrum
3. Sample charge distribution numerically
4. Identify crossover regimes

### Analytic Surmise
1. Single-level approximation in bimodal regime
2. Derive power-law exponents analytically
3. Compare with numerical results

### Functional Integral Approach
1. Write exact functional integral for PDF
2. Take large-N limit
3. Solve analytically in applicable regimes

## When to Use

- Analyzing disordered quantum systems statistically
- Computing charge/spin distributions in impurity models
- Studying universal spectral statistics
- Understanding quantum-to-classical crossovers
- Mesoscopic device theory and quantum dots

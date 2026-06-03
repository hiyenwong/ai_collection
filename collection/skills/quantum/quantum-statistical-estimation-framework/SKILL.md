---
name: quantum-statistical-estimation-framework
description: Framework for quantum statistical estimation theory combining quantum Fisher information, quantum Cramér-Rao bounds, and Bayesian quantum estimation. Bridges quantum mechanics with statistical inference for parameter estimation in quantum systems.
category: quantum
tags: [quantum-mechanics, statistics, estimation-theory, fisher-information, quantum-sensing, metrology]
created: "2026-05-30"
---

# Quantum Statistical Estimation Framework

## When to use
- Estimating parameters of quantum states or processes
- Designing quantum sensors and metrology protocols
- Computing quantum Cramér-Rao bounds
- Analyzing quantum Fisher information
- Bayesian quantum state estimation
- Multi-parameter quantum estimation problems

## Core Methodology

### 1. Quantum Fisher Information (QFI)

For a family of quantum states $ho_	heta$ parameterized by $	heta$:

**Pure states:** $F_Q = 4(\langle \partial_	heta \psi | \partial_	heta \psi angle - |\langle \partial_	heta \psi | \psi angle|^2)$

**Mixed states:** $F_Q = \sum_{i,j} rac{2}{\lambda_i + \lambda_j} |\langle i | \partial_	heta ho | j angle|^2$

where $\lambda_i$ and $|iangle$ are eigenvalues and eigenvectors of $ho_	heta$.

### 2. Quantum Cramér-Rao Bound

For any unbiased estimator $\hat{	heta}$:
$$	ext{Var}(\hat{	heta}) \geq rac{1}{n F_Q}$$

where $n$ is the number of independent measurements.

### 3. Multi-Parameter Estimation

For parameter vector $ec{	heta} = (	heta_1, \ldots, 	heta_k)$:
- Quantum Fisher Information Matrix (QFIM): $[F_Q]_{ij}$
- Matrix CRB: $	ext{Cov}(\hat{ec{	heta}}) \geq F_Q^{-1}/n$
- Compatibility conditions for simultaneous estimation

### 4. Bayesian Quantum Estimation

**Framework:**
1. Prior distribution $p(	heta)$
2. Likelihood from measurement outcomes $p(m|	heta)$
3. Posterior via Bayes: $p(	heta|m) \propto p(m|	heta)p(	heta)$
4. Optimal estimator: minimize expected cost

### 5. Computational Pipeline

```python
import numpy as np
from scipy.linalg import eig, svd

def compute_qfi_pure(psi, d_psi_dtheta):
    """QFI for pure state"""
    term1 = np.vdot(d_psi_dtheta, d_psi_dtheta).real
    term2 = np.abs(np.vdot(d_psi_dtheta, psi))**2
    return 4 * (term1 - term2)

def compute_qfi_mixed(rho, drho_dtheta, eps=1e-12):
    """QFI for mixed state via spectral decomposition"""
    vals, vecs = eig(rho)
    vals = vals.real
    n = len(vals)
    qfi = 0.0
    for i in range(n):
        for j in range(n):
            if vals[i] + vals[j] > eps:
                matrix_elem = vecs[:, i].conj() @ drho_dtheta @ vecs[:, j]
                qfi += 2 * np.abs(matrix_elem)**2 / (vals[i] + vals[j])
    return qfi.real

def quantum_cramer_rao_bound(qfi, n_measurements=1):
    """Minimum variance bound"""
    return 1.0 / (n_measurements * qfi)

def bayesian_update(prior, likelihood, grid):
    """Bayesian posterior update"""
    posterior = prior * likelihood
    posterior /= np.sum(posterior)
    return posterior
```

## Verification Steps
1. Check QFI positivity: $F_Q \geq 0$ always
2. Verify CRB is achievable (asymptotically)
3. For multi-parameter: check QFIM positive definiteness
4. Compare with classical Fisher information: $F_Q \geq F_C$ for any measurement
5. Validate Bayesian posterior normalization

## Pitfalls
- Multi-parameter QFI bounds may not be simultaneously achievable
- Non-commuting observables create fundamental trade-offs
- Mixed state QFI computation is numerically sensitive to small eigenvalues
- Asymptotic bounds may not hold for small sample sizes
- Prior choice in Bayesian estimation significantly impacts results

## Related Work
- Quantum metrology and sensing
- Quantum hypothesis testing
- Quantum tomography
- Variational quantum sensing

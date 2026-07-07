---
name: qmaxcal-open-quantum-control
description: "Path-space regularization for open quantum control using Girsanov's theorem. Use when designing quantum control policies under decoherence, computing trajectory likelihood ratios for monitored quantum systems, or optimizing open quantum system control via stochastic path integrals. Combines Girsanov change-of-measure with quantum trajectory theory for differentiable KL divergence estimation."
metadata:
  arxiv_id: "2606.19947"
  published: "2026-06-18"
  authors: "Merijn Moody, Zier Mensch, Miranda C. N. Cheng, Peter G. Bolhuis, Max Welling"
---

# QMaxCal: Path-Space Regularization for Open Quantum Control

## Core Concept

Open quantum systems under continuous monitoring produce classical measurement records. Two trajectories sharing the same decoherence channels differ only in drift, so **Girsanov's theorem** yields a closed-form differentiable estimator of the KL divergence between trajectory distributions. This enables **path-space regularization** — penalizing control policies that deviate too far from noise-resilient trajectories.

## Mathematical Framework

Given two quantum trajectories with measurement records y_1(t) and y_2(t):

1. **Drift difference**: dy = (h_1 - h_2)dt + dW where h_i are measurement expectations
2. **Girsanov density**: dP_1/dP_2 = exp(integral (h_1-h_2)/sigma dW - 1/2 integral (h_1-h_2)^2/sigma^2 dt)
3. **KL divergence**: D_KL(P_1 || P_2) = 1/2 E_1[integral (h_1-h_2)^2/sigma^2 dt]
4. **Regularization term**: Add lambda * D_KL to control cost function

## Usage Patterns

### Pattern 1: Quantum Trajectory Likelihood Ratio
Compute likelihood ratio between controlled and uncontrolled quantum trajectories using Girsanov density. Useful for importance sampling in quantum control optimization.

### Pattern 2: Path-Space Regularized Control
Add KL regularization to quantum control cost:
- Define reference policy (e.g., noise-aware baseline)
- Compute trajectory KL via Girsanov
- Optimize: minimize E[cost] + lambda * D_KL(pi || pi_ref)

### Pattern 3: Decoherence-Robust Policy Design
Design control policies resilient to environmental noise:
1. Characterize decoherence channel (Lindblad operators)
2. Generate trajectory ensemble under noise
3. Compute Girsanov-based KL for candidate policies
4. Select policy minimizing regularized cost

## Step-by-Step Workflow

1. **Model the open quantum system**: Define Hamiltonian H and Lindblad operators L_k
2. **Generate quantum trajectories**: Use quantum trajectory Monte Carlo (QTMC) or stochastic master equation
3. **Compute measurement records**: Extract classical signals from continuous monitoring
4. **Apply Girsanov transform**: Compute Radon-Nikodym derivative between trajectory measures
5. **Estimate KL divergence**: Use sample average of log-likelihood ratios
6. **Optimize control policy**: Gradient descent on regularized objective

## Key Insights

- **Differentiable**: Girsanov KL is differentiable w.r.t. control parameters — enables gradient-based optimization
- **Channel-agnostic**: Works for any Markovian decoherence channel
- **No simulation needed**: KL computed directly from measurement records, not from full density matrix evolution
- **Scalable**: Computational cost scales with trajectory length, not Hilbert space dimension

## Pitfalls

- **Markovian assumption**: Girsanov requires Markovian noise — non-Markovian environments need extensions
- **Importance sampling collapse**: Large KL values cause high-variance estimates — use control variates
- **Continuous monitoring requirement**: Method assumes continuous weak measurement, not projective measurements

**Activation**: qmaxcal, girsanov quantum control, path-space regularization, quantum trajectory KL, open quantum system control, stochastic quantum control, decoherence-aware policy, quantum trajectory Monte Carlo

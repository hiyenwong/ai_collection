---
name: tensor-network-many-body-trace-norms
description: "Tensor-network algorithm for estimating trace norms of matrix product operators (MPOs) without full diagonalization. Combines Zolotarev's rational approximation to the sign function with a variational formulation for controlled approximation of many-body quantum information quantities. arXiv:2606.11882"
category: "quantum-computing"
metadata:
  arxiv_id: "2606.11882"
  authors: "Seunghun Lee, Eun-Gook Moon"
  published: "2026-06-10"
---

## Context

Trace norms are fundamental to quantum information theory (entanglement measures, distinguishability, fidelity bounds), but their evaluation in many-body systems requires diagonalizing exponentially large operators. This paper introduces a controlled tensor-network algorithm for estimating trace norms of matrix product operators (MPOs) without full diagonalization.

## Core Methodology

1. **Zolotarev rational approximation**: Approximates the sign function sgn(H) using optimal rational functions with exponentially convergent error
2. **Variational formulation**: Combines rational approximation with a variational principle to bound the trace norm
3. **Controlled approximation**: The bond dimension of intermediate MPOs determines approximation quality — increasing bond dimension systematically improves accuracy
4. **No full diagonalization**: Avoids the O(e^N) scaling of exact diagonalization by working entirely in MPO representation

## Implementation Steps

1. Represent the target operator as a matrix product operator (MPO)
2. Apply Zolotarev rational approximation: sgn(H) ≈ Σ_k c_k (H + d_k I)^{-1}
3. Implement each inverse term using variational MPO optimization
4. Combine terms to estimate trace norm ||H||_1 = Tr|H|
5. Control accuracy via bond dimension of intermediate MPOs

## Pitfalls

- **Bond dimension explosion**: Intermediate MPOs during rational approximation can have large bond dimensions
- **Convergence rate**: Zolotarev approximation convergence depends on spectral gap of the operator
- **Numerical stability**: Inverse operations (H + d_k I)^{-1} may be ill-conditioned for small eigenvalues

## Verification

- Test against exactly diagonalizable small systems (N ≤ 20 qubits)
- Verify trace norm estimates converge monotonically with increasing bond dimension
- Compare with known analytical results for simple operators

## Activation

tensor network, trace norm, matrix product operator, MPO, Zolotarev approximation, sign function, many-body quantum information

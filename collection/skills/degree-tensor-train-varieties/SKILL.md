---
name: degree-tensor-train-varieties
description: "Integral geometry methodology for computing degrees of tensor train varieties — tensors arising in quantum many-body physics and machine learning. Provides combinatorial expressions and ready-to-use Julia package TTVarietyDegree.jl. arXiv:2606.11847"
category: "mathematics"
metadata:
  arxiv_id: "2606.11847"
  authors: "Andrea Rosana, Otto T. P. Schmidt"
  published: "2026-06-10"
---

## Context

Tensor train varieties — algebraic varieties of tensors admitting a tensor train (matrix product state) decomposition with bounded ranks — arise in quantum many-body physics and machine learning. Computing their degree (the number of intersection points with a generic linear space of complementary dimension) is important for understanding the complexity and geometry of these tensor formats.

## Core Methodology

1. **Integral geometry approach**: Uses classical results from algebraic geometry (Chern classes, Schubert calculus) to derive degree formulas
2. **Combinatorial expression**: The degree is expressed as a combinatorial function of the tensor train ranks and dimensions
3. **Julia package**: TTVarietyDegree.jl provides ready-to-use computation
4. **Applications**: Results apply to quantum many-body physics (MPS varieties) and machine learning (tensor train decompositions)

## Implementation Steps

1. Identify tensor train ranks (r_1, r_2, ..., r_{d-1}) and mode dimensions (n_1, n_2, ..., n_d)
2. Apply combinatorial formula from paper to compute degree
3. Use TTVarietyDegree.jl Julia package for direct computation
4. Interpret degree as complexity measure for optimization on tensor train varieties

## Pitfalls

- **Combinatorial explosion**: Degree grows rapidly with rank and dimension
- **Numerical overflow**: For large parameters, exact combinatorial computation may overflow

## Verification

- Compare against known results for matrix varieties (d=2 case)
- Verify TTVarietyDegree.jl output matches hand-computed examples for small dimensions
- Cross-validate degree with random linear section counting

## Activation

tensor train, integral geometry, degree computation, algebraic geometry, MPS variety, tensor network geometry, TTVarietyDegree

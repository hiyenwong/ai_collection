---
name: gqsp-hermitian-embedding-pricing
description: Generalised Quantum Signal Processing with Hermitian block embedding for solving 2D Black Scholes equation. Based on arXiv:2606.00458 — quantum linear algebra for option pricing.
category: quantum
trigger_words: quantum signal processing, GQSP, hermitian block embedding, Black Scholes, option pricing, non-Hermitian operator
arxiv_id: 2606.00458v1
---

# GQSP with Hermitian Block Embedding for Financial PDEs

## Overview
Methodology for applying Generalised Quantum Signal Processing (GQSP) to non-Hermitian matrix problems via Hermitian block embedding, demonstrated on the 2D Black Scholes equation for financial derivatives pricing.

## Problem
- Black Scholes equation → finite difference discretisation → non-Hermitian time step matrix
- GQSP requires Hermitian or unitary form for polynomial transformations
- Direct application to non-Hermitian operators impossible

## Solution: Hermitian Block Embedding
- Embed non-Hermitian matrix into larger Hermitian block structure
- Enables GQSP polynomial transformations on the embedded form
- Matrix inverse (for pricing) computed via polynomial approximation

## Results
- Two-asset European call options pricing
- Close agreement with classical backward Euler finite difference
- Accurately captures dynamics of original non-Hermitian operator

## Workflow
1. Discretise PDE → obtain non-Hermitian matrix A
2. Construct Hermitian block embedding H of A
3. Apply GQSP polynomial transformation to H
4. Extract solution from embedded result
5. Validate against classical methods

## When to Use
- Quantum algorithms for financial PDEs
- Non-Hermitian operator processing via GQSP
- Multi-asset option pricing
- Matrix function evaluation for non-normal matrices

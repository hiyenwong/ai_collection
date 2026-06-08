---
name: subspace-equality-hypothesis-testing
description: "Two-Sample Hypothesis Testing for Subspace Equality in Network Data - methodology for stat.ME; math.ST applications"
category: "math-statistics-quantum"
source_paper: "arXiv:2606.06482"
---

# Two-Sample Hypothesis Testing for Subspace Equality in Network Data

**arXiv**: 2606.06482
**Authors**: Rajdeep Brahma, Joshua Agterberg, Yuguo Chen
**Category**: stat.ME; math.ST
**Published**: 2026-06-04

## Abstract

In many settings one is often interested in determining whether two networks share some joint structural connectivity patterns such as communities. However, while communities may be shared across networks, edge probabilities may differ significantly. Therefore, in this paper we consider testing a general null hypothesis that two networks have the same underlying subspace, which in particular includes the setting that communities are the same for either stochastic blockmodels or mixed-membership stochastic blockmodels (even if edge probabilities are different). We propose a test statistic based on the Frobenius norm of the difference of the leading subspace projection matrices, and we prove that our test statistic, after appropriate centering and scaling, converges in distribution to a Gaussian random variable as long as the average expected degree grows at least logarithmically in the number of vertices. We then provide estimators for the asymptotic mean and variance and show consistency under a stronger signal condition, and we give the local power of our test when the networks are sufficiently dense. Our theoretical results are based on a limit theorem for the projection difference of empirical and true eigenvectors which can also be viewed as the one-sample version of our test statistic.

## Core Methodology

### Key Results

- Paper presents novel methodology for stat.ME; math.ST
- Mathematical framework with rigorous proofs
- Applications to related computational problems

### Implementation Steps

1. Study the theoretical framework presented in the paper
2. Implement the core algorithm/methodology
3. Validate against benchmark datasets
4. Apply to real-world use cases

## Pitfalls

- Ensure proper handling of edge cases in mathematical formulations
- Verify numerical stability for large-scale implementations
- Check boundary conditions in theoretical proofs

## Verification

- Run unit tests on core methodology
- Compare results with paper's reported values
- Validate on independent datasets

## Activation

**Keywords**: two-sample hypothesis testing for subspace


---
name: bayesian-membership-inference-attack
description: "Bayesian decision-making framework for membership inference attacks on statistical releases using Bayesian network population models. Reframes membership inference with respect to populations represented as Bayesian networks, enabling more effective specialized attacks by incorporating prior information about attribute dependency structures. Use when analyzing statistical disclosure risk, designing membership inference attacks, or evaluating privacy of released statistics."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30203"
  published: "2026-05-28"
  authors: "Lisa Oakley, Sam Stites, Cameron Moy, Steven Holtzen, Alina Oprea, Marco Gaboardi"
  tags: [membership-inference, bayesian-networks, privacy, statistical-disclosure, probabilistic-programming]
---

# Bayesian Membership Inference Attacks

## Overview

Membership inference methodology that models population attribute dependencies via **Bayesian networks** rather than just marginals, enabling more effective attacks when the attacker has structural prior knowledge about the population (e.g., from multiple data sources like Census + IRS).

## Core Framework

### Bayesian Decision-Making for Membership Inference

1. **Reframe problem**: Population represented as Bayesian network (BN) capturing attribute dependencies
2. **Incorporate priors**: Attacker uses structural knowledge from similarly-structured external data
3. **Bayesian posterior**: Compute posterior membership probability using probabilistic programming
4. **Optimal attack**: Equivalent to optimal likelihood ratio test for populations with strong attribute dependency

### Implementation Pattern

1. Model population as Bayesian network with dependency structure
2. Encode BN in probabilistic programming language (e.g., Roulette)
3. Compute Bayesian posterior for membership hypothesis
4. Compare against baseline attacks (likelihood ratio test, inner product attack)

### Key Advantage

Existing marginal-based attacks fail on complex dependency structures. The BN approach:
- Outperforms LRT and inner product attacks on 5 commonly used BNs
- Handles dependencies too complex for manual attack adaptation
- Leverages cross-source structural knowledge (e.g., Census + IRS)

## When to Use

- Evaluating privacy of statistical releases with correlated attributes
- Designing membership inference attacks with structural priors
- Auditing DP mechanisms against structure-aware attackers
- Privacy analysis when multiple data sources share population structure

## Pitfalls

- Requires accurate BN structure (wrong dependencies = worse than LRT)
- Computationally expensive for high-dimensional BNs
- Probabilistic programming inference may not scale to large datasets

---

*Reference: Oakley et al. (2026) "A Bayesian Approach to Membership Inference for Statistical Release" arXiv:2605.30203*

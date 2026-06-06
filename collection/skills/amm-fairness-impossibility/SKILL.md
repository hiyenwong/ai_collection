---
name: amm-fairness-impossibility
description: "Arrovian impossibility theorem for Automated Market Maker (AMM) design. Proves no aggregation rule for weighted-product AMMs can be simultaneously fair and strategy-proof when n>2 liquidity providers. Key result: fairness forces mean-type aggregation (weighted Aitchison centroid) while strategy-proofness forces median-type; only single-provider dictatorship satisfies both. Obstruction vanishes at n=2. Applies to DeFi protocol design, mechanism design, and prediction markets. (arXiv: 2606.04959)"
tags: ["economics", "game-theory", "defi", "mechanism-design", "market-makers"]
category: economics
---

## Context

This methodology comes from arXiv:2606.04959 "Fairness and Strategy-Proofness in Automated Market Makers" by Frank M. V. Feys (June 2026, 52 pages). The paper establishes a fundamental impossibility result for Automated Market Maker (AMM) design in decentralized finance (DeFi).

## Core Finding: The AMM Impossibility Theorem

**No deployed AMM lets liquidity providers (LPs) vote on the trading function. This is structural, not an oversight.**

On the weighted-product family with n assets:
- **No aggregation rule is simultaneously fair AND strategy-proof** when n > 2
- **Arrovian fairness** forces a unique form: the weighted Aitchison centroid (weighted geometric mean of LPs' preferred pools)
- **Fairness forces mean-type aggregation** while **strategy-proofness forces median-type aggregation**
- The only rule satisfying both is **single-provider dictatorship**
- **The obstruction is sharp**: it vanishes at n=2, where a fair strategy-proof rule exists

## Key Mathematical Results

### 1. Fairness → Weighted Aitchison Centroid
- Under Arrovian fairness (unanimity, scale-invariance, independence of irrelevant alternatives), the unique aggregation rule is the weighted geometric mean of providers' preferred pools
- This is the **weighted Aitchison centroid** in compositional data analysis
- Under the Frongillo–Papireddygari–Waggoner equivalence, the centroid corresponds to **Genest's logarithmic opinion pool**

### 2. Strategy-Proofness → Median-Type Aggregation
- Strategy-proofness (no LP can benefit from misreporting preferences) forces median-type aggregation
- Mean-type and median-type aggregation are fundamentally incompatible for n > 2

### 3. The Impossibility Transfer
- The impossibility transfers to **externally Bayesian pooling** via the Frongillo–Papireddygari–Waggoner equivalence theorem
- This connects AMM design to the broader literature on opinion aggregation and belief pooling

### 4. The n=2 Exception
- When there are exactly 2 LPs (n=2), the obstruction vanishes
- A fair, strategy-proof rule exists for 2-provider AMMs

## Implementation Steps

### Step 1: Identify the AMM Family
- Determine if the AMM uses weighted-product trading functions (e.g., Uniswap v3, Balancer)
- Weighted-product family: ∏(x_i^w_i) = k, where x_i are reserves and w_i are weights

### Step 2: Count Liquidity Providers
- If n = 2 LPs: fair strategy-proof rules exist → proceed with design
- If n > 2 LPs: impossibility holds → must choose between fairness and strategy-proofness

### Step 3: Choose Trade-off Strategy
**Option A: Prioritize Fairness (recommended for DeFi protocols)**
- Implement weighted Aitchison centroid aggregation
- Accept that LPs may have incentives to misreport preferences
- Use reputation systems or stake-weighted voting to mitigate manipulation

**Option B: Prioritize Strategy-Proofness**
- Implement median-type aggregation
- Accept that some LPs' preferences may be systematically underrepresented
- Use rotation mechanisms to ensure long-term representation

**Option C: Restrict to n=2**
- Design AMMs with exactly 2 LPs or 2 LP groups
- Achieve both fairness and strategy-proofness
- Practical for bilateral trading venues

### Step 4: Design Governance Mechanism
- If using centroid aggregation (Option A), implement:
  - Stake-weighted preference submission
  - Time-weighted preference aggregation (prevent flash preference attacks)
  - Preference smoothing to reduce manipulation incentives

### Step 5: Verify Properties
- Check: Does the aggregation rule satisfy unanimity?
- Check: Is the rule scale-invariant?
- Check: Does the rule satisfy IIA (independence of irrelevant alternatives)?
- Check: Is the rule strategy-proof (or accept it isn't)?

## Pitfalls

- **Assuming fairness and strategy-proofness are compatible**: They are not for n > 2 LPs on weighted-product AMMs
- **Ignoring the n=2 exception**: Two-provider AMMs CAN be both fair and strategy-proof
- **Confusing weighted-product with other AMM families**: This impossibility applies specifically to weighted-product family (Constant Product, Constant Sum, etc.)
- **Not considering the Frongillo–Papireddygari–Waggoner equivalence**: This equivalence transfers impossibility to externally Bayesian pooling, affecting broader mechanism design
- **Overlooking Genest's logarithmic opinion pool connection**: The centroid is mathematically equivalent to this pooling method, with known properties and limitations

## Verification

1. For any proposed AMM aggregation rule on weighted-product family with n > 2 LPs:
   - Verify it satisfies Arrovian fairness axioms → it must be the weighted Aitchison centroid
   - Verify it is strategy-proof → it must be median-type aggregation
   - Since centroid ≠ median-type for n > 2, both cannot hold simultaneously

2. For n = 2 LPs:
   - Verify existence of fair, strategy-proof rule
   - The obstruction vanishes at exactly 2 providers

## Activation

AMM design, automated market maker, DeFi protocol, liquidity provider voting, fairness in DeFi, strategy-proof mechanism, Arrovian impossibility, Aitchison centroid, opinion pooling, mechanism design, game theory, weighted-product AMM, Uniswap governance, Balancer governance, prediction market design, externally Bayesian pooling

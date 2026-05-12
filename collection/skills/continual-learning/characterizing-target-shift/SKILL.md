---
name: characterizing-target-shift
description: "Online kernel regression effective target shift theory and correction. Proves online learning is equivalent to offline learning with shifted targets, derives label correction to achieve offline-optimal performance. Use when: online learning, continual learning with distribution shift, target shift correction, kernel regression analysis, EWA equivalence."
---

# Characterizing and Correcting Effective Target Shift

## Core Insight

Online kernel regression is mathematically equivalent to offline kernel regression with **shifted, inaccurate target outputs**. The online predictor only uses the strictly upper-triangular part of the Gram matrix (no access to future samples).

## Key Theorems

**Theorem 3.2**: Online kernel regression ≡ offline kernel regression on corrected targets (X_n, Y_n^e)

**Theorem 4.1**: Using corrected targets Y_n^c for online learning ≡ using original targets for offline learning.

## Practical Application

For continual learning scenarios:
1. Identify target shift in your streaming data
2. Apply iterative target correction: Z_new = Y_new + (Y_new - f_on) * C_on + (f_off - Y_new) * C_off
3. C_on controls online error modulation; C_off injects offline structure

## Paper

- Li & Hiratani, arXiv:2605.07886, 2026

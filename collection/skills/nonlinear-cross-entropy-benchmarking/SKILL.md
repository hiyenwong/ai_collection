---
name: nonlinear-cross-entropy-benchmarking
description: "Sample-efficient quantum advantage benchmarking using nonlinear cross-entropy and heavy output generation classifiers. Use when: (1) benchmarking NISQ quantum circuits, (2) distinguishing quantum computers from classical spoofers, (3) designing quantum advantage experiments, (4) analyzing random circuit sampling results, (5) evaluating shallow-depth quantum circuits."
metadata:
  arxiv_id: "2605.22909"
  published: "2026-05-21"
  authors: "Gregory Bentsen, Bill Fefferman, Soumik Ghosh, Michael J. Gullans, Yinchen Liu"
  tags: [quantum, benchmarking, quantum-advantage, cross-entropy, nisq]
---

# Nonlinear Cross-Entropy Benchmarking

## Description

Benchmarking methodology for demonstrating quantum advantage using nonlinear cross-entropy and heavy output generation classifiers. Addresses the limitation of linear cross-entropy benchmarks that can be classically spoofed in noisy NISQ devices.

## Core Problem

Linear cross-entropy benchmarking (XEB) for random circuit sampling has been classically spoofed due to noise. In shallow-depth regimes where sampling is plausibly classically intractable, no existing benchmark can distinguish noisy quantum computers from classical spoofers.

## Methodology

### Nonlinear Cross-Entropy Score

Nonlinear XEB provides a sample-efficient benchmark whose score cleanly separates noisy quantum computers from classical spoofers, even under depolarizing noise.

**Key insight**: The nonlinear score is more robust to noise-induced degradation than linear XEB.

### Heavy Output Generation (HOG) Binary Classifier

A binary classifier based on heavy output generation with logarithmic sample complexity at short depth.

- Classifies samples as quantum vs classical
- Logarithmic sample complexity at short circuit depths
- Works under depolarizing noise models

### Analytical Framework

Uses replica tricks to derive exact analytic expressions for all-to-all Brownian circuit ensembles. Numerical simulations corroborate results for discrete Haar-random unitary circuits.

## When to Use

- Benchmarking NISQ quantum experiments
- Designing quantum advantage demonstrations
- Evaluating shallow-depth random circuits
- Distinguishing quantum from classical sampling
- Analyzing noise-robust quantum benchmarks

## Verification Steps

1. Confirm benchmark separates quantum from classical under target noise model
2. Verify sample complexity matches theoretical predictions
3. Check that no classical spoofer achieves comparable scores
4. Validate against known quantum advantage thresholds

## Error Handling

### Classical Spoofing Detected
If linear XEB scores are matched by classical algorithms, switch to nonlinear XEB.

### Noise Too High
If depolarizing noise exceeds threshold, consider deeper circuits or error mitigation.

### Sample Budget Constraints
Use HOG classifier which has logarithmic sample complexity at short depths.

## Resources

- arXiv: 2605.22909
- Categories: quant-ph

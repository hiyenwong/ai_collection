---
name: no-go-gaussian-quantum-repeaters
description: "No-go theorem for Gaussian quantum repeaters — proves that Gaussian operations with homodyne measurements and classical communication cannot enhance quantum capacity of pure-loss channels beyond direct transmission, using fractional extendibility framework."
category: quantum
---

# No-Go Theorem for Gaussian Quantum Repeaters

## Context

Based on arXiv:2606.05097 (Ahmed, Smith, Jun 2026). Proves a fundamental no-go theorem: Gaussian repeater protocols cannot enhance quantum communication rates over bosonic attenuation channels beyond direct transmission.

## Core Methodology

1. **Problem setup**: Consider a repeater chain over bosonic attenuation channels where nodes perform Gaussian operations, homodyne measurements, and arbitrary classical communication (LOCC)
2. **Fractional extendibility**: Generalize k-extendibility to a notion of fractional extendibility for Gaussian states
3. **Key properties**: Establish useful properties of fractional extendibility that are preserved under Gaussian operations and LOCC
4. **No-go proof**: Show that any such repeater chain cannot exceed the quantum capacity achievable by direct transmission through the pure-loss channel
5. **Framework for analysis**: The fractional extendibility framework provides a powerful tool for analyzing Gaussian quantum networks more broadly

## Implementation Steps

1. Model the quantum repeater chain as a sequence of Gaussian operations + LOCC
2. Characterize the input state's fractional extendibility
3. Show that fractional extendibility cannot be improved by any Gaussian protocol in the chain
4. Derive the capacity bound: Q(repeater) ≤ Q(direct transmission)
5. Apply the framework to analyze other Gaussian quantum network protocols

## Key Results

- Gaussian repeaters fundamentally cannot enhance quantum capacity of pure-loss channels
- The proof holds for arbitrary classical communication between repeater nodes
- Fractional extendibility generalizes k-extendibility and provides a unifying framework
- The result closes a long-standing open question about Gaussian vs. non-Gaussian repeater protocols

## Pitfalls

- This result applies specifically to pure-loss (bosonic attenuation) channels; other channel types may behave differently
- Non-Gaussian operations can still provide advantage — the no-go theorem does not rule out non-Gaussian repeaters
- The fractional extendibility framework applies to Gaussian states; extension to non-Gaussian states requires different tools
- Classical communication alone (without quantum operations) cannot create or enhance quantum capacity

## Verification

- Verify that the fractional extendibility of the output state is bounded by the input
- Check that the capacity bound matches known direct transmission limits
- Confirm that non-Gaussian protocols (e.g., using photon subtraction) can potentially exceed the bound

## Activation

- gaussian quantum repeaters, no-go theorem, fractional extendibility, quantum capacity, bosonic channels, pure-loss channels
- 高斯量子中继器, 不可能定理, 分数可扩展性, 量子容量, 玻色信道

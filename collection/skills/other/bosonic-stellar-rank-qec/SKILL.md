---
name: bosonic-stellar-rank-qec
description: Stellar rank as resource measure for bosonic quantum error correction. Designs and benchmarks bosonic codes under finite non-Gaussian resources, revealing noise-adapted code structures and concrete resource thresholds.
category: quantum
trigger_words: ["bosonic quantum error correction", "stellar rank", "GKP code", "cat code bosonic", "finite stellar rank qec", "bosonic code optimization"]
---

# Bosonic Quantum Error Correction with Finite Stellar Rank

## Core Idea

Use **stellar rank** as a resource measure to design and benchmark bosonic quantum error-correcting codes under **finite non-Gaussian resource constraints**.

## Key Findings

### Trade-off Triangle
Finite stellar rank creates a trade-off among:
1. **State approximability** - how well the target codeword can be approximated
2. **Energy** - physical energy of the encoded state  
3. **Logical protection** - error correction capability under photon loss and dephasing

### Noise-Adapted Code Structures
- **Photon loss**: Grid-like encodings emerge as optimal
- **Photon-number dephasing**: Approximately rotation-symmetric encodings emerge
- Codewords with better ideal error-correction properties need not be optimal under finite-rank constraints

### Resource Thresholds
- **Stellar rank k=2** suffices to surpass break-even for all dephasing strengths
- Under photon loss, required rank increases with loss rate

## Methodology

### Step 1: Define Stellar Rank Budget
- Fix the maximum stellar rank k available for state preparation
- This bounds the non-Gaussian resource cost

### Step 2: Analyze Fixed Code Families
- Evaluate cat codes and GKP codes at finite stellar rank
- Compute trade-offs using optimal recovery

### Step 3: Direct Optimization
- Optimize bosonic encodings directly at fixed stellar rank
- Discover noise-adapted code structures beyond fixed-target codewords

## Trigger Conditions

- Designing bosonic QEC codes for continuous-variable quantum systems
- Resource-constrained quantum state preparation
- Optimizing codes for specific noise channels (photon loss vs dephasing)
- Evaluating trade-offs in bosonic code design

## Pitfalls

- Better ideal codes ≠ better practical codes under finite-rank constraints
- Required stellar rank depends on specific noise channel and strength
- Must evaluate with optimal recovery, not just naive decoding

## Verification

- Compare code performance across different stellar ranks
- Validate against photon loss and dephasing noise models
- Check break-even thresholds for practical implementations

## References

- arXiv:2607.06404 - Bosonic quantum error-correcting codes with finite stellar rank
- Authors: Rui Wang, Adithi Udupa, Timo Hillmann, Ulysse Chabaud, Alessandro Ferraro, Giulia Ferrini

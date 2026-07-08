---
name: wigner-function-reconstruction
description: |
  Wigner function reconstruction methodology for continuous-variable quantum system characterization.
  Combines provably efficient regression for sparse states (binomial codes, cat states) with deep learning
  for general states (GKP). Use when: (1) characterizing CV quantum systems, (2) reconstructing Wigner functions
  from sparse measurements, (3) identifying error processes in QEC cycles, (4) phase-space tomography,
  (5) reducing measurement overhead in quantum state characterization. Trigger words: wigner function,
  phase-space reconstruction, CV quantum characterization, GKP state tomography, sparse phase-space data.
---

# Wigner Function Reconstruction

## Core Insight

Wigner function learning characterizes continuous-variable (CV) quantum systems by inferring continuous
phase-space functions from sparse pointwise measurements. Complexity scales **logarithmically** with Hilbert
space dimension for sparse states.

## Two-Regime Approach

### Sparse States (Binomial, Cat States)

For states with sparse Fock-space or coherent-state representations:

- Use provably efficient regression models
- Measurement complexity: O(log(d)) where d = effective Hilbert dimension
- No deep learning needed — compressed sensing suffices

### General States (GKP, Unknown States)

For states without sparse structure:

- Train deep learning model on sparse measurements
- Model generalizes to arbitrary phase-space resolution
- Key: learns to identify dominant error processes with fewer measurements than conventional estimation

## Experimental Validation

Validated on circuit-QED experimental data:
- Reconstructs Wigner functions across multiple QEC rounds
- Identifies dominant error processes with significantly fewer measurements
- Works on both simulated and real experimental data

## Pipeline

1. **Data collection**: Sparse pointwise measurements in phase space
2. **State classification**: Determine if state has sparse structure
3. **Method selection**:
   - Sparse → compressed sensing regression (O(log d) measurements)
   - General → trained deep learning model
4. **Reconstruction**: Generate continuous Wigner function
5. **Error identification**: Identify dominant error processes from reconstructed function

## Scripts

See `scripts/wigner_reconstruct.py` for implementation.

## References

- arXiv:2607.06232 - "Learning to Reconstruct Wigner Functions in Phase Space"
- GKP codes: Gottesman-Kitaev-Preskill error correction
- Circuit QED: superconducting qubit-cavity systems

## Activation Keywords

- wigner function, phase-space reconstruction, CV quantum characterization
- GKP state tomography, sparse phase-space data
- quantum state reconstruction, continuous variable tomography

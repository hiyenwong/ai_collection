---
name: neural-phase-correlation
description: "Learned generalization of phase correlation that lifts the fixed Fourier basis restriction to discover unknown transformations between observations. Applicable to image registration, non-rigid deformation, and quantum Hamiltonian eigenstate recovery from observation pairs."
metadata:
  arxiv_id: "2606.18496"
  published: "2026-06-16"
  authors: "Cole Reynolds"
  tags: [phase-correlation, neural-networks, image-registration, quantum, fourier, correspondence]
---

# Neural Phase Correlation

## Description

A learned generalization of phase correlation that lifts the fixed Fourier basis restriction, enabling discovery of unknown transformations between observations. Extends from global translation to dense non-rigid deformations and unitary dynamics. Validated on cardiac MRI, echocardiography, and quantum harmonic oscillator eigenstate recovery.

## Activation Keywords
- neural phase correlation
- learned phase correlation
- image registration neural
- fourier correspondence
- transformation discovery
- quantum eigenstate recovery
- 相位相关学习

## Core Concepts

### Phase Correlation Generalization
- **Classical limitation**: Standard phase correlation only measures global translation via fixed Fourier basis
- **Key insight**: Learn the basis on which the transformation decomposes, rather than using fixed Fourier modes
- **Algebraic primitive**: Same mathematical foundation extends to dense non-rigid deformations and unitary dynamics
- **First-class transformation**: Architecture represents transformation as explicit object, not implicit through similarity functions

### Applications
1. **Medical imaging registration**: ACDC cardiac MRI, CAMUS echocardiography
2. **Quantum physics**: Recovering Hamiltonian eigenstates from observation pairs
3. **Non-rigid deformation**: Dense correspondence beyond global translation

## Usage Patterns

### Pattern 1: Image Registration
When registering medical images or general observation pairs:
1. Encode both observations into shared representation
2. Apply learned phase correlation in Fourier-like domain
3. Decode transformation from correlation peak
4. Achieves state-of-the-art without auxiliary scoring mechanisms

### Pattern 2: Quantum State Analysis
When analyzing quantum systems from observation data:
1. Apply to pairs of time-evolved wavefunctions
2. Framework recovers Hermite-function eigenstates
3. Quantized energy levels extracted from observation pairs alone
4. No prior knowledge of Hamiltonian required

### Pattern 3: Non-rigid Deformation Tracking
When tracking dense non-rigid deformations:
1. Same algebraic primitive extends beyond translation
2. Learns basis for deformation decomposition
3. Matches/exceeds prior baselines on cardiac benchmarks

## Methodology

### Step 1: Representation Learning
- Learn the decomposition basis from data
- Same architecture handles translation, deformation, and unitary dynamics

### Step 2: Correlation Computation
- Apply phase-correlation algebraic primitive on learned basis
- Extract transformation parameters from correlation structure

### Step 3: Validation
- Evaluate on paired observations
- For quantum systems: verify eigenstate and energy recovery

## Error Handling

### Mode Collapse in Learned Basis
- Ensure basis diversity through regularization
- Validate against known ground-truth transformations

### High-Frequency Artifacts
- Apply appropriate filtering in learned frequency domain
- Balance resolution with noise robustness

## Examples

### Example: Quantum Harmonic Oscillator
Applied to time-evolved wavefunction pairs of 1-D quantum harmonic oscillator, the framework recovers Hermite-function eigenstates and quantized energy levels from observation pairs alone — no Hamiltonian specification needed.

## Resources
- arXiv: 2606.18496 - "Neural Phase Correlation"
- Related: `quantum-state-engineering`, `quantum-brain-modeling`

---
name: spatially-coupled-quantum-codes
description: "Spatial coupling methodology for quantum LDPC/CSS codes. Proves that belief-propagation decoding on spatially coupled CSS codes (MN/HA-type) achieves the quantum erasure hashing bound. Uses coupled-vector potential method and density evolution analysis to show BP threshold equals MAP threshold."
---

# Spatially Coupled Quantum Codes

## Description
Spatial coupling is a technique from classical coding theory adapted to quantum error correction. By spatially coupling CSS codes (Calderbank-Shor-Steane), belief-propagation (BP) decoding achieves the maximum-a-posteriori (MAP) performance — specifically the quantum erasure hashing bound — despite BP being a suboptimal decoder. This methodology provides a DE-level proof for seeded BP decoding on finite-degree factor graphs.

## Activation Keywords
- spatially coupled quantum code
- spatial coupling CSS
- quantum erasure hashing bound
- seeded belief propagation
- MN/HA CSS code
- coupled vector potential
- density evolution quantum
- 空间耦合量子码
- 量子删除信道哈希界

## Core Concepts

### Spatial Coupling
- A technique that couples multiple instances of a base code along a chain
- Enables BP decoding to achieve MAP threshold (threshold saturation)
- Originally discovered for classical LDPC codes; extends to quantum CSS codes

### CSS Codes from MN/HA Ensembles
- MacKay-Neal/Hsu-Anastasopoulos punctured sparse ensembles
- Achieve capacity under MAP decoding
- Spatial coupling + seeded BP = achieves hashing bound under BP

### Quantum Erasure Channel & Hashing Bound
- On the quantum erasure channel, erased qubits are replaced by maximally mixed states
- Hashing bound: R = 1 - 2p (for erasure probability p)
- Achieving the hashing bound means optimal performance for the given code rate

### Density Evolution (DE) Analysis
- Tracks message distributions through BP iterations
- Five-message DE recursion for CSS erasure decoding
- Decomposes into Z-side and X-side constituent systems

## Methodology

### Step 1: CSS Ensemble Definition
Define the CSS code ensemble:
1. Specify sparse punctured parity-check matrices for X and Z checks
2. Define corresponding dense parity-check matrices
3. Set finite Z-side degree, X-side degree, and check degrees

### Step 2: Erasure Model Setup
On an erased coordinate:
- Two binary Pauli components remain unresolved
- Erased qubit represented by four Pauli possibilities (I, X, Y, Z)
- Map to hard-erasure CSS decoding problem

### Step 3: Density Evolution Derivation
Derive the DE recursion:
1. Write five-message DE recursion for the uncoupled system
2. Decompose into Z-side and X-side constituent systems
3. Define two constituent potentials (one per side)

### Step 4: Coupled-Vector Potential Analysis
Apply the coupled-vector potential method:
1. Apply to Z-side constituent → Z-side BP threshold
2. Apply to X-side constituent → X-side BP threshold
3. Combined threshold = min(Z-side degree ratio, X-side complementary degree ratio)

### Step 5: Hashing Bound Achievement
For X/Z equal-rate specialization:
- Z-side and X-side constituent design rates are equal
- BP threshold = hashing-bound channel parameter determined by design rate
- Proves seeded BP achieves hashing bound on finite-degree factor graphs

## Workflow

### Pattern 1: Spatially Coupled CSS Code Design
For constructing spatially coupled CSS codes:
1. Choose base MN/HA ensemble parameters (Z-degree, X-degree, check degree)
2. Define spatial coupling window and chain length
3. Design seeded BP decoder with finite-degree factor graphs
4. Verify DE threshold equals hashing bound for equal-rate case

### Pattern 2: Erasure Channel Performance Analysis
For analyzing erasure channel performance:
1. Model erasure probability distribution
2. Run DE analysis for the coupled system
3. Compare BP threshold vs MAP threshold
4. Verify threshold saturation (BP → MAP)

## Error Handling
### Finite-Length Effects
DE analysis assumes infinite block length. For finite-length codes:
- Use BP concentration results for finite-block analysis
- Consider block-error convergence behavior
- Design finite-code realization of ideal DE seed

### Unequal X/Z Rates
For unequal X/Z design rates:
- BP threshold = min(Z-side degree ratio, X-side complementary degree ratio)
- Not equal to hashing bound; requires different analysis

## Resources
- Paper: arXiv:2606.32001
- Related: `quantum-error-correction-methods` (umbrella), `loss-biased-qec` (bias-tailored QEC), `coset-based-qldpc-codes` (CSS code construction)

---
name: reservoir-computation-organization
description: "Analyze how information processing capacity is organized across reservoir state-space modes. Use SVD mode-task projection, degree-wise representation energy, and noise-aware capacity to design or diagnose echo-state networks and physical reservoirs."
metadata:
  arxiv_id: "2607.17858"
  published: "2026-07-21"
  authors: "Mohab Abdalla, Damien Rontani"
  tags: [reservoir-computing, echo-state-network, information-processing-capacity, SVD, mode-decomposition, representation-energy, noise-aware-capacity, computational-neuroscience]
license: Complete terms in LICENSE.txt
---

# Organization of Computation in Reservoir Computing

Analyze how task-relevant information is distributed across the modes of a reservoir computer, using singular value decomposition (SVD) and the information processing capacity (IPC) framework. The method reveals where linear memory and nonlinear transformations live in the reservoir state space and how robust they are to experimental noise.

## When to Use

- Designing or diagnosing echo-state networks (ESNs) and physical reservoir computers.
- You want to know which state-space modes carry task-relevant features.
- You need to quantify the trade-off between absolute IPC and the energy/representation of each nonlinear degree.
- You are evaluating whether high IPC values are practically accessible given readout or setup noise.
- You want to compare activation functions, spectral radii, or input scalings from a geometric perspective.

## Core Methodology

### 1. Standard ESN Setup

- Reservoir state update:

  x(t) = tanh( ρ W_res x(t-1) + ι w_in u(t-1) + β b )

- W_res: random recurrent connectivity matrix, normalized so that its spectral radius is one before scaling by ρ.
- w_in: random input vector.
- ρ: spectral radius; ι: input scaling; β: bias scaling.
- Drive the reservoir with a single-channel white-noise input u(t) ~ U(-1, 1).
- Collect state matrix X ∈ R^{N × T}.

### 2. SVD Mode Decomposition

- Compute the SVD of X:  X = Q Σ V^T.
- Q ∈ R^{N×N}: left singular vectors, orthonormal basis in node space.
- σ_i: singular values; energy fraction η_i = σ_i² / Σ_j σ_j².
- Projected states: ~x_i = q_i^T X  (row i of Q^T X).
- Effective rank: r_e = exp( - Σ_i η_i ln η_i ).

### 3. IPC Targets

- Construct orthogonal target sequences z_k from products of Legendre polynomials of delayed inputs:

  z_k(t) = ∏_m P_{d_m}( u(t-m) )

- The degree d of a target is the sum of polynomial degrees across delays.
- Define ε-threshold target sets Z_d^{(ε)} = { z_k ∈ Z_d | c_k > ε }, where c_k is the capacity to reconstruct target z_k.

### 4. Mode-Task Projection

- For each mode i and target k, compute the mode-task score:

  s_{i,k} = ( ~x_i^T z_k )² / ( ||~x_i||² ||z_k||² )

- Cumulative mode-task score: S_k^i = Σ_{j=0}^{i} s_{j,k}.
- Onset mode: first i where S_k^i ≥ δ_on (and previous mode is below).
- Offset mode: where S_k^{i+1} - S_k^i < δ_off.
- Mode usage: S_i = Σ_k s_{i,k}.
- Degree-resolved mode usage: S_{i,d} = Σ_{k ∈ Z_d^{(ε)}} s_{i,k}.

### 5. Representation Energy and Noise-Aware Capacity

- Degree-wise representation energy: Φ_d = Σ_i η_i S_{i,d}.
- Normalized capacity per degree: C̄_d = C_d / Σ_d C_d.
- Estimate noise floor from the weakest mode: η_noise ≈ η_{N-1}; Φ_noise ≈ N η_noise.
- Signal-to-noise ratio per degree: γ_d = Φ_d / Φ_noise.
- Noise-aware degree-wise capacity: C̄_d^γ = C̄_d * γ_d / (1 + γ_d).

## Key Findings

- Reservoir activity is effectively low-dimensional: most energy is concentrated in a few modes, and effective rank is much smaller than N.
- Linear memory (d=1) typically dominates the higher-energy modes, while higher-degree nonlinear tasks tend to occupy low-energy modes.
- In biased tanh ESNs, d=1 tasks capture ~99.7% of representation energy but only ~17.8% of normalized IPC; d=2 tasks capture ~36% of IPC but only ~0.2% of representation energy.
- A high IPC does not guarantee practical accessibility: high-degree features can be buried in low-energy modes and are easily lost to noise.
- Nonlinearity accessibility depends on both activation function and bias: unbiased sin² can make second-degree nonlinearities more robust to noise than biased tanh, despite lower raw IPC.
- Increasing ρ broadens the energy distribution; increasing ι pushes higher-degree tasks into higher-variance modes.

## Practical Workflow

1. Initialize an ESN or physical reservoir with chosen (ρ, ι, β, activation).
2. Drive it with white-noise input and collect state matrix X.
3. Compute SVD of X; inspect energy fractions η_i and effective rank r_e.
4. Build orthogonal IPC targets up to desired degree d (e.g., d = 1..5).
5. For each target, compute mode-task scores s_{i,k} and cumulative scores S_k^i.
6. Aggregate by degree to obtain S_{i,d} and Φ_d.
7. Compare Φ_d to C̄_d to identify accessible vs buried capacity.
8. Estimate noise floor and compute noise-aware capacity C̄_d^γ.
9. Sweep parameters (ρ, ι, activation, bias) to optimize representation energy, not just IPC.

## Parameters and Defaults

| Parameter | Suggested default | Notes |
|-----------|-------------------|-------|
| Reservoir size N | 50–1000 | Larger N gives more modes but effective rank stays low |
| Input length T | 10^4–10^6 | Longer T improves orthogonality of IPC targets |
| Spectral radius ρ | 0.5–1.0 | Below 1 for ESN stability; near 1 for richer dynamics |
| Input scaling ι | 0.1–1.0 | Higher ι pushes nonlinear modes to higher energy |
| Bias scaling β | 0.0–0.5 | Symmetry-breaking; controls odd/even degree balance |
| Activation | tanh, sin² | Choice strongly affects degree accessibility |
| IPC threshold ε | 10^-10 | Capacity threshold for retaining a target |
| Onset δ_on | 0.8 | Cumulative fraction defining task onset |
| Offset δ_off | 0.01 | Incremental drop defining task offset |

## Pitfalls

- **Equating IPC with accessibility**: high IPC in a low-Φ_d mode is not robust to noise.
- **Ignoring activation symmetry**: unbiased tanh suppresses even-degree nonlinearities; unbiased sin² can enhance them.
- **Short input sequences**: finite T makes IPC targets only approximately orthogonal; mode usage S_i is then approximately bounded by 1.
- **Isotropic noise assumption**: the noise-floor estimate Φ_noise ≈ N η_{N-1} assumes additive isotropic noise. Multiplicative or colored noise requires more careful modeling.
- **Single-node readout**: the framework uses linear readout; nonlinear readouts can recover modes that linear readouts miss.

## Activation Keywords

- reservoir computing mode decomposition
- information processing capacity SVD
- degree-wise representation energy
- echo state network geometry
- noise-aware reservoir capacity
- nonlinear degree accessibility
- physical reservoir design

## References

- Jaeger (2001). The "echo state" approach to analysing and training recurrent neural networks. *GMD Report*.
- Maass et al. (2002). Real-time computing without stable states: a new framework for neural computation. *Neural Computation*.
- Dambre et al. (2012). Information processing capacity of dynamical systems. *Scientific Reports*.
- Kubota et al. (2021). Modal decomposition of echo-state networks. *Neural Networks*.
- Cover (1965). Geometrical and statistical properties of systems of linear inequalities with applications in pattern recognition. *IEEE Trans. Electronic Computers*.

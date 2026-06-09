# Paper: Complex-Valued Kuramoto Networks: A Unified Control-Theoretic Framework

**arXiv**: 2604.07249
**Authors**: Lorenzo Giordano, Josep M. Olm, Mario di Bernardo
**Published**: 2026-04-08
**PDF**: papers/systems-engineering-2026-04-09/kuramoto-control.pdf

## Abstract

Synchronization in networks of coupled oscillators is classically studied via the Kuramoto model, whose intrinsic nonlinearity limits analytical tractability and complicates control design.

Complex-valued extensions circumvent this by embedding phase dynamics into a higher-dimensional linear state space, where regulating complex-state moduli to a common value recovers Kuramoto phase behavior.

Existing approaches to address this problem correspond, within a unified control framework, to state-feedback and hybrid reset-based strategies, each with performance constraints.

We propose two switched control designs that overcome these limitations:
1. Switched feedforward law - ensures exact phase correspondence at all times
2. Feedforward plus sliding-mode law - achieves finite-time convergence without spectral gain tuning

Additionally, we present a non-autonomous complex-valued MIMO sliding-mode controller that enforces phase locking at a prescribed frequency in finite time, independent of natural frequencies and coupling strengths.

Simulations confirm improved transient response, steady-state accuracy, and robustness, including synchronization of heterogeneous networks where the classical real-valued Kuramoto model fails.

## Key Contributions

### 1. Unified Control Framework

- Complex-valued Kuramoto → linear state space
- Classical approaches (state-feedback, reset-based) unified
- New control designs overcoming limitations

### 2. Two Switched Control Designs

**Switched Feedforward**:
- Exact phase correspondence at all times
- No spectral gain tuning

**Feedforward + Sliding-Mode**:
- Finite-time convergence
- Robust to disturbances
- No spectral gain tuning needed

### 3. MIMO Sliding-Mode Controller

- Prescribed frequency locking
- Finite-time convergence
- Independent of natural frequencies
- Independent of coupling strengths
- Handles heterogeneous networks

## Technical Innovations

### Complex-Valued Extension

**Classical Kuramoto**: θ_i ∈ ℝ (nonlinear)
**Complex Extension**: z_i = r_i · e^(iθ_i) ∈ ℂ (linear state space)

**Benefit**: Modern control theory applicable

### Control Objective Translation

Phase synchronization → Regulate |z_i| to common value

### Heterogeneity Handling

Classical Kuramoto fails for heterogeneous networks → Complex-valued succeeds

## Applications to Brain Networks

### Phase Synchronization

- Different brain regions have different natural frequencies (heterogeneous)
- Complex-valued Kuramoto can synchronize them
- MIMO controller for prescribed frequency (e.g., alpha band)

### Finite-Time Convergence

Important for neural dynamics:
- Neural decisions require fast phase locking
- Sliding-mode achieves finite-time (not asymptotic)

### Robustness

- Brain noise handled by sliding-mode design
- Independent of natural frequencies (handles brain region heterogeneity)

## Connections to Existing Skills

### kuramoto-brain-network

This skill extends `kuramoto-brain-network` with:
- Control design framework
- Finite-time convergence methods
- Heterogeneous network handling

### brain-connectivity-analysis

Phase synchronization analysis using:
- Complex-valued Kuramoto model
- Control-theoretic synchronization metrics

## Simulation Results

Paper demonstrates:
- Improved transient response
- Better steady-state accuracy
- Enhanced robustness
- Successful synchronization where classical Kuramoto fails

**Key Result**: Heterogeneous network synchronization achieved

---

*Reference file for kuramoto-control-theory skill*

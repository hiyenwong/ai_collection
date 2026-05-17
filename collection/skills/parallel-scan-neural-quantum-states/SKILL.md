---
name: parallel-scan-neural-quantum-states
description: >
  Parallel Scan Recurrent Neural Quantum States (PSR-NQS) methodology for scalable
  variational Monte Carlo simulations. Based on arXiv:2605.13807 (Merali et al., 2026-05-13).
  Use when: implementing neural quantum states (NQS) for many-body quantum systems,
  scaling variational Monte Carlo to large 2D spin lattices, designing autoregressive
  recurrent wave functions, parallelizing sequential recurrence in quantum state sampling,
  or building efficient neural network ansatze for quantum ground state problems.
  Core idea: replace sequential autoregressive sampling with parallel scan (prefix-sum)
  recurrence, enabling GPU-parallelizable training of recurrent NQS on lattices up to 52x52.
  Categories: quantum physics, neural networks, variational Monte Carlo, many-body systems.
  Activation keywords: parallel scan NQS, neural quantum state, recurrent wave function,
  variational Monte Carlo, PSR-NQS, autoregressive quantum state, spin lattice simulation,
  neural quantum ansatz, parallel recurrent quantum
---

# Parallel Scan Recurrent Neural Quantum States

## Overview

PSR-NQS replaces sequential autoregressive recurrence in neural quantum states with a
parallel scan (prefix-sum) operation, enabling GPU-parallelized training of recurrent
architectures for quantum many-body wave functions. Key result: 2D spin lattices up to
52x52 with accuracy matching quantum Monte Carlo, using modest compute resources.

## Methodology

### Core Innovation

Standard NQS uses sequential autoregressive sampling — slow on GPU. PSR-NQS reformulates
the recurrence as a parallel scan (associative prefix-sum), allowing O(log N) parallel
computation instead of O(N) sequential.

### Implementation Steps

1. **Design autoregressive recurrent cell**: Define hidden state update h_i = f(h_{i-1}, s_i)
   where s_i are spin configurations. The cell must be associative for parallel scan.

2. **Parallel scan formulation**: Rewrite sequential recurrence as associative binary
   operation ⊕ that can be parallelized:
   ```
   h_i = h_{i-1} ⊕ s_i  →  parallel_scan(h_0, s_1, ..., s_N)
   ```

3. **Variational Monte Carlo training**:
   - Sample spin configurations using the autoregressive model
   - Compute local energy E_L(s) = ⟨s|H|ψ⟩/⟨s|ψ⟩
   - Optimize parameters via stochastic reconfiguration or Adam
   - Use parallel scan for efficient forward pass

4. **Wave function representation**:
   - ψ(s) = exp(∑ log p(s_i|s_{<i})) where p is the recurrent output
   - Amplitude and phase can be modeled separately or jointly

### Key Design Principles

- **Associativity is critical**: The recurrent update must form a semigroup for parallel scan
- **Gating mechanisms**: Use GRU/LSTM-style gates that can be reformulated associatively
- **Memory efficiency**: PSR reduces memory from O(N) sequential to O(log N) tree depth
- **Scalability**: Enables 2D lattices 52×52 with standard GPU resources

## Application Domains

- **Transverse field Ising model**: 1D and 2D spin systems
- **Heisenberg antiferromagnet**: Benchmark against exact diagonalization
- **Frustrated magnets**: Systems where QMC suffers from sign problem
- **Fermionic systems**: With appropriate antisymmetrization

## Resources

- **arXiv**: [2605.13807](https://arxiv.org/abs/2605.13807)
- **Authors**: Ejaaz Merali, Mohamed Hibat-Allah, Mohammad Kohandel, Richard T. Scalettar, Ehsan Khatami
- **Published**: 2026-05-13
- **Categories**: cond-mat.str-el, cs.LG, quant-ph

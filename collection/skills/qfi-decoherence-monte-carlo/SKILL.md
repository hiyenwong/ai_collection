---
name: qfi-decoherence-monte-carlo
description: "Quantum Fisher Information estimation under decoherence via MCMC sampling — maps QFI lower bounds onto classical expectation values over wave function amplitude distributions. Enables QFI estimation for system sizes beyond exact diagonalization. Use when: analyzing metrological content of quantum states under noise, computing QFI bounds for Jastrow-Gutzwiller wave functions, evaluating quantum sensing robustness to dephasing/amplitude damping/depolarizing, or studying entanglement scaling in noisy many-body systems."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.22917"
  published: "2026-05-21"
  authors: "Francesco Musso, Vittorio Vitale, Sara Murciano"
  tags: [quantum, fisher-information, decoherence, monte-carlo, metrology, jastrow-gutzwiller]
---

# Quantum Fisher Information via MCMC under Decoherence

Methodology for estimating Quantum Fisher Information (QFI) of many-body quantum states under decoherence, bypassing full spectral resolution of the density matrix.

## Core Methodology

### QFI Mapping to Classical Expectation

For a state |ψ⟩ = Σ_n c_n |n⟩ in occupation-number basis:

1. Define classical probability distribution: P(n) = |c_n|²
2. QFI lower bound: F_Q[ρ, Ô] ≥ 4 · E_P[ (∂_θ log P(n))² ] (for unitary encoding)
3. This maps the quantum QFI onto a classical expectation value
4. Computational cost: "slow" exponential O(e^{cL}) vs O(4^L) for exact diagonalization

### MCMC Sampling Procedure

```
1. Define target distribution P(n) = |c_n|² from wave function amplitudes
2. Construct Metropolis-Hastings chain:
   - Proposal: flip random occupation number n_i → 1-n_i
   - Acceptance: min(1, P(n')/P(n)) = min(1, |c_{n'}|²/|c_n|²)
3. Sample {n^{(k)}} from chain, compute observable A(n) on each sample
4. Estimate: F_Q ≈ (4/N) Σ_k A(n^{(k)})
```

### Jastrow-Gutzwiller Wave Functions

For |ψ⟩ = Π_{i<j} e^{J_{ij} n_i n_j} Π_i e^{h_i n_i} |ref⟩:
- Amplitude ratio |c_{n'}|²/|c_n|² is O(1) computable (local update)
- Efficient MCMC sampling enabled by local structure
- Metrological scaling: F_Q ∝ L^α with α determined by J_{ij} decay

### Noise Channel Analysis

For three noise channels, compute QFI degradation:

1. **Local dephasing**: ρ → Π_i [(1-p)ρ + p Z_i ρ Z_i]
   - Coherence decay: off-diagonal elements suppressed by (1-2p)^L
   - QFI scaling transition: O(L²) → O(L) at critical p

2. **Local amplitude damping**: ρ → Π_i [K_0 ρ K_0† + K_1 ρ K_1†]
   - Particle loss: K_0 = |0⟩⟨0| + √(1-γ)|1⟩⟨1|, K_1 = √γ|0⟩⟨1|
   - QFI bound: F_Q ≥ (1-γ)·F_Q(pure) for single-particle observables

3. **Global depolarizing**: ρ → (1-λ)|ψ⟩⟨ψ| + λ·I/d
   - Linear decay: F_Q(ρ) ≥ (1-λ)²·F_Q(|ψ⟩)
   - Universal bound independent of state structure

## Optimal Observable Identification

To find the observable Ô maximizing QFI:
1. Compute QFI matrix F_{μν} for generator set {Ĝ_μ}
2. Optimal observable: Ô_opt = Σ_μ (F^{-1})_{μν} Ĝ_ν (pseudo-inverse)
3. Practical: restrict to k-local observables, maximize F_Q numerically

## Usage Patterns

### Pattern 1: QFI bound for pure state
When the state is pure (no noise), QFI = 4·Var(|ψ⟩, Ô) — compute directly.

### Pattern 2: MCMC estimation under noise
When the state is mixed (decoherence), use the mapping to classical distribution + MCMC.

### Pattern 3: Scaling analysis
For system size L, run MCMC for multiple L values and fit F_Q(L) ~ L^α to determine metrological scaling exponent.

## Error Handling

### MCMC Convergence
- Check autocorrelation time τ_int; ensure N_samples ≫ τ_int
- Use parallel tempering for multimodal P(n) distributions
- Monitor effective sample size (ESS) — reject if ESS < 1000

### Finite-Size Effects
- For small L (< 10), use exact diagonalization to validate MCMC
- For large L, verify scaling behavior is consistent across L values

### Noise Channel Limitations
- The MCMC mapping assumes wave function amplitudes are known analytically
- For states not in closed form, use variational approach + neural quantum states

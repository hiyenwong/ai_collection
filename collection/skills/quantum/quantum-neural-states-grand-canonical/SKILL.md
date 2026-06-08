---
name: quantum-neural-states-grand-canonical
description: Neural network quantum state architecture for grand canonical ensemble simulations. Use when representing symmetric bosonic wavefunctions in Fock space, studying quantum many-body systems with variable particle number, computing one-body reduced density matrices, or estimating condensate fractions and radial density profiles from first principles.
---

# Neural Network Quantum States in Grand Canonical Ensemble

## Description

Methodology from arXiv:2605.07779 (Hul, Medvidović, Carrasquilla, May 2026). Proposes NQS architecture for symmetric bosonic wavefunctions in Fock space, enabling variable particle number studies. Achieves competitive variational energies across 1D/2D systems with geometric optimization.

## Activation Keywords
- grand canonical quantum states
- bosonic neural quantum states
- Fock space neural network
- variable particle number quantum
- condensate fraction estimation
- one-body reduced density matrix
- NQS grand canonical
- neural quantum bosonic

## Core Methodology

### Problem
Traditional NQS work in fixed particle number sectors (canonical ensemble). Many physical systems require variable particle number (grand canonical ensemble), especially bosonic systems where particle number fluctuates.

### Solution
Design NQS architecture that:
1. **Represents Symmetric Bosonic Wavefunctions**: Invariant under particle permutation
2. **Works in Fock Space**: Directly represents occupation number basis states
3. **Handles Chemical Potential**: Converges to physical boson number under set μ
4. **Enables Observable Computation**: One-body reduced density matrices, condensate fractions

### Architecture Design

1. **Fock Space Representation**:
   ```
   |ψ⟩ = Σ_{n₁,n₂,...,nₘ} ψ(n₁,...,nₘ) |n₁,...,nₘ⟩
   ```
   - Neural network maps occupation configurations → amplitudes
   - Enforces bosonic symmetry automatically

2. **Symmetric Neural Network**:
   ```python
   def symmetric_bosonic_nns(occupations, params):
       """Symmetric function of occupation numbers."""
       # Sort occupations to ensure permutation invariance
       sorted_occ = jnp.sort(occupations)
       # Process through symmetric architecture
       hidden = mlp(sorted_occ, params)
       return hidden
   ```

3. **Chemical Potential Integration**:
   ```python
   def grand_canonical_energy(params, hamiltonian, mu, n_samples):
       """Energy in grand canonical ensemble."""
       samples = sample_fock_states(params, n_samples)
       local_energies = local_energy(samples, hamiltonian)
       # Grand canonical energy: E - μN
       particle_numbers = jnp.sum(samples, axis=1)
       grand_energy = jnp.mean(local_energies - mu * particle_numbers)
       return grand_energy
   ```

### Training Pipeline

1. **Initialize Network**: Random parameters for Fock space NQS
2. **Monte Carlo Sampling**: Sample occupation configurations
3. **Energy Minimization**: ⟨H⟩ - μ⟨N⟩ via gradient descent
4. **Geometric Optimization**: Natural gradient for faster convergence
5. **Observable Computation**: Extract physical quantities

### Key Observables

1. **One-Body Reduced Density Matrix**:
   ```python
   def compute_obrdm(samples, params, n_basis):
       """Compute one-body reduced density matrix."""
       # ρ₁(i,j) = ⟨aᵢ⁺aⱼ⟩
       obrdm = jnp.zeros((n_basis, n_basis), dtype=complex)
       for s in samples:
           # Compute matrix elements for each configuration
           for i in range(n_basis):
               for j in range(n_basis):
                   if s[i] > 0:
                       weight = jnp.sqrt(s[i] * (s[j] + 1))
                       obrdm = obrdm.at[i, j].add(weight)
       return obrdm / len(samples)
   ```

2. **Condensate Fraction**:
   ```python
   def condensate_fraction(obrdm):
       """Largest eigenvalue of OBRDM / total particle number."""
       eigenvalues = jnp.linalg.eigvalsh(obrdm)
       n0 = jnp.max(eigenvalues)
       n_total = jnp.sum(eigenvalues)
       return n0 / n_total
   ```

3. **Radial Density Profile**:
   ```python
   def radial_density(samples, positions):
       """Compute density as function of radial distance."""
       densities = []
       for r in jnp.linspace(0, jnp.max(positions), 50):
           mask = jnp.abs(positions - r) < dr
           density = jnp.mean(jnp.sum(samples[:, mask], axis=1))
           densities.append(density)
       return jnp.array(densities)
   ```

## Implementation Guide

### Step 1: Fock Space Sampling
```python
def sample_fock_configurations(params, n_samples, max_occupation=10):
    """Generate occupation number configurations."""
    # Metropolis-Hastings in Fock space
    configs = []
    current = random_occupation(params, max_occupation)
    
    for _ in range(n_samples):
        # Propose move: change occupation at random site
        proposed = propose_move(current, max_occupation)
        
        # Acceptance probability
        log_p_current = log_amplitude(params, current)
        log_p_proposed = log_amplitude(params, proposed)
        acceptance = jnp.exp(log_p_proposed - log_p_current)
        
        if random() < acceptance:
            current = proposed
        
        configs.append(current)
    
    return jnp.array(configs)
```

### Step 2: Symmetric Architecture
```python
import flax.linen as nn

class SymmetricBosonicNQS(nn.Module):
    """Permutation-invariant NQS for bosonic systems."""
    n_sites: int
    max_occ: int
    hidden_dims: tuple = (64, 64)
    
    @nn.compact
    def __call__(self, occupations):
        # occupations: (n_sites,) - occupation numbers
        
        # Symmetry via sorting + MLP
        sorted_occ = jnp.sort(occupations)
        
        # Embed occupation numbers
        x = jnp.expand_dims(sorted_occ, -1)
        
        for dim in self.hidden_dims:
            x = nn.Dense(dim)(x)
            x = nn.relu(x)
        
        # Output: log amplitude + log phase
        log_amp = nn.Dense(1)(x).squeeze()
        log_phase = nn.Dense(1)(x).squeeze()
        
        return log_amp + 1j * log_phase
```

### Step 3: Geometric Optimization
```python
def natural_gradient_step(params, optimizer, hamiltonian, mu):
    """Natural gradient descent for faster convergence."""
    # Compute standard gradient
    grad = jax.grad(grand_canonical_energy)(params, hamiltonian, mu)
    
    # Compute Fisher information matrix (approximate)
    fisher = compute_fisher(params, n_samples=1000)
    
    # Natural gradient: F⁻¹ g
    nat_grad = jnp.linalg.solve(fisher, grad)
    
    return optimizer.apply_gradients(params, nat_grad)
```

## Common Pitfalls

### Pitfall 1: Fock Space Explosion
**Issue**: Hilbert space grows exponentially with sites × max occupation.
**Fix**: Use importance sampling, truncate max occupation based on physics (e.g., hard-core limit).

### Pitfall 2: Symmetry Enforcement
**Issue**: Naive NN doesn't respect bosonic permutation symmetry.
**Fix**: Always sort occupation numbers before processing, or use explicitly symmetric architectures.

### Pitfall 3: Chemical Potential Convergence
**Issue**: System may not converge to correct particle number.
**Fix**: Monitor ⟨N⟩ during training, adjust μ adaptively if needed.

### Pitfall 4: Complex Phase Handling
**Issue**: Phase structure may be hard to learn.
**Fix**: Initialize with real wavefunctions when possible, use phase reweighting techniques.

## When to Use
- Bosonic quantum many-body simulations
- Systems with variable particle number
- Condensate fraction calculations
- BEC and superfluid studies
- Grand canonical ensemble problems
- Systems requiring one-body reduced density matrices

## References
- arXiv:2605.07779 - "Neural network quantum states in the grand canonical ensemble"
- Related: `parallel-scan-neural-quantum-states` — scalable RNN-based NQS
- Related: `neural-quantum-spectral-operator` — quantum spectral operator learning
- Related: `deep-boltzmann-quantum-states` — Deep Boltzmann quantum states for spin glasses

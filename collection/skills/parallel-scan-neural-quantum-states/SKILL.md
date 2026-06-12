---
name: parallel-scan-neural-quantum-states
description: Parallel Scan Recurrent Neural Quantum States (PSR-NQS) methodology for scalable variational Monte Carlo simulations. Use when designing efficient RNN-based quantum state ansätze, training neural quantum states with autoregressive models, scaling quantum simulations to large 2D spin lattices, or applying parallel scan techniques to sequential quantum architectures.
---

# Parallel Scan Recurrent Neural Quantum States (PSR-NQS)

## Description

Methodology from arXiv:2605.13807 (Merali et al., May 2026). Challenges the view that recurrent NQS are inherently unscalable by showing modern recurrent architectures with parallelizable recurrence can achieve fast, accurate VMC simulations. Achieves 52×52 2D spin lattice accuracy with modest resources.

## Activation Keywords
- PSR-NQS
- parallel scan neural quantum states
- parallelizable recurrent quantum
- RNN quantum state scaling
- autoregressive quantum wavefunction
- recurrent VMC
- neural quantum state parallel scan
- quantum spin lattice recurrent

## Core Methodology

### Problem
Recurrent NQS were traditionally viewed as intrinsically sequential, making them less scalable than transformer-based architectures for quantum many-body simulations.

### Solution
Apply modern parallel scan (associative scan) techniques to recurrent NQS, enabling:
- **Parallel Training**: Replace sequential recurrence with associative scan for GPU parallelism
- **Autoregressive Sampling**: Maintain exact autoregressive probability structure
- **Iterative Retraining**: Progressively scale to larger system sizes

### Architecture

1. **Autoregressive RNN Wavefunction**:
   ```
   ψ(s) = Πᵢ P(sᵢ | s₁...sᵢ₋₁)
   ```
   - RNN processes spins sequentially to build conditional probabilities
   - Each step: hidden state hᵢ = f(hᵢ₋₁, sᵢ), output P(sᵢ|hᵢ)

2. **Parallel Scan Transformation**:
   - Replace sequential RNN with associative scan
   - Leverage parallel prefix-sum structure for O(log N) depth
   - Maintains exact same computation as sequential version

3. **Iterative Retraining Pipeline**:
   - Train on small system (e.g., 8×8)
   - Initialize larger system with extrapolated weights
   - Fine-tune progressively (16×16 → 32×32 → 52×52)

### Key Results
- Accurate on 1D and 2D spin models
- Reaches 52×52 2D lattices (vs. transformer limits)
- Agreement with quantum Monte Carlo benchmarks
- Modest computational resources required

## Implementation Guide

### Step 1: Define Autoregressive RNN Ansatz
```python
import jax
import jax.numpy as jnp

def rnn_cell(hidden, spin, params):
    """Recurrent cell for spin processing."""
    W_h, W_x, b = params
    new_hidden = jnp.tanh(W_h @ hidden + W_x @ spin + b)
    return new_hidden

def log_probability(params, spins):
    """Compute log |ψ(s)|² via RNN."""
    hidden = jnp.zeros(params['h0'].shape)
    log_probs = []
    for s in spins:
        hidden = rnn_cell(hidden, s, params)
        p = jax.nn.softmax(params['output'] @ hidden)
        log_probs.append(jnp.log(p[s] + 1e-10))
    return sum(log_probs)
```

### Step 2: Apply Parallel Scan
```python
from jax.lax import associative_scan

def parallel_rnn_step(carry, x, params):
    """Single step as associative scan element."""
    h_new = rnn_cell(carry, x, params)
    return h_new, h_new

def parallel_log_prob(params, spins):
    """Parallel scan version of RNN."""
    # Transform to associative scan format
    initial_states = jnp.zeros((len(spins), params['h0'].shape[0]))
    
    # Associative scan over recurrence
    _, all_hidden = associative_scan(
        lambda c, x: parallel_rnn_step(c, x, params),
        initial_states, spins
    )
    
    # Compute probabilities in parallel
    logits = all_hidden @ params['output'].T
    log_probs = jax.nn.log_softmax(logits)
    return log_probs
```

### Step 3: VMC Training Loop
```python
def energy_expectation(params, hamiltonian, n_samples=1000):
    """Estimate energy via Monte Carlo sampling."""
    # Autoregressive sampling (can use parallel scan)
    samples = autoregressive_sample(params, n_samples)
    
    # Local energy computation
    local_energies = jax.vmap(
        lambda s: local_energy(params, s, hamiltonian)
    )(samples)
    
    return jnp.mean(local_energies)

def train_step(params, optimizer, hamiltonian):
    """Single training step with gradient descent."""
    def loss_fn(p):
        return energy_expectation(p, hamiltonian)
    
    grad = jax.grad(loss_fn)(params)
    return optimizer.apply_gradients(params, grad)
```

### Step 4: Iterative Scaling
```python
def scale_up(params, old_size, new_size):
    """Initialize larger system from trained smaller system."""
    # Interpolate/extrapolate RNN weights
    new_params = params.copy()
    # Weight initialization strategy depends on architecture
    return new_params

def iterative_training(hamiltonian, sizes=[8, 16, 32, 52]):
    """Progressive training pipeline."""
    params = initialize_params(sizes[0])
    
    for size in sizes:
        if size > sizes[0]:
            params = scale_up(params, sizes[sizes.index(size)-1], size)
        
        params = train_to_convergence(params, hamiltonian, size)
        print(f"Completed {size}x{size} training")
    
    return params
```

## Common Pitfalls

### Pitfall 1: Associative Scan Requirements
**Issue**: Not all recurrence relations support associative scan.
**Fix**: Ensure the recurrence has the form hᵢ = f(hᵢ₋₁, xᵢ) where f is associative in hidden state composition.

### Pitfall 2: Autoregressive Sampling Correctness
**Issue**: Parallel scan must produce identical results to sequential for correctness.
**Fix**: Validate by comparing parallel and sequential outputs on small systems before scaling.

### Pitfall 3: Progressive Initialization
**Issue**: Naive weight extrapolation may not preserve physical properties.
**Fix**: Use physics-informed initialization that respects symmetries (e.g., translation invariance for homogeneous Hamiltonians).

## When to Use
- Quantum many-body ground state problems
- Large 2D spin lattice simulations (beyond transformer capacity)
- Resource-constrained quantum simulation environments
- Systems requiring autoregressive probability structure
- Progressive scaling from small to large system sizes

## References
- arXiv:2605.13807 - "Parallel Scan Recurrent Neural Quantum States for Scalable Variational Monte Carlo"
- Related: `neural-network-quantum-states-grand-canonical` — grand canonical ensemble NQS
- Related: `deep-boltzmann-quantum-states` — Deep Boltzmann quantum states
- Related: `neural-quantum-spectral-operator` — quantum spectral operator learning

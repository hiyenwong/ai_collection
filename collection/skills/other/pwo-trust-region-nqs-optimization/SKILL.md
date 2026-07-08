---
name: pwo-trust-region-nqs-optimization
description: "Proximal Wavefunction Optimization (PWO) methodology for training Neural Quantum States using trust-region optimization. Clips probability-ratio changes in amplitude and phase channels, scales NQS training to billion-parameter models without explicit matrix inversion."
category: neuroscience
---

# PWO Trust-Region NQS Optimization

## Description

Proximal Wavefunction Optimization (PWO) methodology for training Neural Quantum States (NQS) — a trust-region algorithm that clips probability-ratio changes in the amplitude channel and phase increments in the phase channel, combining scalability of first-order optimization with theoretical guarantees. Avoids explicit matrix inversion, reuses samples across multiple updates, and enables NQS training at billion-parameter scale (demonstrated on 1.5B RWKV-7 model).

**Paper**: "One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective" (arXiv:2607.02292)

## Activation Keywords

- proximal wavefunction optimization
- PWO trust-region
- neural quantum state optimization
- NQS training
- trust-region quantum states
- autoregressive NQS training
- wavefunction policy gradient
- NQS optimization stability
- quantum variational optimization
- 神经量子态优化
- 信任区域量子优化
- PWO算法

## Tools Used

- exec: Run Python scripts for NQS training, trust-region optimization
- write: Save trained model checkpoints, optimization logs
- read: Load configuration files, wavefunction data
- search_files: Find existing NQS implementations

## Core Concepts

### 1. NQS as Policy Optimization

The variational energy minimization problem for NQS is reformulated as an **advantage policy-gradient problem** over the Born distribution. This connects quantum physics (variational energy) to reinforcement learning (policy gradients), enabling use of RL optimization techniques for quantum state preparation.

### 2. Trust-Region Clipping

PWO clips two quantities:
- **Amplitude channel**: probability-ratio changes between old and new wavefunction
- **Phase channel**: phase increments to prevent catastrophic phase shifts

This prevents the instability common in Adam (which ignores function space geometry) and the numerical fragility of stochastic reconfiguration (which requires costly matrix inversion).

### 3. Sample Reuse

Unlike stochastic reconfiguration which requires fresh samples per update, PWO reuses samples across multiple gradient steps, dramatically improving wall-clock efficiency.

### 4. Scale

Demonstrated scaling to **1.5B parameter RWKV-7** models — three orders of magnitude beyond prior NQS work.

## Mathematical Framework

### Policy Gradient Formulation

The variational energy gradient:
```
∇_θ E = ⟨(E_loc - E) ∇_θ log|ψ_θ|²⟩
```

is reformulated as a policy gradient where:
- Born distribution |ψ_θ|² is the policy
- Local energy E_loc is the reward signal
- Advantage A = E_loc - E

### PWO Objective

The clipped objective function:
```
L_PWO(θ) = E_s[min(r(θ)·A, clip(r(θ), 1-ε, 1+ε)·A)]
```
where r(θ) = |ψ_θ(s)|² / |ψ_θ_old(s)|² is the probability ratio.

### Phase Channel

For complex-valued wavefunctions, the phase is updated with bounded increments:
```
Δφ ≤ δ_max
```
preventing destructive interference from uncontrolled phase drift.

## Usage Patterns

### Pattern 1: NQS Ground State Training

Train autoregressive NQS for ground state of spin systems:
1. Initialize autoregressive model (RNN/Transformer/RWKV)
2. Sample configurations from Born distribution
3. Compute local energies E_loc = ⟨s|H|ψ⟩/ψ(s)
4. Apply PWO trust-region update
5. Reuse samples for K updates before resampling
6. Monitor energy convergence and KL divergence

### Pattern 2: Large-Scale NQS (Billion Parameters)

For billion-parameter models:
1. Use autoregressive architecture (RWKV/Transformer) for exact sampling
2. Apply PWO with ε ≈ 0.2 (similar to PPO)
3. Set δ_max for phase channel based on system gap
4. Use gradient accumulation for memory efficiency
5. Monitor probability ratio distribution for clipping statistics

### Pattern 3: Frustrated Systems

For frustrated J₁-J₂ spin systems:
1. Initialize with known variational ansatz
2. Use larger clipping threshold (ε ≈ 0.3) for rugged landscapes
3. Apply phase regularization to prevent sign problem
4. Benchmark against Adam, minSR, SPRING baselines

## Step-by-Step Instructions for Agents

1. **Identify the system**: Determine Hamiltonian (Ising, Heisenberg, J₁-J₂, etc.)
2. **Choose architecture**: Autoregressive model (RNN for 1D, Transformer for 2D, RWKV for large scale)
3. **Initialize wavefunction**: Random or informed initialization
4. **Sample configurations**: Draw N samples from |ψ_θ|² (exact for autoregressive)
5. **Compute local energies**: E_loc(s) = Σ_{s'} H_{ss'} ψ(s')/ψ(s)
6. **Apply PWO update**:
   - Compute probability ratio r(θ) for each sample
   - Compute advantage A = E_loc - E_mean
   - Apply clipped objective with ε and δ_max
   - Update parameters via gradient descent
7. **Reuse samples**: Repeat step 6 for K steps without resampling
8. **Monitor convergence**: Track energy, variance, KL divergence, clipping fraction

## Error Handling

### Numerical Instability

If energy diverges:
1. Reduce ε (clipping threshold) from 0.2 to 0.1
2. Reduce learning rate
3. Check for NaN in wavefunction amplitudes
4. Verify sample quality (acceptance rate for MCMC)

### Phase Problem

If phase channel causes instability:
1. Reduce δ_max for phase increments
2. Apply phase regularization term
3. Consider real-valued initialization for systems without frustration

### Memory Overflow

For large models:
1. Use gradient accumulation (smaller batch, more accumulation steps)
2. Enable mixed-precision training
3. Reduce sample reuse K if memory bottleneck

## Examples

### Example: Transverse Field Ising Model

```python
# Pseudo-code for PWO on TFIM
model = AutoregressiveNQS(N_spins=20, hidden_dim=256)
optimizer = Adam(lr=1e-3)
epsilon = 0.2  # clipping threshold
delta_max = 0.1  # phase increment bound
K_reuse = 5  # sample reuse steps

for iteration in range(num_iterations):
    samples = model.sample(N_samples)
    E_loc = compute_local_energy(samples, H_tfi)
    E_mean = E_loc.mean()
    
    for k in range(K_reuse):
        log_prob_new = model.log_prob(samples)
        log_prob_old = old_log_probs
        ratio = torch.exp(log_prob_new - log_prob_old)
        advantage = E_loc - E_mean
        
        # Clipped objective
        clipped_ratio = torch.clamp(ratio, 1-epsilon, 1+epsilon)
        loss = -torch.min(ratio * advantage, clipped_ratio * advantage).mean()
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    old_log_probs = model.log_prob(samples).detach()
```

## Resources

- arXiv:2607.02292 - "One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective"
- Related: `mechanistic-interpretability-neural-quantum-states` (2607.01336)
- Related: `two-dimensional-hyperbolic-rnn-neural-quantum-state` (2606.25600)

## Related Skills

- **mechanistic-interpretability-neural-quantum-states** - SAE-based interpretability for NQS
- **two-dimensional-hyperbolic-rnn-neural-quantum-state** - Hyperbolic geometry for NQS at criticality
- **compact-spin-charge-separated-neural-quantum-states** - Physics-informed NQS architecture
- **neural-polaron-learning-quasiparticle** - Neural operator ansatz for excited states

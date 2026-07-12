# Quantum Noise Models

## Common Noise Channels

### Depolarizing Channel
```
ρ → (1-p)ρ + (p/d)(I - ρ)
```
Probability p: random state replacement

### Amplitude Damping
```
ρ → E_0ρE_0† + E_1ρE_1†

E_0 = |0⟩⟨0| + √(1-γ)|1⟩⟨1|
E_1 = √γ|0⟩⟨1|
```
Energy dissipation with rate γ

### Phase Damping (Dephasing)
```
ρ → (1-p)ρ + p·ZρZ
```
Coherence loss without energy loss

### Bit Flip
```
ρ → (1-p)ρ + p·XρX
```

### Phase Flip
```
ρ → (1-p)ρ + p·ZρZ
```

### Combined Bit-Phase Flip
```
ρ → (1-p)ρ + p·YρY
```

## Kraus Operator Representation

Any quantum channel can be written:
```
ρ → Σ_k K_k ρ K_k†
Σ_k K_k† K_k = I
```

For trajectory method: randomly select K_k with probability:
```
p_k = ⟨ψ|K_k† K_k|ψ⟩
```

## Stochastic Wavefunction Method

### Quantum Jump (Monte Carlo)

1. **No-jump evolution**: |ψ⟩ → exp(-iH_eff dt)|ψ⟩
   ```
   H_eff = H - (i/2) Σ_k K_k† K_k
   ```

2. **Jump probability**: p_jump = dt Σ_k ⟨ψ|K_k† K_k|ψ⟩

3. **If jump occurs**: |ψ⟩ → K_k|ψ⟩/||K_k|ψ⟩|| (randomly select k)

### Implementation

```python
def quantum_jump_trajectory(psi, H, kraus_ops, dt, total_time):
    """Single quantum jump trajectory."""
    
    H_eff = H - 0.5j * sum(K.T.conj() @ K for K in kraus_ops)
    
    for t in np.arange(0, total_time, dt):
        # Compute jump probability
        p_jump = dt * sum(np.vdot(psi, K.T.conj() @ K @ psi) for K in kraus_ops)
        
        if np.random.random() < p_jump:
            # Quantum jump
            weights = [np.vdot(psi, K.T.conj() @ K @ psi) for K in kraus_ops]
            k = np.random.choice(len(kraus_ops), p=weights/p_jump)
            psi = kraus_ops[k] @ psi
            psi /= np.linalg.norm(psi)
        else:
            # No-jump evolution
            psi = expm(-1j * H_eff * dt) @ psi
            psi /= np.linalg.norm(psi)
    
    return psi
```

## Batched Noise Application

For multiple trajectories:
```python
def apply_noise_batch(states, kraus_ops, dt):
    """Apply noise to batch of states."""
    
    n_traj = len(states)
    p_jump = compute_jump_probs_batch(states, kraus_ops, dt)
    
    # Determine which trajectories jump
    jump_mask = np.random.random(n_traj) < p_jump
    
    # Apply jumps
    for i in np.where(jump_mask)[0]:
        states[i] = apply_random_kraus(states[i], kraus_ops)
    
    # Apply no-jump evolution to others
    states[~jump_mask] = apply_effective_hamiltonian(states[~jump_mask], kraus_ops, dt)
    
    return states
```

## Reference

- Nielsen & Chuang, Chapter 8: Quantum noise and quantum operations
- Wiseman & Milburn: Quantum measurement and control
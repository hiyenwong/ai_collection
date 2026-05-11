---
name: quantum-boltzmann-machine-qaoa
description: "Fully connected Quantum Boltzmann Machine (QBM) via bilevel optimization extending QAOA architecture. Covers positive/negative phase training, noise robustness, and single-layer (p=1) QBM implementations. Trigger: quantum boltzmann machine, QBM, QAOA extension, 量子玻尔兹曼机, bilevel quantum optimization, quantum contrastive divergence."
---

# Quantum Boltzmann Machine via Bilevel QAOA

## Description

Implement fully connected Quantum Boltzmann Machines by extending QAOA circuits to bilevel optimization. Achieves superior performance with single-layer (p=1) circuits and exhibits strong noise robustness on NISQ devices.

## Activation Keywords
- quantum boltzmann machine
- QBM
- QAOA extension
- 量子玻尔兹曼机
- bilevel quantum optimization
- quantum contrastive divergence

## Core Architecture

### Bilevel Optimization Structure
- **Inner loop**: Positive phase - energy minimization via QAOA circuit
- **Outer loop**: Negative phase - contrastive divergence via target Hamiltonian structural parameter optimization

### Key Advantage over Standard QAOA
Standard QAOA uses a **fixed** target Hamiltonian. This approach **learns** the target Hamiltonian structure.

## Training Algorithm

```python
def qbm_bilevel_train(p=1, n_shots=10, learning_rate=0.01):
    """
    Bilevel QBM training with QAOA circuit
    
    Inner loop (positive phase):
        - Initialize QAOA parameters (gamma, beta)
        - Run QAOA circuit with current target Hamiltonian
        - Measure energy: E_pos = <psi|H_target|psi>
        - Update QAOA params to minimize E_pos
    
    Outer loop (negative phase):
        - Sample from thermal distribution
        - Compute contrastive divergence
        - Update target Hamiltonian structural params
        - H_target = sum(theta_ij * Z_i Z_j) + sum(h_i * Z_i)
    """
    # Initialize
    theta = initialize_hamiltonian_params()
    
    for outer_step in range(n_outer):
        # Inner: positive phase
        gamma, beta = optimize_qaoa(theta, p)
        E_pos = measure_energy(gamma, beta, theta, n_shots)
        
        # Outer: negative phase (contrastive divergence)
        samples = thermal_sample(theta, n_shots)
        E_neg = compute_negative_energy(samples, theta)
        
        # Update Hamiltonian params
        gradient = E_pos - E_neg
        theta -= learning_rate * gradient
    
    return theta
```

## Performance Characteristics

| Condition | Target State Probability |
|-----------|-------------------------|
| Noiseless, p=1 | 0.9559 |
| NISQ noise, p=1 | 0.6047 |
| 2x NISQ noise, p=1 | 0.3859 |

- Target state maintains highest measurement probability even under 2x noise
- Block-by-block learning with p=1 and 10 shots generates target images robustly

## Noise Robustness Analysis

```python
def analyze_noise_robustness(theta, noise_levels):
    """Test QBM under varying noise intensities."""
    results = {}
    for noise in noise_levels:
        prob = simulate_with_noise(theta, noise, shots=10)
        results[noise] = {
            'target_prob': prob['target'],
            'second_best': prob['second_best'],
            'ratio': prob['target'] / prob['second_best']
        }
    return results
```

## Best Practices
1. Start with p=1 - sufficient for most problems
2. Use block-by-block learning for large systems
3. 10 measurement shots often sufficient with bilevel training
4. Monitor target/second-best probability ratio for robustness

## Error Handling
### Vanishing Gradient
If gradient norm < 1e-6:
- Increase n_shots
- Try randomized initialization
- Check Hamiltonian parameter magnitudes

### Poor Noise Robustness
If target_prob < 0.3 at NISQ noise:
- Reduce problem size
- Add error mitigation
- Consider error-aware training

## References
- arXiv:2605.07473 - "Breaking QAOA's Fixed Target Hamiltonian Barrier" (Jun Liu, May 2026)

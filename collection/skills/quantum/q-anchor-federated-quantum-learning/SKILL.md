---
name: q-anchor-federated-quantum-learning
description: "Q-ANCHOR architecture for Quantum Federated Learning (QFL) that addresses double-drift phenomenon (client drift from non-IID data + hardware bias from noisy quantum gradients). Uses ZNE-guided server anchoring and stateful client correction. Proves convergence under noisy quantum gradient estimates. Activation: Q-ANCHOR, federated quantum learning, QFL, zero-noise extrapolation, quantum federated aggregation, quantum hardware bias, client drift, non-IID quantum data"
metadata:
  arxiv_id: "2605.30075"
  published: "2026-05-28"
  authors: "Hoang M. Ngo, Quan Nguyen, Wanli Xing, My T. Thai"
  tags: [quantum, federated-learning, distributed-systems, error-mitigation, qml]
---

## Core Problem: Double-Drift in Quantum Federated Learning

QFL faces two simultaneous convergence barriers:

1. **Client drift**: Non-IID data causes local models to diverge from global optimum (classical FL problem)
2. **Hardware bias**: Noisy quantum gradient estimates create persistent error floor that standard FedAvg cannot correct (quantum-specific problem)

Standard FedAvg aggregation fails because it averages both signal and hardware bias, creating a persistent error floor.

## Q-ANCHOR Architecture

### Server-Side: ZNE-Guided Anchoring

```
Global update = ZNE_corrected(average(local_gradients))
```

- Server collects quantum circuit outputs from clients
- Applies zero-noise extrapolation (ZNE) using noise scaling factors
- Extrapolates to zero-noise limit before aggregation
- Anchors global update to hardware-corrected estimate

### Client-Side: Stateful Correction

```
Corrected client gradient = local_gradient - hardware_bias_estimate
```

- Each client maintains running estimate of hardware bias
- Bias estimated via shadow circuits / calibration routines
- Stateful tracking prevents bias accumulation across rounds

## Convergence Theory

Q-ANCHOR convergence proof shows:
- Mitigates classical client drift (standard FL convergence rate)
- Actively reduces hardware-bias floor (quantum-specific improvement)
- Achieves significantly more stable training than conventional FL baselines

## Implementation Pattern

```python
# Pseudocode for Q-ANCHOR server update
def q_anchor_server_update(client_gradients, noise_scales=[1, 2, 3]):
    # Collect gradient measurements at multiple noise levels
    noisy_averages = []
    for scale in noise_scales:
        scaled_gradients = [scale_noise(g, scale) for g in client_gradients]
        noisy_averages.append(average(scaled_gradients))
    
    # ZNE extrapolation to zero noise
    zne_corrected = richardson_extrapolation(noisy_averages, noise_scales)
    
    return zne_corrected
```

## Key Metrics

- **Hardware bias floor**: Persistent error from quantum noise, measured via shadow circuits
- **Client drift**: Divergence between local and global optima, measured via gradient norm difference
- **ZNE effectiveness**: Ratio of corrected vs uncorrected gradient variance

## Pitfalls

- **ZNE overhead**: Requires multiple noise scale evaluations per round → 3-5x circuit execution cost
- **Shadow circuit design**: Must match parameterized ansatz to be useful for bias estimation
- **Non-IID + noise coupling**: Both effects interact non-linearly; cannot treat independently

## Related Skills

- `qml-adversarial-robustness-verification` - QML model robustness verification
- `quantum-adversarial-defense` - Quantum adversarial defense patterns
- `federated-quantum-medical-diagnosis` - Federated QNN for medical diagnosis

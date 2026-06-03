---
name: quantum-federated-security-cult
description: "Quantum Federated Learning security analysis methodology - CULT (CircUit-Level backdoor Threat) model for analyzing and defending against circuit-level backdoor attacks in QFL systems. Covers Grover, Pauli, Bit-flip, and Sign-flip attack mechanisms, stealthiness analysis under smoothness assumptions, and defense evaluation (Krum, Multi-Krum, FoolsGold, FLGuardian, Mud-HoG). Trigger: quantum federated learning security, QFL backdoor, circuit-level attack, quantum federated security."
---

# Quantum Federated Learning Security (CULT Model)

Security analysis methodology for Quantum Federated Learning (QFL) systems based on the CircUit-Level backdoor Threat (CULT) model from arXiv:2605.27416.

## Core Contribution

First formalized threat model for circuit-level backdoor attacks in QFL systems. QFL inherits federated optimization vulnerabilities while introducing a new attack surface from variational circuit training and measurement-driven gradients.

## Attack Taxonomy (CULT Model)

### Four Stealthy Attack Types

1. **Grover Attack**: Exploits amplitude amplification to embed malicious patterns in quantum state preparation
2. **Pauli Attack**: Applies targeted Pauli gate perturbations to shift measurement outcomes
3. **Bit-flip Attack**: Flips qubit states during parameterized circuit execution
4. **Sign-flip Attack**: Reverses phase in superposition states to manipulate gradient directions

### Attack Surfaces

- **In-training**: Malicious clients inject corrupted variational parameters during federated averaging
- **Post-training**: Backdoor insertion after model convergence, exploiting measurement-based gradient computation

### Stealthiness Guarantee

Under standard smoothness assumptions, malicious updates maintain proximity to benign update norms:
- Attack vectors constrained within epsilon-ball of legitimate parameter space
- Gradient magnitude statistics match honest client distributions
- Detection evasion via norm-constrained perturbation

## Key Findings

### Empirical Results (MNIST, CIFAR-10)

| Metric | Finding |
|--------|---------|
| Single malicious client accuracy drop | Up to 50% |
| Non-IID data impact | Amplifies attack effectiveness |
| FedAvg vulnerability | No inherent defense against circuit-level attacks |
| Defense failure rate | All tested defenses fail worst-case scenarios |

### Defense Evaluation

| Defense | Effectiveness | Limitation |
|---------|--------------|------------|
| Krum | Partial reduction | Fails on worst-case |
| Multi-Krum | Moderate | Cannot eliminate 50% drops |
| FoolsGold | Limited | Masked by norm proximity |
| FLGuardian | Partial | Evaded by smooth perturbations |
| Mud-HoG | Partial | Insufficient for QFL specifics |

## Security Analysis Framework

### Step 1: Threat Surface Identification
```
Map QFL architecture:
- Variational circuit parameters (theta)
- Measurement operators (M)
- Gradient computation: grad_theta = d/d_theta <psi(theta)|M|psi(theta)>
- Aggregation mechanism (FedAvg, etc.)
- Attack vectors: parameter injection, measurement manipulation, gradient poisoning
```

### Step 2: Attack Vector Formalization
```python
# CULT attack model
def cult_attack(benign_params, attack_type, epsilon):
    if attack_type == 'grover':
        return grover_amplification_poison(benign_params, epsilon)
    elif attack_type == 'pauli':
        return pauli_gate_perturbation(benign_params, epsilon)
    elif attack_type == 'bit_flip':
        return qubit_bit_flip(benign_params, epsilon)
    elif attack_type == 'sign_flip':
        return phase_sign_flip(benign_params, epsilon)
```

### Step 3: Stealthiness Verification
```
Verify: ||malicious_update - benign_mean|| <= epsilon
Verify: gradient_magnitude in [q1, q3] of honest distribution
Verify: parameter perturbation within smoothness bound
```

### Step 4: Defense Testing
```
For each defense mechanism:
1. Run with honest-only baseline
2. Inject CULT attack (vary malicious client fraction)
3. Measure accuracy degradation
4. Identify failure modes
5. Determine minimum detection threshold
```

## Systems Engineering Implications

### Reliability Concerns
- QFL systems cannot assume classical FL security guarantees transfer
- Circuit-level attacks are orthogonal to data poisoning
- Measurement-driven gradients create unique attack surface not present in classical FL

### Design Recommendations
1. **Multi-layer verification**: Cross-check parameter updates against both norm AND circuit structure constraints
2. **Quantum-aware anomaly detection**: Defenses must account for quantum parameter space geometry
3. **Redundant aggregation**: Combine multiple aggregation strategies (Krum + norm-based + structure-based)
4. **Circuit provenance tracking**: Maintain audit trail of circuit modifications across federation rounds
5. **Worst-case robustness**: Design for single-client catastrophic failure scenarios

## Application Domains

- Quantum federated learning systems
- Hybrid quantum-classical distributed training
- Multi-party quantum machine learning
- Quantum edge computing networks
- Distributed quantum sensor networks

## Related Patterns

- [[quantum-error-correction-methods]] - QEC for fault-tolerant quantum computation
- [[hamiltonian-qkd-routing]] - Quantum network routing and security
- [[federated-quantum-medical-diagnosis]] - Privacy-preserving quantum FL for healthcare

## arXiv Reference

- **arXiv:2605.27416** - "Can Quantum Federated Learning Withstand Circuit-Level Backdoors?"
- Categories: quant-ph, cs.CR, cs.LG
- Published: May 2026

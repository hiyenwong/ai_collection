---
name: quantum-fisher-privacy-duality
description: "Quantum Fisher Information (QFI) duality framework for quantum differential privacy. Use when designing privacy-preserving quantum machine learning systems, quantum differential privacy mechanisms, or quantum metrology-privacy trade-offs. Covers QFI-aligned noise injection, privacy-utility uncertainty relations, and hardware noise harnessing. Activation keywords: quantum differential privacy, QFI, quantum privacy, quantum Fisher information, quantum DP, privacy amplification, quantum embedding, quantum metrology privacy, geometry-aware DP, quantum state distinguishability."
---

# Quantum Fisher Information Privacy Duality

Based on arXiv:2605.24166 "Optimal Quantum Differential Privacy via Fisher Information Spectral Analysis"

## Core Principle

The Quantum Fisher Information (QFI) metric governs a **fundamental duality**: it quantifies both (1) how precisely a parameter can be estimated (metrology) and (2) how distinguishable two quantum states are (privacy). This duality enables geometry-aware quantum differential privacy.

## Key Theorems & Patterns

### 1. QFI-Aligned Noise Injection (Minimax-Optimal Mechanism)

Instead of isotropic depolarizing noise, concentrate noise budget in the **dominant QFI eigenmode**:

```
epsilon = (Delta^2 / 2) * lambda_max * (1 - c * gamma)
```

Where:
- `Delta`: sensitivity of the query
- `lambda_max`: largest eigenvalue of the QFI matrix
- `gamma`: alignment factor between noise direction and QFI eigenstructure
- Advantage: `O(d / lambda_max)` over isotropic noise

### 2. Mixed-State QFI Decomposition

- **Dephasing in adversary's basis** → *increases* accessible information (vulnerability)
- **Misaligned-basis dephasing** → *constructive privacy amplification* from hardware noise

Design rule: align dephasing basis *away* from the adversary's measurement basis.

### 3. Privacy-Utility Uncertainty Relation

```
epsilon * (1 - F) >= (Delta^2 / 2) * Tr(F) / d
```

Where `F` is the quantum Fisher information matrix and `d` is the Hilbert space dimension. This provides a hard lower bound on the privacy-utility trade-off.

### 4. Adaptive QFI Estimation

- Converges at `O(1/sqrt(n))` samples
- Yields `1.92x` tighter privacy bounds vs. fixed estimation
- Update QFI estimate periodically during training

### 5. QFI-Aligned Composition

- Standard DP composition: `O(k)` for k queries
- QFI-aligned composition: **saturates at `O(1)`**
- Key: track cumulative QFI budget across composition

### 6. Hardware Noise as Privacy Amplifier

Hardware noise on real quantum devices can be **harnessed** for privacy amplification rather than mitigated. Validate privacy guarantees against actual hardware noise profiles.

## Implementation Patterns

### QFI-Aligned DP Mechanism

```python
def qfi_aligned_noise(state, qfi_matrix, epsilon, delta_sensitivity):
    """Apply direction-dependent noise aligned to QFI eigenstructure."""
    eigenvalues, eigenvectors = np.linalg.eigh(qfi_matrix)
    # Concentrate noise in dominant eigenmode
    noise_budget = (delta_sensitivity**2 / 2) * eigenvalues[-1]
    noise = np.random.normal(0, np.sqrt(noise_budget / eigenvalues[-1]))
    return state + eigenvectors[:, -1] * noise
```

### Privacy-Utility Trade-off Check

```python
def check_privacy_utility_bound(epsilon, fidelity, qfi_trace, dimension):
    """Verify the privacy-utility uncertainty relation holds."""
    delta_sq = 1.0  # sensitivity squared
    lower_bound = (delta_sq / 2) * qfi_trace / dimension
    return epsilon * (1 - fidelity) >= lower_bound
```

## When to Use

- Designing quantum DP mechanisms for QML models
- Analyzing privacy guarantees of quantum embeddings
- Optimizing privacy-utility trade-offs in quantum federated learning
- Leveraging hardware noise for privacy amplification
- Quantum metrology with privacy constraints (e.g., distributed sensing)

## Validation Results (from paper)

- IBM Quantum hardware (ibm_fez, 156 qubits): equivalent utility at **epsilon ~ 0.001** vs **epsilon ~ 4800** for classical DP
- Qiskit Aer GPU simulations confirm O(1) composition saturation

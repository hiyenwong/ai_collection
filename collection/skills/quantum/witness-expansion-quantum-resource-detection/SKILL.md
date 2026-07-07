---
name: witness-expansion-quantum-resource-detection
description: "Witness Expansion framework for detecting quantum resources in mixed states using polynomial criteria"
category: quantum-information
arxiv_id: "2606.27105"
trigger_words: ["witness expansion", "quantum resource detection", "mixed-state resource", "stabilizer entropy", "entanglement witness", "nonstabilizerness", "quantum magic detection", "fermionic non-Gaussianity"]
date_created: "2026-06-29"
---

# Witness Expansion Framework for Quantum Resource Detection

## Overview

Witness Expansion is a unified framework for constructing **nonlinear criteria** for detecting quantum resources associated with a well-defined group of free unitaries. These criteria apply to **both pure and mixed quantum states** and are based on **polynomial functions** of the target state.

**arXiv**: 2606.27105 (June 2026)
**Authors**: Yifan Tang, Chengkai Zhu, Yuzhen Zhang, Jens Eisert, Zi-Wen Liu, Ingo Roth, Otfried Gühne, Xin Wang, Zhenhuan Liu

## Core Methodology

### 1. Free Unitary Group Definition

Define a set of free unitaries $\mathcal{U}$ that generate the set of free states:
- $\mathcal{F} = \{ U |\phi\rangle\langle\phi| U^\dagger : U \in \mathcal{U}, |\phi\rangle \in \mathcal{F}_{\text{pure}} \}$
- The framework works for any resource where free states form a convex set invariant under $\mathcal{U}$

### 2. Polynomial Witness Construction

For a resource detection witness $W$, construct polynomial moments:
- $p_k(\rho) = \text{Tr}(\rho^{\otimes k} W_k)$ where $W_k$ is a Hermitian operator on $k$ copies
- These moments can be estimated experimentally using **multiple copies** of the state
- Nonlinear functions of moments detect resources that linear witnesses miss

### 3. Unified Resource Detection

The framework recovers and unifies several known resource detection quantities:

| Resource | Witness Quantity | Measurement |
|----------|-----------------|-------------|
| Coherence | $l_2$ norm of coherence | $\text{Tr}(\rho^2) - \sum_i \langle i|\rho|i\rangle^2$ |
| Entanglement | Partial-transpose moments | $\text{Tr}((\rho^{T_A})^k)$ |
| Nonstabilizerness (Magic) | Stabilizer entropy | $\text{Tr}(\rho \Pi_{\text{stab}})$ |
| Fermionic Non-Gaussianity | Fermionic antiflatness | Polynomial in fermionic correlators |

### 4. New Detection Criteria

The framework yields **new criteria** for:
- **Qubit and qudit magic states**: Enhanced witness-based detection beyond existing methods
- **Mixed-state fermionic non-Gaussianity**: First analytical criterion with respect to convex hull of pure fermionic Gaussian states, nontrivial for arbitrary qubit numbers

## Implementation Steps

### Step 1: Identify Free Unitary Group

```python
def identify_free_unitaries(resource_type):
    """Map resource type to its free unitary group"""
    groups = {
        'coherence': 'Incoherent unitaries (diagonal + permutation)',
        'entanglement': 'Local unitaries (tensor product)',
        'stabilizer_magic': 'Clifford group',
        'fermionic_gaussianity': 'Gaussian unitaries (Bogoliubov transformations)',
    }
    return groups.get(resource_type)
```

### Step 2: Construct Polynomial Moments

```python
def construct_witness_moments(rho_copies, resource_type, order_k):
    """
    Construct k-th order polynomial witness moments
    rho_copies: tensor product of k copies of state rho
    resource_type: type of quantum resource to detect
    order_k: number of copies needed
    """
    # For entanglement: partial transpose moments
    # For magic: stabilizer projector moments
    # For coherence: dephased state moments
    pass
```

### Step 3: Experimental Estimation

- Use **SWAP tests** or **Bell measurements** on multiple copies
- Estimate $\text{Tr}(\rho^k)$ via randomized measurements
- For entanglement: classical shadows with partial transpose
- For magic: stabilizer measurements + randomized benchmarking

### Step 4: Threshold Comparison

- Compute polynomial witness value $w(\rho)$
- Compare against free state bound: $w(\rho) > \max_{\sigma \in \mathcal{F}} w(\sigma)$
- Violation certifies presence of resource

## Key Insights

1. **Nonlinearity is power**: Linear witnesses are limited; polynomial witnesses detect resources in mixed states that linear methods miss entirely

2. **Experimental accessibility**: All witness moments can be estimated with multi-copy measurements — no full tomography needed

3. **Unified perspective**: Coherence, entanglement, magic, and fermionic non-Gaussianity all emerge as special cases of the same framework

4. **Scalability**: For magic states, the framework provides detection criteria that remain efficient as system size grows

## Applications

- **Quantum device benchmarking**: Verify resource preparation in NISQ devices
- **Quantum phase transitions**: Detect changes in resource content across phase boundaries
- **Quantum advantage certification**: Certify non-classical resources needed for computational advantage
- **Quantum error correction**: Detect residual errors by monitoring resource degradation

## Activation

Use this skill when:
- Analyzing quantum resource detection methods
- Working with mixed-state quantum states
- Benchmarking quantum device resource preparation
- Studying nonstabilizerness/magic states
- Investigating entanglement in mixed states
- Designing resource detection experiments

## References

- Tang, Y. et al. "Witness expansion: A unified framework for analytical and measurable mixed-state resource detection" arXiv:2606.27105 (2026)

---
name: optimal-ansatz-free-hamiltonian-learning
description: "Optimal ansatz-free Hamiltonian learning methodology — control-free, ancilla-free algorithm using randomized-sampling framework with band-limited kernel-based time sampling and displacement sieve for Hamiltonian structure learning. Use for quantum device calibration, signal sensing, and error correction."
metadata:
  arxiv_id: "2606.19486"
  published: "2026-06-17"
  authors: "Taiqi Zhou, Weiyuan Gong"
---

# Optimal Ansatz-free Hamiltonian Learning

## Core Methodology

### Randomized-Sampling Framework
- Learns ansatz-free Hamiltonian H with ||H|| ≤ Λ in total evolution time Θ(Λ/ε² log(Λ/ε))
- Proves matching lower bound Ω(Λ/ε² log(Λ/ε)) for any control-free protocol
- Uses only Pauli product state preparation and measurement — no ancilla, no interleaved control

### Key Innovations
- **Band-limited kernel-based time sampling**: Characteristic probe time resolution depends only on Λ (not ε), making protocol practical for high-precision regimes
- **Displacement sieve**: Efficiently extracts Hamiltonian structure from sampled measurements
- Maintains optimal asymptotic cost under SPAM noise for local Hamiltonians

### Comparison to Prior Work
| Aspect | Prior Heisenberg-limited | This Work |
|--------|------------------------|-----------|
| Circuit depth | Deep circuits with interleaving probes | Control-free, ancilla-free |
| Time resolution | Extremely short (ε-dependent) | Λ-dependent only |
| State prep | Complex probe states | Pauli product states |

## Activation Keywords
- Hamiltonian learning, hamiltonian characterization
- Quantum device calibration, quantum sensing
- Ansatz-free learning, control-free learning
- 哈密顿量学习，量子设备标定

## Usage Patterns

### Pattern 1: Quantum Device Calibration
When calibrating unknown quantum hardware: use randomized-sampling framework instead of deep-circuit protocols for experimental feasibility.

### Pattern 2: High-Precision Sensing
In high-precision regimes where ε << Λ: band-limited kernel sampling avoids the ε-dependent time resolution bottleneck.

### Pattern 3: Local Hamiltonian Structure Learning
For systems known to be local: the displacement sieve efficiently extracts local interaction terms from Pauli measurements.

## Pitfalls
- Lower bound applies only to control-free protocols — protocols with full control can potentially beat the bound
- SPAM noise robustness proven only for local Hamiltonians after calibration
- Total evolution time scales as Λ/ε² — becomes expensive for large Hamiltonian norms or very high precision

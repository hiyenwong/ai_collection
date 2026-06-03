---
name: causal-nonseparability-dephasing
description: "Causal nonseparability robustness under dephasing — quantum processes with indefinite causal order (quantum switch) retain causal nonseparability if any non-future system remains undephased, but become causally separable when all systems or only the future system is undephased. arXiv:2605.22807"
category: ai_collection
---

# Causal Nonseparability Under Dephasing

**Paper**: How many systems can be dephased before the quantum switch becomes causally definite?  
**arXiv**: [2605.22807](https://arxiv.org/abs/2605.22807) (Benhaj, Sengupta, Branciard, May 2026)  
**Category**: Quantum Information Science, Quantum Foundations

## Core Insight

Quantum processes with **indefinite causal order** (causally nonseparable processes) exhibit advantages over fixed-order quantum circuits. The robustness of causal nonseparability under dephasing follows a sharp threshold pattern.

## Methodology

### Bipartite Processes (Open Past and Future)

1. **All systems dephased** → Process becomes causally separable
2. **Only future system undephased** → Process becomes causally separable
3. **Any single non-future system undephased** → Causal nonseparability can persist

### Multipartite Case (QC-QCs)

For quantum circuits with quantum control (QC-QCs):

1. **Dephasing all systems** → Any QC-QC becomes causally separable
2. **Only future system undephased** → Any QC-QC becomes causally separable
3. **Any non-future system left undephased** → Causal nonseparability can persist

## Key Findings

### Robustness Threshold

- **Critical systems**: Past and intermediate systems are essential for maintaining causal nonseparability
- **Future system alone is insufficient**: Keeping only the future system undephased destroys indefinite causal order
- **Single non-future system suffices**: Even one preserved non-future system can maintain causal nonseparability

### Design Implications

1. **Quantum network design**: Protect non-future systems to preserve indefinite causal order
2. **Error correction priority**: Focus decoherence protection on past/intermediate systems, not future
3. **Resource efficiency**: Minimal system preservation needed for causal nonseparability

## Use Cases

- **Quantum switch protocols**: Design robust indefinite causal order circuits
- **Quantum communication**: Leverage causal nonseparability for channel advantages
- **Quantum metrology**: Use indefinite causal order for precision measurements
- **Distributed quantum computing**: Optimize resource allocation for causal order preservation

## Activation

causal nonseparability, quantum switch, indefinite causal order, dephasing, decoherence, QC-QC, quantum control, quantum causality, quantum process matrix

## Related

- `quantum-network-control` - Quantum network entanglement distribution
- `distributed-quantum-computing` - Distributed quantum computing architecture
- `quantum-information-protocol-analyzer` - Quantum protocol analysis

---
name: experimental-quantum-key-distribution-indefinite-causal-order
description: A skill for understanding and applying the methods from the arXiv paper: Experimental Quantum Key Distribution in an Indefinite Causal Order (arXiv: 2608.13561v1)
trigger_words: experimental quantum key distribution, indefinite causal order, quantum switch, arxiv-2608.13561
---

# Experimental Quantum Key Distribution in an Indefinite Causal Order

**arXiv ID**: 2608.13561v1
**Authors**: Yann Valibouse, Martí Cladera-Rosselló, Michael Antesberger, Hector Spencer-Wood, Kyrylo Simonov, Patrik Sund, Mathieu Bozzio, Philip Walther, Lee A. Rozema
**Date**: 2026-08-13

## Core Methodology

This paper presents an experimental implementation of quantum key distribution (QKD) protocol that leverages indefinite causal order through a photonic quantum SWITCH. The key innovation is placing Alice and Bob's measurement-and-preparation operations in superposition of different causal orders.

### Key Contributions
- **Quantum SWITCH Implementation**: BB84-like quantum cryptography with operations embedded within a quantum SWITCH
- **Eavesdropper Detection Without Key Disclosure**: Achieves average eavesdropper detection probability of 0.15 ± 0.02 per shared qubit through control qubit measurements rather than comparing key material
- **Novel Measurement Technique**: New method to measure photon polarization inside the quantum SWITCH without destroying path coherence
- **Resource Efficiency**: Every retained qubit can potentially be tested for eavesdropping while remaining available for key generation

## Technical Details

The protocol differs from standard BB84 by not requiring public revelation and discarding of key fractions for eavesdropping detection. Instead, it uses measurements of the control qubit to detect eavesdropping attempts.

## Limitations

The current implementation requires post-selection for measurements within the quantum SWITCH, so it doesn't yet constitute a fully secure QKD protocol. However, it provides proof-of-principle that indefinite causal order can be exploited for eavesdropping detection.

## Applications

- Quantum cryptography protocols leveraging indefinite causal order
- Resource-efficient QKD implementations
- Fundamental tests of quantum mechanics with indefinite causal structures

## References

- [Experimental Quantum Key Distribution in an Indefinite Causal Order](https://arxiv.org/abs/2608.13561v1)
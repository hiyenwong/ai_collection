---
name: magic-entanglement-complementarity
description: "Magic-entanglement complementarity methodology — under local amplitude damping, n-qubit GHZ states lose entanglement irreversibly but magic (non-stabilizerness) can be reborn through dissipation. Stabilizer membership is not preserved by local channels, allowing system-environment duality to concentrate magic onto single qubits for distillation. arXiv:2605.22603"
category: ai_collection
---

# Magic-Entanglement Complementarity

**Paper**: Sudden death of entanglement, rebirth of magic  
**arXiv**: [2605.22603](https://arxiv.org/abs/2605.22603) (Chenfeng Cao, May 2026)  
**Category**: Quantum Information Science, Quantum Resource Theory

## Core Insight

Local Markovian noise **cannot bring entanglement back**, but it **can bring magic back**. Unlike separability, stabilizer membership is **not preserved by local channels**, allowing dissipation to push states both out of and into the stabilizer polytope.

## Methodology

### Magic-Entanglement Complementarity

Under local amplitude damping on the n-qubit GHZ family α|0ⁿ⟩ + β|1ⁿ⟩ (0 < α < β):

1. **Magic death**: State loses magic at damping strength γ₋
2. **Magic rebirth**: State regains magic at higher damping strength γ₊
3. **Entanglement death**: Entanglement is irreversibly lost at γₑ
4. **Complementarity relation**: γₑ + γ₊ = 1 for every n

This reflects a **system-environment duality** of amplitude damping.

### Key Findings

- **Reborn magic in separable states**: For small α, the reborn magic resides in a fully separable state with all proper marginals being stabilizer
- **Parity-syndrome concentration**: Parity-syndrome extraction concentrates reborn magic onto a single qubit for magic-state distillation
- **Magic-generators vs Magic-insulators**: Local dissipation divides pure stabilizer states:
  - |Φ⁺⟩ (Bell state) generates magic immediately
  - |Ψ⁺⟩ (Bell-state partner) remains stabilizer

### Practical Implications

1. **Magic-state distillation from noise**: Dissipation can be a resource, not just a liability
2. **Quantum error correction**: Understanding when noise helps vs. harms quantum resources
3. **Resource theory symmetry**: Magic and entanglement reveal symmetries invisible to either alone

## Use Cases

- **Quantum error mitigation**: Design protocols that leverage noise-induced magic rebirth
- **Magic-state distillation**: Use parity-syndrome extraction to concentrate distributed magic
- **Quantum resource theory**: Analyze complementarity between different quantum resources under noise

## Activation

magic entanglement, stabilizer polytope, magic state distillation, amplitude damping, GHZ state, quantum resource theory, non-stabilizerness, Clifford circuits, quantum error correction

## Related

- `quantum-error-correction-methods` - QEC patterns
- `quantum-ai-patterns` - Quantum AI research patterns
- `ensemble-engineering-quantum` - Quantum ensemble engineering

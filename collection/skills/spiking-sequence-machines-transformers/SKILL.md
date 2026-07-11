---
name: spiking-sequence-machines-transformers
description: "Theoretical framework showing spiking Sparse Distributed Memory and transformers share identical five functional operations (encoding, context maintenance, retrieval, storage, decoding) with cosine similarity as shared primitive. Formalizes Phase-Latency Isomorphism between sinusoidal positional encoding and spike timing. Activation: spiking transformer, sequence learning theory, phase-latency isomorphism, spike timing positional encoding, SNN transformer equivalence."
---

# Spiking Sequence Machines and Transformers

> Proves that spiking Sparse Distributed Memory (2007) and transformers (2017) independently instantiate the same five functional operations with cosine similarity as the shared retrieval primitive, formalizing Phase-Latency Isomorphism between sinusoidal positional phase and spike timing.

## Metadata
- **Source**: arXiv:2605.00662
- **Authors**: Joy Bose
- **Published**: 2026-05-01

## Core Methodology

### Key Innovation
Sequence learning reduces to **similarity-based retrieval over a temporally indexed representation space** — a universal constraint, not an architecture-specific property. Both spiking SDM and transformers implement:

1. **Encoding** — mapping input to representation
2. **Context Maintenance** — preserving temporal context
3. **Associative Retrieval** — similarity-based pattern matching
4. **Storage** — updating memory with new information
5. **Decoding** — producing output from retrieved patterns

### Phase-Latency Isomorphism

The paper proves a fundamental equivalence:
- **Sinusoidal positional phase** (transformer PE) ↔ **Spike timing** (SNN)
- They are **linearly related**
- Dot product attention is **invariant** to this mapping (up to global scale factor on positional component)

**Lemma 1**: Dot product attention is invariant to phase-latency mapping.

### Three Instantiations of Temporal Indexing
1. **Time** — absolute temporal position
2. **Phase** — sinusoidal positional encoding
3. **Rank** — learned rank-based embedding

All three are instantiations of the same computational primitive: an **ordered index** whose structure survives similarity-based retrieval.

### Empirical Findings
- **Frequency-compressed PE** fails to converge on positionally demanding copy tasks
- **Learned rank-based embedding** matches or exceeds sinusoidal encoding
- Critical property: **distance discriminability under dot-product similarity**, not sinusoidal form

## Implementation Implications

### For SNN Design
- Spike timing can substitute for positional encoding in sequence models
- Temporal coding naturally implements the same retrieval mechanism as attention
- Sparse distributed memory provides a biologically plausible sequence learning foundation

### For Transformer Design
- Positional encoding alternatives (rank-based) may outperform sinusoidal PE
- The five-operation framework provides a lens for analyzing sequence model variants
- Cosine similarity is the fundamental retrieval primitive across architectures

## Applications
- Designing spiking transformer architectures
- Understanding theoretical foundations of sequence learning
- Bridging neuroscience (SDM) and deep learning (transformers)
- Alternative positional encoding strategies
- Energy-efficient sequence processing via SNNs

## Pitfalls
- Theoretical paper — no experimental validation of proposed architectures
- Phase-latency isomorphism proven for dot-product attention only
- Does not address multi-head attention interactions
- Sparse distributed memory implementation details not provided

## Related Skills
- wta-spiking-transformer-language
- spiking-transformer-effective-dimension
- stdp-spiking-transformer-attention
- kuramoto-oscillatory-phase-encoding-vision-transformer
- attention-residuals
- kernel-hopfield-associative-memory
---
name: fped-brain-decoding
description: FPED (Functional-Network Prior-Guided Mixture-of-Experts) framework for interpretable brain decoding from fMRI. Models different functional brain networks as specialized experts with adaptive routing for visual semantic understanding. Incorporates neurobiologically grounded priors for structured network-level representation learning. Use when: decoding fMRI for image/semantic reconstruction, building brain-computer interface models, designing interpretable neuroimaging ML architectures, incorporating brain network topology into deep learning, applying MoE to neuroimaging data, or studying functional brain network contributions to cognition. Activation: FPED, fMRI decoding, functional brain network, brain network MoE, interpretable brain decoding, visual reconstruction fMRI, brain topology deep learning
---

## FPED Framework

FPED addresses limitations of flat fMRI decoding by explicitly modeling functional brain networks as specialized experts with adaptive routing.

### Problem Addressed

Conventional fMRI decoding flattens signals from visual cortices into 1D vectors, disrupting brain network topology and losing interpretability. FPED preserves network structure.

### Architecture

```
fMRI Volumes → Functional Network Partitioning → Expert Networks (per network)
             → Adaptive Routing → Semantic Latent Space → Image Reconstruction
```

### Key Design Principles

1. **Functional Network Priors**: Each expert corresponds to a known functional brain network
2. **Adaptive Routing**: Learned weights determine each network's contribution to specific semantic dimensions
3. **Biological Interpretability**: Routing dynamics reveal correspondence between functional networks and modality-specific processing
4. **Parameter Efficiency**: Achieves competitive performance with only 0.68B parameters

### Expert Networks

Each functional brain network (e.g., visual, default mode, attention, language) becomes a specialized expert:
- Experts process their assigned network's fMRI signals
- Routing module learns to weight expert contributions adaptively
- Routing patterns are interpretable: they reflect which brain networks contribute to which semantic features

### Routing Interpretation

- Routing weights indicate functional network importance for specific decoding tasks
- Biologically meaningful patterns emerge: visual networks route to visual semantics, language networks to text-related features
- Enables transparent analysis of brain-computer interface decision pathways

### Integration Notes

- Replace flat fMRI vectorization with network-aware expert processing
- Routing module is end-to-end differentiable
- Compatible with CLIP or other vision-language latent spaces
- Particularly effective when neuroscientific interpretability is required alongside performance

### When to Apply

- fMRI-to-image or fMRI-to-text reconstruction tasks
- Building BCIs where interpretability matters
- Studying distributed functional network contributions to cognition
- Any neuroimaging task where brain topology should be preserved in the model

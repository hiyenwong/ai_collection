---
name: bcpnn-native-explainability
description: >
  BCPNN (Bayesian Confidence Propagation Neural Network) native explainability
  framework. First XAI taxonomy for BCPNN, mapping architectural primitives to
  attribution, prototype, concept, counterfactual, and mechanistic explanations.
  Introduces 16 architecture-level explanation primitives (P1–P16) computed from
  quantities the model already maintains, plus 5 design-time Configuration-as-
  Explanation primitives (Config-P1 to Config-P5). Addresses EU AI Act compliance
  for brain-like neural networks, neuromorphic-friendly sparsity, and edge
  deployment. Activation: bcpnn explainability, bayesian confidence propagation,
  brain-like AI explainability, BCPNN XAI, EU AI Act neural network,
  neuromorphic explainability, interpretable brain-like AI.
---

# BCPNN Native Explainability Framework

**Paper:** Native Explainability for Bayesian Confidence Propagation Neural Networks: A Framework for Trusted Brain-Like AI
**arXiv:** 2605.11595 [cs.AI]
**Authors:** Georgios Makridis, Georgios Fatouros, John Soldatos, George Katsis, Dimosthenis Kyriazis

## Motivation

The EU AI Act (fully applicable August 2026) creates urgent demand for
trustworthy, transparent AI — especially on resource-constrained edge devices.
BCPNNs have re-emerged as credible alternatives to backpropagation DNNs,
offering state-of-the-art unsupervised learning, neuromorphic sparsity, and
existing FPGA implementations. But no systematic XAI framework existed — until now.

## Key Insight

BCPNN is **inherently transparent** — its architectural primitives map directly
onto established XAI families. No post-hoc explanation needed; explanations are
native to the model.

## Contribution 1: XAI Taxonomy for BCPNN

Maps BCPNN quantities to explanation modalities:

| BCPNN Quantity | XAI Modality |
|---------------|-------------|
| Weights | Attribution |
| Biases | Attribution |
| Hypercolumn posteriors | Prototype |
| Structural-plasticity usage scores | Concept |
| Attractor dynamics | Mechanistic |
| Input-reconstruction populations | Counterfactual |

## Contribution 2: 16 Explanation Primitives (P1–P16)

Architecture-level explanations computed from quantities the model already maintains:
- **No additional computation** needed during inference
- Several primitives have no analogue in standard ANNs
- Closed-form algorithms for each primitive
- Cover: attribution, prototype, concept, counterfactual, mechanistic modes

## Contribution 3: Configuration-as-Explanation (Config-P1 to Config-P5)

Five design-time primitives treating BCPNN hyperparameter choices as auditable
pre-deployment explanation artifacts:
- Document architectural decisions as explanations
- Enable regulatory compliance auditing
- Provide pre-deployment transparency

## Contribution 4: Industrial Integration Roadmap

- EU AI Act alignment pathway
- Edge deployment feasibility
- Industry 5.0 implications
- IoT deployment patterns

## When to Use

- Designing explainable brain-like neural networks
- EU AI Act compliance for neural network systems
- Edge/neuromorphic AI deployment requiring transparency
- BCPNN-based systems needing interpretability
- Comparing brain-inspired vs. backpropagation approaches for trustworthiness

## Relation to Standard ANNs

| Standard ANN XAI | BCPNN Native Equivalent |
|-----------------|----------------------|
| Gradient-based attribution (GradCAM, etc.) | BCPNN weights + posteriors (intrinsic) |
| Post-hoc LIME/SHAP | Built-in explanation primitives |
| Attention visualization | Hypercolumn attractor dynamics |
| Concept activation vectors (TCAV) | Structural-plasticity usage scores |

## Implementation Notes

- BCPNN maintains all explanation quantities during normal operation
- No separate explanation pass needed
- FPGA implementations already exist for edge deployment
- Primitives are closed-form — computable from existing model state

## Related Skills

- **bispikclm-binary-spiking-llm**: Another brain-inspired architecture
- **neuro-grounded-foundation-models**: Brain-inspired model foundations

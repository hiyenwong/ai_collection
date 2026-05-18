---
name: native-explainability-bcpnn
description: "First XAI taxonomy for BCPNN mapping architectural primitives to 16 explanation primitives (P1-P16) and 5 design-time Configuration-as-Explanation primitives. Inherently transparent brain-like neural network with EU AI Act compliance."
---

# Native Explainability BCPNN

## Description

Framework for native explainability in Bayesian Confidence Propagation Neural Networks (BCPNN). Maps BCPNN architectural primitives (weights, posteriors, attractor dynamics) to 16 explanation primitives and 5 Configuration-as-Explanation design-time primitives. Provides inherently transparent brain-like neural networks compliant with EU AI Act requirements.

Based on: "Native Explainability for Bayesian Confidence Propagation Neural Networks: A Framework for Trusted Brain-Like AI" (arXiv: 2605.11595) by Makridis et al., May 2026.

## Activation Keywords

- BCPNN explainability
- native XAI brain-like
- configuration-as-explanation
- Bayesian confidence propagation XAI
- EU AI Act neural networks
- inherently transparent neural network
- 贝叶斯置信传播可解释性
- 原生可解释脑类AI

## Core Framework

### 16 Explanation Primitives (P1-P16)

BCPNN inherently maps its architectural elements to XAI modalities:

| Primitive Category | Explanation Type | BCPNN Element |
|-------------------|-----------------|---------------|
| **Attribution** | Feature importance, saliency | Weights (confidence values) |
| **Prototype** | Representative examples | Attractor states |
| **Concept** | High-level concept activation | Posterior probabilities |
| **Counterfactual** | What-if analysis | Alternative attractor basins |
| **Mechanistic** | Internal process explanation | Bayesian update dynamics |

### 5 Configuration-as-Explanation Primitives

Design-time configuration that provides runtime explainability:

1. **P1**: Weight configuration as feature attribution
2. **P2**: Attractor landscape as concept space
3. **P3**: Posterior distributions as confidence scores
4. **P4**: Bayesian update path as decision trace
5. **P5**: Network topology as dependency graph

## Implementation Patterns

### Pattern 1: BCPNN with Native Attribution

```python
class BCPNNExplainer:
    """BCPNN with native explainability primitives."""
    
    def __init__(self, n_features, n_classes):
        # BCPNN stores log-likelihood ratios as weights
        self.weights = np.zeros((n_features, n_classes))
        self.bias = np.zeros(n_classes)
        self.posteriors = np.zeros(n_classes)
        
    def fit(self, X, y):
        """Learn weights from data using Bayesian estimation."""
        # Co-activation statistics
        co_activation = X.T @ one_hot(y)
        # Convert to log-likelihood ratios (BCPNN weights)
        self.weights = np.log(co_activation + eps) - np.log(1.0 - co_activation + eps)
        
    def explain(self, x):
        """Generate all 16 explanation primitives."""
        explanations = {}
        
        # P1-P4: Attribution (feature importance)
        attributions = self.weights.T @ x
        explanations['attribution'] = attributions
        
        # P5-P8: Prototype (attractor states)
        explanations['prototype'] = self.get_nearest_attractor(x)
        
        # P9-P12: Concept (posterior probabilities)
        logits = self.weights.T @ x + self.bias
        self.posteriors = softmax(logits)
        explanations['concept'] = self.posteriors
        
        # P13-P16: Counterfactual
        explanations['counterfactual'] = self.find_counterfactual(x)
        
        return explanations
```

### Pattern 2: EU AI Act Compliance

```python
def ai_act_compliance_report(explanations):
    """Generate EU AI Act compliance report from BCPNN explanations."""
    report = {
        'transparency_score': compute_transparency(explanations),
        'traceability': explanations['decision_trace'],
        'human_oversight': explanations['confidence_scores'],
        'risk_assessment': explanations['uncertainty_bounds'],
    }
    return report
```

## Key Advantages Over Post-Hoc XAI

| Aspect | Post-Hoc XAI | BCPNN Native XAI |
|--------|-------------|-----------------|
| **Faithfulness** | Approximation | Exact (inherent to model) |
| **Consistency** | Varies by method | Always consistent |
| **Computational Cost** | Additional overhead | Zero overhead |
| **Interpretability** | Model-specific | Brain-like intuitive |

## Pitfalls

1. **Not All Neural Networks Are BCPNN**: This framework specifically applies to BCPNN architecture; standard DNNs don't have these native explanation primitives
2. **Attractor Convergence**: BCPNN dynamics must converge to attractor states for prototype explanations to be meaningful
3. **Bayesian Priors Matter**: Explanation quality depends on appropriate prior selection during training
4. **Scalability**: BCPNN can be computationally expensive for very large networks due to co-activation statistics

## Applications

- Medical AI requiring EU AI Act compliance
- Brain-inspired AI systems with inherent transparency
- Critical decision-making systems needing explainability
- Neuroscience-AI bridge applications

## Related Skills

- `bcpnn-native-explainability` - BCPNN native explainability
- `brain-inspired-intelligence-paradigm` - Brain-like AI paradigms

## Resources

- Paper: https://arxiv.org/abs/2605.11595
- EU AI Act: European regulatory framework for AI transparency

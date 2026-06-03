---
name: ai-interpretability-dead-salmon
description: "Statistical-causal reframing of AI interpretability: treating explanations as parameters of statistical models inferred from computational traces, with uncertainty quantification and testing against alternative computational hypotheses. Inspired by the famous 'dead salmon fMRI' study. Activation: dead salmon AI, interpretability statistics, causal interpretability, explanation uncertainty, statistical AI explanation, false discovery interpretability."
---

# The Dead Salmons of AI Interpretability

> Pragmatic statistical-causal reframing of AI interpretability: explanations should be treated as statistical model parameters inferred from computational traces, tested against alternative hypotheses with quantified uncertainty — guarding against "dead salmon" artifacts in interpretability research.

## Metadata
- **Source**: arXiv:2512.18792
- **Authors**: Maxime Méloux, Giada Dirupo, François Portet, Maxime Peyrard
- **Published**: 2025-12-21
- **Category**: cs.AI

## Core Methodology

### Key Insight
The famous "dead salmon fMRI" study (Bennett et al., 2009) showed that standard statistical analyses can produce seemingly meaningful brain activation patterns from a dead fish — a cautionary tale about misapplied statistical inference. The same artifact plagues AI interpretability: feature attribution, probing, sparse auto-encoding, and causal analyses can produce plausible-looking explanations for randomly initialized neural networks.

### Statistical-Causal Reframing

1. **Explanations as Statistical Parameters**
   - Interpretability methods should be treated as statistical estimators
   - Explanations are parameters of a model, inferred from computational traces
   - Findings must be tested against explicit alternative computational hypotheses

2. **Uncertainty Quantification**
   - Go beyond measuring statistical variability due to finite input sampling
   - Quantify uncertainty with respect to the postulated statistical model
   - Report confidence intervals for attribution scores, not just point estimates

3. **Identifiability Analysis**
   - Many interpretability queries are fundamentally non-identifiable
   - Different computational hypotheses can produce identical explanations
   - Understanding identifiability limits is critical to avoiding false discoveries

4. **Testing Framework**
   - Establish null hypotheses (e.g., randomly initialized network)
   - Test explanations against these null models
   - Require explanations to exceed significance thresholds
   - Report effect sizes, not just statistical significance

### Practical Guidelines

1. **Always test against random baseline**: Does your explanation method produce meaningful results on randomly initialized networks?
2. **Report uncertainty**: Include confidence intervals or credible intervals for attribution scores
3. **Check identifiability**: Can different models produce the same explanation? If so, the explanation is ambiguous
4. **Use causal interventions**: Verify explanations by intervening on the model (e.g., ablating features)
5. **Multiple hypothesis correction**: When testing many features/neurons, apply FDR correction

### Code Example
```python
# Pseudocode for statistically rigorous interpretability
import numpy as np

def dead_salmon_test(attribution_method, model, random_model, data, n_permutations=100):
    """Test if attribution method produces meaningful results beyond random baseline."""
    
    # Get attributions on real model
    real_attributions = attribution_method(model, data)
    
    # Get attributions on random baseline
    random_attributions = attribution_method(random_model, data)
    
    # Permutation test
    null_distribution = []
    for _ in range(n_permutations):
        shuffled_data = np.random.permutation(data)
        null_attr = attribution_method(model, shuffled_data)
        null_distribution.append(np.mean(np.abs(null_attr)))
    
    # Calculate p-value
    p_value = np.mean(np.abs(real_attributions) <= np.percentile(null_distribution, 95))
    
    return {
        "real_attribution_mean": np.mean(np.abs(real_attributions)),
        "random_attribution_mean": np.mean(np.abs(random_attributions)),
        "p_value": p_value,
        "significant": p_value < 0.05
    }

def confidence_interval_attribution(attribution_method, model, data, n_bootstrap=50):
    """Bootstrap confidence intervals for attribution scores."""
    bootstrap_scores = []
    for _ in range(n_bootstrap):
        resample = data[np.random.randint(0, len(data), len(data))]
        scores = attribution_method(model, resample)
        bootstrap_scores.append(scores)
    
    bootstrap_scores = np.array(bootstrap_scores)
    ci_lower = np.percentile(bootstrap_scores, 2.5, axis=0)
    ci_upper = np.percentile(bootstrap_scores, 97.5, axis=0)
    
    return {"mean": bootstrap_scores.mean(axis=0), "ci_lower": ci_lower, "ci_upper": ci_upper}
```

## Applications
- **Feature attribution validation**: Ensure SHAP, Integrated Gradients, etc. produce meaningful results
- **Probing analysis**: Verify that probing classifiers aren't finding spurious correlations
- **Sparse auto-encoder interpretation**: Validate that learned features correspond to real concepts
- **Causal analysis**: Test causal claims with proper statistical controls
- **AI safety research**: Rigorous evaluation of model behavior explanations

## Pitfalls
- **Computational cost**: Permutation tests and bootstrapping are expensive
- **Null model choice**: The "random model" must be carefully defined
- **Multiple comparisons**: Testing many features requires correction
- **Identifiability limits**: Some questions fundamentally cannot be answered with current methods

## Related Skills
- representation-steering
- transformer-prototype-readout
- self-verification
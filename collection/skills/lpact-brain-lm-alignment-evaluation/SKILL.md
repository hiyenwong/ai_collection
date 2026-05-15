---
name: lpact-brain-lm-alignment-evaluation
description: "L-PACT (Locked Predictive-Aligned Cross-modal Testing) framework for rigorous brain-language model alignment evaluation. Goes beyond prediction scores with four evidence gates: predictive-control, relational-profile, mechanism-stripping, and reliability-bounded evaluation. Use when evaluating brain-model alignment, interpreting neural prediction scores, designing brain-AI comparison studies, or critically assessing claims of structural alignment between LLMs and brain activity. Activation: L-PACT, brain alignment, brain-language model, prediction scores, brain-AI comparison, neural prediction, alignment evaluation, brain-model alignment."
---

# L-PACT: Brain-LM Alignment Evaluation Framework

Source-audited framework for evaluating whether language model representations genuinely align with brain activity, beyond surface-level prediction scores.

## Problem

Brain-language model comparisons commonly interpret neural prediction scores (encoding model performance) as evidence that model representations capture brain-relevant language computation. L-PACT demonstrates that high prediction scores alone are insufficient — controls, baselines, and nuisance factors can produce positive results without genuine structural alignment.

## Four Evidence Gates

### 1. Predictive-Control Gate

Compare real model features against:
- Nuisance baselines (acoustic envelopes, low-level neural features)
- Severe controls (shuffled, deterministic signals)
- Brain-brain ceiling (upper bound from inter-subject reliability)

A model passes only if it significantly outperforms all controls.

### 2. Relational-Profile Gate

Test whether model-to-brain similarity profiles reproduce brain-to-brain patterns:
- Extract representational similarity structure from model features
- Compare with brain RSM (Representational Similarity Matrix)
- Validate against brain-brain relational ceiling

### 3. Mechanism-Stripping Gate

Remove suspected alignment mechanisms from the model and re-test:
- Strip predictive features (e.g., next-word prediction heads)
- Recompute held-out alignment scores post-stripping
- If scores collapse, alignment is superficial rather than structural

### 4. Reliability-Bounded Gate

Normalize all evidence against brain-brain reliability ceilings:
- Estimate test-retest reliability of neural data
- Ceiling-normalize model-to-brain scores
- Operational Turing bound: can the model pass given measurement noise limits?

## Key Findings (arXiv:2605.14025)

- 414 predictive-control rows, 2304 relational profile rows, 4320 mechanism-stripping rows, 420 brain-brain ceiling rows, 146 integrated decision rows analyzed
- Assay sensitivity confirmed: framework produces positive evidence when expected (brain-brain reliability, implanted-signal simulation)
- **No real model row passed all four gates**; all 146 integrated rows were control-explained
- Less stringent single-criterion rules would count raw positive effects, but L-PACT downgrades them because controls explain the apparent evidence

## Usage Guidelines

### When Evaluating Brain-Model Alignment

1. **Never rely solely on prediction scores** — always run control analyses
2. **Establish brain-brain ceilings** — normalize against inter-subject reliability
3. **Test nuisance alternatives** — low-level features, acoustic properties, deterministic baselines
4. **Perform mechanism stripping** — verify alignment is structural, not artifact of specific components
5. **Report control-explained taxonomy** — convert apparent positives into auditable categories

### Implementation Checklist

```python
# Pseudocode for L-PACT evaluation
def lpact_evaluate(model_features, brain_data, nuisance_baselines):
    results = {}
    
    # Gate 1: Predictive-Control
    results['predictive'] = test_against_controls(
        model_features, brain_data, 
        baselines=nuisance_baselines,
        ceiling=brain_brain_reliability(brain_data)
    )
    
    # Gate 2: Relational Profile
    results['relational'] = compare_rsm_profiles(
        model_features, brain_data,
        brain_brain_rsm=inter_subject_rsm(brain_data)
    )
    
    # Gate 3: Mechanism Stripping
    stripped = strip_prediction_head(model_features)
    results['stripping'] = test_stripped_model(stripped, brain_data)
    
    # Gate 4: Reliability Bounding
    results['reliability'] = normalize_by_ceiling(
        results['predictive'], brain_brain_reliability(brain_data)
    )
    
    # Integrated decision: ALL gates must pass
    return all(results.values())
```

## Core Takeaways

- High prediction scores ≠ structural brain alignment
- Control analyses are essential — nuisance features can mimic alignment
- Brain-brain reliability ceilings provide necessary normalization
- Mechanism stripping distinguishes genuine vs. superficial alignment
- Apparent positives should be catalogued as control-explained, not dismissed

## Related Skills

- `naturality-violation-score` — Category-theory-based brain-DNN alignment
- `computational-lesions-multilingual-language-models-separate` — Causal framework for multilingual brain-model alignment
- `brain-dnn-transformation-alignment` — Category-theoretic brain-to-DNN transformation analysis

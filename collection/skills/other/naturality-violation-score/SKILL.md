---
name: naturality-violation-score
description: "Category-theory-based brain-DNN alignment methodology using Naturality Violation Score (NVS). Goes beyond stimulus-level RSA by measuring whether brain and model preserve the same stimulus transformations. Use when: (1) evaluating brain-model alignment, (2) comparing representational dynamics, (3) analyzing transformation preservation in neural representations, (4) extending beyond RSA/DSA methods, (5) category-theoretic approaches to neuroscience. Activation: NVS, naturality violation, brain-DNN alignment, representational naturality, category theory neuroscience, transformation alignment, naturality score."
---

# Naturality Violation Score (NVS)

Brain-DNN alignment methodology using category theory to measure whether brains and models preserve the same stimulus transformations. Introduced in arXiv:2605.06420 (Kamitani, 2026).

## Core Insight

Standard alignment metrics (RSA, DSA) compare static representational geometry. NVS asks a deeper question: **do brain and model preserve the same candidate transformations among stimuli?**

## Mathematical Framework

### Approximate Naturality

Given a proxy-defined stimulus transformation T:
- **Path A**: stimulus → brain representation → translate to model → apply T
- **Path B**: stimulus → apply T → brain representation → translate to model

The naturality square **commutes** if both paths yield equivalent results.

### Naturality Violation Score

$$NVS = || f_B(T(x)) - T(f_M(x)) ||$$

Where:
- $f_B$: brain-side transformation propagation
- $f_M$: model-side transformation propagation
- $T$: stimulus transformation operator
- $||\cdot||$: chosen distance metric (typically Frobenius or spectral norm)

## Workflow

### Step 1: Define Transformation Set

Identify meaningful stimulus transformations:
- Visual: rotation, scaling, translation, contrast change
- Auditory: pitch shift, time stretch, volume change
- Abstract: semantic perturbation, style transfer

### Step 2: Extract Representations

```python
import numpy as np

def extract_representations(model, brain_data, stimuli, transformations):
    """Extract paired representations for each stimulus and transformation."""
    reps = {
        'brain': {},
        'model': {}
    }
    
    for stim in stimuli:
        reps['brain'][stim] = get_brain_response(brain_data, stim)
        reps['model'][stim] = get_model_activation(model, stim)
        
        for T_name, T_func in transformations.items():
            transformed = T_func(stim)
            reps['brain'][f'{stim}_{T_name}'] = get_brain_response(brain_data, transformed)
            reps['model'][f'{stim}_{T_name}'] = get_model_activation(model, transformed)
    
    return reps
```

### Step 3: Compute Translation Functions

```python
def compute_translation(brain_reps, model_reps, stimuli):
    """Learn linear mapping from brain to model representation space."""
    # Collect paired data
    B = np.array([brain_reps[s] for s in stimuli])
    M = np.array([model_reps[s] for s in stimuli])
    
    # Linear regression: M = W @ B + b
    B_aug = np.hstack([B, np.ones((B.shape[0], 1))])
    W = np.linalg.lstsq(B_aug, M, rcond=None)[0]
    
    def translate(brain_rep):
        return W @ np.append(brain_rep, 1)
    
    return translate
```

### Step 4: Calculate NVS

```python
def calculate_nvs(reps, translate, transformations, stimuli):
    """Compute Naturality Violation Score for each transformation."""
    nvs_scores = {}
    
    for T_name in transformations:
        violations = []
        for stim in stimuli:
            # Path A: brain → translate → apply T
            brain_transformed = reps['brain'][f'{stim}_{T_name}']
            path_a = translate(brain_transformed)
            
            # Path B: translate brain → apply T in model space
            brain_original = reps['brain'][stim]
            model_original = translate(brain_original)
            model_transformed = reps['model'][f'{stim}_{T_name}']
            path_b = model_transformed
            
            violation = np.linalg.norm(path_a - path_b)
            violations.append(violation)
        
        nvs_scores[T_name] = np.mean(violations)
    
    return nvs_scores
```

### Step 5: Interpretation

| NVS Range | Interpretation |
|-----------|----------------|
| ≈ 0 | Perfect transformation preservation |
| Low | Similar transformation dynamics |
| Medium | Partial alignment, some transformations preserved |
| High | Divergent transformation handling |

## Comparison with RSA

| Aspect | RSA | NVS |
|--------|-----|-----|
| What it measures | Static geometry similarity | Dynamic transformation preservation |
| Question answered | "Do they represent similarly?" | "Do they transform similarly?" |
| Sensitivity | Representational distances | Representational dynamics |
| Category theory | No | Yes (naturality) |

## Key Advantages

1. **Catches functional mismatches** RSA can't detect
2. **Reveals transformation-specific alignment** which transformations are preserved vs broken
3. **Theoretically grounded** in category theory naturality
4. **Complementary to RSA** use both for comprehensive alignment assessment

## Practical Tips

- Use multiple transformations to get a complete alignment profile
- Normalize representations before comparison
- Consider using spectral norm for matrix representations
- NVS is sensitive to translation quality; use regularized regression for noisy data
- Compare NVS across models to rank transformation preservation

## References

- arXiv:2605.06420 - "Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?" (Kamitani, 2026)
- Representational Similarity Analysis (RSA) - Kriegeskorte et al. (2008)
- Category Theory for Neural Representations - Gao et al. (2023)

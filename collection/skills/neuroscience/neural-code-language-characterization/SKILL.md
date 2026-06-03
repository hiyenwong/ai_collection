---
name: neural-code-language-characterization
description: Natural language characterization of neural coding methodology. Closed-loop framework using digital twins to translate neural activation patterns into semantic descriptions. Generates hypotheses via LLM, synthesizes test images, and verifies in silico. Use when: characterizing neural selectivity, interpreting neural codes, digital twin neuroscience, automated neuron characterization, V1/V4 neural analysis.
---

# Neural Code Language Characterization

Methodology for automated neural characterization using natural language and digital twins.

## Core Framework

### Digital Twin Architecture

1. Build digital twin of neural population (V1/V4)
2. Generate high-activating and low-activating images
3. Translate activation patterns to dense captions
4. Generate semantic hypotheses via LLM
5. Synthesize test images from hypotheses
6. Verify hypotheses in silico

### Semantic Description Pipeline

```python
# 1. Extract activating/suppressing images
high_activating = get_images_with_high_response(neuron, threshold=0.95)
low_activating = get_images_with_low_response(neuron, threshold=0.05)

# 2. Generate captions for image sets
high_captions = caption_images(high_activating)
low_captions = caption_images(low_activating)

# 3. Form semantic hypothesis
hypothesis = generate_hypothesis(high_captions, low_captions)

# 4. Synthesize test images
test_images = synthesize_from_hypothesis(hypothesis)

# 5. Verify hypothesis
activation = predict_response(neuron, test_images)
verified = activation > percentile_threshold
```

## Key Findings

### V1 vs V4 Characterization

- **V1 neurons**: Selectivity captured by oriented edges, spatial frequency
- **V4 neurons**: Conjunctions of form, color, and texture
- V4 activation: 96.1% driven above 95th percentile
- V4 suppression: 97.6% driven below 5th percentile
- V1 suppression less describable in language

### Representational Alignment

- Vision embeddings most aligned with neural activity
- Language embeddings show partial alignment
- Text bottleneck loses information recovered when rendered back to images
- Linguistic compression is lossy but semantically faithful

## Implementation

### LLM-Based Hypothesis Generation

```python
def generate_semantic_hypothesis(high_captions, low_captions):
    prompt = f"""
    Given images that strongly activate this neuron:
    {high_captions}
    
    And images that suppress it:
    {low_captions}
    
    Generate a concise, verifiable description of what this neuron responds to.
    Format: "This neuron responds to [feature] with [properties]"
    """
    return llm_generate(prompt)
```

### Verification Metrics

- Activation percentile against natural image distribution
- Direction selectivity index
- Circular variance
- Pinwheel density (for topographic maps)

## Applications

- Automated neural characterization at scale
- Cross-species neural comparison
- Agentic scientific discovery for neuroscience
- Interpretable neural population analysis

## Related Skills

- `neural-dynamics-universal-translator`
- `brain-foundation-model-inversion`
- `computational-neuroscience-in-llm-era`

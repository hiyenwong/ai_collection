---
name: llm-semantic-convergence-human-neural-representations
description: "LLM-Human neural semantic convergence methodology - dimension-resolved interbrain encoding modeling comparing LLM-derived and human-shared neural semantic representations across 10 semantic dimensions. Use when: LLM brain alignment, semantic representation analysis, interbrain synchronization, dimensional semantic space, neural encoding modeling, shared semantics, human-LLM comparison, MEG encoding analysis. Activation: LLM convergence, semantic alignment, neural representation, interbrain encoding, semantic dimensions, brain-LLM comparison, shared neural semantics"
metadata:
  arxiv_id: "2606.11598"
  published: "2026-06-10"
  authors: ["Chen Hong", "Ximing Shao", "Gangyi Feng"]
  tags: [neuroscience, llm, semantic, representation, alignment, meg, interbrain, encoding, convergence]
license: Complete terms in LICENSE.txt
---

# LLM Semantic Convergence with Human Neural Representations

**arXiv: 2606.11598** | Published: 2026-06-10 | Categories: q-bio.NC

## Context

Interpersonal communication requires building shared semantics that enable listeners to understand speakers' meanings. LLMs increasingly approximate human language capability and neural responses. This research addresses: **Do LLMs capture the same semantic structure shared between human brains?**

**Key Question**: Are LLM semantic representations converging with human-shared neural semantics, and if so, is this convergence selective or complete?

## Core Methodology

### 1. Ten-Dimensional Semantic Space Framework

Semantic dimensions rated for each content word:

| Dimension | Description | LLM Alignment Status |
|-----------|-------------|---------------------|
| **Perception** | Sensory experiences | Moderate alignment |
| **Motor** | Action-related | Moderate alignment |
| **Space** | Spatial relations | High alignment |
| **Time** | Temporal concepts | High alignment |
| **Socialness** | Social interactions | **Partial divergence** |
| **Animacy** | Living vs non-living | Moderate alignment |
| **Emotion** | Emotional content | **Partial divergence** |
| **Attention** | Attentional focus | Moderate alignment |
| **Causality** | Cause-effect relations | Moderate alignment |
| **Drive** | Motivational states | **Partial divergence** |

### 2. Dimension-Resolved Interbrain Encoding Modeling

**Procedure**:

```python
# Step 1: Word-level semantic dimension rating
for word in narrative_content_words:
    human_ratings[word] = [perception, motor, space, time, 
                          socialness, animacy, emotion, attention, 
                          causality, drive]
    
    # LLM ratings (5 recent LLMs)
    llm_ratings[word] = [LLM_rate(word, dim) for dim in semantic_dimensions]

# Step 2: Neural synchronization (NS) modeling
# Speaker-listener MEG pseudo-hyperscanning
for dimension in semantic_dimensions:
    # Test dimension contribution to NS beyond acoustic/phonological features
    ns_model = fit_encoding(
        speaker_semantics[dimension],
        listener_meg_response,
        baseline_features=[acoustic, phonological]
    )
    
    # Measure explained variance
    r2_dimension[dimension] = ns_model.score()

# Step 3: Representational geometry comparison
# Compare human vs LLM semantic space geometry
geometry_alignment = compare_semantic_geometry(
    human_semantic_space,
    llm_semantic_space,
    metrics=[RSA, CKA, procrustes_distance]
)

# Step 4: Model scaling analysis
# Test larger LLMs → closer human alignment
for model_size in [small, medium, large, largest]:
    alignment[model_size] = measure_convergence(
        model_size, 
        human_neural_semantics,
        dimensions=semantic_dimensions
    )
```

### 3. Individual Differences Prediction

Link neural alignment to story comprehension:

```python
# Predict listener comprehension from NS
comprehension_score = predict_from_alignment(
    neural_synchronization_strength,
    listener_behavioral_measures
)
```

## Key Findings

### Finding 1: Multidimensional Structure (Not Single Global Signal)

Shared semantics is characterized as **multidimensional neural structure**, not a single global semantic signal. Different dimensions contribute differentially to neural synchronization.

### Finding 2: LLM Dimension-Dependent Alignment

- **High alignment dimensions**: Space, Time (abstract, structural)
- **Moderate alignment**: Perception, Motor, Animacy, Attention, Causality
- **Partial divergence dimensions**: Socialness, Emotion, Drive (agency, affect, social experience)

**Pattern**: Dimensions closely tied to **agency, affect, and social experience** show largest divergences.

### Finding 3: Model Scaling Improves Approximation

**Larger LLMs** → closer alignment with human semantic structure:

- Greater overlap in semantic geometry
- Higher NS prediction accuracy
- BUT: incomplete convergence even for largest models
- Convergence remains **selective**, not complete

### Finding 4: Comprehension Prediction

Neural alignment patterns predict individual differences in listeners' story comprehension, linking neural synchronization to cognitive performance.

## Implementation Steps

### Step 1: Define Semantic Dimensions

```python
semantic_dimensions = {
    'perception': 'Sensory experiences (visual, auditory, tactile)',
    'motor': 'Action-related concepts',
    'space': 'Spatial relations and locations',
    'time': 'Temporal concepts and sequences',
    'socialness': 'Social interactions and relationships',
    'animacy': 'Living vs non-living entities',
    'emotion': 'Emotional content and valence',
    'attention': 'Attentional focus and salience',
    'causality': 'Cause-effect relationships',
    'drive': 'Motivational states and goals'
}
```

### Step 2: Dimension Rating Protocol

```python
def rate_semantic_dimension(word, dimension, rater_type='human'):
    """
    Rate word on semantic dimension.
    
    Args:
        word: Content word from narrative
        dimension: One of 10 semantic dimensions
        rater_type: 'human' or 'llm'
    
    Returns:
        rating: Continuous score (e.g., 0-10)
    """
    if rater_type == 'human':
        # Human expert rating
        return human_rating_process(word, dimension)
    else:
        # LLM rating via prompt
        prompt = f"Rate '{word}' on {dimension} dimension (0-10)"
        return llm_generate_rating(prompt)
```

### Step 3: Interbrain Encoding Analysis

```python
def dimension_resolved_encoding(speaker_data, listener_meg):
    """
    Test dimension contribution to neural synchronization.
    
    Args:
        speaker_data: Semantic dimension ratings
        listener_meg: Listener MEG responses
    
    Returns:
        dimension_r2: Dict of dimension → explained variance
    """
    results = {}
    
    # Baseline: acoustic + phonological features
    baseline_features = extract_baseline(speaker_audio)
    
    for dimension in semantic_dimensions:
        # Full model: baseline + semantic dimension
        full_model = fit_encoding(
            features=[baseline_features, speaker_data[dimension]],
            response=listener_meg
        )
        
        # Baseline-only model
        baseline_model = fit_encoding(
            features=baseline_features,
            response=listener_meg
        )
        
        # Unique contribution of dimension
        results[dimension] = full_model.r2 - baseline_model.r2
    
    return results
```

### Step 4: Representational Geometry Comparison

```python
def compare_semantic_geometry(human_space, llm_space):
    """
    Compare semantic space geometry between human and LLM.
    
    Methods:
    - RSA (Representational Similarity Analysis)
    - CKA (Centered Kernel Alignment)
    - Procrustes distance
    """
    rsa_score = compute_rsa(human_space, llm_space)
    cka_score = compute_cka(human_space, llm_space)
    procrustes_dist = compute_procrustes(human_space, llm_space)
    
    return {
        'rsa': rsa_score,
        'cka': cka_score,
        'procrustes': procrustes_dist
    }
```

## Pitfalls

### Pitfall 1: Single Global Signal Assumption

**Error**: Treating semantic alignment as single global measure.

**Fix**: Use dimension-resolved analysis. Test each dimension's contribution separately beyond baseline features.

### Pitfall 2: Overlooking Dimension-Dependent Divergence

**Error**: Assuming complete LLM-human alignment from overall scores.

**Fix**: Check dimension-specific divergences, especially social/affective dimensions. These show largest gaps even for large models.

### Pitfall 3: Ignoring Model Scaling Effects

**Error**: Testing only one model size.

**Fix**: Compare multiple model sizes. Larger models improve alignment but remain incomplete.

### Pitfall 4: Acoustic/Phonological Confound

**Error**: Not controlling for acoustic and phonological features.

**Fix**: Include baseline model with acoustic/phonological features. Measure unique semantic dimension contribution.

### Pitfall 5: Individual Differences Ignored

**Error**: Focusing only on group-level alignment.

**Fix**: Link neural alignment patterns to individual comprehension performance.

## Verification

### Verification 1: Dimension Independence

```python
# Test dimensions are not redundant
correlation_matrix = compute_dimension_correlations(ratings)
# Expect: moderate intercorrelation, not perfect collinearity
```

### Verification 2: NS Prediction Significance

```python
# Test semantic dimensions explain NS beyond baseline
for dimension in dimensions:
    p_value = test_significance(
        full_model_score, 
        baseline_model_score
    )
    # Expect: significant unique contribution
```

### Verification 3: Geometry Alignment Scaling

```python
# Test larger models → higher alignment
alignment_scores = []
for model in models_increasing_size:
    score = measure_alignment(model, human_space)
    alignment_scores.append(score)

# Expect: monotonic increase with model size
assert is_monotonic_increasing(alignment_scores)
```

### Verification 4: Comprehension Link

```python
# Test NS predicts comprehension
correlation = correlate(neural_alignment, comprehension_scores)
# Expect: significant positive correlation
```

## References

- **Paper**: Hong, C., Shao, X., Feng, G. (2026). Large language models selectively converge with human-shared neural semantic representations. arXiv:2606.11598
- **Method**: Pseudo-hyperscanning MEG + dimension-resolved interbrain encoding
- **Semantic Dimensions**: 10-dimension framework (perception, motor, space, time, socialness, animacy, emotion, attention, causality, drive)
- **Related Skills**: See `brain-llm-alignment`, `semantic-representation-analysis`, `neural-encoding-modeling`

## Activation Keywords

- `LLM convergence`
- `semantic alignment`
- `neural representation`
- `interbrain encoding`
- `semantic dimensions`
- `brain-LLM comparison`
- `shared neural semantics`
- `dimension-resolved encoding`
- `MEG semantic analysis`
- `LLM human brain alignment`
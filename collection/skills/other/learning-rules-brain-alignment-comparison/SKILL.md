---
name: learning-rules-brain-alignment-comparison
description: "Comparative methodology for analyzing brain alignment across learning rules (backpropagation, feedback alignment, predictive coding, STDP). Tracks representational similarity analysis (RSA) alignment to human fMRI data during training. Key finding: local learning rules (PC, STDP) preserve brain-like structure better than global error signals (BP). Use when: (1) analyzing learning rule effects on neural representations, (2) understanding why untrained networks match brain activity, (3) designing biologically plausible training methods, (4) comparing representational dynamics across learning paradigms. Activation: brain alignment, RSA, learning rules comparison, backprop vs biological learning, V1 cortex, fMRI alignment, STDP, predictive coding, representational similarity."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30556"
  published: "2026-06-01"
  authors: "Author names from paper"
  tags: [neuroscience, brain-alignment, learning-rules, RSA, fMRI, backpropagation, predictive-coding, STDP, V1-cortex]
---

# Learning Rules Brain Alignment Comparison

Comparative framework analyzing how different learning rules affect representational similarity to human visual cortex during training.

## Background

Random, untrained neural networks consistently match or exceed trained networks in representational similarity to early visual cortex. This paradox challenges assumptions about learning improving brain alignment. This methodology systematically compares four learning rules to understand this phenomenon.

## Core Finding

**Key insight**: A single epoch of training reduces V1 alignment by 25-90%, depending on the learning rule:
- **Backpropagation (BP)**: Most severe degradation (delta r = -0.080)
- **Predictive Coding (PC)** and **STDP**: Better preservation (delta r ~ -0.04)
- **Feedback Alignment (FA)**: Intermediate degradation

**Interpretation**: Untrained architectures capture low-level visual statistics through inductive biases alone. Global error signals (BP) reshape early representations more aggressively than local learning rules (PC, STDP), which better preserve brain-like structure.

## Methodology

### Experimental Setup

1. **Learning rules tested**:
   - Backpropagation (BP) — global error signal
   - Feedback Alignment (FA) — random feedback weights
   - Predictive Coding (PC) — local predictive learning
   - Spike-Timing-Dependent Plasticity (STDP) — biologically plausible Hebbian rule

2. **Dataset**:
   - 720 object images from THINGS database
   - Human fMRI data from 3 subjects
   - Six visual ROIs (V1, V2, V3, V4, LOC, IT)

3. **Analysis pipeline**:
   ```
   For each learning rule:
     For each checkpoint (epochs 0-40):
       1. Extract model activations for 720 images
       2. Compute Representational Dissimilarity Matrix (RDM)
       3. Compute Spearman correlation with brain RDM
       4. Track alignment trajectory across training
   ```

4. **Alignment measurement**:
   - Spearman correlation between model RDM and brain RDM
   - Eight training checkpoints: epochs 0, 1, 5, 10, 15, 20, 30, 40
   - Separate analysis per ROI (V1 through IT cortex)

### Critical Implementation Details

**RDM computation**:
```python
def compute_rdm(activations):
    """
    Compute representational dissimilarity matrix
    
    Parameters:
        activations: [n_images, n_features] tensor
    
    Returns:
        rdm: [n_images, n_images] correlation distance matrix
    """
    # Flatten activations per image
    # Compute pairwise correlation distances
    # Return upper triangle for RSA
```

**Alignment trajectory tracking**:
```python
def track_alignment(model, brain_rdm, checkpoints, images):
    """
    Track RSA alignment across training checkpoints
    
    Returns:
        trajectory: Dict[epoch, Dict[roi, correlation]]
    """
    trajectory = {}
    for epoch in checkpoints:
        # Load model at epoch checkpoint
        # Extract activations
        # Compute model RDM
        # Compute Spearman correlation per ROI
        trajectory[epoch] = compute_spearman(model_rdm, brain_rdm)
    return trajectory
```

## Key Results

### V1 Cortex Alignment Trajectory

| Learning Rule | Epoch 0 | Epoch 1 | Epoch 40 | Delta r |
|--------------|---------|---------|----------|---------|
| BP           | 0.65    | 0.57    | 0.58     | -0.080  |
| FA           | 0.65    | 0.60    | 0.62     | -0.055  |
| PC           | 0.65    | 0.61    | 0.63     | -0.04   |
| STDP         | 0.65    | 0.61    | 0.64     | -0.04   |

**Pattern**: Initial alignment (epoch 0) identical across all rules. Local learning rules (PC, STDP) preserve ~2x more alignment than BP after training.

### Object-Selective Cortex (LOC) Trajectory

Opposite tendency: BP shows largest **increase** in alignment during training (small absolute change). This suggests global error signals may improve higher-level visual representation alignment.

### Three Key Insights

1. **Untrained networks as baseline**: Architectural inductive biases alone capture low-level visual statistics
2. **Learning rule signature**: Global vs local error signals differ in representational reshaping aggression
3. **Hierarchical specificity**: Early vs late visual cortex show opposite alignment dynamics

## Applications

### Use Case 1: Biologically Plausible Training Design

When designing training methods for brain-inspired models:
- Prefer local learning rules (PC, STDP) for early visual layers
- Consider global error signals for higher-level layers if alignment to LOC is desired
- Monitor RSA trajectory during training to avoid excessive V1 degradation

### Use Case 2: Understanding Untrained Network Paradox

When investigating why random networks match brain:
- Measure initial alignment epoch (baseline from inductive bias)
- Track degradation trajectory per learning rule
- Identify learning rule preserving most brain-like structure

### Use Case 3: Learning Rule Selection for Brain Modeling

Decision framework:
```
If task requires:
  - V1 alignment → Prefer PC or STDP
  - LOC alignment → Consider BP with monitoring
  - Balanced alignment → Hybrid approach (local early, global late)
```

## Pitfalls

1. **Subject variability**: Brain RDMs vary across individuals. Use multiple subjects (minimum 3) for statistical reliability.

2. **ROI selection sensitivity**: Alignment dynamics differ by ROI. Analyze full hierarchy (V1-V4 + LOC + IT), not single region.

3. **Image set diversity**: THINGS database (720 objects) provides good coverage. Small image sets may underrepresent visual statistics.

4. **Checkpoint frequency**: Eight checkpoints (epochs 0-40) capture trajectory. Fewer checkpoints miss rapid early degradation (epoch 0→1 shows 25-90% drop).

5. **Architectural dependence**: Results shown for standard CNN. Different architectures may alter baseline alignment epoch 0.

6. **Inverse correlation interpretation**: LOC increase during BP training is small absolute magnitude. Statistical significance requires careful interpretation.

## References

- arXiv:2605.30556 — Source paper
- THINGS database — 720 object images with fMRI
- RSA methodology — Representational Similarity Analysis
- Predictive coding theory — Local learning framework
- STDP literature — Spike-timing-dependent plasticity rules

## Related Skills

- `brain-alignment-learning-rules` — Related alignment analysis
- `predictive-coding-neural-networks` — PC implementation details
- `stdp-spiking-networks` — STDP biologically plausible learning
- `rsa-representational-similarity` — RSA methodology details
- `fmri-neural-encoding` — fMRI analysis patterns
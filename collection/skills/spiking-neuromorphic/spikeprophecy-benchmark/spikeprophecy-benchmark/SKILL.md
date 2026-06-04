---
name: spikeprophecy-benchmark
description: "SpikeProphecy: First large-scale benchmark for causal, autoregressive neural population spike-count forecasting. Introduces population metric decomposition (temporal fidelity, spatial pattern accuracy, magnitude-invariant alignment) on 105 Neuropixels sessions (~89,800 neurons). arXiv:2605.12992"
tags: ["neural-population", "forecasting", "benchmark", "neuropixels", "spike-count", "evaluation", "ssm", "transformer"]
related_skills: ["realm-lfp-retrospective-decoding", "neural-population-dynamics"]
---

# SpikeProphecy: Large-Scale Benchmark for Autoregressive Neural Population Forecasting

**Paper**: arXiv:2605.12992v1 (May 13, 2026)
**Authors**: John R. Minnick, Jinghui Geng, Kamran Hussain, Jesus Gonzalez-Ferrer, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason K. Eshraghian, Mircea Teodorescu (UC Santa Cruz)

## Problem

Neural population models (predicting joint firing of many simultaneously recorded neurons) are evaluated by a single aggregate Pearson correlation r, which:
- Masks critical structure (brain region differences, neuron subpopulation failures)
- Collapses temporal dynamics capture vs. spatial pattern fidelity
- Hides the distinction between population-level vs. individual-neuron accuracy

**No established benchmark existed** for spike-count forecasting at scale on real electrophysiology data.

## SpikeProphecy Benchmark

### Scale
- **105 Neuropixels sessions** from two public datasets:
  - Steinmetz 2019: 75 sessions, multiple brain regions
  - IBL Repeated Site: 30 sessions, repeated recording sites
- **~89,800 neurons** total
- **First large-scale autoregressive spike-count forecasting benchmark**

### Population Metric Decomposition (Core Contribution)

Instead of a single aggregate Pearson r, SpikeProphecy decomposes evaluation into three orthogonal axes:

1. **`pop_rate_r`** (Temporal Fidelity)
   - How well does the model capture population-level firing rate dynamics over time?
   - Measures temporal pattern matching across the entire population
   - Example: r_pop = 0.76 (good temporal capture)

2. **`spatial_r`** (Spatial Pattern Accuracy)
   - How well does the model capture which specific neurons are firing?
   - Measures individual neuron identity preservation
   - Example: r_spatial = 0.55 (moderate spatial capture)

3. **`cosine_sim`** (Magnitude-Invariant Alignment)
   - Directional alignment of population activity vectors, independent of magnitude
   - Captures whether the model gets the "shape" of population activity right

### Why Decomposition Matters

An aggregate r = 0.50 sounds mediocre, but decomposition reveals:
- Temporal population dynamics: r_pop = 0.76 (well captured)
- Individual neuron identity: r_spatial = 0.55 (moderately captured)

This guides targeted model improvement.

## Architecture Baselines Tested

Seven models across four structural families:

### State Space Models (SSMs) - 4 variants
1. **S4** (Structured State Space)
2. **Mamba** (Selective SSM)
3. **Griffin** (Gated SSM)
4. **RWKV** (Receptance Weighted Key Value, non-diagonal SSM)

### Other architectures
5. **Transformer** (standard attention-based)
6. **LSTM** (classic recurrent)
7. **Spiking Network** (event-driven SNN)

## Key Findings

### 1. Brain-Region Predictability Ranking
- A consistent hierarchy of brain region predictability emerges across ALL seven baselines
- Survives ANCOVA correction for firing-statistics covariates (region ΔR² = 0.018)
- Some regions are inherently more predictable than others, independent of model choice

### 2. Sub-Poisson Evaluation Floor
- Rigorous metrics combined with genuine biophysical constraints reveal a "floor"
- Regular spike trains have inherent unpredictability below Poisson level
- This is a fundamental biophysical limit, not a model limitation

### 3. KL-on-Output-Rates Distillation (Negative Result)
- ANN→SNN transfer via KL divergence on output rates does NOT work well
- In this Poisson count domain, distillation fails to preserve distributional properties
- Important negative result for the community

### 4. Linear vs. Deep Model Hierarchy
- Decomposition exposes distinct failure modes between linear and deep models
- Single-scalar reporting misses these failure mode differences entirely

## Why This Matters

### For BCI Development
- 50-100ms look-ahead predictions compensate for sensing/processing delays
- Essential for closed-loop BCIs
- Enables "digital twin" neural simulators for algorithm development without animal experiments

### For Neural Science
- Provides standardized evaluation protocol for neural population models
- Enables fair comparison across architectures
- Reveals fundamental structure in neural population predictability

## Application Protocol

### When to Use SpikeProphecy
- Evaluating neural population forecasting models
- Comparing architectures for spike-count prediction
- Building closed-loop BCI systems requiring look-ahead predictions
- Developing in silico neural population simulators
- Studying brain-region-specific neural dynamics predictability

### Metric Selection Guide
```
For temporal pattern analysis:     → pop_rate_r
For neuron-specific prediction:    → spatial_r
For population geometry:           → cosine_sim
For comprehensive evaluation:      → all three metrics
Avoid:                             → single aggregate Pearson r alone
```

### Architecture Selection Guide
```
For best overall performance:      → SSM family (Mamba, Griffin)
For interpretability:              → S4 (structured state space)
For event-driven efficiency:       → Spiking network (with caveats)
For baseline comparison:           → LSTM, Transformer
```

## Implementation Pattern

```python
class SpikeProphecyEvaluator:
    """Population metric decomposition for spike-count forecasting."""
    
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
    
    def pop_rate_r(self, predicted, actual):
        """Temporal fidelity: population-level firing rate dynamics."""
        # Sum across neurons at each timestep
        # Pearson r between predicted and actual population rates
        pred_rates = predicted.sum(axis=1)  # sum across neurons
        actual_rates = actual.sum(axis=1)
        return pearsonr(pred_rates, actual_rates)
    
    def spatial_r(self, predicted, actual):
        """Spatial pattern accuracy: individual neuron identity."""
        # Pearson r per neuron, then average
        neuron_rs = [pearsonr(predicted[:, i], actual[:, i]) 
                     for i in range(self.n_neurons)]
        return np.mean(neuron_rs)
    
    def cosine_sim(self, predicted, actual):
        """Magnitude-invariant alignment: population activity shape."""
        # Cosine similarity between population activity vectors
        return cosine_similarity(predicted, actual)
```

## Data Access

- **Steinmetz 2019**: 75 sessions, publicly available
- **IBL Repeated Site**: 30 sessions, International Brain Laboratory
- Total: ~89,800 neurons across 105 sessions

## Activation Keywords

- spike forecasting, neural population model, Neuropixels
- population metric decomposition, spike-count prediction
- autoregressive neural forecasting, closed-loop BCI
- brain region predictability, neural digital twin
- SSM for neural data, Mamba neural population
- benchmark neural population, spike prophecy

## Pitfalls

- **Don't use aggregate Pearson r alone** — it masks critical structure
- **Account for sub-Poisson floor** — some unpredictability is biophysical, not model failure
- **KL distillation fails** on output rates in Poisson count domain
- **Match temporal context** when comparing models (same look-ahead window)
- **Fire-rate covariates matter** — region predictability differences persist after ANCOVA correction

## Related Work

- **LFADS**: Latent Factor Analysis via Dynamical Systems
- **NDT/NDT2/NDT3**: Neural Decoding Transformers
- **CEBRA**: Contrastive Embedding for Brain Activity
- **S4/Mamba/Griffin**: State space model families
- **REALM** (arXiv:2605.14867): LFP-based decoding (complementary modality)

## Open Questions

- What determines brain-region predictability hierarchy?
- Can models surpass the sub-Poisson evaluation floor?
- How does forecast quality scale with session count and neuron count?
- Can the metric decomposition guide architecture search?
- What is the minimum look-ahead needed for effective closed-loop BCI?

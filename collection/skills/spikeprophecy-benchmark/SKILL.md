---
name: spikeprophecy-benchmark
description: >
  SpikeProphecy methodology for evaluating autoregressive neural population
  forecasting models. First large-scale benchmark for causal, autoregressive
  spike-count forecasting on real electrophysiology recordings. Features
  population metric decomposition (temporal fidelity, spatial pattern accuracy,
  magnitude-invariant alignment). Use when: evaluating neural forecasting models,
  designing neural population benchmarks, comparing SSM/RNN/Transformer/SNN
  architectures for spike prediction, benchmarking brain-computer interface (BCI)
  components, analyzing brain-region predictability hierarchies, or building
  neural dynamics prediction pipelines.
  Activation: spikeprophecy, neural forecasting benchmark, spike count prediction,
  neural population forecasting, autoregressive neural dynamics, BCI forecasting,
  population metric decomposition, Neuropixels benchmark.
---

# SpikeProphecy Benchmark Methodology

First large-scale benchmark for causal, autoregressive spike-count forecasting
on real electrophysiology recordings (105 Neuropixels sessions, ~89,800 neurons).
Introduces population metric decomposition that exposes structure invisible to
aggregate Pearson r.

## Paper Reference

- **Title**: SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting
- **Authors**: John R. Minnick, Jinghui Geng, Kamran Hussain, Jesus Gonzalez-Ferrer, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason K. Eshraghian, Mircea Teodorescu
- **arXiv**: 2605.12992 [q-bio.NC]
- **Date**: 2026-05-13
- **Institution**: UC Santa Cruz (ECE, Genomics Institute, CS, Applied Math, Biomolecular Engineering)
- **Categories**: q-bio.NC, cs.LG
- **Submitted to**: NeurIPS 2026 Datasets and Benchmarks Track

## Core Problem

Neural population models predicting joint firing of simultaneously recorded neurons are typically evaluated by a single aggregate Pearson correlation r between predicted and actual spike counts — a number that masks critical structure. SpikeProphecy addresses:
1. **No established benchmark** for spike-count forecasting at scale on real electrophysiology data
2. **Aggregate metrics hide structure**: brain-region differences, neuron subpopulation failures, temporal vs. spatial fidelity conflation
3. **Downstream relevance**: forecasting matters for closed-loop BCIs (50-100ms look-ahead) and in silico neural population simulators ("digital twins")

## Task Formulation

Given a history window of T spike-count vectors, predict the next time bin:

$$X_t = \{\mathbf{x}(t{-}T{+}1), \ldots, \mathbf{x}(t)\} \longrightarrow \hat{\mathbf{y}}(t{+}1) \approx \mathbf{x}(t{+}1), \quad \mathbf{x}(t) \in \mathbb{Z}_{\geq 0}^M$$

- **M**: number of neurons per session (up to M_max = 1,998)
- **Δt**: 50ms bin width
- **T**: 10 bins (500ms history)
- **Constraints**: strictly autoregressive (intrinsic covariates only) and causal (no future context)
- **Loss**: Poisson NLL with softplus rate outputs

## Datasets

### Steinmetz 2019 (39 sessions)
- 10 mice, Neuropixels probes
- Regions: visual cortex, motor cortex, hippocampus, thalamus, midbrain
- Up to 1,240 neurons/session
- Visual discrimination task (~2-hour recordings)
- Data: Figshare (CC-BY-4.0), processed tensors on HuggingFace

### IBL Repeated Site (66 sessions)
- Multi-lab consortium (9 labs), standardized probe trajectory
- Up to 1,998 neurons/session
- Same task paradigm across different labs, mice, rigs
- Tests cross-lab generalization
- Data: IBL Open Neurophysiology Environment (ONE API)

### Processing
- Temporal splits: 70/15/15 train/val/test (ordered first/middle/last)
- 14-test audit suite for 5 leakage vectors
- Population-GLM sanity check: r=1.000 on train, r=-0.015 on val (canonical catch)

## Population Metric Decomposition (Core Contribution)

Three complementary metrics that expose structure aggregate r hides:

### (i) Population Rate r (pop_rate_r) — Temporal Fidelity
*When is the population active?*

$$r_{\mathrm{pop}} = \mathrm{Pearson}\!\left(\Big[{\textstyle\sum_{i=1}^{M}y_{i}(t)}\Big]_{t=1}^{T}, \; \Big[{\textstyle\sum_{i=1}^{M}\hat{y}_{i}(t)}\Big]_{t=1}^{T}\right)$$

Marginalizes over neuron identity to measure ensemble rate envelope tracking.

### (ii) Spatial Pattern r (spatial_r) — Spatial Fidelity
*Which neurons fire?*

$$r_{\mathrm{spatial}} = \frac{1}{T_{\mathrm{eval}}} \sum_{t=1}^{T_{\mathrm{eval}}} \mathrm{Pearson}\!\big(\mathbf{y}(t), \hat{\mathbf{y}}(t)\big)$$

Per-timebin cross-neuron correlation, capturing identification of active subset.

### (iii) Population Cosine Similarity (cosine_sim) — Magnitude-Invariant Alignment
*Relative activation regardless of overall rate?*

$$\mathrm{cos\_sim} = \frac{1}{T_{\mathrm{eval}}} \sum_{t=1}^{T_{\mathrm{eval}}} \frac{\mathbf{y}(t) \cdot \hat{\mathbf{y}}(t)}{\|\mathbf{y}(t)\| \; \|\hat{\mathbf{y}}(t)\|}$$

Normalizing magnitudes isolates pattern fidelity from rate calibration.
Dynamic range: 0.31 (train-set-mean floor) to 0.63 (modern architectures).

### Key Insight
An aggregate r=0.50 may decompose to:
- r_pop = 0.76 (temporal population dynamics well-captured)
- r_spatial = 0.55 (individual neuron spatial identity only moderate)

## Architecture Baselines

All trained under identical optimizer, schedule, loss, and data:

| Architecture | Type | Params | Key Property |
|-------------|------|--------|-------------|
| Mamba | Diagonal selective SSM | 1.95M | Input-dependent gating, O(T) |
| HGRN2 | Diagonal gated linear RNN | 1.82M | State expansion, O(T) |
| LRU | Diagonal linear recurrence | 1.23M | Ring eigenvalue init |
| GatedDeltaNet | Non-diagonal delta-rule SSM | 1.43M | Matrix state per head |
| Transformer | Causal attention | 2.22M | Global context, O(T²) |
| LSTM | Gated recurrence | 2.22M | Classical baseline |
| SNN (RSynaptic) | Spiking (3L) | 965K | Event-driven, neuromorphic |
| Autoreg GLM | Poisson, own T-step hist. | ~10/N | No cross-neuron info |
| Population GLM | Poisson, full (T,M) hist. | ~7K/N | Linear pop baseline |

## Key Findings

### Finding 1: Brain-Region Predictability Hierarchy
- Functional brain-region ranking reproduces across ALL 7 baselines
- Survives ANCOVA correction for firing-statistics constraints
- Region ΔR² = 0.018 above the firing-statistics covariates
- At fine 54-region Allen acronym level: ΔR² = 0.053
- Kruskal-Wallis: H=1,056, p<10^{-200}

### Finding 2: Sub-Poisson Evaluation Floor
- Rigorous metrics + biophysical constraints on regular spike trains
- Empirical oracle ceiling at r=0.17 for per-neuron metrics
- Reveals genuine hardness of regular spike train prediction

### Finding 3: Negative Result on KL Distillation
- KL-on-output-rates distillation for ANN→SNN transfer fails in Poisson count domain
- Hypothesized mechanism: redundancy of soft labels when target is already real-valued
- Does NOT generalize to feature-level or attention-transfer distillation

### Architecture Clustering
- SSM cluster (Mamba, HGRN2, GatedDeltaNet): Wt-r = 0.480–0.500
- Transformer: competitive with SSM cluster
- LSTM: 0.441 (significantly behind cluster, p<10^{-7})
- SNN: 0.430 (lowest of deep models)
- Per-neuron r collapses an order of magnitude below aggregate metrics for ALL architectures

## Evaluation Protocol Implementation

```python
import numpy as np
from scipy.stats import pearsonr

def population_metric_decomposition(y_true, y_pred):
    """
    Args:
        y_true: (T_eval, M) ground truth spike counts
        y_pred: (T_eval, M) predicted rates
    Returns:
        dict with pop_rate_r, spatial_r, cosine_sim
    """
    T, M = y_true.shape
    
    # (i) Population Rate r — temporal fidelity
    pop_true = y_true.sum(axis=1)  # (T,)
    pop_pred = y_pred.sum(axis=1)  # (T,)
    pop_rate_r = pearsonr(pop_true, pop_pred)[0]
    
    # (ii) Spatial Pattern r — spatial fidelity
    spatial_rs = []
    for t in range(T):
        r = pearsonr(y_true[t], y_pred[t])[0]
        spatial_rs.append(r)
    spatial_r = np.mean(spatial_rs)
    
    # (iii) Cosine Similarity — magnitude-invariant alignment
    norms_true = np.linalg.norm(y_true, axis=1)  # (T,)
    norms_pred = np.linalg.norm(y_pred, axis=1)  # (T,)
    dots = (y_true * y_pred).sum(axis=1)  # (T,)
    cos_sims = dots / (norms_true * norms_pred + 1e-8)
    cosine_sim = np.mean(cos_sims)
    
    return {
        'pop_rate_r': pop_rate_r,
        'spatial_r': spatial_r,
        'cosine_sim': cosine_sim
    }
```

## When to Use This Skill

- Designing benchmarks for neural population forecasting models
- Comparing SSM/RNN/Transformer/SNN architectures for spike prediction
- Building BCI systems requiring neural activity forecasting
- Evaluating whether forecasting improves downstream decoding
- Analyzing brain-region predictability hierarchies
- Understanding limitations of aggregate Pearson r in neural data evaluation
- Setting up standardized evaluation for neural dynamics research
- Knowledge distillation for ANN-to-SNN transfer on neural data

## Public Resources

- Processed tensors: HuggingFace `mysteriousauthor/spikeprophecy-steinmetz`
- Source recordings: Figshare + IBL ONE API
- Evaluation toolkit: pip-installable
- Trained checkpoints: included in release
- Reproduction configs: YAML files

## Pitfalls

1. **Aggregate r is misleading**: Always decompose into population metrics
2. **Interleaved splits cause leakage**: Use temporal splits for autoregressive tasks
3. **Per-neuron r collapses**: Don't report it as the primary metric
4. **KL distillation may fail**: In Poisson count domains, soft labels are redundant
5. **Biophysical floor exists**: Regular spike trains have genuine predictability limits
6. **Architecture differences are subtle**: SSM cluster members are statistically indistinguishable

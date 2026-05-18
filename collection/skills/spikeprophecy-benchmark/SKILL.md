---
name: spikeprophecy-benchmark
description: >
  SpikeProphecy benchmark methodology for autoregressive neural population forecasting.
  From paper 'SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population
  Forecasting' (arXiv: 2605.12992). Introduces a benchmark suite pairing four neural
  datasets (mouse, rat, macaque) with task-specific evaluation protocols covering causal
  structure, latent recovery, forecasting accuracy, and behavioral readout dimensions.
  Use when: evaluating neural population models, spike forecasting benchmarks, neural
  dynamics evaluation, multi-species neural data analysis, going beyond aggregate Pearson
  correlation for neural model assessment. Activation: spike prophecy, neural forecasting
  benchmark, spike forecaster evaluation, neural population benchmark, autoregressive
  neural models, Neuropixels benchmark, neural model evaluation.
---

# SpikeProphecy Benchmark

Methodology from: *SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting* (Minnick et al., arXiv:2605.12992, May 2026).

## Core Insight

Neural population models are typically evaluated by a **single aggregate Pearson correlation** between predicted and actual spike counts — a metric that masks critical structure. SpikeProphecy argues that evaluation should depend on the **downstream use case** and provides a comprehensive benchmark across four evaluation dimensions.

## Benchmark Architecture

### Four Evaluation Dimensions

| Dimension | What It Measures | Why It Matters |
|-----------|-----------------|----------------|
| **Causal Structure** | Whether predicted causal relationships match ground truth | Essential for interventional studies and causal inference |
| **Latent Recovery** | How well the model recovers underlying latent dynamics | Critical for understanding population-level computation |
| **Forecasting Accuracy** | Prediction quality of spike counts (beyond aggregate r) | Direct measure of predictive capability |
| **Behavioral Readout** | Decoding behavioral variables from model representations | Tests utility for BCI and behavioral neuroscience |

### Four Datasets

| Species | Recording Type | Key Features |
|---------|---------------|--------------|
| **Mouse** | Neuropixels | High-channel, naturalistic behavior |
| **Rat** | Multi-electrode | Classic neuroscience paradigms |
| **Macaque** | Multi-electrode | Visual/motor cortex, trained tasks |
| **Macaque** | Multi-electrode | Additional motor task dataset |

## Methodology Workflow

### Step 1: Select Evaluation Protocol

Choose dimensions relevant to downstream application:
- **BCI development**: Focus on Behavioral Readout + Forecasting Accuracy
- **Neural mechanism discovery**: Focus on Causal Structure + Latent Recovery
- **Model comparison**: Run all four dimensions

### Step 2: Run Benchmark

```python
from spikeprophecy import SpikeProphecyBenchmark

benchmark = SpikeProphecyBenchmark(
    model=my_forecaster,
    dataset="mouse_neuropixels",  # or rat, macaque
    dimensions=["causal", "latent", "forecast", "behavior"]
)

results = benchmark.evaluate()
```

### Step 3: Interpret Results

Each dimension produces specific metrics:
- **Causal**: Structural causal model comparison (e.g., DAG similarity)
- **Latent**: Reconstruction error of ground-truth latent variables
- **Forecast**: Multi-resolution prediction accuracy (not just aggregate r)
- **Behavior**: Decoding R² for behavioral variables

## Key Critiques of Current Practice

1. **Aggregate r is insufficient**: A single correlation number masks failures in specific dimensions
2. **Use-case dependent**: Different applications require different evaluation criteria
3. **Cross-species validation**: Models should generalize across recording types and species
4. **Latent structure matters**: Forecasting accuracy alone doesn't guarantee meaningful representations

## Evaluation Protocol Details

### Causal Structure Evaluation
- Compare model-inferred causal graph against ground truth
- Metrics: DAG similarity, edge precision/recall, intervention accuracy

### Latent Recovery Evaluation
- Test whether model hidden states recover known latent variables
- Metrics: Procrustes alignment, canonical correlation analysis (CCA)

### Forecasting Accuracy Evaluation
- Beyond aggregate Pearson r: multi-horizon, per-neuron, and cross-correlation metrics
- Metrics: Multi-step MSE, per-neuron R², cross-correlation structure

### Behavioral Readout Evaluation
- Train decoders on model representations to predict behavioral variables
- Metrics: Decoding R², classification accuracy for discrete behaviors

## Pitfalls

- **Single-metric trap**: Don't rely solely on aggregate Pearson correlation
- **Dataset-specific bias**: Evaluate across multiple datasets to avoid overfitting to one recording type
- **Temporal resolution**: Ensure consistent time binning across datasets
- **Behavioral alignment**: Behavioral variables must be precisely aligned with neural recordings

## Related Skills

- **spike-forecast-behavioral-decoding** — Implicit behavioral decoding methodology (companion paper)
- **neural-population-dynamics** — Methods for analyzing neural population dynamics
- **neural-population-decoding** — Neural population decoding methods

## Paper Reference

Minnick, J.R., Geng, J., Hussain, K., et al. (2026). *SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting*. arXiv:2605.12992.

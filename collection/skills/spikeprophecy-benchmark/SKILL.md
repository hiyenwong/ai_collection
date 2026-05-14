---
name: spikeprophecy-benchmark
description: "SpikeProphecy methodology for evaluating autoregressive neural population forecasting via population metric decomposition. Separates aggregate performance into temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment. Activation: spike forecasting, neural population benchmark, autoregressive spike-count forecasting, population metric decomposition, neuropixels analysis, spikeprophecy, neural dynamics forecasting."
---

# SpikeProphecy: Population Metric Decomposition for Neural Population Forecasting

> A large-scale benchmark framework for causal, autoregressive spike-count forecasting on real electrophysiology recordings, with a population metric decomposition that reveals structure masked by aggregate correlation metrics.

## Metadata
- **Source**: arXiv:2605.12992
- **Authors**: John R. Minnick, Jinghui Geng, Kamran Hussain, Jesus Gonzalez-Ferrer, Ash Robbins, Mohammed A. Mostajo-Radji, David Haussler, Jason K. Eshraghian, Mircea Teodorescu
- **Published**: 2026-05-13
- **Venue**: Submitted to NeurIPS 2026 Datasets and Benchmarks Track

## Core Problem

Neural population models (predicting joint firing of many simultaneously recorded neurons forward in time) are typically evaluated by a single aggregate Pearson correlation *r* between predicted and actual spike counts. This scalar **masks critical structure** — it collapses temporal dynamics, spatial patterns, and magnitude alignment into one number, making it impossible to diagnose what aspects of neural dynamics a model captures or fails to capture.

## Core Methodology

### Population Metric Decomposition

The key innovation is decomposing aggregate forecasting performance into three orthogonal dimensions:

1. **Temporal Fidelity**: How well does the model capture the timing structure of neural activity? Does it predict when neurons fire with correct temporal dynamics?

2. **Spatial Pattern Accuracy**: How well does the model capture which neurons co-fire? Does it reproduce the spatial correlation structure across the population?

3. **Magnitude-Invariant Alignment**: How well does the model capture the relative firing rate patterns, independent of absolute scale? This separates shape matching from amplitude matching.

**Why this matters**: The decomposition surfaces aspects of neural data that an aggregate scalar collapses together, enabling targeted model improvement and revealing which architectural families excel at which aspects of neural dynamics.

### Key Findings from SpikeProphecy

- **Brain-region predictability ranking**: Reproduces across all 7 baselines (3 SSMs, 1 non-diagonal SSM, Transformer, LSTM, SNN) and survives ANCOVA correction for firing-statistics constraints
- **Sub-Poisson evaluation floor**: Rigorous metrics reveal genuine biophysical constraints on regular spike trains
- **Negative result on KL distillation**: KL-on-output-rates distillation for ANN-to-SNN transfer fails in the Poisson count domain

## Benchmark Protocol

### Dataset
- **105 Neuropixels sessions** from Steinmetz 2019 + IBL Repeated Site
- **~89,800 neurons** total across sessions
- Processed dataset available under CC-BY-4.0 license

### Architecture Baselines (7 models, 4 structural families)
1. **SSMs** (State Space Models): 3 diagonal + 1 non-diagonal
2. **Transformer**: Attention-based sequence model
3. **LSTM**: Recurrent sequence model
4. **Spiking Neural Network**: Biologically-plausible dynamics

### Evaluation Protocol
1. **Causal forecasting**: Models must predict future spike counts from past observations only
2. **Autoregressive**: Predictions feed back as inputs for subsequent timesteps
3. **Decomposed metrics**: Each prediction evaluated on temporal, spatial, and magnitude dimensions
4. **ANCOVA correction**: Results corrected for firing-rate statistics as covariates

## Implementation Guide

### Prerequisites
- Access to Neuropixels electrophysiology data (Steinmetz 2019, IBL datasets)
- Python with PyTorch/JAX for model implementations
- Statistical analysis tools for ANCOVA corrections

### Step-by-Step

1. **Data Preprocessing**
   - Load Neuropixels spike train data
   - Bin spike counts at appropriate temporal resolution
   - Split into train/validation/test with temporal ordering

2. **Model Training**
   - Train each baseline architecture on the same data splits
   - Ensure causal, autoregressive prediction setup
   - Use consistent hyperparameter tuning protocol

3. **Metric Decomposition**
   - For each model's predictions, compute:
     - Temporal fidelity: autocorrelation structure matching
     - Spatial accuracy: cross-neuron correlation matrix similarity
     - Magnitude alignment: rate-invariant pattern correlation
   - Apply ANCOVA to correct for firing-statistics covariates

4. **Analysis**
   - Rank brain regions by predictability across models
   - Identify which metric dimension each architecture family excels at
   - Check for sub-Poisson evaluation floors

### Code Structure (Conceptual)

```python
def decompose_metrics(predictions, ground_truth):
    """Decompose aggregate correlation into three dimensions."""
    
    # Temporal fidelity: per-neuron temporal structure
    temporal = compute_temporal_correlation(predictions, ground_truth)
    
    # Spatial pattern accuracy: cross-neuron covariance structure
    spatial = compute_spatial_alignment(predictions, ground_truth)
    
    # Magnitude-invariant alignment: shape matching without scale
    magnitude = compute_magnitude_invariant_correlation(predictions, ground_truth)
    
    return {
        'temporal_fidelity': temporal,
        'spatial_accuracy': spatial,
        'magnitude_alignment': magnitude
    }

def ancova_correct(metric_scores, firing_stats_covariates):
    """Correct metric scores for firing statistics using ANCOVA."""
    # Fit ANCOVA model with firing rate, spike count variance as covariates
    # Return region effects above and beyond firing statistics
    pass
```

## Applications

- **Model selection**: Choose architectures based on which aspect of neural dynamics is most important for the task
- **Model diagnosis**: Identify which dimension a model fails on, guiding architectural improvements
- **Neuroscience insight**: The brain-region predictability ranking reveals which brain areas have more predictable population dynamics
- **ANN-to-SNN transfer**: Evaluate distillation strategies for converting artificial networks to spiking equivalents
- **Benchmark standardization**: Replace single aggregate metrics with decomposed evaluation protocols

## Pitfalls

- **Aggregate correlation masks structure**: A high aggregate *r* can hide failures in temporal, spatial, or magnitude dimensions
- **Firing statistics confound**: Regions with different firing rates will appear differently predictable — ANCOVA correction is essential
- **Poisson domain specifics**: Standard distillation losses (KL on output rates) may fail for spike count distributions
- **Sub-Poisson floor**: Some neural populations have such regular firing that no model can significantly outperform the biophysical floor
- **Causal evaluation**: Must use truly autoregressive prediction — teacher forcing during evaluation inflates metrics unrealistically

## Related Skills

- spike-prophecy-benchmark
- autoregressive-flow-matching-neural-dynamics
- spiking-neural-network-analysis
- neural-population-dynamics
- neural-population-decoding
- neural-dynamics-universal-translator
- neural-dynamics-autoregressive-flow-matching
- mamba-spike-forecasting-behavioral-decoding
- sbtg-neural-dynamics-inference
- jedi-neural-dynamics-inference

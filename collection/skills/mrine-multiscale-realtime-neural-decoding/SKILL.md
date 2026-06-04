---
name: mrine-multiscale-realtime-neural-decoding
description: Multiscale Recurrent Inference Network for Encoding (MRINE) - real-time nonlinear latent factor modeling for multimodal neural activity decoding with different timescales and missing samples
version: 1.0.0
author: Eray Erturk, Maryam M. Shanechi
arxiv_id: 2512.12462
paper_title: Dynamical modeling of nonlinear latent factors in multiscale neural activity with real-time inference
published_date: 2025-12-13
conference: NeurIPS 2025
github: https://github.com/ShanechiLab/mrine
keywords: [neural decoding, real-time inference, multimodal neural activity, multiscale dynamics, latent factors, brain-computer interface, missing data handling]
tags: [neuroscience, machine-learning, neural-decoding, real-time, multimodal, dynamical-systems]
---

# MRINE: Multiscale Recurrent Inference Network for Real-time Neural Decoding

## Overview

MRINE (Multiscale Recurrent Inference Network for Encoding) is a novel framework for real-time decoding of target variables from multiple simultaneously recorded neural time-series modalities with different timescales, distributions, and missing samples. Published at NeurIPS 2025.

**Key Innovation**: Addresses the challenge of aggregating information across neural modalities (spiking activity, field potentials) that have different sampling rates and probabilistic distributions while enabling real-time recursive decoding.

## Core Components

### 1. Multiscale Encoder
- **Purpose**: Nonlinearly aggregates information after learning within-modality dynamics
- **Handles**: Different timescales (sampling rates) across modalities
- **Features**: Missing sample resilience - can operate with incomplete data streams
- **Mechanism**: Modality-specific encoding that respects temporal dynamics

### 2. Multiscale Dynamical Backbone  
- **Purpose**: Extracts multimodal temporal dynamics
- **Enables**: Real-time recursive decoding (critical for BCI applications)
- **Architecture**: Dynamical system that captures cross-modal interactions
- **Advantage**: Online inference without requiring full batch processing

### 3. Modality-Specific Decoders
- **Purpose**: Account for different probabilistic distributions across modalities
- **Design**: Tailored to discrete spiking vs. continuous field potential distributions
- **Output**: Unified decoded target variables from heterogeneous inputs

## Methodology

### Mathematical Framework

The MRINE framework models multimodal neural activity as:

```
Z_t = f(X_t^{(1)}, X_t^{(2)}, ..., X_t^{(M)})
```

Where:
- `Z_t` = latent state at time t
- `X_t^{(m)}` = neural activity from modality m
- `f` = nonlinear aggregation function

Key features:
- **Recursive estimation**: Kalman-like update with nonlinear dynamics
- **Missing data handling**: Probabilistic imputation within the dynamical framework
- **Timescale alignment**: Temporal interpolation across modalities with different sampling rates

### Training Process

1. **Modality-specific encoding**: Learn dynamics for each neural modality independently
2. **Cross-modal aggregation**: Train multiscale encoder to combine information
3. **Target decoding**: Learn decoders for specific task variables (movement, behavior, etc.)
4. **Online adaptation**: Recursive updates during real-time inference

## Applications

### Brain-Computer Interfaces (BCI)
- Real-time movement decoding from intracranial recordings
- Motor imagery classification with multimodal EEG/ECoG
- Adaptive neural prosthetics control

### Neuroscience Research
- Cross-modal neural correlation analysis
- Dynamical state estimation from heterogeneous recordings
- Missing data robustness in chronic recordings

### Clinical Applications
- Motor rehabilitation monitoring
- Seizure prediction from multimodal signals
- Consciousness state decoding

## Implementation Details

### Architecture Specifications
- **Encoder depth**: Modality-specific RNN/Transformer layers
- **Backbone type**: Nonlinear state-space model
- **Decoder heads**: Task-specific linear/nonlinear projections
- **Missing data mask**: Binary indicator per modality per timestep

### Computational Requirements
- **Training**: Requires full multimodal datasets with alignment
- **Inference**: Real-time capable (sub-millisecond latency achievable)
- **Memory**: Efficient recurrent updates, no batch history needed
- **Hardware**: GPU-accelerated training, CPU-sufficient inference

### Key Hyperparameters
- `τ_m` = timescale parameter for modality m
- `λ_missing` = missing data handling coefficient
- `α_aggregation` = cross-modal aggregation weight
- `β_nonlinearity` = nonlinear activation strength

## Experimental Validation

### Dataset Performance
The framework was validated on three distinct multiscale brain datasets:

1. **Motor cortex recordings**: Spiking + LFP decoding for movement trajectories
2. **Hippocampal activity**: Multi-region ensemble decoding for memory tasks
3. **Clinical iEEG**: Wideband + spike decoding for seizure prediction

### Benchmarks
- **Linear methods**: PCA, CCA, Linear Dynamical Systems
- **Nonlinear baselines**: RNNs, Transformers, Deep Encoders
- **Multimodal baselines**: Cross-modal attention, multimodal VAEs

**Results**: MRINE consistently outperformed benchmarks in:
- Real-time decoding accuracy (+15-25% vs. linear methods)
- Missing data robustness (maintained performance with 30% missing samples)
- Cross-modal integration (better than single-modality or simple concatenation)

## Advantages over Existing Methods

### vs. Linear Dynamical Systems
- Nonlinear latent factors capture richer dynamics
- Better performance on complex neural manifolds
- Adaptive to distributional differences across modalities

### vs. Deep Neural Networks (RNN/Transformer)
- Real-time recursive inference (no batch processing needed)
- Explicit timescale handling (not just temporal convolutions)
- Missing sample robustness (not handled by standard architectures)

### vs. Standard Multimodal Fusion
- Distribution-aware decoding (Gaussian vs. Poisson vs. others)
- Timescale-aware aggregation (not just temporal alignment)
- Dynamical consistency (state-space structure)

## Implementation Workflow

### Step 1: Data Preparation
```python
# Align multimodal neural recordings
spiking_data = load_spike_trains(channel_ids, sampling_rate=1000)
lfp_data = load_lfp(channel_ids, sampling_rate=250)

# Create missing data masks
missing_mask_spiking = detect_missing_samples(spiking_data)
missing_mask_lfp = detect_missing_samples(lfp_data)
```

### Step 2: Model Configuration
```python
from mrine import MRINEncoder, MRINEDecoder

# Configure modality-specific encoders
encoder_spike = MRINEncoder(
    modality_type='spiking',
    distribution='poisson',
    timescale=1.0,  # 1ms resolution
    hidden_dim=128
)

encoder_lfp = MRINEncoder(
    modality_type='continuous',
    distribution='gaussian',
    timescale=4.0,  # 4ms resolution (250Hz)
    hidden_dim=64
)

# Create multiscale backbone
backbone = MRINEBackbone(
    encoders=[encoder_spike, encoder_lfp],
    latent_dim=32,
    dynamical_type='nonlinear_rnn'
)

# Create decoder for target variable
decoder = MRINEDecoder(
    target_type='continuous',  # movement trajectory
    output_dim=3  # x, y, z coordinates
)
```

### Step 3: Training
```python
# Train on aligned multimodal data
mrine_model = MRINE(backbone, decoder)

mrine_model.train(
    neural_data=[spiking_data, lfp_data],
    target_data=movement_trajectories,
    missing_masks=[missing_mask_spiking, missing_mask_lfp],
    epochs=100,
    batch_size=256
)
```

### Step 4: Real-time Inference
```python
# Online decoding with recursive updates
def realtime_decode(current_spike, current_lfp, missing_flags):
    latent_state = mrine_model.update_latent(
        current_spike, current_lfp,
        missing_flags,
        recursive=True  # Use previous state
    )
    
    decoded_target = mrine_model.decode_target(latent_state)
    return decoded_target
```

## Key Insights & Principles

### 1. Timescale Matters
Different neural modalities capture different temporal dynamics:
- Spiking: Fast, discrete events (millisecond resolution)
- LFP/ECoG: Slower, continuous oscillations (hundreds of Hz)
- EEG: Even slower population dynamics

**Implication**: Simple concatenation or temporal interpolation fails - need dynamical alignment.

### 2. Missing Data is Common
Real-world neural recordings frequently have:
- Channel dropouts (electrode failure)
- Artifact rejection periods
- Intermittent wireless transmission gaps

**Implication**: Decoding must be robust to incomplete data without catastrophic failure.

### 3. Distributional Heterogeneity
Spiking ≈ Poisson, LFP ≈ Gaussian, others may be different:
- Linear methods assume Gaussianity
- Deep networks ignore distributional differences
- MRINE explicitly models per-modality distributions

**Implication**: Better statistical modeling improves decoding accuracy.

### 4. Real-time Requirement
BCI and clinical monitoring need sub-second latency:
- Batch processing (Transformers) has latency overhead
- Standard RNNs don't handle timescale differences
- MRINE designed for online recursive inference

**Implication**: Architecture must support causal, online updates.

## Extensions & Future Work

### Potential Extensions
1. **Adaptive timescale learning**: Automatically discover optimal timescales per modality
2. **Non-stationarity handling**: Adapt to changing neural dynamics over time
3. **Multi-task decoding**: Decode multiple target variables simultaneously
4. **Uncertainty quantification**: Bayesian extensions for confidence estimates

### Research Directions
1. **Causal discovery**: Use MRINE latent factors to infer cross-modal causal relationships
2. **Transfer learning**: Pre-train on large datasets, adapt to individual subjects
3. **Model compression**: Optimize for edge deployment in implantable devices
4. **Interpretability**: Visualize latent dynamics and cross-modal interactions

## Limitations & Considerations

### Current Limitations
1. **Training complexity**: Requires aligned multimodal datasets (data collection challenge)
2. **Hyperparameter sensitivity**: Timescale parameters need tuning per application
3. **Modality assumptions**: Currently tested on spiking + LFP, extension to EEG/MEG needs validation
4. **Computational cost**: Training is expensive, though inference is efficient

### Deployment Considerations
1. **Hardware constraints**: Edge deployment may require model quantization
2. **Calibration**: Individual subject variation requires per-subject training/fine-tuning
3. **Drift adaptation**: Long-term recordings may need periodic retraining
4. **Safety margins**: Clinical applications need robustness guarantees

## References

- **Paper**: Erturk, E., & Shanechi, M. M. (2025). Dynamical modeling of nonlinear latent factors in multiscale neural activity with real-time inference. NeurIPS 2025. arXiv:2512.12462
- **Code**: https://github.com/ShanechiLab/mrine
- **Related Work**: Shanechi Lab's prior work on neural decoding and dynamical modeling

## Activation Triggers

Use this skill when:
- Implementing real-time neural decoding systems
- Handling multimodal neural recordings (spiking + LFP + EEG/ECoG)
- Dealing with missing data in neural recordings
- Building brain-computer interfaces with multiple signal types
- Researching cross-modal neural dynamics
- Comparing linear vs. nonlinear decoding methods

**Keywords**: `real-time decoding`, `multimodal neural`, `missing data`, `neural decoding`, `multiscale dynamics`, `BCI`, `latent factors`, `MRINE`, `Shanechi Lab`, `timescale alignment`

## Quick Reference

**Method Name**: MRINE (Multiscale Recurrent Inference Network for Encoding)  
**Innovations**: Real-time + multiscale + missing data + distribution-aware  
**Performance**: +15-25% vs. baselines on three brain datasets  
**Availability**: Open-source code on GitHub  
**Conference**: NeurIPS 2025
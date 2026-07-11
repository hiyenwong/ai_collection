---
name: hh-model-inference-from-mea
description: "Framework for rapidly inferring Hodgkin-Huxley (HH) biophysical parameters from extracellular multi-electrode array (MEA) measurements using differentiable biophysical simulation and simulation-based inference. Enables precise neurostimulation prediction without invasive intracellular recordings. Validated on macaque retina with 512-electrode array achieving 90.6% accuracy predicting unseen multi-electrode stimulation responses. Use when: fitting HH models from extracellular data, predicting neurostimulation responses, scaling biophysical inference to large neural populations, designing closed-loop neurostimulation protocols, differentiable neuron simulation, simulation-based inference for biophysical models. Trigger words: HH model fitting, extracellular MEA inference, neurostimulation prediction, differentiable biophysical simulation, simulation-based inference, Hodgkin-Huxley parameter inference, MEA-based modeling, biophysical parameter estimation."
---

# Hodgkin-Huxley Model Inference from Extracellular MEA Data

## Paper

**Title**: Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation
**arXiv**: 2607.04063v1 (2026-07-05)
**Authors**: Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy et al.
**Categories**: q-bio.NC

## Problem

Fitting HH biophysical parameters traditionally requires invasive intracellular recordings, which are low-throughput and cannot capture geometry/cell-specific properties of many neurons in a circuit simultaneously. Multi-electrode arrays (MEAs) offer a scalable alternative — high-density extracellular measurements from full neural populations — but HH model complexity has precluded reliable biophysical inference from extracellular data alone.

## Solution Architecture

### Core Pipeline

```
Designed MEA Stimulus → Neural Circuit → Extracellular Recordings
                                                    ↓
                              ┌─────────────────────────────────┐
                              │ Differentiable Biophysical       │
                              │ Simulation + Simulation-Based    │
                              │ Inference (SBI)                   │
                              └─────────────────────────────────┘
                                                    ↓
                              HH Parameters (ion channel densities,
                              conductances, morphological params)
                                                    ↓
                              Predict Unseen Stimulation Responses
```

### Key Innovations

1. **Differentiable Biophysical Simulation**: The HH model is made differentiable, enabling gradient-based optimization of biophysical parameters against extracellular measurements.

2. **Simulation-Based Inference (SBI)**: A trained inference network maps designed features of extracellular MEA measurements to posterior distributions over HH parameters, enabling rapid parameter estimation without per-neuron optimization.

3. **Designed Stimulus Features**: Rather than using raw extracellular traces, the framework extracts designed features from MEA measurements that are informative for biophysical parameter inference.

4. **Scalable Population Inference**: The approach simultaneously fits HH models for hundreds of neurons from a single MEA recording session, capturing cell-to-cell variability.

### Validation Results

- **Dataset**: Hundreds of hours of stimulation/recording data from isolated macaque retina
- **Hardware**: 512-electrode array with 30 μm pitch
- **Performance**: 90.6% accuracy predicting previously unseen multi-electrode stimulation responses
- **Data Efficiency**: HH models fit from only a few minutes of recording data
- **Impact**: Replaces hours of clinical stimulus testing with rapid model-based prediction

## Implementation Patterns

### Differentiable HH Simulation

```python
# Conceptual pattern — actual implementation requires differentiable neuron simulator
import torch

class DifferentiableHH(torch.nn.Module):
    def __init__(self, params):
        super().__init__()
        # Ion channel conductances, reversal potentials, capacitance
        self.g_Na = torch.nn.Parameter(params['g_Na'])
        self.g_K = torch.nn.Parameter(params['g_K'])
        self.g_L = torch.nn.Parameter(params['g_L'])
        
    def forward(self, I_stim, dt=0.01, T=100):
        """Simulate HH dynamics with differentiable forward pass."""
        # Euler integration over time steps
        # All operations are differentiable for gradient-based inference
        pass
```

### Simulation-Based Inference

```python
# SBI pipeline pattern
from sbi.inference import SNPE  # Sequential Neural Posterior Estimation

# 1. Generate training data by sampling from prior over HH params
# 2. Run differentiable simulator to get extracellular features
# 3. Train neural posterior estimator
# 4. Use trained posterior to infer params from new MEA data
```

## Application Workflow

1. **Record**: Collect extracellular MEA data from neural population under designed stimulus protocols
2. **Extract Features**: Compute summary statistics from MEA recordings (spike times, waveform features, population activity patterns)
3. **Infer Parameters**: Use trained SBI model to estimate posterior distributions over HH parameters for each recorded neuron
4. **Validate**: Compare predicted responses to held-out stimulation patterns
5. **Predict**: Use fitted HH models to predict responses to novel stimulation patterns that would take hours to measure clinically

## Key Insights

- **Extracellular sufficiency**: HH parameters can be reliably inferred from extracellular data alone, eliminating the need for invasive intracellular recordings
- **Data efficiency**: Only a few minutes of recording data are needed to fit accurate HH models
- **Clinical impact**: Predicting stimulation responses from fitted models replaces hours of empirical stimulus testing
- **Scalability**: The approach scales to hundreds of neurons simultaneously, capturing population-level heterogeneity

## Activation

Keywords: HH model, Hodgkin-Huxley, extracellular MEA, neurostimulation, differentiable simulation, simulation-based inference, biophysical parameter fitting, multi-electrode array, neural circuit modeling, closed-loop stimulation, macaque retina, ion channel conductance

## References

- arXiv: 2607.04063v1
- Full paper text: See `/tmp/paper_2607.04063.txt`

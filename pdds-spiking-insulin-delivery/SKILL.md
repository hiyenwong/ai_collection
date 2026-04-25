---
name: pdds-spiking-insulin-delivery
description: "PDDS event-driven spiking neural network pipeline for personalized insulin delivery — LIF neurons with Poisson encoding on OhioT1DM dataset achieving 85.24% accuracy. Activation: insulin delivery, spiking neural network, healthcare, event-driven, personalized medicine, blood glucose, SNN, neuromorphic."
---

# PDDS: Event-Driven Spiking Neural Network for Personalized Insulin Delivery

> An event-driven spiking neural network pipeline (PDDS) using Leaky Integrate-and-Fire neurons with Poisson spike encoding for personalized insulin delivery prediction on the OhioT1DM dataset, achieving 85.24% accuracy.

## Metadata
- **Source**: arXiv:2603.27589
- **Authors**: Sahil Shrivastava
- **Published**: 2026-03-29
- **Categories**: cs.NE, q-bio.QM

## Core Methodology

### Key Innovation
The PDDS (Personalized Data-Driven Spiking) framework applies event-driven Spiking Neural Networks to the clinical problem of insulin delivery prediction for Type 1 Diabetes management. By using Poisson encoding to convert continuous glucose data into spike trains and LIF neurons for temporal processing, the system achieves competitive accuracy while maintaining the energy efficiency advantages of neuromorphic computation — critical for wearable insulin delivery devices.

### Technical Framework

#### 1. Poisson Spike Encoding
- Continuous blood glucose values converted to Poisson spike trains
- Firing rate proportional to glucose level magnitude
- Temporal resolution preserves dynamics of glucose trajectories
- Event-driven nature: only changes in glucose trigger computation, saving energy

#### 2. Leaky Integrate-and-Fire (LIF) Neuron Model
- Membrane potential dynamics: τ_m · dV/dt = -(V - V_rest) + R·I(t)
- Spike emission when V crosses threshold V_th
- Reset mechanism after spike
- Leaky integration provides natural temporal filtering of glucose signals

#### 3. PDDS Pipeline Architecture
- **Input layer**: Poisson-encoded glucose time-series
- **Hidden layers**: Recurrent LIF neuron populations
- **Output layer**: Insulin dose prediction (regression or classification)
- **Event-driven processing**: Computation only when input spikes arrive
- **Personalization**: Patient-specific model adaptation using OhioT1DM data

#### 4. OhioT1DM Dataset Integration
- Real-world Type 1 Diabetes patient data
- Continuous glucose monitoring (CGM) traces
- Insulin bolus/basal records
- Patient metadata for personalization

## Implementation Guide

### Prerequisites
- Python 3.8+ with PyTorch
- Spiking neural network framework (SpikingJelly, snnTorch, or Norse)
- OhioT1DM dataset (available upon request from Ohio University)

### Step-by-Step

1. **Data preprocessing**
   ```python
   import numpy as np
   
   def preprocess_ohiot1dm(glucose_traces, insulin_records):
       """Preprocess OhioT1DM data for spike encoding."""
       # Normalize glucose values to [0, 1] range
       g_min, g_max = 40, 400  # mg/dL typical range
       normalized = (glucose_traces - g_min) / (g_max - g_min)
       normalized = np.clip(normalized, 0, 1)
       return normalized, insulin_records
   ```

2. **Poisson spike encoding**
   ```python
   def poisson_encode(data, n_steps=100, max_rate=200):
       """Convert continuous glucose data to Poisson spike trains."""
       batch_size, features = data.shape
       spikes = np.random.rand(batch_size, features, n_steps) < (data[:, :, None] * max_rate / n_steps)
       return spikes.astype(np.float32)
   ```

3. **LIF neuron implementation**
   ```python
   import torch
   import torch.nn as nn
   
   class LIFNeuron(nn.Module):
       def __init__(self, threshold=1.0, decay=0.9, reset=0.0):
           super().__init__()
           self.threshold = threshold
           self.decay = decay
           self.reset = reset
       
       def forward(self, x, mem):
           mem = self.decay * mem + x
           spike = (mem > self.threshold).float()
           mem = mem * (1 - spike) + self.reset * spike
           return spike, mem
   ```

4. **Build PDDS model and train**
   ```python
   class PDDSModel(nn.Module):
       def __init__(self, input_dim, hidden_dim, output_dim):
           super().__init__()
           self.fc1 = nn.Linear(input_dim, hidden_dim)
           self.lif1 = LIFNeuron()
           self.fc2 = nn.Linear(hidden_dim, output_dim)
       
       def forward(self, x, n_steps):
           mem = torch.zeros(x.size(0), self.fc1.out_features)
           outputs = []
           for t in range(n_steps):
               cur = self.fc1(x[:, :, t])
               spike, mem = self.lif1(cur, mem)
               out = self.fc2(spike)
               outputs.append(out)
           return torch.stack(outputs).mean(dim=0)
   ```

5. **Personalize per patient**
   - Fine-tune base model on individual patient data
   - Adjust Poisson encoding rate to patient glucose range
   - Calibrate output to patient insulin sensitivity

## Applications
- **Insulin pump control**: Neuromorphic backend for closed-loop insulin delivery
- **Blood glucose prediction**: Event-driven forecasting of glucose levels
- **Wearable health devices**: Energy-efficient SNN inference on edge hardware
- **Personalized medicine**: Patient-adaptive neural network models
- **Clinical decision support**: Assist clinicians with insulin dose recommendations

## Key Results
- 85.24% accuracy on OhioT1DM dataset
- Event-driven computation reduces energy vs. conventional ANN
- Poisson encoding preserves temporal glucose dynamics
- LIF neurons provide natural temporal integration

## Pitfalls
- OhioT1DM is a small dataset — risk of overfitting, use cross-validation
- Poisson encoding introduces stochasticity — results may vary across runs
- Clinical deployment requires extensive safety validation (FDA/CE approval)
- Blood glucose dynamics have significant inter-patient variability
- Spike encoding parameters (max_rate, n_steps) need careful tuning
- Not directly comparable to non-spiking baselines without matched architectures

## Related Skills
- neuromorphic-low-power-ai
- snn-learning-neuromorphic
- async-delta-modulator-bmi
- spike-ptsd-adversarial
- bci-rehabilitation-protocols

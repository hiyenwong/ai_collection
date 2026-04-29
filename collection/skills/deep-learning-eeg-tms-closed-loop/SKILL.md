---
title: Deep Learning EEG-TMS Closed-Loop System
description: Closed-loop deep learning framework combining real-time EEG monitoring with TMS stimulation. Uses DL models to predict optimal TMS parameters from brain state with <50ms latency for real-time adaptive neuromodulation.
activation: "EEG-TMS closed-loop, deep learning TMS, real-time brain stimulation, adaptive neuromodulation"
categories: ["neuroscience", "closed-loop", "TMS", "EEG", "deep-learning", "neuromodulation"]
trigger_keywords: ["EEG TMS closed-loop", "deep learning TMS", "adaptive stimulation", "real-time neuromodulation", "closed-loop brain stimulation", "EEG-guided TMS", "TMS parameter optimization", "real-time brain state", "personalized TMS", "adaptive TMS protocol"]
related_skills:
  - neuro-planner-llm-brain-interfaces
  - brain-dit-fmri-foundation-model
  - eeg-foundation-model-adapters
  - eeg-brain-connectivity-bci
  - brain-state-transition-network-control
source_paper: "Deep Learning EEG-TMS Closed-Loop System"
source_url: "https://arxiv.org/abs/2604.15099"
created: 2026-04-19
version: 1.0
---

# Deep Learning EEG-TMS Closed-Loop System

## Overview

A closed-loop framework that combines real-time EEG monitoring with transcranial magnetic stimulation (TMS) guided by deep learning models. The system continuously analyzes brain state from EEG and dynamically adjusts TMS parameters (frequency, intensity, timing, location) for personalized neuromodulation with <50ms latency.

## When to Use

- Personalized depression treatment (rTMS)
- Stroke rehabilitation with adaptive stimulation
- Epilepsy seizure prediction and prevention
- Chronic pain management
- Cognitive enhancement protocols
- Research on causal brain network manipulation

## Closed-Loop Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CLOSED-LOOP SYSTEM                          │
│                                                                     │
│  EEG Acquisition → Preprocessing → State Estimation → TMS Parameters│
│       ↑                                                    │         │
│       │                                                    ↓         │
│       │                                           TMS Delivery       │
│       │                                                    │         │
│       └──── Response Monitoring ←←←←←←←←←←←←←←←←←←←←←←←←←─┘         │
│                                                                     │
│  Total latency: < 50ms (EEG→TMS)                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Component Details

**1. EEG Acquisition (1-2ms)**
- High-density EEG (64-256 channels)
- Sampling rate: 500-1000 Hz
- Hardware: Active electrodes with low impedance

**2. Real-time Preprocessing (5-10ms)**
- Online artifact removal (eye blink, muscle)
- Bandpass filtering (1-45 Hz)
- Re-referencing (common average)
- Epoch extraction (sliding window)

**3. State Estimation (10-20ms)**
- Deep learning encoder (TCN or Transformer)
- Brain state features:
  - Power spectral density in canonical bands
  - Functional connectivity patterns
  - Phase-amplitude coupling
  - Network state classification
- Latent state representation

**4. TMS Parameter Prediction (5-10ms)**
- Deep policy network mapping state → TMS parameters
- Parameters:
  - Frequency (1-20 Hz)
  - Intensity (% motor threshold)
  - Coil position (target ROI)
  - Pulse timing (phase-locked)
  - Train duration
- Safety constraints embedded in network

**5. TMS Delivery (5-10ms)**
- Robot-assisted coil positioning
- Phase-locked stimulation (EEG phase)
- Intensity modulation in real-time
- Automated coil cooling management

**6. Response Monitoring (continuous)**
- Post-TMS EEG changes
- Behavioral feedback (if available)
- Safety monitoring (seizure detection)
- Adaptation signal for next iteration

## Deep Learning Models

### EEG Encoder Architecture

**Temporal Convolutional Network (TCN):**
```python
class EEGEncoder(nn.Module):
    def __init__(self, n_channels=64, n_classes=8):
        super().__init__()
        self.conv1 = nn.Conv1d(n_channels, 128, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(128, 256, kernel_size=3, padding=1)
        self.conv3 = nn.Conv1d(256, 512, kernel_size=3, padding=1)
        self.fc = nn.Linear(512, latent_dim)

    def forward(self, x):
        # x: (batch, channels, time)
        x = F.gelu(self.conv1(x))
        x = F.gelu(self.conv2(x))
        x = F.gelu(self.conv3(x))
        x = F.adaptive_avg_pool1d(x, 1)
        return self.fc(x.squeeze(-1))
```

**Transformer-based Encoder:**
```python
class EEGTransformer(nn.Module):
    def __init__(self, n_channels=64, d_model=256, n_heads=8):
        super().__init__()
        self.proj = nn.Linear(n_channels, d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=1024
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=6)

    def forward(self, x):
        # x: (batch, time, channels)
        x = self.proj(x)
        return self.transformer(x)[:, -1, :]  # Last time step
```

### TMS Policy Network

**Reinforcement Learning Approach:**
```python
class TMSPolicy(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim),
            nn.Tanh()  # Bounded output
        )
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 1)
        )

    def forward(self, state):
        action = self.actor(state)
        value = self.critic(state)
        return action, value
```

### Real-time Inference Optimization
```python
# Optimized for <50ms latency
class RealTimeEngine:
    def __init__(self, model):
        self.model = model
        self.model.eval()
        self.model = torch.jit.script(self.model)  # JIT compilation

    def predict(self, eeg_segment):
        with torch.no_grad():
            state = self.encoder(eeg_segment)
            action, _ = self.policy(state)
        return action  # TMS parameters
```

## Training Pipeline

### Phase 1: Supervised Pre-training
- Use historical EEG-TMS datasets
- Learn state-action mappings from expert protocols
- Loss: MSE between predicted and expert TMS parameters

### Phase 2: Reinforcement Learning Fine-tuning
- Deploy in simulation (computational brain model)
- Reward function:
  - Target engagement: +1 for desired brain state
  - Safety penalty: -10 for adverse patterns
  - Stability bonus: +0.5 for consistent state
- Algorithm: PPO or SAC

### Phase 3: Clinical Validation
- Pilot studies with safety monitoring
- Offline analysis of closed-loop performance
- Gradual transition to real-time deployment

## Safety Mechanisms

1. **Hard Limits:**
   - Maximum intensity: 120% resting motor threshold
   - Maximum frequency: 20 Hz
   - Maximum train duration: 10 seconds
   - Minimum inter-train interval: 10 seconds

2. **Soft Constraints:**
   - Adverse pattern detection (epileptiform activity)
   - Cumulative dose monitoring
   - Patient discomfort feedback integration

3. **Emergency Stop:**
   - Automatic shutdown on seizure detection
   - Manual override button
   - Continuous vital sign monitoring

## Applications

- **Depression:** Adaptive rTMS targeting DLPFC based on real-time EEG biomarkers
- **Stroke:** Phase-locked stimulation to enhance neuroplasticity
- **Epilepsy:** Pre-seizure state detection and preventive stimulation
- **Pain:** Closed-loop motor cortex stimulation for chronic pain
- **Cognition:** Working memory enhancement via targeted stimulation

## Pitfalls

1. **Latency Budget:** Total loop latency must be <50ms. Any component exceeding this breaks real-time operation.
2. **TMS Artifact:** TMS pulses create massive EEG artifacts. Need specialized artifact removal algorithms.
3. **Individual Variability:** Brain responses to TMS vary significantly. Personalization is essential.
4. **State Estimation Noise:** EEG state estimates are noisy. Use temporal smoothing or Bayesian filtering.
5. **Safety First:** Always have hardware-level safety limits independent of the AI system.
6. **Regulatory Compliance:** Closed-loop medical devices require FDA/CE approval. Plan for clinical trials.

## Evaluation Metrics

- **Loop Latency:** Time from EEG acquisition to TMS delivery
- **State Tracking Accuracy:** Correlation between estimated and true brain state
- **Target Engagement:** E-field strength at target ROI
- **Clinical Outcomes:** Standardized rating scales (e.g., HAM-D for depression)
- **Safety Incidents:** Number of adverse events per session
- **Adaptation Speed:** Time to reach optimal stimulation parameters

## Future Directions

- Multi-site closed-loop stimulation for network-level modulation
- Integration with fMRI for deeper brain target guidance
- Federated learning across clinical sites
- Automated protocol discovery
- Combination with pharmacological interventions

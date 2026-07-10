---
name: bimoe-brain-inspired-experts-eeg
description: "Brain-Inspired Mixture of Experts (BiMoE) framework for EEG-dominant affective state recognition. Uses brain-topology-aware expert partitioning with dual-stream encoders and adaptive routing for multimodal sentiment analysis combining EEG with peripheral physiological signals. Activation: BiMoE, brain-inspired MoE, EEG affective recognition, multimodal sentiment analysis, topology-aware experts, physiological signal fusion."
---

# BiMoE: Brain-Inspired Mixture of Experts for EEG-Dominant Affective State Recognition

> A brain-topology-aware Mixture of Experts framework that addresses EEG signal heterogeneity and enhances interpretability through region-specific expert partitioning and adaptive fusion with peripheral physiological signals.

## Metadata
- **Source**: arXiv:2603.29205v1
- **Authors**: Yansen Wang, Xiangfei Meng, Jingyu Liu, Shuang Qiu, Haichao Liu, Hongze Zhao, Ziyu Jia
- **Published**: 2026-03-31
- **Category**: Computer Science > Human-Computer Interaction
- **Institution**: Beijing University of Technology, Beijing Laboratory of Advanced Information Networks

## Core Methodology

### Problem Statement
Multimodal Sentiment Analysis (MSA) integrating Electroencephalogram (EEG) with peripheral physiological signals (PPS) faces three key challenges:

1. **Region-specific characteristics overlooked**: Existing methods treat EEG signals as homogeneous, ignoring the brain-topology organization of affective processing
2. **Lack of interpretability**: EEG is treated as black-box input without revealing neural representations
3. **Ineffective fusion**: EEG features are not effectively combined with complementary PPS features

### Key Innovation

**Brain-Topology-Aware Expert Partitioning**: Unlike conventional MoE architectures that partition experts arbitrarily, BiMoE explicitly maps experts to brain regions based on known functional localization:

- **Frontal Experts**: Handle affective valence and executive control
- **Temporal Experts**: Process auditory and emotional memory
- **Parietal Experts**: Integrate sensory information
- **Occipital Experts**: Process visual stimuli
- **PPS Expert**: Dedicated expert for peripheral physiological signals

### Technical Framework

#### 1. Topology-Aware EEG Partitioning
```
EEG Channels → Brain Region Mapping → Expert Assignment
   ↓                    ↓                    ↓
128 channels      5 functional           5 specialized
(10-20 system)    regions                experts
```

**Region Channel Assignment** (based on international 10-20 system):
- Frontal: Fp1, Fp2, AF3, AF4, AF7, AF8, F1, F2, F3, F4, F5, F6, F7, F8, Fz, FC1, FC2, FC3, FC4, FC5, FC6
- Temporal: FT7, FT8, T7, T8, TP7, TP8
- Parietal: CP1, CP2, CP3, CP4, CP5, CP6, P1, P2, P3, P4, P5, P6, P7, P8, Pz, PO3, PO4, PO7, PO8
- Occipital: O1, O2, Oz, POz
- Central: C1, C2, C3, C4, C5, C6, Cz

#### 2. Dual-Stream EEG Encoder
Each EEG expert employs a **dual-stream architecture**:

- **Local Stream**: Small-kernel convolutions (1×3, 1×5) for fine-grained temporal dynamics
- **Global Stream**: Large-kernel convolutions (1×31) with dilation for long-range dependencies

**Channel Attention Mechanism**:
- Applies squeeze-and-excitation across channels
- Adaptively weights electrode contributions within each region
- Enhances region-specific feature learning

#### 3. PPS Expert with Multi-Scale Convolutions

**Peripheral Physiological Signals** include:
- GSR (Galvanic Skin Response)
- TEMP (Skin Temperature)
- RESP (Respiration)
- ECG (Electrocardiogram)

**Processing**:
- Multi-scale large-kernel convolutions (1×7, 1×15)
- Captures diverse temporal scales in physiological responses
- Single-stream design (PPS signals are more homogeneous)

#### 4. Adaptive Expert Fusion

**Routing Mechanism**:
```
EEG Features (4 experts) + PPS Features (1 expert)
           ↓
    Gating Network
           ↓
    Softmax Weights → Weighted Sum → Fused Representation
```

**Gating Strategy**:
- Input-dependent routing: Different samples activate different expert combinations
- Sparse activation: Top-k expert selection for efficiency
- Learnable temperature: Controls exploration vs exploitation

#### 5. Joint Loss Function

$$
\mathcal{L}_{total} = \mathcal{L}_{sentiment} + \lambda_1 \mathcal{L}_{consistency} + \lambda_2 \mathcal{L}_{diversity}
$$

Where:
- $\mathcal{L}_{sentiment}$: Binary cross-entropy for sentiment classification
- $\mathcal{L}_{consistency}$: Expert prediction agreement loss
- $\mathcal{L}_{diversity}$: Encourages diverse expert specializations

## Implementation Guide

### Prerequisites
- Python ≥ 3.8
- PyTorch ≥ 1.12
- NumPy, SciPy
- GPU with CUDA support (recommended)

### Step-by-Step Implementation

#### Step 1: Define Brain Region Mappings
```python
# Brain region channel mapping (DEAP dataset format)
BRAIN_REGIONS = {
    'frontal': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 
                15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    'temporal': [27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    'parietal': [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 
                 49, 50, 51, 52, 53, 54, 55],
    'occipital': [56, 57, 58, 59],
    'central': [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
}
```

#### Step 2: Implement Dual-Stream Expert
```python
import torch
import torch.nn as nn

class DualStreamExpert(nn.Module):
    """
    Dual-stream expert for EEG signal processing
    """
    def __init__(self, in_channels, out_channels, kernel_sizes=[3, 5, 31]):
        super().__init__()
        
        # Local stream - fine temporal patterns
        self.local_conv1 = nn.Conv1d(in_channels, out_channels//2, kernel_sizes[0])
        self.local_conv2 = nn.Conv1d(in_channels, out_channels//2, kernel_sizes[1])
        
        # Global stream - long-range dependencies
        self.global_conv = nn.Conv1d(
            in_channels, out_channels, kernel_sizes[2], 
            dilation=6, padding=(kernel_sizes[2]-1)//2 * 6
        )
        
        # Channel attention
        self.se = nn.Sequential(
            nn.AdaptiveAvgPool1d(1),
            nn.Conv1d(out_channels * 2, out_channels * 2 // 4, 1),
            nn.ReLU(),
            nn.Conv1d(out_channels * 2 // 4, out_channels * 2, 1),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        # Local features
        local = torch.cat([self.local_conv1(x), self.local_conv2(x)], dim=1)
        
        # Global features  
        global_feat = self.global_conv(x)
        
        # Concatenate and apply channel attention
        combined = torch.cat([local, global_feat], dim=1)
        attention = self.se(combined)
        return combined * attention
```

#### Step 3: Implement Gating Network
```python
class GatingNetwork(nn.Module):
    """
    Adaptive routing for expert fusion
    """
    def __init__(self, input_dim, num_experts, top_k=3):
        super().__init__()
        self.num_experts = num_experts
        self.top_k = top_k
        
        self.gate = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_experts)
        )
        
    def forward(self, x, temperature=1.0):
        logits = self.gate(x)
        
        # Top-k gating with temperature
        weights = torch.softmax(logits / temperature, dim=-1)
        
        # Sparsify: keep only top-k
        top_k_weights, top_k_indices = torch.topk(weights, self.top_k, dim=-1)
        sparse_weights = torch.zeros_like(weights)
        sparse_weights.scatter_(-1, top_k_indices, top_k_weights)
        
        # Re-normalize
        sparse_weights = sparse_weights / sparse_weights.sum(dim=-1, keepdim=True)
        
        return sparse_weights, top_k_indices
```

#### Step 4: Complete BiMoE Model
```python
class BiMoE(nn.Module):
    """
    Brain-Inspired Mixture of Experts for EEG-dominant affective recognition
    """
    def __init__(self, eeg_channels=128, pps_channels=8, 
                 seq_len=128, num_experts=5, expert_dim=128):
        super().__init__()
        
        # EEG experts (4 brain regions)
        self.eeg_experts = nn.ModuleList([
            DualStreamExpert(len(ch), expert_dim)
            for ch in [
                BRAIN_REGIONS['frontal'],
                BRAIN_REGIONS['temporal'], 
                BRAIN_REGIONS['parietal'],
                BRAIN_REGIONS['occipital']
            ]
        ])
        
        # PPS expert (1)
        self.pps_expert = nn.Sequential(
            nn.Conv1d(pps_channels, expert_dim, 7, padding=3),
            nn.BatchNorm1d(expert_dim),
            nn.ReLU(),
            nn.Conv1d(expert_dim, expert_dim, 15, padding=7),
            nn.BatchNorm1d(expert_dim),
            nn.ReLU()
        )
        
        # Gating network
        self.gating = GatingNetwork(eeg_channels * seq_len, num_experts)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(expert_dim * num_experts, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 2)  # Binary sentiment
        )
        
    def forward(self, eeg, pps, temperature=1.0):
        batch_size = eeg.size(0)
        
        # Extract features from each EEG expert
        eeg_features = []
        regions = [
            BRAIN_REGIONS['frontal'],
            BRAIN_REGIONS['temporal'],
            BRAIN_REGIONS['parietal'], 
            BRAIN_REGIONS['occipital']
        ]
        
        for i, expert in enumerate(self.eeg_experts):
            region_eeg = eeg[:, regions[i], :]
            feat = expert(region_eeg)
            feat = torch.mean(feat, dim=-1)  # Global average pooling
            eeg_features.append(feat)
        
        # Extract PPS features
        pps_feat = self.pps_expert(pps)
        pps_feat = torch.mean(pps_feat, dim=-1)
        
        # Combine all expert outputs
        all_features = eeg_features + [pps_feat]
        
        # Flatten for gating
        flat_eeg = eeg.view(batch_size, -1)
        gate_weights, _ = self.gating(flat_eeg, temperature)
        
        # Weighted fusion
        fused = torch.stack(all_features, dim=1)  # [B, num_experts, dim]
        gate_weights = gate_weights.unsqueeze(-1)  # [B, num_experts, 1]
        fused = (fused * gate_weights).sum(dim=1)  # [B, dim]
        
        # Classification
        output = self.classifier(fused)
        return output, gate_weights.squeeze(-1)
```

### Training Configuration

```python
# Hyperparameters
CONFIG = {
    'learning_rate': 1e-4,
    'batch_size': 32,
    'epochs': 100,
    'temperature': 1.0,
    'temperature_decay': 0.95,
    'lambda_consistency': 0.1,
    'lambda_diversity': 0.05,
    'top_k': 3
}

# Temperature annealing during training
def update_temperature(epoch, initial_temp=1.0, decay_rate=0.95):
    return initial_temp * (decay_rate ** epoch)
```

## Experimental Results

**Dataset**: DEAP (Database for Emotion Analysis using Physiological Signals)
- 32 participants
- 40 one-minute music video trials
- 32-channel EEG + 8 peripheral signals
- Valence-Arousal annotations

**Subject-Independent Evaluation**:
| Method | Accuracy | F1 Score | Interpretability |
|--------|----------|----------|------------------|
| SVM (baseline) | 62.3% | 0.61 | Low |
| CNN-LSTM | 68.5% | 0.67 | Low |
| Transformer | 70.2% | 0.69 | Medium |
| MM-Sparse | 72.1% | 0.71 | Low |
| **BiMoE** | **76.8%** | **0.75** | **High** |

**Expert Specialization Analysis**:
- Frontal expert: Most active for high-arousal stimuli (38.2%)
- Temporal expert: Dominates for music-induced emotions (29.5%)
- PPS expert: Consistent across all conditions (22.1% average)

## Applications

1. **Affective Computing**: Real-time emotion recognition for adaptive interfaces
2. **Mental Health Monitoring**: Depression and anxiety assessment via EEG
3. **Brain-Computer Interfaces**: Emotion-aware BCI for neurofeedback
4. **Human-Robot Interaction**: Emotion recognition for social robots
5. **Gaming**: Adaptive difficulty based on player affective state

## Pitfalls

1. **Channel Position Dependency**: Requires accurate electrode positioning; results degrade with misaligned caps
2. **Individual Differences**: EEG patterns vary significantly across subjects; requires subject-independent validation
3. **Expert Imbalance**: Some experts may dominate; monitor gate weight distribution
4. **Computational Cost**: Multiple experts increase inference time; consider pruning for deployment
5. **Limited Generalization**: Trained on DEAP; performance on other datasets requires fine-tuning

## Related Skills

- `eeg-mftnet-multi-scale-temporal`: Multi-scale temporal convolutions for EEG
- `bandrouternet-eeg-artifact`: EEG artifact removal techniques
- `mixture-of-experts-routing`: General MoE routing principles
- `multimodal-brain-network-m3d-bfs`: Multimodal brain network fusion
- `neurocognitive-governance-ai-agents`: Affective state in cognitive architectures

## Key Insights

**Neuroscience-Inspired Design**: By explicitly mapping experts to brain regions, BiMoE achieves both:
- **Performance**: Higher accuracy through specialized feature learning
- **Interpretability**: Gate weights reveal which brain regions drive predictions

**Adaptive Fusion**: The gating mechanism learns which modalities/regions are most predictive for each sample, enabling dynamic allocation of computational resources.

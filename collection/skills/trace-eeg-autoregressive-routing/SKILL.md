---
name: trace-eeg-autoregressive-routing
description: "TRACE (Temporal Routing with Autoregressive Cross-channel Experts) framework for EEG representation learning. Autoregressive pre-training that predicts future EEG patches from causal context using a novel Temporal Routing MoE (TR-MoE) architecture. Key innovation: Cross-Channel Temporal Routing FFN (CTR-FFN) that routes all channels at the same temporal step to the same experts based on causal cross-channel history, preserving instantaneous cross-channel coherence while adapting computation to non-stationary temporal EEG states. Supports heterogeneous pre-training across different channel counts (16-128), montages, sequence lengths, and recording domains. Evaluated on 8 downstream BCI benchmarks across 6 task categories. arXiv: 2605.11380 (cs.LG, cs.AI). Ma, An, Chen, Qian, Lan, Jiang, Gu, Papademetris, Xu."
---

# TRACE: Temporal Routing with Autoregressive Cross-channel Experts

Autoregressive EEG pre-training framework that predicts future EEG patches from causal context
while performing temporally adaptive and cross-channel coherent computation. Addresses the
fundamental challenge that standard MoE routing (token-wise, per-channel) breaks cross-channel
coherence in multi-channel EEG.

**Source**: arXiv 2605.11380v1 (2026-05-12), cs.LG, cs.AI
**Institution**: Yale University, Department of Biomedical Informatics and Data Science

## Core Problem

Learning transferable EEG representations is challenging because:
1. EEG signals are inherently **multi-channel and non-stationary**
2. Channels at the same time step are **coupled measurements** of a shared latent brain state
3. Standard token-wise MoE routing assigns each channel patch independently, **breaking cross-channel coherence**
4. Masked modeling (BERT-style) overlooks **intrinsic causal dynamics** crucial for online monitoring

## Key Innovation

**Cross-Channel Temporal Routing (CTR)**: At each temporal step, derive a single expert routing
decision from the causal cross-channel history, and apply it **jointly to all channels** at that step.
This preserves instantaneous cross-channel coherence while allowing different temporal regimes
to activate different computation pathways.

## Architecture

### Overall Framework

```
Raw EEG Signal → Patch Encoder → TR-MoE Block → Forecasted EEG Patches
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
    Causal Spatial-temporal    Cross-channel          Multi-horizon
         Attention            Temporal Routing FFN       Decoder
              │                     │                     │
              │    TemporalFormer → Expert Selector       │
              │         Router          │                 │
              └─────────────────────────┴─────────────────┘
```

### TR-MoE Block Components

#### 1. Multi-Scale Patch Encoder

- Time Conv with multi-scale temporal receptive fields
- FFT Mask for frequency-aware processing
- Channel Positional Encoding (no fixed montage assumption)

#### 2. Causal Spatial-Temporal Attention

Processes spatial (cross-channel) and temporal dependencies:
- Spatial Attention: Cross-channel information exchange
- Temporal Attention: Causal-time dependency modeling
- **Gated Fusion**: Combines spatial and temporal representations

#### 3. CTR-FFN (Cross-channel Temporal Routing Feed-Forward Network)

**Core innovation** — replaces standard FFN in Transformer blocks:

```
TemporalFormer Router → Expert Selector → CTR-FFN
         │                   │                │
    (summarizes          (routes all     (applies expert
     cross-channel        channels to     computation to
     causal history)      same experts)   all channels)
```

- **TemporalFormer Router**: Summarizes causal cross-channel history into a temporal-state representation
- **Expert Selector**: Uses temporal-state representation to select K experts for the current time step
- **Shared routing decision**: All channels at the same temporal step receive the same expert assignment
- Preserves cross-channel coherence while enabling adaptive computation

#### 4. Multi-Horizon Autoregressive Decoder

Predicts EEG patches at multiple future horizons: H = {1, 2, 4} steps ahead.
This captures both short-term dynamics and longer-range temporal transitions.

### Heterogeneous Pre-Training

TRACE supports training across heterogeneous EEG corpora **without projecting to a common montage**:

| Corpus | Type | Channels | Description |
|---|---|---|---|
| TUEG | Clinical | Variable | Temple University Hospital EEG |
| HBN | Healthy population | High-density | Healthy Brain Network |
| Task datasets | Various | 16-128 | Motor imagery, emotion, etc. |

- **1.5M+ EEG segments** for pre-training
- Channel counts: 16-128
- Sequence lengths: 4-30 seconds
- Pre-trained on **4 NVIDIA H100 GPUs**

### Pre-Training Objective

Multi-horizon autoregressive forecasting:

$$L_{AR} = \sum_{h \in H} \| \text{EEG}[t+h] - \hat{\text{EEG}}[t+h] \|^2$$

where H = {1, 2, 4} captures different temporal scales of neural dynamics.

## Downstream Evaluation

Evaluated on **8 datasets** across **6 BCI task categories**:

| Task Category | Datasets | Transfer Type |
|---|---|---|
| Sleep Staging | ISRUC | Seen-domain |
| Emotion Recognition | SEED-V, FACED | Unseen/Seen |
| Motor Imagery | PhysioNet-MI, SHU-MI | Seen/Unseen |
| Seizure Detection | CHB-MIT | Seen-domain |
| Imagined Speech | BCIC2020-3 | Unseen |
| Event Classification | TUEV | Unseen |

**Two transfer regimes**:
1. **Seen-domain**: Downstream domain observed only through unlabeled pre-training data
2. **Unseen-dataset**: Downstream dataset completely excluded from pre-training

## Implementation Pattern

```python
import torch
import torch.nn as nn

class TRMoEBlock(nn.Module):
    """Temporal Routing Mixture-of-Experts Block for EEG."""
    
    def __init__(self, d_model, n_experts, top_k=2, n_heads=8):
        super().__init__()
        # Causal spatial-temporal attention
        self.spatial_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True)
        self.temporal_attn = nn.MultiheadAttention(d_model, n_heads, batch_first=True, causal=True)
        self.gated_fusion = nn.Sequential(
            nn.Linear(d_model * 2, d_model),
            nn.GELU(),
            nn.Linear(d_model, d_model)
        )
        
        # CTR-FFN components
        self.temporal_router = nn.TransformerEncoderLayer(
            d_model, n_heads, dim_feedforward=d_model * 4
        )
        self.expert_selector = nn.Linear(d_model, n_experts)
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_model * 4),
                nn.GELU(),
                nn.Linear(d_model * 4, d_model)
            ) for _ in range(n_experts)
        ])
        self.top_k = top_k
        
    def forward(self, x):
        """
        x: (batch, n_channels, seq_len, d_model)
        """
        # 1. Spatial-temporal attention
        # Reshape for cross-channel attention
        batch, n_ch, seq, dim = x.shape
        
        # Spatial attention: treat channels as sequence
        x_spatial = x.transpose(1, 2).reshape(batch * seq, n_ch, dim)
        x_spatial, _ = self.spatial_attn(x_spatial, x_spatial, x_spatial)
        x_spatial = x_spatial.view(batch, seq, n_ch, dim).transpose(1, 2)
        
        # Temporal attention: causal over time
        x_temporal = x.reshape(batch * n_ch, seq, dim)
        x_temporal, _ = self.temporal_attn(x_temporal, x_temporal, x_temporal)
        x_temporal = x_temporal.view(batch, n_ch, seq, dim)
        
        # Gated fusion
        x = self.gated_fusion(torch.cat([x_spatial, x_temporal], dim=-1))
        
        # 2. Cross-Channel Temporal Routing
        # Router: summarize cross-channel history for each time step
        cross_channel_state = x.mean(dim=1)  # (batch, seq, dim)
        router_output = self.temporal_router(cross_channel_state)
        
        # Expert selection: one decision per time step, shared across channels
        routing_logits = self.expert_selector(router_output)  # (batch, seq, n_experts)
        top_k_experts = torch.topk(routing_logits, self.top_k, dim=-1)
        
        # Apply selected experts to all channels at each time step
        expert_outputs = torch.zeros_like(x)
        for t in range(seq):
            selected = top_k_experts.indices[:, t, :]  # (batch, top_k)
            weights = top_k_experts.values[:, t, :]
            weights = torch.softmax(weights, dim=-1)
            
            for b in range(batch):
                combined = torch.zeros(dim)
                for k in range(self.top_k):
                    expert_idx = selected[b, k].item()
                    combined = combined + weights[b, k] * self.experts[expert_idx](x[b, :, t, :])
                expert_outputs[b, :, t, :] = combined
        
        return expert_outputs

class TRACE(nn.Module):
    def __init__(self, n_layers=6, d_model=256, n_experts=8, top_k=2):
        super().__init__()
        self.patch_encoder = MultiScalePatchEncoder()
        self.blocks = nn.ModuleList([
            TRMoEBlock(d_model, n_experts, top_k) for _ in range(n_layers)
        ])
        self.decoder = MultiHorizonDecoder(horizons=[1, 2, 4])
        
    def forward(self, eeg_signal):
        x = self.patch_encoder(eeg_signal)
        for block in self.blocks:
            x = block(x)
        return self.decoder(x)
```

## Use Cases

1. **EEG foundation model pre-training**: Building general-purpose EEG representations
2. **Online clinical monitoring**: Autoregressive modeling captures causal neural dynamics
3. **Heterogeneous EEG corpora**: Training across different montages without common projection
4. **Multi-channel EEG analysis**: Preserving cross-channel coherence in MoE architectures
5. **Temporal state adaptation**: Different neural states activate different expert pathways

## Comparison to Prior EEG Foundation Models

| Model | Pre-training Objective | MoE Routing | Cross-channel Coherence | Heterogeneous Support |
|---|---|---|---|---|
| BIOT | Masked reconstruction | None | Full | Limited |
| LaBraM | Token-level masking | None | Full | Limited |
| CBraMod | Masked reconstruction | None | Full | Limited |
| EEGPT | Autoregressive | Token-wise | Broken | Partial |
| **TRACE** | **Autoregressive** | **Cross-channel temporal** | **Preserved** | **Full** |

## Activation Keywords

- TRACE EEG framework, autoregressive EEG pre-training
- cross-channel temporal routing, TR-MoE
- CTR-FFN, temporal routing mixture-of-experts
- EEG foundation model, heterogeneous EEG training
- multi-channel EEG routing, non-stationary EEG representation
- causal EEG modeling, multi-horizon forecasting

## Pitfalls & Notes

- **Token-wise routing breaks EEG coherence**: Standard MoE assigns each channel independently,
  ignoring that channels at the same time step reflect the same latent brain state. Always use
  cross-channel shared routing for multi-channel EEG.
- **Autoregressive > Masked for temporal tasks**: Masked modeling (BERT-style) is effective for
  static classification but misses causal dynamics crucial for online continuous monitoring.
- **No fixed montage required**: TRACE encodes each channel as a temporal patch sequence with
  channel positional encoding. This eliminates the need to project all recordings onto a common montage.
- **Multi-horizon forecasting**: Using H={1,2,4} captures both short-term neural dynamics and
  longer-range state transitions. Single-horizon forecasting is insufficient.
- **Pre-training scale matters**: 1.5M+ segments across diverse corpora (clinical, healthy, task)
  is needed for robust generalization. Small pre-training corpora limit transfer performance.
- **Router design is critical**: The TemporalFormer router must summarize cross-channel history
  effectively. Simple pooling loses temporal structure.
- **Two transfer regimes are distinct**: Seen-domain and unseen-dataset generalization test
  different capabilities. Evaluate both for comprehensive assessment.

## Applications

1. Brain-computer interfaces (BCI) with transfer learning
2. Clinical EEG monitoring and seizure detection
3. Sleep staging and emotion recognition
4. Motor imagery classification
5. Cross-subject and cross-domain EEG generalization

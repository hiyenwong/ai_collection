---
name: wavemoe-time-series
description: "Wavelet-Enhanced Mixture-of-Experts (WaveMoE) foundation model for time series forecasting. Use when building time series prediction models, incorporating frequency-domain information, or designing MoE architectures for temporal data."
---

# WaveMoE: Wavelet-Enhanced Mixture-of-Experts for Time Series

A time series foundation model combining wavelet transforms with Mixture-of-Experts architecture for universal forecasting.

## Core Innovation

WaveMoE integrates:
1. **Wavelet Decomposition**: Captures multi-scale temporal patterns
2. **Mixture-of-Experts (MoE)**: Enables sparse, specialized computation
3. **Foundation Model Approach**: Pre-trained on diverse time series data

## Activation Keywords

- WaveMoE
- wavelet time series
- MoE forecasting
- time series foundation model
- frequency-domain time series
- multi-scale temporal
- wavelet MoE

## Architecture

### 1. Wavelet Transform Layer

```
Input: x(t) → Wavelet Transform → [cA_n, cD_n, ..., cD_1]
```

Where:
- cA_n: Approximation coefficients (low-frequency)
- cD_i: Detail coefficients (high-frequency at scale i)

### 2. Multi-Scale Expert Networks

Each wavelet component feeds into specialized experts:

```
cA_n → Expert_0 (trend)
cD_n → Expert_1 (coarse patterns)
cD_{n-1} → Expert_2
...
cD_1 → Expert_n (fine details)
```

### 3. Gating Network

Learns to route inputs to appropriate experts:

```
g_i(x) = Softmax(W_g · x + b_g)_i
output = Σ_i g_i(x) · Expert_i(x)
```

## Implementation Steps

### Step 1: Wavelet Decomposition

```python
import pywt

# Decompose time series
coeffs = pywt.wavedec(time_series, wavelet='db4', level=4)
cA4, cD4, cD3, cD2, cD1 = coeffs
```

### Step 2: Expert Architecture

```python
class WaveletExpert(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, x):
        return self.network(x)
```

### Step 3: WaveMoE Block

```python
class WaveMoEBlock(nn.Module):
    def __init__(self, num_experts, input_dim, expert_dim):
        super().__init__()
        self.experts = nn.ModuleList([
            WaveletExpert(input_dim, expert_dim) 
            for _ in range(num_experts)
        ])
        self.gate = nn.Linear(input_dim, num_experts)
    
    def forward(self, x_wavelet_coeffs):
        # x_wavelet_coeffs: list of wavelet coefficients
        outputs = []
        for expert, coeff in zip(self.experts, x_wavelet_coeffs):
            outputs.append(expert(coeff))
        
        # Gating
        gate_weights = F.softmax(self.gate(
            torch.cat(x_wavelet_coeffs, dim=-1)
        ), dim=-1)
        
        # Weighted combination
        output = sum(w * o for w, o in zip(gate_weights, outputs))
        return output
```

### Step 4: Training

```python
# Pre-training on diverse datasets
def pretrain_wavemoe(model, datasets, epochs):
    for epoch in range(epochs):
        for batch in datasets:
            x, y = batch
            coeffs = wavelet_decompose(x)
            pred = model(coeffs)
            loss = forecast_loss(pred, y)
            loss.backward()
            optimizer.step()
```

## Key Features

1. **Multi-Scale Modeling**: Wavelets naturally capture patterns at different time scales
2. **Sparse Computation**: MoE activates only relevant experts
3. **Frequency Awareness**: Explicit handling of frequency-domain information
4. **Universal**: Pre-trained across diverse time series domains

## Applications

- **Financial Forecasting**: Stock prices, trading volumes
- **Energy Load Prediction**: Power consumption forecasting
- **Weather Prediction**: Temperature, precipitation
- **Traffic Forecasting**: Transportation demand
- **Healthcare**: Vital signs prediction

## Advantages

1. Better handling of non-stationary data
2. Captures both local and global patterns
3. Computationally efficient via sparse expert activation
4. Improved generalization across domains

## Tools Used

- python: PyTorch/TensorFlow implementation
- exec: Run training and inference scripts
- write: Save model configurations, results

## References

- arXiv:2604.10544v1 (2026) - "WaveMoE: A Wavelet-Enhanced Mixture-of-Experts Foundation Model for Time Series Forecasting"
- Wavelet theory (Mallat, Daubechies)
- Mixture-of-Experts literature (Shazeer et al.)
- Time series foundation models (TimeGPT, etc.)

## Related Skills

- time-series-forecasting: General forecasting methods
- moe-architecture: Mixture-of-Experts patterns
- wavelet-analysis: Wavelet transform methods

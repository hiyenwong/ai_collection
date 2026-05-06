# SL-FAC: A Communication-Efficient Split Learning Framework with Frequency-Aware Compression

**arXiv ID**: 2604.07316v1
**Published**: 2026-04-08
**Authors**: Zehang Lin, Miao Yang, Haihan Zhu, Zheng Lin, Jianhao Huang
**PDF**: https://arxiv.org/pdf/2604.07316v1

## Summary

This paper proposes a communication-efficient split learning framework using frequency-aware compression. The approach decomposes smashed data (activations/gradients) into frequency components and applies adaptive quantization based on spectral energy.

## Key Contributions

### 1. Adaptive Frequency Decomposition (AFD)

Transform smashed data to frequency domain:
- FFT/DCT based decomposition
- Separation by spectral energy levels
- Identify critical vs. compressible components

### 2. Frequency-Based Quantization Compression (FQC)

Adaptive bit width assignment:
- High-energy components: 8-bit (preserve convergence)
- Low-energy components: 2-bit (aggressive compression)
- Spectral energy determines quantization level

### 3. Communication-Reduction Strategy

Preserve information critical for convergence while reducing bandwidth:
```
Bandwidth reduction = (high_bits + low_bits) / original_bits
                     = (8 + 2) / 32 ≈ 10× reduction
```

## Architecture

```
┌────────────────────────────────────────────┐
│  Edge Device                               │
│  ┌──────────────────────────────────────┐ │
│  │ Client Model (First Layers)          │ │
│  │ Output: Smashed Data [activations]   │ │
│  └──────────────────────────────────────┘ │
│              ↓                              │
│  ┌──────────────────────────────────────┐ │
│  │ Adaptive Frequency Decomposition     │ │
│  │ FFT → High/Low Energy Separation     │ │
│  └──────────────────────────────────────┘ │
│              ↓                              │
│  ┌──────────────────────────────────────┐ │
│  │ Frequency-Based Quantization         │ │
│  │ High: 8-bit, Low: 2-bit              │ │
│  └──────────────────────────────────────┘ │
└────────────────────────────────────────────┘
              ↓ Compressed Transmission
┌────────────────────────────────────────────┐
│  Edge Server                               │
│  ┌──────────────────────────────────────┐ │
│  │ Reconstruction from Quantized        │ │
│  │ Inverse FFT → Full Activations       │ │
│  └──────────────────────────────────────┘ │
│              ↓                              │
│  ┌──────────────────────────────────────┐ │
│  │ Server Model (Remaining Layers)      │ │
│  │ Training & Gradient Computation      │ │
│  └──────────────────────────────────────┘ │
│              ↓                              │
│  [Same compression pipeline for gradients] │
└────────────────────────────────────────────┘
```

## Key Results

| Metric | SL-FAC | Baseline |
|--------|--------|----------|
| Communication reduction | ~10× | 1× |
| Accuracy preserved | ✓ | - |
| Training convergence | Normal | - |

## Technical Details

### Frequency Decomposition

```python
# Transform to frequency domain
freq = dct(smashed_data, type=2, axis=-1, norm='ortho')

# Calculate spectral energy
energy = np.abs(freq) ** 2

# Threshold separation
high_energy_mask = energy >= threshold
low_energy_mask = ~high_energy_mask
```

### Adaptive Quantization

```python
# High-energy: preserve for convergence
high_bits = 8  # 256 levels

# Low-energy: aggressive compression
low_bits = 2   # 4 levels

# Energy-weighted quantization
quant_scale = energy / total_energy  # Per-component importance
```

## Applications to Distributed Systems

### Edge-Server Split Learning

- Partition large models between edge and server
- Minimize communication overhead
- Preserve training quality

### Multi-Device Coordination

- Scale to many edge devices
- Bandwidth-efficient aggregation
- Frequency-based gradient compression

### Resource-Constrained Deployment

- Enable distributed training on limited devices
- Reduce memory requirements
- Maintain accuracy

## Citation

Lin, Z., Yang, M., Zhu, H., Lin, Z., & Huang, J. (2026). SL-FAC: A Communication-Efficient Split Learning Framework with Frequency-Aware Compression. arXiv:2604.07316v1.
# WTA Spiking Transformer Examples

Complete PyTorch implementation of the Winner-Take-All Spiking Transformer from arXiv:2604.11321.

## Files

- `wta_spiking_transformer.py` - Full implementation with all components

## Quick Start

```python
from wta_spiking_transformer import WESpikingformer, WDSpikingformer

# Encoder-only for masked language modeling
we_model = WESpikingformer(
    vocab_size=30522,
    dim=768,
    depth=12,
    num_heads=12,
    time_steps=4
)

# Decoder-only for causal language modeling
wd_model = WDSpikingformer(
    vocab_size=50257,
    dim=1024,
    depth=24,
    num_heads=16,
    time_steps=4
)
```

## Running the Demo

```bash
python wta_spiking_transformer.py
```

This will run three demonstrations:
1. WE-Spikingformer (Encoder-only) for Masked Language Modeling
2. WD-Spikingformer (Decoder-only) for Causal Language Modeling
3. Training step demonstration

## Components Overview

### Spiking Neurons
- `T_LIF`: Ternary Leaky Integrate-and-Fire (-α, 0, α)
- `NI_LIF`: Normalized Integer LIF (faster training)

### Attention Mechanisms
- `WSSA`: WTA Spiking Self-Attention (encoder)
- `CWSSA`: Causal WTA Spiking Self-Attention (decoder)

### WTA Implementations
- `hard_wta`: Hard Winner-Take-All (one winner)
- `topk_wta`: Top-K Winner-Take-All (K winners)
- `SurrogateWTA`: WTA with softmax surrogate gradient

### Models
- `WESpikingformer`: Encoder-only for MLM
- `WDSpikingformer`: Decoder-only for CLM

## Requirements

```
torch>=2.0.0
```

## Paper Reference

Zhou et al. (2026). Winner-Take-All Spiking Transformer for Language Modeling. arXiv:2604.11321.

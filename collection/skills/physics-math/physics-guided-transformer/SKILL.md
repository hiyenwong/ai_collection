---
name: physics-guided-transformer
description: "Design Transformer architectures that embed physical structure (heat kernels, diffusion dynamics, temporal causality) into attention mechanisms. Use for physics-aware sequence modeling, scientific computing with Transformers, or when physical priors improve Transformer performance. Keywords: PGT, physics-guided attention, physics-aware Transformer, heat-kernel Transformer, diffusion attention, physical Transformer."
---

# Physics-Guided Transformer (PGT)

Embed physical structure directly into Transformer attention mechanisms for physics-aware sequence modeling.

## Core Innovation

**Key Insight:** Instead of pure self-attention, incorporate physics-derived biases into attention logits, encoding physical dynamics and causality.

## Design Pattern

### Heat-Kernel Attention Mechanism

**From arxiv:2603.27929 - Physics-Guided Transformer (PGT)**

The attention mechanism is augmented with a heat-kernel-derived additive bias:

```
Attention = softmax(QK^T / d + H) V

where H = heat kernel bias encoding:
  - Diffusion dynamics
  - Temporal causality
  - Spatial locality
```

**Physics Embedded:**
- **Heat Kernel**: Encodes diffusion process (spatial-temporal smoothing)
- **Causality**: Time-like attention direction
- **Locality**: Physics-inspired locality constraints

### Architecture Template

```
Input: Sequential data (time series, physical states)

Physics-Guided Attention Layers:
  1. Standard Q, K, V projection
  2. Heat-kernel bias computation:
     - H(x_i, x_j) = exp(-||x_i - x_j||^2 / 4τ)
     - τ = diffusion time parameter
  3. Attention logits: logits = QK^T + H
  4. Physics-aware softmax
  5. Value aggregation

Physical Constraints:
  - Temporal causality (attention respects time order)
  - Diffusion smoothing (heat kernel regularizes attention)
  - Energy conservation (total attention mass = 1)

Output: Physics-constrained sequence representations
```

## Implementation Guide

### Step 1: Choose Physical Prior

| Physical Prior | Bias Type | Application |
|---------------|-----------|-------------|
| Heat Kernel | Gaussian diffusion | Smoothing, locality |
| Wave Equation | Oscillatory | Wave propagation |
| Schrödinger | Quantum probability | Quantum systems |
| Dirac | Relativistic | Particle physics |

### Step 2: Compute Physical Bias

```python
# Heat kernel bias for attention
def heat_kernel_bias(x_i, x_j, tau):
    """Heat kernel H(x_i, x_j; τ) = exp(-||x_i - x_j||^2 / 4τ)"""
    distance_sq = torch.sum((x_i - x_j)**2, dim=-1)
    return torch.exp(-distance_sq / (4 * tau))

# Add to attention logits
attention_logits = Q @ K.transpose() / sqrt(d) + heat_kernel_bias
```

### Step 3: Temporal Causality

```python
# Enforce causality: attention only to past
def causal_mask(sequence_length):
    """Mask prevents attention to future positions"""
    return torch.triu(torch.ones(L, L), diagonal=1) * -inf

# Combined attention
attention_logits = QK + heat_kernel + causal_mask
```

### Step 4: Validate Physics

- Check attention mass conservation (sum to 1)
- Verify locality structure (nearby positions get higher attention)
- Test causality enforcement (no future leakage)

## Example: Diffusion Process Modeling

```
Physics: Heat equation u_t = α∇²u
Task: Predict temperature evolution

Architecture:
  Input: Temperature field sequence

  Physics-Guided Transformer:
    - Heat-kernel attention (diffusion dynamics)
    - Causal masking (time evolution)
    - Locality bias (local diffusion)

  Output: Next temperature state

  Physical Validation:
    - Heat equation satisfaction
    - Energy conservation
    - Stable long-time evolution

Benefits:
  - Attention respects diffusion physics
  - Natural locality from heat kernel
  - Stable extrapolation
```

## Comparison to Standard Transformer

| Feature | Standard Transformer | Physics-Guided Transformer |
|---------|---------------------|---------------------------|
| Attention | Pure learned weights | Physics-augmented weights |
| Locality | Learned position encoding | Physical locality from kernel |
| Causality | Optional mask | Physical causality enforcement |
| Stability | May need regularization | Physics provides stability |
| Interpretability | Black box | Physical meaning in attention |

## Key Papers

- **Physics-Guided Transformer (PGT)** (arxiv:2603.27929): Heat-kernel attention mechanism
- **Transformers are GNNs** (arxiv:2506.22084): Transformer-GNN connection
- **Geometric Algebra Transformer** (2604.01466): E(3)-equivariant architecture

## Tools Used

- `exec`: Run Transformer training, physical simulations
- `read`: Load physical equations, domain knowledge
- `write`: Document physics-guided architectures
- `edit`: Modify attention configurations

## Instructions for Agents

### Step 1: Identify Physical Process
Determine the physical dynamics (diffusion, wave propagation, etc.) relevant to the sequence data.

### Step 2: Design Physics Bias
Create heat-kernel or physics-derived bias matrix encoding the physical process.

### Step 3: Modify Attention
Augment standard attention with physics bias: `softmax(QK^T + H) V`.

### Step 4: Validate Physics
Ensure the model satisfies physical constraints (conservation, causality, stability).

### Step 5: Train and Deploy
Train with physics-augmented loss, deploy for scientific prediction tasks.

## Examples

### Example 1: Heat Equation Prediction

```
User: "Build a Transformer to predict heat diffusion"

Agent:
1. Identify: Heat equation dynamics ∂u/∂t = α∇²u
2. Design: Heat-kernel attention bias H = exp(-||x_i - x_j||²/4τ)
3. Modify: Attention = softmax(QK^T + H) V
4. Validate: Check energy conservation and stability
5. Train: On temperature field sequences
```

### Example 2: Wave Propagation Modeling

```
User: "Model wave propagation with physics-aware Transformer"

Agent:
1. Identify: Wave equation dynamics
2. Design: Wave-kernel attention with causality mask
3. Modify: Implement physics-guided attention layers
4. Validate: Ensure wave speed and dispersion match physics
5. Deploy: For seismic or acoustic wave prediction
```

## Activation Keywords

- physics-guided transformer
- PGT
- heat-kernel transformer
- physics-aware attention
- diffusion transformer
- 物理指导变换器

## Related Skills

- **physics-guided-neural-network**: General PGNN framework
- **gnn-transformer-fusion**: GNN-Transformer hybrid
- **transformer-architecture-optimization**: Transformer optimization

## Notes

- Heat kernel provides natural locality without learned position encoding
- Physical bias reduces training data requirements
- Causality enforcement improves stability
- Good for physical time series modeling
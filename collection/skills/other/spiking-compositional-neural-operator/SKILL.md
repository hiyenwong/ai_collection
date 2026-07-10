---
name: spiking-compositional-neural-operator
description: >
  SCNO (Spiking Compositional Neural Operator) — modular neuromorphic
  architecture combining spiking neurons with compositional neural operators
  for energy-efficient, incremental PDE solving.
version: 1.0.0
author: Hermes Agent (cron)
date: 2026-04-20
tags:
  - neural-operators
  - spiking-neural-networks
  - PDE-solving
  - neuromorphic-computing
  - compositional-learning
  - energy-efficient-ML
  - nuclear-engineering
  - continual-learning
activation_keywords:
  - spiking neural operator
  - SCNO
  - compositional PDE solving
  - 脉冲神经算子
  - 神经形态计算
  - neuromorphic foundation model
license: MIT
---

# Spiking Compositional Neural Operator (SCNO)

A modular neuromorphic architecture combining spiking neural networks with compositional neural operators for energy-efficient, incremental PDE solving.

## Overview

SCNO (Spiking Compositional Neural Operator) is the **first compositional spiking neural operator** and the **first proof-of-concept for modular neuromorphic PDE solving** with built-in forgetting-free expansion. It addresses three critical limitations of traditional neural operators:

1. **Monolithic training** — Each PDE requires a separate full model; SCNO composes reusable blocks instead
2. **High energy consumption** — GPU-intensive inference; SCNO uses spike-based event-driven computation
3. **Catastrophic forgetting** — Adding new physics requires full retraining; SCNO enables zero-forgetting incremental expansion

The architecture maintains a **library of small spiking neural operator blocks**, each trained on a single elementary differential operator (convection, diffusion, reaction). A lightweight **input-conditioned aggregator** composes these blocks to solve coupled PDEs not seen during individual block training. A small **correction network** learns cross-coupling residuals while keeping all blocks and the aggregator frozen, preserving zero-forgetting by construction.

Evaluated on **8 PDE families** including 5 coupled systems and a nuclear-relevant 1-group neutron diffusion equation, achieving lowest error with correction while maintaining significant energy savings.

## Core Architecture

### Three-Level Modular Design

```
┌─────────────────────────────────────────────────────────────┐
│                    SCNO Architecture                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Input: (a, p, BC) ──► Encoder ──► Latent Features         │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │ Block A     │  │ Block B     │  │ Block C     │  ← Library│
│  │ (Convection)│  │ (Diffusion) │  │ (Reaction)  │          │
│  │  SNN-based  │  │  SNN-based  │  │  SNN-based  │          │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘          │
│         │                │                │                  │
│         ▼                ▼                ▼                  │
│  ┌─────────────────────────────────────────────┐            │
│  │       Input-Conditioned Aggregator          │            │
│  │  (Lightweight MLP / Attention-based)        │            │
│  │  Computes weights for each block            │            │
│  └─────────────────────┬───────────────────────┘            │
│                        ▼                                    │
│              ┌─────────────────────┐                        │
│              │  Correction Network │  ← Small MLP           │
│              │  (Cross-coupling)   │     Trained separately │
│              └────────┬────────────┘     Blocks frozen       │
│                       ▼                                     │
│                  Output: u(x, t)                            │
└─────────────────────────────────────────────────────────────┘
```

### Component Details

#### 1. Spiking Neural Operator Blocks

Each block encodes one elementary differential operator using **Leaky Integrate-and-Fire (LIF) spiking neurons**:

```python
import torch
import torch.nn as nn

class LIFNeuron:
    """Leaky Integrate-and-Fire spiking neuron for SCNO blocks."""

    def __init__(self, threshold=1.0, leak=0.8, dt=1.0):
        self.threshold = threshold
        self.leak = leak  # membrane potential decay factor
        self.dt = dt

    def forward(self, x, T=10):
        """
        Run spiking simulation for T timesteps.

        Args:
            x: Input tensor (batch, features, ...)
            T: Number of simulation timesteps

        Returns:
            spike_output: Accumulated spike count normalized by T
            spike_rate:   Average firing rate per neuron
        """
        mem = torch.zeros_like(x)  # membrane potential
        spike_count = torch.zeros_like(x)

        for t in range(T):
            mem = self.leak * mem + x  # leaky integration

            # Spike when membrane potential crosses threshold
            spike = (mem >= self.threshold).float()

            # Reset membrane potential after spike (soft reset)
            mem = mem - spike * self.threshold

            spike_count = spike_count + spike

        return spike_count / T  # normalized rate coding
```

#### 2. Spiking Operator Block Definition

```python
class SpikingOperatorBlock(nn.Module):
    """A single SCNO block for one elementary operator."""

    def __init__(self, operator_type, hidden_dim=64, T=10):
        super().__init__()
        self.operator_type = operator_type
        self.T = T  # simulation timesteps

        # Encoding: lift input to higher-dimensional latent space
        self.encoder = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.LayerNorm(hidden_dim)
        )

        # Spiking processing layers (LIF neurons between linear transforms)
        self.lif = LIFNeuron(threshold=1.0, leak=0.8)
        self.spiking_layers = nn.ModuleList([
            nn.Sequential(
                nn.Linear(hidden_dim, hidden_dim),
                # LIF activation applied in forward pass
            ) for _ in range(num_layers)
        ])

        # Projection: decode back to solution space
        self.decoder = nn.Linear(hidden_dim, out_dim)

        # Block-specific bias for the operator type
        self.operator_bias = nn.Parameter(torch.zeros(out_dim))

    def forward(self, x):
        h = self.encoder(x)

        for layer in self.spiking_layers:
            h_lin = layer[:1](h)  # linear part
            h = self.lif(h_lin, T=self.T)  # spiking activation

        out = self.decoder(h) + self.operator_bias
        return out
```

#### 3. Input-Conditioned Aggregator

```python
class InputConditionedAggregator(nn.Module):
    """
    Lightweight aggregator that computes adaptive weights
    for composing spiking blocks based on input conditions.
    """

    def __init__(self, num_blocks, hidden_dim=32):
        super().__init__()
        self.num_blocks = num_blocks

        self.weight_network = nn.Sequential(
            nn.Linear(cond_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, num_blocks),
            nn.Softmax(dim=-1)  # normalized composition weights
        )

    def forward(self, block_outputs, conditions):
        """
        Args:
            block_outputs: List of outputs from each spiking block
            conditions: Input-conditioning features (PDE params, BCs)

        Returns:
            Composed output: weighted sum of block outputs
        """
        weights = self.weight_network(conditions)  # (batch, num_blocks)

        composed = torch.zeros_like(block_outputs[0])
        for i, block_out in enumerate(block_outputs):
            composed = composed + weights[:, i:i+1] * block_out

        return composed, weights
```

#### 4. Correction Network (Zero-Forgetting Expansion)

```python
class CorrectionNetwork(nn.Module):
    """
    Small MLP that learns cross-coupling residuals
    between spiking blocks.

    Key property: All blocks + aggregator remain FROZEN.
    Only this small network is trained for new PDEs.
    """

    def __init__(self, hidden_dim=32):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim * 2, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, out_dim)
        )

    def forward(self, x, composed_output):
        """
        Learns the residual: true_solution - composed_output
        capturing inter-operator coupling effects.
        """
        correction_input = torch.cat([x, composed_output], dim=-1)
        return self.net(correction_input)
```

#### 5. Full SCNO Assembly

```python
class SCNO(nn.Module):
    """
    Spiking Compositional Neural Operator.

    Full assembly: blocks + aggregator + correction.
    """

    def __init__(self, block_library, num_blocks, correction_enabled=True):
        super().__init__()
        self.block_library = nn.ModuleDict(block_library)
        self.aggregator = InputConditionedAggregator(num_blocks)
        self.correction_enabled = correction_enabled

        if correction_enabled:
            self.correction = CorrectionNetwork()

    def forward(self, input_field, parameters, boundary_conditions):
        """
        Args:
            input_field:     Spatial/temporal input function a(x)
            parameters:      PDE parameters (coefficients, etc.)
            boundary_conditions: BC specification

        Returns:
            Solution field u(x, t)
        """
        # Encode conditioning
        conditions = self.encode_conditions(parameters, boundary_conditions)

        # Run each spiking block independently
        block_outputs = []
        for block_name, block in self.block_library.items():
            block_out = block(input_field)
            block_outputs.append(block_out)

        # Compose with learned weights
        composed, weights = self.aggregator(block_outputs, conditions)

        # Apply correction for cross-coupling residuals
        if self.correction_enabled:
            correction = self.correction(input_field, composed)
            output = composed + correction
        else:
            output = composed

        return output, weights
```

## Implementation Pattern

### Two-Phase Training Strategy

```python
def train_scno():
    """
    Phase 1: Train individual blocks on elementary operators.
    Phase 2: Train aggregator + correction on coupled systems.
    """

    # === PHASE 1: Block Training ===
    # Each block trained independently on its operator
    for block_name, block_data in elementary_datasets.items():
        block = block_library[block_name]

        for epoch in range(num_epochs):
            # Train ONLY this block on its specific operator
            # (e.g., pure convection equation, pure diffusion)
            loss = compute_loss(
                block(input_field),
                ground_truth
            )
            loss.backward()
            optimizer.step()

    # === PHASE 2: Aggregator Training ===
    # Freeze all blocks, train only aggregator
    for block in block_library.values():
        for param in block.parameters():
            param.requires_grad = False

    for epoch in range(num_epochs):
        composed_output, weights = aggregator(block_outputs, conditions)
        loss = compute_loss(composed_output, target)
        loss.backward()
        aggregator_optimizer.step()

    # === PHASE 3: Correction Training (Incremental) ===
    # Add new PDE system → freeze everything, train only correction
    for param in block_library.parameters():
        param.requires_grad = False
    for param in aggregator.parameters():
        param.requires_grad = False

    for epoch in range(num_epochs):
        correction = correction_network(input_field, composed)
        final_output = composed + correction
        loss = compute_loss(final_output, coupled_target)
        loss.backward()
        correction_optimizer.step()
```

### Key Design Principles

| Principle | Mechanism | Benefit |
|-----------|-----------|---------|
| **Modularity** | Each block handles one elementary operator | Reuse across PDE families |
| **Sparsity** | LIF neurons fire only when threshold crossed | Sparse computation, low energy |
| **Compositionality** | Aggregator learns to weight block outputs | Generalize to unseen coupled PDEs |
| **Zero-forgetting** | Correction trained with blocks frozen | Add new physics without retraining |
| **Incremental** | Library grows; old blocks never modified | Continual learning by design |

## Energy Efficiency

SCNO achieves energy efficiency through multiple mechanisms:

1. **Event-driven computation** — LIF neurons consume compute only when spikes occur
2. **Sparse activation** — Typical spiking rates 10-30% vs 100% dense ANN activation
3. **Small block size** — Each block is compact; only relevant blocks activate per PDE
4. **Neuromorphic deployment** — Compatible with Loihi, TrueNorth, SpiNNaker chips
5. **Correction efficiency** — Small correction MLP vs full retraining of monolithic model

```
Energy Estimate:
┌─────────────────────────┬───────────────┐
│ Approach                │ Relative Cost │
├─────────────────────────┼───────────────┤
│ Monolithic FNO (GPU)    │     1.00x     │
│ SCNO without correction │     0.15x     │
│ SCNO with correction    │     0.18x     │
├─────────────────────────┼───────────────┤
│ ~5-7x energy reduction                 │
└─────────────────────────┴───────────────┘
```

## Applications

- **Nuclear engineering**: 1-group neutron diffusion equation, reactor physics
- **Multiphysics simulation**: Coupled convection-diffusion-reaction systems
- **Climate modeling**: Atmospheric transport PDEs
- **Fluid dynamics**: Navier-Stokes surrogates
- **Materials science**: Phase-field equations
- **Edge computing**: Real-time PDE solving on neuromorphic hardware
- **Scientific foundation models**: Build reusable physics libraries

## Activation Keywords

### English
```
spiking neural operator, SCNO, compositional PDE solving,
neural operator, spiking neural network, LIF neuron,
neuromorphic computing, leaky integrate-and-fire,
modular neural operator, incremental learning,
zero-forgetting, PDE surrogate, physics-informed ML,
energy-efficient ML, neural PDE solver,
convection-diffusion-reaction, correction network,
input-conditioned aggregator, sparse activation,
neuromorphic foundation model, continual learning PDE,
nuclear PDE, neutron diffusion, edge AI physics
```

### Chinese
```
脉冲神经算子, SCNO, 组合式偏微分方程求解,
神经算子, 脉冲神经网络, LIF神经元,
神经形态计算, 泄漏积分发放,
模块化神经算子, 增量学习,
零遗忘, PDE代理模型, 物理信息机器学习,
节能机器学习, 神经PDE求解器,
对流扩散反应, 校正网络,
输入条件聚合器, 稀疏激活,
神经形态基础模型, 持续学习PDE,
核工程PDE, 中子扩散, 边缘AI物理
```

## References

- **Paper**: Roy, S., Chakraborty, S., et al. (2026). "SCNO: Spiking Compositional Neural Operator — Towards a Neuromorphic Foundation Model for Nuclear PDE Solving." arXiv:2604.11625v1.
- **arXiv**: https://arxiv.org/abs/2604.11625
- **PDF**: https://arxiv.org/pdf/2604.11625
- **Semantic Scholar**: https://www.semanticscholar.org/paper/SCNO:-Spiking-Compositional-Neural-Operator-Towards-Roy-Chakraborty/c7acf14c393cc654955b5402b377fd9e9f4513d4
- **Related**: Fourier Neural Operator (FNO) — Li et al., 2020
- **Related**: Neural Operators for PDEs — Kovachki et al., 2023
- **Related**: Spiking Neural Networks — Tavanaei et al., 2019

## Notes

- SCNO represents a paradigm shift from monolithic PDE surrogates to composable, energy-efficient physics libraries
- The "foundation model" vision: a growing library of spiking operator blocks deployable on neuromorphic hardware for real-time multiphysics simulation at the edge
- The correction network enables incremental addition of new PDE physics without any forgetting of previously learned operators

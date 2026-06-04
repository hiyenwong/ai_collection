---
name: dual-axis-zebrafish-circuits
description: 斑马鱼被盖微电路双轴归因方法论。基于斑马鱼视网膜被盖微电路的双轴功能归因（能量高效信息处理和鲁棒稳定）方法，将生物学电路组织转化为类脑神经网络架构设计。适用于脉冲神经网络、类脑架构设计、电路归因。触发词：dual-axis, 双轴归因, zebrafish tectal, microcircuit attribution, energy efficiency, robustness, ns_TIN, superficial_TIN
---

# Dual-Axis Zebrafish Tectal Microcircuit Attribution Methodology

斑马鱼被盖微电路的双轴功能归因方法，将生物学电路结构转化为类脑神经网络设计模式。

## Source Paper

**Title:** Dual-axis attribution of zebrafish tectal microcircuits for energy-efficient and robust neurocomputing
**arXiv:** 2605.13924
**Date:** 2026-05-15
**Authors:** Ningping Li, Hao Zhang, Yi Zhou
**Category:** cs.NE (Neural and Evolutionary Computing)
**URL:** https://arxiv.org/abs/2605.13924

## Core Concept

生物神经网络包含支持不同计算功能的特化子结构，但许多类脑神经网络借用生物基序而不识别其电路级起源。本方法提出沿两个计算轴对斑马鱼被盖微电路进行功能归因：

1. **Energy-Efficient Information Processing（能量高效信息处理）**
2. **Robustness-Preserving Stabilization（鲁棒保存稳定）**

## Key Innovations

### 1. Directed Retinotectal Microcircuit Graph Reconstruction

- 从斑马鱼视网膜被盖系统重建有向微电路图
- 通过动态仿真验证视网膜被盖信号传播
- 建立从生物结构到计算图的映射

### 2. Dual-Axis Attribution Framework

通过 LIF (Leaky Integrate-and-Fire) 脉冲神经网络作为非线性扰动测试台：

#### Energy Sensitivity Index (ESI)

$$ESI_i = \frac{|E_{baseline} - E_{ablated}|}{E_{baseline}}$$

- 测量子电路 $i$ 被消融后的能量敏感性
- 低 ESI 但显著影响预测误差 → 能量高效信息门

#### Robustness Sensitivity Index (RSI)

$$RSI_i = \frac{|R_{baseline} - R_{ablated}|}{R_{baseline}}$$

- 测量子电路 $i$ 被消融后的鲁棒性敏感性
- 高 RSI → 反馈式系统稳定性维护

### 3. Functional Dissociation Findings

| Subcircuit | Spike Footprint | Sensitivity | Role |
|------------|----------------|-------------|------|
| **ns_TIN** | Low | Prediction error (ESI) | Spike-efficient internal information gate |
| **superficial_TIN** | Higher | System robustness (RSI) | Feedback-like stability maintenance |

### 4. Transfer to Artificial Neural Networks

将归因功能转移到 ResNet18 架构中：

- **ns_TIN-inspired module:** 在推理预算缩减下提升性能保持
- **superficial_TIN-inspired module:** 在输入噪声下提升鲁棒性

## Methodology Steps

### Step 1: Microcircuit Reconstruction

```python
import networkx as nx

def build_retinotectal_graph():
    """Construct directed microcircuit graph from zebrafish tectal connectivity."""
    G = nx.DiGraph()
    
    # Add nodes (cell types)
    G.add_nodes_from([
        'RGC',           # Retinal Ganglion Cells
        'ns_TIN',        # Non-superficial Tectal Interneurons  
        'superficial_TIN', # Superficial Tectal Interneurons
        'TPC',           # Tectal Projection Cells
        'Pyr',           # Pyramidal neurons
    ])
    
    # Add edges (known connectivity)
    G.add_edges_from([
        ('RGC', 'ns_TIN'),
        ('RGC', 'superficial_TIN'),
        ('ns_TIN', 'TPC'),
        ('superficial_TIN', 'TPC'),
        ('superficial_TIN', 'ns_TIN'),  # lateral connection
    ])
    
    return G
```

### Step 2: LIF-SNN Ablation Testing

```python
def ablation_test(G, target_subcircuit, model):
    """Selectively ablate a subcircuit and measure sensitivity."""
    
    # Baseline performance
    baseline_pred = model.predict(G)
    baseline_energy = compute_spike_footprint(model)
    baseline_robust = evaluate_robustness(model, noise_level=0.1)
    
    # Ablated performance
    G_ablated = G.copy()
    G_ablated.remove_nodes_from(target_subcircuit)
    ablated_pred = model.predict(G_ablated)
    ablated_energy = compute_spike_footprint(model)
    ablated_robust = evaluate_robustness(model, noise_level=0.1)
    
    # Compute indices
    ESI = abs(baseline_energy - ablated_energy) / baseline_energy
    RSI = abs(baseline_robust - ablated_robust) / baseline_robust
    
    return {'ESI': ESI, 'RSI': RSI}
```

### Step 3: Functional Transfer

```python
class DualAxisModule(nn.Module):
    """Dual-axis inspired neural architecture module."""
    
    def __init__(self, in_channels, out_channels, mode='energy'):
        super().__init__()
        self.mode = mode
        
        if mode == 'energy':  # ns_TIN-inspired
            # Lightweight gating for efficient computation
            self.gate = nn.Sequential(
                nn.Linear(in_channels, in_channels // 4),
                nn.ReLU(),
                nn.Linear(in_channels // 4, in_channels),
                nn.Sigmoid()
            )
        elif mode == 'robustness':  # superficial_TIN-inspired
            # Feedback stabilization module
            self.stabilizer = nn.Sequential(
                nn.LayerNorm(in_channels),
                nn.Linear(in_channels, in_channels),
                nn.GELU(),
                nn.Dropout(0.1),
            )
    
    def forward(self, x):
        if self.mode == 'energy':
            # Sparse gating for energy efficiency
            gate = self.gate(x.mean(dim=-1))
            return x * gate.unsqueeze(-1)
        else:
            # Stabilization feedback
            return self.stabilizer(x) + x
```

## Design Patterns

### Pattern 1: Energy-Efficient Information Gate (ns_TIN)

```
Input → [Lightweight Gate] → Sparse Activation → Output
              ↓
         Computation Budget
         Reduction Module
```

**Use when:** Need to reduce computation while preserving key information flow

### Pattern 2: Robustness Stabilizer (superficial_TIN)

```
Input → [Normalization] → [Feedback Path] → [+ Residual] → Output
              ↓                ↓
         Stabilizer       Robustness
         Module           Enhancement
```

**Use when:** Need to improve robustness against noise/perturbations

## Application Guidelines

1. **Architecture Design:** Use dual-axis modules in hybrid networks
   - Front layers: ns_TIN for efficient early processing
   - Deep layers: superficial_TIN for robust feature stabilization

2. **Resource-Constrained Deployment:** ns_TIN-inspired gating for edge deployment

3. **Safety-Critical Systems:** superficial_TIN-inspired stabilization for robust operation

## Verification

- Test ESI/RSI tradeoff on target architecture
- Validate on CIFAR-10 with budget reduction and noise corruption
- Compare spike footprint vs. accuracy preservation
- Measure robustness improvement under adversarial conditions

## Related Skills

- `spiking-neural-network-analysis`
- `brain-inspired-snn-pattern-analysis`
- `brain-inspired-intelligence-paradigm`
- `energy-regularized-neural-mpc`

## Activation Keywords

- dual-axis attribution
- 双轴归因
- zebrafish tectal microcircuit
- microcircuit attribution
- energy efficient neurocomputing
- robustness-preserving stabilization
- ns_TIN
- superficial_TIN
- retinotectal circuit
- biological circuit transfer
- LIF-SNN ablation
- circuit-level bio-inspiration

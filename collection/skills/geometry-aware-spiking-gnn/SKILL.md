---
name: geometry-aware-spiking-gnn
description: Geometry-Aware Spiking Graph Neural Network combining SNN energy efficiency with Riemannian manifold learning for non-Euclidean graph structures
---

# Geometry-Aware Spiking Graph Neural Network

**Source:** arXiv:2508.06793v2 (August 2025)
**Utility:** 0.89
**Authors:** Bowen Zhang

---

## Description

This skill implements GSG (Geometry-Aware Spiking Graph Neural Network) - a
novel architecture that unifies spike-based neural dynamics with adaptive
representation learning on Riemannian manifolds. Overcomes limitations of
Euclidean spiking GNNs by modeling hierarchies and cycles in curved spaces.

**Core Components:**
1. **Riemannian Embedding Layer** - Projects nodes into constant-curvature manifolds
2. **Manifold Spiking Layer** - Membrane potential evolution in curved spaces
3. **Manifold Learning Objective** - Instance-wise geometry adaptation

---

## Tools Used

- `pytorch` - Deep learning framework
- `torch_geometric` - Graph neural networks
- `spikingjelly` - Spiking neural network toolkit
- `geoopt` - Riemannian optimization
- `networkx` - Graph data structures

---

## Instructions for Agents

1. **Prepare graph data** - Node features and edge structure
2. **Riemannian embedding** - Project to constant-curvature manifolds
3. **Manifold spiking** - Model membrane potential in curved space
4. **Geometry-consistent aggregation** - Neighbor aggregation on manifold
5. **Curvature-based attention** - Adaptive message passing
6. **Joint optimization** - Classification + link prediction losses
7. **Riemannian SGD training** - No backpropagation through time

---

## Examples

### Example 1: Hierarchical Graph Learning

**User:** 如何用 GSG 学习层次图结构？

**Agent:** GSG 方法：

1. **黎曼嵌入** - 将节点投影到负曲率流形（双曲空间）
2. **流形脉冲** - 在弯曲空间建模膜电位演化
3. **几何一致聚合** - 沿测地线聚合邻居信息
4. **曲率注意力** - 自适应曲率的消息传递

**优势：** 捕获层次结构，比欧几里得 GNN 更高效

### Example 2: Energy-Efficient Graph Learning

**User:** 如何实现高能效的图学习？

**Agent:** GSG 能效特性：

| 特性 | 说明 |
|------|------|
| 脉冲计算 | 稀疏、事件驱动 |
| 黎曼优化 | Riemannian SGD，无需 BPTT |
| 几何适应 | 实例级曲率自适应 |
| 能效 | 优于欧几里得 SNN 和流形 GNN |

---

## Activation Keywords

- 几何感知脉冲 GNN、geometry-aware spiking GNN
- 黎曼流形学习、Riemannian manifold learning
- 脉冲图神经网络、spiking graph neural network
- 曲率自适应、curvature-aware
- 测地线距离、geodesic distance
- 常曲率流形、constant-curvature manifold

---

## Key Concepts

### 1. Riemannian Embedding Layer

**Purpose:** Project node features into pool of constant-curvature manifolds

**Manifold types:**
- Hyperbolic (negative curvature) - Hierarchies
- Spherical (positive curvature) - Cycles
- Euclidean (zero curvature) - Standard graphs

### 2. Manifold Spiking Layer

**Mechanism:**
- Membrane potential evolution in curved space
- Geometry-consistent neighbor aggregation
- Curvature-based attention weights

**Formula:**
```
Spiking on manifold: u(t+1) = f(u(t), messages, curvature)
```

### 3. Manifold Learning Objective

**Joint optimization:**
- Classification loss (geodesic-based)
- Link prediction loss (geodesic distance)
- Instance-wise geometry adaptation

### 4. Riemannian SGD

**Advantage:** No backpropagation through time (BPTT)

**Training:** Direct optimization on manifold

---

## Architecture

```
Graph Input → Riemannian Embedding Layer
    ↓
Manifold Spiking Layer (curved space dynamics)
    ↓
Geometry-Consistent Aggregation + Curvature Attention
    ↓
Manifold Learning Objective (classification + link prediction)
    ↓
Riemannian SGD Optimization
```

---

## Results (Paper)

| Metric | Performance |
|--------|-------------|
| Accuracy | Superior vs Euclidean SNNs ✅ |
| Robustness | Superior vs manifold GNNs ✅ |
| Energy efficiency | Best in class ✅ |
| Hierarchy modeling | Captured via hyperbolic ✅ |
| Cycle modeling | Captured via spherical ✅ |

---

## When to Use

1. **Hierarchical graphs** - Trees, taxonomies, social networks
2. **Cyclic graphs** - Molecular structures, ring patterns
3. **Energy-efficient learning** - Edge deployment
4. **Non-Euclidean structures** - Complex geometries
5. **Graph classification** - Node and edge prediction

---

## Advantages over Prior Methods

| Euclidean SNNs | Manifold GNNs | GSG (This) |
|----------------|---------------|-----------|
| Fixed geometry | No spiking | ✅ Unified approach |
| Limited expressiveness | High energy | ✅ Energy efficient |
| No curvature adaptation | Static manifolds | ✅ Adaptive geometry |

---

## Limitations

1. Computational cost of Riemannian operations
2. Curvature selection requires tuning
3. Limited to constant-curvature manifolds
4. Training stability on complex manifolds

---

## Related Skills

- `spikingjelly-framework` - SNN toolkit
- `geometry-aware-spiking-gnn` - Related architecture
- `hyperbolic-brain-network-neurodegeneration` - Hyperbolic networks
- `graph-laplacian-denoising` - Graph signal processing
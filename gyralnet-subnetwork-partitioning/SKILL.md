---
name: gyralnet-subnetwork-partitioning
description: GyralNet Subnetwork Partitioning
---

# GyralNet Subnetwork Partitioning

**Source:** arXiv:2503.19823v2 (March 2025)
**Utility:** 0.90
**Authors:** Yan Zhuang

---

## Description

This skill implements a differentiable subnetwork partitioning framework for
GyralNet - a network representation of cortical folding patterns. Using spectral
modularity maximization, it modularizes three-hinge gyri (3HGs) while preserving
cross-subject community consistency.

**Core Method:**
1. **GyralNet Modeling** - 3HGs as nodes, gyral crests as edges
2. **Spectral Modularity Optimization** - Differentiable partitioning
3. **Attribute Features** - Topological similarity + DTI connectivity
4. **Cross-subject Consistency** - Community-level correspondence

---

## Tools Used

- `structural_mri` - Cortical folding data
- `dti_connectivity` - Diffusion tensor imaging
- `spectral_clustering` - Modularity maximization
- `gyralnet_graph` - Network representation
- `hcp_dataset` - Human Connectome Project data

---

## Instructions for Agents

1. **Extract cortical folding** - Identify 3HGs from structural MRI
2. **Build GyralNet** - Nodes = 3HGs, edges = gyral crests
3. **Compute attributes** - Topological similarity + DTI patterns
4. **Spectral optimization** - Differentiable modularity maximization
5. **Partition GyralNet** - Assign 3HGs to subnetworks
6. **Validate consistency** - Cross-subject community correspondence
7. **Analyze connectivity** - Study cortico-cortical hubs

---

## Examples

### Example 1: Cortical Folding Analysis

**User:** 如何分析脑回折叠模式？

**Agent:** GyralNet 分区流程：

1. **识别三折点脑回 (3HG)** - 关键结构地标
2. **构建 GyralNet 网络**
   - 节点 = 3HG
   - 边 = 脑回脊
3. **计算属性特征**
   - 拓扑结构相似性
   - DTI 连接模式
4. **谱模块优化** - 可微分分区
5. **验证一致性** - 跨受试者社区对应

**优势：** 生物有意义 + 跨受试者一致

### Example 2: Hub Connectivity Study

**User:** 3HG 在脑连接中有什么作用？

**Agent:** 3HG 作为皮质连接关键枢纽：

| 特性 | 描述 |
|------|------|
| 结构角色 | 三折点脑回 = 连接枢纽 |
| 网络位置 | GyralNet 核心节点 |
| DTI 模式 | 高白质连接密度 |
| 功能意义 | 皮质-皮质连接关键点 |

**研究价值：** 理解脑组织结构-功能关系

---

## Activation Keywords

- GyralNet、gyral network
- 三折点脑回、three-hinge gyrus、3HG
- 子网络分区、subnetwork partitioning
- 谱模块优化、spectral modularity optimization
- 脑回折叠、cortical folding
- HCP、Human Connectome Project

---

## Key Concepts

### 1. Three-Hinge Gyrus (3HG)

**Definition:** Structural landmark where three gyral crests meet

**Properties:**
- Sub-voxel scale at typical neuroimaging resolutions
- Key hub in cortico-cortical connectivity
- Community-level relationships important

### 2. GyralNet Representation

```
GyralNet = {
  Nodes: Three-Hinge Gyri (3HGs)
  Edges: Gyral Crests
}
```

**Model:** Network representation of cortical folding patterns

### 3. Spectral Modularity Maximization

**Objective:** Maximize modularity Q for optimal partitioning

```
Q = 1/(2m) * Σ_ij [A_ij - k_i*k_j/(2m)] * δ(c_i, c_j)
```

**Differentiable:** Allows gradient-based optimization

### 4. Attribute Features

| Feature Type | Description |
|--------------|-------------|
| Topological similarity | Structural pattern matching |
| DTI connectivity | White matter connection patterns |
| Combined | Biologically meaningful representation |

---

## Architecture

```
Structural MRI → 3HG Extraction → GyralNet Construction
    ↓
DTI → Connectivity Patterns → Attribute Features
    ↓
Spectral Modularity Optimization → Differentiable Partitioning
    ↓
GyralNet Subnetworks → Cross-subject Consistency Validation
```

---

## Results (Paper)

| Metric | HCP Dataset |
|--------|-------------|
| Partitioning | Individual-level ✅ |
| Cross-subject consistency | Community-level ✅ |
| Biological meaning | Preserved ✅ |
| Robustness | Strong foundation for connectivity analysis |

---

## When to Use

1. **Cortical folding analysis** - Study gyral patterns
2. **Brain connectivity research** - Hub identification
3. **Cross-subject correspondence** - Establish alignment
4. **Structural-functional coupling** - Organization analysis
5. **HCP data analysis** - Human Connectome Project studies

---

## Advantages over Traditional Methods

| Traditional | This Method |
|------------|-------------|
| Sub-voxel scale challenge | ✅ Handles 3HG scale |
| Computational complexity | ✅ Differentiable optimization |
| Independent node treatment | ✅ Community relationships |
| No correspondence | ✅ Cross-subject consistency |

---

## Limitations

1. Requires high-resolution structural MRI
2. DTI quality affects connectivity features
3. Modularity optimization may have local minima
4. Cross-subject validation needs sufficient samples

---

## Related Skills

- `brain-higher-order-structures` - Higher-order brain analysis
- `mesoscale-brain-organization` - Mesoscale organization
- `linear-structure-function-coupling` - Structure-function coupling
- `dcho-higher-order-brain-connectivity` - Higher-order connectivity
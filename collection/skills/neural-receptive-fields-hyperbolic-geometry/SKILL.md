# Neural Receptive Fields via Hyperbolic Geometry

**Source:** arXiv:2509.25453v2 (January 2026)
**Utility:** 0.90
**Authors:** Yuri A. Dabaghian

---

## Description

This skill implements a physiologically grounded framework where neural receptive
fields arise naturally from the effective hyperbolic geometry of scale-free
networks - **without synaptic fine-tuning**. By embedding stimulus space at the
boundary of hyperbolic geometry, localized activity patterns reflect stimulus
structure.

**Core Insight:** Receptive field size depends on neuron's connectivity degree,
following experimentally observed statistics. Generalizes across modalities
(orientation, place selectivity).

---

## Tools Used

- `scale_free_network` - Network structure modeling
- `hyperbolic_embedding` - Geometric representation
- `rate_based_model` - Neural dynamics simulation
- `spiking_model` - Spiking neuron dynamics
- `stimulus_space` - Boundary embedding
- `place_field_data` - Hippocampal recordings

---

## Instructions for Agents

1. **Construct scale-free network** - Connectivity structure
2. **Hyperbolic embedding** - Embed network in hyperbolic space
3. **Associate stimulus space** - Map to hyperbolic boundary
4. **Simulate neural dynamics** - Rate-based or spiking models
5. **Observe receptive fields** - Localized activity patterns
6. **Validate statistics** - Compare with experimental data
7. **Analyze degree-dependence** - RF size vs connectivity degree

---

## Examples

### Example 1: Orientation Selectivity

**User:** 如何理解方向选择性感受野的形成？

**Agent:** 双曲几何框架：

1. **网络结构** - 无标度网络
2. **双曲嵌入** - 有效几何表示
3. **刺激空间** - 方向空间映射到边界
4. **神经动力学** - 模拟产生局部活动
5. **感受野** - 自然形成方向选择性

**优势：** 无需精细调整突触连接！

### Example 2: Place Fields (Hippocampus)

**User:** 海马位置场如何从网络几何产生？

**Agent:** 实验验证支持：

| 发现 | 描述 |
|------|------|
| 感受野大小 | 依赖神经元连接度 |
| 统计特性 | 符合实验观察 |
| 线性轨道 | 海马位置场验证 |
| 模态推广 | 方向 + 位置选择性 |

**核心原理：** 刺激空间边界 → 局部活动模式 → 感受野形成

---

## Activation Keywords

- 感受野、receptive field
- 双曲几何、hyperbolic geometry
- 无标度网络、scale-free network
- 刺激空间嵌入、stimulus space embedding
- 方向选择性、orientation selectivity
- 位置场、place field、hippocampal

---

## Key Concepts

### 1. Scale-Free Network Geometry

**Structure:** Power-law degree distribution

**Effective geometry:** Hyperbolic space naturally represents scale-free
networks

**Key property:** High-degree neurons → smaller receptive fields

### 2. Hyperbolic Embedding

**Purpose:** Map network to hyperbolic space

**Stimulus space:** Associated with hyperbolic boundary

**Result:** Localized activity patterns reflect stimulus structure

### 3. Receptive Field Statistics

| Property | Observation |
|----------|-------------|
| Size vs degree | Degree-dependent (high degree = small RF) |
| Statistics | Match experimental data |
| Modality | Orientation, place selectivity |
| Fine-tuning | **Not required** |

### 4. Organizing Principle

```
Scale-Free Network → Hyperbolic Geometry
    ↓
Stimulus Space Boundary → Neural Dynamics
    ↓
Localized Activity → Receptive Fields
```

**Novel insight:** Network structure → Stimulus encoding → Neural dynamics
linkage without fine-tuning

---

## Architecture

```
Scale-Free Network → Hyperbolic Embedding
    ↓
Stimulus Space (Boundary)
    ↓
Neural Dynamics (Rate/Spiking) → Receptive Fields
    ↓
Experimental Validation (Place Fields)
```

---

## Results (Paper)

| Metric | Result |
|--------|--------|
| RF formation | Natural emergence ✅ |
| Synaptic fine-tuning | **Not required** ✅ |
| RF statistics | Match experiments ✅ |
| Degree-dependence | Validated ✅ |
| Modality generalization | Orientation + Place ✅ |
| Hippocampal validation | Linear track place fields ✅ |

---

## When to Use

1. **Receptive field modeling** - RF formation without fine-tuning
2. **Network-encoding coupling** - Structure-function relationship
3. **Hippocampal place fields** - Spatial navigation research
4. **Orientation selectivity** - Visual cortex modeling
5. **Scale-free network analysis** - Brain network geometry

---

## Advantages over Fine-Tuning Approach

| Fine-Tuning | This Framework |
|-------------|---------------|
| Synaptic adjustment required | ✅ No fine-tuning |
| Limited biological plausibility | ✅ Physiologically grounded |
| RF statistics artificial | ✅ Match experiments |
| Single modality | ✅ Generalizes across modalities |

---

## Biological Plausibility

**Why no fine-tuning needed?**

1. **Effective geometry** - Hyperbolic structure inherent in scale-free
   networks
2. **Stimulus boundary** - Natural encoding at hyperbolic boundary
3. **Degree-dependence** - Connectivity determines RF properties
4. **Population attractors** - Dynamics arise from geometry

---

## Limitations

1. Assumes scale-free network structure
2. Hyperbolic embedding computational complexity
3. Validation limited to hippocampal place fields
4. Extension to other brain areas needs testing

---

## Related Skills

- `brain-network-joint-embedding` - Network embedding methods
- `hyperbolic-brain-network-neurodegeneration` - Hyperbolic brain networks
- `mesoscale-brain-organization` - Brain organization principles
- `neutral-theory-neural-dynamics` - Neural dynamics theory
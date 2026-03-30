---
name: tensor-decomposition-brain-states
description: Tensor Decomposition for Dynamic Brain Network States
---

# Tensor Decomposition for Dynamic Brain Network States

**Source:** arXiv:1410.0446v1 (October 2014)
**Utility:** 0.89
**Authors:** Arash Mahyari

---

## Description

This skill implements a tensor decomposition method to identify temporally
invariant 'network states' in dynamic functional brain networks. Applied to
EEG data during error-related negativity (ERN) study, it finds common
topographic representations for each quasi-stationary state.

**Core Method:**
1. **Dynamic connectivity tensor** - Time-varying brain networks
2. **Tensor decomposition (Tucker/CP)** - Identify network states
3. **State identification** - Quasi-stationary intervals
4. **Topographic representation** - Common patterns per state

---

## Tools Used

- `eeg_data` - Electroencephalogram recordings
- `functional_connectivity` - Dynamic network computation
- `tensor_decomposition` - Tucker/Canonical Polyadic decomposition
- `network_states` - Quasi-stationary intervals
- `graph_theory` - Network analysis indices

---

## Instructions for Agents

1. **Collect EEG/fMRI data** - Time-series neural recordings
2. **Compute dynamic connectivity** - Sliding window correlation
3. **Construct connectivity tensor** - Time × Region × Region
4. **Apply tensor decomposition** - Tucker or CP decomposition
5. **Identify network states** - Temporally invariant patterns
6. **Extract topographic maps** - Common representation per state
7. **Analyze state transitions** - Quasi-stationary intervals

---

## Examples

### Example 1: EEG Error-Related Negativity (ERN)

**User:** 如何用张量分解识别 ERN 脑网络状态？

**Agent:** 张量分解流程：

1. **收集 EEG 数据** - 错误相关负波实验
2. **动态连接计算** - 滑动窗口相关性
3. **构建张量** - 时间 × 区域 × 区域
4. **张量分解** - Tucker/CP 分解
5. **网络状态识别** - 时间不变模式
6. **地形图提取** - 每状态共同表示

**优势：** 识别准稳态间隔 + 共同拓扑表示

### Example 2: fMRI Dynamic States

**User:** 能否应用于 fMRI 动态脑网络？

**Agent:** 可以！扩展应用：

| 数据类型 | 应用 |
|---------|------|
| EEG | ERN 研究 |
| fMRI | 休息态网络状态 |
| MEG | 认知任务动态 |

**关键洞察：** 功能连接是动态过程，网络重组是认知理解关键

---

## Activation Keywords

- 张量分解、tensor decomposition
- 动态脑网络、dynamic brain network
- 网络状态、network states
- 准稳态、quasi-stationary
- ERN、error-related negativity
- 地形图表示、topographic representation
- Tucker 分解、CP 分解

---

## Key Concepts

### 1. Dynamic Connectivity Tensor

**Structure:**
```
Tensor T ∈ ℝ^(Time × Region × Region)
T[t, i, j] = connectivity between regions i, j at time t
```

**Dynamic process:** Functional connectivity changes over time

### 2. Tensor Decomposition Methods

| Method | Description |
|--------|-------------|
| Tucker | Multi-way decomposition with core tensor |
| CP (Canonical Polyadic) | Sum of rank-1 tensors |

**Purpose:** Extract temporally invariant network states

### 3. Network States

**Definition:** Temporally invariant connectivity patterns

**Properties:**
- Quasi-stationary intervals
- Common topographic representation
- Reorganization across states

### 4. Quasi-Stationary Intervals

**Key insight:** Brain networks are not static but have quasi-stationary periods

**Detection:** Tensor decomposition identifies these intervals

---

## Architecture

```
EEG/fMRI Data → Dynamic Connectivity Computation
    ↓
Connectivity Tensor (Time × Region × Region)
    ↓
Tensor Decomposition (Tucker/CP)
    ↓
Network States Identification → Topographic Maps
    ↓
State Transition Analysis → Cognitive Understanding
```

---

## Results (Paper)

| Application | ERN EEG Study |
|-------------|---------------|
| Method | Tensor decomposition ✅ |
| Network states | Identified ✅ |
| Topographic maps | Extracted ✅ |
| Quasi-stationary intervals | Detected ✅ |

---

## When to Use

1. **Dynamic brain network analysis** - Time-varying connectivity
2. **Network state identification** - Quasi-stationary patterns
3. **Cognitive process tracking** - State transitions
4. **EEG/fMRI/MEG analysis** - Multi-modal neural data
5. **Error-related negativity studies** - ERN experiments

---

## Advantages over Static Analysis

| Static Networks | Tensor Decomposition |
|-----------------|---------------------|
| Long-time averages | ✅ Dynamic tracking |
| No temporal info | ✅ Quasi-stationary states |
| Single connectivity | ✅ Multiple states |
| No reorganization | ✅ State transitions |

---

## Theoretical Background

**Complex network theory:**
- Graph theoretic indices for brain networks
- Static averages miss dynamics

**Dynamic networks:**
- Functional connectivity is dynamic process
- Network construction and reorganization key to cognition

**Tensor decomposition:**
- Mathematical tool for multi-way data
- Identifies invariant patterns across dimensions

---

## Limitations

1. Sliding window size affects connectivity estimation
2. Tensor rank selection needs validation
3. EEG spatial resolution limited
4. State interpretation requires domain expertise
5. Temporal resolution trade-offs

---

## Related Skills

- `time-varying-brain-connectivity` - Dynamic connectivity methods
- `discrete-heat-kernels-simplicial` - Simplicial complex analysis
- `brain-graph-augmentation-template` - Graph augmentation
- `eeg-brain-connectivity-bci` - EEG connectivity BCI
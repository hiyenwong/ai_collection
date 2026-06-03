---
name: reshaping-neural-representation-presynaptic-plasticity
description: Associative presynaptic short-term plasticity via information-theoretic learning rules maximizing stimulus information under resource constraints
---

# Reshaping Neural Representation via Associative Presynaptic STP

**Source:** arXiv:2601.10397v2 (January 2026)
**Utility:** 0.89
**Authors:** Genki Shimizu

---

## Description

This skill implements associative presynaptic short-term plasticity (STP) using
normative information-theoretic theory. Derives learning rules for baseline
weight and release probability that maximize stimulus information under resource
constraints, extending Fisher-information-based learning to Tsodyks-Markram
synapses.

**Core Innovation:**
- **Associative STP** - Depends on pre- and postsynaptic coactivation
- **Information-theoretic** - Maximizes stimulus information
- **Phase-advanced detection** - Selectively detects stimulus onset
- **Temporal reconfiguration** - Rapidly reconfigurable temporal coding

---

## Tools Used

- `numpy` - Numerical computing
- `scipy` - Optimization and analysis
- `matplotlib` - Visualization
- `neuron_simulator` - Neural dynamics simulation

---

## Instructions for Agents

1. **Define Tsodyks-Markram synapse** - STP model parameters
2. **Compute Fisher information** - Stimulus information metric
3. **Derive learning rules** - Maximize information under constraints
4. **Implement associative STP** - Pre- and postsynaptic coactivation
5. **Analyze phase selectivity** - Frequency-dependent properties
6. **Study temporal asymmetry** - Release-probability tuning

---

## Examples

### Example 1: Stimulus Onset Detection

**User:** 如何用联想性 STP 检测刺激起始？

**Agent:** 方法流程：

1. **突触模型** - Tsodyks-Markram STP
2. **学习规则** - 最大化 Fisher 信息
3. **相位超前项** - 突触前检测刺激起始
4. **联想性** - 依赖前后突触共激活

**优势：** 选择性检测刺激起始，快速时间编码

### Example 2: Temporal Coding Reconfiguration

**User：** 释放概率可塑性如何支持时间编码？

**Agent：** 关键机制：

- **频率依赖相位选择性** - STP 产生相位调谐
- **时间不对称性** - 释放概率约束调节
- **反因果连接** - 慢变输入下的偏好
- **逆向重放** - 驱动移除后的响应

---

## Activation Keywords

- 联想性突触前可塑性、associative presynaptic plasticity
- 短时程可塑性、short-term plasticity STP
- Fisher 信息学习、Fisher information learning
- Tsodyks-Markram 突触、Tsodyks-Markram synapse
- 释放概率可塑性、release probability plasticity
- 时间编码重构、temporal coding reconfiguration

---

## Key Concepts

### 1. Associative STP

**Traditional view:** STP as presynaptic filter, independent of postsynaptic

**This work:** STP depends on pre- and postsynaptic coactivation

**Significance:** More flexible and adaptive synaptic dynamics

### 2. Information-Theoretic Learning

**Objective:** Maximize stimulus information under resource constraints

**Method:** Fisher-information-based learning

**Constraints:** Resource limitations on release probability

### 3. Learning Rules

**Baseline weight:** Postsynaptic term tracking local firing

**Release probability:** Presynaptic phase-advanced term

**Result:** Selective stimulus onset detection

### 4. Temporal Coding Properties

| Property | Mechanism |
|----------|-----------|
| Onset sensitivity | Phase-advanced presynaptic term |
| Anti-causal connectivity | Slowly varying inputs |
| Response offset | Enhanced during drive |
| Reverse replay | After drive removal |

---

## Mathematical Framework

### Fisher Information Maximization

```
Maximize: I(θ; r) = E[(∂/∂θ log p(r|θ))²]
Subject to: Resource constraints on release probability
```

### Learning Rules

**Baseline weight update:**
```
Δw ∝ ∂I/∂w + postsynaptic activity term
```

**Release probability update:**
```
ΔU ∝ ∂I/∂U + presynaptic phase-advanced term
```

---

## Results (Paper)

| Finding | Result |
|---------|--------|
| Associative STP | Depends on coactivation ✅ |
| Onset detection | Phase-advanced presynaptic term ✅ |
| Anti-causal bias | For slowly varying inputs ✅ |
| Frequency selectivity | STP yields phase selectivity ✅ |
| Temporal asymmetry | Tuned by release-probability constraints ✅ |

---

## When to Use

1. **Temporal coding** - Rapidly reconfigurable time coding
2. **Stimulus onset detection** - Selective detection mechanisms
3. **Synaptic plasticity modeling** - Beyond traditional STP
4. **Information maximization** - Normative synaptic learning
5. **Recurrent circuit dynamics** - Response offset and replay

---

## Advantages over Traditional STP

| Traditional STP | Associative STP |
|-----------------|-----------------|
| Presynaptic only | ✅ Pre- and postsynaptic dependent |
| Fixed filter | ✅ Adaptive and flexible |
| No onset selectivity | ✅ Phase-advanced onset detection |
| Limited temporal coding | ✅ Rapidly reconfigurable |

---

## Limitations

1. Requires Tsodyks-Markram model parameters
2. Fisher information computation is complex
3. Resource constraints need careful tuning
4. Limited to specific synapse types

---

## Related Skills

- `tsodyks-markram-chaotic-dynamics` - Tsodyks-Markram model
- `neuromodulated-synaptic-plasticity` - Synaptic plasticity
- `stochastic-synaptic-plasticity` - Stochastic plasticity
- `multi-plasticity-snn-training` - Multiple plasticity mechanisms
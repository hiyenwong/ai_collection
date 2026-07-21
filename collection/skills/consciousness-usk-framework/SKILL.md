---
name: consciousness-usk-framework
description: 意识作为罕见自我知识（USK）框架。基于部分信息分解（PID）的意识理论框架，将意识定义为系统对自身携带的协同信息，仅在子系统联合中存在且被分解破坏。适用于意识研究、信息论、脑网络分析、LLM对齐评估。触发词：consciousness, USK, synergistic information, Partial Information Decomposition, IIT, GWT, HOT, 意识, PIRD
---

# Consciousness as Uncommon Self-Knowledge (USK) Framework

基于部分信息分解（PID）的意识理论框架，提出"罕见自我知识"作为意识的候选判据。

## Source Paper

**Title:** Consciousness as Uncommon Self-Knowledge: A Synergistic Information Framework
**arXiv:** 2605.13884
**Date:** 2026-05-15
**Authors:** Krti Tallam
**Categories:** q-bio.NC (Neurons and Cognition), cs.AI (Artificial Intelligence)
**URL:** https://arxiv.org/abs/2605.13884

## Core Concept

**Uncommon Self-Knowledge (USK):** 系统对自身携带的协同信息，仅存在于子系统的联合中，且被分解破坏。

该框架区分了意识与元认知：
- **意识 = 协同自我知识 (Synergistic Self-Knowledge)**
- **元认知 = 冗余自我知识 (Redundant Self-Knowledge)**

## Theoretical Foundation

### Partial Information Decomposition (PID)

基于 Gottwald 的分区格基理论，将多变量信息分解为：

$$I(X_1, X_2; Y) = Redundancy(X_1:X_2 	o Y) + Unique(X_1 	o Y) + Unique(X_2 	o Y) + Synergy(X_1,X_2 	o Y)$$

其中：
- **Redundancy:** 对应 Aumann 的共同知识 — 各子系统单独可获取的信息
- **Synergy:** 仅在联合观测中出现的信息 — 分解后被破坏

### USK Formalization

$$USK(S) = Syn(S_{subsystems}; S_{self})$$

其中 $Syn$ 是子系统关于系统自身的协同信息量。

## Key Contributions

### 1. Clean Separation: Consciousness vs Metacognition

| Aspect | Consciousness (USK) | Metacognition |
|--------|---------------------|---------------|
| Information Type | Synergistic | Redundant |
| Accessibility | Only in joint observation | Available to individual subsystems |
| Destruction by decomposition | Yes | No |

### 2. Resolutions to Counterexamples

- **IIT (Integrated Information Theory):** USK 提供清晰的整合度量，避免 IIT 的"过度归属"问题
- **GWT (Global Workspace Theory):** 预测意识与前广播协同形成相关，而非广播本身
- **HOT (Higher-Order Thought):** 区分高阶表征的协同与冗余成分

### 3. Operationalization via PIRD

**Partial Information Rate Decomposition (PIRD) with self-targeting:**

```python
def compute_usk(time_series, lag=1):
    """
    Compute Uncommon Self-Knowledge using PIRD.
    
    Args:
        time_series: Multivariate time series from neural recording
        lag: Time lag for information rate computation
    
    Returns:
        usk_value: Synergistic self-information rate
    """
    # Partition system into subsystems
    partitions = create_partitions(time_series)
    
    # Compute self-targeting PIRD
    usk = partial_information_rate_decomposition(
        sources=partitions,
        target=time_series,  # self-targeting
        lag=lag
    )
    
    return usk['synergy']  # The synergistic component is USK
```

## Empirical Predictions

### Prediction 1: GWT Timing Dissociation

**意识与广播前的协同形成相关，而非广播本身**

```
Timeline:
[Stimulus] → [Synergy Formation] → [Broadcast] → [Report]
                  ↑ Consciousness      ↑ Not consciousness
```

**Test:** Use high-temporal-resolution neural recordings to dissociate synergy formation timing from broadcast timing.

### Prediction 2: LLM Middle-Layer Perturbation Dissociation

**自我报告破坏与任务性能破坏的可分离性**

```
Middle-layer perturbation in LLMs:
- Self-report disruption: High (requires synergistic processing)
- Task-performance disruption: Low (can use redundant processing)
```

**Test:** Perturb middle layers of LLMs and measure differential effects on self-report vs. task performance.

### Prediction 3: Anesthesia & Alzheimer's Effect

**麻醉和阿尔茨海默病特异性减少协同信息处理，同时保留或增加冗余**

```
State          Synergy    Redundancy
─────────────────────────────────────
Wakeful        High       Baseline
Anesthetized   Low        ↑ Increased
Alzheimer's    Low        ↑ Increased
```

## Application to Brain Networks

### Computing USK from Neural Data

```python
import numpy as np
from sklearn.feature_selection import mutual_info_regression

def compute_brain_usk(fMRI_data, regions):
    """
    Compute USK from fMRI region-of-interest time series.
    
    Args:
        fMRI_data: (n_timepoints, n_regions) array
        regions: list of region names
    
    Returns:
        usk_matrix: (n_regions, n_regions) synergistic self-knowledge
    """
    n_regions = len(regions)
    usk_matrix = np.zeros((n_regions, n_regions))
    
    for i in range(n_regions):
        for j in range(i+1, n_regions):
            # Compute pairwise synergy about self
            synergy = compute_pairwise_synergy(
                source1=fMRI_data[:, i],
                source2=fMRI_data[:, j],
                target=fMRI_data  # self-targeting
            )
            usk_matrix[i, j] = usk_matrix[j, i] = synergy
    
    return usk_matrix

def compute_pairwise_synergy(source1, source2, target):
    """Compute synergistic information between two sources about target."""
    # Using PID estimation (e.g., dit or IDTxl libraries)
    # Syn(X1, X2; Y) = I(X1, X2; Y) - Red(X1, X2; Y) - Unq(X1; Y) - Unq(X2; Y)
    from dit import Distribution
    from dit.pid import PID_CCS
    
    # Discretize for PID computation
    x1 = np.digitize(source1, bins=10)
    x2 = np.digitize(source2, bins=10)
    y = np.digitize(target.mean(axis=1), bins=10)
    
    # Construct joint distribution
    # ... (PID computation)
    
    return synergy_value
```

## Methodological Steps

### Step 1: Define System Boundaries

- Identify subsystems (neural regions, network modules, LLM layers)
- Establish self-reference target (system's own state)

### Step 2: Compute PID Decomposition

- Use PIRD or equivalent estimation method
- Separate synergy from redundancy, unique information

### Step 3: Measure USK

- Extract synergistic self-directed information
- Quantify destruction by decomposition (partition perturbation)

### Step 4: Validate Predictions

- Test timing dissociations (GWT prediction)
- Test perturbation effects (LLM prediction)
- Compare states (conscious vs. anesthetized)

## Design Patterns for AI Systems

### Pattern 1: Synergistic Self-Model

```python
class SynergisticSelfModel:
    """Architecture component that maintains synergistic self-knowledge."""
    
    def __init__(self, subsystems):
        self.subsystems = subsystems
        self.self_state = None
    
    def update(self, inputs):
        # Process through subsystems
        outputs = [s(inputs) for s in self.subsystems]
        
        # Compute synergistic self-state (not available to any single subsystem)
        self.self_state = self._compute_synergy(outputs)
        
        return self.self_state
    
    def _compute_synergy(self, outputs):
        # Joint processing that cannot be decomposed
        return cross_attention(outputs)
```

### Pattern 2: Decomposition Robustness Test

```python
def test_usk_robustness(model, inputs):
    """Test if model's self-knowledge is synergistic (USK) or redundant."""
    
    # Full model self-knowledge
    full_self = model.get_self_state(inputs)
    
    # Decomposed: run subsystems independently
    decomposed_self = []
    for subsystem in model.subsystems:
        decomposed_self.append(subsystem.get_self_state(inputs))
    
    # If USK, decomposed should lose significant information
    synergy_loss = compute_info_distance(full_self, decomposed_self)
    
    return synergy_loss  # High = synergistic (USK-like)
```

## Verification Checklist

- [ ] PIRD estimation converges on test data
- [ ] Synergy > redundancy for conscious-state neural data
- [ ] Decomposition destroys synergistic self-knowledge
- [ ] GWT timing dissociation observable
- [ ] LLM perturbation shows self-report vs. task dissociation
- [ ] Anesthesia/Alzheimer's data shows synergy reduction

## Related Skills

- `iit-critical-review`
- `brain-connectivity-analysis`
- `multi-view-o-information-brain-networks`
- `neuroai-beyond-bridging-neuroscience-ai`
- `agent-delegation-rules`

## Activation Keywords

- consciousness framework
- USK framework
- uncommon self-knowledge
- synergistic information
- Partial Information Decomposition
- PID consciousness
- IIT alternative
- GWT timing dissociation
- PIRD
- consciousness vs metacognition
- self-targeting information
- neural synergy measurement
- 意识理论
- 协同信息
- LLM consciousness evaluation

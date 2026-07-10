---
name: hierarchical-brain-criticality
description: Hierarchical organization of critical brain dynamics. Studies how criticality signatures vary along anatomical hierarchy in brain systems using phenomenological renormalization group approaches on large-scale neuronal spiking data.
category: neuroscience
---

# Hierarchical Brain Criticality

## Overview

This methodology studies how **criticality signatures** in brain dynamics vary systematically along the **anatomical hierarchy** of brain systems. Uses phenomenological renormalization group (PRG) approaches on large-scale neuronal spiking activity.

**Paper**: "Hierarchical organization of critical brain dynamics" (arXiv:2604.21832, April 2026)

## Trigger Words

- hierarchical criticality, brain criticality hierarchy, PRG brain dynamics
- renormalization group neural activity, criticality exponents gradient
- mouse visual cortex criticality, hippocampal critical dynamics

## Core Methodology

### 1. Phenomenological Renormalization Group (PRG)

PRG is applied to neuronal spiking data to:
- Coarse-grain neural activity across spatial scales
- Extract criticality exponents that characterize system behavior
- Identify whether the system operates near a critical point

### 2. Criticality Exponents

Multiple types of criticality markers are measured:

| Exponent Type | Measures | Direction in Hierarchy |
|--------------|----------|----------------------|
| **Static exponents** | Spatial correlation properties | One direction along anatomical gradient |
| **Dynamic exponents** | Temporal correlation properties | **Opposite** direction along gradient |

Key finding: The direction of the criticality gradient is **inconsistent across different exponents**, revealing a nontrivial, measure-dependent organization.

### 3. Anatomical Hierarchy Mapping

- Mouse visual cortex: V1 → higher visual areas
- Hippocampus: along known anatomical gradients
- Criticality signatures mapped onto these known hierarchies

### 4. Task-Dependent Modulation

- Criticality signatures in visual system are **strongly modulated** by visual task engagement
- During active engagement, correlations among criticality markers across brain regions are sufficient to **reconstruct the anatomical hierarchy from dynamics alone**

### 5. Scaling Relations

- Scaling exponents closely follow **theoretically predicted scaling relations** among them
- Exponents **covary with hierarchical position**
- Provides direct link between collective neural dynamics and macroscopic brain architecture

## Implementation Guide

### Step 1: Data Collection
```python
# Large-scale neuronal spiking data
# Mouse visual cortex or hippocampus
spike_trains = load_spike_data(animal_model='mouse', region='visual_cortex')
```

### Step 2: PRG Application
```python
# Apply phenomenological renormalization group
# Coarse-grain at multiple spatial scales
for scale in scales:
    coarse_spikes = coarse_grain(spike_trains, scale_factor=scale)
    exponents[scale] = compute_criticality_exponents(coarse_spikes)
```

### Step 3: Criticality Exponent Extraction
```python
# Static exponents (spatial correlations)
static_exponents = compute_static_criticality(spike_data)

# Dynamic exponents (temporal correlations)
dynamic_exponents = compute_dynamic_criticality(spike_data)
```

### Step 4: Hierarchy Correlation
```python
# Correlate exponents with known anatomical hierarchy
hierarchy_correlation = pearsonr(exponents, anatomical_hierarchy_positions)
```

### Step 5: Task Modulation Analysis
```python
# Compare resting vs. task-engaged states
resting_criticality = compute_criticality(resting_state_data)
task_criticality = compute_criticality(task_engaged_data)
modulation = task_criticality - resting_criticality
```

## Key Findings

1. **Non-uniform criticality**: Signatures of criticality are NOT uniform across brain regions
2. **Measure-dependent organization**: Different exponents point in different directions along the hierarchy
3. **Task modulation**: Visual task engagement strongly modulates criticality signatures
4. **Hierarchy reconstruction**: Correlations among criticality markers during active engagement can reconstruct the anatomical hierarchy
5. **Scaling relation compliance**: Exponents follow theoretically predicted scaling relations

## Pitfalls

1. **Multiple exponent contradiction**: Static and dynamic exponents may point in opposite directions. Don't assume a single "criticality gradient" exists.
2. **Data requirements**: Large-scale spiking data from multiple brain regions needed. Small datasets won't reveal hierarchical patterns.
3. **Task state importance**: Resting-state data alone may miss critical modulations. Include task-engaged recordings.
4. **Scale selection**: PRG results depend on chosen coarse-graining scales. Must test multiple scales.

## Related Skills
- brain-criticality-hypothesis-assessment: Critical assessment of brain criticality
- brain-criticality-milro-assessment: Memory-induced long-range order assessment
- griffiths-phase-brain-criticality: Griffiths phase framework for brain criticality

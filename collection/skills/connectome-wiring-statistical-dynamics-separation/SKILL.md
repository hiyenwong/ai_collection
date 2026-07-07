---
name: connectome-wiring-statistical-dynamics-separation
description: Separating wiring-specific from statistical control of dynamics in a complete connectome. Analysis of larval Drosophila brain showing coarse statistics set dynamical regime while specific wiring determines activity routing.
version: 1.0.0
category: neuroscience
arxiv_id: 2606.17745
author: Stavros Therianos
institution: Independent Researcher
published: 2026-06-16
activation_words:
  - connectome dynamics
  - wiring statistics
  - statistical versus specific wiring
  - larval drosophila
  - connectome control
  - network operator gain
  - mushroom body dynamics
  - olfactory pathway routing
  - degree-weight matching
  - null model hierarchy
related_skills:
  - connectome-wiring-statistics-control-dynamics
  - brain-network-controllability
  - connectome-constrained-neural-network
  - connectome-genetic-environmental-architecture
  - effective-plasticity
---

# Separating Wiring-Specific from Statistical Control of Dynamics in a Complete Connectome

## Core Innovation

首次在**完整连接组**（果蝇幼虫脑）上系统性分离：
- **粗粒统计特性**：决定全局动力学 regime（增益、维度、线性度）
- **精细接线模式**：决定活动传播路径和主导电路

**核心发现**: 统计特性设定 regime，精细接线设定几何。

## Methodology

### Frozen Operator Assay

将连接组作为**固定动力学算子**运行：
- **无单神经元参数调优**: 所有属性归因于接线
- **Rate-based model**: 无动作电位、时间常数、突触动力学
- **Spectral radius ρ = 0.99**: Leaky-tanh update

```python
# Frozen operator framework
W = connectome_weight_matrix  # Fixed
x_{t+1} = tanh(ρ * W @ x_t + input)
# No tuned physiology
```

### Null Model Ladder

从最不保留接线到最保留接线：

| Level | Model | Preserves |
|-------|-------|-----------|
| 1 | Unstructured Gaussian | Nothing |
| 2 | Degree + Weight Matched | In/out-degree, weight distribution |
| 3 | Block-Preserving Rewire | + Cell-class architecture |
| 4 | Connectome | Exact placement |

**关键**: Level 2-3 保留统计特性但 scramble 接线位置。

### Structural-Dynamical Properties

1. **Operator Gain**: How much it amplifies input
2. **Dimensionality**: How many directions survive
3. **Mode Leverage**: Which neurons shape modes
4. **Sparse-Input Routing**: Where input lands

## Key Results

### Global Regime: Statistical Control

**Degree+Weight matched ensemble reproduces**:
- Operator gain
- Dimensionality
- Near-linearity

**Implication**: 这些全局性质不依赖具体接线，只依赖统计特性。

### Pathways: Wiring-Specific Control

**Sparse input routing**:
- Connectome: Activity confined to olfactory pathway
- Rewired networks: Activity floods widely

**Mushroom body dominance**:
- Leading modes concentrated in MB (learning center)
- Rewiring distributes modes uniformly
- Convergence neurons depleted from driving modes

### Cell-Class Architecture Contribution

**Partial reproduction of confinement**:
- Block-preserving rewire captures ~50% of routing specificity
- Remaining 50% driven by fine synaptic placement

**MB-specific wiring concentration**:
- Not just cell-class labels
- Fine-grained synapse placement matters

### Null Hierarchy Working: Retraction Example

**Lateral horn localization claim**:
- Initial observation: LH concentrates driven-side modes
- Size-matched control: Random sets show similar
- **Result**: Claim retracted (false positive)

## Anatomical Context

### Larval Drosophila Brain

- **3,013 neurons** total
- **111,243 directed connections**
- **Strongly connected core**: 2,825 neurons, 109,438 synapses
- **536 self-loops**

### Identified Circuits

| Circuit | Neurons | Function |
|---------|---------|----------|
| Mushroom Body (MB) | 231 | Learning center |
| Lateral Horn (LH) | 201 | Olfactory processing |
| Central Complex (CX) | 77 | Navigation |
| Remaining | 2,316 | Mixed populations |

### Input/Output Ports

- **Afferent**: 80 input ports
- **Efferent**: 97 output ports

## Theoretical Framework

### Operator Gain

```python
gain = ||W @ x|| / ||x||
# Degree+weight matched ensemble reproduces
```

### Dimensionality

```python
dim = count(eigenvalues with |λ| > threshold)
# Statistical control only
```

### Mode Leverage (Adjoint-Side)

```python
# Which neurons shape the modes?
mode_leverage = W^T @ dominant_eigenvectors
# MB concentrates beyond matched ensemble
```

### Sparse-Input Routing

```python
# Where does sparse input land?
activation_pattern = W^n @ sparse_input
# Connectome: confined to olfactory pathway
# Rewired: distributed everywhere
```

## Biological Interpretation

### Statistics → Regime

**Coarse features determine**:
- Overall responsiveness (gain)
- Information capacity (dimensionality)
- Linear/nonlinear behavior

**Why**: All neurons have similar connectivity statistics → similar dynamical role

### Wiring → Geometry

**Specific placement determines**:
- Which pathways activate
- Which circuits dominate dynamics
- Where information flows

**Why**: Exact synapse locations create privileged channels

### Mushroom Body Significance

**MB as dynamical hub**:
- Concentrates leading adjoint modes
- Shapes which neurons drive dynamics
- Learning center has outsized control

**Not cell-class alone**: Fine MB-specific wiring critical

## Null Model Details

### Degree + Weight Matching

```python
# Preserve statistics
for neuron in connectome:
    in_degree[n] = count(inputs)
    out_degree[n] = count(outputs)
    total_weight[n] = sum(connections)
    
# Scramble placement
rewire_connections(preserve=in/out_degree, weights)
```

### Block-Preserving Rewire

```python
# Preserve cell-class architecture
blocks = [MB, LH, CX, Others]
for block in blocks:
    preserve_internal_connections(block)
    scramble_between_blocks()
```

### Size-Matched Random Control

```python
# For circuit-specific claims
circuit = MB neurons  # n = 231
random_set = random_neurons(size=231)
compare(circuit, random_set)
```

## Experimental Validation

### White-Noise Drive

- Input through afferent ports
- Measure core state evolution
- No behavioral/physiological state

### Readout Metrics

1. **Operator gain**: Signal amplification
2. **Dimensionality**: Active subspace
3. **Mode leverage**: Driving neurons
4. **Routing confinement**: Pathway specificity

## Limitations

### What Model Omits

- Action potentials
- Single-neuron time constants
- Synaptic/receptor kinetics
- Neuromodulation
- Behavioral state
- Gap junctions

### Interpretation Caution

**Not physiological simulation**:
- Structural-dynamical instrument
- No odor-evoked activity claims
- Wiring-only analysis

## Applications

### Connectome Analysis
1. **Wiring vs statistics claims**: Null model hierarchy
2. **Circuit dominance**: Mode leverage analysis
3. **Pathway routing**: Sparse-input confinement
4. **Architecture effects**: Block-preserving tests

### Comparative Connectomics
- Cross-species statistics comparison
- Developmental wiring changes
- Evolutionary wiring optimization

### Neural Network Theory
- Weight initialization insights
- Architectural inductive bias
- Connectivity regime analysis

## Technical Requirements

### Dependencies
- NumPy/SciPy (linear algebra)
- NetworkX (graph operations)
- Matplotlib (visualization)

### Hardware
- CPU: Network analysis
- RAM: ~10GB for full connectome

## Key Takeaways

1. **Separation**: Statistics set regime, wiring sets geometry
2. **Null hierarchy**: Different claims need different controls
3. **MB dominance**: Learning center shapes dynamics
4. **Retraction example**: Null models catch false positives
5. **Frozen operator**: Wiring-only attribution

## Citation

```bibtex
@article{therianos2026connectome,
  title={Separating wiring-specific from statistical control of dynamics in a complete connectome},
  author={Therianos, Stavros},
  journal={arXiv preprint arXiv:2606.17745},
  year={2026}
}
```

---

**Activation**: Use when analyzing connectome dynamics, wiring vs statistics separation, network regime analysis, or mushroom body functional dominance in complete connectomes.
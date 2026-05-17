---
name: quantum-like-cognitive-modeling
description: "量子类认知建模方法论。运用希尔伯特空间形式化方法模拟认知系统中的情境性、观测量的不相容性以及类纠缠相关性，而非假设大脑中存在物理量子过程。适用于决策分析、认知建模、神经动力学测试。触发词：量子认知、quantum cognition、量子类建模、情境性、认知纠缠、mental markers、leggett-garg"
---

# Quantum-Like Cognitive Modeling

## Overview

Quantum-like modeling (QLM) applies the mathematical formalism of quantum mechanics — Hilbert spaces, operators, superposition, entanglement — to model cognitive phenomena **without** assuming physical quantum processes in the brain. This methodology captures non-classical features of human cognition including contextuality, order effects, incompatible mental observables, and entanglement-like correlations between cognitive and affective components.

## Activation Keywords

- quantum cognition
- 量子认知
- quantum-like modeling
- 量子类建模
- contextuality cognition
- 情境性认知
- cognitive entanglement
- 认知纠缠
- mental markers
- leggett-garg neural
- incompatibility mental observables
- non-classical cognition

## Core Framework

### 1. Quantum-Like State Representation

Represent cognitive states as vectors in a Hilbert space:

```
|ψ⟩ = α|A⟩ + β|B⟩  (superposition of mental states)
```

Where:
- `|ψ⟩` is the cognitive state vector
- `|A⟩`, `|B⟩` are basis states representing definite cognitive outcomes
- `α`, `β` are complex probability amplitudes
- Measurement (decision) collapses the state to a basis state

### 2. Contextuality Modeling

Mental observables are context-dependent. Different measurement contexts yield different results:

```python
# Different question orderings produce different probability distributions
P(A then B) ≠ P(B then A)  # Order effects
```

**Implementation**: Use non-commuting operators for incompatible observables:
```
[A, B] = AB - BA ≠ 0
```

### 3. Incompatibility of Mental Observables

Two cognitive variables are incompatible if they cannot be simultaneously measured with arbitrary precision. This models situations where:
- Asking about one belief changes another
- Emotional and rational evaluations interfere
- Context shifts the available cognitive options

### 4. Intra-System Entanglement

Unlike inter-system entanglement (between separate agents), intra-system entanglement models correlations **within** a single cognitive system:

```
|M⟩ = Σᵢⱼ cᵢⱼ |cognitiveᵢ⟩ ⊗ |affectiveⱼ⟩
```

This captures how rational evaluation and emotional coloring are structurally entangled in decision-making.

### 5. Mental Markers Framework

Under information overload, individuals respond to compact "mental markers" — structured quantum-like states carrying both cognitive and affective components:

```python
class MentalMarker:
    """A quantum-like mental marker with cognitive-affective structure."""
    
    def __init__(self, cognitive_basis, affective_basis):
        # Hilbert space = H_cognitive ⊗ H_affective
        self.state = self._prepare_marker_state(cognitive_basis, affective_basis)
    
    def measure(self, context_operator):
        """Measure the marker in a specific context."""
        return self._collapse(context_operator, self.state)
    
    def entanglement_degree(self):
        """Compute cognitive-affective entanglement."""
        return self._compute_schmidt_decomposition()
```

## Leggett-Garg Tests in Neural Dynamics

The Leggett-Garg inequality provides a **temporal** analogue of Bell inequalities for testing non-classical behavior in neural systems:

### Methodology

1. **Define observable**: Choose a binary neural variable (e.g., spike/no-spike, active/inactive)
2. **Measure at three time points**: t₁, t₂, t₃
3. **Compute temporal correlations**: K = C₁₂ + C₂₃ - C₁₃
4. **Test inequality**: Classical (diffusive) models require K ≤ 1
5. **Violation detection**: K > 1 indicates non-classical temporal structure

### Key Insight

**Violation ≠ quantum coherence**: A Leggett-Garg violation in neural dynamics indicates persistent, non-diffusive stochastic structure with memory effects — not necessarily microscopic quantum processes. The Telegrapher's equation (finite-velocity Kac processes) can produce such violations.

### Practical Application

```python
def leggett_garg_test(correlations):
    """Test Leggett-Garg inequality on temporal correlations.
    
    Args:
        correlations: dict with keys C12, C23, C13
    Returns:
        (K, violated): tuple of K value and whether inequality is violated
    """
    C12, C23, C13 = correlations['C12'], correlations['C23'], correlations['C13']
    K = C12 + C23 - C13
    return K, K > 1

# Interpretation:
# K ≤ 1: Compatible with classical diffusive dynamics
# K > 1: Non-classical temporal correlations (persistent/memory effects)
```

## Contextuality-Incompatibility-Entanglement Triad

Three non-classical features that together characterize quantum-like cognitive systems:

| Feature | What it models | Mathematical signature |
|---------|---------------|----------------------|
| **Contextuality** | Context-dependent judgments | Measurement outcome depends on measurement context |
| **Incompatibility** | Conflicting mental variables | Non-commuting operators [A,B] ≠ 0 |
| **Entanglement** | Cognitive-affective coupling | Non-separable joint states |

## Applications

### 1. Decision-Making Under Uncertainty
- Model order effects in sequential choices
- Capture framing effects as basis changes
- Explain preference reversals as context-dependent measurements

### 2. Information Overload Analysis
- Use mental markers to model how agents process excessive information
- Quantify cognitive-affective entanglement in stress responses
- Predict decision degradation under information saturation

### 3. Neural Dynamics Testing
- Apply Leggett-Garg tests to neural time-series data
- Distinguish diffusive vs. persistent stochastic models
- Identify non-Markovian structure in neural recordings

### 4. Affective Computing
- Model emotion-cognition interference patterns
- Predict how emotional context alters rational evaluation
- Design adaptive systems that respect quantum-like interference

## Error Handling

### Classical Sufficiency Check
Before applying QLM, test whether classical models suffice:
1. Check if order effects exist in the data
2. Test Kolmogorov probability axioms for violations
3. Apply Leggett-Garg test for temporal non-classicality
4. Only use QLM if classical models fail

### Over-interpretation Warning
- QLM is a **mathematical formalism**, not a claim about quantum physics in the brain
- Always interpret violations conservatively (non-classical ≠ quantum)
- Distinguish between quantum-like (formalism) and quantum (physical)

## Resources

- **arXiv:2605.12126** - Leggett-Garg Tests in Neural Dynamics (Partha Ghose, 2026)
- **arXiv:2603.03358** - Contextuality, Incompatibility, and Intra-System Entanglement of Mental Markers (Khrennikov et al., 2026)
- **Busemeyer & Bruza (2012)** - Quantum Models of Cognition and Decision

## Related Skills

- `quantum-cognition` - General quantum cognition methodology
- `neuro-quantum-research` - Quantum methods for neuroscience
- `decision-making-models` - Cognitive decision frameworks

## Notes

- This methodology is **informational**, not physical — it uses quantum mathematics as a tool for modeling, not as a claim about brain physics
- The framework is particularly powerful for systems exhibiting interference, contextuality, and non-commutativity
- Always validate QLM predictions against classical alternatives
- Mental markers are especially useful for modeling behavior under cognitive load
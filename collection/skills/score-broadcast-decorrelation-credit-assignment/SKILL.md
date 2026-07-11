---
name: score-broadcast-decorrelation-credit-assignment
description: "Score Broadcast and Decorrelation (SBD)方法论 - 广播式信用分配的通用框架，为三因子学习规则提供理论基础。Error broadcast作为backpropagation的生物合理替代方案，适用于不同iable losses。Activation: SBD, score broadcast, credit assignment, three-factor learning, error broadcast, 生物可塑性."
---

# Score Broadcast and Decorrelation (SBD): Broadcast-Based Credit Assignment

Principled framework for biologically plausible credit assignment across general differentiable losses, providing theoretical grounding for three-factor learning rules from neuroscience.

## Core Concept

**Key Insight**: Error broadcast is a biologically plausible alternative to backpropagation that sends output information to hidden layers without weight transport.

**Foundation**: Stochastic orthogonality of optimal estimators—optimal residual orthogonal to functions of input.

## Theoretical Foundation

### Orthogonality Principle

**Core Equation**
```
Score(output) ⟂ Hidden_Activation
```

Where:
- **Score** = ∇L / ∂output (gradient of loss w.r.t. final-layer output)
- **Orthogonality holds**: When optimal score has conditional mean zero

### Loss Score as Broadcast Signal

**Three-Factor Learning Rule Grounding**
```
Δw = f(input) × g(output_activity) × neuromodulatory_factor
↓
 neuromodulatory_factor = broadcast_loss_score
```

## Unifying Framework

### Applicable Loss Families

**Unified across standard differentiable losses**:

1. **Cross-Entropy**
   - Classification tasks
   - Score derivation explicit
   
2. **Bregman Divergences**
   - Generalization of MSE
   - Natural gradient-like
   
3. **Proper Scoring Rules**
   - Calibration metrics
   - Probabilistic predictions
   
4. **Exponential-Family Negative Log-Likelihoods**
   - Statistical estimation
   - Information geometry connection

### Single Principle Unification

```
Output_Score ⟂ Hidden_Activation
↓ (conditional mean zero)
↓
Broadcast-based credit assignment valid for all loss types
```

## Key Contributions

### 1. Score Vector Expansion

**Enriching Broadcast Signal**

```python
def score_vector_expansion(score_scalar):
    """
    Expand score into vector to enrich decorrelation directions
    while preserving orthogonality framework.
    """
    # Create orthogonal basis
    basis = construct_orthogonal_basis(score_scalar)
    
    # Expand to vector representation
    score_vector = project_to_basis(score_scalar, basis)
    
    return score_vector  # Richer representation, same principle
```

**Benefits**:
- More informative broadcast signal
- Better gradient estimation
- Preserves theoretical grounding
- Improves performance on CIFAR-10/Tiny ImageNet

### 2. Cross-Entropy Case Explicit Derivation

**Mathematical Derivation**

For cross-entropy loss:
```
L_CE = -y_true * log(y_pred)
↓
Score = ∇L_CE / ∂y_pred = -y_true / y_pred
↓
Orthogonality condition: E[Score | hidden] = 0
↓
Broadcast signal: Score broadcast to all layers
↓
Credit assignment: Δw_ij = x_i × h_j × Score
```

### 3. Admissible Loss Class Characterization

**Definition**: Losses where orthogonality principle holds

**Condition**: Optimal score has conditional mean zero
```
Loss ∈ AdmissibleClass iff E[Score | Hidden] = 0
```

**Examples**:
- MSE ✓
- Cross-Entropy ✓
- Bregman Divergences ✓
- Proper Scoring Rules ✓
- Exponential Family NLL ✓

## Implementation Framework

### SBD Algorithm

```python
def score_broadcast_decorrelation(
    input, hidden, output, loss_fn, 
    score_expansion_dim=None
):
    """
    Score Broadcast and Decorrelation credit assignment.
    
    Args:
        input: Input layer activations
        hidden: Hidden layer activations
        output: Output layer activations
        loss_fn: Differentiable loss function
        score_expansion_dim: Optional score vector expansion
    
    Returns:
        Weight updates for each layer
    """
    # Compute loss score
    score = compute_loss_score(output, loss_fn)
    
    # Optional score vector expansion
    if score_expansion_dim:
        score = expand_score_vector(score, score_expansion_dim)
    
    # Broadcast score to hidden layers
    broadcast_signal = broadcast_score(score, hidden)
    
    # Decorrelation update
    updates = decorrelation_update(input, hidden, broadcast_signal)
    
    return updates
```

### Compute Loss Score

```python
def compute_loss_score(output, loss_fn):
    """
    Compute gradient of loss w.r.t. output (score).
    """
    # Differentiate loss
    score = torch.autograd.grad(
        loss_fn(output), 
        output, 
        create_graph=True
    )[0]
    
    return score
```

### Score Vector Expansion

```python
def expand_score_vector(score_scalar, expansion_dim):
    """
    Expand scalar score into vector for richer broadcast.
    
    Preserves orthogonality while adding decorrelation directions.
    """
    # Create orthogonal basis vectors
    basis = torch.randn(expansion_dim)
    basis = torch.nn.functional.normalize(basis, dim=0)
    
    # Project score onto basis
    score_vector = score_scalar * basis
    
    # Add perturbation directions
    perturbation = torch.randn(expansion_dim) * 0.1
    score_vector = score_vector + perturbation
    
    # Maintain zero conditional mean
    score_vector = decorrelation_adjust(score_vector)
    
    return score_vector
```

### Broadcast Mechanism

```python
def broadcast_score(score, hidden_activations):
    """
    Broadcast loss score to all hidden layers.
    
    No weight transport (biologically plausible).
    """
    # Broadcast signal (same for all hidden units)
    broadcast_signal = score.detach()  # Prevent weight transport
    
    # Modulate hidden activations
    modulated = hidden_activations * broadcast_signal
    
    return modulated
```

### Decorrelation Update

```python
def decorrelation_update(input_activations, hidden_activations, broadcast_signal):
    """
    Compute weight updates via decorrelation.
    
    Orthogonality: Score ⟂ Hidden ensures unbiased updates.
    """
    # Three-factor rule
    neuromodulatory_factor = broadcast_signal
    
    # Input factor
    input_factor = input_activations
    
    # Hidden factor  
    hidden_factor = hidden_activations
    
    # Weight update: Δw = input × hidden × neuromodulatory
    updates = input_factor * hidden_factor * neuromodulatory_factor
    
    return updates
```

## Biological Plausibility

### Three-Factor Learning Rule Grounding

**Neuroscience Connection**:
```
Δw_synapse = f(pre_activity) × g(post_activity) × neuromodulator
↓
SBD identifies neuromodulator = broadcast_loss_score
```

**Biological Interpretation**:
1. **Pre-synaptic activity** → Input activations
2. **Post-synaptic activity** → Hidden activations
3. **Neuromodulatory signal** → Broadcast loss score (dopamine-like)

### No Weight Transport

**Key Biological Advantage**:
- Backpropagation requires weight transport (non-local)
- SBD: Only broadcast output score (local updates)
- Matches biological synaptic plasticity constraints

## Experimental Results

### CIFAR-10 Performance

**Baseline Comparison**:
- Backpropagation: 92% accuracy
- Error Broadcast (EBD, MSE only): 85% accuracy
- **SBD (all losses)**: 89% accuracy
- **SBD + Score Expansion**: 91% accuracy

### Tiny ImageNet Performance

- Backpropagation: 65% accuracy
- Error Broadcast (EBD): 58% accuracy
- **SBD**: 62% accuracy
- **SBD + Score Expansion**: 64% accuracy

### Key Findings

1. **SBD substantially improves over existing broadcast approaches**
2. **Score vector expansion delivers further gains**
3. **Approaches backpropagation performance**
4. **Maintains biological plausibility**

## Algorithm Comparison

### Backpropagation vs. SBD

| Aspect | Backpropagation | SBD |
|--------|----------------|-----|
| Credit Assignment | Weight transport | Broadcast score |
| Biological Plausibility | No (weight transport) | **Yes** (local) |
| Applicable Losses | All differentiable | All admissible losses |
| Performance | Highest | Near-backprop |
| Neuromodulator Link | No theoretical link | **Grounded** |

### Error Broadcast and Decorrelation (EBD) vs. SBD

| Aspect | EBD (prior work) | SBD (this work) |
|--------|------------------|----------------|
| Loss Type | MSE only | **All differentiable losses** |
| Orthogonality | Residual ⟂ input | **Score ⟂ hidden** |
| Theoretical Scope | Limited | **Generalized** |
| Three-Factor Grounding | Implicit | **Explicit derivation** |
| Score Expansion | No | **Yes** |

## Use Cases

### Use Case 1: Biologically Plausible Neural Networks

**Scenario**: Build neural networks matching biological constraints

**SBD Application**:
1. Use SBD instead of backpropagation
2. Local updates only (no weight transport)
3. Three-factor rule matches synaptic plasticity
4. Neuromodulatory signal = loss score

### Use Case 2: Neuromorphic Hardware

**Scenario**: Implement learning on neuromorphic chips

**SBD Advantages**:
- No weight transport → simpler hardware
- Local updates → distributed processing
- Broadcast signal → global neuromodulator injection
- Real-time adaptation possible

### Use Case 3: Continual Learning Systems

**Scenario**: Systems that learn continuously

**SBD Benefits**:
- Local updates → less interference
- Broadcast neuromodulator → selective plasticity
- General loss applicability → diverse tasks
- Biological inspiration → robust learning

## Mathematical Details

### Orthogonality Derivation

**For admissible losses**:
```
Let Score = ∇L/∂output

Optimal estimator theory: 
E[Score | Hidden] = 0 (conditional mean zero)

Orthogonality consequence:
⟨Score, Hidden⟩ = 0 (inner product zero)

This enables:
Δw unbiased = E[input × Hidden × Score] = correct gradient
```

### Cross-Entropy Explicit

**Derivation**:
```
L_CE(y_pred, y_true) = -Σ y_true_i log(y_pred_i)

Score_i = ∇L/∂y_pred_i = -y_true_i / y_pred_i

Orthogonality check:
E[Score_i | Hidden] = E[-y_true_i/y_pred_i | Hidden]
                    = -E[y_true_i | Hidden] / y_pred_i
                    = 0 (when y_true independent of hidden)

Valid for: classification, proper scoring rules
```

### Score Vector Expansion Mathematics

**Expansion construction**:
```
Score_scalar s → Score_vector v

v = s * basis + perturbation
where:
- basis: orthonormal vectors
- perturbation: small random vector
- E[v | Hidden] ≈ 0 (preserve zero mean)

Enriches decorrelation directions:
Δw = input × Hidden × v (richer gradient estimate)
```

## Implementation Tips

### Tip 1: Choose Expansion Dimension

```python
# Small expansion: simpler, faster
score_dim = 3-5

# Large expansion: richer, slower
score_dim = 10-20

# Recommendation: Start with 5-10, tune experimentally
```

### Tip 2: Balance Real-time and Memory

```python
# Real-time info factor
realtime_weight = 0.7

# Memory info factor
memory_weight = 0.3

# Combined update
update = realtime_weight * current_update + memory_weight * past_update
```

### Tip 3: Check Orthogonality

```python
# Verify orthogonality holds
orthogonality = torch.dot(score_vector, hidden_activation)

# Should be near zero
assert abs(orthogonality) < threshold
```

## Limitations and Future Work

### Current Limitations

1. **Admissible Loss Restriction**: Not all losses valid
2. **Expansion Trade-off**: Complexity vs. performance
3. **Performance Gap**: Still below backpropagation
4. **Implementation Complexity**: More complex than backprop

### Future Directions

1. **Extend admissible loss class**
2. **Improve score expansion methods**
3. **Hardware neuromorphic implementations**
4. **Biological validation experiments**

## Related Skills

- **neuromodulated-synaptic-plasticity**: Three-factor learning
- **feedback-hebbian-continual-learning**: Biologically plausible learning
- **three-factor-snn-learning**: SNN three-factor rules
- **local-rl-alignment-engineering**: Local learning rules

## Key Papers

- Original: Uzun et al. (2026) arXiv:2605.30638
- Prior: Error Broadcast and Decorrelation (EBD)
- Background: Three-factor learning rules in neuroscience
- Related: Biologically plausible credit assignment literature

## Activation Triggers

- SBD
- score broadcast
- decorrelation
- credit assignment
- three-factor learning
- error broadcast
- 生物可塑性
- neuromodulated learning
- local learning rules
- biologically plausible neural network

## Recommended Model

- **sonnet4.5** (Implementation)
- **opus4.5** (Mathematical analysis)
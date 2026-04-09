# SKILL.md - Heavy-Tailed Weight Distribution Emergence

## Activation Keywords

- heavy-tailed distribution, weight distribution, connection weights
- structural plasticity, network topology, convergent-divergent units
- homeostatic dynamics, adaptive weight adjustment, rewiring
- brain network evolution, self-regulated emergence

## What It Does

Provides a unified mechanism for the simultaneous emergence of heavy-tailed weight distributions and complex network topologies in evolving brain networks through homeostatic self-regulation.

## When To Use

**Use this skill when:**
- Modeling brain network weight distributions
- Simulating structural plasticity with rewiring
- Generating heavy-tailed connectivity patterns
- Designing self-organizing neural networks
- Understanding convergent-divergent unit formation

**Do NOT use for:**
- Static network analysis (no plasticity)
- Scale-free network generation (different mechanism)
- Simple weight decay models (no homeostatic regulation)

## How To Use

### Step-by-Step Workflow

1. **Initialize Network**
   - Start with random connectivity matrix W
   - Set target activity level (homeostatic setpoint)
   - Define rewiring probability and weight adjustment rate

2. **Homeostatic Weight Adjustment**
   - Monitor neuronal activity: a_i(t)
   - Compute deviation from target: δ_i = a_i - a_target
   - Adjust weights: Δw_ij = -η * δ_i * w_ij
   - Weights strengthen when under-active, weaken when over-active

3. **Structural Plasticity (Rewiring)**
   - Based on same homeostatic signal δ_i
   - Remove weak connections: if w_ij < θ_remove, delete
   - Add new connections: if δ_i > θ_add, create new synapse
   - Preferentially connect to active neurons

4. **Self-Regulated Emergence**
   - Iterative process: weight adjustment → rewiring → topology change
   - Heavy-tailed distribution emerges naturally
   - Convergent-divergent units form automatically
   - Network reaches stable configuration

5. **Validation**
   - Check weight distribution tail: P(w) ~ w^(-α), α ≈ 2-3
   - Identify hub neurons (high in-degree)
   - Measure convergent-divergent unit density

### Key Parameters

| Parameter | Range | Biological Basis |
|-----------|-------|------------------|
| η (learning rate) | 0.001-0.1 | Synaptic plasticity rate |
| a_target | 0.1-0.5 Hz | Homeostatic setpoint |
| θ_remove | 0.01-0.1 | Synapse elimination threshold |
| θ_add | 0.5-1.0 | New synapse threshold |

### Emergent Properties

**Heavy-tailed weight distribution:**
```
P(w) ~ w^(-α) where α ≈ 2-3
```

**Convergent-divergent units:**
- Hubs with high convergence (many inputs)
- Hubs with high divergence (many outputs)
- Rich-club organization

## Example Usage

### Network Simulation

**Problem:** Model brain network with realistic weight distribution

**Traditional approach (separate mechanisms):**
```python
# Scale-free topology
G = barabasi_albert_graph(n, m)
# Heavy-tailed weights
weights = power_law_distribution(alpha=2.5)
```

**Self-regulated emergence (unified):**
```python
def homeostatic_plasticity_step(W, activity, target_activity):
    # Compute homeostatic error
    delta = activity - target_activity
    
    # Weight adjustment
    dW = -eta * np.outer(delta, np.ones(n)) * W
    W += dW
    
    # Rewiring
    for i in range(n):
        if delta[i] > theta_add:  # Under-active: add connections
            j = np.random.choice(np.where(W[i,:] == 0)[0])
            W[i,j] = w_init
        elif delta[i] < -theta_remove:  # Over-active: remove weak
            weak = np.where(W[i,:] < w_threshold)[0]
            W[i,weak] = 0
    
    return W
```

**Result:** Heavy-tailed distribution + complex topology emerge together

### Network Analysis

**Input:** Simulated brain network

**Analysis:**
1. Compute weight distribution histogram
2. Fit power-law tail: P(w) ~ w^(-α)
3. Identify hub neurons (degree > 2σ)
4. Measure convergent-divergent ratio

**Output:**
```
Weight distribution: α = 2.4 (heavy-tailed)
Hub neurons: 5% of population (convergent-divergent units)
Network efficiency: 0.78 (optimal regime)
```

## Description
Framework from arXiv papers. See paper reference for details.
## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply heavy-tailed-weight-emergence?

**Agent:** I'll help you understand and apply heavy-tailed-weight-emergence...

### Example 2: Advanced Application

**User:** What are the key considerations for heavy-tailed-weight-emergence?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **synaptic-weight-distributions-plasticity-geometry** - Weight distribution theory
- **brain-higher-order-structures** - Network topology analysis
- **neuromodulated-synaptic-plasticity** - Plasticity with neuromodulation

## Source

- arXiv:2508.21445v2
- Title: Self-regulated emergence of heavy-tailed weight distributions in evolving complex network architectures
- Utility: 0.88
- Authors: Jia Li, Cees van Leeuwen, Roman Bauer, Ilias Rentzeperis

## Notes

- Key insight: Same homeostatic rule drives both weight and topology
- Heavy-tailed distribution + complex topology emerge simultaneously
- Parsimonious mechanism: one rule, two emergent properties
- Applications: brain network modeling, neuromorphic engineering
- Validated across wide range of dynamical regimes

---

_Created: 2026-04-01_
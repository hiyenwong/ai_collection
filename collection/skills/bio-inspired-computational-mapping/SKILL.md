---
name: bio-inspired-computational-mapping
description: "Map biological neural processes to computational implementations. Translate neuroscience concepts (synaptic plasticity, neural dynamics, connectivity patterns) into algorithmic and software abstractions. Use when: (1) Implementing biologically-plausible learning rules, (2) Translating brain connectivity patterns to graph algorithms, (3) Mapping neuron models to computational units, (4) Bridging neuroscience papers to code implementations."
---

# Bio-Inspired Computational Mapping

Map biological neural processes to computational implementations.

## Activation Keywords

- bio-inspired computational mapping
- biological to computational
- neuroscience implementation
- biologically plausible algorithm
- neural process mapping
- 生物启发计算映射
- 神经科学实现
- brain-to-code mapping

## Tools Used

- `read`: Load neuroscience papers and biological models
- `write`: Generate computational implementations and mappings
- `exec`: Run simulation scripts for biological models

## Core Mapping Patterns

### Pattern 1: Neuron Model → Computational Unit

| Biological | Computational |
|------------|---------------|
| Membrane potential | State variable (float) |
| Action potential (spike) | Binary event / threshold crossing |
| Synaptic weight | Connection weight matrix |
| Refractory period | Cool-down timer after spike |
| LIF neuron | `V += -V/tau + I; spike = V > threshold` |

### Pattern 2: Learning Rule → Optimization Algorithm

| Biological Rule | Computational Equivalent |
|-----------------|--------------------------|
| Hebbian learning | `Δw = η * pre * post` |
| STDP | Spike-timing dependent weight update |
| BCM rule | Sliding threshold homeostasis |
| Backpropagation-free | Forward-Forward or perturbation methods |

### Pattern 3: Connectivity → Graph Structure

| Brain Structure | Graph Representation |
|-----------------|---------------------|
| Cortical columns | Hierarchical node clusters |
| Long-range connections | Sparse inter-cluster edges |
| Small-world topology | Watts-Strogatz graph model |
| Scale-free hubs | Barabási-Albert preferential attachment |

## Instructions for Agents

### Step 1: Identify Biological Concept
Read the neuroscience paper or description; identify: neuron type, learning rule, connectivity pattern, or dynamics model.

### Step 2: Select Mapping Pattern
Match biological concept to the appropriate computational pattern (neuron model, learning rule, or connectivity).

### Step 3: Generate Implementation
Translate to Python/NumPy code using the mapping table; add type hints and docstrings.

### Step 4: Validate
Test computational implementation against known biological properties (e.g., spike rate, learning convergence).

### Step 5: Document Mapping
Record the biological source, computational abstraction, and any simplifications made.

## Examples

### Example 1: Implement LIF Neuron from Biology

```
User: "Implement a leaky integrate-and-fire neuron from the biology paper"

Agent:
1. Extract biological parameters: tau_m, V_rest, V_threshold, V_reset
2. Map to computational model: V(t+dt) = V(t) + dt/tau_m * (-V(t) + R*I(t))
3. Add spike detection: if V >= threshold: spike, V = V_reset
4. Implement refractory period
5. Test with step current input
```

### Example 2: Map Brain Connectivity to Graph

```
User: "Convert this brain connectivity matrix to a graph algorithm"

Agent:
1. Load connectivity matrix from neuroscience paper
2. Identify topology: small-world or scale-free?
3. Map to NetworkX graph with appropriate edge weights
4. Apply PageRank or community detection
5. Report computational properties matching biological findings
```

## Resources

- `references/`: Neuroscience-to-computation mapping references
- Related: `brain-connectivity-analysis`, `brain-inspired-snn-pattern-analysis`

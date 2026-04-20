---
name: skill.md---neuro-pc-causal-functional-connectivity
description: Skill for AI agent capabilities
---

# SKILL.md - Neuro-PC Causal Functional Connectivity

## Activation Keywords

- Neuro-PC, causal functional connectivity, neural dynamics
- causal inference, neural connectivity, functional connectome
- time series causality, Granger causality, neural pathways
- multi-dimensional time series, neuronal recordings

## What It Does

Neuro-PC is a novel algorithm for inferring causal functional connectivity between neurons from multi-dimensional time series (neuronal recordings). Maps how neural activity flows within circuits and enables inference of functional neural pathways.

## When To Use

**Use this skill when:**
- Inferring causal connectivity from neural recordings
- Analyzing multi-dimensional neural time series
- Mapping functional neural pathways
- Understanding information flow in neural circuits
- Differentiating direct vs indirect connectivity

**Do NOT use for:**
- Correlation-based connectivity (no causality)
- Static connectivity analysis (no temporal dynamics)
- Single-neuron analysis (requires population data)

## How To Use

### Step-by-Step Workflow

1. **Collect Neural Time Series**
   - Multi-electrode recordings (MEA, Neuropixels)
   - Calcium imaging data
   - LFP/ECoG signals
   - Format: N neurons × T time points

2. **Preprocess Data**
   - Filter and denoise signals
   - Normalize firing rates
   - Handle missing data
   - Detrend if necessary

3. **Apply Neuro-PC Algorithm**
   - Construct time-lagged variables
   - Build predictive models
   - Test for causal relationships
   - Estimate connectivity strength

4. **Infer Causal Graph**
   - Identify direct connections
   - Distinguish from indirect paths
   - Build directed connectivity matrix

5. **Validate and Interpret**
   - Test robustness to perturbations
   - Compare with known anatomy
   - Identify functional pathways

### Key Concepts

**Causal Functional Connectivity:**
- Not just correlation, but causation
- X → Y means X influences Y's future state
- Captures direction and strength of influence

**Neural Pathways:**
- Sensory-motor-behavioral chains
- Feedforward and feedback loops
- Recurrent circuits

### Algorithm Framework

1. **Time-lagged prediction:**
```
Y(t) = f(X(t-1), X(t-2), ..., X(t-τ)) + ε(t)
```

2. **Causal test:**
- If adding X improves prediction of Y → causal link
- Conditional independence tests for direct vs indirect

3. **Connectivity matrix:**
```
C[i,j] = causal strength from neuron i to j
```

## Example Usage

### Inferring Causal Connectivity

**Problem:** Infer causal connectivity from neural recordings

**Pipeline:**
```python
import numpy as np
from sklearn.linear_model import Ridge

class NeuroPC:
    def __init__(self, n_neurons, max_lag=10, alpha=1.0):
        self.n_neurons = n_neurons
        self.max_lag = max_lag
        self.alpha = alpha  # Regularization
        
    def infer_causality(self, data):
        """
        Infer causal connectivity from neural time series
        
        Parameters:
        -----------
        data : array (n_neurons, n_timepoints)
            Neural activity data
            
        Returns:
        --------
        causal_matrix : array (n_neurons, n_neurons)
            Causal connectivity matrix
        """
        n, T = data.shape
        causal_matrix = np.zeros((n, n))
        
        for target in range(n):
            # Target variable Y
            Y = data[target, self.max_lag:].T
            
            # Build lagged predictors for all sources
            X = []
            for lag in range(1, self.max_lag + 1):
                X.append(data[:, self.max_lag-lag:-lag].T)
            X = np.hstack(X)  # Shape: (T-max_lag, n * max_lag)
            
            # Fit model
            model = Ridge(alpha=self.alpha)
            model.fit(X, Y)
            
            # Extract causal weights
            # Weight for neuron i → target at each lag
            for source in range(n):
                weights = []
                for lag in range(self.max_lag):
                    idx = lag * n + source
                    weights.append(np.abs(model.coef_[idx]))
                causal_matrix[source, target] = np.mean(weights)
        
        return causal_matrix
    
    def test_significance(self, data, n_permutations=100):
        """
        Test statistical significance via permutation
        """
        causal_matrix = self.infer_causality(data)
        null_dist = []
        
        for _ in range(n_permutations):
            # Shuffle time series
            shuffled = np.random.permutation(data.T).T
            null_causal = self.infer_causality(shuffled)
            null_dist.append(null_causal)
        
        # Compute p-values
        null_dist = np.array(null_dist)
        p_values = np.mean(causal_matrix < null_dist, axis=0)
        
        return causal_matrix, p_values
```

### Pathway Analysis

**Analysis:**
```python
def identify_pathways(causal_matrix, threshold=0.1):
    """
    Identify significant causal pathways
    """
    n = causal_matrix.shape[0]
    
    # Threshold
    significant = causal_matrix > threshold
    
    # Find paths (e.g., sensory → processing → motor)
    pathways = []
    for start in range(n):
        for end in range(n):
            if start != end:
                # Find paths via BFS/DFS
                paths = find_paths(significant, start, end)
                pathways.extend(paths)
    
    return pathways

def find_paths(adj_matrix, start, end, max_length=5):
    """
    Find all paths from start to end
    """
    paths = []
    stack = [(start, [start])]
    
    while stack:
        node, path = stack.pop()
        if node == end and len(path) > 1:
            paths.append(path)
        elif len(path) < max_length:
            for next_node in np.where(adj_matrix[node])[0]:
                if next_node not in path:
                    stack.append((next_node, path + [next_node]))
    
    return paths
```

## Comparison with Other Methods

| Method | Causality | Direction | Direct vs Indirect |
|--------|-----------|-----------|-------------------|
| Correlation | No | No | No |
| Granger Causality | Yes | Yes | Limited |
| Neuro-PC | Yes | Yes | Yes |

## Description

SKILL.md - Neuro-PC Causal Functional Connectivity

**Key Concepts:**
- Not just correlation, but causation
- X → Y means X influences Y's future state
- Captures direction and strength of influence

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Collect Neural Time Series

### Step 2: Preprocess Data

### Step 3: Apply Neuro-PC Algorithm

### Step 4: Infer Causal Graph

### Step 5: Validate and Interpret

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Neuro-PC Causal Functional Connectivity to my analysis.

**Agent:** I'll help you apply neuro-pc-causal-connectivity. First, let me understand your specific use case...

**Context:** Not just correlation, but causation

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for neuro-pc-causal-connectivity?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **ccep-causal-brain-network** - CCEP causal connectivity
- **time-varying-brain-connectivity** - Dynamic connectivity
- **task-aware-brain-connectivity** - Task-based connectivity

## Source

- arXiv:2011.03913v1
- Title: Neuro-PC: Causal Functional Connectivity from Neural Dynamics
- Utility: 0.87
- Authors: Rahul Biswas et al.

## Notes

- Key innovation: Causal inference from neural time series
- Goes beyond correlation to identify true causation
- Distinguishes direct from indirect connections
- Applications: neural circuit mapping, pathway identification
- Can infer sensory-motor-behavioral pathways
- More informative than standard functional connectivity

---

_Created: 2026-04-01_
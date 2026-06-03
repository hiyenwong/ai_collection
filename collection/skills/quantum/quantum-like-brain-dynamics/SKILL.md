---
name: quantum-like-brain-dynamics
description: "Quantum-like (QL) probability dynamics methodology for whole-brain modeling. Uses coupled oscillators to produce QL states that compute in a QL fashion, achieving better empirical neuroimaging fit with significantly lower energy consumption than non-QL networks. Applies quantum-like interference effects to human brain topology for advanced cognition modeling."
---

# Quantum-like Brain Dynamics

## Description

Quantum-like (QL) probability dynamics methodology for whole-brain modeling. Based on Deco et al. (2025), this approach uses coupled oscillators to produce QL states that compute in a QL fashion, achieving better empirical neuroimaging fit with significantly lower energy consumption than non-QL networks. The special topology of human brain anatomy together with QL bits promotes the rich dynamic repertoire necessary for human advanced cognition.

**Key Finding**: The QL regime provided the best whole-brain model fit to large-scale human empirical neuroimaging data, with significantly lower energy consumption than non-QL networks. The significantly larger whole-brain spectral gap induced by QL processing is a key signature of efficient brain dynamics.

**Source Paper**: "Quantum-like dynamics in the human brain" - Gustavo Deco, Yonatan Sanz Perl, Natasha Greenstein, Shamil Chandaria, Greg Scholes, Morten L. Kringelbach (bioRxiv, 2025)

## Activation Keywords

- quantum-like dynamics
- QL brain dynamics
- quantum-like probability
- whole-brain quantum-like
- coupled oscillator brain model
- spectral gap brain dynamics
- 量子似脑动力学
- quantum brain modeling
- efficient brain computation
- brain energy optimization

## Tools Used

- **exec**: Run coupled oscillator simulations, compute spectral gaps
- **read**: Load neuroimaging data, connectivity matrices
- **write**: Save model configurations, simulation results
- **web_search**: Find related papers, QL literature

## Core Concepts

### 1. Quantum-like (QL) Probability Laws
- QL states emerge from coupled oscillators even in non-quantum physical systems
- Interference effects produce QL probability distributions
- QL processing enables richer computational dynamics

### 2. Whole-Brain Coupled Oscillator Model
- Human brain anatomy topology serves as coupling structure
- Oscillators at each brain region interact via structural connectivity
- QL bits added to oscillator dynamics enable QL computation

### 3. Spectral Gap as Efficiency Signature
- The whole-brain spectral gap is significantly larger under QL processing
- Larger spectral gap correlates with lower energy consumption
- Spectral gap serves as key metric for model optimization

### 4. Energy Efficiency
- QL regime achieves optimal fit to empirical data
- At the QL optimum, energy consumption is significantly lower
- Trade-off: more complex dynamics, less energy required

## Instructions for Agents

### Step 1: Load Brain Connectivity Data
```python
# Load structural connectivity matrix (e.g., from HCP, ADNI)
# Shape: (N, N) where N = number of brain regions
import numpy as np
SC = np.loadtxt("structural_connectivity.csv", delimiter=",")
```

### Step 2: Configure Coupled Oscillator Model
```python
# Kuramoto-based coupled oscillators with QL extension
class QLCoupledOscillator:
    def __init__(self, n_regions, SC, ql_strength=0.5):
        self.n = n_regions
        self.SC = SC  # Structural connectivity
        self.ql_strength = ql_strength  # Quantum-like processing level
        self.phases = np.random.uniform(0, 2*np.pi, n_regions)
    
    def step(self, dt=0.01, K=1.0):
        """One integration step with QL coupling."""
        # Standard Kuramoto coupling
        coupling = K * self.SC @ np.sin(self.phases[:, None] - self.phases)
        
        # QL interference term
        ql_term = self.ql_strength * np.sin(2 * self.phases)  # QL interference
        
        dphases = coupling.mean(axis=1) + ql_term
        self.phases += dt * dphases
        return self.phases
    
    def spectral_gap(self):
        """Compute spectral gap of the coupled system."""
        # Laplacian of connectivity matrix
        L = np.diag(self.SC.sum(axis=1)) - self.SC
        eigenvalues = np.linalg.eigvalsh(L)
        # Spectral gap = difference between first two eigenvalues
        return eigenvalues[1] - eigenvalues[0]
```

### Step 3: Systematically Vary QL Processing Level
```python
# Sweep QL strength from 0 (classical) to 1 (full QL)
ql_levels = np.linspace(0, 1, 20)
results = []

for ql in ql_levels:
    model = QLCoupledOscillator(n_regions=SC.shape[0], SC=SC, ql_strength=ql)
    
    # Run simulation
    for _ in range(1000):
        model.step()
    
    # Compute metrics
    sg = model.spectral_gap()
    energy = compute_energy(model.phases)  # Define based on model
    fit = compute_fit_to_empirical(model.phases, empirical_data)
    
    results.append({"ql": ql, "spectral_gap": sg, "energy": energy, "fit": fit})
```

### Step 4: Find Optimal QL Regime
```python
# The optimal QL level maximizes fit to empirical data
# while minimizing energy consumption
import numpy as np

best_result = max(results, key=lambda r: r["fit"] / (r["energy"] + 1e-8))
optimal_ql = best_result["ql"]
optimal_spectral_gap = best_result["spectral_gap"]
```

### Step 5: Validate Against Empirical Data
```python
# Compare model output to fMRI/MEG data
# Metrics: functional connectivity correlation, power spectrum match
def validate_model(model_phases, empirical_fc):
    """Validate model against empirical functional connectivity."""
    model_fc = np.corrcoef(np.cos(model_phases), np.sin(model_phases))
    return np.corrcoef(model_fc.flatten(), empirical_fc.flatten())[0, 1]
```

## Usage Patterns

### Pattern 1: Whole-Brain QL Modeling
Use when modeling brain dynamics with quantum-like probability interference.

### Pattern 2: Energy-Efficient Brain Computation
Use when optimizing computational models for minimal energy consumption.

### Pattern 3: Spectral Gap Analysis
Use the spectral gap as a biomarker for efficient brain dynamics.

## Examples

### Example 1: Find Optimal QL Level for Brain Model
```
User: 用QL模型分析人脑结构连接数据，找到最优量子似处理水平

Agent Process:
1. Load structural connectivity matrix from dataset
2. Initialize QLCoupledOscillator with SC matrix
3. Sweep QL strength from 0 to 1 in 20 steps
4. For each level: simulate 1000 steps, compute spectral gap, energy, fit
5. Identify QL level with maximum fit-to-energy ratio
6. Report optimal QL level and its spectral gap value
```

### Example 2: Compare QL vs Classical Brain Dynamics
```
User: Compare quantum-like vs classical coupled oscillator models for brain dynamics

Agent Process:
1. Run two models: ql_strength=0 (classical) and ql_strength=optimal (QL)
2. Compare: functional connectivity fit, energy consumption, spectral gap
3. Generate side-by-side comparison table
4. Plot phase coherence distributions for both regimes
```

## Error Handling

### No Empirical Data Available
If empirical neuroimaging data is not available:
- Use synthetic data from known brain models
- Validate against published functional connectivity matrices
- Focus on relative comparisons between QL levels

### Spectral Gap Computation Fails
If the connectivity matrix is not positive semi-definite:
- Apply small regularization: L_reg = L + epsilon * I
- Use absolute values of negative eigenvalues

## Best Practices

1. **Start with Classical Baseline**: Always run with ql_strength=0 as baseline
2. **Systematic Sweeps**: Test at least 10-20 QL levels for robust results
3. **Multiple Metrics**: Track fit, energy, AND spectral gap simultaneously
4. **Cross-Validate**: Test on multiple subjects/datasets
5. **Reproducibility**: Fix random seeds for phase initialization

## Limitations

- QL dynamics are mathematical abstractions, not claims about quantum physics in the brain
- Requires structural connectivity data (DTI/MRI)
- Coupled oscillator model is a simplification of real neural dynamics
- Optimal QL level may vary across brain states (rest vs. task)

## Related Skills

- **kuramoto-brain-network**: Kuramoto oscillator modeling for brain networks
- **brain-network-controllability**: Structural brain network controllability analysis
- **energy-based-neurocomputation**: Energy-based dynamical systems for neuroscience

## Notes

- This skill captures the finding that QL probability dynamics in coupled oscillator models
  can better explain human brain dynamics than purely classical models.
- The "quantum-like" refers to mathematical interference effects, not actual quantum physics.
- The key insight is that QL processing leads to both better model fit AND lower energy cost.

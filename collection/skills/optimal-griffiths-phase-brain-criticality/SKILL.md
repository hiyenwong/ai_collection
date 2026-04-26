---
name: optimal-griffiths-phase-brain-criticality
description: "Optimal Griffiths Phase framework for brain criticality analysis. Extends standard criticality theory by identifying optimal Griffiths phases where structured heterogeneity in brain networks maximizes computational capabilities. Links structural heterogeneity to extended critical regimes, balancing robustness and adaptability. Activation: Griffiths phase, brain criticality, critical dynamics, heterogeneous network, optimal criticality, extended critical regime."
---

# Optimal Griffiths Phase Brain Criticality

> Identifies optimal Griffiths phases in brain networks where structured heterogeneity creates extended critical regimes that maximize computational capabilities, bridging network structure and critical dynamics.

## Metadata
- **Source**: arXiv:2512.03409
- **Authors**: S. Muñoz, M.A. Muñoz, L. Schimansky-Geier
- **Published**: 2025-12-04
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
The brain criticality debate traditionally focuses on whether the brain operates at a precise critical point. This work advances **Griffiths phase theory** for brain networks:
1. **Griffiths phases**: Extended regions of parameter space showing critical-like behavior, arising from network heterogeneity (not just a single point)
2. **Optimal Griffiths phase**: There exists a *specific level* of heterogeneity that maximizes computational properties
3. **Structure-dynamics link**: Topological features (degree distribution, modularity) determine the width and position of Griffiths phases

### Technical Framework

**Background: Griffiths Phases**
- In disordered systems, rare-region effects create extended semi-critical regimes
- Below percolation threshold but above the ordered phase
- Power-law distributions coexist with exponential cutoffs → "Griffiths phase"
- In brain networks: structural heterogeneity (degree, weight distributions) naturally creates Griffiths phases

**Optimal Heterogeneity Analysis**
1. **Network model**: Build brain-inspired networks with tunable heterogeneity (degree distribution exponent γ, weight disorder σ)
2. **Spreading dynamics**: Simulate SIS/SIR-like activity propagation on the network
3. **Order parameter**: Measure activity density ⟨ρ⟩ as function of control parameter λ
4. **Critical exponents**: Estimate from finite-size scaling; Griffiths phase shows non-universal exponents

**Key Equations**
- Activity density in Griffiths phase: ⟨ρ⟩ ~ L^(-β/ν) × f((λ - λc)L^(1/ν))
- With rare-region effects: τ_eff(λ) varies continuously — hallmark of Griffiths phase
- Optimal condition: maximize susceptibility χ = ∂⟨ρ⟩/∂λ over heterogeneity parameter

**Structural Predictors of Optimal Griffiths Phase**
- **Degree heterogeneity**: Broader degree distribution → wider Griffiths phase (up to a point)
- **Modular structure**: Inter-module coupling strength tunes Griffiths phase extent
- **Weight disorder**: Log-normal weight distributions with σ_opt ≈ 1-2 maximize computational range
- **Embedding dimension**: Spatial network constraints sharpen Griffiths boundaries

### Key Results
- Brain connectomes naturally sit in or near optimal Griffiths phases
- Too much heterogeneity → disordered (subcritical) behavior dominates
- Too little heterogeneity → narrow critical point, not Griffiths phase
- Optimal Griffiths phase maximizes: dynamic range, sensitivity, information transmission
- Consistent across human connectome (HCP), macaque, and C. elegans networks

## Implementation Guide

### Prerequisites
- Network data (adjacency matrix or connectome)
- Python: numpy, networkx, scipy for simulation
- Understanding of statistical physics (phase transitions, critical phenomena)

### Step-by-Step
1. **Construct network**: Load connectome or generate heterogeneous network
2. **Characterize heterogeneity**: Compute degree distribution, weight distribution, modularity
3. **Simulate dynamics**: Run SIS/SIR spreading with tunable infection rate λ
4. **Phase diagram**: Sweep λ and heterogeneity parameters
5. **Detect Griffiths phase**: Continuous variation of effective exponents
6. **Find optimum**: Maximize susceptibility or dynamic range over heterogeneity

### Code Example
```python
import numpy as np
import networkx as nx
from scipy import stats

def generate_heterogeneous_network(n, gamma, sigma_w, k_avg=10):
    # Generate network with power-law degree distribution (exponent gamma)
    # and log-normal weight distribution (log-std sigma_w).
    
    # Power-law degree sequence
    degrees = nx.utils.powerlaw_sequence(n, exponent=gamma)
    degrees = np.round(degrees / np.mean(degrees) * k_avg).astype(int)
    degrees = np.maximum(degrees, 1)  # minimum degree 1
    
    # Configuration model
    G = nx.configuration_model(degrees.tolist())
    G = nx.Graph(G)  # remove multi-edges
    G.remove_edges_from(nx.selfloop_edges(G))
    
    # Log-normal weights
    weights = {}
    for u, v in G.edges():
        w = np.random.lognormal(mean=0.0, sigma=sigma_w)
        weights[(u, v)] = w
    nx.set_edge_attributes(G, weights, 'weight')
    
    return G

def sis_griffiths_simulation(G, lambda_range, n_steps=5000, transient=2000):
    # SIS dynamics on network to detect Griffiths phase.
    n = G.number_of_nodes()
    adj = nx.to_numpy_array(G)
    
    results = {}
    for lam in lambda_range:
        # Initialize: small fraction active
        state = np.zeros(n, dtype=int)
        state[np.random.choice(n, max(1, n//10), replace=False)] = 1
        
        density_history = []
        for t in range(n_steps):
            new_state = state.copy()
            for i in range(n):
                if state[i] == 1:  # Infected → recover with rate 1
                    if np.random.random() < 1.0 / (n_steps / 100):
                        new_state[i] = 0
                else:  # Susceptible → infect with rate λ × (weighted infected neighbors)
                    infected_input = lam * np.sum(adj[i] * state)
                    if np.random.random() < 1 - np.exp(-infected_input / (n_steps / 100)):
                        new_state[i] = 1
            state = new_state
            if t > transient:
                density_history.append(np.mean(state))
        
        results[lam] = {
            'density': np.mean(density_history),
            'density_std': np.std(density_history),
            'density_history': density_history
        }
    
    return results

def compute_susceptibility(results, lambda_range):
    # Compute susceptibility d<rho>/d(lambda).
    densities = [results[lam]['density'] for lam in lambda_range]
    susceptibility = np.gradient(densities, lambda_range)
    return susceptibility

def find_optimal_heterogeneity(n_nodes=200, gamma_range=(2.1, 4.0), 
                                 sigma_range=(0.1, 3.0), lambda_range=None):
    # Sweep heterogeneity parameters to find optimal Griffiths phase.
    if lambda_range is None:
        lambda_range = np.linspace(0.01, 5.0, 50)
    
    gammas = np.linspace(*gamma_range, num=8)
    sigmas = np.linspace(*sigma_range, num=8)
    
    best = {'chi_max': 0, 'gamma': None, 'sigma': None}
    
    for gamma in gammas:
        for sigma in sigmas:
            G = generate_heterogeneous_network(n_nodes, gamma, sigma)
            results = sis_griffiths_simulation(G, lambda_range)
            chi = compute_susceptibility(results, lambda_range)
            chi_max = np.max(chi)
            
            if chi_max > best['chi_max']:
                best.update({'chi_max': chi_max, 'gamma': gamma, 'sigma': sigma})
    
    return best
```

## Applications
- **Brain criticality assessment**: Determine if connectome operates in Griffiths phase
- **Network design**: Engineer optimal heterogeneity for neuromorphic systems
- **Disorder biomarkers**: Abnormal Griffiths phase → psychiatric/neurological conditions
- **Drug response prediction**: Neuromodulation shifts system within Griffiths phase
- **Anesthesia monitoring**: Track transition out of Griffiths phase during sedation

## Pitfalls
- Finite-size effects strongly affect Griffiths phase detection
- Distinguishing Griffiths phase from true criticality requires very large systems
- SIS dynamics is a simplified model; real neural dynamics are more complex
- Network construction method affects heterogeneity measures
- Optimal heterogeneity may differ across brain regions

## Related Skills
- griffiths-phase-brain-criticality
- neural-critical-dynamics-theory
- brain-state-transition-network-control
- neutral-theory-neural-dynamics
- neural-code-dynamics-analysis

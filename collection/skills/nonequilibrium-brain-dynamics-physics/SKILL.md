---
title: Nonequilibrium Physics of Brain Dynamics
name: nonequilibrium-brain-dynamics-physics
category: ai_collection
description: Comprehensive review of nonequilibrium physics in neuroscience. Analyzes time-irreversibility, entropy production, and broken detailed balance in neural dynamics as signatures of cognitive complexity and consciousness.
arXiv_id: 2504.12188
author: Ramón Nartallo-Kaluarachchi, Morten L. Kringelbach, Gustavo Deco, Renaud Lambiotte, Alain Goriely
date: 2026
venue: Physics Reports (2026), Vol 1152, Pages 1-43
---

# Nonequilibrium Physics of Brain Dynamics

## Overview

Comprehensive review (Physics Reports 2026) covering nonequilibrium dynamics in neuroscience. The brain operates in a nonequilibrium stationary state with time-irreversible dynamics and broken detailed balance. The level of nonequilibrium, measured by entropy production or irreversibility, appears to be a crucial signature of cognitive complexity and consciousness.

## Core Concepts

### 1. Nonequilibrium Signatures in Neural Dynamics

**Time-Irreversibility**: 
- Forward trajectory probability ≠ Backward trajectory probability
- P[x(t)] ≠ P[x(-t)]

**Broken Detailed Balance**:
- Transition rates violate: P(i→j)/P(j→i) ≠ P(j)/P(i)
- Indicates active energy consumption

**Entropy Production**:
- Quantifies distance from equilibrium
- Related to thermodynamic efficiency

```python
import numpy as np
from scipy import stats

class NonequilibriumAnalyzer:
    """
    Analyze nonequilibrium properties of neural dynamics
    """
    def __init__(self, data):
        """
        Args:
            data: Neural recordings [time, neurons]
        """
        self.data = data
        self.n_time, self.n_neurons = data.shape
        
    def time_irreversibility_index(self, tau=1):
        """
        Compute time-irreversibility index
        
        Measures asymmetry between forward and backward trajectories
        
        I = ⟨[x(t+τ) - x(t)]³⟩ / ⟨[x(t+τ) - x(t)]²⟩^(3/2)
        
        Args:
            tau: Time lag
        
        Returns:
            index: Irreversibility index (0 = reversible)
        """
        # Compute increments
        increments = self.data[tau:] - self.data[:-tau]
        
        # Third moment (skewness)
        third_moment = np.mean(increments**3, axis=0)
        
        # Second moment (variance)
        second_moment = np.mean(increments**2, axis=0)
        
        # Irreversibility index
        index = third_moment / (second_moment**(3/2) + 1e-10)
        
        return index
    
    def entropy_production_rate(self, method='kde', bins=50):
        """
        Estimate entropy production rate from data
        
        σ = ∫ dx [J(x)/P(x)]² D(x) P(x)
        
        where J is probability current, D is diffusion coefficient
        """
        if method == 'histogram':
            return self._ep_histogram(bins)
        elif method == 'kde':
            return self._ep_kde()
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def _ep_histogram(self, bins):
        """Entropy production via histogram method"""
        # Discretize state space
        hist, edges = np.histogramdd(self.data, bins=bins)
        
        # Compute transitions
        transitions = np.zeros((bins, bins))
        for t in range(len(self.data) - 1):
            # Find bins for current and next state
            i = np.digitize(self.data[t], edges[0]) - 1
            j = np.digitize(self.data[t+1], edges[0]) - 1
            
            if 0 <= i < bins and 0 <= j < bins:
                transitions[i, j] += 1
                
        # Normalize to get transition probabilities
        row_sums = transitions.sum(axis=1, keepdims=True)
        P = transitions / (row_sums + 1e-10)
        
        # Stationary distribution
        pi = hist / hist.sum()
        
        # Entropy production: Σ π_i P_ij ln(P_ij / P_ji)
        ep = 0
        for i in range(bins):
            for j in range(bins):
                if P[i,j] > 0 and P[j,i] > 0:
                    ep += pi[i] * P[i,j] * np.log(P[i,j] / P[j,i])
                    
        return ep
    
    def detailed_balance_violation(self):
        """
        Measure detailed balance violation
        
        Returns violation score and which transitions break DB
        """
        # Estimate transition matrix
        from sklearn.neighbors import KernelDensity
        
        # Fit KDE for probability estimation
        kde = KernelDensity(bandwidth=0.1).fit(self.data)
        
        # Compute log probabilities
        log_prob = kde.score_samples(self.data)
        prob = np.exp(log_prob)
        
        # Estimate pairwise transitions
        n = len(self.data)
        violations = []
        
        for i in range(n-1):
            for j in range(i+1, n):
                # P(i→j) vs P(j→i)
                # Simplified: use distance-based estimates
                d_ij = np.linalg.norm(self.data[i+1] - self.data[i])
                d_ji = np.linalg.norm(self.data[i] - self.data[i+1])
                
                if prob[i] > 0 and prob[j] > 0:
                    ratio = (d_ji / d_ij) * (prob[j] / prob[i])
                    if abs(np.log(ratio)) > 0.1:  # Threshold
                        violations.append((i, j, np.log(ratio)))
                        
        return {
            'violation_score': len(violations) / (n * (n-1) / 2),
            'violations': violations
        }

    def compute_kolmogorov_entropy(self, embedding_dim=3, delay=1):
        """
        Compute Kolmogorov-Sinai entropy rate
        
        Measures dynamical complexity and unpredictability
        """
        from nolitsa import entropy
        
        # Embed time series
        embedded = self._embed(self.data[:, 0], embedding_dim, delay)
        
        # Compute KS entropy
        ks_entropy = entropy.sampen(embedded, order=embedding_dim)
        
        return ks_entropy
    
    def _embed(self, x, dim, delay):
        """Time-delay embedding"""
        N = len(x) - (dim - 1) * delay
        embedded = np.zeros((N, dim))
        for i in range(dim):
            embedded[:, i] = x[i*delay : i*delay + N]
        return embedded
```

### 2. Continuous State-Space Analysis

```python
class ContinuousStateAnalysis:
    """
    Analyze nonequilibrium dynamics in continuous state space
    
    Based on Fokker-Planck equation analysis
    """
    def __init__(self, trajectories, dt=0.01):
        self.trajectories = trajectories
        self.dt = dt
        
    def estimate_drift_diffusion(self, method='local'):
        """
        Estimate drift and diffusion coefficients
        
        dx = D^(1)(x)dt + √(2D^(2)(x))dW
        """
        if method == 'local':
            return self._local_estimation()
        elif method == 'global':
            return self._global_estimation()
            
    def _local_estimation(self, n_bins=50):
        """Local linear estimation of drift and diffusion"""
        x = self.trajectories
        
        # Bin the data
        x_min, x_max = x.min(), x.max()
        bins = np.linspace(x_min, x_max, n_bins)
        
        drift = np.zeros(n_bins - 1)
        diffusion = np.zeros(n_bins - 1)
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        
        for i in range(n_bins - 1):
            mask = (x[:-1] >= bins[i]) & (x[:-1] < bins[i+1])
            
            if mask.sum() > 10:  # Enough samples
                dx = x[1:][mask] - x[:-1][mask]
                
                # Kramers-Moyal coefficients
                drift[i] = np.mean(dx) / self.dt
                diffusion[i] = np.var(dx) / (2 * self.dt)
                
        return {
            'drift': drift,
            'diffusion': diffusion,
            'bin_centers': bin_centers
        }
    
    def compute_entropy_production_functional(self, drift, diffusion, stationary_dist):
        """
        Compute entropy production using functional approach
        
        σ = ∫ dx [D^(1)(x) - D^(2)(x) ∂_x ln P_s(x)]² / D^(2)(x) * P_s(x)
        """
        integrand = (
            (drift - diffusion * np.gradient(np.log(stationary_dist)))**2 
            / diffusion * stationary_dist
        )
        
        # Integrate
        sigma = np.trapz(integrand)
        
        return sigma
    
    def fluctuation_theorem_check(self, trajectories, time_window):
        """
        Verify fluctuation theorems
        
        Checks if P(ΔS = A) / P(ΔS = -A) = exp(A)
        """
        # Compute entropy changes over windows
        entropy_changes = []
        
        for i in range(0, len(trajectories) - time_window, time_window):
            window = trajectories[i:i+time_window]
            
            # Estimate entropy change (simplified)
            # In practice, use more sophisticated methods
            ds = np.sum(np.gradient(window)**2) * self.dt
            entropy_changes.append(ds)
            
        entropy_changes = np.array(entropy_changes)
        
        # Check fluctuation relation
        A_values = np.linspace(0, np.max(np.abs(entropy_changes)), 50)
        ratios = []
        
        for A in A_values:
            p_pos = np.mean(np.abs(entropy_changes - A) < 0.1)
            p_neg = np.mean(np.abs(entropy_changes + A) < 0.1)
            
            if p_neg > 0:
                ratios.append(np.log(p_pos / p_neg))
            else:
                ratios.append(np.nan)
                
        return {
            'entropy_changes': entropy_changes,
            'A_values': A_values,
            'log_ratios': ratios,
            'theorem_satisfied': np.allclose(ratios[~np.isnan(ratios)], A_values[~np.isnan(ratios)], rtol=0.2)
        }
```

### 3. Discrete State-Space (Spike Trains)

```python
class SpikeTrainNonequilibrium:
    """
    Analyze nonequilibrium properties in spike train data
    """
    def __init__(self, spike_trains, bin_size=0.01):
        """
        Args:
            spike_trains: List of spike times for each neuron
            bin_size: Bin size for discretization (seconds)
        """
        self.spike_trains = spike_trains
        self.bin_size = bin_size
        self.n_neurons = len(spike_trains)
        
    def spike_train_entropy_production(self):
        """
        Compute entropy production rate for spike trains
        
        Uses discrete Markov chain approximation
        """
        # Bin spike trains
        binned = self._bin_spike_trains()
        
        # Estimate transition matrix
        transition_matrix = self._estimate_transitions(binned)
        
        # Stationary distribution
        stationary = self._stationary_distribution(transition_matrix)
        
        # Entropy production
        ep = 0
        for i in range(len(stationary)):
            for j in range(len(stationary)):
                if transition_matrix[i,j] > 0 and transition_matrix[j,i] > 0:
                    ep += (stationary[i] * transition_matrix[i,j] - 
                           stationary[j] * transition_matrix[j,i]) * \
                          np.log(transition_matrix[i,j] / transition_matrix[j,i])
                          
        return ep / self.bin_size  # Rate per second
    
    def _bin_spike_trains(self, duration=None):
        """Convert spike times to binary matrix"""
        if duration is None:
            duration = max(max(st) for st in self.spike_trains if len(st) > 0)
            
        n_bins = int(duration / self.bin_size) + 1
        binned = np.zeros((self.n_neurons, n_bins))
        
        for i, spikes in enumerate(self.spike_trains):
            bins = (np.array(spikes) / self.bin_size).astype(int)
            bins = bins[bins < n_bins]
            binned[i, bins] = 1
            
        return binned
    
    def spike_time_irreversibility(self):
        """
        Compute time-irreversibility specifically for spike trains
        
        Uses ISI (inter-spike interval) statistics
        """
        all_isi = []
        
        for spikes in self.spike_trains:
            if len(spikes) > 1:
                isi = np.diff(spikes)
                all_isi.extend(isi)
                
        all_isi = np.array(all_isi)
        
        # Irreversibility: asymmetry in ISI distribution
        skewness = stats.skew(all_isi)
        
        return skewness
    
    def neural_thermodynamic_efficiency(self, input_energy):
        """
        Estimate thermodynamic efficiency of neural computation
        
        η = (useful_work) / (energy_input)
        
        Args:
            input_energy: Estimated energy input rate
        """
        # Entropy production as proxy for work
        ep = self.spike_train_entropy_production()
        
        # Efficiency (very rough estimate)
        efficiency = ep / input_energy if input_energy > 0 else 0
        
        return efficiency
```

## Cognitive Complexity Signatures

### Consciousness and Nonequilibrium

```python
class ConsciousnessSignatures:
    """
    Analyze relationship between nonequilibrium and consciousness
    
    Based on review findings:
    - Higher entropy production in conscious states
    - Time-irreversibility correlates with awareness
    """
    def __init__(self, awake_data, anesthesia_data, sleep_data):
        self.data = {
            'awake': awake_data,
            'anesthesia': anesthesia_data,
            'sleep': sleep_data
        }
        
    def compare_nonequilibrium_levels(self):
        """
        Compare nonequilibrium measures across states
        """
        results = {}
        
        for state, data in self.data.items():
            analyzer = NonequilibriumAnalyzer(data)
            
            results[state] = {
                'entropy_production': analyzer.entropy_production_rate(),
                'time_irreversibility': np.mean(analyzer.time_irreversibility_index()),
                'detailed_balance_violation': analyzer.detailed_balance_violation()['violation_score']
            }
            
        return results
    
    def consciousness_classifier(self, threshold_dict):
        """
        Classify consciousness state based on nonequilibrium metrics
        """
        def classify(data):
            analyzer = NonequilibriumAnalyzer(data)
            
            ep = analyzer.entropy_production_rate()
            ti = np.mean(analyzer.time_irreversibility_index())
            
            if ep > threshold_dict['high_ep'] and abs(ti) > threshold_dict['high_ti']:
                return 'awake/conscious'
            elif ep < threshold_dict['low_ep']:
                return 'deep_sleep/anesthesia'
            else:
                return 'intermediate'
                
        return classify
```

## Model-Based Approaches

### Nonequilibrium Neural Mass Models

```python
class NonequilibriumNeuralMass:
    """
    Neural mass model with explicit nonequilibrium dynamics
    
    Extended Jansen-Rit or Wendling models with thermodynamic terms
    """
    def __init__(self, params):
        self.params = params
        
    def simulate(self, duration, dt=0.001):
        """
        Simulate nonequilibrium neural mass dynamics
        """
        n_steps = int(duration / dt)
        
        # State variables: excitatory, inhibitory, pyramidal
        y = np.zeros((3, n_steps))
        
        # Add nonequilibrium forcing (non-conservative)
        for t in range(1, n_steps):
            # Standard neural mass dynamics
            dy = self._neural_mass_dynamics(y[:, t-1])
            
            # Add nonequilibrium term (energy input)
            noneq_term = self._nonequilibrium_forcing(y[:, t-1], t*dt)
            
            y[:, t] = y[:, t-1] + dt * (dy + noneq_term)
            
        return y
    
    def _neural_mass_dynamics(self, y):
        """Standard neural mass ODEs"""
        # Simplified Jansen-Rit type equations
        dy = np.zeros(3)
        
        # Excitatory population
        dy[0] = y[2]
        dy[1] = -2 * self.params['a'] * y[2] - self.params['a']**2 * y[0] + \
                self.params['A'] * self.params['a'] * self._sigmoid(y[1] - y[2])
        
        # Similar for others...
        
        return dy
    
    def _nonequilibrium_forcing(self, y, t):
        """Non-conservative forcing for nonequilibrium"""
        # Time-asymmetric forcing
        forcing = self.params['noneq_amplitude'] * np.sin(2 * np.pi * self.params['f'] * t)
        
        return np.array([forcing, 0, 0])
```

## Key Findings from Review

1. **Entropy Production and Cognition**: Higher entropy production correlates with:
   - Conscious awareness
   - Cognitive complexity
   - Task engagement

2. **Time-Irreversibility**: Strong signature of:
   - Active information processing
   - Energy consumption
   - Non-passive neural states

3. **Broken Detailed Balance**: Indicates:
   - Metabolic activity
   - Directed information flow
   - Functional hierarchy

## Implementation Guide

```python
def full_nonequilibrium_analysis(neural_data, sampling_rate=1000):
    """
    Complete nonequilibrium analysis pipeline
    
    Args:
        neural_data: [time, channels] neural recordings
        sampling_rate: Sampling rate in Hz
    
    Returns:
        comprehensive analysis results
    """
    dt = 1.0 / sampling_rate
    analyzer = NonequilibriumAnalyzer(neural_data)
    
    # Core measures
    results = {
        'time_irreversibility': analyzer.time_irreversibility_index(),
        'entropy_production': analyzer.entropy_production_rate(),
        'detailed_balance': analyzer.detailed_balance_violation(),
        'kolmogorov_entropy': analyzer.compute_kolmogorov_entropy()
    }
    
    # State classification
    if results['entropy_production'] > 0.5:
        results['state'] = 'highly_nonequilibrium'
    elif results['entropy_production'] > 0.1:
        results['state'] = 'moderately_nonequilibrium'
    else:
        results['state'] = 'near_equilibrium'
        
    return results
```

## References

- Paper: "Nonequilibrium physics of brain dynamics" (arXiv:2504.12188)
- Authors: Ramón Nartallo-Kaluarachchi, Morten L. Kringelbach, Gustavo Deco, Renaud Lambiotte, Alain Goriely
- Venue: Physics Reports (2026), Vol 1152, Pages 1-43
- DOI: 10.1016/j.physrep.2025.10.003

## Trigger Words
- nonequilibrium brain dynamics, entropy production neuroscience, time-irreversible neural dynamics, broken detailed balance brain, cognitive complexity thermodynamics, consciousness entropy production, neural fluctuation theorems
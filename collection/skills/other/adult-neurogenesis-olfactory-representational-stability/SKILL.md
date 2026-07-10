---
name: adult-neurogenesis-olfactory-representational-stability
description: Adult-neurogenesis dual role methodology — spiking network model showing how continuous addition of new neurons supports both odor representational stability and flexibility in olfactory circuits.
tags: [neuroscience, neurogenesis, olfactory-system, representational-drift, spiking-network, computational-neuroscience, plasticity, neural-coding, brain-network]
created: 2026-05-27
source: "DOI: 10.7554/eLife.107905 | PMID: 42112574"
---

# Adult-Neurogenesis Allows for Representational Stability and Flexibility in Early Olfactory System

## Overview

This methodology from Chen & Padmanabhan (eLife, 2026) uses a **detailed spiking network model of early olfactory circuits** to reveal how adult neurogenesis (continuous addition of new neurons throughout life) simultaneously enables two seemingly opposing properties:

1. **Representational stability**: faithful odor encoding at the population level
2. **Representational flexibility/drift**: experience-dependent plasticity and learning

The model covers two major olfactory processing stages with distinct computational roles.

## Core Model Architecture

### Stage 1: Main Olfactory Bulb (MOB)
- Adult neurogenesis affects **individual cell responses** but **preserves population-level representations**
- New neurons (granule cells) provide inhibitory interneuron replacement
- Net effect: individual mitral/tufted cells shift, but population code remains robust
- Mechanism: lateral inhibition redistribution via new granule cells

### Stage 2: Piriform Cortex (PCx)
- Both individual cell responses AND population dynamics undergo progressive change
- **Representational drift**: stimulus-evoked activity patterns gradually change
- Drift rate is experience-dependent — repeated odor exposure reduces drift
- Implements a form of temporal context coding

## Key Findings

1. **MOB preserves population code**: Even as individual neurons are replaced/rewired, the high-dimensional population vector representation of each odor remains stable
2. **PCx implements representational drift**: The cortex continuously updates its odor representations — encoding not just *what* but *when*
3. **Experience protects stability**: Frequently encountered odors have more stable representations (reduced drift)
4. **Dual functional role**: Same neurogenesis process serves both stability (MOB) and flexibility (PCx) via different circuit mechanisms

## Spiking Network Model

```python
import numpy as np
from typing import List, Tuple

class OlfactoryBulbModel:
    """Simplified spiking network model of main olfactory bulb."""
    
    def __init__(self, n_glomeruli=200, n_mitral=200, n_granule=1000,
                 neurogenesis_rate=0.01):
        self.n_glom = n_glomeruli
        self.n_mitral = n_mitral
        self.n_granule = n_granule
        self.neurogenesis_rate = neurogenesis_rate  # Fraction replaced per day
        
        # Connectivity matrices
        self.W_olf_mitral = np.random.randn(n_mitral, n_glomeruli) * 0.1
        self.W_granule_mitral = np.random.randn(n_mitral, n_granule) * 0.05
        self.W_mitral_granule = np.random.randn(n_granule, n_mitral) * 0.05
        
        # Neuron properties
        self.tau_m = 20e-3   # Membrane time constant (s)
        self.V_rest = -65.0  # Resting potential (mV)
        self.V_thresh = -50.0  # Spike threshold (mV)
        
    def apply_neurogenesis(self, n_replace=None):
        """Replace a fraction of granule cells with new neurons."""
        if n_replace is None:
            n_replace = int(self.n_granule * self.neurogenesis_rate)
        
        replace_idx = np.random.choice(self.n_granule, n_replace, replace=False)
        
        # New neurons have weak, random connections (not yet integrated)
        self.W_granule_mitral[:, replace_idx] = np.random.randn(self.n_mitral, n_replace) * 0.01
        self.W_mitral_granule[replace_idx, :] = np.random.randn(n_replace, self.n_mitral) * 0.01
        
        return replace_idx
    
    def simulate_response(self, odor_input, dt=0.1e-3, duration=0.5):
        """Simulate network response to odor stimulus using LIF neurons."""
        n_steps = int(duration / dt)
        
        V_mitral = np.ones(self.n_mitral) * self.V_rest
        V_granule = np.ones(self.n_granule) * self.V_rest
        
        spikes_mitral = np.zeros((n_steps, self.n_mitral))
        
        for t in range(n_steps):
            # Feedforward from glomeruli
            I_ff = self.W_olf_mitral @ odor_input
            
            # Lateral inhibition from granule cells
            I_inh = self.W_granule_mitral @ (V_granule > self.V_thresh).astype(float)
            
            # Update mitral cell voltages
            dV_m = (-(V_mitral - self.V_rest) + I_ff - I_inh) / self.tau_m * dt
            V_mitral += dV_m
            
            # Spike detection and reset
            fired = V_mitral >= self.V_thresh
            spikes_mitral[t] = fired
            V_mitral[fired] = self.V_rest
            
            # Update granule cells
            I_exc = self.W_mitral_granule @ fired.astype(float)
            dV_g = (-(V_granule - self.V_rest) + I_exc) / self.tau_m * dt
            V_granule += dV_g
        
        return spikes_mitral
    
    def population_vector(self, spikes, time_window=0.1):
        """Compute population firing rate vector for odor representation."""
        return np.mean(spikes[-int(time_window / 0.1e-3):], axis=0)


class RepresentationalDriftAnalysis:
    """Analyze representational drift across neurogenesis events."""
    
    @staticmethod
    def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
        """Compute cosine similarity between two population vectors."""
        norm1, norm2 = np.linalg.norm(v1), np.linalg.norm(v2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return np.dot(v1, v2) / (norm1 * norm2)
    
    @staticmethod
    def measure_drift(representations: List[np.ndarray]) -> np.ndarray:
        """Measure drift over time as cosine distance from initial representation."""
        initial = representations[0]
        return np.array([
            1 - RepresentationalDriftAnalysis.cosine_similarity(initial, r)
            for r in representations
        ])
    
    @staticmethod
    def experience_dependent_protection(model, odor, n_exposures=50,
                                        neurogenesis_per_day=10):
        """
        Simulate repeated odor exposure and measure drift reduction.
        
        Returns drift trajectory with vs without repeated exposure.
        """
        # Baseline: no experience
        reps_naive = []
        for _ in range(20):
            model.apply_neurogenesis(neurogenesis_per_day)
            spikes = model.simulate_response(odor)
            reps_naive.append(model.population_vector(spikes))
        
        # Reset model
        model2 = OlfactoryBulbModel()
        reps_experienced = []
        for day in range(20):
            model2.apply_neurogenesis(neurogenesis_per_day)
            # Repeated odor exposure strengthens synapses (Hebbian)
            if day % 2 == 0:  # Exposure every other day
                for _ in range(n_exposures):
                    spikes = model2.simulate_response(odor)
                    # Hebbian plasticity: strengthen connections for this odor
                    pvec = model2.population_vector(spikes)
                    model2.W_olf_mitral += 0.001 * np.outer(pvec, odor)
            
            spikes = model2.simulate_response(odor)
            reps_experienced.append(model2.population_vector(spikes))
        
        naive_drift = RepresentationalDriftAnalysis.measure_drift(reps_naive)
        exp_drift = RepresentationalDriftAnalysis.measure_drift(reps_experienced)
        return naive_drift, exp_drift
```

## When to Use

- Modeling adult neurogenesis effects in hippocampus, olfactory bulb, or cortex
- Studying representational drift in sensory systems
- Building computational models of learning-induced circuit changes
- Understanding how biological neural networks balance stability and plasticity
- Modeling olfactory system computations (odor discrimination, recognition)
- Continual learning in artificial neural networks inspired by neurogenesis

## Key Insights for AI Systems

| Biological Principle | AI Application |
|---------------------|----------------|
| MOB population stability | Ensemble methods for stable feature representations |
| PCx representational drift | Temporal context encoding in sequence models |
| Experience-dependent protection | Rehearsal/replay in continual learning |
| Neurogenesis turnover | Growing neural networks, neuron dropout/replacement |

## Pitfalls

- Neurogenesis rate is species/region-specific (mice: ~1-2% granule cells/day in OB)
- New neuron integration time (weeks) must be modeled for accurate drift dynamics
- Model granularity (single neuron vs. population) affects stability predictions
- Experience-dependent stabilization requires realistic exposure statistics

## Parameters

| Parameter | Description | Biological Value |
|-----------|-------------|-----------------|
| Neurogenesis rate | Fraction cells replaced/day | 0.5–2% (OB granule) |
| Integration time | New neuron maturation | 2–4 weeks |
| Drift timescale | Days to weeks for PCx drift | Weeks–months |
| Stabilization threshold | Exposures to protect representation | 20–100 |

## References

- Chen Z, Padmanabhan K. "Adult-neurogenesis allows for representational stability and flexibility in early olfactory system." *eLife*, 2026. DOI: 10.7554/eLife.107905
- Bhattacharya S, Bhattacharya S. "Olfactory bulb granule cells: New neurons in an old circuitry." *Progress in Neurobiology*, 2020.
- Rangel LM et al. "Temporally selective contextual encoding in the dentate gyrus of the hippocampus." *Nature Communications*, 2016.

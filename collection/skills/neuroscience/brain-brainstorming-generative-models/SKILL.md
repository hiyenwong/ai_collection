---
name: brain-brainstorming-generative-models
description: Generative models for brain "brainstorming" — studying the brain's spontaneous idea generation using free energy principle, critical dynamics, and default mode network analysis. Based on Smith et al. (2026) linking neural criticality, predictive coding, and spontaneous thought patterns. Triggers: brain brainstorming, spontaneous thought, neural idea generation, predictive coding creativity, free energy imagination, default mode network generative, 脑风暴生成模型, 自发思维生成
version: 1.0.0
metadata:
  hermes:
    source_paper: "Brainstorming in the Brain: A Generative Model of Spontaneous Idea Generation (arXiv:2604.14080)"
    authors: "Rory J. Smith, Ziyang Li, Thomas P. O'Dwyer, Andrea Alamino"
    date: "2026-04-15"
    category: "cs.AI"
    tags: [spontaneous-thought, free-energy-principle, default-mode-network, generative-modeling, creativity, critical-dynamics]
---

# Brain Brainstorming — Generative Models of Spontaneous Thought

## Overview

A formal generative model of spontaneous thought ("brainstorming") in the brain, using the free energy principle as a unifying framework. Spontaneous thought arises from the interaction of the default mode network (DMN) with other large-scale brain networks through critical dynamics.

## Core Framework

### Free Energy Principle Applied to Thought

The brain maintains an internal generative model p(o,s) over observations o and hidden states s. Free energy F bounds surprise:

F = D_KL[q(s)||p(s|o)] - log p(o)

During spontaneous thought, the brain minimizes free energy over internally generated observations, enabling imagination without external input.

### Key Hypothesis

Brainstorming operates near criticality — a phase transition point where:
- Network activity shows power-law distributed avalanches
- Information capacity is maximized
- Novel associations emerge from balanced excitation-inhibition

## Implementation Pattern

```python
class BrainstormModel:
    """Generative model of spontaneous thought via critical dynamics."""

    def __init__(self, n_regions, n_hidden=64):
        self.n_regions = n_regions  # Brain regions (DMN + others)

        # Generative model parameters
        self.A = np.random.randn(n_regions, n_hidden)  # Likelihood matrix
        self.B = np.eye(n_hidden)  # Transition dynamics
        self.C = np.zeros(n_regions)  # Prior preferences

        # Critical dynamics parameters
        self.coupling = 1.0  # Near critical: ~1.0
        self.noise_scale = 0.1

    def spontaneous_thought(self, t_steps=100, temperature=1.0):
        """Generate spontaneous thought patterns via sampling."""
        states = np.random.randn(t_steps, self.n_hidden)

        for t in range(1, t_steps):
            # Transition dynamics (predictive coding)
            predicted = self.B @ states[t-1]

            # Critical branching: balance between amplification and decay
            noise = np.random.randn(self.n_hidden) * self.noise_scale
            states[t] = self.coupling * predicted + noise * temperature

        # Decode to "thoughts" (observable patterns)
        thoughts = states @ self.A.T
        return thoughts

    def detect_criticality(self, activity):
        """Test if network operates near critical point."""
        # Avalanche size distribution
        thresholds = np.percentile(activity, [50, 75, 90])
        avalanche_sizes = []

        for thresh in thresholds:
            above = activity > thresh
            # Find contiguous regions above threshold
            sizes = self._measure_avalanches(above)
            avalanche_sizes.extend(sizes)

        # Power-law fit: P(s) ~ s^(-alpha)
        alpha = self._fit_power_law(avalanche_sizes)
        is_critical = 1.5 < alpha < 2.5  # Critical range
        return is_critical, alpha
```

## Applications

- **AI creativity models**: Design generative models inspired by spontaneous brain dynamics
- **DMN analysis**: Study default mode network activity patterns in resting-state fMRI
- **Mind-wandering research**: Model the neural basis of spontaneous thought and creativity
- **Mental health**: Understand altered spontaneous thought in depression, ADHD, schizophrenia

## Related Skills

- energy-based-neurocomputation
- neural-dynamics-decision-making
- neural-population-dynamics

## Activation Keywords

- brainstorming in the brain
- spontaneous thought model
- free energy principle creativity
- default mode network generative
- neural criticality idea generation
- mind wandering model

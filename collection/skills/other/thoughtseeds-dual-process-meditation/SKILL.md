---
name: thoughtseeds-dual-process-meditation
description: "A computational phenomenology framework for modeling focused-attention meditation using dual-process active inference and hierarchical Markov-blanket architecture. Use when modeling meditation states, attentional dynamics, or cognitive phenomenology with latent mental content representations."
metadata:
  arxiv_id: "2607.14833"
  authors: ["Prakash Chandra Kavi", "Daniel Ari Friedman", "Gustavo Patow"]
  subjects: ["Neurons and Cognition (q-bio.NC)"]
---

# Thoughtseeds Dual Process Meditation Skill

This skill implements the computational phenomenology framework from arXiv:2607.14833 for modeling focused-attention meditation as a dual-process active inference system with hierarchical Markov-blanket architecture.

## Core Methodology

The model implements a three-layer nested Markov-blanket architecture:

1. **L1 - Physiological Neuronal Substrate**: High-dimensional neuronal activity modeled as a stochastic multivariate Ornstein--Uhlenbeck process over attentional Yeo networks
2. **L2 - Low-dimensional Generative Model (System 1)**: Encodes latent mental content as "thoughtseeds" and evaluates autonomic action tendencies
3. **L3 - Agentic Metacognitive Monitor (System 2)**: Implements a Global Neuronal Workspace (GNW) capacity bottleneck to selectively gate these tendencies

Key mechanisms:
- Meta-awareness functions as the GNW ignition signal, derived from policy-prior divergence
- Direct competition between orchestrator and distractor thoughtseeds gates L3
- Policy selection actively minimizes expected free energy
- L2 actions furnish descending predictions over network activity to close the enactive perception--action cycle
- Training uses variational Expectation-Maximization (EM) across expert and novice phenotypes

## Implementation Steps

### 1. Define the Hierarchical Architecture

```python
# L1: Physiological substrate (Ornstein-Uhlenbeck process)
def neuronal_substrate_dynamics(state, t, attention_networks):
    """Models L1: high-dimensional physiological neuronal substrate"""
    # Ornstein-Uhlenbeck process over attentional Yeo networks
    return -theta * (state - mu) + sigma * np.random.wiener()

# L2: Latent mental content as thoughtseeds
def thoughtseed_dynamics(latent_state, autonomic_tendencies):
    """Models L2: low-dimensional generative model encoding thoughtseeds"""
    # Generate latent mental content (thoughtseeds)
    # Evaluate autonomic action tendencies
    return latent_state_update, autonomic_evaluation

# L3: Metacognitive monitor with GNW bottleneck
def metacognitive_monitor(thoughtseeds, policy_prior_divergence):
    """Models L3: agentic metacognitive monitor with GNW capacity bottleneck"""
    # Meta-awareness as GNW ignition signal
    meta_awareness = compute_meta_awareness(policy_prior_divergence)
    # Gating via competition between orchestrator and distractor thoughtseeds
    gated_output = competition_gating(thoughtseeds, meta_awareness)
    return gated_output

# Full system dynamics
def dual_process_active_inference(state, t):
    """Complete dual-process active inference model"""
    # L1 dynamics
    l1_state = neuronal_substrate_dynamics(state, t, attention_networks)
    # L2 processing
    l2_state, autonomic_output = thoughtseed_dynamics(l1_state, autonomic_tendencies)
    # L3 monitoring and control
    l3_output = metacognitive_monitor(l2_state, policy_prior_divergence)
    # Closed-loop perception-action
    updated_state = update_state_with_predictions(l1_state, l2_state, l3_output)
    return updated_state
```

### 2. Implement Variational Expectation-Maximization Training

```python
def variational_em_training(expert_data, novice_data):
    """Train using variational EM across expert and novice phenotypes"""
    # E-step: compute posterior over latent states
    # M-step: update model parameters
    # Iterate until convergence
    pass

# Training across phenotypes
trained_model = variational_em_training(expert_meditators, novice_meditators)
```

### 3. Simulate and Validate Against Empirical Data

```python
def simulate_meditation_trajectory(initial_state, time_points):
    """Simulate the meditation trajectory across attractor states"""
    trajectory = []
    state = initial_state
    for t in time_points:
        state = dual_process_active_inference(state, t)
        trajectory.append(state)
    return trajectory

# Validate against empirical neurophysiological measures
validation_results = compare_with_empirical(simulated_trajectory, empirical_data)
```

## Validation

- Compare simulated attractor state transitions with empirical fMRI/EEG data
- Verify that meta-awareness signals correlate with GNW ignition
- Check that policy-prior divergence drives attentional switching
- Ensure simulated thoughtseed dynamics match subjective reports

## Resources

### scripts/
- `simulate_meditation.py`: Implementation of the dual-process active inference model
- `validate_against_empirical.py": Validation scripts comparing simulation to empirical data

### references/
- `yeo_networks.md`: Details on attentional Yeo networks and their parcellation
- `ornstein_uhlenbeck_process.md": Mathematical formulation of the OU process used for L1 dynamics
- `global_neuronal_workspace.md": Overview of GNW theory and its implementation as a capacity bottleneck

### assets/
- `attractor_states_diagram.png": Visualization of the four attractor states (breath focus, mind-wandering, meta-awareness, redirect attention)
- `hierarchical_markov_blanket.svg": Diagram of the three-layer nested Markov-blanket architecture

## Activation Keywords

- thoughtseeds-dual-process-meditation
- computational phenomenology meditation
- dual-process active inference
- hierarchical Markov-blanket
- global neuronal workspace
- attentional dynamics modeling
---
name: ember-hybrid-snn-llm-architecture
description: EMBER hybrid cognitive architecture combining LLM reasoning with persistent SNN substrate. 220K-neuron spiking network with STDP, 4-layer hierarchy, E/I balance, reward-modulated learning, and autonomous action triggering via lateral STDP propagation.
version: 1.1
authors:
  - William Savage
paper: arXiv:2604.12167
date: 2026-04-14
tags:
  - spiking-neural-network
  - hybrid-architecture
  - LLM
  - cognitive-architecture
  - STDP
  - neuromorphic
  - autonomous-behaviour
category: ai_collection
---

# EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture

## Summary

EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) is a hybrid cognitive architecture that places a Large Language Model as a **replaceable reasoning engine** within a **persistent spiking neural network (SNN) substrate**. The SNN provides autonomous behavioural dynamics, memory, and decision-making, while the LLM handles complex language reasoning on demand.

**Key Innovation**: The SNN is not merely a front-end to the LLM — it learns autonomous behaviours through STDP and reward modulation. LLM actions are triggered by SNN dynamics (lateral STDP propagation), not external prompts. The LLM is hot-swappable without retraining the SNN.

## Key Contributions

1. **Hybrid Architecture with Persistent SNN Substrate**: 220K-neuron SNN with 4-layer hierarchical organization maintaining excitatory/inhibitory (E/I) balance. The SNN persists across sessions, accumulating experience.

2. **Text Embedding via Population Coding**: Z-score standardized top-k population code converts text embeddings into spiking patterns compatible with SNN processing.

3. **Autonomous Action Triggering**: STDP lateral propagation within the SNN autonomously triggers LLM actions — the SNN decides *when* and *what* to ask the LLM, not the other way around.

4. **Reward-Modulated STDP Learning**: Synaptic plasticity is modulated by reward signals, enabling the SNN to learn from outcomes without backpropagation.

5. **LLM as Replaceable Component**: The LLM can be swapped (e.g., GPT-4 → Claude → Llama) without retraining the SNN, demonstrating architectural modularity.

## Architecture Details

### SNN Substrate (220K neurons)
- **4-layer hierarchy**: Sensory → Association → Integration → Motor/Action
- **E/I balance**: ~80% excitatory, ~20% inhibitory neurons per layer
- **Connectivity**: Sparse recurrent connections with distance-dependent probability
- **Neuron model**: Leaky Integrate-and-Fire (LIF) with adaptive threshold

### Population Code Bridge
```
Text Embedding → Z-score Normalization → Top-k Selection → Population Rate Code → Spike Trains
```
- Converts dense LLM embeddings into sparse spiking patterns
- Top-k selection ensures sparse, biologically plausible activation
- Z-score standardization normalizes across different embedding spaces

### STDP Learning Rules
- **Lateral STDP**: Within-layer synaptic modification based on spike timing
- **Hierarchical STDP**: Cross-layer plasticity enabling bottom-up and top-down learning
- **Reward modulation**: Dopamine-like signal gates plasticity based on behavioural outcomes

### Autonomous Decision Loop
1. Sensory input → Population coding → Spike trains
2. SNN processes through hierarchical layers via recurrent dynamics
3. Lateral STDP propagation accumulates evidence in association layers
4. Integration layer threshold crossing triggers LLM query
5. LLM response → Population code → Feedback into SNN
6. Reward signal modulates STDP based on outcome quality

## Implementation Considerations

### SNN Simulation
- Use Brian2 or NEST for large-scale SNN simulation
- 220K neurons requires GPU acceleration (CUDA or OpenCL backend)
- Time resolution: 1ms simulation step
- Typical simulation: 1000-5000 steps per decision cycle

### Population Code Implementation
```python
def text_to_spikes(embedding, k=50, rate_max=100):
    # Z-score standardize
    z_scores = (embedding - embedding.mean()) / embedding.std()
    # Top-k selection
    top_k_indices = np.argsort(z_scores)[-k:]
    # Convert to spike rates
    rates = np.zeros_like(embedding)
    rates[top_k_indices] = z_scores[top_k_indices] * rate_max
    return rates
```

### Memory Requirements
- 220K neurons × ~1000 synapses/neuron ≈ 220M synapses
- STDP traces: 2 × 220M = 440M floating point values
- Total: ~5-10 GB GPU memory for full simulation

## Key Equations

### LIF Neuron Dynamics
$$\tau_m \frac{dV}{dt} = -(V - V_{rest}) + R \cdot I_{syn}$$

### STDP Weight Update
$$\Delta w = \sum_{t_{pre}} \sum_{t_{post}} W(t_{post} - t_{pre})$$

Where the STDP window function:
$$W(\Delta t) = \begin{cases} A_+ \exp(-\Delta t / \tau_+) & \text{if } \Delta t > 0 \\ -A_- \exp(\Delta t / \tau_-) & \text{if } \Delta t < 0 \end{cases}$$

### Reward-Modulated Plasticity
$$\Delta w_{ij} \propto \text{STDP}_{ij} \times R(t) \times \text{eligibility}_{ij}$$

## Relevance

This work bridges the gap between deep learning (LLMs) and neuromorphic computing (SNNs), offering:
- **Energy efficiency**: SNN substrate runs at ~100x less energy than continuous LLM inference
- **Autonomy**: SNN makes decisions without LLM for routine tasks
- **Modularity**: LLM can be upgraded without system retraining
- **Biological plausibility**: STDP-based learning follows neuroscience principles

## Triggers (激活词)

hybrid SNN-LLM, cognitive architecture, autonomous behaviour, STDP, population coding, reward-modulated learning, neuromorphic AI, spiking neural network, LLM integration, EMBER, biologically-inspired AI, persistent memory, hot-swappable LLM

---
name: ember-hybrid-snn-llm-architecture
description: EMBER hybrid cognitive architecture combining LLM reasoning with biologically-inspired spiking neural network memory. Uses experience-modulated plasticity for autonomous cognitive behavior.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [spiking-neural-network, llm, cognitive-architecture, hybrid, memory, neuromorphic]
    source_paper: "EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture (arXiv:2604.12167v1)"
---

# EMBER: Hybrid SNN-LLM Cognitive Architecture

## Overview
EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) reorganizes the LLM-memory relationship by replacing traditional retrieval-augmented generation with a learned spiking neural network (SNN) that provides autonomous, self-modulating memory dynamics. The SNN encodes experiences as attractor states and uses biologically-plausible plasticity rules to autonomously consolidate and retrieve memories during generation.

## Core Concepts

### Architecture
- **LLM as Reasoner**: The LLM handles language understanding and generation
- **SNN as Memory**: A recurrent spiking network stores experiences as dynamical attractors
- **Experience Modulation**: Interactions trigger Hebbian-like updates in the SNN, enabling autonomous memory formation without explicit training

### Key Mechanisms
1. **Encoding**: Text experiences mapped to SNN initial conditions via embedding projection
2. **Dynamics**: SNN evolves autonomously, retrieving related memories through attractor dynamics
3. **Plasticity**: Synaptic weights update during interaction via local learning rules
4. **Modulation**: LLM receives SNN state as additional context, influencing generation

### Advantages Over RAG
- No explicit retrieval step needed -- memory emerges from network dynamics
- Continual learning without catastrophic forgetting via attractor separation
- Biologically-inspired consolidation (similar to hippocampal-neocortical memory systems)
- Autonomous behavior without explicit prompting for memory recall

## Implementation Pattern
```python
class EMBER:
    def __init__(self, llm, snn, embedding_dim=768, snn_size=256):
        self.llm = llm
        self.snn = snn  # Recurrent spiking network
        self.encoder = nn.Linear(embedding_dim, snn_size)  # Text to SNN state
        
    def encode_experience(self, text):
        embedding = self.llm.get_embedding(text)
        initial_state = self.encoder(embedding)
        return initial_state
    
    def snn_dynamics(self, initial_state, timesteps=50):
        state = initial_state
        for _ in range(timesteps):
            spikes = self.snn.step(state)
            state = self.snn.update(state, spikes)
        return state
    
    def plasticity_update(self, state, context):
        delta_w = torch.outer(state, context)
        self.snn.weights += 0.01 * delta_w
    
    def generate(self, prompt, context_history):
        for ctx in context_history:
            state = self.encode_experience(ctx)
            memory = self.snn_dynamics(state)
            self.plasticity_update(memory, state)
        snn_context = self.snn.get_current_state()
        return self.llm.generate(prompt + str(snn_context))
```

## Applications
- Autonomous AI agents with persistent memory
- Continual learning systems without catastrophic forgetting
- Brain-inspired cognitive architectures
- Neuromorphic computing implementations

## Activation Keywords
- EMBER architecture, hybrid SNN LLM, spiking neural network memory, cognitive architecture, experience-modulated memory, autonomous cognitive behavior, biologically-inspired memory, neuromorphic LLM, 混合 SNN LLM 架构, 脉冲神经网络记忆

## References
- EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture
- Authors: William Savage
- Published: 2026-04-14
- arXiv: https://arxiv.org/abs/2604.12167v1
---
name: ember-hybrid-snn-llm-architecture
description: "Hybrid cognitive architecture combining a 220K-neuron SNN with STDP and hierarchical organization as a persistent associative substrate, with an LLM as a replaceable reasoning engine"
version: "0.1.0"
arxiv: "2604.12167v1"
paper_title: "EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture"
tags:
  - spiking-neural-networks
  - hybrid-architecture
  - stdp
  - llm-integration
  - cognitive-architecture
  - associative-memory
  - neuromorphic
---

# EMBER: Hybrid SNN-LLM Architecture

## Overview

EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) is a hybrid cognitive architecture that reorganizes the relationship between LLMs and memory. Rather than augmenting an LLM with retrieval tools, it places the LLM as a **replaceable reasoning engine** within a persistent, biologically-grounded associative substrate.

## Key Principles

### Architecture Components

- **SNN Core**: 220,000-neuron spiking neural network with STDP (spike-timing-dependent plasticity)
- **Four-Layer Hierarchy**: Sensory → Concept → Category → Meta-pattern
- **E/I Balance**: Excitatory/inhibitory balance for stable dynamics
- **Reward-Modulated Learning**: Plasticity guided by reward signals
- **LLM Reasoning Engine**: Pluggable component that receives SNN-triggered associations

### Population Encoding

- **Z-score standardized top-k population code**: Dimension-independent encoding of text embeddings
- Achieves **82.2% discrimination retention** across embedding dimensionalities

### Autonomous Operation

- STDP lateral propagation during idle operation triggers and shapes LLM actions
- **No external prompting or scripted triggers** required
- SNN determines *when* to act and *what* associations to surface
- LLM selects the action type and generates content
- First SNN-triggered action occurs after only **7 conversational exchanges** (14 messages) from cold start

## Implementation Guidance

1. Initialize SNN with four hierarchical layers and E/I balanced connectivity
2. Encode text inputs via z-score standardized top-k population encoding
3. Run STDP learning during both active interaction and idle periods
4. Monitor lateral propagation patterns to detect association formation
5. Trigger LLM reasoning when SNN activity crosses action thresholds
6. Apply reward modulation to reinforce useful association pathways

## References

See `references/implementation.md` for code patterns and implementation details.

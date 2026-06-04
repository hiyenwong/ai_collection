---
name: recursive-multi-agent-systems
description: "RecursiveMAS framework for scaling multi-agent collaboration through recursive latent-space computation. Enables heterogeneous agents to form collaboration loops via RecursiveLink module with inner-outer loop learning. Activation triggers: recursive multi-agent, RecursiveMAS, latent-space agent collaboration, recursive scaling, agent loop, cross-agent latent transfer."
---

# Recursive Multi-Agent Systems (RecursiveMAS)

> A recursive multi-agent framework that casts the entire system as a unified latent-space recursive computation, scaling agent collaboration through recursion rather than just single-model recursion.

## Metadata
- **Source**: arXiv:2604.25917 [cs.AI, cs.CL, cs.LG]
- **Authors**: Xiyuan Yang, Jiaru Zou, Rui Pan, Ruizhong Qiu, Pan Lu, Shizhe Diao, Jindong Jiang, Hanghang Tong, Tong Zhang, Markus J. Buehler, Jingrui He, James Zou
- **Published**: 2026-04-28
- **Project Page**: https://recursivemas.github.io

## Core Problem

Traditional multi-agent systems (MAS) arrange agents in sequential pipelines or parallel expert ensembles, but these are static structures that cannot evolve over time. Recursive language models (RLMs) show that iterating computation over latent states deepens reasoning — this paper asks: **Can agent collaboration itself be scaled through recursion?**

## Key Innovation

**RecursiveMAS**: Treats the entire multi-agent system as a single recursive computation loop, where each agent functions like a layer in a deep RLM, with information flowing and recurring within and across agents as a hidden stream.

### RecursiveLink Module

The lightweight **RecursiveLink (R)** bridges heterogeneous agents by preserving and transmitting last-layer hidden states across embedding spaces:

1. **Dense-to-Shallow Transition**: Previous step's last-layer embeddings fed back as next-step input embeddings during latent thoughts generation
2. **Cross-Model Transition**: One model's newly generated latent states mapped to another model's embedding space

This enables in-distribution latent thought generation and cross-agent latent state transfer without text-based communication overhead.

### System Architecture: Chain All Agents as a Loop

- Each agent in RecursiveMAS is cast as an **RLM layer**
- Agents reason and interact in **latent space** (not text space)
- Information flows recursively: Agent A → Agent B → ... → Agent A (loop)
- The residual stream loops across agents, increasing reasoning depth
- Four representative collaboration patterns supported:
  - Sequential pipeline
  - Parallel expert ensemble
  - Debate/verification
  - Hierarchical orchestration

### Learning Algorithm: Inner-Outer Loop

**Inner Loop (Preliminary)**:
- Equips each agent with stronger latent thoughts generation capabilities
- Trains individual agents to produce useful hidden state representations

**Outer Loop (Iterative)**:
- Progressively optimizes the system as one unified entity over recursion rounds
- Only trains on the **RecursiveLink** module
- Shared gradient-based credit assignment across recursion rounds
- Whole-system co-optimization

### Theoretical Properties

1. **Runtime Efficiency**: RecursiveMAS is more efficient than standard text-based MAS
   - Latent-space communication avoids token generation overhead
   - Linear complexity in recursion depth vs. exponential for text-based MAS
2. **Gradient Stability**: Maintains stable gradients during recursive training
   - Theoretical analysis of learning dynamics shows no vanishing/exploding gradients
3. **Credit Assignment**: Shared gradient flow across recursion rounds enables end-to-end optimization

## Empirical Results

Evaluated across **9 benchmarks** in 4 domains with **sub-1.5B agents** and **5-10B scaled agents**:

| Metric | Improvement |
|--------|-------------|
| Average accuracy | +8.3% over baselines |
| Inference speedup | 1.2×–2.4× |
| Token usage reduction | 34.6%–75.6% |

Benchmarks: MATH500, AIME2025, AIME2026, GPQA-Diamond, MedQA, LiveCodeBench-v6, MBPP Plus, HotpotQA, and more.

**Scaling behavior**: Clean performance scaling as recursion depth increases (r=1,2,3). Sub-1.5B agents with deeper recursion match or exceed larger single models.

## Implementation Guide

### Prerequisites
- Transformer-based LLM agents (heterogeneous models supported)
- Access to intermediate hidden states (last-layer embeddings)
- Training framework with gradient flow across modules

### Architecture Design Steps

1. **Design RecursiveLink**:
   ```
   R: h_prev → E_next
   Where h_prev is last-layer hidden state, E_next is input embeddings for next agent
   ```
   - Map between different embedding spaces if agents use different models
   - Preserve semantic information during transition

2. **Define Collaboration Pattern**:
   - Sequential: Agent1 → Agent2 → ... → AgentN → Agent1
   - Parallel: Multiple agents → Aggregator → Loop
   - Debate: AgentA ↔ AgentB (iterative refinement)
   - Hierarchical: Orchestrator → Workers → Orchestrator

3. **Set Recursion Depth**:
   - Training depth r_train and inference depth r_inference
   - Deeper recursion = more reasoning depth but longer latency
   - Scaling law observed: performance improves monotonically with r

4. **Train with Inner-Outer Loop**:
   - Phase 1: Inner loop — train each agent's latent generation
   - Phase 2: Outer loop — optimize RecursiveLink for system-level performance
   - Use shared gradient assignment across recursion rounds

### Code Sketch
```python
class RecursiveMAS:
    def __init__(self, agents, recursive_link, collaboration_pattern):
        self.agents = agents  # List of LLM agents
        self.R = recursive_link  # RecursiveLink module
        self.pattern = collaboration_pattern
    
    def forward(self, x, recursion_depth):
        h = self.encode_input(x)
        for r in range(recursion_depth):
            for agent in self.agents:
                h = agent.forward(h)  # Latent-space reasoning
                h = self.R(h)  # Cross-agent transfer
        return self.decode_output(h)
    
    def train(self, data):
        # Inner loop: train agent latent generation
        self.inner_loop_train(data)
        # Outer loop: optimize RecursiveLink
        self.outer_loop_train(data)
```

## Applications
- Complex reasoning tasks requiring iterative refinement (math, science, code)
- Multi-domain expert collaboration with cross-domain knowledge transfer
- Token-efficient agent systems where text-based communication is too costly
- Scalable MAS architecture that improves with more recursion (not just more agents)

## Pitfalls
- Requires access to intermediate hidden states — not all LLM APIs expose these
- RecursiveLink must handle embedding space mismatches between heterogeneous models
- Training stability depends on proper gradient flow across recursion rounds
- Deeper recursion increases latency — trade-off between accuracy and speed

## Related Skills
- agent-collaboration-protocol
- agent-delegation-rules
- psi-shared-state-architecture
- shared-state-architecture

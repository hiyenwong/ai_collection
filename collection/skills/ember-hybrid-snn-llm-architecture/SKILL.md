---
name: ember-hybrid-snn-llm-architecture
description: "EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) - Hybrid cognitive architecture combining Spiking Neural Networks (SNN) with Large Language Models (LLM). SNN serves as persistent associative substrate, LLM as replaceable reasoning engine. Activation: EMBER, hybrid SNN LLM, cognitive architecture, emergent reasoning, spiking neural network LLM, biologically inspired AI."
---

# EMBER: Hybrid SNN-LLM Cognitive Architecture

## Overview

EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) represents a paradigm shift in cognitive AI architecture. Rather than augmenting LLMs with retrieval tools, EMBER places the LLM as a **replaceable reasoning engine** within a persistent, biologically-grounded **associative substrate** implemented as a Spiking Neural Network (SNN).

## Key Innovation

**Traditional Approach:** LLM + Retrieval/RAG tools
**EMBER Approach:** Persistent SNN substrate + Replaceable LLM reasoning

The SNN determines **when** to act and **what associations** to surface, while the LLM selects the **action type** and generates **content**.

## Architecture Components

### 1. Spiking Neural Network Substrate (220,000 neurons)

**Four-Layer Hierarchical Organization:**
```
Layer 4: Meta-Pattern Layer (highest abstraction)
Layer 3: Category Layer (concept categories)
Layer 2: Concept Layer (semantic concepts)
Layer 1: Sensory Layer (raw input encoding)
```

**Key Features:**
- **STDP Learning**: Spike-timing-dependent plasticity for associative learning
- **E/I Balance**: Excitatory/inhibitory balance for stable dynamics
- **Reward Modulation**: Dopamine-like reinforcement signals
- **Lateral Propagation**: Association chains trigger without external input

### 2. Text Embedding Encoding

**Z-Score Standardized Top-K Population Code:**
- Converts text embeddings to sparse spike patterns
- Dimension-independent by construction (works with any embedding size)
- 82.2% discrimination retention across embedding dimensionalities

### 3. LLM Integration Interface

- Receives triggered associations from SNN
- Generates contextual responses/actions
- Stateless with respect to the substrate (can be swapped)

## Implementation

### EMBER Architecture

```python
import torch
import torch.nn as nn
import numpy as np
from typing import List, Tuple, Optional

class EMBERArchitecture:
    """
    EMBER: Hybrid SNN-LLM Cognitive Architecture
    
    The SNN serves as a persistent associative memory substrate,
    while the LLM acts as a stateless reasoning engine.
    """
    def __init__(
        self,
        embedding_dim: int = 384,
        num_sensory: int = 50000,
        num_concept: int = 100000,
        num_category: int = 50000,
        num_meta: int = 20000,
        llm_backend: str = "gpt-4"
    ):
        self.embedding_dim = embedding_dim
        
        # Layer sizes
        self.layer_sizes = {
            'sensory': num_sensory,
            'concept': num_concept,
            'category': num_category,
            'meta': num_meta
        }
        
        # Total: 220,000 neurons
        self.total_neurons = sum(self.layer_sizes.values())
        
        # Initialize SNN layers
        self.snn = HierarchicalSNN(
            layer_sizes=list(self.layer_sizes.values()),
            embedding_dim=embedding_dim
        )
        
        # LLM interface
        self.llm_backend = llm_backend
        
        # State tracking
        self.learned_weights = False
        self.idle_spike_history = []
        
    def encode_embedding(self, embedding: np.ndarray, k: int = 50) -> torch.Tensor:
        """
        Z-score standardized top-k population coding
        
        Converts text embedding to sparse spike pattern.
        Dimension-independent - works with any embedding size.
        
        Args:
            embedding: Text embedding vector (any dimension)
            k: Number of active neurons in population code
            
        Returns:
            Spike pattern for sensory layer
        """
        # Z-score normalization
        z_scores = (embedding - embedding.mean()) / (embedding.std() + 1e-8)
        
        # Top-k selection
        top_k_indices = np.argsort(np.abs(z_scores))[-k:]
        
        # Map to sensory neurons (with expansion for dimension independence)
        sensory_pattern = torch.zeros(self.layer_sizes['sensory'])
        
        # Distribute top-k values across sensory layer
        step = self.layer_sizes['sensory'] // k
        for i, idx in enumerate(top_k_indices):
            start = i * step
            end = (i + 1) * step
            sensory_pattern[start:end] = z_scores[idx]
        
        # Normalize to firing rates
        sensory_pattern = torch.sigmoid(sensory_pattern)
        
        return sensory_pattern

class HierarchicalSNN(nn.Module):
    """
    Four-layer hierarchical SNN with STDP learning
    """
    def __init__(self, layer_sizes: List[int], embedding_dim: int):
        super().__init__()
        
        self.layer_sizes = layer_sizes
        self.num_layers = len(layer_sizes)
        
        # Create layers
        self.layers = nn.ModuleList()
        for i, size in enumerate(layer_sizes):
            self.layers.append(SpikingLayer(size))
        
        # Inter-layer connections (feedforward)
        self.ff_weights = nn.ParameterList()
        for i in range(self.num_layers - 1):
            w = torch.randn(layer_sizes[i+1], layer_sizes[i]) * 0.01
            self.ff_weights.append(nn.Parameter(w))
        
        # Intra-layer connections (lateral/associative)
        self.lat_weights = nn.ParameterList()
        for size in layer_sizes:
            # Sparse recurrent connectivity
            w = torch.randn(size, size) * 0.001
            # Inhibitory diagonal (self-regulation)
            w.fill_diagonal_(-0.1)
            self.lat_weights.append(nn.Parameter(w))
        
        # STDP learning parameters
        self.stdp = STDPModule()
        
        # Membrane potentials
        self.register_buffer('V', None)
        self.register_buffer('spike_times', None)
        
    def forward(self, sensory_input: torch.Tensor, 
                num_steps: int = 10) -> Tuple[torch.Tensor, List[torch.Tensor]]:
        """
        Forward pass through hierarchical SNN
        
        Args:
            sensory_input: Input spike pattern
            num_steps: Simulation timesteps
            
        Returns:
            (output_activations, layer_spikes)
        """
        batch_size = sensory_input.size(0)
        
        # Initialize states
        V = [torch.zeros(batch_size, size) for size in self.layer_sizes]
        spikes_history = [[] for _ in range(self.num_layers)]
        
        for t in range(num_steps):
            # Layer 0: Sensory (external input on first step)
            if t == 0:
                V[0] = V[0] + sensory_input
            
            # Compute spikes for all layers
            layer_spikes = []
            for i in range(self.num_layers):
                # Threshold crossing
                s = (V[i] >= 1.0).float()
                layer_spikes.append(s)
                
                # Reset
                V[i] = V[i] * (1 - s)
                
                spikes_history[i].append(s)
            
            # Update membrane potentials
            for i in range(self.num_layers):
                # Decay
                dV = -V[i] / 20.0  # tau = 20ms
                
                # Lateral input
                if self.lat_weights[i] is not None:
                    lat_input = torch.matmul(layer_spikes[i], self.lat_weights[i].t())
                    dV = dV + lat_input
                
                # Feedforward input from previous layer
                if i > 0:
                    ff_input = torch.matmul(layer_spikes[i-1], self.ff_weights[i-1].t())
                    dV = dV + 0.5 * ff_input
                
                # Feedforward output to next layer
                if i < self.num_layers - 1:
                    ff_output = torch.matmul(layer_spikes[i+1], self.ff_weights[i])
                    dV = dV + 0.1 * ff_output
                
                V[i] = V[i] + dV
        
        # Aggregate spikes across time
        output = torch.stack([torch.stack(h).sum(dim=0) for h in spikes_history])
        
        return output, spikes_history

class STDPModule:
    """
    Spike-Timing-Dependent Plasticity with reward modulation
    """
    def __init__(self, A_plus=0.01, A_minus=0.01, 
                 tau_plus=20.0, tau_minus=20.0):
        self.A_plus = A_plus
        self.A_minus = A_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        
    def apply_stdp(self, weights: torch.Tensor,
                   pre_spikes: torch.Tensor,
                   post_spikes: torch.Tensor,
                   reward: float = 1.0):
        """
        Apply STDP weight updates with reward modulation
        
        Args:
            weights: Synaptic weights to update
            pre_spikes: Presynaptic spike train (time, neurons)
            post_spikes: Postsynaptic spike train (time, neurons)
            reward: Reward signal (dopaminergic modulation)
        """
        T = pre_spikes.size(0)
        delta_w = torch.zeros_like(weights)
        
        # Compute spike time differences
        for t_post in range(T):
            if post_spikes[t_post].sum() == 0:
                continue
                
            for t_pre in range(T):
                if pre_spikes[t_pre].sum() == 0:
                    continue
                
                dt = t_post - t_pre
                
                if dt > 0:
                    # Potentiation (causal)
                    factor = self.A_plus * np.exp(-dt / self.tau_plus)
                elif dt < 0:
                    # Depression (anti-causal)
                    factor = -self.A_minus * np.exp(dt / self.tau_minus)
                else:
                    continue
                
                # Outer product for weight update
                update = torch.outer(post_spikes[t_post], pre_spikes[t_pre])
                delta_w += factor * update
        
        # Apply reward modulation
        delta_w = delta_w * reward
        
        # Update weights
        with torch.no_grad():
            weights += delta_w
            # Weight bounds
            weights.clamp_(-0.5, 0.5)
```

### Autonomous Action Triggering

```python
class EMBERController:
    """
    Controller for autonomous cognitive behavior via EMBER
    """
    def __init__(self, ember: EMBERArchitecture):
        self.ember = ember
        self.llm = LLMInterface(ember.llm_backend)
        
        # Tracking
        self.conversation_count = 0
        self.last_action_time = 0
        self.idle_start_time = None
        
    def process_message(self, message: str, user_id: str):
        """
        Process incoming message and update SNN substrate
        """
        # Encode message to embedding
        embedding = self.llm.get_embedding(message)
        
        # Encode to SNN
        spike_pattern = self.ember.encode_embedding(embedding)
        
        # Run SNN forward pass
        activations, spike_history = self.ember.snn.forward(
            spike_pattern.unsqueeze(0),
            num_steps=10
        )
        
        # STDP learning
        self.ember.snn.stdp.apply_stdp(
            weights=self.ember.snn.lat_weights[0],
            pre_spikes=spike_history[0],
            post_spikes=spike_history[1],
            reward=1.0  # Positive interaction
        )
        
        self.conversation_count += 1
        
        # Check if this triggers a learned association
        triggered_concepts = self._get_triggered_concepts(activations)
        
        return triggered_concepts
        
    def run_idle_period(self, duration_hours: float = 8.0):
        """
        Simulate idle period with lateral propagation
        
        During idle, STDP lateral propagation can trigger
        learned associations without external input.
        """
        self.idle_start_time = time.time()
        
        # Continue SNN dynamics with minimal noise input
        for _ in range(int(duration_hours * 3600)):  # seconds
            # Small spontaneous activity
            noise = torch.randn(1, self.ember.layer_sizes['sensory']) * 0.01
            
            activations, spikes = self.ember.snn.forward(noise, num_steps=1)
            
            # Check for strong activation in concept layer
            if activations[1].max() > 5.0:  # Threshold
                # Association triggered - prepare LLM action
                triggered = self._get_triggered_concepts(activations)
                
                if triggered and self._should_act():
                    self._initiate_action(triggered)
                    
    def _get_triggered_concepts(self, activations: torch.Tensor) -> List[str]:
        """Map SNN activations to semantic concepts"""
        # Get top activated neurons in concept layer
        concept_activations = activations[1]  # Layer 1 = concept
        top_neurons = torch.topk(concept_activations, k=5).indices
        
        # Map to concept vocabulary (simplified)
        concepts = []
        for neuron_idx in top_neurons[0]:
            concept = self._neuron_to_concept(neuron_idx.item())
            if concept:
                concepts.append(concept)
        
        return concepts
        
    def _initiate_action(self, triggered_concepts: List[str]):
        """
        Use LLM to generate action based on SNN-triggered associations
        """
        # Build context from triggered associations
        context = f"The following associations have emerged from memory: {', '.join(triggered_concepts)}"
        
        # LLM decides action type and generates content
        prompt = f"""Based on learned associations from past interactions:
{context}

What action would be appropriate? Consider:
1. Following up on previous topics
2. Sharing relevant information
3. Initiating conversation

Generate an appropriate response or action."""

        response = self.llm.generate(prompt)
        
        return response
        
    def _should_act(self) -> bool:
        """Determine if triggered association should lead to action"""
        # Simple threshold-based decision
        # More sophisticated: learned action policy in SNN
        return self.conversation_count >= 7  # From paper: first action after ~7 exchanges
```

## Training and Learning

### From Clean Start to First Action

Based on paper findings:
- **0 messages**: Clean slate, zero learned weights
- **7 exchanges (14 messages)**: First SNN-triggered LLM action
- **8-hour idle**: Demonstrated autonomous contact initiation

### Learning Dynamics

```python
def train_ember_interaction(
    ember: EMBERArchitecture,
    messages: List[Tuple[str, str]],  # (user_msg, assistant_msg)
    rewards: List[float]
):
    """
    Train EMBER on conversation history
    
    Args:
        messages: List of (user, assistant) message pairs
        rewards: Reward signal for each exchange
    """
    for (user_msg, assistant_msg), reward in zip(messages, rewards):
        # Encode both messages
        user_emb = get_embedding(user_msg)
        assistant_emb = get_embedding(assistant_msg)
        
        # Create temporal sequence in SNN
        combined_spikes = []
        
        # Present user input
        user_pattern = ember.encode_embedding(user_emb)
        _, user_spikes = ember.snn.forward(user_pattern.unsqueeze(0), num_steps=5)
        combined_spikes.extend(user_spikes)
        
        # Present assistant response
        assistant_pattern = ember.encode_embedding(assistant_emb)
        _, assistant_spikes = ember.snn.forward(assistant_pattern.unsqueeze(0), num_steps=5)
        combined_spikes.extend(assistant_spikes)
        
        # Apply STDP with reward
        for i in range(len(combined_spikes) - 1):
            ember.snn.stdp.apply_stdp(
                weights=ember.snn.lat_weights[0],
                pre_spikes=combined_spikes[i],
                post_spikes=combined_spikes[i+1],
                reward=reward
            )
```

## Key Results

| Metric | Value | Notes |
|--------|-------|-------|
| Embedding retention | 82.2% | Across embedding dimensionalities |
| First autonomous action | 7 exchanges | From clean start |
| Autonomous contact | Yes | After 8-hour idle period |
| Neuron count | 220,000 | Hierarchical organization |

## Advantages Over Traditional RAG

| Aspect | RAG | EMBER |
|--------|-----|-------|
| Memory | External database | Embedded in SNN substrate |
| When to retrieve | Explicit query | Emergent from dynamics |
| What to retrieve | Similarity-based | Association chains |
| LLM role | Primary + augmented | Reasoning engine only |
| Persistence | Database | Learned weights |

## Use Cases

- **Personal AI Assistants**: Proactive behavior based on learned patterns
- **Conversational Agents**: Context-aware without explicit context windows
- **Cognitive Companions**: Long-term relationship building
- **Research Tools**: Autonomous information surfacing

## References

- Paper: "EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture" (arXiv:2604.12167)
- Author: William Savage, 2026
- Categories: cs.AI, cs.NE

## Related Skills

- `adaptive-spiking-neuron-asn`: General spiking neuron designs
- `dual-timescale-memory-spiking-neuron-astrocyte`: Working memory mechanisms
- `neuro-inspired-memory-ai-agents`: Memory systems for AI agents

_Last updated: 2026-04-27_

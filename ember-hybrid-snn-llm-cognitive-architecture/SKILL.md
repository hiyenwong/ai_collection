---
name: ember-hybrid-snn-llm-cognitive-architecture
description: "EMBER hybrid cognitive architecture combining LLM reasoning with persistent biologically-grounded SNN memory substrate. Autonomous cognitive behavior via STDP-based lateral propagation."
---

# EMBER: Hybrid SNN-LLM Cognitive Architecture

Methodology from paper: "EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture" (arXiv:2604.12167, 2026-04-14)

## Core Concept

EMBER (Experience-Modulated Biologically-inspired Emergent Reasoning) reorganizes the LLM-memory relationship:

**Traditional**: LLM + retrieval tools
**EMBER**: LLM as replaceable reasoning engine within persistent SNN substrate

## Architecture

### SNN Substrate (220,000 neurons)
- **Spike-Timing-Dependent Plasticity (STDP)**: Online learning
- **Four-Layer Hierarchy**:
  1. Sensory layer
  2. Concept layer  
  3. Category layer
  4. Meta-pattern layer
- **E/I Balance**: Inhibitory-excitatory balance mechanisms
- **Reward-Modulated Learning**: Associative learning with reinforcement

### Text Encoding
**Z-score Standardized Top-K Population Code**:
- Dimension-independent by construction
- 82.2% discrimination retention across embedding sizes
- Converts embeddings to sparse population codes

## Key Innovation: Autonomous Action

### STDP Lateral Propagation
- **Idle Operation**: Continuous internal dynamics
- **Autonomous Triggering**: SNN determines when to act
- **Association Surfacing**: Learned associations fire laterally
- **LLM Integration**: LLM selects action type and generates content

### Real-World Example
- 8-hour idle period → learned person-topic associations fired
- System autonomously initiated contact with user
- No external prompting or scripted triggers

## Performance

- **Learning Speed**: First SNN-triggered action after only 7 conversations (14 messages) from clean start
- **Discrimination**: 82.2% retention across embedding dimensionalities
- **Autonomy**: True self-directed behavior without explicit triggers

## Applications

- **Autonomous Agents**: Self-directed AI assistants
- **Proactive Systems**: Anticipating user needs
- **Long-Term Memory**: Persistent associative memory
- **Cognitive Architectures**: Biologically-inspired AI

## Implementation Notes

```python
class EMBERArchitecture:
    def __init__(self, llm_engine, snn_config):
        self.llm = llm_engine  # Replaceable reasoning engine
        self.snn = SpikingNeuralNetwork(snn_config)
        self.encoder = ZScoreTopKEncoder()
        
    def encode_input(self, text):
        """Convert text to SNN population code"""
        embedding = self.llm.embed(text)
        normalized = (embedding - embedding.mean()) / embedding.std()
        top_k_indices = torch.topk(normalized.abs(), k=K).indices
        population_code = torch.zeros_like(embedding)
        population_code[top_k_indices] = normalized[top_k_indices]
        return population_code
        
    def process_conversation(self, messages):
        for msg in messages:
            code = self.encode_input(msg['content'])
            self.snn.inject_spikes(code)
        
        self.snn.run_steps(duration='idle_period')
        
        if self.snn.detect_strong_association():
            associations = self.snn.retrieve_active_associations()
            action = self.llm.generate_action(associations)
            return action
        return None
```

## References

- Savage, W. (2026). EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics in a Hybrid LLM Architecture. arXiv:2604.12167.
- arXiv: https://arxiv.org/abs/2604.12167

## Activation Keywords

- EMBER architecture
- hybrid SNN LLM
- autonomous cognitive behavior
- STDP lateral propagation
- biologically-grounded memory
- proactive AI agents
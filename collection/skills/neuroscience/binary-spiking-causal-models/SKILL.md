---
name: binary-spiking-causal-models
description: "Causal analysis of Binary Spiking Neural Networks (BSNNs) using logic-based explainable AI methods. Formally defines BSNNs as binary causal models and provides tractable algorithms for computing abductive explanations."
---

# Binary Spiking Neural Networks as Causal Models

Research methodology from paper "Binary Spiking Neural Networks as Causal Models" (2026-04-29).

## Core Idea
Formally represents Binary Spiking Neural Networks (BSNNs) as **binary causal models**, enabling logic-based explanations of network behavior using methods from explainable AI (XAI).

## Key Contributions

### 1. Formal BSNN Definition
- Binary spiking activity mapped to causal model variables
- Each neuron's spike/non-spike state as a binary variable
- Causal dependencies defined by network connectivity

### 2. Causal Representation
- Spiking activity represented as structural causal model
- Input-output relationships captured through causal pathways
- Enables formal reasoning about network decisions

### 3. Abductive Explanations
- **Abductive explanation**: minimal set of input features that suffice to explain the output
- Problem proven **computationally tractable** under certain conditions
- Algorithms provided for computing explanations efficiently

### 4. Logic-Based XAI Integration
- Leverages existing XAI literature for logic-based explanations
- Bridges spiking neural networks and interpretable AI
- Formal guarantees on explanation correctness

## When to Use
- Need interpretable SNN decisions (medical, safety-critical applications)
- Analyzing BSNN behavior and decision pathways
- Comparing SNN explanations with ANN explanation methods
- Formal verification of spiking network behavior

## Implementation Pattern

```python
# Conceptual causal explanation for BSNN
class BSNNCausalExplainer:
    def __init__(self, bsnn_model):
        self.model = bsnn_model
        self.causal_graph = self.build_causal_graph()
    
    def build_causal_graph(self):
        """Map BSNN connectivity to causal graph."""
        # Each neuron = binary variable
        # Synaptic weights = causal strengths
        pass
    
    def abductive_explanation(self, input_spikes, output):
        """Find minimal input subset explaining output."""
        # Tractable under certain network conditions
        pass
    
    def necessary_causes(self, output):
        """Find inputs that are necessary for the output."""
        pass
```

## Theoretical Results
- Finding abductive explanations is **tractable** for BSNNs under specific structural conditions
- Complexity depends on network depth and connectivity patterns
- Provides formal guarantees missing from post-hoc explanation methods

## Related Skills
- `spiking-neural-network-analysis`
- `quantization-spiking-neural-networks-beyond-accuracy`
- `snn-universal-approximation-theory`

## Paper Reference
- **arXiv:** 2604.27007
- **Authors:** Aditya Kar, Emiliano Lorini, Timothee Masquelier
- **Date:** 2026-04-29
- **Categories:** cs.AI
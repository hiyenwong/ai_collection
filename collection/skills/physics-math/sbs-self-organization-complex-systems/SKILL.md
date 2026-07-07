---
name: sbs-self-organization-complex-systems
description: Surviving by Serving (SBS) principle for self-organization in complex adaptive systems. Components persist when outputs are utilized; non-utilization triggers adaptation. Emergence of functional networks without centralized control.
version: 1.0.0
arxiv_id: 2606.26733
authors: ["Metzner, Claus", "Ghebleh, Ali", "Schilling, Achim", "Maier, Andreas", "Kinfe, Thomas", "Krauss, Patrick"]
published: 2026-06-25
tags: [self-organization, complex-systems, adaptive-systems, multi-agent, emergence, functional-networks]
activation_keywords: [Surviving by Serving, SBS, self-organization, functional emergence, complex adaptive systems, core-periphery]
---

# Surviving by Serving: Functional Relevance Drives Self-Organization

**ArXiv: [2606.26733](https://arxiv.org/abs/2606.26733)** | **Published: 2026-06-25**

## Core Principle

**Surviving by Serving (SBS)**: Components persist as long as their outputs are utilized by other components; prolonged non-utilization promotes adaptation and exploration.

This provides a **substrate-independent mechanism** for self-organization without:
- Centralized control
- Global objectives
- External selection pressures

## Key Findings

1. **Spontaneous functional networks**: Self-organization into interaction networks with only local feedback
2. **Stable transformation chains**: Emergence of stable processing pathways
3. **Core-periphery organization**: Structural differentiation into functional core and exploratory periphery
4. **Novel state generation**: Creation of states enabling previously unreachable targets
5. **Pre-adaptive search phase**: Self-sustaining networks arise without selection, creating conditions for later solutions

## Multi-Agent Model

```
Agents:
 - Transform shared resources
 - Receive local feedback when outputs utilized
 - Persist while utilized → stability
 - Non-utilized → exploration/adaptation

Emergence:
 - Functional interaction networks
 - Transformation chains
 - Core-periphery structure
 - Novel state generation
```

## Mechanistic Framework

### Utilization Feedback
- Local signal when output consumed by downstream agent
- Positive feedback → stability
- No feedback → adaptation pressure

### Resource Flow Dynamics
- Shared resource pool
- Agent-specific transformations
- Network-level flow patterns

### Stability-Exploration Trade-off
- Utilized agents → maintain function
- Non-utilized agents → explore alternatives

## Applications

- Neural network self-organization
- Biological system development
- Social network formation
- Economic system emergence
- Technical infrastructure evolution

## Neuroscience Implications

- **Brain development**: Neural circuits organize by functional utilization
- **Synaptic stability**: Utilized connections persist; unused adapt
- **Skill acquisition**: Functional pathways strengthen through use
- **Network plasticity**: Non-utilized pathways explore alternatives

## Technical Implementation

```python
# Minimal SBS agent model
class SBSAgent:
    def __init__(self):
        self.persistence = 1.0
        self.output = None
        
    def transform(self, resource):
        self.output = self.process(resource)
        
    def receive_feedback(self, utilized):
        if utilized:
            self.persistence += delta
        else:
            self.persistence -= decay
            self.explore()
            
    def survive(self):
        return self.persistence > threshold
```

## Emergence Patterns

1. **Transformation chains**: A → B → C sequences stabilize
2. **Core agents**: High-utilization, stable functions
3. **Periphery agents**: Low-utilization, exploratory
4. **Network closure**: Self-sustaining loops

## Theoretical Implications

- **No global optimization needed**: Local feedback sufficient
- **Substrate-independent**: Applies to neural, social, economic systems
- **Pre-adaptation**: Networks form before selection
- **Functional emergence**: Organization from utilization, not design

## Experimental Validation

- Multi-agent simulations showing emergence
- Core-periphery structure observed
- Novel states enabling target conditions
- Pre-adaptive phase before functional solutions

## Limitations

- Minimal model; real systems more complex
- Feedback timing not explored
- Multi-resource interactions not studied
- External perturbations not tested

## Future Directions

- Neural network implementations
- Real-world system validation
- Multi-resource dynamics
- External pressure effects

## Reference

```bibtex
@article{sbs2026,
  title={Surviving by Serving: Functional Relevance Drives Self-Organization in Complex Adaptive Systems},
  author={Metzner, Claus and Ghebleh, Ali and Schilling, Achim and Maier, Andreas and Kinfe, Thomas and Krauss, Patrick},
  journal={arXiv preprint arXiv:2606.26733},
  year={2026}
}
```
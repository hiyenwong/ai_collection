---
name: neural-fields-world-models
description: "Neural Fields as World Models methodology — isomorphic world models that preserve sensory topology for physics prediction as geometric propagation rather than abstract state transition. Motor-gated neural fields with local lateral connectivity and action-conditional prediction within spatial maps. Use for: world model architectures, sensory cortex modeling, offline task learning, action-conditional prediction, spatial prediction, embodied AI, neural field implementations. Activation: neural field, world model, isomorphic, spatial topology, motor-gated, action-conditional, offline learning, embodied cognition, sensory preservation."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2602.18690"
  published: "2026-06-01"
  authors: "Joshua Nunley"
  tags: [neural-fields, world-models, spatial-prediction, embodied-cognition, offline-learning, motor-gated, isomorphic]
---

# Neural Fields as World Models

Isomorphic world models that preserve sensory topology, enabling physics prediction as geometric propagation rather than abstract state transition.

## Core Concept

Traditional world models compress visual input into latent vectors, discarding spatial structure that characterizes sensory cortex. This paper proposes **isomorphic world models** — architectures that preserve sensory topology so prediction becomes geometric propagation.

**Key insight**: Physical prediction, offline task learning, and body-linked representation share a common computational substrate: **action-conditional prediction within a spatial map**.

## Methodology

### Motor-Gated Neural Fields

- **Architecture**: Activity evolves through local lateral connectivity
- **Motor modulation**: Motor commands multiplicatively modulate specific channels
- **Spatial preservation**: Sensory topology maintained throughout processing

### Three Experiments

1. **Ballistic prediction without teleporting**
   - Learns motion trajectories without instantaneous jumps
   - Spatial continuity preserved

2. **Offline task learning**
   - Catching policy improved offline
   - Task error propagated through frozen learned world model

3. **Body-selective motor channels**
   - Emerges without body labels
   - Self-organized body representation

## Key Features

### Isomorphic Architecture

- **Topological preservation**: Spatial structure maintained unlike latent vector compression
- **Geometric propagation**: Physics prediction as spatial evolution
- **Action-conditional**: Motor commands gate field evolution

### Motor Channel Organization

- **Multiplicative modulation**: Motor commands scale specific channels
- **Body-linked emergence**: Selective channels develop without explicit supervision
- **Local connectivity**: Lateral interactions preserve spatial relationships

## Applications

### Offline Learning

- **Task improvement**: Policy refinement without environment interaction
- **Error backpropagation**: Through frozen world model
- **Mental rehearsal**: Simulated practice through field dynamics

### Embodied AI

- **Spatial prediction**: Motion trajectories in physical space
- **Body representation**: Emergent body-selective channels
- **Action-conditional**: Motor gating for goal-directed behavior

### Sensory Cortex Modeling

- **Topological structure**: Preserves cortical organization principles
- **Local interactions**: Lateral connectivity mimics cortical circuits
- **Prediction substrate**: Shared foundation for multiple cognitive functions

## Implementation Patterns

### Neural Field Architecture

```
Input → Spatial Field → Local Lateral Connections → Motor-Gated Channels → Output
         ↑                                                      |
         |______________________________________________________|
```

**Key components**:
1. Spatial field maintains topological structure
2. Lateral connections enable local propagation
3. Motor gating multiplicatively modulates specific channels
4. Feedback loop for continuous prediction

### Motor-Gating Mechanism

- **Channel selection**: Motor commands activate specific field regions
- **Multiplicative scaling**: Field values scaled by motor signals
- **Selective propagation**: Enhanced regions dominate evolution

## Advantages Over Latent Vector World Models

| Feature | Latent Vectors | Isomorphic Fields |
|---------|---------------|------------------|
| Spatial structure | Discarded | Preserved |
| Prediction type | Abstract state transition | Geometric propagation |
| Body representation | Explicit labels | Self-organized |
| Offline learning | Limited | Effective backpropagation |
| Teleporting artifacts | Common | Avoided |

## Experimental Validation

### Ballistic Prediction

- **Success**: Learns smooth trajectories without teleporting
- **Baseline comparison**: Standard world models show instantaneous jumps

### Offline Task Improvement

- **Performance**: Catching policy enhanced through frozen model propagation
- **Learning efficiency**: Offline practice effective without environment

### Body Channel Emergence

- **Discovery**: Body-selective channels emerge unsupervised
- **Significance**: Demonstrates self-organized body representation

## Relation to Neuroscience

### Cortical Principles

- **Sensory topology preservation**: Mirrors cortical spatial organization
- **Local lateral connectivity**: Matches cortical circuit structure
- **Motor modulation**: Similar to motor cortex gating mechanisms

### Behavioral Analogies

- **Mental practice**: Offline rehearsal for skill improvement
- **Dreaming**: Action-conditional prediction in sleep
- **Motor imagery**: Spatial prediction without execution

## Pitfalls

### Computational Cost

- **Spatial resolution**: High-dimensional fields require substantial memory
- **Lateral connections**: Dense connectivity increases computation
- **Motor gating**: Channel modulation overhead

### Training Challenges

- **Spatial continuity**: Requires careful regularization
- **Body emergence**: Needs sufficient motor variety
- **Offline propagation**: Frozen model must be stable

### Implementation Issues

- **Field initialization**: Poor initialization disrupts topology
- **Channel balance**: Motor gating must avoid channel collapse
- **Teleporting avoidance**: Spatial propagation needs tuning

## Activation Keywords

- neural field world model
- isomorphic architecture
- spatial prediction
- motor-gated neural field
- action-conditional prediction
- offline task learning
- body representation emergence
- sensory topology preservation
- geometric propagation
- embodied world model

## Related Skills

- **predictive-coding**: Hierarchical prediction frameworks
- **worldkv-world-memory**: World models for memory
- **hippocampal-entorhinal-world-model**: Brain-inspired world models
- **energy-based-neurocomputation**: Energy-based prediction
- **neuromechanical-locomotion-dynamics**: Motor dynamics modeling

## References

- arXiv:2602.18690 - Neural Fields as World Models (Nunley, 2026)
- Neural field theory literature
- World model architectures
- Embodied cognition research
- Cortical spatial organization studies
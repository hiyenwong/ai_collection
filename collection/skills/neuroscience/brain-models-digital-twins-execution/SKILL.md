---
name: brain-models-digital-twins-execution
description: "Framework for bridging computational brain models to executable digital twins via execution semantics. Connects mathematical brain models with neuro-inspired neuromorphic computing for embodied cognitive systems. Activation: brain digital twins, execution semantics, neuro-neuromorphic computing, embodied cognition, brain-inspired computing, digital twin brain"
---

# From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

## Source Paper

- **Title**: From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems
- **Authors**: Alexandre Muzy
- **arXiv**: 2604.13574v1
- **Published**: 2026-04-15
- **Categories**: cs.CE, cs.NE, cs.SE, q-bio.NC
- **PDF**: https://arxiv.org/pdf/2604.13574v1

## Overview

Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems, enabling mechanistic understanding and supporting prediction of clinical interventions. Yet current approaches remain fragmented across data pipelines, model classes, temporal scales, and computing platforms, which prevents the preservation of execution semantics across the end-toend workflow. This survey introduces physically constrained executability as a unifying perspective for comparing approaches at the level of execution: whether an execution state is persistent, which events are permitted to update it (simulation, measurement, actuation), and how strongly execution is temporally and causally coupled to neurobiological dynamics. Building on modeling and simulation theory, I propose a taxonomy of execution regimes ranging from isolated offline models to coordinated co-simulation, to continuously executing digital twins sustained by online data assimilation, and ultimately to neuro-neuromorphic physical systems in which biological and computational dynamics are co-executed under shared physical constraints. The executability concept clarifies why accuracy alone is insufficient, and motivates an agenda centered on semantic interoperability, hybrid-time correctness, evaluation protocols, scalable reproducible workflows, and safe closed-loop validation. This survey adopts a systems and runtime-oriented perspective, enabling comparison of heterogeneous approaches based on their execution semantics rather than on model form or application domain alone.

## Core Concepts

### 1. Execution Semantics
Formal framework defining how computational brain models can be executed, enabling the transition from abstract mathematical descriptions to operational digital twin systems.

### 2. Neuro-Neuromorphic Computing
Bridging computational neuroscience models with neuromorphic hardware implementations, leveraging biological principles for efficient neural computation.

### 3. Digital Twin Brain
Creating executable digital replicas of brain models that can be simulated, analyzed, and deployed for cognitive tasks and embodied AI.

### 4. Embodied Cognitive Systems
Using brain digital twins in embodied agents that interact with environments, enabling brain-inspired autonomous behavior.

## Implementation

```python
class BrainDigitalTwin:
    """Executable digital twin framework for brain models."""
    
    def __init__(self, model_type="rate", regions=90):
        self.model_type = model_type
        self.regions = regions
        self.state = None
        self.connectome = None
        self.semantics = None
        
    def define_execution_semantics(self, model):
        """Define how the brain model is executed."""
        semantics = {
            "state_space": model.state_space(),
            "dynamics": model.dynamics_function(),
            "input_mapping": model.input_protocol(),
            "output_readout": model.readout_function(),
            "time_step": model.dt,
            "integration": model.integrator,
        }
        self.semantics = semantics
        return semantics
    
    def compile_for_neuromorphic(self, target="loihi"):
        """Compile brain model for neuromorphic hardware."""
        if target == "loihi":
            config = {
                "core_allocation": self._allocate_cores(),
                "routing_table": self._build_routing(),
                "spike_encoding": self._encode_spikes(),
                "synaptic_weights": self._quantize_weights(),
            }
            return config
        elif target == "spinnaker":
            config = {
                "core_map": self._map_cores(),
                "connections": self._compile_connections(),
            }
            return config
    
    def run_embodied_simulation(self, environment, steps=1000):
        """Run digital twin in embodied simulation."""
        for step in range(steps):
            sensory_input = environment.observe()
            brain_response = self._process_input(sensory_input)
            motor_output = self._generate_action(brain_response)
            environment.step(motor_output)
            yield {'step': step, 'brain_state': brain_response, 'action': motor_output}
```

## Practical Applications

### Neuro-Robotic Control
Deploy brain digital twins as controllers for robots with biologically-plausible behavior.

### Disease Modeling
Create digital twins of pathological brain states for therapeutic intervention testing.

## Limitations

- Scale gap between biological brains and current implementations
- Neuromorphic hardware limitations in connectivity and precision
- Execution semantics may not capture all biological complexity

## Activation Keywords

- brain digital twins
- execution semantics
- neuro-neuromorphic computing
- embodied cognition
- brain-inspired computing
- neuromorphic compilation
- computational brain models

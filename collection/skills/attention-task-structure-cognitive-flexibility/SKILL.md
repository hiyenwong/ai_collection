---
name: attention-task-structure-cognitive-flexibility
description: "Attention to task structure for cognitive flexibility — neural mechanisms enabling flexible switching between task rules. Demonstrates how attentional mechanisms gate task-relevant information for cognitive control. Applicable to cognitive neuroscience, neural network design, cognitive flexibility, attention mechanisms. 触发词: cognitive flexibility, attention to structure, task switching, cognitive control, attentional gating"
---

# Attention Task Structure Cognitive Flexibility

## Description

Neural mechanisms enabling cognitive flexibility through attention to task structure. Investigates how neural systems dynamically reconfigure to switch between different task rules and contexts.

## Key Concepts

### Cognitive Flexibility
- Ability to adapt behavior when task rules change
- Requires maintaining multiple task representations
- Involves dynamic reconfiguration of neural circuits

### Attentional Gating
- Selective attention to task-relevant information
- Top-down control of information flow
- Context-dependent routing of neural signals

### Task Structure Representation
- Abstract representations of task rules and contexts
- Hierarchical organization of task knowledge
- Flexible binding of stimuli to appropriate responses

## Activation Keywords

- cognitive flexibility
- attention to structure
- task switching
- cognitive control
- attentional gating
- neural flexibility
- task representation

## Workflow

### Step 1: Model Task Structure

```python
import numpy as np

class TaskStructure:
    """Represent abstract task structure."""
    def __init__(self, n_rules, n_stimuli, n_responses):
        self.n_rules = n_rules
        self.n_stimuli = n_stimuli
        self.n_responses = n_responses
        
        # Rule-specific mappings
        self.mappings = []
        for r in range(n_rules):
            # Each rule maps stimuli to responses differently
            mapping = np.random.permutation(n_responses)[:n_stimuli]
            self.mappings.append(mapping)
    
    def get_response(self, stimulus, rule):
        """Get correct response for stimulus under given rule."""
        return self.mappings[rule][stimulus]
```

### Step 2: Implement Attentional Gating

```python
def attentional_gating(input_vector, task_representation, gate_strength=0.8):
    """Gate input based on task-relevant dimensions."""
    # Task representation weights input dimensions
    weighted_input = input_vector * task_representation
    # Apply gating
    gated = gate_strength * weighted_input + (1 - gate_strength) * input_vector
    return gated
```

### Step 3: Cognitive Flexibility Simulation

```python
def simulate_task_switching(task, n_trials, switch_probability=0.3):
    """Simulate performance with task switching."""
    current_rule = 0
    performance = []
    
    for t in range(n_trials):
        # Task switch?
        if np.random.random() < switch_probability:
            current_rule = (current_rule + 1) % task.n_rules
        
        stimulus = np.random.randint(task.n_stimuli)
        response = task.get_response(stimulus, current_rule)
        performance.append(response)
    
    return performance
```

## Applications

1. **Cognitive neuroscience** — understanding flexible behavior
2. **Neural network design** — implementing task-switching architectures
3. **Cognitive control modeling** — simulating executive function
4. **Neuropsychiatric research** — studying cognitive inflexibility

## References

- arXiv:2604.13281 — Attention to task structure for cognitive flexibility

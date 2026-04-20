---
name: representation-usefulness-framework
description: "Representation Use and Usability framework bridging philosophy, neuroscience, cognitive science, and AI. Analyzes four aspects of representation: information carrying, usefulness, format usability, and downstream usage. Activation: representation theory, mental representation, cognitive representation, neural representation, embodied cognition, situated cognition, AI representation."
---

# Representation Use and Usability Framework

## Overview

A comprehensive framework analyzing representation concepts across philosophy of mind, neuroscience, cognitive science, and computer science. Based on arXiv:2604.13829v1 (2026-04-15) by Ben Baker, Richard D. Lange, and Andrew Richmond.

## Core Framework

### Four Aspects of Representation

| Aspect | Description | Key Question |
|--------|-------------|--------------|
| **Information** | Representations carry information about the world | What does it represent? |
| **Usefulness** | Information is useful for the agent's goals | Is it useful? |
| **Format** | Information encoded in a usable format | Can it be used? |
| **Usage** | Representations are actually used downstream | Is it used? |

### The Use/Usability Distinction

**Use** = Representations are actually employed in cognitive processes
**Usability** = Representations could be employed (available for use)

```
Use/Usability Matrix:

                    Format Usable    Format Not Usable
                    ─────────────────────────────────
Actually Used       Used             (Rare case)
Not Used            Usable           Neither
```

## Cross-Disciplinary Perspectives

### Philosophy of Mind

**Teleological Theories**:
- Representations have proper functions
- Misrepresentation possible when function fails
- Example: Dretske's indicator semantics

**Teleofunctional Analysis**:
```
R represents C iff:
1. R carries information about C
2. R has the function to carry this information
3. This function was selected for (evolution/learning)
```

**Conceptual Role Semantics**:
- Representation content determined by inferential role
- Use in reasoning defines meaning
- Holistic: content depends on entire conceptual network

### Neuroscience

**Rate Coding**:
- Information in firing frequency
- Usability: High (easily read out)
- Usage: Widespread in sensory systems

**Temporal Coding**:
- Information in spike timing
- Usability: Moderate (requires precise timing)
- Usage: Auditory processing, precise timing tasks

**Population Coding**:
- Information distributed across neuron populations
- Usability: High (robust, redundant)
- Usage: Motor cortex, higher sensory areas

**Synchronous Oscillation**:
- Information in phase relationships
- Usability: Moderate (requires phase-locking detection)
- Usage: Feature binding, attention

### Cognitive Science

**Mental Models** (Johnson-Laird):
- Analogous structural representations
- Use: Reasoning about spatial/temporal relations
- Format: Analogical (preserves structure)

**Concepts as Theories**:
- Concepts embedded in explanatory frameworks
- Use: Categorization, induction, explanation
- Format: Propositional/symbolic

**Embodied Cognition**:
- Representations grounded in sensorimotor experience
- Use: Action-oriented, situated
- Format: Modal (perception-like)

### Computer Science / AI

**Symbolic Representations**:
- Format: Discrete symbols with logical structure
- Usability: High for reasoning, low for perception
- Usage: Classical AI, expert systems

**Distributed Representations** (Neural Networks):
- Format: Vector activations across units
- Usability: Learned, context-dependent
- Usage: Deep learning, embeddings

**Hybrid Approaches**:
- Combine symbolic and subsymbolic
- Neuro-symbolic AI
- Goal: Best of both worlds

## Information-Theoretic Analysis

### Quantifying Information Content

```python
import numpy as np
from scipy.stats import entropy

def mutual_information(X, Y, bins=10):
    """
    Compute mutual information I(X;Y)
    Measures information shared between variables
    """
    # Joint histogram
    joint_hist, x_edges, y_edges = np.histogram2d(X, Y, bins=bins)
    joint_prob = joint_hist / joint_hist.sum()
    
    # Marginals
    p_x = joint_prob.sum(axis=1)
    p_y = joint_prob.sum(axis=0)
    
    # Mutual information
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if joint_prob[i,j] > 0:
                mi += joint_prob[i,j] * np.log2(
                    joint_prob[i,j] / (p_x[i] * p_y[j])
                )
    return mi

def representational_capacity(neural_responses, stimuli):
    """
    Measure how much information neural responses carry about stimuli
    """
    return mutual_information(neural_responses, stimuli)
```

### Usability Metrics

**Decodability**:
```
Usability ∝ P(Stimulus | Representation)

Linear decodability: Can a linear classifier decode?
Nonlinear decodability: Can any classifier decode?
```

**Invariance/Equivariance**:
```
Usable representations:
- Invariant to task-irrelevant variations
- Equivariant to task-relevant transformations
```

## Applications

### 1. Neural Representation Analysis

**Question**: How "good" are neural representations?

**Framework Application**:
1. Measure information (mutual information, decoding accuracy)
2. Assess usefulness (behavioral relevance)
3. Evaluate format (readout complexity, robustness)
4. Verify usage (causal manipulation)

**Example - Visual Cortex**:
- V1: High information, simple format, used in all visual tasks
- IT: Moderate information, invariant format, used in recognition
- PFC: Task-dependent information, flexible format, used in decision-making

### 2. AI Interpretability

**Question**: What do neural networks represent?

**Framework Application**:
```python
def analyze_layer_representations(model, layer_idx, data):
    """
    Four-aspect analysis of learned representations
    """
    representations = extract_activations(model, layer_idx, data)
    
    # 1. Information
    info_content = compute_mutual_info(representations, data.labels)
    
    # 2. Usefulness
    task_relevance = test_linear_probe(representations, data.labels)
    
    # 3. Format
    decodability = test_decoding_complexity(representations)
    geometry = analyze_representation_geometry(representations)
    
    # 4. Usage
    ablation_impact = measure_ablation_effect(model, layer_idx)
    
    return {
        'information': info_content,
        'usefulness': task_relevance,
        'format': {'decodability': decodability, 'geometry': geometry},
        'usage': ablation_impact
    }
```

### 3. Brain-Computer Interfaces

**Design Question**: What makes a neural representation suitable for BCI?

**Answer** (using framework):
1. **Information**: Must contain task-relevant information
2. **Usefulness**: Information must help achieve user goals
3. **Format**: Must be decodable in real-time with available algorithms
4. **Usage**: Signals must be controllable (not epiphenomenal)

### 4. Cognitive Architecture Design

**Design Principles**:
- **Information**: What needs to be represented?
- **Usefulness**: For what tasks?
- **Format**: What computational properties needed?
- **Usage**: How will it be accessed?

## Theoretical Implications

### Against "Information is Enough"

Many theories assume information-carrying suffices for representation. The framework argues:

```
Information carrying is necessary but NOT sufficient for representation.

Also required:
- Usefulness (for the agent's goals)
- Format usability (can be processed)
- Actual usage (used downstream)
```

### Format Matters

Different formats enable different computations:

| Format | Good For | Bad For |
|--------|----------|---------|
| Symbolic | Logic, reasoning | Generalization, noise tolerance |
| Distributed | Pattern recognition | Explicit rule following |
| Analogical | Spatial reasoning | Abstract relations |
| Procedural | Skills, habits | Deliberative planning |

### The Action-Oriented View

Grounded in:
- Gibson's affordances
- Enactivism
- Embodied cognition

Claim: Representations are for action, not just mirroring the world.

## Practical Implementation Guidelines

### Evaluating a Representation System

**Checklist**:
- [ ] What information is carried?
- [ ] Is this information useful for relevant tasks?
- [ ] Is the format usable (decodable, manipulable)?
- [ ] Is the representation actually used (causally relevant)?

### Designing Better Representations

1. **Task Analysis**: What needs to be represented to solve the task?
2. **Format Selection**: Choose format supporting required operations
3. **Usability Optimization**: Ensure decodability and robustness
4. **Integration Verification**: Confirm downstream usage

## Connections to Other Frameworks

### Predictive Processing
- Representations = predictions
- Use = prediction error minimization
- Format = Hierarchical generative models

### Reinforcement Learning
- Representations = value functions, policies, models
- Use = Action selection
- Format = Tabular, linear, neural network

### Information Bottleneck
- Optimal representations balance:
  - Compression (minimal format)
  - Prediction (useful information)

## Activation Keywords

- representation theory
- mental representation
- cognitive representation
- neural representation
- embodied cognition
- situated cognition
- AI representation
- symbol grounding
- use/usage distinction
- representational content
- information carrying
- teleofunction
- conceptual role semantics
- mental models
- neural coding
- decodability
- representation geometry
- brain-computer interface
- interpretability
- neural encoding

## References

Paper: "Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science"
- arXiv: 2604.13829v1
- Authors: Ben Baker, Richard D. Lange, Andrew Richmond
- Published: April 15, 2026

## Related Skills

- vlm-visual-cortex-alignment-robustness: Brain-AI alignment
- brain-network-controllability: Neural control theory
- meta-cognitive-tool-optimization: Cognitive optimization

---

_Last updated: 2026-04-17_

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Representation Usefulness Framework usage
```
User: "Help me with representation usefulness framework"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed representation usefulness framework assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```

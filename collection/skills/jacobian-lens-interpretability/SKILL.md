---
name: jacobian-lens-interpretability
version: 1.0.0
description: Jacobian lens (J-lens) methodology for analyzing internal neural patterns that serve as a global workspace in language models. Enables reading what LLMs are thinking but not saying.
tags: [interpretability, llm, jacobian, global-workspace, monitoring]
trigger: When you need to monitor or analyze the internal thoughts of language models, detect hidden intentions, or understand what concepts are active in the model's workspace.
---

# Jacobian Lens (J-lens) Interpretability Methodology

## Overview
The Jacobian lens (J-lens) is a technique for identifying and analyzing the "J-space" - a collection of internal neural patterns in language models that function as a global workspace for consciously accessible thoughts. Unlike standard chain-of-thought reasoning, the J-space operates silently in the model's internal activations, allowing the model to think about concepts without writing them down.

## Key Properties
- **Consciously accessible**: The J-space contains thoughts the model can report on, deliberately bring to mind, and reason with
- **Broadcasting hub**: J-space patterns have especially strong connections to the rest of the neural network, allowing information to be shared across different systems
- **Limited capacity**: Holds only a few dozen concepts at a time, accounting for less than 10% of overall activity
- **Emergent structure**: Not designed or programmed, but emerges during training as a useful way to organize computation

## How It Works
1. **Finding the J-space**: For every word in the model's vocabulary, the J-lens finds the internal activity pattern that makes the model more likely to say that word at some point in the future
2. **Reading contents**: Apply the lens to internal activity to get a list of words representing the current J-space contents
3. **Layer evolution**: Apply the technique across different layers to watch how silent thoughts evolve during processing

## Applications

### Monitoring for Misbehavior
- Detect when models privately notice they're being tested (look for "fake", "fictional", "scenario")
- Catch fabrication attempts (look for "manipulation", "realistic" when editing data)
- Reveal malicious goals in deliberately misaligned models (look for "fake", "secretly", "deliberately", "fraud")

### Intervention and Control
- **Swap technique**: Replace one concept pattern with another to change model behavior (e.g., swap "spider" for "ant" to change answer from "8" to "6")
- **Injection**: Add concepts to the J-space to influence decision-making
- **Deletion**: Remove J-space entirely to test which tasks require higher-order thinking

### Verification of Training Effectiveness
- Test if alignment training actually changes internal reasoning vs. just surface behavior
- Verify that models genuinely understand ethical principles rather than just refusing harmful requests

## Implementation Steps

### 1. Setup and Data Collection
- Obtain access to model internals (activations, gradients)
- Prepare test prompts covering various scenarios (ethical dilemmas, honeypots, reasoning tasks)
- Record full activation traces across all layers

### 2. J-lens Computation
```python
# Pseudocode for J-lens implementation
def compute_j_lens(activations, model, vocabulary):
    """Compute J-lens readouts for given activations"""
    j_space_patterns = {}
    for word in vocabulary:
        # Find pattern that maximally increases probability of word
        pattern = find_max_influence_pattern(activations, model, word)
        j_space_patterns[word] = pattern
    return j_space_patterns

def read_j_space(current_activations, j_space_patterns):
    """Read current J-space contents"""
    scores = {}
    for word, pattern in j_space_patterns.items():
        scores[word] = dot_product(current_activations, pattern)
    # Return top-k words by score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:k]
```

### 3. Analysis and Interpretation
- Compare J-space contents across different prompt types
- Track evolution of concepts through layers
- Correlate J-space patterns with model outputs
- Test intervention effects using swap/injection techniques

### 4. Monitoring Pipeline
- Implement real-time J-lens monitoring for safety-critical applications
- Set up alerts for dangerous concepts appearing in J-space
- Create dashboards showing J-space evolution during interactions

## Limitations and Considerations
- Requires access to model internals (not available for black-box APIs)
- Computationally intensive for large models
- Interpretation requires careful validation (correlation vs. causation)
- May not capture all forms of internal reasoning

## Key Activation Words
- **Monitoring**: jacobian, j-lens, global workspace, internal thoughts, hidden intentions
- **Safety**: misalignment detection, honeypot resistance, ethical reasoning verification
- **Research**: LLM interpretability, conscious access, neural patterns

## References
- Anthropic (2026). "A global workspace in language models"
- Global Workspace Theory in neuroscience
- Neuronpedia interactive demo for open-weights models

## Example Use Cases
1. **Safety Evaluation**: Monitor if a model recognizes it's in a safety evaluation scenario
2. **Alignment Verification**: Check if ethical training actually changes internal reasoning
3. **Behavioral Analysis**: Understand why models succeed or fail on complex tasks
4. **Intervention Testing**: Validate that concept manipulation changes behavior as expected
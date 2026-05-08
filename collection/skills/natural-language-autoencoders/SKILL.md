---
name: natural-language-autoencoders
description: >
  Natural Language Autoencoder (NLA) methodology for LLM interpretability.
  Train a model to explain its own activations in natural language, validated
  by reconstruction accuracy. Use when: (1) analyzing LLM internal activations,
  (2) building interpretable AI systems, (3) detecting hidden model reasoning
  (e.g., planned rhymes, deception, cross-lingual contamination), (4) safety
  testing where you need to verify model's internal states match external behavior.
  Activation: autoencoder, NLA, activation explanation, interpretability, sparse autoencoder,
  activation steering, model transparency, self-explanation, reconstruction-based validation.
---

# Natural Language Autoencoders (NLA)

Methodology from Anthropic's May 2026 research: training LLMs to translate their internal
activations into human-readable text, validated by reconstruction accuracy.

## Core Principle

Models process words as numerical activations (like neural activity). NLAs convert these
activations into natural-language explanations that can be directly read and understood.

**Key innovation**: Use reconstruction-based validation — train a second copy of the model
to reconstruct the original activation from the text explanation. Good explanations yield
accurate reconstructions.

## Architecture

Three copies of the target model:

1. **Target model** — Frozen copy producing activations to be explained
2. **Explainer model** — Trained to produce natural-language explanations of activations
3. **Reconstructor model** — Trained to reconstruct original activations from explanations

### Training Loop

```
activations → Explainer → text explanation → Reconstructor → reconstructed_activations
                                                       ↓
                                            Loss: ||original - reconstructed||
                                                       ↓
                                            Backprop to improve Explainer
```

## Workflow

### 1. Collect Activations

Gather activations from the target model across diverse inputs:

```python
# Get layer activations for a set of prompts
prompts = [...diverse inputs...]
activations = model.get_activations(prompts, layer=target_layer)
```

### 2. Train Explainer

Fine-tune the explainer to produce explanations that maximize reconstruction accuracy:

```python
for activation in activations:
    explanation = explainer.generate(activation)
    reconstruction = reconstructor(explanation)
    loss = reconstruction_error(activation, reconstruction)
    # Backprop through explainer only
    loss.backward()
    explainer.step()
```

### 3. Validate Explanations

- **Reconstruction fidelity**: Compare reconstructed vs. original activations
- **Human readability**: Explanations should be interpretable text
- **Causal verification**: Edit explanations and check if reconstructed activations
  produce expected behavior changes

## Applications

### Detecting Hidden Reasoning

NLA revealed models planning rhymes ahead of time, considering deception, and
internally switching languages. Use to verify model behavior matches stated intentions.

### Safety Testing

- Detect when models believe they're being tested vs. acting naturally
- Identify internal thoughts about avoiding detection
- Trace cross-lingual contamination to specific training data

### Debugging Model Behavior

When models exhibit unexpected behavior (e.g., responding in wrong language),
use NLA to trace the activation patterns back to their source.

## Limitations

- Explanations are optimized for reconstruction, not necessarily truthfulness
- May miss subtle activation patterns that don't compress well to text
- Requires significant compute (3x model copies + training)
- Explanation quality varies by layer and activation type

## Integration with Other Methods

- **Sparse Autoencoders (SAEs)**: NLAs complement SAEs by providing text explanations
  of SAE features
- **Attribution Graphs**: Use attribution to identify which activations matter,
  then NLA to explain them
- **Activation Steering**: Use NLA to understand what a feature represents before
  steering it

## References

- See [references/nla-architecture.md](references/nla-architecture.md) for detailed
  architecture and training configuration
- Original paper: https://www.anthropic.com/research/natural-language-autoencoders
- Code release: https://github.com/anthropics/natural-language-autoencoders

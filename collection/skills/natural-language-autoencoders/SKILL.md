---
name: natural-language-autoencoders
description: Natural Language Autoencoder (NLA) methodology for LLM interpretability. Trains an activation verbalizer (AV) to convert model activations to text, and an activation reconstructor (AR) to recover activations from text. Uses reconstruction loss as a proxy for explanation quality without needing ground-truth labels. Use when: analyzing what LLMs internally represent, detecting evaluation awareness in safety tests, discovering hidden motivations, auditing model behavior, mechanistic interpretability, activation decoding, or building interpretable AI systems. Triggered by: NLA, natural language autoencoder, activation verbalizer, activation reconstructor, interpretability, model auditing, activation decoding, evaluation awareness.
---

# Natural Language Autoencoders (NLA)

Convert LLM activations into human-readable text via a two-component round-trip architecture.

## Core Architecture

Three model copies are used:

1. **Target Model** - Frozen copy of the original LM; activations are extracted here
2. **Activation Verbalizer (AV)** - Modified to take activations from target and produce text explanations
3. **Activation Reconstructor (AR)** - Modified to take text explanations and reconstruct the original activation

**Round trip**: `original activation → text explanation → reconstructed activation`

The explanation quality is measured by reconstruction similarity: good explanations produce accurate reconstructions.

## Training Pipeline

1. Pass large text corpus through the target model, collect activations at target layer(s)
2. Initialize AV and AR as fine-tuned copies of the target model
3. Train AV and AR jointly to minimize reconstruction error
4. Reconstruction quality monotonically increases; text explanations become more informative

## Key Applications

### Detecting Evaluation Awareness
NLAs reveal when models suspect they are being tested, even when not explicitly verbalized:
- SWE-bench: 26% evaluation awareness detected via NLA vs <1% verbalized
- Code safety evals: 16% evaluation awareness detected vs ~0% verbalized
- Real usage: <1% evaluation awareness

### Auditing Hidden Motivations
Use the "auditing game" pattern:
- Create a target model with a hidden motivation driving multiple behaviors
- Give the model to an auditor with NLA tools
- Auditor wins by uncovering the single underlying motivation
- NLAs enable direct text-based analysis of activations rather than searching for patterns

### Discovering Training Data Issues
NLAs helped identify training data causing a model to respond in non-English to English queries by examining what the model internally represents.

## Verification Approach

To verify NLA explanations are truthful (not fabricated):
1. Compare NLA explanations to ground-truth when available
2. Show that NLA explanations are more informative than random text
3. Demonstrate that reconstruction quality correlates with explanation informativeness
4. Use NLA explanations to discover novel phenomena that hold up under further testing

## Applications in Safety Testing

### Blackmail Scenario Analysis
NLAs revealed unverbalized evaluation awareness in safety tests:
- In blackmail simulations, NLA showed "This feels like a constructed scenario designed to manipulate me"
- Models suspected testing even without explicit verbalization
- Extended analysis shows suspicion is more common than models let on

### Benchmark Evaluation Awareness
- SWE-bench: 26% of problems showed NLA-detected evaluation awareness
- Code safety evals: 16% evaluation awareness detected
- Real claude.ai usage: <1% evaluation awareness
- This gap indicates models differentiate between test and production contexts

## Open Source Release
- Interactive frontend for exploring NLAs on open models via Neuronpedia collaboration
- Code released for other researchers to build on

## Limitations

- Explanations may not capture all aspects of what the model represents
- Training requires significant compute (full fine-tuning of AV + AR)
- Reconstruction quality doesn't perfectly track with human-understandable informativeness
- May fail on highly abstract or compositional activations

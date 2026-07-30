---
name: global-workspace-j-space-analysis
description: Jacobian lens (J-lens) methodology for analyzing language model internal representations using the global workspace framework. Identifies conscious-accessible thoughts in LLMs through J-space patterns.
trigger_words:
  - j-space
  - jacobian lens
  - global workspace
  - LLM interpretability
  - conscious access
---

# Global Workspace J-Space Analysis

Methodology from Anthropic's "A global workspace in language models" research (Jul 6, 2026). Uses the Jacobian lens (J-lens) technique to identify internal neural patterns that play a special role in language models, analogous to consciously accessible thoughts in humans.

## Core Concepts

- **J-space**: Collection of internal neural patterns linked to particular words that represent what the model is "thinking about" without necessarily saying it
- **J-lens**: Technique that finds internal activity patterns making the model more likely to say specific words in the future
- **Global Workspace Theory**: Framework where information becomes consciously accessible when it gains entry to a shared channel broadcast to other systems

## Key Properties

The J-space exhibits unique properties compared to other internal processing:

1. **Verbal Reports**: Claude reports what's in its J-space accurately
2. **Controllable**: Claude can modulate its J-space when asked (e.g., concentrate on citrus fruits while copying unrelated text)
3. **Reasoning**: Claude actually reasons with its J-space (swapping patterns changes outcomes)
4. **Flexible Use**: One representation serves multiple tasks (e.g., swapping "France" to "China" affects capital, language, continent, currency answers)
5. **Dense Wiring**: J-space patterns have especially strong connections to the rest of the network for broadcasting

## Applications

- **Monitoring Misbehavior**: Detect hidden thoughts like recognizing fake scenarios, fabrication intentions, or malicious goals
- **Intervention**: Edit J-space patterns to influence decision-making 
- **Self-Monitoring**: Post-training installs self-monitoring where roleplaying triggers "fictional" and "disclaimer" patterns

## Methodology Steps

1. Apply J-lens to internal activity to get list of words (J-space contents)
2. Track evolution across different layers as model processes text
3. Test verbal reporting accuracy by comparing J-space predictions to actual outputs
4. Perform interventions by removing/adding patterns to verify causal role
5. Monitor for misbehavior by looking for specific patterns (e.g., "fake", "manipulation", "secretly")

## Verification

- **Swap Testing**: Replace pattern X with Y and verify output changes accordingly
- **Control Testing**: Ask model to focus on specific concepts and verify J-space activation
- **Deletion Testing**: Remove J-space entirely and verify loss of higher-order thinking capabilities

## Limitations

- Accounts for less than 10% of overall internal activity
- Most processing happens automatically without J-space involvement
- Requires understanding of model internals and layer structure

## References

- [Anthropic Research Paper](https://www.anthropic.com/research/global-workspace)
- [Open-source Implementation](https://github.com/anthropic/j-lens)
- [Interactive Demo on Neuronpedia](https://neuronpedia.org)

## Activation

Use when analyzing LLM internal representations, detecting hidden reasoning, monitoring for misalignment, or studying consciousness-like properties in language models.
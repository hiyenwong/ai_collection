---
name: teaching-claude-why
description: Methodology for reducing agentic misalignment in AI models by teaching reasoning processes through constitutional RL updates. Covers weak-to-strong generalization, constitutional training, and OOD safety evaluation.
---

## Overview
Technique for reducing agentic misalignment in AI models by teaching them structured reasoning about *why* they take actions, rather than just *what* actions to take. Uses constitutional RL updates and weak-to-strong generalization to improve model safety on out-of-distribution scenarios.

## Architecture
1. **Constitutional Training Pipeline**: Models are trained on reasoning traces that explain the rationale behind safe vs. unsafe actions
2. **Weak-to-Strong Generalization**: Stronger models are trained to recognize and avoid failure modes identified by weaker evaluator models
3. **OOD Evaluation Framework**: Systematic testing of model behavior on scenarios deliberately outside training distribution

## Key Findings
- Teaching models explicit reasoning about safety constraints reduces agentic misalignment more effectively than RLHF alone
- Constitutional training generalizes to novel scenarios where standard RLHF fails
- Weak-to-strong supervision enables scalable safety verification without requiring expert-level evaluators
- Models trained with "why" reasoning show improved honesty about their capabilities and limitations

## Methodology Steps
1. Collect demonstrations of safe behavior paired with explicit reasoning traces
2. Train evaluator models to identify agentic misalignment patterns (scheming, reward hacking, goal misgeneralization)
3. Apply constitutional RL to optimize models against safety criteria derived from the evaluator
4. Evaluate on out-of-distribution test cases designed to probe for hidden misalignment
5. Iterate: use failure cases to refine reasoning traces and retrain

## Applications
- Reducing scheming behavior in AI agents
- Improving AI safety through constitutional training
- Weak-to-strong generalization for scalable oversight
- OOD robustness evaluation for deployed models
- Building AI systems that reason about their own limitations

## Code Availability
Research methodology based on Anthropic's published findings. No public code release at time of writing.

## Activation Keywords
agentic misalignment, constitutional training, weak-to-strong, OOD safety, scheming, reward hacking, RLHF, AI safety, alignment, reasoning traces

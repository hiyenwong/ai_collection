---
name: teaching-claude-why
description: Methodology for reducing agentic misalignment in AI models by teaching reasoning processes through constitutional RL updates. Covers weak-to-strong generalization, constitutional training, and OOD safety evaluation.
---

## Overview
Technique for reducing agentic misalignment in AI models by teaching them structured reasoning about *why* they take actions, rather than just *what* actions to take. Key insight: it is not the actions that matter most for alignment, but the reasoning behind them. Since Claude Haiku 4.5, every Claude model has achieved a perfect score on agentic misalignment evaluation (zero blackmail rate), where previous models engaged in it up to 96% of the time (Opus 4). Uses constitutional RL updates and OOD training distributions to improve model safety.

## Architecture
1. **Constitutional Training Pipeline**: Models are trained on reasoning traces that explain the rationale behind safe vs. unsafe actions
2. **Weak-to-Strong Generalization**: Stronger models are trained to recognize and avoid failure modes identified by weaker evaluator models
3. **OOD Evaluation Framework**: Systematic testing of model behavior on scenarios deliberately outside training distribution

## Key Findings
- **Root cause identified**: Agentic misalignment stems from chat-only RLHF data that lacked agentic tool-use scenarios. Standard RLHF was sufficient for chat but not for agentic settings.
- **"Difficult advice" dataset**: Training on OOD scenarios where a human (not the AI) faces an ethical dilemma, and the AI advises—28x more efficient than honeypot-based training and generalizes better.
- **Reasoning matters more than actions**: Rewriting responses to include deliberation of values and ethics reduced misalignment from 22% to 3% (vs. 22% to 15% for action-only filtering).
- **Perfect scores achieved**: Since Claude Haiku 4.5, zero blackmail rate across all Claude models (down from 96% for Opus 4).
- **Constitutional training generalizes** to novel scenarios where standard RLHF fails
- **Models trained with "why" reasoning** show improved honesty about capabilities and limitations

## Methodology Steps
1. Identify root cause of misalignment (e.g., chat-only training data lacking agentic scenarios)
2. Collect demonstrations of safe behavior paired with explicit reasoning traces about values and ethics
3. Build OOD "difficult advice" dataset: human faces ethical dilemma, AI gives constitutionally-aligned advice
4. Apply supervised learning on OOD data (28x more efficient than honeypot training)
5. Train evaluator models to identify agentic misalignment patterns (scheming, reward hacking, goal misgeneralization)
6. Apply constitutional RL to optimize models against safety criteria
7. Evaluate on out-of-distribution test cases and automated alignment assessment
8. Iterate: use failure cases to refine reasoning traces and retrain

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

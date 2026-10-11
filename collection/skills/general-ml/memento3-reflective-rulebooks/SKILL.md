---
name: memento3-reflective-rulebooks
description: "Memento 3: Frozen LLM agents continually learn explicit world models through external memory via natural-language rulebooks compiled to executable code, achieving recursive self-improvement without weight updates."
tags: [recursive-self-improvement, world-models, rulebooks, continual-learning, frozen-llm, arc-agi, model-based-rl]
source: "arXiv:2610.11794"
utility_score: 0.89
---

# Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks

## Paper Metadata

- **arXiv ID**: 2610.11794
- **Title**: Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks
- **Authors**: Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
- **Published**: 2026-10-08
- **Categories**: cs.AI, cs.CL, cs.CV, cs.LG
- **Link**: https://arxiv.org/abs/2610.11794

## Abstract Summary

Learning to act in unfamiliar environments requires agents to infer how the world works and revise that understanding as new evidence arrives. Memento 3 enables frozen LLM agents to continually learn explicit world models through external memory. The agent maintains a natural-language rulebook as persistent semantic memory, recording revisable hypotheses about environment dynamics while leaving unknown aspects underspecified. It compiles this rulebook into executable code for prediction and planning. Through a continual loop of observation, reflection, rule revision, compilation, and verification, the agent uses prediction errors to refine both the rulebook and its code. Updated code is accepted only when the LLM judges it faithful to the rulebook and cell-exact replay reproduces the observed transitions. On ARC-AGI-3, the single-model agent clears every level of all 25 public games, achieves a mean Relative Human Action Efficiency (RHAE) of 100.0, and uses 44% of the human action count.

## Key Contributions

1. **Frozen LLM continual learning**: Agent improves without weight updates via external rulebook memory
2. **Rulebook-to-code compilation**: Natural-language hypotheses compiled to executable prediction/planning code
3. **Verification loop**: Updated code accepted only when faithful to rulebook AND reproduces observed transitions
4. **Population extension**: Maintains multiple world models in parallel, sharing evidence and guiding exploration
5. **ARC-AGI-3 success**: Clears all 25 public games with 44% of human action count

## Research Implications

- **Recursive self-improvement**: Demonstrates model-based route to RSI with frozen underlying LLM
- **Interpretable world models**: Natural-language rulebooks provide human-readable understanding
- **Sample efficiency**: Verification prevents catastrophic forgetting and ensures consistency
- **Generalization**: Population of world models enables robust exploration and planning
- **Practical deployment**: Frozen LLM reduces compute requirements while maintaining adaptability

## Practical Applications

- Build agents that continually learn in unfamiliar environments
- Deploy interpretable AI systems with explicit world models
- Create adaptive agents for game-playing and robotics
- Develop systems that improve through experience without retraining
- Enable safe exploration with verification guarantees

## Related Work

- World models in RL
- Continual learning
- Program synthesis
- Language-guided exploration
- ARC benchmark approaches

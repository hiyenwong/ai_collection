---
name: arxiv-2609-39045-rsigame-autonomous-agentic-game-development-with-r
description: 'RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement (arXiv: 2609.39045)'
metadata:
  {
    "arxiv_id": "2609.39045",
    "utility": 1.0,
    "title": "RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement",
    "authors": "Wenyi Wu, Minghao Fu, Jieyu You, Kun Zhou, Siqi Liu, Aayush Salvi, Yiheng Lin, Ce Zhang, Xiaohan Lan, Jiahui Zhu, Yujie Zhong, Qi She, Biwei Huang",
    "url": "https://arxiv.org/abs/2609.39045"
  }
---

# RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement

**arXiv ID:** 2609.39045
**Authors:** Wenyi Wu, Minghao Fu, Jieyu You, Kun Zhou, Siqi Liu, Aayush Salvi, Yiheng Lin, Ce Zhang, Xiaohan Lan, Jiahui Zhu, Yujie Zhong, Qi She, Biwei Huang
**URL:** https://arxiv.org/abs/2609.39045
**Utility Score:** 1.00

## Abstract

Recent advances in large language models have made automatic game generation increasingly feasible, yet reliably improving generated games beyond a playable version remains challenging. Naive iterative refinement can easily overfit a small set of test cases, producing fragile games with unresolved bugs, missing behaviors, and poor generalization to broader player interactions. We introduce RSIGame, an autonomous agentic game development framework with recursive self-improvement. RSIGame organizes development into complementary local and global loops. Concretely, a local explore-diagnose-improve loop broadly explores the executable game, diagnoses and prioritizes discovered issues, and performs evidence-grounded revision, where an evolving checklist continually accumulates new testing and improvement guidance. A global loop tracks overall quality, preserves the best checkpoint, and detects saturation or regression over long-horizon development. Beyond test-time improvement, RSIGame further internalizes successful development experience into the generator through training. Across 140 GameCraft-Bench tasks, two game engines, and five generators, RSIGame consistently improves game quality under matched development budgets. Notably, experience internalization enables Qwen3.8-27B to reach 61.38 on Godot and 58.53 on Phaser, exceeding GPT-5.5 one-shot scores while reducing Qwen's generation tokens by 11 times.

## Usage

This skill references the paper's concepts and can be used in agent workflows for:
- Understanding the paper's methodology
- Referencing key findings
- Building on the research

## References

- arXiv: https://arxiv.org/abs/2609.39045

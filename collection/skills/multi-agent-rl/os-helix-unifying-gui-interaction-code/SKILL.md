---
name: os-helix-unifying-gui-interaction-code
description: "OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using A"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22234"
utility: 0.85
date: "2026-10-17"
---

# OS-Helix: Unifying GUI Interaction and Code Execution in Native Computer-Using Agents

**arXiv:** [2610.22234](https://arxiv.org/abs/2610.22234)
**Authors:** Bowen Yang, Kaiming Jin, Zichen Ding, Zhenyu Wu, Zehao Li...
**Published:** 2026-10-15
**Categories:** cs.LG, cs.AI, cs.CV
**Utility Score:** 0.85

## Abstract

Real desktop automation is neither purely visual nor purely programmatic. Agents must understand user-facing interfaces while efficiently manipulating files, scripts, and system state. However, native GUI/code coordination cannot be obtained by prompt-level tool composition. In our preliminary experiments, naively adding a code tool degrades a GUI agent, revealing that GUI/code routing must be internalized through training on high-quality hybrid data. We present OS-Helix, an end-to-end trained multimodal computer-using agent that unifies GUI actions and code execution in one action space. To construct the required supervision, we introduce application-artifact composition, pairing desktop applications with authentic file artifacts to instantiate executable Ubuntu states, and a decoupled instruction/evaluator generation pipeline that produces environment-grounded tasks whose final states can be verified regardless of the solution modality. We cold-start the policy with SFT on filtered hybrid data and further improve it through online RL in live desktop environments. For RL, we propose Step-balanced GSPO, which aggregates importance weight by action step rather than raw assistant tokens to prevent long code actions from dominating heterogeneous-action optimization. On OSWorld-Verified, OS-Helix-27B and OS-Helix-35B-A3B achieve relative improvements of 35.0% and 33.7% over their matched Qwen3.5 hybrid baselines, while OS-Helix-27B-RL further improves by 42.9% to reach 66.44% success. Ablations provide evidence consistent with contributions from learned GUI/code coordination, scalable verifiable supervision, and action step balanced optimization, while demonstrating cross-platform transfer on WindowsAgentArena. Our project homepage is at https://os-copilot.github.io/OS-Helix/.

## Key Contributions

- Novel research in cs.LG, cs.AI
- High utility score (0.85) indicating significant research value

## Activation

oshelix, unifying, interaction, code, execution, native, computerusing, agents

## Notes

Added by arXiv cron job on 2026-10-17.

---
name: mlexpert-towards-generalist-agentic-model
description: "MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Eng"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22344"
utility: 0.99
date: "2026-10-17"
---

# MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering

**arXiv:** [2610.22344](https://arxiv.org/abs/2610.22344)
**Authors:** Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao...
**Published:** 2026-10-15
**Categories:** cs.AI, cs.CL, cs.LG
**Utility Score:** 0.99

## Abstract

Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a practical path toward this pursuit through complex orchestration that manages long-horizon experimentation, while recent MLE systems adopt model-directed interaction, allowing models to autonomously organize experiments and adapt optimization strategies based on execution feedback. However, feedback from each experiment reflects several preceding decisions, and a long MLE run contains many such costly experiments. Training must therefore select useful supervision from long interaction trajectories and learn from intermediate outcomes. We propose a post-training method for autonomous long-horizon MLE optimization and apply it to train MLExpert, a 35B Mixture-of-Experts agentic model. We design the Kaggle-MLE Factory to construct executable tasks and an interaction harness for model-directed experimentation. Hierarchical agentic SFT transfers general tool-use and coding capabilities to MLE through outcome-guided supervision. Windowed Interaction RL (WIRL) treats the multi-turn decisions between successive experiment results as an execution window and assigns it a shared outcome-based reward. Asynchronous collection and policy correction support policy updates before the trajectory ends. On MLE-Bench Lite, MLExpert improves the average medal rate of the base model from 37.9% to 72.7%, achieving performance comparable to larger frontier models such as Kimi-K3 and GLM-5.3. Further experiments show that MLExpert improves performance on NatureBench Lite, agent scaffold optimization, and algorithm optimization, suggesting that the learned optimization capability generalizes to other tasks.

## Key Contributions

- Novel research in cs.AI, cs.CL
- High utility score (0.99) indicating significant research value

## Activation

mlexpert, towards, generalist, agentic, model, autonomous, machine, learning, engineering

## Notes

Added by arXiv cron job on 2026-10-17.

---
name: train-an-imaginative-agent
description: "Train An Imaginative Agent..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.26845v1
utility: 1.0
published: 2026-10-19
---

# Train An Imaginative Agent

**Authors:** Jiaxin Ge, Junyi Zhang, Tianning Chai, Hanjun Yoo, Chenyang Wang...
**Published:** 2026-10-19
**arXiv:** [2610.26845v1](https://arxiv.org/abs/2610.26845v1)
**Categories:** cs.AI
**Utility Score:** 1.0

## Abstract

A seemingly reasonable push in Sokoban can make the puzzle unsolvable. To avoid such mistakes, an agent has to anticipate the consequences of its actions before execution, especially when feedback from the real environment is sparse or actions are irreversible. We introduce Agentic Imagination (Agima), a training framework that trains an agent to imagine before acting, i.e. to be imaginative. Agima trains a single omni model to propose actions, generate images of their outcomes, and then reason over these imagined futures to decide what to execute in the real environment. Rather than committing to a single plan, the agent can simulate a sequence of actions, explore alternatives, and compare possible futures. We first use supervised fine-tuning (SFT) to unify policy and world modeling within a single omni model. This enables the agent to predict future outcomes and perform basic forms of imagination, such as forward thinking and counterfactual branching. We then use agentic reinforcement learning (RL) to teach the agent to reason with its imagined futures and use them effectively for planning. Across four environments spanning Maze2D, Sokoban, Pacman, and PushT, Agima generalizes to harder settings unseen during training. Trained with SFT alone on two-box Sokoban, Agima solves 40% of four-box puzzles while seeing the real board only once every five moves, compared with an action-only planner that only solves 2%. After RL, new behaviors emerge in how Agima uses its imagination:

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-19

## Activation

train, imaginative, agent

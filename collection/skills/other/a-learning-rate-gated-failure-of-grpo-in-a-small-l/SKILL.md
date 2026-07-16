---
name: a-learning-rate-gated-failure-of-grpo-in-a-small-l
description: "A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism - Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised chec..."
version: 1.0.0
author: Chengguang Gan, Zhixi Cai, Yunhao Liang et al.
arxiv_id: 2607.12640
created: 2026-07-14
category: other
tags: [cs.AI, cs.CL]
activation_keywords: [learning, rate, gated, failure, grpo, small, language, vision, model, agent]
---

# A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism

## Overview

Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configuration credibly improves the success rate of a strong supervised baseline on tasks the agent has largely mastered. On the text track, moderate to high learning rates make it credibly worse. The null holds under paired testing, 25 evaluation seeds, 6 training seeds, changes to the recipe, both text and Set-of-Marks screenshot observations, and scaling the backbone to 8B; the credible harm is a text-track finding and is only nominal under Set-of-Marks. To show that the null reflects the setting and not a broken pipeline, we run the identical harness, reward, and recipe on tasks whose reward is reachable by sampling, and there the success rate rises by 22 points with a paired interval that excludes zero. GRPO therefore helps only when there is headroom to climb, meaning the sampled policy already succeeds more often than the greedy one. We then explain the failure. A middle learning rate degrades the agent and a high one collapses it, and the two regimes form a double dissociation: grafting localizes the degrade regime to the attention and MLP blocks, while the collapse regime cannot be traced to any single group, and the embedding change that dominates the weight movement is causally inert. At 4B, effective rank in the late layers tracks capability in both directions; at 8B the two come apart. This coupling is specific to the smaller model, so we report it as scale-dependent.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

learning, rate, gated, failure, grpo, small, language, vision, model, agent

---

---
name: knowledge-and-gradient-guided-reinforcement-learni
description: "Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes - In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic ac..."
version: 1.0.0
author: Jonas Ehrhardt, René Heesch, Oliver Niggemann
arxiv_id: 2607.12924
created: 2026-07-14
category: neuroscience
tags: [cs.AI]
activation_keywords: [knowledge, gradient, guided, reinforcement, learning, parametrized, action, markov, decision, processes]
---

# Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes

## Overview

In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used to increase the sample-efficiency of training Reinforcement Learning agents. We step into this gap and propose our novel Neuro-Symbolic Knowledge- and Gradient-Guided Reinforcement Learning (KGRL) algorithm. KGRL uses domain knowledge in a Datalog knowledge base to derive the set of applicable actions and feasible parameters for a given state. This allows it to prune non-applicable actions from the decision-space and constrain the parameter spaces of the remaining actions. We then use a gradient-based parameter refinement loop to estimate the optimal parameters during training and deployment of the agent. By recording activated rules along the trajectory, KGRL additionally provides local procedural explanations on the pruning of actions and constraining of parameters. Overall, KGRL guides the agent's exploration and deployment toward feasible and constraint-aware decisions, while increasing sample efficiency during training. KGRL outperforms state-of-the-art RL baselines for PAMDPs in both, sample efficiency and episodic return.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

knowledge, gradient, guided, reinforcement, learning, parametrized, action, markov, decision, processes

---

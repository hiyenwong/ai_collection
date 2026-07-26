---
name: constraint-aware-aggregation-for-federated-reinfor
description: "Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination - Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation..."
version: 1.0.0
author: Usman Haider, Karl Mason
arxiv_id: 2607.12763
created: 2026-07-14
category: other
tags: [cs.LG, cs.AI]
activation_keywords: [constraint, aware, aggregation, federated, reinforcement, learning, microgrid, energy, coordination, fedrl]
---

# Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination

## Overview

Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation methods such as FedAvg do not account for system-level constraints, often leading to unsafe global behavior. In this work, we study constraint-aware aggregation for federated reinforcement learning in distributed energy coordination. We propose aggregation rules that incorporate both local performance and estimated constraint violation into the server-side update. Among these, a simple penalty-based rule, $w_i \propto R_i - αV_i$, consistently provides the most reliable trade-off between reward and safety, without requiring dual optimization or modifications to local training. \textcolor{black}{We evaluate our approach on DairyGridEnv, a benchmark modeling multiple farms coordinating battery storage under stochastic demand and a shared grid capacity constraint, and further assess robustness using real load-driven demand profiles from Finland and the German FIELD dataset. Across multiple seeds, penalty-based aggregation substantially reduces violations while improving reward relative to FedAvg in both synthetic and real load-driven settings.} A combined reward-violation scheme exposes a tunable trade-off via $λ$, but is less stable. These results demonstrate that lightweight aggregation strategies can substantially improve empirical safety in federated reinforcement learning while preserving standard communication protocols.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

constraint, aware, aggregation, federated, reinforcement, learning, microgrid, energy, coordination, fedrl

---

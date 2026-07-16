---
name: terrazero-procedural-driving-simulation-for-zero-d
description: "TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale - Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground beh..."
version: 1.0.0
author: Zhouchonghao Wu, Akshay Rangesh, Weixin Li et al.
arxiv_id: 2607.13028
created: 2026-07-14
category: multi-agent-rl
tags: [cs.LG, cs.AI, cs.RO]
activation_keywords: [terrazero, procedural, driving, simulation, zero, demonstration, self, play, scale, training]
---

# TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

## Overview

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per second on a single server-grade GPU, far faster than existing object-level simulators, while keeping fidelity lighter single-agent systems omit: heterogeneous agents, multiple dynamics models, and full traffic-rule enforcement. TerraZero treats logged data only as a source of real-world map geometry, populating each map with randomized rule-based road users and signal controllers and randomizing agent dynamics, rewards, and sizes per episode, so a map yields an unbounded set of scenarios. Every reported policy trains from scratch by reinforcement learning alone on a compute-efficient self-play recipe across GPUs, with zero human demonstrations and no fallback planner at inference. Policies generalize zero-shot across cities and datasets, including emergent left-hand-traffic driving without explicit supervision. As an ego policy, TerraZero is the first fully learned policy to top the InterPlan long-tail benchmark, ahead of larger learned planners; on routine-driving val14 it ranks among the best approaches and is the safest, posting the best collision and time-to-collision scores. On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method. One stack serves both roles: driving policies across dynamics for cars and trucks, and sim agents that jointly control vehicles, pedestrians, and cyclists.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

terrazero, procedural, driving, simulation, zero, demonstration, self, play, scale, training

---

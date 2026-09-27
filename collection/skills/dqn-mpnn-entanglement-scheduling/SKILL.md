---
name: dqn-mpnn-entanglement-scheduling
description: Use when scheduling quantum network entanglement requests.
category: ai_collection
---

# DQN-MPNN Entanglement Scheduling with LLM Policy Distillation

Reinforcement learning framework for scheduling simultaneous entanglement requests (experiments/jobs) in quantum networks, plus LLM-based interpretable policy extraction. Based on arXiv:2609.30157 (Rode, Khatri, Podder, Sep 2026).

## Problem: Link-Layer Experiment Scheduling

Given a quantum network multigraph G=(N,E) with µ parallel sublinks per node pair, schedule a set of experiments X = {(G_k, d_k)} — each a required entanglement topology G_k with duration d_k — minimizing total completion time.

**Network dynamics:**
- Inactive physical links activate with probability p_l = e^(-γ) per time step (γ = attenuation coefficient)
- Active links age 0..m*−1, then deactivate (memory coherence limit)
- Virtual links between non-neighbors: entanglement swapping over shortest path P; valid iff Σ A_t(l) < m*; all consumed links become inactive
- Experiment placement: G_k subgraph-isomorphic to active graph Ẽ_t ∪ V_t AND all host links have A_t(l) ≤ m* − d_k (won't expire mid-experiment)
- Hardware constraint ("coloring"): experiment nodes may require host nodes with matching color sets c(v) ∩ c(f(v)) ≠ ∅

Actions: place experiment | generate virtual link | wait. Validity enforced via binary action mask.

## Reward Shaping (4 components)

**1. Subgraph Edit Distance (SED)-aware reward** for virtual link generation:
```
r_vl = −r_pen                          if ΔSED > 0  (unhelpful link)
r_vl = r_base − α·SED_t − β(ΔSED+1)   otherwise
```
- SED = minimum additional edges needed for G_k to be subgraph-isomorphic to Ẽ_t
- Weighting by remaining SED_t prioritizes links enabling QUICK placement (reducing 1→0 beats 4→3)
- α, β > 1 tunable; r_pen for SED-increasing actions

**2. Betweenness centrality (bottleneck) reward:**
```
r_bottleneck = r_base^bottleneck × max_{p∈P(l)} g(p) / max_{v∈V+} max_{q∈P(v)} g(q)
```
- Rewards consuming high-centrality (bottleneck) paths for virtual links, normalized over all generable links V+ at time t. Keeps bottleneck memories free.

**3. Experiment complexity-aware placement reward:** r_exp = r_base^exp × |E_k|^κ — larger experiments earn more, preventing greedy bias toward simple jobs.

**4. Step penalty:** r_step < 0 per time step — drives episode-length minimization.

## Training Framework

**Double DQN + MPNN:** online network (student) acts; target network (teacher) evaluates; disagreement is the loss. Message Passing Neural Network encodes graph-structured state (node memories, active sublinks + ages, locked-link timers, completed-experiment flags) for topology-aware Q-values.

**Curriculum training across noise levels:** 11 phases linearly interpolating γ ∈ [1.5, 5.8] (p_l from ≈0.22 down to ≈0.003).
- Phase mastery = 100% mean success over 100-episode window → advance phase
- Converge in low noise first (clear signal), then adapt to increasing stochasticity
- Weights warm-start next phase

**Expert-seeded replay buffer:** capacity 100k transitions. Each phase seeds with 500 episodes of prior-phase policy rollouts ("expert" section, kept frozen for the phase). Mini-batches: 25% expert / 75% online ε-greedy transitions (256 samples). Polyak target-network updates.

## LLM Policy Distillation (interpretable extraction)

Prompt a frontier LLM (paper used Gemini 3.1 Pro) with example (state, action) trajectories from the trained DQN → LLM returns a natural-language heuristic.

Extracted heuristic structure: partition nodes into hub/leaf → process experiments in order → find optimal placements (prioritize hub nodes) → place if possible → else generate virtual links useful for those placements → repeat.

Result: LLM heuristic ≈ DQN performance (succeeds slightly less for γ<5.0; DQN faster for γ>3.2). Use when direct RL training on large networks is computationally expensive — distill from a small-topology policy instead.

## Behavior Profiling Metrics

Diagnose WHY a policy succeeds — compare policies along:
- **HOLDING TIME**: avg time a sublink stays active-and-unused. High = patient policy (waits for better link configurations instead of greedy consumption)
- **BRIDGE SPAN**: avg shortest-physical-path length of generated virtual links. Low = generates only necessary-span links
- **HUB ANCHOR BIAS**: avg max degree of virtual-link endpoints. Low = prefers peripheral nodes, preserves hub memories

## Results (baselines: AgeCriticalFirst, ShortestHopFirst, DCTR)

- First failure at 51–71% LOWER link activation probability vs best heuristics across starlink/dumbbell/grid topologies
- At γ=4.0: ~50–95 steps vs 125–170 for heuristics (≈2.5–3× faster)
- Robust under hardware coloring constraint (≥80% success at 59% lower p_l)
- Learned policy: patient (higher holding time), short-span links, peripheral placement — heuristics fail by greedily consuming bottleneck memories

## Reusable Patterns

1. **Curriculum-over-noise** for RL in probabilistic environments: master low noise → warm-start higher noise, expert-seeded buffer per phase
2. **Distance-to-goal-shaped reward** (SED): reward ∝ remaining distance + step progress, penalize distance-increasing actions
3. **Bottleneck-consumption reward**: normalize centrality of consumed resources against best alternative to keep hubs free
4. **Complexity-weighted job rewards**: |E_k|^κ prevents greedy simple-job bias in multi-job scheduling
5. **LLM trajectory-to-heuristic distillation**: feed (state, action) examples → natural-language policy → benchmark against RL policy; scalable interpretable alternative where retraining is costly
6. **Metric triplet (holding/span/anchor)** for auditing any network-scheduling policy's resource behavior

## Topologies

- **Starlink**: 3 subnetworks on a hub — contention at hub memories
- **Dumbbell**: two networks bridged by bottleneck node
- **Grid**: dense urban/datacenter-style redundancy

Setup: |N|=9, m*=52, µ=5, X={(K4,1),(K4,1)}, episode truncated at 200 steps.

## Related Skills

- [[quantum-network-scheduling]] — classical queuing/allocation heuristics (DE, LQF, WLQF)
- [[quantum-network-control]] — sequential vs simultaneous swapping link-layer control
- [[quantum-network-task-control]] — centralized task-based resource scheduling

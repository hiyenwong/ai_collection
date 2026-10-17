---
name: mapf-temporal-margin-executability
description: Add temporal margins to MAPF schedules so real controllers can execute them. Use when planned paths fail in execution.
category: systems-engineering
---

# Temporal Margins for MAPF Executability (T-robustness)

**Source**: arXiv:2610.20118 — Roselli, Combrink, Zhang, 14 Oct 2026
**Domain**: Multi-agent path finding / fleet coordination

## Core Insight

MAPF solvers are evaluated on the schedules they produce, **not on how well those schedules execute**. Continuous-time optimal solvers exploit near-zero temporal/spatial separation to lower cost — and such schedules are often **un-executable** by realistic closed-loop controllers. On congested MovingAI instances (21–40 agents) with MPC tracking, only a fraction of optimally-solved instances complete execution without intervention.

The fix is to price **executability into the schedule itself**: add a *temporal margin* (minimum time gap between agents at shared locations) and/or *spatial inflation* (larger agent footprint). The paper calls this T-robustness.

## Key Quantitative Findings

- Temporal margin and spatial margin have **different effects**:
  - **Temporal margin decreases deviation** — it gives the controller room to stay on schedule (mean position discrepancy vs schedule falls significantly).
  - **Spatial margin** primarily prevents physical interference conflicts.
- Execution success rises with either margin for a **relatively small increase in sum-of-costs** — the "cost of executability" is cheap.
- Integrated system: AOC-CBS (anytime-optimal continuous-time MAPF) → per-agent MPC tracking of timed paths.

## Method Pattern

1. Solve continuous-time MAPF to optimality (AOC-CBS or similar) → baseline schedule.
2. Re-solve / post-process with constraint: `|t_i − t_j| ≥ τ_margin` at every shared location, plus footprint radius inflation.
3. Track each timed path with MPC (or any closed-loop controller) at execution time.
4. Metrics: execution success rate, mean schedule deviation, sum-of-costs overhead.
5. Sweep τ to trace the cost-vs-executability frontier; pick the knee.

## When to Use

- Fleet coordination / warehouse robotics / AMR traffic where planned schedules repeatedly fail at execution
- Any MAPF deployment where the consumer is a *tracking controller*, not a kinematic oracle
- Schedule robustness analysis: quantify how much optimality you trade for executability
- Choosing between temporal vs spatial margins: use temporal to fix tracking deviation, spatial to fix near-miss conflicts

## Implementation Notes

- The margin is a scheduling-layer constraint — no change to the controller needed.
- On dense graphs with high connectedness, optimal schedules are MORE aggressive (tighter separations) → margins matter more, not less.
- Report both sum-of-costs overhead AND success rate — executability is invisible to cost-only benchmarks.
- Related notion: this is the closed-loop analogue of robustness margins in robust MPC, applied to the *plan* rather than the *control*.

## Related

- [[karma-economy-resource-allocation]] — decentralized MAPF coordination
- Robust MPC / tube MPC provide the tracking-layer counterpart; this skill fixes the planning layer.

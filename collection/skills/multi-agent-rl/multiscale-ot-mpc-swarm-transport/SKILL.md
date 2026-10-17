---
name: multiscale-ot-mpc-swarm-transport
description: Two-level optimal transport planning plus distributed MPC tracking for large swarms. Use for macroscopic density control.
category: systems-engineering
---

# Multiscale Distributed MPC for Optimal Transport of Swarms

**Source**: arXiv:2610.19390 — Pascual, Huang, Martínez (UCSD), 14 Oct 2026
**Domain**: Swarm control / optimal transport / distributed MPC

## Core Insight

Control large swarms by **separating scales**: a macroscopic Optimal Transport (OT) layer plans the *density flow*, while a microscopic MPC layer lets each agent *track its nominal velocity* under control-affine dynamics and reject disturbances. The key theoretical result: the interface between layers is **quantified** — distributional input-to-state stability in the 1-Wasserstein metric proves that microscopic tracking error only perturbs the macroscopic density flow by a bounded, computable amount.

## Architecture

```
Target density ρ_target(t)  — time-varying
        │
        ▼  top level: OT with terminal penalty
Nominal velocity field v*(x,t)  →  regularized static dual, solved DISTRIBUTEDLY
        │
        ▼  low level: per-agent MPC
Agent i: control-affine dynamics, tracks v*(x_i,t), rejects disturbances
        │
        ▼
Density flow ρ(t)  ≈ OT geodesic flow toward ρ_target, with W₁-bounded perturbation
```

## Three Technical Contributions

1. **Terminal-penalty dynamic OT** handles time-varying target densities (standard static OT cannot). Proved equivalent to a *regularized static dual* that agents solve in a distributed way to compute nominal velocities.
2. **Low-level MPC** for control-affine agents: velocity tracking + disturbance rejection, fully local.
3. **Distributional ISS in W₁**: |ρ_flow deviation| ≤ γ(tracking error + target motion mismatch) — the macroscopic flow inherits a bounded perturbation from microscopic errors. This is the certificate that the two-level separation is sound.

## When to Use

- Swarm distribution shaping: coverage, redistribution, delivery of density to moving/evolving targets
- Cases where per-agent trajectory optimization (single-level MAPF/MPC) does not scale with swarm size
- Any density-control task needing a formal guarantee that microscopic noise doesn't destabilize the macroscopic plan
- Time-varying target densities (moving crowds, shifting coverage priorities) where static OT fails

## Implementation Notes

- Top level solves a regularized Kantorovich dual (distributed, one dual variable per agent region) — cheaper than dynamic OT on the full space.
- Low level is a standard tracking MPC: horizon short enough for real-time, cost = ||v_i − v*(x_i,t)||² + input effort.
- The W₁ ISS bound gives a concrete design rule: budget the tracking-error bound first, then the macroscopic plan tolerates that much density deviation.
- Contrast with D²OC (density-driven coverage): D²OC folds density cost into a single-layer stochastic MPC; this skill separates scales and adds the time-varying-target + ISS certificate machinery.

## Related

- [[density-driven-multi-agent-control]] / [[density-driven-optimal-control]] — single-layer density MPC for coverage
- [[dr-data-driven-predictive-control]] — Wasserstein ambiguity sets (different role: robustness, not flow control)
- [[mapf-temporal-margin-executability]] — complementary executability margin for discrete path schedules

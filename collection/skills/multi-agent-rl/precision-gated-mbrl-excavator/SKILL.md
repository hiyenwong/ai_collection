---
name: precision-gated-mbrl-excavator
description: Precision-gated model-based RL for real robots - probabilistic dynamics ensemble learned from scratch on hardware with sampling-based MPC, progress reward conditioned on path accuracy (precision gates speed). Use for sample-efficient learning on heavy machinery, precision tracking under actuation dynamics, or direct-on-hardware RL without demonstrations.
category: ai_collection
trigger_words: model-based RL, hydraulic excavator, sampling-based MPC, probabilistic ensemble, precision-gated reward, contouring control, hardware learning, sample efficiency, path tracking, no demonstrations, real robot learning
---

# Precision at Speed: Sample-Efficient Online MBRL for Hydraulic Excavator Control

**Source**: arXiv:2609.31025v1 (2026-09-25) — Canales, Nan, Hutter, Ruiz-del-Solar (ETH Zürich / U. Chile), cs.RO/cs.LG/eess.SY.

## Problem

Precise high-speed control of robots with **complex actuation dynamics** (hydraulics: deadbands, delays, nonlinear valve behavior) is hard, and learning directly on hardware is bottlenecked by the cost of real-world interaction — a 11.5-ton excavator cannot collect millions of samples.

## Core Mechanism

**Online model-based RL, from scratch, directly on hardware:**

1. **Probabilistic dynamics ensemble**: learn a dynamics model (ensemble for epistemic uncertainty) entirely online — no demonstrations, no simulation pretraining.
2. **Sampling-based MPC**: at each control step, sample candidate action sequences, roll out with the ensemble, pick the best (CEM/shooting style) — MPC absorbs model error by re-planning every step.
3. **Precision-gated contouring objective**: the progress/speed reward is **conditioned on path accuracy** — progress only counts when the tracking error is within tolerance. **Precision gates speed**; the controller cannot game progress by cutting corners.

## Validation Results

- In a data-driven excavator **simulator**: higher sample efficiency than evaluated MBRL baselines.
- **On the real 11.5-ton Menzi Muck M445**: after **20 minutes** of interaction, tracking accuracy matches prior learned controllers that needed **100–150 minutes** (5–7× data reduction).
- After **40 minutes**: sustains **sub-centimeter mean path error at high operating speeds**.

## Recipe

1. Model the dynamics online: state = joint/cylinder states; probabilistic ensemble (e.g., greedy ensemble of probabilistic nets); train continuously from the live stream.
2. Define the contouring task: reference path + tolerance band.
3. Reward: `r = progress_along_path × 1[tracking_error < tolerance]` — the gate makes precision a precondition for reward.
4. Planner: sampling-based MPC over the ensemble at control rate (excavator rates are low enough that MPC is real-time).
5. Exploit MPC's robustness: re-planning each step compensates for early model error, so the policy is safe-ish from the start and improves as the ensemble sharpens.

## Reusable Design Principles

- **Gate progress rewards on accuracy** whenever the task has a speed–accuracy tradeoff: prevents reward hacking via sloppy fast trajectories. Applicable to writing/route tasks, machining, drone racing.
- **Sampling-based MPC + online learned ensemble** is the practical sample-efficiency combo on hardware: the planner requires no policy gradients, and online model learning converts every second of interaction into planning improvement.
- **From scratch beats imitation priors** when the actuation regime is far from any demonstrator's distribution (hydraulic dynamics); interactions are cheap for the planner but expensive for supervised datasets.

**Activation**: precision-gated reward, online MBRL, hydraulic control, sampling MPC, sub-centimeter tracking, real-robot sample efficiency.

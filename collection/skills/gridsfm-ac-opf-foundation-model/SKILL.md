---
name: gridsfm-ac-opf-foundation-model
version: v1.0.0
last_updated: 2026-09-26
description: "GridSFM methodology — physics-inspired GNN foundation model for AC Optimal Power Flow with disconnected-feasible-set repair via log-penalized slack lifting, plus Newton-based physics-informed fine-tuning for unseen grids. Use when: (1) neural solvers fail because the feasible set is disconnected (non-approximable by continuous nets), (2) building pretrain-then-finetune neural PDE/optimization solvers across topologies, (3) few-shot adaptation (100 instances) to new system instances. Keywords: AC-OPF, foundation model, feasible set repair, contractible lifting, physics-informed fine-tuning."
arxiv_id: "2609.30173"
authors: "Luke Bhan, Weiwei Yang, Margaret Capetz, Baosen Zhang"
tags: [opf, power-systems, foundation-model, gnn, feasibility-repair, physics-informed]
---

# GridSFM: AC-OPF Foundation Model

From arXiv:2609.30173 (2026-09-24). Models/data/code released.

## Problem

AC Optimal Power Flow is a hard neural-approximation target for a fundamental reason: **its feasible set can be disconnected** — and no continuous neural network can approximate a solution map over a disconnected set. This is an obstruction, not just a data problem.

## Method

### 1. Feasible-Set Repair (the transferable core)

Lift the problem by relaxing constraints with **logarithmically penalized slack variables**:

- Add elastic slacks to hard equality/inequality constraints, penalized by log-barrier terms
- Prove the resulting **elastic feasible set is contractible** (connected, hole-free) → continuous nets CAN approximate the elastic solution map
- Prove AC-OPF minimizers remain minimizers of the elastic problem **above an explicit penalty threshold** (solutions preserved)
- Prove **projecting an approximate elastic solution back onto the true feasible set is well posed** (recovery guaranteed)

### 2. Scale-Generalizing Backbone

- 15M-parameter physics-inspired GNN pretrained across **54 topologies, 500–4000 buses**
- 2.45% zero-shot generation-cost error on 10,000-bus held-out conditions; no degradation with system size

### 3. Physics-Informed Fine-Tuning

- Newton's-method-based fine-tuning design: with only **100 solved instances**, adapts to unseen grids up to 10,000 buses
- Beats dedicated single-topology networks trained on more data; better as solver warm-start (fewer iterations)

## Reusable Pattern

**Repair the geometry before learning it.** When a continuous function approximator fails on a constrained problem, check whether the failure is topological (disconnected/non-contractible feasible set) rather than capacity-related. If so: lift to an elastic relaxation that (a) makes the set contractible, (b) provably preserves minimizers above a penalty threshold, and (c) admits well-posed projection back to the original set. Log-barrier slack lifting is the concrete tool here; it applies to any constrained regression/optimization-surrogate task with union-type solution spaces (unit commitment, dispatch, routing with discrete jumps).

## Resources

- Paper: https://arxiv.org/abs/2609.30173

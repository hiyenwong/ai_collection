---
name: cfm-multitask-policy-distillation
description: Use when training multi-task robot manipulation policies. Distills single-task conditional flow matching experts into one shared multi-task policy by transferring velocity fields, avoiding capacity blow-up or performance drops of naive concatenated training.
trigger: multitask flow matching distillation, robot manipulation policy, velocity field transfer, CFM expert distillation, multi-task policy learning, RLBench multi-task, shared policy fixed capacity
category: ai_collection
---

# CFM Multitask Policy Distillation: Transferring Velocity Fields

**Source**: arXiv:2609.28107v1 (2026-09-23) — Deshmukh, Mahdi, Heppert, Valada (University of Freiburg).

## Problem

Conditional Flow Matching (CFM) trained on expert demonstrations beats existing methods on robot manipulation, but prior work is **single-task**. Training independent models per task is computationally expensive; naive training on a concatenated multi-task dataset either needs **increased model capacity** or suffers **performance drops**.

## Core Method

Distill knowledge from **single-task CFM experts into a shared multi-task policy by transferring their learned velocity fields**:

```
L = L_CFM(demonstrations)  +  λ · L_distill(velocity-field match to expert)
```

- **Velocity fields are the transferable object**: a CFM policy is its velocity field v(x_t, t | obs); matching student velocity to expert velocity transfers *how to flow* toward actions, not just final actions.
- The distillation signal is **combined with the original CFM objective** — retaining fidelity to the demonstrations while gaining cross-task structure from experts.
- **Fixed model size**: no capacity increase over a single-task model.

## Verified Results

- **RLBench**: improves multi-task policy performance over naive concatenated training **at fixed model size**.

## Why Velocity-Field Transfer Works

- CFM learns a continuous-time vector field; per-task experts learn high-quality fields with task-specific structure.
- A shared student conditioned on task/goal can average/interpolate these fields without inheriting their parameterization — smoother aggregation than logit distillation (used in classification) because the output is a dense function, not discrete modes.
- The residual CFM loss anchors the student to real demonstrations, preventing drift toward expert biases.

## Implementation Checklist

1. Train single-task CFM experts per task (or load existing).
2. Multi-task student: CFM conditioned on (obs, task embedding/goal image).
3. Loss: `L_CFM` on the multi-task demonstration set + velocity-field regression `||v_student(x_t,t|obs) − v_expert_k(x_t,t|obs)||²` where sample belongs to task k.
4. Keep model size fixed vs single-task baseline to isolate the distillation benefit.
5. Compare against naive concatenated-dataset training at the same capacity.

## Related Skills

- `dream-rehearsal-continual-rl` — continual model-based RL
- `distributional-portfolio-optimization` — flow-based modeling elsewhere
- `daca-grpo-denoising-credit-assignment` — diffusion/flow policy training patterns

---
name: raised-prompt-injection-self-distillation
description: Use when defending tool-using LLM agents against indirect prompt injection, or when training-based defenses cause utility loss. RAISED combines self-generation of tool-use scenarios with self-distillation matching teacher clean-context behavior on clean and injected trajectories, preserving benign utility.
trigger: prompt injection defense, indirect prompt injection, tool-use agent security, self-distillation robustness, output distribution drift, benign refusal failure mode, training-time defense utility degradation
category: ai_collection
---

# RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents

**Source**: arXiv:2610.06401v1 (2026-10-05) — Dhouib, Elliker, Canesse, Jenny, Thil et al. (8 authors, incl. Bursztein)

## Problem

Tool-using agents must act on **untrusted external content** (tool outputs), enabling indirect prompt injection. Existing training-time defenses reduce attack success but degrade general capability — through two identified mechanisms:

1. **Output distribution drift**: defenses shift model behavior even in benign settings.
2. **Benign-refusal failure mode**: on legitimate tasks, the model refrains from a step required to complete an *authorized* task — especially when that step is indicated by a tool output (the defense over-generalizes "don't obey tool outputs").

## The RAISED Framework

**R**obust **A**ttack **I**nvariance through **S**elf-**D**istillation:

1. **Self-generation**: the model generates its own tool-use training scenarios, emphasizing cases where task completion requires acting on *legitimate* guidance from tool outputs (anti-benign-refusal data).
2. **Self-distillation**: student is trained to match the teacher's **clean-context behavior** on both clean and injected variants of the same trajectory.

Key design: the target is the teacher's output distribution on the *clean* trajectory, applied to both clean and attacked inputs — the student becomes invariant to injection without drifting from benign behavior, because the supervision signal never changes.

## Reusable Patterns

### Pattern 1: Invariance-to-Attack via Clean-Teacher Distillation
For any input-perturbation robustness problem (injection, adversarial suffix, style attacks): construct paired trajectories (clean, perturbed), and distill the model's own clean-input behavior onto the perturbed input. Avoids reward-modeling drift and over-refusal because the target stays the unperturbed distribution.

### Pattern 2: Self-Generation for the Refusal-Refusal Gap
When a defense causes over-refusal, generate targeted training data where *acting on external content is correct*. Balance the attack-invariance objective with legitimate-compliance coverage.

### Pattern 3: Defense Evaluation Protocol
Evaluate any agent defense on three axes: (a) attack success rate on injected tool outputs, (b) agentic benchmark utility, (c) **benign refusal rate** — measure steps skipped on authorized tasks where completion requires obeying tool outputs. Drift in output distribution (e.g. KL on benign prompts) is an early warning signal.

## Related Skills

- `designing-agents-to-resist-prompt-injection` — injection defense methodology
- `brain-prompt-injection-bci-llm-security` — BCI prompt injection audit

---
name: capability-boundary-data-evolution
description: Evolve distillation data at the student capability boundary.
category: ai_collection
---

# Capability-Boundary Data-Model Co-Evolution (BoundaryEvo)

Source: "BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation" (arXiv: 2610.13285, Su et al., 2026)

## Core Principle

The usefulness of a reasoning example changes as the student evolves. Already-mastered examples give little new supervision; examples far beyond the student's capability are unlearnable. But reliable boundary selection is impossible when the student is initially weak — so **prime first, select later**: establish basic capability with unfiltered distillation, then repeatedly re-select training data at the evolving capability boundary. With only 1,000 total examples, Qwen3.5-4B went 62.9→75.3 on IMO-AnswerBench, 26.8→46.0 on AMO-Bench.

## Two-Stage Procedure

**Stage 1 — Capability Priming (judge-free)**:
- Distill a small set (~100) of teacher-generated long reasoning trajectories via plain SFT, after only basic response-validity checks.
- NO model-based judging, NO capability-gap filtering. Rationale: premature filtering discards useful teacher behaviors (exploration, unsuccessful attempts); the student must acquire an initial capability before boundary estimation is meaningful.

**Stage 2 — Capability-Boundary Co-Evolution (per turn t)**:
1. Student M_t and a **fixed** expert E independently solve each candidate question from pool P (2K = 2×turn budget).
2. Analyzer scores: capability gap `g_i = s_expert − s_student`, quality `q_i`, validity flags `b_clear, b_answerable, c_i` (clear / answerable / context-supported).
3. **Hard boundary filters** — accept into A_t only if ALL: `s_expert ≥ τ_e` (expert reliably solves), `s_student < τ_s` (student has not mastered), `g_i ≥ τ_g`, `q_i ≥ τ_q`, validity flags pass. Ambiguous questions must not be mistaken for student limitations.
4. **Replay-first budget** (K=300/turn): keep eligible replay examples (previously used, still unsolved) up to quota; fill remainder with quality-ranked novel examples.
5. **Fresh teacher rollouts** (L≥2 per selected question); retain only trajectories whose final answers pass reference verification. Separate *which questions to learn* (expert rollout) from *which solutions to imitate* (teacher rollouts).
6. SFT update → boundary shifts → re-scan pool next turn.

**Training objective**: token-normalized cross-entropy on full reasoning trajectories (only response tokens contribute).

## Lessons

- Data selection is stage-dependent: broad unfiltered transfer early, boundary-aware selection late. One fixed selection policy for the whole run is suboptimal.
- Track the *student–expert gap*, not student correctness alone — student failure on an ambiguous/broken question is not a learning opportunity.
- Re-estimate the boundary after every student update; a static "hard examples" set goes stale as the student improves.
- Replay unsolved-but-valid examples before acquiring novel ones; unresolved signals are already paid for.
- Under a tiny supervision budget, a 2× candidate pool rescanned each turn beats one-shot selection.

## Activation

reasoning distillation data selection, capability boundary active learning, student-expert gap filtering, small-budget distillation, curriculum co-evolution, replay-first data budget

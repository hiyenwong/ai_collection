---
name: splice-consistency-knowledge-coevolution
description: "Use when co-evolving agent skills and models consistently."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [agentic-knowledge-evolution, consistency-regularization, evolution-views, common-gain, task-replay, contrastive-self-distillation, GRPO, skill-extraction, agent-memory, knowledge-internalization]
    related_skills: [self-evolving-agent-experience, skill-extractor, admem-advanced-agent-memory, self-challenge]
trigger: agent skill extraction validation, knowledge-model co-evolution, consistency regularization for knowledge, evolution views, common gain selection, pairwise minimum estimator, inconsistent utility gains, task replay evaluation, noisy knowledge contrastive reference, gated self-distillation, plausible knowledge underperforms, experience-to-knowledge transformation, skill library curation
---

# SPLICE: Consistency-Regularized Knowledge-Model Co-Evolution

**Source**: "Agentic Knowledge-Model Co-Evolution via Consistency Regularization" — Sirui Chen, Zhining Liu, Chao Zhang, Jingrui He (UIUC), Zheng Li (Amazon), arXiv:2610.30790 (cs.AI, 22 Oct 2026). SPLICE = consistency-regularized knowledge-model co-evolution; +3.0–4.6 pts accuracy over strongest baselines (Qwen3.5-4B/9B), up to −44% output tokens per correct solution.

## When to Use

Use when an LLM agent **extracts reusable knowledge (skills, memories, tool guidance) from its own experience** and you must decide which extractions actually help; when different analyses of the same trajectory yield conflicting guidance; when plausible-looking knowledge might underperform using no knowledge at all; when internalizing external knowledge into model weights (self-distillation + RL); when curating a skill library that grows from agent experience.

## The Core Problem

The transformation experience→knowledge is a function parameterized by textual analysis instructions p. **Different ways of analyzing the same experience yield knowledge with substantially different utility** — e.g., a failed purchase analyzed as "include size requirements in queries" vs. "verify selected size before purchase": on a page that lists the requested size but defaults to another option, the first rule leaves the error unchanged. Prior work: even reasonable extraction criteria yield less useful knowledge; plausible knowledge can underperform no knowledge.

## Consistency-Regularization Analogy

Prediction consistency: regularize predictions to be invariant under parameter perturbations → better generalization. **Utility consistency (SPLICE)**: knowledge whose utility gains persist across perturbed *analysis* views is not view-specific → more generalizable.

## Method

### 1. Evolution views + common gain
- Agent π_θ solves a batch of tasks with current knowledge K → experience E.
- Generate N textual revisions δ_j of the analysis instructions p ("identify planning errors", "review tool choices", "identify missed task requirements", ...). Each defines an evolution view: K^(j) = G(E, K; p ⊕ δ_j).
- **Task replay**: evaluate each candidate K^(j) by re-running the tasks used to collect E. Δ_ij = mean reward gain of K^(j) vs. K on task x_i.
- **Common gain** per task: Ĉ_i = (1/N²) Σ_{j<ℓ} min(Δ_ij, Δ_iℓ) — mean gain minus inconsistency penalty. The pairwise-minimum form measures the gain *shared* by two views; isolated high gains (lucky runs, view-specific guidance) get discounted.
- Select up to n tasks with Ĉ_i > 0; their replay trajectories across all candidates form the evidence base.
- Knowledge optimizer G compares these trajectories to relate *knowledge changes to behavior changes*, consolidating updates supported by consistent gains (not merely content overlap across candidates).
- **Validation gate**: accept K̂ only if held-out validation improves; otherwise keep K unchanged.

### 2. Proposition 1 (why consistency works)
With ∆, ∆′ = utility gains of two i.i.d. evolution views, population common gain C = E[min(∆,∆′)] > 0 implies µ = E[∆] > 0 and **Pr(∆ > 0) ≥ C/µ = 1 − E|∆−∆′|/(2µ)**. Lower inconsistency at fixed mean gain ⇒ stronger lower bound on improvement probability under a *new* view. Common-gain selection is a nonparametric, minimax-flavored statistic: robust to view-distribution asymmetry.

### 3. Model evolution: GRPO + gated contrastive self-distillation (CSD)
- **Positive side**: self-distillation from the model conditioned on K (teacher) to the model without K, weighted per task by observed benefit w_i (rollout with-K vs without-K mean rewards).
- **Contrastive reference (noisy knowledge K⁻)**: rerun the selection with −Δ_ij; extract guidance associated with *consistent utility degradation* into K⁻. Used as a contrastive reference — discouraging incorrect responses — rather than a teacher.
- **Token-level gate** on K⁻'s contribution: keep guidance where K and K⁻ point the same direction, suppress where they conflict; preserves shared useful guidance hidden inside degrading knowledge.
- Rebuild K⁻ fresh at each model-evolution start; interleave knowledge evolution ↔ model evolution — updated model generates new experience, changing K's measured utility.

## Pitfalls

- **Single-view extraction overfits the analyst prompt**: one analysis of a trajectory is one sample from a noisy function; replay-validate across perturbed views before committing knowledge.
- **High average gain can be one lucky trajectory**: pairwise-minimum across views, not mean across tasks, is the robust statistic.
- **Content overlap ≠ utility support**: consolidate by comparing replay trajectories (behavior deltas), not by intersecting candidate texts.
- **Noisy knowledge is not garbage**: consistently-degrading guidance is a valuable contrastive signal when gated at token level.
- **Knowledge useful overall can hurt specific tasks**: task-level benefit weighting w_i for internalization, not uniform distillation.

## Lightweight Adoption (no training loop needed)
Even without model evolution, the knowledge-evolution half applies directly to skill/memory curation: (1) extract candidate knowledge under ≥3 perturbed analysis prompts; (2) replay/validate each candidate on the triggering tasks; (3) accept only knowledge whose gains are consistent across views; (4) keep a validation gate before library commit; (5) log consistently-degrading guidance as anti-patterns.

## References

- arXiv:2610.30790 — SPLICE (this skill's source)
- Consistency regularization lineage: prediction invariance under parameter perturbation
- GRPO (Shao et al.) — group-relative policy optimization baseline
- Huang et al. 2026, Li et al. 2026, Dong et al. 2026 — plausible knowledge can underperform no knowledge

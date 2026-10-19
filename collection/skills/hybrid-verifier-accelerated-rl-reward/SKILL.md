---
name: hybrid-verifier-accelerated-rl-reward
version: v1.0.0
last_updated: 2026-10-17
description: "Neural pre-screen + exact oracle for fast RL verifiers."
arxiv_id: "2610.21881"
authors: "Lazar Milikic, Etienne Bamas, Emmanuel Abbe, Viktor Kunčak"
tags: [theorem-proving, reward-models, RL-training, verifiers, efficiency]
---

# Learning Lean Feedback for Efficient Proof-Candidate Evaluation

From arXiv:2610.21881 (2026-10-15).

## Problem

Training LLMs for formal theorem proving requires huge numbers of verifier (Lean 4) calls. Slow checks and timeouts leave GPUs idle and withhold rewards from potentially correct proofs — the verifier is the throughput bottleneck, not the model.

## Method

**Hybrid neural-exact reward system:**

1. Train neural evaluators on 4.84M labelled Lean programs to predict verdicts + compiler feedback (goal states, error messages) on GPU.
2. **Two-stage evaluator**: a validity classifier screens candidates first; only its positive predictions are scored by a richer feedback model annotating predicted goal states and error messages.
3. Reach 87.8% accuracy in predicting whether Lean accepts a proof (on a 68,932-program benchmark from public provers).
4. 3.5 candidates/sec on one H100 = 4.2× a 64-worker Lean baseline with environment reuse.
5. **Hybrid reward**: combine neural evaluator with Lean verdicts — GRPO training steps shorten ~31%, keeping miniF2F pass@1 nearly identical (62.2% vs 62.4%) and pass@32 slightly better (72.4% vs 71.3%).

## Reusable Pattern

**Neural pre-screen feeding an exact oracle.** Any RL pipeline whose reward comes from an expensive exact verifier (compilers, unit tests, simulators, formal checkers) can be accelerated by a two-stage scheme: train a fast neural judge on (input, oracle-verdict) pairs, use it to screen candidates and route only likely-positives to the real oracle, then combine both signals in the final reward. Key design points: the screening classifier needs only binary quality; the richer feedback model (predicting *why* a candidate fails) can be applied to the small surviving set; hybridization guarantees correctness where it matters (final reward) while cutting the bulk of oracle calls. Also fixes the GPU-idle problem: evaluation moves onto the same hardware as training.

## Resources

- Paper: https://arxiv.org/abs/2610.21881

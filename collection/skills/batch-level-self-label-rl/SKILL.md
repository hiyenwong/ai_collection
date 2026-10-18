---
name: batch-level-self-label-rl
description: Use when self-label RL rewards replace verified rewards.
---

# Batch-Level Self-Label RL (Majority-Vote ≈ Gold)

Source: arXiv:2610.20898 (Wilson, Huang, Huang — "Wrong Votes, Right Gradients: Why Majority-Vote Rewards Track Verifiable RL", 14 Oct 2026). Code: github.com/dylan518/wrong-votes-right-gradients

## Activation
- majority-vote reward, TTRL, self-generated labels, label-free RL, self-label RL, majority vote vs gold, batch update cosine, error coherence vs error rate, reward-model vs verifier

## Core Claim
Prompt-level analysis says majority vote (MV) only sharpens a model's modal answer and "cannot add information." The paper shows the prompt is the wrong unit: because parameters are shared, at practical batch sizes (B=64–256) **a prompt's own gradient accounts for <1% of the change in that prompt's output** — the batch update is what matters, and a wrong label costs little if the errors across prompts don't share a direction.

## Formal Framework

Batch update with reward r: G(r) = Σ_i g_i(r), where prompt gradient g_i(r) = Σ_j A_ij ∇θ log π(y_ij|x_i).

**Decomposition** of MV update relative to gold update:
- G_mv = (1−β)·G_gold + E⊥,  E⊥ ⊥ G_gold
- β = shrinkage (only rescales the step — SGD: like smaller LR; adaptive optimizer: absorbed by second-moment normalization)
- E⊥ = misdirection (changes direction — the only thing that matters)
- R⊥ = ‖E⊥‖/‖G_gold‖; cos(G_mv,G_gold) = (1−β)/√((1−β)²+R⊥²)

**Growth of a sum (Prop. 1)**: for vectors v_1..v_B with mean pairwise alignment ρ̄:
- ‖Σv_i‖² = B·s²·(1+(B−1)ρ̄), s² = mean norm²
- Incoherent (ρ̄=0) → grows as B^(1/2) (random walk); shared component → grows as B beyond crossover B* ≈ 1/ρ̄ (gradient noise scale, McCandlish 2018: B*−1 = E‖ξ‖²/‖μ‖²)
- Growth exponent α(B) = 1/2 + 1/2 · Bρ̄/(1+(B−1)ρ̄); α≈1/2 means no shared direction, α→1 a dominant one

**Noise-corrected cosine**: compare MV-of-half-A vs gold-of-half-B (X), gold-vs-gold (Y), MV-vs-MV (Z) across split halves; c∞ = X/√(YZ). c∞ = 1 means MV update ≡ gold update within sampling noise.

## Measured Findings (5 models, 2 families)
1. MV update agrees with gold as closely as two independent gold updates agree with each other; c∞ = 1 within error at every checkpoint.
2. MV label errors are **as incoherent as a random-reward null** (α ≈ 1/2), while gold gradients share a direction (α ≈ 0.9) beyond a few dozen prompts.
3. **Randomly flipping up to 30% of gold labels leaves the update direction intact** (c∞ stays 1); the same fraction flipped by a **shared rule destroys it**. Error *structure*, not error rate, governs.
4. Rewards that favor a kind of response on EVERY prompt (frequent answers, confident answers, a learned reward model's preference) fall measurably short — they inject a coherent error direction.
5. Mechanism for repair: on prompts with wrong majorities, MV batch update still increases expected gold reward on 82% of them — the other prompts' gold gradient (+0.075 cosine contribution) outvotes the prompt's own mislabeled term (+0.007).
6. **Local equivalence only**: gold training still ends ahead on held-out majority accuracy; MV mainly sharpens single-sample answers. MV repairs wrong majorities ~3× faster than resampling alone.

## When to Use Self-Labels vs Verification (decision rule)
- SAFE: model's residual errors sparse and prompt-specific → MV/self-labels can replace verifiers
- FAIL: errors shared across prompts (widely-held misconceptions; prompts revisited until errors accumulate; any reward that systematically prefers one response type everywhere — including learned reward models)
- Audit recipe: estimate error coherence (pairwise alignment ρ̄ or growth exponent α) between self-label and gold updates on a probe set; if α ≈ 1/2, self-labels are safe to scale; if a shared direction emerges (α → 1), fall back to verification.

## Implementation Notes
- Per-response gradient sketches allow evaluating any reward on the same samples (reuse rollouts; no re-training per reward variant).
- Split-half X/Y/Z cosine protocol is the cheap practical audit — no second full run needed.
- Setup that reproduces findings: Qwen3-4B-Base + DeepScaleR, B=256 prompts, n=16 responses/prompt, no KL/entropy bonus; eval MATH-500 64 samples @ temp 1.

## Limitations (from authors)
Equivalence is checkpoint-local, not trajectory-global; no claim MV = gold on end-state accuracy; labels must come from the current policy snapshot.
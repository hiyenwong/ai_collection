---
name: dreaming-learning-model-collapse
description: Use when model collapse hits synthetic-data training loops.
category: ai_collection
---

# Dreaming Learning vs Model Collapse (Spectral Theory + Regularizer)

**Paper**: Benati, Londei, Lanzieri, Mastromarino, Loreto — "Mitigating Model Collapse through Dreaming Learning" (arXiv:2610.30009, 2nd PriGM Workshop @ NeurIPS 2026)

## When to use
- Iterative retraining loops where a generative model trains on its own outputs (self-consuming loops)
- Diversity loss / mode narrowing when finetuning LLMs on synthetic corpora
- Diagnosing collapse beyond scalar test loss — via the transition-operator spectrum
- Designing regularizers that keep learned-operator eigenvalues away from the unit circle

## Core theory — spectral view of collapse
1. Track the **learned transition operator** (Markov chain / next-token conditional structure), not just test loss. Subdominant eigenvalues |λ_{i>1}| set the mixing rate, i.e. how much of the state space keeps being visited.
2. Sampling at temperature T_s < 1 acts as a **row-wise sharpening operator**:
   `S_T(M)_ij = M_ij^(1/T) / Σ_k M_ik^(1/T)`
   Repeated sharpening concentrates each row on its largest entry → deterministic matrix. A deterministic row-stochastic matrix is the transition matrix of a map whose recurrent part is a union of cycles; a cycle of length L > 1 contributes the L-th roots of unity → **subdominant eigenvalues approach the unit circle, spectral gap narrows**.
3. Two independent collapse routes: (a) tail truncation from finite-sample retraining (present even at T_s = 1); (b) mode bias from T_s < 1 sharpening (dominant route — **data accumulation does NOT arrest it**).
4. **Dobrushin bound**: a row-stochastic matrix whose entries are all ≥ c has ergodicity coefficient ≤ 1 − nc, which bounds every non-Perron eigenvalue away from 1. A floor on conditional probabilities ⇒ spectral protection. Dreaming Learning supplies exactly this floor.

## Dreaming Learning regularizer (recipe)
- Requirements: probabilistic model whose output is mappable back into its input space (autoregressive next-token models work natively).
- At each training step, generate a batch of k sequences of length ℓ by **recursively sampling from the model's own Softmax outputs tempered at T_d > 1** (same sharpening operator with T = T_d, which flattens rows).
- Dreaming loss = cross-entropy of the model on that batch:
  `L_dream = −(1/(k(ℓ−1))) Σ_i Σ_t log P(x̃_{t+1}^{(i)} | x̃_{1:t}^{(i)})`
- Total objective: `L = L_reg + α·L_dream`, where L_reg is the usual next-token cross-entropy on real data. α is a **loss coefficient, not a data mixing weight** — it can exceed 1.
- Mechanism: high-temperature samples flatten the predicted distribution → training on them keeps operator entries from becoming vanishingly small → eigenvalues bounded away from the unit circle. Interpretation: the model explores its own Adjacent Possible (Kauffman).

## Hyperparameters (empirically validated ranges)
- Useful ranges: **T_d ∈ [1, 3], α ∈ [0.3, 1]** (optimal pairs vary by setting)
- Markov chain benchmark (n=10 states, T_s=0.7, accumulation, 5000 generations): **T_d = 1.5, α = 0.8** — KL between true and reconstructed stationary distribution improves by >2 orders of magnitude; large α is best (consistent with the entry-floor mechanism)
- LSTM LM (4×400, recursive retraining): **T_d = 3** — validation loss flat at both T_s = 0.7 and 1.0, and converges to a lower loss already at generation 0. Vanilla slope: 8.7e-3/gen (T_s=0.7) vs 9.6e-5/gen (T_s=1) — accumulation is nearly harmless at unit temperature, clearly harmful below it.
- GPT-2 124M (scratch-pretrained OpenWebText, WikiText-2 finetune, 15 generations at T_s=0.8): **T_d = 1.1, α = 0.5** — perplexity ~980 vs ~1960 vanilla at generation 15 (~2.0× ratio from generation 5 on). Dreaming **slows but does not arrest** drift at LLM scale.
- Budget-constrained tuning (two-line sweep): fix α=0.5 and sweep T_d ∈ {1.0, 1.05, 1.1, 1.5}; fix T_d and sweep α ∈ {0.5, 0.7, 0.8} — ~36 GPU-hours at GPT-2 scale vs 88 trajectories for a full grid.

## Diagnostics to run
- |λ_2|…|λ_5| of the reconstructed transition matrix across generations (moving average w=100, ≥10 seeds) — vanilla drifts upward toward 1; dreaming stays flat in t.
- KL(p‖q) between true and reconstructed stationary distributions after N generations.
- Validation-loss slope per generation as a cheap proxy: harmfulness of accumulation is temperature-controlled.
- Known bias to watch: the dreaming spectrum **settles below the true one** → the learned chain mixes faster than the target (stable ≠ correct); offset controlled by T_d and α.

## Limitations & honest negatives
- Stable spectrum is not a correct spectrum (faster-mixing residual bias persists).
- T_s sweep only at {0.7, 0.8, 1.0} — behavior near T_s = 1 is suggested by the sharpening picture, not established by fine-grained sweep.
- T_d and α require empirical tuning; dreaming roughly **doubles per-step generation cost**.
- GPT-2 scale: mitigation attenuates (slows, not arrests) — asymmetry vs Markov/LSTM left open; candidate follow-ups are annealing T_d and characterizing the entry floor to predict the optimal (T_d, α).
- Theory treats the operator as exactly recoverable; real reconstruction is approximate.

## Related
- Original Dreaming Learning (Londei et al., arXiv:2410.18156) — targets adaptation to regime shifts; this paper repurposes it as an epoch-based diversity-preserving regularizer.
- Shumailov et al., Nature 631, 2024 — tail-truncation collapse route under unbiased sampling.
- Gerstgrasser et al., 2024 — accumulation mitigation (effective at T_s = 1).

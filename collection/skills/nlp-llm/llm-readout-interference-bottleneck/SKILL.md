---
name: llm-readout-interference-bottleneck
description: "Mechanistic dissociation methodology from arXiv:2610.21176 (Yale, Gong 2026). Tests why LLMs fail N-back working-memory tasks: 15 pretrained LLMs (Pythia/GPT-2/Qwen2.5, 70M-14B) locate the target with attention but fail at readout — distractor letter content interferes with the decision variable, not attention precision. Sharpening attention barely helps (+0.05 d'); suppressing distractor letter-identity subspace raises d' in 42/43 cells (median +0.60). Includes formal propositions on when sharpening vs. interference-removal helps, and when softmax precision actually binds (single-layer transformers only; depth removes the bound). Use when analyzing LLM working-memory limits, attention-based retrieval errors, interference vs precision accounts, activation patching of task-critical heads, linear probes exceeding behavioral performance, or causal subspace interventions on residual streams. Activation: working memory, N-back, readout bottleneck, interference account, attention precision, lure errors, activation patching, linear probe, residual stream, distractor suppression, d-prime."
---

# LLM Readout Interference Bottleneck

Source: arXiv:2610.21176, Dongyu Gong (Yale). Companion evidence to Xiong et al. 2026 with the decisive causal dissociation.

## The question

LLMs reproduce the human N-back signature: d′ declines with load N, and false alarms concentrate on **lures** (query letter repeated at N±1). Nothing is ever "forgotten" in an LLM context — so the limit must arise in retrieval or use. Two accounts:

- **Precision account**: softmax attention can't concentrate weight on the item N-back; neighbors soak up mass; model reads the lure's letter. Fix: sharpen attention.
- **Interference account**: attention *finds* the target, but competing items' content leaks into the decision variable. Fix: remove distractor content.

Behavior alone cannot tell these apart (both predict lure errors). The paper dissociates them mechanistically in 15 pretrained LLMs (Pythia 70M–6.9B, GPT-2 124M–1.5B, Qwen2.5 0.5B–14B; 200× size range) + minimal transformers trained from scratch.

## Procedure (replicable workflow)

1. **Task format**: 24-letter sequences from 20 consonants, 4 lures per sequence; one letter+answer per line; measure preference as logprob("m") − logprob("-"); threshold on 200 calibration sequences, evaluate on 1000 test sequences; report d′ (not accuracy — immune to no-match bias).
2. **Find task-critical heads via activation patching**: run two sequences differing only in the target letter (answer flips); patch one head's output from run A into run B; the head(s) restoring much of the answer difference carry the task. Usually one dominant head (N=2: recovers 16–73% alone).
3. **Attention-on-error analysis**: on misses (true match answered "no"), check whether the top-5 heads locate the target line. Result: attention is off-target on only 16%/7%/8% of misses at N=2/3/4 — precision fails to explain errors.
4. **Linear probe > behavior**: logistic regression on the residual stream at the query, trained to separate match vs lure positions. Probe AUC ≈ 1.00/0.98 at best depth vs model's own decision AUC 0.63/0.58 — the model *computes* where the match was but doesn't *use* it. Probe classifies 95% (N=2) / 86% (N=3) of the model's own lure false alarms as lures.
5. **Causal interventions** (the decisive step — correlational probes are insufficient per their own argument):
   - Ablate top-10 heads → d′ drops in 42/43 cells (median −0.93). Ten random heads: no effect.
   - Sharpen top-3 heads (temperature τ<1 on scores): median +0.05. Flattening (τ=2) costs −0.32. Global best temperature is *flatter* in 19/30 cells — heads are already near-optimal sharpness.
   - **Distractor suppression**: estimate the 19-dim letter-identity subspace (mean activations of 20 letters minus their mean), remove half of each non-target item's component at every layer, sparing the target → d′ up in 42/43 cells (median +0.60, max +1.78). False alarms fall ~0.2–0.3 → ~0.1, hits unchanged.
   - Controls: random 19-dim subspace removal: −0.03 (nothing). Removing the *target's* component: −1.54 (destroys performance). Half-strength beats full removal (over-suppression).
6. **Scale effects**: head ablation costs *less* in bigger models (ρ=0.74, task spreads over more heads — solution distributes), while interference removal helps *more* (ρ=0.57). Qwen2.5-14B: suppression takes 3-back (1.60→3.38) above unaided 2-back (2.42). The bottleneck is scale-invariant; the implementing circuit is not.

## Formal core (when does what help)

**Proposition 1** — decision variable r = w⊤h, h = γy·e + Σ_j B_j g_j + z, distractor contents g_j in a q-dim subspace, d′ = (2γw⊤e + β)/√(σ_D² + σ_z²) with β = b₊ − b₋ (lure-induced match bias):
- Removing fraction α of distractor content: d′(α) = (2γw⊤e + (1−α)β)/√((1−α)²σ_D² + σ_z²), increasing in α whenever β ≤ 0. Works on *all* distractor content regardless of which head wrote it.
- A head already attending to target with weight ≥ 1−ε can contribute at most ε·max‖w⊤W_O v_j‖ of distractor content — sharpening one head removes almost nothing. This is why sharpening is bounded and suppression is not.

**Minimal-transformer results** (720 one-layer models trained on N-back):
- Prop 2/Cor 1: a one-layer model with fixed attention weights cannot test letter equality — the match signal must be carried by *content-dependent shifts of attention mass*; pure positional attention (fixed split between i and i−N) yields d′≈0 even though it "locates" the target perfectly.
- Prop 3 (softmax dispersion): target weight ≥ 1/(1+Ke^(−Δ)); N±1 items get e^(−δ_P)× target weight. But in trained models δ_P does *not* shrink with N and predicts neither lure FAs (ρ=−0.03) nor d′ (ρ=−0.05) — the precision account's specific predictions fail.
- Sigmoid or top-k attention flatten the decline; scalable softmax does not.
- **Prop 4 (depth removes the bound)**: with 2 layers + residual stream + absolute/rotary position code, layer 1 copies x_{i−N} into position i, layer 2/MLP compares equality without competing positions. ALiBi or no position code fails at every N. So: **precision binds only transformers too shallow to compare two items directly** — i.e., never pretrained LLMs.

## Takeaways

1. LLM working-memory limit = **readout under interference**, not retrieval. Same conclusion as interference accounts of human WM (Oberauer, Engle): items are available but compete at the moment of use.
2. Convergence claim: 15 models / 3 families / 200× size share the *bottleneck* while the *circuit* varies — mechanism-level convergence is about the computational stage that fails, not the heads implementing it.
3. Methodological warning: **decodable information ≠ used information** (probe AUC 1.0 while behavioral AUC 0.63). Any cross-system similarity claim (RSA/CKA/probes) needs causal intervention on the candidate content before claiming mechanism sharing.
4. Practical: to improve LLM recall/retrieval tasks, separating item content from decision (architectural or training-time) beats attention sharpening.
5. Decline is not softmax-specific: a selective SSM (Mamba-style) trained from scratch also declines with N.

## Limitations noted by author

Letter N-back with synthetic stimuli only; line-by-line format with correct earlier answers shown; head-level account may not transfer beyond 14B; GPT-2 family loses part of the probe information by last layer at N=3 (AUC 0.84–0.89); Prop 1 is a linear readout model, not derived from trained weights.

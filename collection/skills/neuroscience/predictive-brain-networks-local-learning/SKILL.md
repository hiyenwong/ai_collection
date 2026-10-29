---
name: predictive-brain-networks-local-learning
description: "Use when local predictive coding must match deep nets."
category: ai_collection
tags: [predictive-coding, brain-alignment, local-learning, self-supervised, computational-neuroscience, ventral-stream]
trigger_words: [predictive brain networks, local learning pc, brain-aligned representations, cpc hierarchy, pc-compliant dnn, rsa ventral stream]
---

# Predictive Brain Networks (PBN): Local PC Learning With Deep-Net Representational Power

**Source:** Gütlin, Auksztulewicz & Doerig, "Local learning is all you need: brain-aligned predictive coding networks" (arXiv:2610.37327, Oct 2026, q-bio.NC, FU Berlin / Bernstein Center / Maastricht).

## The PC Paradox and Its Resolution

Predictive Coding (PC) is neurobiologically influential, yet PC-compliant models (PredNet etc.) consistently failed to match modern DNNs in performance AND brain alignment. PBNs resolve this: a hierarchical recurrent framework with **strictly local PC learning** achieves human ventral-stream alignment **matching or exceeding ResNet-50 / ConvNeXt-tiny** (NSD fMRI, reweighted noise-ceiling-corrected RSA, 7 visual regions) — while outperforming PredNet in 35/35 region comparisons. The untrained PBN architecture does NOT differ from PredNet: the win comes from learning, not architecture capacity.

## Six PC-Compliance Requirements (checklist for any "PC" model)
1. Hierarchical organization with repeating computational blocks at increasing abstraction.
2. A generative model component — top-down prediction of bottom-up input.
3. Learning driven by the mismatch (prediction error) between top-down prediction and bottom-up input.
4. Predictions and errors in functionally/anatomically distinct populations.
5. Spatially LOCAL synaptic learning (no global error propagation).
6. Probabilistic/Bayesian predictions.

## Architecture

**Hierarchy of stacked autoencoders**, each level's input = latent of the level below:
- Per level: encoder (bottom-up) + decoder (top-down predictor of the NEXT sequence element) — autoregressive by construction.
- **Two skip connections per level:** (a) *posterior connection* — encoder→decoder U-Net-style skip providing information for the posterior; (b) *prior connection* — previous decoder state fed into the next-step encoder, making the network inherently recurrent: decoder state at t is the prior for input at t+1.
- **Optional memory module:** Continuous Gated Cell projecting input to a 32-dim state, learned sigmoid gate blends previous memory + current input, residually added back — extra recurrent capacity beyond the decoder-output state.
- **Vision instantiation:** ConvNeXt-stage-matched encoder — 4 conv stages (96/192/384/768 channels; 3-3-3-9 residual blocks), BatchNorm (beats LayerNorm under CPC), global-average-pool + 2 dense layers; dropout 0.1 throughout (enables MC-dropout); mirrored lightweight decoder (dense + upsample + transposed-conv + skip-conv).

## Losses and Local Gradient Blocking

- **CPC (Contrastive Predictive Coding, Oord 2018) at every hierarchy level**, placed at the *prior fill-in layer*: top-down decoder prediction from t vs bottom-up encoder input at t+1. Contrastive pulls matching (prediction, future) pairs together and pushes mismatched pairs apart.
- **MSE pixel reconstruction only at the lowest level** (no need to compress at pixel level; enables visualization + pixel-wise MC-dropout uncertainty).
- **Stop-gradient layers between hierarchy levels** enforce strictly local learning: each level's loss tunes only that level. Rationale: shallow backprop is biologically conceivable; exact gradients through thousands of nonlinear ops are not. Placement is fine-grained (can allow/forbid BPTT within a level; can decide whether the bottom-up signal is also tuned by the adjacent top-down prediction — works for contrastive, trivializes pure invariance losses).
- **Naturalistic light augmentation:** Gaussian smoothing (blur), hue jitter (lighting), constrained low-level crops (saccades) — no zoom crops, no flips. Masking achieves similar effects.

## Six Model Variants (ablation ladder)

| Variant | Loss | Local loss | Local gradients | Prior subtract | Aug-free |
|---|---|---|---|---|---|
| PBN untrained | — | — | — | — | — |
| PBN backprop | CPC top + recon | no | no | no | no |
| PBN backprop + local loss | CPC each level | yes | no | no | no |
| **PBN local gradients** (main) | CPC each level | yes | **yes** | no | no |
| PBN local gradients + subtract | CPC each level | yes | yes | yes | no |
| PBN classic PC | MSE each level | yes | yes | yes | yes |

## Key Results

1. **Brain alignment:** PBN local gradients significantly beats established DNNs in 7/14 region×model comparisons, never significantly worse (Wilcoxon, FDR<0.01). All 5 trained variants beat PredNet 35/35. **Prior-subtraction variants collapse in higher visual areas** (outperformed by DNNs in 21/28 comparisons) — explicit classic-PC subtraction LIMITS representational similarity even though it stays PC-compliant.
2. **Decoder-unique brain variance** R²(brain|enc∪dec) − R²(brain|enc): CPC variants explain significant unique fMRI variance vs untrained (28/28); local gradients ≥ backprop everywhere (significant in early/mid-parietal/ventral). Top-down predictions carry brain-relevant information beyond bottom-up features, growing with learning locality.
3. **Downstream (UCF-101 kNN-1 / linear):** local gradients 0.828/0.270; backprop+local loss 0.849/0.309; classic PC 0.854/0.237 vs PredNet 0.773/0.071 (ResNet-50: 0.921/0.337). +subtract variant collapses (0.338) — contrastive loss is load-bearing.
4. **Macaque prediction-violation replication** (Schwiedrzik & Freiwald 2017): view-violation errors decay from early→late response windows while identity-violation errors persist — top-down identity predictions reshape lower-level errors. PBN reproduces the interaction (Layer 1: t=4.841, p<1e-6; Layer 2: t=13.9, p<1e-37). Feedforward DNNs cannot express this temporal signature.
5. **Uncertainty:** MC dropout (Gal & Ghahramani 2016 — dropout+weight-decay training ≈ variational inference over weights) — prediction variance scales linearly with true Markov-transition entropy; model recovers the transition matrix (Wilcoxon W=135, p<1e-4). Satisfies requirement 6 without constraining posterior form.

## Design Lessons (transferable)

- **Local gradients do NOT cost representational quality** — despite per-level updates being linearly suboptimal vs end-to-end backprop, brain alignment matches or exceeds global training. Cross-level credit assignment is unnecessary for rich abstract representations here.
- **Contrastive (CPC) > invariance (MSE) for representational richness** — contrastive framing of PC preserves information the classic reconstruction objective destroys.
- **Classic prior subtraction hurts** — subtracting the top-down prior from the bottom-up input (Rao-Ballard style) is neither required for PC compliance nor helpful for brain alignment; it converged fastest (<100 epochs) but to worse representations.
- **Report the encoder/decoder split** — decoder-unique variance is the evidence that predictive (top-down) computation carries neural information a purely feedforward model misses; RSA on encoder layers alone would hide it.
- **Architectural priors matter less than learning rules here**: untrained PBN ≈ PredNet trained — check untrained baselines before crediting architecture.

## Implementation Recipe

- Data: naturalistic video (Moments in Time + UCF-101 + Something-Something), clips ≤3s, 6-frame sequences at 3.2 Hz.
- Optimizer: SGD momentum 0.9, lr 0.075 cosine-decayed to 0 over ~2.6M steps, weight decay 1e-6, global grad-clip 1.0.
- Early stopping: keep lowest-validation-loss checkpoint, ≥350 epochs, stop after 50 non-improving.
- Eval: NSD 515 shared images as repeated 3-frame stills (recurrent warmup); reweighted RSA (fit betas on 32-sample draws ×200 from non-515 NSD images, apply to held-out 515); noise-ceiling correction via leave-one-subject-out; Wilcoxon + Benjamini-Hochberg FDR.
- Framework: Keras 3 (backend-agnostic). Param budget: PredNet matched to 3% of PBN (33.7M vs 34.6M).

## When to Use / Related Work

- Use PBN when a task needs biologically plausible (local, hierarchical, predictive, probabilistic) learning WITHOUT giving up DNN-grade representations — e.g., neuroAI modeling, ventral-stream hypothesis testing, brain-aligned feature learning.
- Contrast with PredNet (video prediction focus, weak brain alignment, non-local loss), Whittington-Bogacz (small-scale exact PC inference, not deep-net scale), and plain self-supervised CPC (global backprop, no PC compliance).
- Open questions the framework enables: catastrophic-forgetting resilience of local PC learning, biological plausibility of learning trajectories, whether locality speeds convergence (observed informally: subtract variants converge earliest).

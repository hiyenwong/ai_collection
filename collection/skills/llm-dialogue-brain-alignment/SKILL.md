---
name: llm-dialogue-brain-alignment
description: Use when analyzing LLM brain alignment in dialogue fMRI.
trigger: LLM brain alignment, dialogue fMRI, language production vs comprehension, Natural Dialogue fMRI Dataset, intrinsic dimension GRIDE, LEACE concept scrubbing, dialogue acts, Japanese LLM Swallow, encoding model layerwise alignment
category: ai_collection
---

# LLM Brain Alignment during Dialogue — Production vs Comprehension

Source: arXiv:2610.22961 (Nakagi, Chiba, Kishino — NTT Inc., cs.CL/cs.LG/q-bio.NC, 16 Oct 2026). First whole-brain voxelwise decomposition of LLM–fMRI alignment during live DIALOGUE, separating language production from comprehension, across LLM layers, brain ROIs, and dialogue context lengths.

## Why it matters

Prior brain-alignment work is almost entirely passive comprehension (reading/listening). Dialogue adds production + comprehension + communicative intent (dialogue acts). This paper shows the alignment profile is mode-dependent: production and comprehension share the intermediate-layer peak but diverge regionally, and the features that carry alignment differ by mode (concrete lexical info dominates production; abstract communicative info adds to comprehension).

## Mode-separated latent extraction (the core design)

For target speaker s and 1-TR segment x_t (TR=1s), with dialogue context c_t,l built by concatenating both speakers' utterances from the preceding l TRs chronologically:

- **Production**: h^P_t,l = π[c_t,l, u^P_t] — context + participant's own current utterance
- **Comprehension**: h^I_t,l = π[c_t,l, u^P_t, u^I_t] — context + own utterance + interlocutor's utterance

π = final-token latent, extracted per layer. Context lengths l ∈ {1, 4, 16, 32} TRs. Use conversational post-tuned LLMs for dialogue (here Japanese-tuned: Llama-3.1-Swallow, Gemma-2-Swallow, GPT-OSS-Swallow, 8–21B; main results on Llama-3.1-Swallow). Alignment increases monotonically with context length in both modes.

## Encoding pipeline

Voxel-wise ridge regression (himalaya), per-voxel λ via 5-fold CV on train (grid 1e-2..1e7), hemodynamic delays 2–9s, head-motion components removed from BOLD before fitting. 3-fold leave-one-session-out CV; Pearson r on held-out sessions. Null: 20-TR block shuffling ×1000, one-sided, FDR q<0.05. ROIs (Destrieux): A1, STG, STS, MTG, AG, MFG, IFG, SM.

## Finding 1 — Mode-specific regional alignment profiles

- Both modes peak at intermediate layers (extends the classic intermediate-layer result to dialogue) and both predict auditory + sensorimotor cortex.
- Production additionally: parietal; consistently high across ALL layers in SM and AG.
- Comprehension additionally: frontal; consistently high in A1 and STG; in A1 alignment rises AGAIN near output layers (relative depth 0.9–1.0) — a second peak unique to comprehension.
- Production map = auditory + sensorimotor + parietal; comprehension map = auditory + sensorimotor + frontal.

## Finding 2 — Intrinsic dimension predicts alignment per mode

ID (GRIDE estimator, Denti et al. 2022) computed per layer per mode; Spearman(ID, alignment) across layers, averaged in Fisher-z space:

- Whole-cortex: strong ID–alignment correlation in BOTH modes once context ≥ 4 TRs (the Cheng et al. 2026 "representational richness" hypothesis extends from passive comprehension to dialogue).
- Regional dissociation: A1 ID-correlation stronger for COMPREHENSION; SM stronger for PRODUCTION; language ROIs (AG/MFG/IFG) equal across modes. Pattern: regions dominant for a processing mode show the ID association for THAT mode.

## Finding 3 — LEACE feature-scrubbing ladder (unique contributions)

Four interpretable features, low → high level: bunsetsu count BC (utterance length; bunsetsu = minimal Japanese phrase unit), lexicon L (word one/multi-hot), POS, dialogue acts DA (communicative intention). LEACE concept scrubbing applied sequentially across ALL layers. Two analyses:

1. **Individual removal**: lexicon L is the largest single contributor at every layer in both modes; at layer 1 removing L drops alignment 79–86% (BC ~28–32%, POS ~72–75%, DA ~68–76%); at L13/L26/L32 removing L still costs 34–50%. L-contribution is even stronger for production.
2. **Unique contribution** (cumulatively erase lower-level features first, then measure each feature's residual effect — solves the nesting problem, e.g. backchannel DAs are short so BC/DA confound): BC dominant in SM (production) and A1/STG (comprehension) — articulatory/duration information; L dominant in temporal/parietal/frontal incl. AG; POS and DA dominant in surrounding higher-order regions — DA (most abstract) concentrates in frontal cortex + TPJ, consistent with ToM and multiple-demand networks (Fedorenko et al. 2024). BC/L are prominent from EARLY layers; POS/DA from INTERMEDIATE layers onward.

**Interpretation**: production alignment is carried more by concrete lexical content; comprehension recruits additional abstract, context-dependent information. Feature hierarchy maps onto cortical hierarchy.

## Limitations (stated)

3 models only (one family each), single dataset, casual Japanese everyday-topic dialogue, text-only (no audio/faces/gestures), 7 participants.

## Reuse patterns

- **Asymmetric latent design for dialogue**: comprehension input must include the participant's own utterance AND the interlocutor's; production only needs own. Copy this asymmetry when building dialogue encoding models.
- **1-TR segment + variable context window** is a cheap, effective scan of "how much context does the brain use".
- **ID (GRIDE) per layer × mode** as a model-derived alignment predictor — no training needed, complements feature scrubbing.
- **LEACE cumulative-erasure ladder**: order features low→high, erase cumulatively, measure each feature's UNIQUE effect — the correct way to attribute alignment among nested linguistic features (individual removal over-credits every correlated feature).
- Evaluate brain alignment across MULTIPLE processing modes, not just passive comprehension.

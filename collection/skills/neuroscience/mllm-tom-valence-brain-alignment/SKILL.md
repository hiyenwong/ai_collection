---
name: mllm-tom-valence-brain-alignment
description: Use when scoring MLLM ToM/valence annotations against fMRI.
trigger: MLLM annotation evaluation, Theory of Mind continuous rating, affective valence annotation, movie fMRI encoding, cartoon movie naturalistic paradigm, diffusion MLLM LLaDA-V, Qwen3-VL, Gemma 3, scalable annotation, rater reliability screening, lag-optimized correlation
category: ai_collection
---

# Brain-Aligned MLLM Annotation of Social/Emotional Movie Content (ToM + Valence)

Source: arXiv:2610.22706 (Huang, Zhang, Biswal, Di, Xu — NJIT, cs.AI/q-bio.NC, 15 Oct 2026). Evaluation framework for open-weight MLLMs as scalable frame-wise annotators of Theory of Mind (ToM) and affective valence in cartoon movies, validated behaviorally against continuous human ratings AND neurally via fMRI encoding models. Code/prompts: github.com/Yiran-H/functional-MRI-Movie-MLLMs.

## Pipeline (5 stages, all reusable)

### 1. Frame-wise MLLM rating
Sample frames every 0.8s (TP/DM, TR=0.8s) or 1.0s (PC, TR=2.0s). Same prompt template for all models, rating scale [-10,+10] matched to human joystick scale. Gaussian-smooth ratings (σ=2s), resample to TR grid. Models: autoregressive Qwen3-VL-8B-Instruct, Gemma 3 12B-IT + **diffusion-based LLaDA-V-8B** (first brain-alignment test of a diffusion MLLM — text via iterative masked-token denoising).

### 2. Temporal context conditions
Models first generate scene descriptions of preceding frames; a FIXED count of descriptions (5 for TP/DM, 4 for PC) is injected into the rating prompt, evenly spaced over lookback windows {4, 8, 12, 16}s. Fixed count = tests temporal REACH of context, not quantity.

### 3. Human rating reference + rater screening
Continuous joystick ratings (CARMA, 4Hz, [-10,10]); ToM cohort n=34, valence n=42. **Leave-one-out reliability screening**: correlate each rater with the mean of the others, drop the lowest 20% (retains 28/34 ToM, 34/42 valence raters), average survivors.

### 4. Lag discipline (human response delay)
Joystick ratings lag perceived content; models rate the presented frame directly. Compare model(t) vs human(t+L), L searched 0–6.4s in 1-TR steps. Because lag selection and evaluation use the same data, lag-optimized r* is UPWARD-BIASED — always report unshifted r0 as primary, r* as exploratory (here: median gain 0.025, max 0.09 → agreement is lag-robust).

### 5. fMRI encoding
114 ROIs (100 Schaefer cortical + 14 AAL subcortical). Subject-specific multi-output ridge; ROI-specific coefficients, shared λ from 40 log-spaced values 1e-3..1e10 by mean inner-CV R²; fixed 4s hemodynamic delay; nested temporal CV over contiguous 16-s segments assigned intact (every TR tested exactly once); Pearson r per ROI; one-sided sign-flip permutation (5000) on subject-level r; BH FDR q<0.05 per source×movie×measure. Datasets: The Present (87 subs), Despicable Me (83), Partly Cloudy (82; children+adults).

## Key findings

1. **Valence > ToM asymmetry**: mean human–model r = 0.434 (valence) vs 0.265 (ToM) across models/movies. Visible expressions give accessible emotional cues; mental-state inference needs beyond-frame context (worst on dialogue-rich DM where models saw no audio dialogue).
2. **Models cluster with models, not humans**: inter-model agreement exceeds human–model agreement in nearly all pairs. Systematic distribution shifts: LLaDA-V and Qwen3-VL rate higher than humans (esp. ToM); Gemma 3 closest to human rating distributions.
3. **Context helps autoregressive, not diffusion**: preceding scene descriptions improve Qwen3-VL/Gemma 3 alignment (sweet spot 8–12s lookback); LLaDA-V flat. Context can HURT: Gemma 3 ToM on TP dropped at 4s lookback — injected descriptions induced over-interpretation of ambiguous scenes ("combined with the previous moments..." vs "lack of context..."). Treat MLLM context as double-edged.
4. **MLLM ratings are brain-predictive**: significant held-out encoding in visual, dorsal-attention, default-mode (valence esp. extensive), salience/ventral-attention networks. In The Present, MORE ROIs reached significance for MLLM ratings than for human ratings; but spatial overlap was mostly model–model. Human-inclusive overlap concentrated in posterior cingulate/precuneus (bilateral) and, in DM, one focal 4-source ROI (right temporo-occito-parietal salience network — the only ROI significant for human AND all three models).
5. **Counting caveat** (methodological): each rating source is tested against zero SEPARATELY — "more significant ROIs for X than Y" does NOT mean X predicts the brain better than Y. Direct source comparisons need paired tests.

## Limitations (stated)

Encoding ≠ human-like social understanding (ratings may covary with character presence, visual motion, arousal); frame + text descriptions miss audio; adult raters vs largely child/adolescent scanners (adult reference only); lag-optimized r* exploratory; generative architecture effect not isolated (model ≠ architecture alone).

## Reuse patterns

- **MLLM-as-annotator validation stack**: behavioral agreement + distribution check + context ablation + fMRI encoding — the minimal complete evidence set before trusting MLLM annotations as stimulus features.
- **Rater screening (LOO, drop lowest 20%)** before averaging any human continuous-rating reference.
- **Fixed-count evenly-spaced context injection** to dissociate temporal reach from token budget.
- **Report unshifted r0 as primary**; lag-optimized r* only as exploratory with the bias stated.
- **Overlap maps split into model-only vs human-inclusive** — inter-model convergence alone can masquerade as human alignment.
- Prefer open-weight models (reproducibility) over proprietary annotators; span architecture families (AR vs diffusion) when claiming "MLLM" conclusions.

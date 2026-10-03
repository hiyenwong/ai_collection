---
name: simpleb2t-timing-shortcut-brain-to-text
description: Timing leakage in word-aligned B2T decoding. Use when building M/EEG speech decoders or benchmarks.
category: ai_collection
version: "1.0.0"
source: arXiv:2609.40359
source_title: "Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text"
authors: "Dulhan Jayalath, Oiwi Parker Jones (Neural Processing Lab, Oxford)"
published: 2026-09-30
categories: "cs.LG, q-bio.NC"
trigger_words:
  - brain-to-text decoding
  - word-aligned B2T
  - timing shortcut
  - shortcut learning BCI
  - MEG speech decoding
  - overlapping window leakage
  - LLM rescoring BCI
  - synthetic control
---

# SimpleB2T: Removing Timing Shortcuts in Non-Invasive Brain-to-Text

**arXiv**: 2609.40359 (30 Sep 2026) · Jayalath & Parker Jones, Neural Processing Lab, Oxford
**Code**: github.com/neural-processing-lab/SimpleB2T · Benchmark: github.com/neural-processing-lab/pnpl

## TL;DR

The influential d'Ascoli et al. (2025) word-aligned brain-to-text (B2T) pipeline — jointly decoding all
word-aligned windows of a sentence with a transformer — gains almost **nothing from brain data**.
Fixed-length (3 s) windows extracted from a continuous M/EEG recording at each word onset overlap
(natural speech: 99.9996% of adjacent pairs overlap, sharing 90.6% of samples). The relative offset of
shared samples reveals inter-onset intervals → word duration → word identity priors ("the" is short,
"supercalifragilisticexpialidocious" is not). A **synthetic signal with zero brain information but the
same overlap structure reproduces the entire reported gain** (22.0% vs 22.3% balanced accuracy on real
MEG). Fix: decode each window **independently** (20M-param CNN+MLP instead of 200M-param transformer),
aggregate k observations, and rescore with an LLM prior → **WER 36.6%** on a clinical benchmark
(invasive landmark: 25.6%, Moses et al. 2021).

## The Shortcut, Formally

Windows are extracted from one continuous recording X(t):
```
x_i   = X[t_i : t_i + 3s]
x_i+1 = X[t_i+1 : t_i+1 + 3s]        # t_i+1 << t_i + 3s in natural speech
```
Because both windows contain the same samples at relative displacement d = t_i+1 − t_i:
```
x_i[n + d] = x_i+1[n]   in the overlap region
d = argmin_ℓ Σ_c Σ_n (x_i^c[n+ℓ] − x_i+1^c[n])²    # trivially recoverable by SSD matching
```
Onset interval ↔ word duration correlation r = 0.90. So jointly encoding all windows gives the model
the duration of every word for free — a shortcut (Geirhos et al. 2020) that does not transfer to
intended use (decoding from neural activity).

**Evidence ladder (the reusable methodology)**:
1. **Joint (MEG)**: full d'Ascoli decoder → 22.3% top-1 balanced accuracy (50-word vocab)
2. **Isolated (MEG)**: same encoder, windows processed independently → 9.5%
3. **Joint (synthetic)**: replace MEG with a continuous signal unrelated to the stimulus, same onsets → **22.0%**
4. **Isolated (synthetic)**: independent synthetic per window (no shared samples) → 5.8%
5. **Timing-only**: feed only the log inter-onset intervals → 22.9%

Additional fingerprints of duration-driven decoding:
- Joint decoder is much more accurate for words whose duration is *consistent* across training
  occurrences (r = 0.41 duration-σ vs accuracy) — isolated decoder: r = 0.33, much weaker.
- Top-10 predictions' typical durations match the *specific occurrence's* duration (r = −0.90***).
- Of d'Ascoli et al.'s 9 datasets, only the two reading protocols with fixed per-word time
  (LittlePrinceRead, Nieuwland) are shortcut-free — and those are exactly the only two where joint
  decoding showed no benefit. Cross-paper consistency check.

## The Fix: SimpleB2T

### 1. Independent word decoding
Keep d'Ascoli's CNN word encoder + T5-large embedding targets + contrastive training, but drop the
joint 16-layer bidirectional transformer entirely:
```
ẑ_i = f_θ(x_i)                       # small CNN → temporal pooling → residual MLP, ~20M params
p_brain(w | x_i) = softmax(ẑ_i^T e_w / T)   # temperature T tuned once on validation
```
No window ever sees another window → shortcut unlearnable by construction.

### 2. Aggregating k observations (agreement-weighted)
Encode k distinct recordings of the same word, average the (unit-normalized) embeddings:
```
m_i = (1/k) Σ_j ẑ_i,j        r_i = ||m_i||₂      u_i = m_i / r_i
A_i(w) = (1 + α r_i) · u_i^T e_w / T
```
r_i measures inter-observation agreement (→1 when predictions point the same direction).
α=2 selected on dev set. Agreement modulates score sharpness — normalizing away r_i would discard it.

### 3. LLM rescoring
```
S(y) = Σ_i A_i(w_i) + λ log p_LLM(y | q)      # beam search over 92-word vocab, λ=0.5, beam 200
```
- p_LLM: Qwen3-8B **base** model. Prompt q matters: task-oriented prompt ("patient communication
  needs...") 36.6% vs generic prompt 55.2%.
- Sentence length known (word-aligned setting), decoding terminates after n words.
- Oracle selection among top beam candidates would reach 16.4% → ranking, not generation, is the
  remaining bottleneck.

### Key results (Core clinical set, k=5)
| Method | k | WER ↓ | SMR ↑ |
|---|---|---|---|
| LM only | – | 73.8 | 2.0 |
| d'Ascoli (joint) | 5 | 98.9 | 0.0 |
| d'Ascoli + LM | 5 | 79.4 | 2.4 |
| SimpleB2T | 1 | 65.6 | 6.4 |
| SimpleB2T | 5 | **36.6** | **26.0** |
| shuffled brain + LM | 5 | 88.3 | – |
| noise + LM | 5 | 97.1 | – |

- Complementarity: brain helps verbs, LM helps function words; 74.3% (brain) + 73.8% (LM) → 36.6%.
- Crucially, **aggregation and LM rescoring only work after shortcut removal**: with the joint
  (shortcut) model, aggregation just improves the duration estimate through the same leak, and LM
  rescoring adds little beyond the LM itself (77→79% WER).

## Implementation Checklist (for any word-aligned neural decoder)

1. **Audit window construction**: if windows from a continuous recording are extracted at event
   onsets and (any of) them are modeled jointly, quantify overlap. If overlap exists and onset
   intervals vary, you have a duration channel.
2. **Run the synthetic control**: same pipeline, stimulus-unrelated continuous input (matched
   statistics), same onsets. If accuracy ≈ real-data accuracy → your gain is not neural.
3. **Also run**: timing-only input (log intervals), and non-overlapping natural sentence control
   (truncate windows at word boundaries — note truncation itself leaks timing, so prefer independent
   processing).
4. **Independent processing per window** is the simplest leak-proof design; sentence-level structure
   should enter only at the *scoring* stage (LLM prior), never the *encoding* stage.
5. **Aggregate multiple observations** with the agreement-weighted mean above (P300-speller
   tradition; 5 observations give large gains vs 100/phoneme in the 2025 PNPL competition).
6. **LLM prior**: constrained domain → describe the domain in the prompt; tune λ once on dev;
   base (non-instruct) model suffices.
7. Report WER **and** SMR (sentence match rate); report brain-only, LM-only, noise, and shuffled
   controls.

## Pitfalls

- **Truncating/masking windows at word boundaries re-leaks timing** — boundary position encodes
  duration. Independent processing is the only clean fix in word-aligned settings.
- The shortcut issue is *not* limited to d'Ascoli: extends to Brain2Qwerty-style keystroke-aligned
  windows (though timing explains little of its performance — synthetic control on typing intervals
  run in Appendix A.7), and to any pipeline jointly modeling overlapping aligned inputs (reading
  paradigms with variable per-word time, video, ECoG windows).
- Word-aligned B2T ≠ open-loop decoding: onsets are assumed known (as in Moses et al., who used a
  separate speech detector). Segmentation-free decoding is a harder, different task.
- WER gains from k observations trade recording time; report k explicitly.
- This critiques *perceived*-speech decoding; imagined/internal speech remains the open frontier.

## Applications

- Non-invasive speech BCI evaluation hygiene (MEG/EEG word decoding benchmarks: NeuralBench, PNPL).
- Shortcut audits for any "aligned-window + joint model" pipeline (also typing, listening paradigms).
- Design pattern: independent encoders + symbolic/LLM scorer for low-SNR neural decoding.
- Brain-attention/alignment claims based on word-aligned joint decoders need revalidation.

## Related Skills

- [[brain-mri-foundation-clinical]] (benchmark hygiene patterns)
- [[eeg-decoding-scaling-laws]] (data scaling context for EEG decoding)
- [[untrained-cnns-match-backpropagation-v1-rsa]] (RSA cautionary context)

## Source

arXiv:2609.40359 — Jayalath, D. & Parker Jones, O. (2026). *Removing Timing Shortcuts Improves
Non-Invasive Brain-to-Text*. ICML 2026 submission. Data: LibriBrain100 (MEG, ~80 h subject-0 split).

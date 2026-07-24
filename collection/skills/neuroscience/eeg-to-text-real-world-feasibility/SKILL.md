---
name: eeg-to-text-real-world-feasibility
description: "Neuropsychology-inspired EEG-to-Text benchmark (COFETT) that addresses EEG instability and enables teacher-forcing-free evaluation, providing evidence for real-world EEG2Text feasibility. Use when evaluating or building non-invasive brain-to-text decoders, designing EEG benchmarks, or studying EEG instability in neural decoding."
---

# EEG-to-Text Real-World Feasibility (COFETT)

## Description

This skill summarizes the methodology and findings of the ACL 2026 paper *Is EEG-to-Text Feasible in Real-World Scenarios?* (arXiv:2607.18749). The authors argue that existing EEG2Text benchmarks have been evaluated with teacher-forcing, which masks exposure bias and inflates performance. They identify **EEG instability**—trial-to-trial and session-to-session shifts in signal statistics and spatial topography—as a neglected confound, and introduce **COFETT**, a 128-channel high-density EEG dataset collected with a neuropsychology-informed inner-speech imagery paradigm. COFETT supports teacher-forcing-free evaluation and shows stronger discriminative power among model architectures than prior benchmarks.

## When to Use

- Designing or evaluating EEG-to-text / brain-to-language decoders
- Building benchmarks for neural decoding, especially with EEG
- Studying EEG instability, non-stationarity, and cross-session generalization
- Comparing teacher-forcing vs. autoregressive evaluation for sequence decoders in BCI
- Collecting high-density EEG datasets for inner speech or imagined speech

## Core Contributions

1. **COFETT dataset** — 128-channel high-density EEG recordings collected with a multi-round inner-speech imagery paradigm; repeated readings across sessions explicitly account for EEG instability.
2. **Teacher-forcing-free evaluation** — Prohibits ground-truth token feeding during inference, measuring genuine linguistic decoding from EEG rather than exposure-bias-inflated scores.
3. **Feasibility evidence** — Shows that EEG contains linguistically decodable information and that robust evaluation protocols can distinguish model architectures, opening a path toward practical non-invasive BCI communication.

## Key Concepts

- **EEG instability**: Temporal drift in EEG signal statistics and topography within the same participant, driven by attention, fatigue, electrode impedance, and physiological fluctuations. This makes cross-session decoding difficult.
- **Teacher-forcing evaluation**: Sequence-model evaluation that feeds the ground-truth previous token to predict the next token. Inappropriate for real-world use because ground-truth tokens are unavailable; it masks exposure bias and can make models appear meaningful even when fed random noise.
- **Neuropsychology-informed paradigm**: Data collection design that maximizes recoverable linguistic signal through carefully spaced repetitions and multi-round inner-speech imagery.
- **COFETT**: Corpus OF Eeg-To-Text, a dedicated benchmark for EEG2Text evaluation. Open-sourced at https://github.com/baoyudu/COFETT.

## Workflow

### 1. Diagnose Benchmark Limitations
- Check whether reported EEG2Text results use teacher-forcing during evaluation.
- If so, re-evaluate models autoregressively (no ground-truth tokens at inference).
- Check whether the dataset accounts for cross-session / cross-day EEG instability.

### 2. Collect or Augment Data for Stability
- Use high-density EEG caps (e.g., 128 channels) to capture spatial topography.
- Include repeated readings of the same linguistic items across multiple sessions/days.
- Record participants in a consistent state and track electrode impedance/quality.

### 3. Build a Teacher-Forcing-Free Evaluation Protocol
- Train sequence decoders with any teacher-forcing schedule during training (standard practice).
- At inference, generate text autoregressively from the EEG-conditioned initial token.
- Report metrics such as BLEU, ROUGE, CIDEr, BERTScore, and semantic similarity on the generated text, not on teacher-forced outputs.
- Compare model performance against random-EEG and shuffled-label baselines to detect inflated scores.

### 4. Apply Stability-Aware Preprocessing
- Consider common spatial patterns (CSP) or stationary CSP variants biased toward invariant subspaces.
- Apply domain adaptation or adversarial normalization to reduce session shifts.
- Use correlated components analysis (CCA) or similar methods to align session-specific EEG distributions.

### 5. Interpret Results with Neuroscience
- Compare learned representations to known language-related EEG components (e.g., N400, P600-like effects).
- Analyze whether the model relies on genuine neural signals rather than artifacts (eye movement, muscle noise).
- Report cross-session generalization as the primary robustness criterion.

## Pitfalls

- **Teacher-forcing inflation**: High BLEU/ROUGE under teacher-forcing does NOT imply real-world usability. Always evaluate autoregressively.
- **Ignoring EEG instability**: Models trained on a single session may fail dramatically on data collected a day later from the same subject.
- **Small datasets**: COFETT emphasizes repeated within-participant data over large cross-participant data; design studies accordingly.
- **Artifact leakage**: Ensure models are not exploiting eye-tracking or muscle correlates that happen to align with linguistic labels.

## Activation Keywords

- EEG-to-text
- EEG2Text
- brain-to-text
- teacher-forcing-free evaluation
- EEG instability
- cross-session EEG
- COFETT
- inner speech decoding
- non-invasive BCI
- 128-channel EEG
- neural decoding benchmark
- neuropsychology-informed paradigm

## Resources

- Paper: https://arxiv.org/abs/2607.18749
- Dataset & code: https://github.com/baoyudu/COFETT
- DOI: https://doi.org/10.18653/v1/2026.acl-long.61

## References

- Zhang, Z., Bao, Y., Ding, X., Jiang, T., & Xiong, K. (2026). Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark. *Proceedings of ACL 2026*, 1378–1393.

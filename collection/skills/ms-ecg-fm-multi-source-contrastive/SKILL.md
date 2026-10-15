---
name: ms-ecg-fm-multi-source-contrastive
description: Use when building ECG/biosignal foundation models. Multi-source contrastive alignment.
category: medical
---

# MS-ECG-FM: Multi-Source Contrastive ECG Foundation Model

**Source**: MS-ECG-FM: Towards a More Universal Electrocardiogram Foundation Model for Health Monitoring using Multi-source Contrastive Learning (arXiv:2610.07662, Apple/MIT, Oct 2026)

## Core Insight

Prior ECG foundation models are limited by using **ECG interpretation reports as the sole supervision**. Machine reports only capture what clinicians routinely annotate, capping representation richness. MS-ECG-FM instead aligns one waveform to **multiple distinct clinical note types** — ECG machine reports, echocardiography (ECHO) reports, chest X-ray/radiology reports, and discharge summaries — capturing complementary diagnostic signal.

## Reusable Methodology

### 1. Multi-source stochastic pairing
- Each ECG instance i has an available report subset R_i (reports are sparsely co-occurring).
- On each pre-training draw, pick ONE report type uniformly at random: r_i ~ Uniform(R_i).
- Rationale: prevents the encoder from collapsing onto the easiest (most tightly coupled) report type; forces broader discriminative feature learning. ECG machine reports are trivially coupled to the waveform; discharge summaries share only a fraction of information — stochastic selection regularizes across this coupling-strength spectrum.

### 2. Frozen text encoder + offline embeddings
- Use a strong pre-trained medical text encoder (MedGemma-27B here) **frozen**, with text embeddings computed OFFLINE before pre-training.
- Contrastive loss only trains the waveform encoder + projector: InfoNCE over cosine similarity with learnable temperature.
- Benefits: (a) avoids instability/catastrophic forgetting of jointly-trained text tower, (b) large memory savings — discharge reports reach 15K tokens, ECHO 1.1K; embedding them offline removes the text tower from the training loop entirely.
- Follows the "lock a strong pre-trained encoder" pattern (LitLa-Flexi in image-text).

### 3. Preserve absolute amplitude — do NOT normalize the waveform
- Key ECG diagnoses depend on absolute voltage (LVH via Sokolow-Lyon/Cornell criteria). Per-lead/per-recording z-scoring or min-max destroys the scale information.
- **No input normalization**; instead stabilize training with **batch norm after each conv layer** in the tokenizer (batch norm preserves cross-sample scale statistics; per-sample layer norm would not).

### 4. Architecture & augmentation
- Deep conv tokenizer (patch 250 samples = 0.5 s @ 500 Hz) → 12 leads × 20 = 240 tokens; weights shared across leads; learnable lead-identity embeddings + sinusoidal temporal PE; transformer backbone; global average pooling.
- Augmentation: random lead masking (RLM) + stochastic time-shift. RLM directly promotes reduced-lead robustness.

### 5. Checkpoint selection without OOD leakage
- Select pre-trained checkpoint via **RankMe** (unsupervised effective-rank of embedding singular values) on in-distribution validation embeddings — never via OOD zero-shot validation (which leaks test signal into model selection).

## Key Results
- 98-label linear-probe benchmark: macro AUROC 93.6 vs 91.5 (ECGFounder, strongest baseline) and 91.2 (MELP, same-data baseline).
- Reduced-lead configs (single lead I/II/V2, subsets): consistently strongest except ARR/ECG-HYP on single V2.
- Single-source ablations confirm: no single report type is universally best; ECG-CR (cardiologist-edited) best for ECG-centric labels; other note types lift complementary domains.

## Transferable Patterns (beyond ECG)
1. **Multi-report stochastic pairing**: any modality with multiple heterogeneous co-occurring text reports (imaging + labs + discharge) — draw one report type per step to regularize alignment.
2. **Frozen-encoder offline text embeddings**: cuts text tower memory to zero when long documents (up to 15K tokens) are contrastive targets.
3. **Domain-critical invariants (amplitude)**: identify diagnosis-relevant raw-signal invariants BEFORE choosing normalization; replace per-sample norm with batch-level statistics when scale carries meaning.
4. **Unsupervised checkpoint selection (RankMe)**: effective-rank of embedding covariance detects collapse without touching downstream/OOD data.

## Activation
ECG foundation model, biosignal SSL, clinical multimodal contrastive, multi-source report alignment, frozen text encoder, RankMe selection, reduced-lead, LVH amplitude preservation

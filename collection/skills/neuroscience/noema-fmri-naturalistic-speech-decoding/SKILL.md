---
name: noema-fmri-naturalistic-speech-decoding
description: Use for decoding naturalistic speech from fMRI (NOEMA).
category: ai_collection
---

# NOEMA — Temporal Convolutional fMRI Decoder for Naturalistic Speech Retrieval

**Source**: Caris, Jalouzot, Rajabi, Ilinca, Hassayoune, Muminov, Delebarre, Fonteneau, Maussion, Thirion, Thual, Collas — "Decoding Naturalistic Speech from fMRI with Temporal Modeling and Multimodal Alignment" (arXiv: 2610.22049, Karavela/UNICOG/Inria, 15 Oct 2026).

**Trigger words**: fMRI decoding, naturalistic speech, brain-to-text retrieval, temporal convolutional network, TCN, multimodal stimulus embeddings, CLIP contrastive alignment, hemodynamic lag, Cephalonauts One, LeBel, retrieval evaluation, distractor generalization, session-disjoint split, integrated gradients language cortex

## Core Idea

fMRI decoders for static stimuli exploit spatial patterns; naturalistic speech unfolds over time but BOLD is noisy and temporally smeared. NOEMA (Neural Ordered Embeddings with Multimodal Alignment) combines both: a **temporal convolutional decoder** maps a window of 7 consecutive fMRI frames to a **concatenated multimodal embedding** (text + audio + speech encoders) of the corresponding stimulus segment, trained with CLIP contrastive loss, evaluated as **segment retrieval** (rank the true segment among ~2000 candidates by cosine similarity).

## Architecture (253.8M params — arithmetically verified)

```python
class TCNblock(nn.Module):
    def __init__(self, hidden_dim, dilation):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size=3, padding=dilation, dilation=dilation),
            nn.GELU(),
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size=1),
        )
        self.norm = nn.LayerNorm(hidden_dim)
    def forward(self, x):  # x: (batch, frames, hidden_dim)
        return self.norm(x + self.layers(x.transpose(1, 2)).transpose(1, 2))

class NOEMA(nn.Module):
    def __init__(self, input_dim, output_dim=8704, hidden_dim=4096, dropout=0.7):
        super().__init__()
        self.spatial = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.GELU(), nn.Dropout(dropout))
        self.temporal = nn.Sequential(TCNblock(hidden_dim, dilation=1), TCNblock(hidden_dim, dilation=2))
        self.output = nn.Linear(hidden_dim, output_dim)
    def forward(self, x):  # x: (batch, frames, input_dim)
        x = self.temporal(self.spatial(x))
        return self.output(x[:, x.shape[1] // 2])   # central-frame readout
```

- Spatial projection: pointwise per frame, V=20,484 fsaverage5 cortical vertices → H=4096, GELU, **dropout 0.7**.
- Two residual TCN blocks (kernel 3, dilations 1,2) ⇒ central frame sees a **7-frame receptive field** (1+2+4), noncausal.
- Only the central frame is projected to the D=8704 target; only it takes the training loss.
- **Hemodynamic lag**: for stimulus context ending at t, the fMRI window is centered at t+2.5s (peak alignment; NOEMA near-peak across offsets).

## Multimodal Target Construction

Three frozen encoders, all precomputed (never trained):
- **Text**: Qwen3-Embedding-8B, transcript words with end-time ≤ t over 10s context → 4096d (last non-padding token).
- **Audio**: LCO-Embedding-Omni-7B on the 10s waveform → 3584d.
- **Speech (ASR)**: Parakeet-TDT-0.6B-v3, window (t−Δ, t] with Δ=2.08s marker spacing, mean-pooled penultimate layer → 1024d (temporally precise, tiles stimulus without overlap).
Each modality is **ℓ2-normalized separately, then concatenated** (so cosine similarity normalizes the whole concatenated vector). At inference the decoder sees only fMRI; candidates are precomputed.

## Training & Evaluation Protocol

- CLIP loss over batches (B=4096), temperature τ=6.2e-3 (per-model Optuna-tuned), AdamW lr=1.1e-4, wd=6.8e-3, early stopping patience 10.
- **Session-level splits only** (random splits leak: consecutive frames share stimulus + autocorrelation). 5 folds, held-out session = test, another = validation. No stimulus repeated within a participant.
- Preprocessing: DeepPrep, fsaverage5 surface, per-run detrend+standardize; Cephalonauts One TR=0.52s → 4-TR moving average, keep every 4th frame → Δ=2.08s; LeBel Δ=2.0s native.
- Metrics: Top-10@M accuracy, median rank, **median relative rank** (rank/M — comparable across retrieval-set sizes).

## Key Results

- Top-10@2000: **42.7%** (Cephalonauts One, 3 subj × ~30h French podcasts) and **43.6%** (LeBel, 3 subj × 16h English stories); chance 0.5%. Beats Ridge / single-frame MLP / MindEye MLP / **Context MLP with identical 7-frame input** (which has more params: 623.0M vs 253.8M).
- Stimulus representations (Cephalonauts): text-only 27.6% → +audio 35.5% → +speech-ASR **42.7%** — complementary targets, largest gains for NOEMA (+1.58/+2.34 pp over Context MLP).
- Temporal context: 1→7 frames 28.7%→42.7% for NOEMA (Context MLP 25.4%→34.5%@5f, declining to 33.7%@7f).
- **Frame-order shuffle ablation** (retrained, rule applied at train+test): fixed global permutation: Context MLP +0.33 pp (dense layer absorbs it) vs NOEMA −4.26 pp; per-sample permutations: −10.90 vs −18.46. NOEMA's advantage is chronology-matched inductive bias, not just capacity.
- **Extended retrieval**: adding up to 8,494 ten-second segments from 50 unseen same-podcast episodes (5.1× larger set, no retraining): median rank +66 (NOEMA) vs +112 (Context MLP) vs +191 (MLP); all models grow sub-proportionally; NOEMA keeps lowest median relative rank (0.9% of pool).
- Interpretation: integrated gradients → lateral temporal cortex + frontal patches (language network, Fedorenko/Pallier-consistent), no left-right asymmetry (echoes Bonnasse-Gahot & Pallier: asymmetry re-emerges only with larger LMs); only NOEMA shows central-frame importance bias.

## When to Use

- Building fMRI (or other slow-signal) decoders for naturalistic/time-varying stimuli — retrieval-first, generation later (predicted embeddings can guide LM beam search).
- Deciding target representations for brain decoding: concatenate ℓ2-normalized text+audio+ASR embeddings from frozen large encoders.
- Designing leak-free evaluation: session-disjoint splits + distractor-extended retrieval + median relative rank.
- Attributing decoder gains: context-length sweeps, input-shuffle retraining (isolates temporal inductive bias), and modality-additive ablations.
- Hemodynamic lag handling: align window center to stimulus end + ~2.5s, tune by ablation.

## Limitations

- 6 participants total, participant-specific decoders; cross-participant generalization untested.
- 7-frame receptive field is an architecture bound, not an established optimum.
- Retrieval from a finite candidate set ≠ unrestricted reconstruction (although distractor extension shows robustness).

---
name: matched-input-eeg-fm-audit
category: ai_collection
description: Use when auditing EEG foundation models on BCI transfer.
version: 1.0.0
source: https://arxiv.org/abs/2609.23924
source_title: "Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery"
authors: "Kevin Zhou, Sparsh Roy"
published: 2026-09-20
arxiv_categories: cs.LG, q-bio.NC
trigger_words:
  - EEG foundation model audit
  - matched-input control
  - validation-locked protocol
  - LaBraM CBraMod motor imagery
  - BCI benchmark leakage
  - temperature scaling calibration
---

# Matched-Input EEG Foundation-Model Audit

Methodology from arXiv:2609.23924 — Zhou & Roy (Sep 2026). A leakage-controlled audit of pretrained EEG encoders (LaBraM, CBraMod) on motor imagery, whose central methodological finding is that **matched-input control estimates flip sign across comparator architectures** — so single-comparator decompositions of "pretrained vs supervised" gaps are untrustworthy.

## When to Use

- Benchmarking EEG/brain-signal foundation models (LaBraM, CBraMod, BIOT, etc.) against supervised baselines
- Designing a leakage-proof evaluation protocol for cross-session BCI (or any small-N subject study)
- Deciding whether input-pipeline differences (band, sampling rate, scaling) explain a model gap
- Reporting calibration alongside accuracy for downstream BCI deployment

## Protocol: Validation-Locked Evaluation

1. **Split by session** (not random trials): training session → 80% fit / 20% selection; held-out session touched exactly once after configuration lock.
2. **All tunable decisions from training data only**: preprocessing, architecture, LR, freeze depth, checkpoint, temperature, method selection. Store machine-checkable provenance artifacts (SHA256 manifest) — every table regenerated from artifacts by script, no manual transcription.
3. **Architecture-matched random-init control**: same encoder trained from scratch separates "pretrained weights carry task-relevant info" from "architecture is hard to train on ~230 trials". Verify checkpoint loading (178/179 tensors differ from fresh init).

## Core Findings (BCI Competition IV-2a, 4-class, n=9 subjects)

| Configuration | Acc | Brier | ECE |
|---|---|---|---|
| ShallowConvNet | 0.6962 | 0.4047 | 0.0808 |
| ATCNet (broadband) | 0.6562 | 0.4695 | 0.1062 |
| EEG Conformer (broadband) | 0.5305 | 0.5858 | 0.1072 |
| CBraMod fine-tuned | 0.4796 | 0.6493 | 0.1236 |
| CBraMod frozen | 0.3927 | 0.7080 | 0.1030 |
| CBraMod random init | 0.3407 | 0.7396 | 0.0993 |
| LaBraM frozen | 0.3322 | 0.7323 | 0.0874 |

1. **Every supervised comparator beats every foundation-model configuration** (fine-tuning included). Paired comparisons hit the exact-Wilcoxon floor; zero subject wins for FM arms. Pretrained-vs-random-init effect is robust across 3 reseeds (+0.130–0.139 acc) — pretraining DOES help over random init, just not to supervised level.
2. **Matched-input term (narrow−broad, same architecture)**: ATCNet −0.078 (broadband better, 8/9 subjects) vs EEG Conformer +0.088 (narrowband better, 8/9) — **opposite signs**. None survives BH correction individually (p=0.073/0.304/0.176), so treat descriptively: never apportion a "pipeline share" percentage from one comparator.
3. **Task-dependence**: the 4-class deficit does NOT reproduce on 2-class BNCI2014-004 (CBraMod fine-tuned 0.8085 vs best supervised 0.8458 — competitive). Dataset identity + channel count changed simultaneously, so don't attribute to class count alone.
4. **Fine-tuning recipe is not transferable**: validation favors 10 frozen LaBraM blocks @1e-4 but FULL CBraMod unfreezing @5e-4. Models peak before warm-up ends under reference recipes — per-model re-tuning is mandatory.
5. **Calibration ≠ discrimination**: raw FM logits are severely overconfident (temperatures 3.5–9.5, some hitting 20 cap vs ~1.03 supervised). One validation-fitted temperature returns FM ECE to supervised range (0.103–0.124) despite much lower accuracy. Report both axes.
6. **Under-trained control check**: random-init arm extended to 240 epochs gained only +0.017 (best Brier 0.755 ≈ chance 0.750) — the deficit is not an artifact of under-training.

## Audit Checklist (copy into benchmark repos)

- [ ] Cross-session split; held-out labels never enter selection (enforced by artifact hashes)
- [ ] ≥3 supervised comparator architectures, independently tuned per input pathway
- [ ] Matched-input control repeated per architecture; report raw differences, NOT a single "pipeline share" percentage
- [ ] Architecture-matched random-init control with checkpoint-load verification + extended-epoch check
- [ ] Fine-tuning grid: freeze depth × LR, selected on validation only
- [ ] Subject-paired Wilcoxon + Benjamini-Hochberg within each family; state n and the attainable p floor (2^(1−n))
- [ ] Temperature scaling fit on validation, capped; report cap saturation count
- [ ] Distinguish "failure to detect" from "evidence of equality"

## Pitfalls

- **Within-session random splits inflate BCI IV-2a headline numbers** — many published results use them; only cross-session numbers are comparable.
- **Single-comparator matched-input decomposition is unstable** — the term can flip sign with architecture; replicate across architectures before interpreting.
- **Temperature repair is cosmetic for accuracy** — calibration ECE fixed ≠ discrimination fixed; on-device low-precision stability of the temperature is untested.
- **Small-N inference floor**: n=9 → min two-sided exact Wilcoxon p = 2·2^(−9) ≈ 0.0039; don't promise more.
- **AI-disclosure hygiene**: the authors restrict LLM use to prose editing post-analysis — keep model involvement out of design/data/results if following this protocol.

## Related Skills
- `identity-trap-eeg-foundation-models` — FMScope diagnosis of LaBraM/CBraMod identity reliance
- `eeg-fm-audit-systematic-evaluation` — ASHA benchmark + paradigm ablation pipeline
- `eeg-based-lm-evaluation` / `same-brain-different-prediction` — reliability and evaluation framings

## Source
- arXiv:2609.23924v1 [cs.LG, q-bio.NC], submitted 2026-09-20
- Code + per-subject artifacts + SHA256 manifest accompany the study (full reproducibility pipeline)
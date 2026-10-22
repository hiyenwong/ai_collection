---
name: pathology-vlm-controlled-probes
description: Use when evaluating pathology vision-language model claims.
trigger: pathology VLM evaluation, vision-language model computational pathology, SlideChat grounding, slide-level VQA, NOTA none-of-the-above control, text-only arm, mismatched slide control, paraphrase answer flip, prompt sensitivity zero-shot, stage redaction survival, report embedding prognostic, C-index language increment, TCGA benchmark contamination, tissue-source-site disjoint splits, supervised linear probe baseline, benchmark upper bound reading, medical VLM audit, whole slide image VQA robustness, agentic navigation self-reported, evidence tiers evaluation
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: leakbench-clinical-agent-leakage-audit, label-space-mismatch-cross-cohort-eval, retrieved-not-read-evidence-use-failure, eeg-based-lm-evaluation
---

# Four Controlled Probes of Pathology Vision-Language Models — What Language Adds, and at What Cost

**Source**: arXiv 2610.26805 (Zhang, Zhou, Ping, Wang, Li — UVA + Merck, 19 Oct 2026). Tier-1 controlled re-evaluation of released pathology VLM checkpoints on public TCGA data, **varying one input at a time** under a leakage-controlled harness (patient- and tissue-source-site-disjoint 5-fold splits; 1,000-resample bootstrap CIs; significance = CI excludes zero). Companion to a 51-system review. Headline: language adds **real but narrow** value — report text carries prognostic signal beyond stage, prompts add nothing at inference, and slide-level answers are neither grounded in the slide nor stable under rewording.

## When to Use

- Evaluating any **pathology (or general medical) VLM** claim: survival gains, zero-shot subtyping, slide-level VQA, agentic navigation, few-shot language priors.
- Designing an evaluation harness for multimodal medical models — the probe structure (frozen representation + fixed predictor/split + single-input variation) is the reusable pattern.
- Reviewing/grading published evidence: tier 1 = independent multi-system re-evaluation, tier 2 = third-party reproduction, tier 3 = self-reported numbers (most of the literature is tier 3).

## The Four Probes (protocol)

1. **Survival (language increment)** — 6 arms differing only in input: A vision; B vision+full report; B′ vision+**stage-redacted** report; C structured stage+grade; T_full/T_red report-text alone. Frozen PubMedBERT report embedding ⊕ frozen TITAN slide embedding → L2-penalized linear Cox. Contrasts: clean increment (B′−A), staging leakage (B−B′), text-channel leakage (T_full−T_red), text-vs-vision (T_red−A). n=1,633 TCGA (BRCA/LUAD/COAD), 394 PFI + 345 OS events.
2. **Subtyping (prompt isolation)** — L2 linear probes on frozen slide embeddings (CONCH v1/v1.5, TITAN, Prov-GigaPath; NSCLC n=930, RCC n=718). Within-encoder arm: zero-shot (top-k or mean pooling) vs supervised linear probe on the **same features** — any gap is attributable to the prompt, since features/pooling are fixed.
3. **Grounding (does the model read the slide?)** — slide-conditioned MCQ VQA with perturbation arms relative to unperturbed P0: **remove slide (text-only), zero features, mismatched slide, cyclic option shift, NOTA substitution** for the correct option. Compare against the most-frequent-letter baseline. A model that doesn't drop when the slide is removed isn't reading the slide.
4. **Wording robustness** — canonical vs paraphrase banks / prompt reframings (persona line) with slide+answer fixed. Report **accuracy change AND answer-flip rate AND consistency** — accuracy can be unchanged while 8–23% of answers flip.

## Findings to Reuse (with numbers)

- **Report text adds prognostic signal**: B′−A = **+0.019 C-index (PFI), +0.016 (OS)**, positive in all six cohort–endpoint settings; both leakage contrasts null (restoring stage adds nothing); stage+grade alone is the weakest arm. The signal is complementary information in the report (e.g., tumour size descriptions survive redaction), captured by a **frozen text encoder — not by a VLM**.
- **Prompts add no measurable accuracy**: with CONCH v1 features+pooling fixed, zero-shot ≈ supervised linear probe (Δ balanced accuracy −0.020 NSCLC / −0.019 RCC, CI includes 0). Top-k zero-shot advantage vanishes under shared pooling — an **instance-selection effect, not a prompt effect**. Language-aligned encoders beat pure-vision Prov-GigaPath under identical probes, but the cross-encoder comparison is confounded (backbone/data/dim differ).
- **Slide-level VQA is barely grounded**: SlideChat 74.82% with slide vs **74.41% without it** (gap 0.41, indistinguishable from 0); mismatched-slide gap also null. Its own language backbone (Qwen2.5-7B) blind scores 43.52% ≈ 40.7% letter baseline, so **~31 points of SlideChat's blind accuracy come from instruction-tuning regularities, not the slide** (74.41 − 43.52 = 30.89). Option shift significantly lowers accuracy; NOTA substitution pushes SlideChat **below the letter baseline** — it cannot reject remaining options when the correct content is removed.
- **Paraphrase: accuracy intact, answers unstable** — 8–23% answer flips under paraphrase, 25% under paraphrase+reframing (consistency 0.57); a single persona line significantly shifts Qwen3-VL accuracy. "In the clinic, where the same case must yield the same diagnosis, it is disqualifying."
- **Self-reported gains cannot yet be attributed**: CPathAgent's +15.4 over Gemini-2.5-Pro on PathMMU-HR2 shrinks to +2.9 over ABMIL at slide level and trails TITAN on CPTAC-Lung; prompted-to-navigate Gemini rises 73.2→76.4, so part of the "navigation" margin is promptable in any model. No intervals/seeds reported anywhere in tier-3 evidence → grade weakly supported.
- Benchmark contamination: PathMMU/PathVQA/Quilt-VA images come from literature/textbook/social sources that also populate pretraining corpora; TCGA slide benchmarks share cohorts with instruction-tuning data.

## Minimum Controls Checklist (propose for any medical-VLM evaluation)

1. Slide-conditioned VQA: report **text-only, mismatched-slide, option-shift, NOTA arms** alongside majority-answer baseline.
2. Report **answer-flip rates and consistency** under paraphrase/reframing, not just accuracy deltas.
3. Survival-with-text claims: include **stage-redacted and text-only arms** (B−B′ and T_full−T_red contrasts).
4. Prompt claims: **within-encoder** comparisons with features and pooling fixed.
5. **CIs and seeds** for every headline comparison; independent replication where possible.
6. Compute in six fields: GPU type/count, GPU-hours, peak train/inference memory, visual tokens per WSI, end-to-end latency on a reference slide.

## Design Implications

- Spend language where it is **irreplaceable**: prognosis (report text), interaction, reporting — not subtyping, where vision+linear probe already saturates.
- Grounding should be a **training objective**: answers cite tissue evidence, change when it changes, abstain when absent, stay invariant to paraphrase.
- Score-only systems fail through correlational shortcuts (e.g., tissue-source-site signatures passed by frozen encoders) **without a trace** — hallucinated text is at least inspectable; silent wrong predictions are not.
- Read benchmark scores as **upper bounds on what the model reads from the slide**, not as evidence that it does.

## Verification (this session)

- Internal arithmetic of headline claims checks out: 74.82−74.41 = 0.41 (blind gap ≈ 0) ✓; 74.41−43.52 = 30.89 ≈ "about 31 points from instruction-tuning regularities" ✓; 43.52−40.7 = 2.82 (backbone barely above letter baseline) ✓.
- Not reproduced: TCGA Cox fits / VQA inference (requires WSI pipeline + GPU); findings transcribed from the paper's tables with numbers cross-checked between abstract and body.

## Limitations (paper's own)

Probes cover released checkpoints on TCGA-derived data, 2 assistants, 3 language-aligned + 1 vision encoders; reasoning-tuned/agentic/MIL systems not directly probed. Null leakage contrast would also arise if the frozen text encoder were insensitive to stage; no arm combines vision with structured stage+grade; MCQ-only (free-text may differ); navigation/few-shot grades rest on self-reported numbers.

---
name: neuroact-dual-loop-eeg-autoresearch
description: Use when building EEG research agents. Dual-loop NeuroAct.
category: neuroscience
trigger: autonomous EEG research agent, dual-loop self-improvement, EEG foundation model adaptation, experience reuse, model combination, conditional recommendations, BrainBench
---

# NeuroAct: Dual-Loop Autonomous Research for EEG Analysis and Decoding

**Source**: "NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research" — Xiong et al. (Tongji/Ant Group/SJTU), arXiv:2610.25211 (Oct 2026).

## Core Results
- Setting A (EEG General Analysis, BrainBench): 80.88 macro vs BrainAgent 63.13 (+17.75); consistent >75 across DeepSeek-V4 Flash / GPT-5.6 Luna / Qwen3.8 Flash Next backends.
- Setting B (Cross-task Model Optimization): raises EEGPT 4-target mean BA 47.50→54.84, HBN Pearson r 0.6894→0.7362, MSE 6.080→5.447 within ONE shared checkpoint.
- Setting C (Single-task Open Research): ADFTD +16.33 BA (EEGNet 54.93 → ShallowFBCSPNet 71.26 after evidence-guided architecture switch).
- Setting D (Collaborative Prediction): Workload BA 79.69→85.02 (best member → score-shifted combination); ADFTD 71.26→74.89 via sample-dependent combination.
- Experience reuse: PhysioMI→BCIC-IV-2a transfer raises BA 34.66→50.81 while CUTTING tokens 64% (29.21M→10.51M).

## Architecture

### Inner loop — autonomous EEG research
- **Coordinator** decomposes the objective into parallel questions, dispatches specialist assignments, integrates handoffs, and selects next actions from (evidence Ht, implemented solutions Pt, adopted experience Kt, budget Bt): (ut, Jt) = πC(g, D, A; Ht, Pt, Kt, Bt). Can refine candidate, redirect exploration, revert to earlier solution, or stop.
- **Three specialist personas with SEPARATE contexts and permissions**: Researcher (literature + dataset semantics + EEG evidence → feasible proposal), Developer (implements proposal, executes analyses/training), Reviewer (challenges unsupported conclusions, examines implementation). Handoffs record: requested deliverable, supporting evidence, unresolved issues, actionable recommendation.
- **Investigation-as-experiment**: every proposed analysis must have outcomes that DISTINGUISH COMPETING EXPLANATIONS and imply different actions. When unresolved mechanisms would lead to different actions, run a discriminative analysis BEFORE an intervention experiment.
- **Progressive disclosure**: role contexts get compact capability indexes first (tool domains → operations → signatures; skill indexes → instructions; experience summaries → full evidence on demand). Only adopted content enters specialist assignments — context economy without losing access.
- Policies are prompted, not trained — behavior evolves via conditioning on accumulated evidence, no LLM parameter updates. Research budget capped (50M LLM tokens / 5 GPU hours); cost includes ALL attempted experiments.

### Evidence taxonomy (the diagnostic core)
Four evidence types drive intervention choice — this is what fixed pipelines and reward-driven search omit:
1. **Signal structure** (montage, reference, spectral content — e.g. undeclared reference → within-window relative power and band ratios instead of absolute power)
2. **Representations** (what the encoder preserves vs what the readout uses; patch-information retention)
3. **Predictor behavior** (per-class recall, error patterns, decision-rule vs discrimination changes)
4. **Training dynamics** (loss curves, gradient behavior, overfitting onset, validation instability)
Cross-model **error overlap** decides whether model-combination research is merited at all.

### Outer loop — experience-based self-improvement
- Experience items are **conditional, testable recommendations**: k = (c, a, e+, e−, b) — applicable task/model conditions c, recommended action a, supporting evidence e+, conflicting evidence e−, reassessment conditions b.
- **Distillation from contrasting outcomes**: compare an intervention's expected vs observed effects against considered alternatives.
- **Matching & adoption**: retrieval filters incompatible entries, ranks by task/model compatibility, goal overlap, source evidence, paradigm, class structure; Coordinator decides adopt / bounded applicability check / reject. Candidate advice shown to Coordinator FIRST; specialists receive only adopted, assignment-relevant content within a character budget.
- **Revision**: target outcomes narrow, revise, or suspend a recommendation; matched trials assess transfer via performance AND research cost. This recursion improves the research STRATEGY (which experiments to run and when), not just interaction memory.

## Four Research Settings
- **A. EEG General Analysis**: question + recordings → evidence-supported answer (exercises analytical reasoning).
- **B. Cross-task Model Optimization**: ONE pretrained encoder adapted across heterogeneous datasets via task-specific adapters; revise task sampling and loss contributions under coupled classification+regression objectives.
- **C. Single-task Open Research**: refine a strong candidate OR switch model family based on evidence (pretrained ↔ task-specific predictors).
- **D. Collaborative Prediction**: examine aligned errors/residuals for complementarity; develop ŷ = Fω({fm(x)}, z(x)) combination or routing; may train additional members.

## Ablation-Verified Mechanisms (fixed CBraMod + DeepSeek)
| Ablation | Effect |
|---|---|
| w/o EEG diagnostics (basic stats only) | −21.14 BA on ADFTD (62.94→41.80) |
| w/o code editing (registered recipes only) | −11.51 BA on Workload (77.73→66.22) |
| w/o specialist personas (single persona) | −1.65 Workload / −4.69 BCIC / −1.65 ADFTD |
| w/o runtime skills | −7.13 Workload, −13.99 ADFTD |
| w/o auxiliary metrics (primary score only) | −6.60 BCIC-IV-2a (56.34→49.74) |
Ordering: EEG diagnostics > code editing > runtime skills ≈ auxiliary metrics > personas. Feeding the agent macro-F1/AUROC/loss/gradient info (not just the headline score) is itself a mechanism.

## Reusable Patterns
1. Diagnose with all four evidence types BEFORE intervening; pick the analysis whose outcomes discriminate hypotheses.
2. Store experience as conditional recommendations with counterevidence and reassessment triggers — not free-form lessons.
3. Adoption gate: Coordinator sees candidate advice summaries first; only adopted, assignment-relevant slices reach specialists (token budget).
4. Feedback redirects: early overfitting → amplitude-scaled training perturbations (+5.64 BA); failed LR change → investigate class imbalance → class-weighted objective (+6.45 val BA). Dead-end results still narrow the hypothesis space.
5. Experience focuses the next experiment but the target side refines HOW to test it (Coordinator requests narrowed comparisons isolating the recommended change from recipe changes).
6. Model pools for combination: BENDR, BIOT, LaBraM, EEGPT, CBraMod, CSBrain, REVE (+ShallowFBCSPNet for small-cohort clinical data).

## Scope Notes
Evaluated on HBN, Workload, PhysioMI, BCIC-IV-2a, ADFTD, HMC with protected test labels unavailable during research. Clinical use would need independent validation under demographic/recording shifts. Baselines adapted to identical task interfaces for fair comparison (CodeAct, BrainPilot, BrainAgent).
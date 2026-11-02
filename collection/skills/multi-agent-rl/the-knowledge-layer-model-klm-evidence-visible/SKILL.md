---
name: the-knowledge-layer-model-klm-evidence-visible
description: "The Knowledge Layer Model (KLM): Evidence-Visible ..."
tags: [cs.AI, cs.CL]
source: arxiv
arxiv_id: 2610.42066v1
utility: 0.88
published: 2026-10-30
---

# The Knowledge Layer Model (KLM): Evidence-Visible AI Output, Routing Diagnostics, and Negative Results

**Authors:** Omer Asim Ozturk, Cihan Aydiner
**Published:** 2026-10-30
**arXiv:** [2610.42066v1](https://arxiv.org/abs/2610.42066v1)
**Categories:** cs.AI, cs.CL
**Utility Score:** 0.88

## Abstract

AI answers require more than apparent correctness: reviewers need to inspect their recorded basis. We introduce the Knowledge Layer Model (KLM), an open, implementation-neutral specification for inference records with versioned epistemic assessments, evidence relations, and explicit unknowns. SEDIM, the knowledge and evidence architecture of Nage AI OS, is a reference implementation. We reference KLM v0.3 (repository tag v0.3.0). Empirical material consists of separate internal experiments, not end-to-end validation. A historical platform-domain routing benchmark reports 137/150 classifications across 15 classes (91.3%; nominal 95% Wilson interval 85.7-94.9%); the numerator is recovered from a rounded summary, and historical example membership is unverified. A native-model weight-path configuration yielded 0/15 successful answers in a corrected two-source test. A capacity-growth comparison could not establish a reliable effect because of a defective legacy scorer and missing original outputs. Lexical and scoped diagnostics each yielded AUC 0.008 for silent-versus-contradicted examples, below the registered minimum of 0.65. Legacy packing lost gold-containing text in 118/221 selected cases; repaired packing retained it in 221/221. These measure text presence, not answer quality. Python and TypeScript verifiers reportedly agreed on six checks per synthetic fixture; a separate production disclosure was not accepted. Restoration, re-derivation, human-rubric support, boundary isol

## Key Contributions

- Novel research in cs.AI, cs.CL
- Published 2026-10-30

## Activation

knowledge, layer, model, evidencevisible, output, routing, diagnostics, negative, results

---
name: radiology-guideline-derived-decision-graph-for-efficient
description: "Radiology Guideline-derived Decision Graph for Eff..."
tags: [cs.CV, cs.AI]
source: arxiv
arxiv_id: 2610.40327v1
utility: 0.91
published: 2026-10-29
---

# Radiology Guideline-derived Decision Graph for Efficient Clinical Decision Support

**Authors:** Xuewen Zhou, Zhen Chen
**Published:** 2026-10-29
**arXiv:** [2610.40327v1](https://arxiv.org/abs/2610.40327v1)
**Categories:** cs.CV, cs.AI
**Utility Score:** 0.91

## Abstract

Radiological risk stratification and management planning are essential downstream tasks in medical imaging. Automating these tasks is challenging because clinical guideline criteria are distributed across prose, tables, and cross-referenced definitions. We present Guideline-derived Decision Graph (GDGraph), a framework that decouples guideline compilation from case evaluation. During compilation, a large language model partitions guidelines into section-based chunks, extracts local decision subgraphs with linked definitions, and aggregates related branches into an executable decision graph. During inference, a fast System One model answers localized clinical questions while deterministic traversal resolves Boolean logic, turning opaque single-pass predictions into a traceable decision path without task-specific training. Across 347 cases spanning renal cyst, adnexal mass, and thyroid nodule guidelines, GDGraph improves System One accuracy from 57.3% to 90.8%, outperforming retrieval-augmented GPT-4o (80.1%) and graph-guided GPT-4o with chain-of-thought (82.7%) at substantially lower latency and cost. The source code will be available.

## Key Contributions

- Novel research in cs.CV, cs.AI
- Published 2026-10-29

## Activation

radiology, guidelinederived, decision, graph, efficient, clinical, decision, support

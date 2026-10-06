---
name: aligning-multimodal-patient-evidence-with-biomedical
description: "Aligning Multimodal Patient Evidence with Biomedic..."
tags: [cs.LG, cs.CL]
source: arxiv
arxiv_id: 2610.06685v1
utility: 1.0
published: 2026-10-05
---

# Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs

**Authors:** Jiawen Du, Arshan Ali Khan, Chenhao Zhang, Zachary Plotkin, Li Shen...
**Published:** 2026-10-05
**arXiv:** [2610.06685v1](https://arxiv.org/abs/2610.06685v1)
**Categories:** cs.LG, cs.CL
**Utility Score:** 1.0

## Abstract

Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their evidence sources nor removed to measure their contributions. We present MM-KG (Multimodal Knowledge Graph), which represents heterogeneous, multimodal patient observations and biomedical concepts as separate layers in one typed graph, joined by explicit alignment edges. First, modality-specific harmonizers convert EHR text, imaging, genomic, and biospecimen data into typed observations mapped to UMLS concepts, which a route-prioritized aligner links to a biomedical knowledge graph. Query-conditioned retrieval then selects a compact subgraph for downstream use by a large language model or a graph neural network. We build MM-KGs for MIMIC-IV and ADNI, and evaluate them with a 2x2 design that separates patient evidence, biomedical knowledge, and their interaction. On questions that require both sources, neither source alone performs far above chance, whereas their combination yields a drug-controlled AUROC interaction of +0.194 on MIMIC and +0.299 on ADNI. On held-out five-candidate ranking, MM-KG outperforms MindMap by +0.131 Hits@1 and leads an adapted GraphCare on the items that require consulting the patient, and deleting the single answer-bearing relation from the retrieved packet returns Hits@1 to the no-knowledge baseline. Finally, query-conditioned retrie

## Key Contributions

- Novel research in cs.LG, cs.CL
- Published 2026-10-05

## Activation

aligning, multimodal, patient, evidence, biomedical, knowledge, graphs, clinical, llms

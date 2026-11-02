---
name: peeling-the-matryoshka-extracting-ontological-structure
description: "Peeling the Matryoshka: Extracting Ontological Str..."
tags: [cs.CL, cs.IR, cs.LG]
source: arxiv
arxiv_id: 2610.41785v1
utility: 0.89
published: 2026-10-30
---

# Peeling the Matryoshka: Extracting Ontological Structure from Retrieval Embeddings

**Authors:** Eunchan Kim, Inwhee Joe
**Published:** 2026-10-30
**arXiv:** [2610.41785v1](https://arxiv.org/abs/2610.41785v1)
**Categories:** cs.CL, cs.IR, cs.LG
**Utility Score:** 0.89

## Abstract

Taxonomy construction is essential for knowledge-intensive NLP yet remains costly: clustering-based methods (i) need careful per-corpus tuning and yield unstable hierarchies, while LLM-based pipelines (ii) depend on expensive task-specific training that does not transfer across domains. We report an empirical finding that bears on both: in Matryoshka Representation Learning (MRL) embeddings, where each leading prefix is itself a usable, coarser vector, prefix length aligns with the coarse-to-fine granularity of gold taxonomies; shuffled- and reverse-dimension controls isolate the alignment to the learned early prefix dimensions. The pattern holds across three architecturally distinct MRL models. To test whether this regularity is usable, we introduce PEEL (Peeling Embeddings to Extract Latent ontologies): a minimal probe over these frozen embeddings, trained once with an order-embedding objective that represents hierarchy as vector containment; a minimum spanning arborescence then decodes taxonomic DAGs. Using only a concept vocabulary (no documents), PEEL recovers taxonomic DAGs with high structural fidelity on two OLLM benchmarks, transferring to a new domain with no target-edge supervision. The end-to-end OLLM pipeline, which jointly discovers concepts and induces structure from document corpora, is reported as a cross-task reference. Pre-trained retrieval embeddings encode a decodable granularity gradient; a minimal probe renders it as explicit parent-child (is-a) structu

## Key Contributions

- Novel research in cs.CL, cs.IR
- Published 2026-10-30

## Activation

peeling, matryoshka, extracting, ontological, structure, retrieval, embeddings

---
name: circuitatlas-agentic-kg-target-discovery
description: "Circuit-first agentic knowledge-graph drug target discovery."
category: ai_collection
---

# CircuitATLAS: Agentic Reasoning over a Systems-Neuroscience Knowledge Graph for Target Discovery in Circuitopathies

**Source**: arXiv:2610.09643 (Ocana-Santero & Tvrdic, Exin Therapeutics, 7 Oct 2026)

## Core Thesis

Drug discovery for neurological disease traditionally starts from molecules altered by disease. But the molecule causing pathology is not necessarily the best intervention point. CircuitATLAS reframes target discovery: **which otherwise-unaltered molecular control points can restore pathological neural circuits toward functional states?** Diseases are treated as *circuitopathies* — phenotypes emerge from maladaptive circuit dynamics, and different molecular perturbations converge on similar circuit-level dysfunction, so targets shared circuit nodes can work despite genetic heterogeneity.

## 1. Knowledge Graph Construction

- **Scale**: 3,831,997 nodes / 7,659,618 edges (5.31M LLM-extracted + 2.35M canonical); 23 node types, 105 relation types.
- **Node vocabulary**: genes (NCBI), transcripts (Ensembl), proteins (UniProt), pathways (Reactome), brain regions + cell types (Allen Brain Atlas), phenotypes (HPO), plus purpose-built lists for poorly-standardized concepts (circuits, circuit motifs, brain states, cellular/circuit electrophysiology features). Every node: canonical name + synonyms + node class + internal ID, retaining external DB IDs.
- **Deterministic candidate generation** (LLM NOT used for extraction): 1,701-term neuroscience lexicon screens PubMed/PMC/Europe PMC/bioRxiv/medRxiv/arXiv → 15.9M papers → 8 topic-stratified subcorpora → co-mention within 400-char window → 57.7M candidate edges with supporting passages.
- **LLM as semantic verifier only**: Nova 2 Lite classifies each candidate edge as supported/unsupported/uncertain with confidence + supporting quotation; Haiku 4.5 as second pass; Opus 5 audit found 17.8% disagreement → second verification placed at inference-time on edges a reasoning chain depends on.
- **Every edge stores**: supporting quotation, source doc, year, canonical IDs, model verdict, confidence, extraction metadata → auditable provenance.

## 2. Anti-Shortcut Design (the key trick)

**Direct disease→gene and disease→protein edges are deliberately EXCLUDED from the discovery graph.** This prevents target discovery from collapsing onto familiar disease-associated molecules. Candidates must be reached through evidence that they act on relevant cell types, circuits, or activity phenotypes. During molecular-agent reasoning, disease-molecule associations are additionally **masked**.

## 3. Three Evidence Layers (all as typed edges on canonical nodes)

1. **Literature**: interpreted findings from papers (bias: publication bias, negative results missing).
2. **Public molecular atlases**: Human Cell Atlas brain → 108 region nodes, 24 cell-type nodes, ~129,234 new edges: `EXPRESSES` (region→receptor, cell-type→receptor) with quantitative metadata (fraction expressing, mean expression, specificity, n cells, receptor family) + `HAS_CELL_TYPE`. Answers "which effectors are physically available in the relevant human biological context".
3. **In-house multimodal in vivo data**: EEG, intracranial ephys, markerless pose (DeepLabCut), fiber photometry, histology, transcriptomics → edges like `SHOWS` / `RECAPITULATES` linking disease models to quantitative phenotypes with direction, statistics (P, Hedges' g), assay, cohort, provenance. E.g., Fmr1 KO → +gamma power (g=1.17); 6-OHDA → −33% locomotor speed; 4-AP → gamma 10.2%→18.6%.

## 4. Evidence-Gated Agentic Workflow

Modeled on a translational systems-neuroscience lab:
- **PI agent**: converts disease+modality brief into search sequence, applies gates, re-triggers stages.
- **Circuit agent**: identifies disease-relevant activity phenotypes + anatomical/cellular substrates.
- **Gate**: sourced, directionally coherent evidence required.
- **Molecular agent**: searches effectors that shift the phenotype, with disease-molecule edges masked.
- **Modality agent**: feasibility (intervention, vector, promoter, campaign constraints).
- **Clinical agent**: trials, biomarkers, safety, translatability.
- **Adversarial sceptic**: independently challenges each stage.
- **Three memory layers**: read-only semantic KG + episodic campaign graph (written by PI agent) + compacted working transcript.
- **Output**: ranked target dossiers with evidence, assumptions, uncertainties, validation route; failing dossiers rejected or returned for search.

## 5. Human-Governed Lab-in-the-Loop

- Laboratory as machine-readable resource via **MCP server**: 81 SOPs exposed as 25 tools + 20 resources (operator competence, equipment state, colony, consumables, capacity, cost).
- Experiment-design agent evaluates proposed experiments on statistical power, expected information gain, **3Rs compliance**, feasibility → human approval required.
- Missing assays return as **capability requests**.
- Results fed back as typed edges → graph updates → next reasoning round.

## 6. Validation Case: ATP1A3 in Epilepsy

1. Workflow nominates ATP1A3 (neuronal α3 Na⁺/K⁺-ATPase): pump turnover exports net positive charge, recruited by firing-induced Na⁺ load → activity-dependent hyperpolarizing current. Neuron-restricted, GABAergic-enriched; LOF epileptogenic, inhibition convulsant → direction = **potentiation**.
2. In vivo test: AAV9.mDlx.ATP1A3 interneuron-specific expression; focal 4-AP challenge. Result: within-animal fold change 11.16→1.33 (beta), 9.73→1.19 (low gamma), 7.81→1.02 (high gamma), q=0.0087, Cliff's δ=−1.0; delta/theta/alpha unchanged.
3. Structure-guided campaign: 5 α3 cryo-EM structures, 203 sub-pockets, docking+generation+retrosynthesis+ADMET; cardiotonic steroid pocket excluded as **anti-target**. 250 binders, 74 with synthetic route, 50 orderable.
4. Key uncertainty exposed: docking predicts binding, **not polarity** → next experiment defined: thallium-flux polarity screen on α3 with α1/α2 in parallel on ouabain-resistant background at sub-maximal Na⁺ load.

Other nominations: partial SLC17A6/VGLUT2 knockdown in thalamic relay neurons (Fragile X thalamocortical hyperexcitability); partial somatodendritic HTR1A autoreceptor suppression in dorsal raphe (Dravet — releasing 5-HT neurons from autoinhibition, fenfluramine precedent).

## Reusable Methodology Patterns

- **Circuit-first reframing**: start from measurable pathological phenotype (oscillation, excitability, behavior), not from disease-altered molecules; search for *control points* regardless of disease association.
- **Edge-exclusion anti-shortcut**: remove the most-familiar direct associations (disease→gene) from the reasoning graph so the agent must build multi-hop mechanistic paths.
- **Deterministic narrowing + LLM verification**: never let the LLM free-extract; co-occurrence windows generate candidates, LLM only verifies with quotation + confidence.
- **Quantitative edges**: ingest datasets as typed edges carrying effect size, statistics, cohort, direction — not as disconnected files.
- **Inference-time re-verification**: re-check only the few edges a candidate chain depends on during traversal (cheap, targets the 17.8% error rate).
- **Adversarial sceptic agent** + evidence gates at each stage = falsifiable, inspectable hypotheses.
- **MCP lab integration**: SOPs as tools; power/info-gain/3Rs gates before human approval; capability requests for missing assays.
- **Uncertainty-driven experiment selection**: advance a hypothesis until its key uncertainty becomes experimentally resolvable; that experiment defines the next step.

## Contrast with Related Systems

SPOKE / TxGNN / PROTON organize biomedical relationships around molecular disease associations; ROBIN couples literature reasoning to experiments. CircuitATLAS differs by making electrophysiology, circuits, regions, cell populations **explicit intermediate reasoning objects** rather than contextual annotations, and by masking disease-molecule edges during target generation.

## Activation

circuitopathies, target discovery, systems neuroscience knowledge graph, agentic reasoning, drug discovery, evidence-gated workflow, MCP lab-in-the-loop, ATP1A3, anti-shortcut graph design, LLM relation extraction with verification, Human Cell Atlas integration, phenotype-to-circuit reasoning

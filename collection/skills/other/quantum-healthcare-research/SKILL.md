---
name: quantum-healthcare-research
description: >
  Research methodology for quantum computing applications in healthcare and medicine
  using knowledge graph analysis. Covers: (1) searching kg.db for quantum+medical papers
  via vector similarity and keyword search, (2) PageRank-based importance ranking of
  research papers, (3) Louvain community detection for identifying research clusters,
  (4) extracting hybrid quantum-classical patterns for disease classification, drug
  discovery, and medical imaging. Use when researching quantum healthcare topics through
  the knowledge graph, analyzing quantum ML medical papers, or identifying research
  trends in quantum biomedical computing. Triggers: quantum healthcare research,
  quantum medical paper analysis, knowledge graph quantum medicine, 量子医疗研究,
  知识图谱量子医学, quantum healthcare survey.
---

# Quantum Healthcare Research

Research methodology using knowledge graph analysis for quantum computing in healthcare.

## Knowledge Graph Workflow

### Step 1: Search kg.db for Relevant Papers
```python
# Vector similarity search
scripts/kg_tool/target/release/kg_tool search --query "quantum healthcare" --limit 10

# SQL-based keyword search (fallback)
SELECT id, title, category FROM kg_entities
WHERE (title LIKE '%quantum%') AND (title LIKE '%medical%' OR content LIKE '%healthcare%')
```

### Step 2: Rank by PageRank
```bash
scripts/kg_tool/target/release/kg_tool pagerank --limit 20
```
High-impact papers in quantum healthcare domain:
- Entity 173: "Quantum computing and artificial intelligence: status and perspectives" (PR=0.014)
- Entity 193: "Quantum Circuit-Based Learning Models Bridging Quantum Computing and ML"

### Step 3: Community Detection
```bash
scripts/kg_tool/target/release/kg_tool communities --limit 20
```
KG stats (as of 2026-05-14): 125 entities, 126 relationships, 23 vectors, 5 skills tracked, 20 Louvain communities.
Main quantum community (Community 2): 31 papers covering QML, quantum neural networks, QKAN.
Neuroscience-AI bridge community (Community 3): 9 papers (ZenBrain, NeuroAI).
See `references/quantum-biology-simulation-milestone.md` for the IBM 12,635-atom protein simulation milestone details.

### Step 4: Import New Papers
```bash
scripts/kg_tool/target/release/kg_tool import-paper \
  --title "Paper Title" \
  --url "https://arxiv.org/abs/XXXX.XXXXX" \
  --abstract "Paper abstract text" \
  --authors "Author names"
```

## Key Research Domains

### Disease Classification (QNN/QSVM)
- QNN and QSVM for cancer, diabetes, heart failure detection
- Quantum models handle imbalanced datasets better than classical
- Hybrid quantum-classical pipelines: PCA → quantum encoding → classification

### Drug Discovery (VQE Pipeline)
- VQE for molecular property prediction
- Active space selection critical for accuracy on drug-like molecules
- Quantum chemistry calculations intractable for classical computers

### Medical Image Processing
- Fourier-based quantum image encoding and compression
- HQNN for breast cancer thermographic classification
- X-ray fracture diagnosis via hybrid quantum-classical pipeline

### Privacy-Aware Federated Learning
- Tensor-network frontends with MPC-secure aggregation
- Federated medical image classification without sharing patient data

## Paper Import Templates

### Medical Diagnosis Paper
```
title: "Disease Detection Using [Quantum Method]"
category: "quant-ph, cs.LG"
key_pattern: "Classical preprocessing → Quantum encoding → QNN/QSVM classification"
metrics: "Accuracy, AUC-ROC, F1 on imbalanced datasets"
```

### Drug Discovery Paper
```
title: "Quantum [Method] for Drug [Task]"
category: "quant-ph, cs.AI"
key_pattern: "Molecular encoding → VQE ansatz → Energy minimization → Property prediction"
metrics: "RMSE, MAE for binding affinity, toxicity prediction"
```

### Medical Imaging Paper
```
title: "Quantum [Method] for [Modality] Analysis"
category: "quant-ph, cs.CV"
key_pattern: "Image patches → Quantum feature extraction → Classical classification"
metrics: "Classification accuracy, sensitivity, specificity"
```

### Emerging Patterns (Updated 2026-05-14)

### Federated Quantum Diagnosis (FQNN)
- arXiv:2605.08324: FQPDR — Multi-hospital federated QNN for diabetic retinopathy
- Pattern: angle embedding → PQC → local training → FedAvg aggregation
- Privacy guarantee: data stays local, quantum measurement adds noise barrier
- Pitfall: Non-IID convergence needs personalization; barren plateaus need shallow circuits

### Quantum PK/PD Simulation
- arXiv:2605.09691: Classical ODE drug models → open quantum systems via VQE/QAOA
- Pattern: C(t) → |ψ(t)⟩, rate constants → Hamiltonian, elimination → Lindblad terms
- Enables exponential state space and parallel dosing scenario evaluation
- See `references/quantum-drug-simulation.md` in `quantum-medical-diagnosis` skill for details

### Quantum Biology Simulation Milestone
- **IBM 12,635-atom protein** (2026-05-05): Largest known biological molecule on quantum hardware
- 94 qubits, ~6,000 quantum operations, Cleveland Clinic + RIKEN + IBM
- Pattern: Molecular Hamiltonian → Quantum encoding → VQE/QPE → Classical reassembly
- Signal: Quantum computing maturing from theoretical to practical biological simulation

### QML Clinical Advantage Verification Protocol
From systematic review of QML for digital health:
1. Define clinical task and dataset
2. Establish classical ML baseline
3. Design equivalent QML model
4. Compare on identical data
5. Statistical significance testing for quantum advantage
6. Analyze NISQ hardware limitations

### Quantum Clinical Trial Design
- Entity 280: "Towards quantum computing for clinical trial design and optimization"
- New domain: Using quantum optimization for patient stratification, trial protocol design
- Combines quantum optimization with clinical research methodology

## Related Skills

- `quantum-healthcare-foundation-models` — quantum foundation models for drug discovery, medical imaging, clinical AI (FeNNx-Bio1, HPQC architecture)
- `hybrid-quantum-medical-classification` — hybrid quantum-classical architectures for medical image classification
- `quantum-drug-discovery` — quantum methods for drug discovery
- `quantum-medical-imaging` — quantum medical imaging analysis
- `quantum-eeg-foundation` — quantum-enhanced EEG signal analysis

**Scope note**: This skill covers the *research methodology* — searching, importing, ranking, and analyzing quantum+medical papers via the knowledge graph. For quantum model architectures and implementation patterns, see the related skills above.

## Limitations

- arxiv API rate-limited (429 errors) — use web_search as fallback
- Vector search may return empty for niche topics — fall back to SQL LIKE
- NISQ hardware limits quantum circuit depth in practical applications
- Most papers are preliminary — clinical validation rarely present
- **QML advantage not yet empirically proven** for most healthcare tasks (2026-05-06 systematic review)

## References

- `references/quantum-biology-simulation-milestone.md` — IBM 12,635-atom protein simulation details, hybrid pattern extraction, and comparison with prior art (captured 2026-05-06)

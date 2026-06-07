# Medical + Quantum RSS Feeds

## Verified Feed Combinations

### 2026-06-03 - Broad Medicine + Quantum Discovery (CONFIRMED, updated)

**Feed**: `quant-ph+q-bio.QM+q-bio.TO+cs.AI+cs.LG`
- **Total items**: ~10,899 lines (varies per fetch)
- **Medicine+Quantum overlap**: 67 papers (2026-06-03 confirmed with broad keyword filter)
- **Yield rate**: ~2-8% depending on keyword strictness
- **Status**: CONFIRMED working

This broader feed (adding cs.AI+cs.LG) catches QNN clinical applications, quantum ML for diagnosis, and AI-driven medical imaging that narrower quant-ph-only feeds miss.

**Top papers discovered (2026-06-03)**:
- 2606.03517: Scalable On-Hardware Training of QNNs for Clinical Data Imputation → [[scalable-on-hardware-qnn-training]]
- 2606.02662: Adaptive On-The-Fly Multifidelity ML for Quantum Chemistry → [[adaptive-multifidelity-quantum-ml]] (new, 30x cost reduction)
- 2606.02104: Penalty-free quantum optimization applied to lattice protein folding → [[penalty-free-quantum-protein-folding]]
- 2606.03914: Quantum Erasure Imaging → [[quantum-erasure-imaging]]
- 2606.03232: GFFMERGE: Efficient Merging of Graph Neural Force Fields → [[gffmerge-model-merging-gnns]]
- 2606.00818: Retinomorphic Optical Spiking Neuron (physics.app-ph, quant-ph)
- 2606.01110: Accelerating PINNs using hybrid quantum-classical FBPINN

**Pattern note**: After multiple cron runs, the med+quantum intersection consistently shows 2-8% yield from broad feeds. Most discovered papers already have existing skills — this is expected for mature research areas. New discoveries tend to be in emerging intersections (e.g., quantum + clinical data, quantum + protein folding, adaptive multifidelity ML for quantum chemistry).

### 2026-05-27 - Narrower Feed

**Feed**: `quant-ph+q-bio.QM+q-bio.TO`
- ~207 items, ~10 after keyword filtering
- Higher precision but lower recall for quantum-biology intersection

### 2026-05-27 - Original Pattern

**Feed**: `quant-ph+q-bio`
- Returns thousands of entries but keyword-filtering for medical+quantum intersection frequently yields 0 results
- Expected for niche cross-domain topics — intersection is sparse on any given day

## Keyword Filter Sets

### Medical Keywords (title + abstract)
medical, healthcare, clinical, diagnosis, treatment, patient, disease, therapy, drug, protein, imaging, biomarker, cancer, hospital, medicine, pharma, molecular, genomic, genome, dna, rna, bioimaging, bioinformatics, biomedical, health

### Quantum Keywords (title + abstract)
quantum, qubit, qaoa, vqe, entanglement, superposition, quantum neural, quantum machine, quantum computing, quantum algorithm, quantum chemistry, quantum simulation

## Recommended Strategy

1. **Start broad**: `quant-ph+q-bio.QM+q-bio.TO+cs.AI+cs.LG` for maximum coverage
2. **Keyword filter**: Search title+abstract for medical terms AND quantum terms
3. **Narrow if needed**: `quant-ph+q-bio.QM+q-bio.TO` for focused quantum-biology only
4. **Fallback**: If 0 results, the intersection is simply sparse — not a feed failure
5. **Skill overlap check**: Most med+quantum papers already have skills. Use grep-based duplicate check before creating new skills.

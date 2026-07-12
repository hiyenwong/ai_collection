# Medical + Quantum RSS Feeds

## Verified Feed Combinations

### `quant-ph+q-bio.QM+q-bio.TO` → ~207 items
- **quant-ph**: Quantum physics (broad coverage)
- **q-bio.QM**: Quantitative Methods in biology
- **q-bio.TO**: Tissues and Organs

### `quant-ph+cs.LG+q-bio` → ~1000+ items (2026-06-03 Confirmed)
- Broader cross-domain feed combining quantum + ML + all biology subcategories
- Captures medical+quantum+ML intersection papers
- Keyword filtering (score ≥4) yielded 149 relevant papers from ~1000+
- More comprehensive than narrow q-bio subcategory feeds
- Best used as a **broad sweep** to complement the narrow `quant-ph+q-bio.QM+q-bio.TO` feed

### Medical Keyword Filter
From `quant-ph+q-bio.QM+q-bio.TO` (207 items), keyword scoring (threshold ≥3) yielded 10 papers.
From `quant-ph+cs.LG+q-bio` (~1000+ items), combined medical+quantum keyword scoring (threshold ≥4) yielded 149 papers.

**Medical keywords**: medical, health, clinical, diagnos, treatment, cancer, tumor, disease, patient, therapy, biomarker, drug, pharma, hospital, imaging, surgery, retin, protein, molecule, genetic, rna, dna, bio

**Quantum keywords**: quantum, qubit, qnn, qml, qaoa, vqe, hamiltonian, entangle, superposition, hilbert, quantiz

**Scoring**: title match = 2 (medical) / 3 (quantum), abstract match = 1 each. Threshold ≥3 for narrow feed, ≥4 for broad feed.

### Key Papers Discovered (2026-06-03)
- **2606.01051**: Interaction-Limited Safe Continuous-Time RL for Dynamical Medical Treatment
- **2606.01028**: MedGym: A Unified Continuous-Time Benchmark for Dynamic Medical Treatment RL
- **2606.02104**: Penalty-free quantum optimization applied to lattice protein folding
- **2606.01611**: Peptide Structure Prediction Using CD-QAOA
- **2606.00818**: Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
- **2503.22939**: Interpretable Graph KANs for Multi-Cancer Classification

### Discovery Strategy
Use **dual-feed approach**:
1. Narrow feed (`quant-ph+q-bio.QM+q-bio.TO`) → high precision, fewer results
2. Broad feed (`quant-ph+cs.LG+q-bio`) → high recall, more results, needs stronger keyword filtering
3. Combine deduplicated results for comprehensive coverage

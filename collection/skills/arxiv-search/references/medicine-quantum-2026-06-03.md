# 2026-06-03 Wednesday Medicine + Quantum Discovery

## RSS Discovery Summary
- **Feed**: `quant-ph+q-bio.QM+q-bio.TO+cs.AI+cs.LG` → 10,899 lines, **67 med+quantum papers**
- **Filter**: Broad keyword sets (30+ medical terms, 15+ quantum terms)
- **New paper**: 2606.02662 (adaptive-MFML for quantum chemistry)
- **Already-skilled papers**: 2606.03517, 2606.03914, 2606.02104, 2606.03232

## Keyword Filter Sets Used

### Medical (30 terms)
medical, healthcare, clinical, diagnosis, treatment, patient, disease, therapy, drug, protein, imaging, biomarker, cancer, hospital, medicine, pharma, molecular, genomic, genome, dna, rna, bioimaging, bioinformatics, biomedical, health, neural, brain, neuro, EEG, fMRI, signal, classification, segmentation, anomaly detection

### Quantum (15 terms)
quantum, qubit, qaoa, vqe, entanglement, superposition, quantum neural, quantum machine, quantum computing, quantum algorithm, quantum chemistry, quantum simulation, quantum circuit, quantum error, quantum state, qnn, vqc

## Discovery Pattern
- Most med+quantum papers from RSS are already skilled (expected for mature intersection)
- New skills tend to emerge from emerging sub-intersections
- Broad keyword filters yield 2-8% overlap from feeds with 800-1000+ items

## Paper 2606.02662 - Adaptive MFML Full Abstract
"Machine learning has accelerated quantum chemistry but is hindered by the prohibitive cost of generating high fidelity training data. Multifidelity machine learning (MFML) mitigates this overhead by systematically combining abundant low fidelity data with sparse high fidelity data. In spite of its success, standard MFML schemes rely on pre-defined scaling factors to determine sparse data ratio across fidelities, often generating redundant multifidelity data resulting in a loss of efficiency. Here, we introduce an adaptive on-the-fly multifidelity framework for machine learning that autonomously determines training dataset composition. By dynamically querying training samples at each fidelity, the algorithm saturates model accuracy at lower fidelities before moving up to more expensive reference calculations. We benchmark the novel adaptive-MFML across diverse chemical properties including the computational chemistry gold standard coupled cluster energies, and the more chemically challenging excitation energies. In our numerical experiments we show that our adaptive algorithm reduces data generation costs by up to a factor of 30 compared to single fidelity methods and improves upon standard MFML by up to a factor of 5. The mitigation of data redundancy establishes a high-accuracy low-cost pathway for sustainable cost-aware machine learning in quantum chemistry."

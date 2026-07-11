# Medicine + Quantum Dual-Keyword Scoring (Verified 2026-06-10)

## Keyword Sets

### Medicine/Healthcare keywords (26 terms)
medical, healthcare, clinical, diagnosis, treatment, patient, drug, protein, gene, cancer, tumor, imaging, mri, ct, molecular, therapy, disease, biomarker, pharma, hospital, surgical, pathology, histology, radiology, surgery, medicine

### Quantum keywords (20 terms)
quantum, qubit, qaoa, vqe, entanglement, hamiltonian, gate, fidelity, decoherence, quantum neural, quantum machine, quantum computing, quantum algorithm, quantum chemistry, quantum simulation, qec, quantum error, density matrix, wavefunction, measurement

## arXiv API Query Pattern (Verified Working 2026-06-10)
Use `all:X+AND+all:Y` syntax with urllib + proxy:
```python
queries = [
    'all:quantum+AND+all:machine+AND+all:learning+AND+all:medical',
    'all:quantum+AND+all:healthcare',
    'all:quantum+AND+all:diagnosis',
    'all:quantum+AND+all:clinical',
    'all:quantum+AND+all:drug',
    'all:quantum+AND+all:molecular',
    'all:quantum+AND+all:protein',
    'all:quantum+AND+all:imaging',
    'all:quantum+AND+all:neural+AND+all:network+AND+all:medical',
]
```
**Avoid**: `+OR+` in API queries (causes HTTP 400). Use `+AND+` between terms.

## Verified Yields (2026-06-10)
- 116 unique papers across 9 queries
- Top cross-domain: 2604.13608 (HQNN Chronic Kidney Disease, score 8), 2604.10487 (CovAngelo QM/QM/MM, score 8)
- Domain saturation: HIGH — most Medicine+Quantum papers already have skills
- New skill created: covangelo-hybrid-quantum-drug-discovery

## Medicine+Quantum Research Themes
1. **Hybrid Quantum-Classical Medical Imaging** — breast cancer thermography, blood cell classification, CV-QNN
2. **Quantum Chemistry for Drug Discovery** — CovAngelo QM/QM/MM, 12,000-atom quantum chemistry
3. **Post-Quantum Security in Healthcare** — ML-KEM+ML-DSA pharmacovigilance, QT-PUF IoMT
4. **Clinical Data with QNNs** — MIMIC-III imputation, clinical time series, butterfly circuit gradient estimation

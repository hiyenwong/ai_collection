# Medicine + Quantum Discovery Pattern (Verified 2026-06-10)

## Cross-Domain Signal
"Neural" keyword in quantum papers (neural decoders, GNNs, neural state preparation) is a VALID cross-domain signal with medical/ML relevance — NOT a false positive. Neural+quantum papers are inherently cross-domain.

## Discovery Method
1. browser_navigate to arXiv search: `quantum+machine+learning+medical+OR+healthcare+OR+diagnosis+OR+clinical`
2. Also: `quantum+neural+network+medical+OR+diagnosis+OR+treatment+OR+clinical`
3. Browse quant-ph listing page `/list/quant-ph/recent` for papers with neural/medical keywords

## Medicine Keywords (26 terms)
medical, healthcare, clinical, diagnosis, treatment, patient, drug, protein, gene, cancer, tumor, imaging, mri, ct, molecular, therapy, disease, biomarker, pharma, hospital, surgical, pathology, histology, radiology, surgery, medicine

## Quantum Keywords (28 terms)
quantum, qubit, qaoa, vqe, entanglement, hamiltonian, gate, fidelity, decoherence, quantum neural, quantum machine, quantum computing, quantum algorithm, quantum chemistry, quantum simulation, QEC, quantum error, density matrix, wavefunction, measurement

## Skill Creation Pattern
- Select papers with quantum_score ≥ 1 (quantum methods with medical/chemical/molecular applications)
- Also consider pure-quantum papers with neural network methodology (inherently cross-domain)
- Check skill existence before creation: `search_files(path=~/.hermes/skills, pattern=keyword, target=files)`
- Create skill in ~/.hermes/skills/ai_collection/{name}/
- Copy to ~/ai_github/ai_collection/collection/skills/{name}/
- Update INDEX.md (prepend after heading)
- Git commit on branch: medicine-cron-YYYY-MM-DD
- Import to kg.db arxiv_papers table

## kg.db arxiv_papers Schema (2026-06-10 Verified)
Columns: id TEXT, title TEXT, authors TEXT, published TEXT, categories TEXT, summary TEXT, pdf_url TEXT, abs_url TEXT
NOTE: NO url, NO abstract, NO created_at columns

## Session Results (2026-06-10)
3 skills created: trainability-iqp-born-machines, jacobian-geometry-robustness-qnn, analog-quantum-event-gnn
All 3 papers were new (not previously in kg.db)

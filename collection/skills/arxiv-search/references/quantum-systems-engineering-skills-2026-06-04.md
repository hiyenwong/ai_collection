# Systems Engineering + Quantum Skills — 2026-06-04

## New Skills Created

### 1. quantum-mirror-tomography (arXiv: 2606.04277)
- CV quantum state tomography via quantum mirrors
- Transfers photonic state info onto control atom
- Three methods: kernel functions, direct wavefunction reconstruction, pointwise Wigner function
- Bypasses exponential sample complexity

### 2. photon-heralded-error-characterization (arXiv: 2606.04312)
- Analytic perturbative framework for photon-heralded quantum error analysis
- Extended ZPG framework with closed-form solutions
- Bridges physical imperfections to abstract Pauli noise models
- Full physical stack coverage

### 3. hybrid-quantum-classical-pinn (arXiv: 2606.04679)
- Hybrid quantum-classical PINN for nonlinear PDE solving
- Classical backbone + PQC integration
- Benchmarked on Burgers', Allen-Cahn, KdV equations
- Identifies when quantum hybridization outperforms classical PINN

## Sync Details

- All 3 skills copied to `~/.hermes/skills/ai_collection/{name}/` and `~/ai_github/ai_collection/collection/skills/{name}/`
- INDEX.md updated with entries at top of file
- Git commit: 714c5b0e — "feat: add 3 quantum systems engineering skills (arXiv: 2606.04277, 2606.04312, 2606.04679)"
- Pushed to: https://github.com/hiyenwong/ai_collection.git

## KG Import Details

- 8 papers imported into kg.db
- 4 new kg_entities created (4 already existed)
- All 8 entities have vector embeddings
- Entity IDs: 1993, 1967, 1966, 1998, 1994, 1999, 2000, 2001

## Pitfall: kg_entities ID is INTEGER auto-increment

Cannot insert string IDs (e.g., "arxiv_2606.04277"). Must insert with auto-increment, then track the generated ID separately.
The `arxiv_papers` table uses the arXiv ID string as its primary key — use that for deduplication.
The `kg_entities.url` field has a UNIQUE constraint — use URL to check existence before inserting.

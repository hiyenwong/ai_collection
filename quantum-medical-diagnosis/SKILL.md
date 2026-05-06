---
name: quantum-medical-diagnosis
description: Quantum computing methods for medical diagnosis and healthcare analytics. Covers quantum-enhanced diagnostic systems, QML classifiers, quantum optimization for medical imaging, and quantum-resilient federated medical learning. Use when analyzing quantum approaches to medical diagnosis, clinical decision support, medical AI systems, or quantum healthcare applications.
---

# Quantum Medical Diagnosis

## Quick Reference

| Domain | Key Methods | Applications |
|--------|-------------|--------------|
| Medical Imaging | QUBO optimization, Quantum CNN, EP | PET reconstruction, blood cell analysis |
| Clinical Diagnosis | Quantum classifiers, QNN, QBM | Disease prediction, radiology |
| Drug Discovery | HPQC hybrid, VQE, QSVM | Molecular screening, binding prediction |
| Federated Learning | Lattice-based encryption | Privacy-preserving diagnosis |

## Activation Keywords
- quantum medical diagnosis
- quantum healthcare
- quantum clinical
- QML diagnosis
- quantum radiology
- quantum pathology
- quantum drug discovery

## Analysis Framework

When analyzing a quantum medical diagnosis paper/article, extract:

```yaml
Paper_ID: [arxiv/DOI]
Title: [full title]
Domain: [imaging/diagnosis/drug_discovery/federated]
Quantum_Method:
  - Primary: [VQE/QUBO/QNN/EP/QBM/QSVM/etc]
  - Hybrid: [Yes/No - classical components]
Application:
  - Type: [reconstruction/classification/screening/etc]
  - Medical_area: [radiology/pathology/drug/genomics/etc]
Performance:
  - Metric: [accuracy/F1/AUC/speedup/etc]
  - Value: [quantitative result]
  - Comparison: [vs classical baseline]
Quantum_Advantage: [speedup/accuracy/privacy/scalability/etc]
NISQ_Limitations: [qubit count/circuit depth/error rates/etc]
Validation_Level: [simulation/small_scale/clinical/etc]
Key_Reference: [DOI/arxiv ID]
```

## Key Methods

### 1. Equilibrium Propagation (EP)
- Energy-based learning, no backpropagation
- Quantum-compatible (avoids state collapse)
- Used in: blood cell imaging, medical classification

### 2. QUBO Optimization
- Quadratic Unconstrained Binary Optimization
- Applications: PET image reconstruction, medical tomography
- Advantage: polynomial speedup potential

### 3. Quantum Neural Networks (QNN)
- Variational quantum circuits for classification
- Hybrid quantum-classical training
- Medical: radiology, pathology classification

### 4. HPQC Hybrid Architecture
- High-Performance Quantum Computing
- QPU-GPU hybrid for drug discovery
- ML foundation models (FeNNx-Bio1)

### 5. Quantum Reservoir Computing
- Neutral atom platforms
- Small, complex medical datasets
- Temporal pattern recognition

## Workflow

### Step 1: Domain Identification
Categorize the paper/application:
- **Imaging**: reconstruction, denoising, classification
- **Diagnosis**: disease prediction, clinical decision support
- **Drug Discovery**: molecular screening, binding prediction
- **Federated**: privacy-preserving distributed learning

### Step 2: Method Analysis
Identify quantum method:
- Check if hybrid (quantum-classical)
- Analyze quantum circuit structure
- Identify classical preprocessing/postprocessing

### Step 3: Performance Evaluation
Compare with classical baselines:
- Accuracy metrics
- Computational efficiency
- Scalability potential

### Step 4: Limitation Assessment
NISQ-era constraints:
- Available qubit count
- Circuit depth limitations
- Error rates and mitigation

### Step 5: Clinical Readiness
Validation level:
- Simulation only
- Small-scale pilot
- Clinical validation
- Regulatory pathway

## Resources

### References
- [QUANTUM_IMAGING.md](references/QUANTUM_IMAGING.md) - Medical imaging methods
- [QUANTUM_DRUG.md](references/QUANTUM_DRUG.md) - Drug discovery applications
- [QUANTUM_FEDERATED.md](references/QUANTUM_FEDERATED.md) - Privacy-preserving learning

### Key Papers in kg.db
- arxiv 2601.18710: Equilibrium Propagation for Blood Cell Imaging
- arxiv 2603.17790: HPQC Drug Discovery Hybrid
- Nature npj: Quantum-Machine-Assisted Drug Discovery
- IEEE: QUBO Medical Imaging Optimization

## Related Skills
- `quantum-medical-imaging`: Focus on imaging reconstruction
- `quantum-drug-discovery`: Focus on pharmaceutical applications
- `quantum-neuroscience-analysis`: Brain network quantum methods
- `quantum-federated-healthcare`: Privacy-preserving medical AI

## Notes
- Hybrid quantum-classical is the practical approach
- NISQ limitations require careful method selection
- Clinical validation is still limited
- Drug discovery shows most near-term potential
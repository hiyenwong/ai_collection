---
name: quantum-medical-imaging
description: "Analysis and research synthesis skill for quantum-enhanced medical imaging papers. Use when working with papers on quantum computing for medical image reconstruction (MRI/CT/PET), quantum sensors for diagnostics (NV centers, quantum dots), or quantum algorithms in radiology. Triggers: quantum medical imaging, quantum radiology, quantum MRI, quantum sensors medicine, quantum diagnostics."
---

# Quantum Medical Imaging Analysis

Analyzes and synthesizes research on quantum computing applications in medical imaging and diagnostics.

## Overview

This skill provides structured analysis patterns for papers on quantum-enhanced medical imaging, including image reconstruction algorithms, quantum sensors for diagnostics, and quantum algorithms for radiology applications.

## Core Capabilities

### 1. Paper Analysis Framework

When analyzing quantum medical imaging papers, extract:

| Component | Key Questions |
|-----------|---------------|
| **Quantum Algorithm** | Which quantum algorithm is used? (QFT, VQE, QAOA, quantum annealing) |
| **Medical Application** | What imaging modality? (MRI, CT, PET, ultrasound, radiology) |
| **Performance Metric** | What improvement? (speed, resolution, radiation dose, accuracy) |
| **Quantum Hardware** | What qubit technology? (NV centers, superconducting, trapped ions) |
| **Clinical Felevance** | Is this clinically validated? Preclinical? Simulation? |

### 2. Quantum Algorithm Taxonomy

**Image Reconstruction:**
- Quantum Fourier Transform (QFT) - faster Fourier-based reconstruction
- Variational Quantum Eigensolver (VQE) - optimization for reconstruction parameters
- Quantum Approximate Optimization Algorithm (QAOA) - image quality optimization

**Sensing & Diagnostics:**
- NV-center magnetometry - enhanced MRI sensitivity
- Quantum dots - biosensing at molecular level
- Quantum interferometry - precision measurement

### 3. Performance Benchmarks

Standard metrics to compare:

| Metric | Classical Baseline | Quantum Target | Key Papers |
|--------|-------------------|----------------|------------|
| Reconstruction Time | O(N log N) | O(log N) potential | Martinez & Zhang 2026 |
| MRI Resolution | ~1mm | <0.1mm (NV centers) | Lee et al. 2026 |
| Radiation Dose | Standard CT | 50% reduction | Zhang et al. 2024 |

### 4. Analysis Workflow

```
Paper → Identify Algorithm → Map to Application → Extract Metrics → Compare Benchmarks → Synthesize Insight
```

## Quick Reference

### Paper Extraction Template

```markdown
# Paper: [Title]
- **Algorithm**: [QFT/VQE/QAOA/etc.]
- **Application**: [MRI reconstruction / CT denoising / PET imaging]
- **Performance**: [X% speedup / Y resolution improvement]
- **Hardware**: [NV centers / superconducting qubits]
- **Status**: [Simulation / Preclinical / Clinical validation]
- **Key Insight**: [1-2 sentence takeaway]
```

### Common Patterns

**Pattern 1: Speed vs Quality Tradeoff**
- Quantum reconstruction often trades speed for quality
- Check if paper addresses reconstruction accuracy (RMSE, SSIM)

**Pattern 2: Hardware Limitations**
- Current NISQ devices limit practical implementation
- Note if paper discusses fault tolerance requirements

**Pattern 3: Clinical Readiness**
- Most papers are theoretical/simulation
- Distinguish between validated vs proposed approaches

**Pattern 5: CV Photonic QNNs for Edge Medical AI (2026-06-26)**
- Continuous-variable photonic quantum computing operates at room temperature — no cryogenics needed
- Demonstrated in oral cancer detection using smartphone-based screening pipeline
- Parameter-efficient compared to classical equivalents for same accuracy
- Edge-deployable: suitable for low-resource healthcare settings
- Reference skill: `cv-photonic-qnn-edge-medical`

**Pattern 6: Quantum Ophthalmology (2026-06-17)**
- Four research directions: photon-limited retinal imaging, correlation-based imaging, nanoscale optical probes, quantum-limited visual perception
- OCT advances + single-photon detection enable imaging under strict photon budget constraints
- Reduces phototoxicity while preserving diagnostic image quality
- Reference: arXiv:2606.19238

**Pattern 7: First-in-Human Quantum Entanglement Imaging (2026-06-28)**
- J-PET scanner achieved first in vivo quantum entanglement imaging in human subjects
- Plastic scintillators proved viable for clinical quantum entanglement measurement
- Opens new diagnostic modality leveraging quantum correlations of annihilation photons
- Reference skills: `quantum-entanglement-pet-imaging`

**Pattern 8: Fourier-Based Quantum Image Encoding (2025-05-09, arXiv:2505.06471)**
- Fourier-based quantum image encoding reduces gate count to ≤ N/4 (vs. traditional O(2×N) for N pixels)
- Demonstrated on 1024×1024 medical images from BABA robotic thyroidectomy surgery
- Two compression stages: frequency thresholding + block-based encoding
- Key insight: Medical images have sparse frequency content, enabling aggressive gate reduction with negligible quality loss
- Reference skill: `quantum-image-encoding-compression`

**Pattern 9: Schmidt Decomposition for Efficient Quantum Image Encoding (2026-06-09, arXiv:2606.10874)**
- Low-rank state approximation via Schmidt decomposition reduces circuit depth by 97% while maintaining near-perfect reconstruction (MSE ~0.27)
- Compares FRQI, QPIE, NEQR encoding methods with low-rank approximation
- FRQI achieves best trade-off for medical imaging applications
- Key insight: Keep only significant parts of quantum state's entanglement structure for NISQ-friendly encoding

**Pattern 10: Kurtosis-Difference Weighted Covariance for Quantum Imaging (2026-06-30, arXiv:2606.31005)**
- Fourth-order statistic (kurtosis difference) discriminates correlated photon pairs 40x faster than standard covariance
- Achieves CNR > 7 at 5000 frames vs. CNR < 2 for standard methods
- Automatically identifies correlated pairs without precise correlation center calibration
- Key insight: Weighting covariance by exponential of kurtosis difference selects symmetric pixels while preserving true coincidences
- Enables practical quantum imaging in sparse correlated-photon regimes (relevant for low-dose medical imaging)

**Pattern 11: VQE Active Space Benchmarking for Quantum Drug Discovery (2025-12-20, arXiv:2512.18203)**

**Pattern 12: Quanvolutional Neural Networks for Medical Imaging (2025-10-26, arXiv:2510.23660)**
- Quanvolutional Neural Networks (QNNs) replace classical convolutional layers with parameterized quantum circuits (PQCs) for medical image feature extraction
- 2x2 pixel patches encoded via rotational Y-gates into 4-qubit states, then entangled
- Outperformed classical CNN baseline: 83.33% vs 73.33% on PneumoniaMNIST
- Key advantage: enhanced convergence and sample efficiency, particularly effective with limited labeled data
- Pattern is generalizable beyond pneumonia to any small-resolution medical image classification task
- Reference skill: `quanvolutional-neural-network-medical`

- First systematic benchmark for active space driven VQE in drug discovery (lovastatin, oseltamivir, morphine)
- Active space selection is more critical than ansatz choice for molecular quantum computing success
- Chemically motivated active spaces outperform automated selection
- Comprehensive evaluation: chemistry metrics + architecture-centric metrics + hardware feasibility
- Reference skill: `vqe-active-space-benchmarking`

## Pattern 4: Benchmark Rigor for Quantum Generative Models (2026-06-22)
- **Matched parameter budgets are essential**: Claims of quantum advantage in generative models often use unmatched parameter counts between quantum and classical generators. Always verify parameter budgets match (e.g., 1648 vs 1632 params).
- **Low-data "benefits" are regularization, not data expansion**: When quantum GANs appear to help at low data fractions, the improvement typically comes from regularization effects, not faithful data generation. Synthetic samples are often off-distribution and mode-collapsed.
- **Proper statistical testing required**: Use multiple random seeds (≥8), paired significance testing with multiple-comparison correction (FDR), and evaluate across data fraction spectrum (5%-100%).
- **Testbed protocol**: arXiv:2606.18970 released a controlled benchmark protocol as a testbed for rigorous evaluation of quantum generative augmentation in medical imaging.
- Reference skill: `quantum-lmri-gan-benchmark`

## Scripts

### extract_paper_insights.py

Extracts structured information from quantum medical imaging papers.

```bash
python scripts/extract_paper_insights.py --paper "path/to/paper.pdf" --output insights.json
```

Output includes: algorithm, application, metrics, hardware, status, key_insight.

## References

For detailed quantum computing concepts in medicine:
- `references/quantum_algorithms.md` - algorithm explanations
- `references/medical_imaging.md` - imaging modality background
- `references/nv_centers.md` - NV-center technology for sensing

## Related Skills

- **arxiv-search** - Find quantum medical papers on arXiv
- **neural-dynamics-universal-translator** - Related brain imaging quantum approaches
- **skill-extractor** - Extract patterns from analyzed papers
- **quantum-autoencoder-anomaly-detection** (QAE for brain MRI anomaly detection)
- **quantum-entanglement-pet-imaging** (quantum entanglement PET, 2606.25804 + first-in-human 2606.29421)
- **cv-photonic-qnn-edge-medical** (CV photonic QNN for oral cancer detection, 2606.28252)
- **quantum-ophthalmology** (quantum ophthalmology, 2606.19238)
- **quantum-state-preparation-medical** (quantum state preparation for medical data, 2508.05063)
- **quantum-image-encoding-compression** (Fourier-based quantum medical image encoding, 2505.06471)
- **vqe-active-space-benchmarking** (VQE benchmarking for quantum drug discovery, 2512.18203)
- **quantum-metrology-sensing-review** (quantum metrology and sensing review, 2605.21702)
- **quanvolutional-neural-network-medical** (Quanvolutional NNs for pneumonia detection, 2510.23660)

## Notes

- Quantum medical imaging is rapidly evolving - check recent papers
- Distinguish theoretical claims from validated results
- Clinical adoption timeline is typically 5-10 years from research
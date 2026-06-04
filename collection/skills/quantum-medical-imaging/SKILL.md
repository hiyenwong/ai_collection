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

## Notes

- Quantum medical imaging is rapidly evolving - check recent papers
- Distinguish theoretical claims from validated results
- Clinical adoption timeline is typically 5-10 years from research
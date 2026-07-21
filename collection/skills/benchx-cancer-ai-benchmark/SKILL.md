---
name: benchx-cancer-ai-benchmark
description: "Large-scale AI benchmarking methodology for cancer detection models. Evaluates tumor-detection AI across tumor size, location, demographic subgroups, and imaging protocols using 85,355 CT scans and 12 models. Use when: benchmarking medical AI models, evaluating cancer detection systems, assessing subgroup fairness in healthcare AI, analyzing CT scan AI performance, building robust tumor detection pipelines."
metadata:
  arxiv_id: "2606.24883"
  published: "2026-06-23"
  authors: "BenchX Consortium"
  tags: ["medical-ai", "cancer-detection", "benchmarking", "fairness", "ct-imaging", "subgroup-analysis"]
---

# BenchX: Cancer Detection AI Benchmarking

## Overview

BenchX is a large-scale open benchmark systematically evaluating AI models for cancer detection and localization across 85,355 CT scans. It reveals that SOTA AI models optimized for average accuracy perform poorly in rare or underrepresented subgroups, providing a foundation for building more reliable AI models for tumor detection.

## Core Methodology

### Multi-Dimensional Evaluation Framework

Evaluate AI models across four critical dimensions simultaneously:

1. **Tumor Size**: Micro (<5mm), small (5-10mm), medium (10-30mm), large (>30mm)
2. **Anatomical Location**: Per-organ and per-region analysis
3. **Patient Subgroups**: Age, gender, ethnicity, comorbidity status
4. **Imaging Protocol**: Scanner manufacturer, slice thickness, contrast phase, radiation dose

### LLM-Assisted Subgroup Extraction

Use LLMs to automatically extract and organize subgroup information from unstructured clinical data:
- Parse radiology reports for patient demographics
- Extract imaging protocol metadata from DICOM headers
- Classify tumor characteristics from pathology reports
- Build structured subgroup taxonomy for stratified evaluation

### Bias Detection Protocol

For each model-subgroup combination:
1. Compute detection sensitivity, specificity, and localization accuracy
2. Calculate performance gap relative to overall average
3. Identify subgroups with >15% performance degradation
4. Flag models with systematic bias patterns

## Usage Patterns

### Pattern 1: Cancer Detection Model Evaluation
Benchmark a new cancer detection model against BenchX standards:
1. Run model on standardized CT scan subset
2. Compute per-subgroup metrics using LLM-extracted metadata
3. Generate fairness report highlighting performance gaps
4. Compare against published baselines

### Pattern 2: Subgroup Fairness Audit
Audit an existing AI system for demographic bias:
1. Stratify evaluation dataset by subgroup dimensions
2. Compute detection metrics per stratum
3. Identify statistically significant performance disparities
4. Recommend data augmentation or model reweighting strategies

### Pattern 3: Imaging Protocol Robustness
Test model robustness across imaging protocols:
1. Group scans by protocol parameters (scanner, thickness, contrast)
2. Measure detection accuracy per protocol group
3. Identify protocol-dependent failure modes
4. Suggest protocol-invariant training strategies

## Implementation Guide

### Required Components
- LLM for clinical text extraction and subgroup classification
- CT scan dataset with ground truth tumor annotations
- Detection model producing bounding boxes or segmentation masks
- Statistical analysis toolkit for subgroup comparison

### Evaluation Metrics
- **Detection sensitivity**: TP / (TP + FN) per subgroup
- **Localization accuracy**: IoU > 0.5 threshold per subgroup
- **Performance gap**: max(subgroup_metric) - min(subgroup_metric)
- **Fairness index**: Ratio of worst-performing subgroup to overall average

## Error Handling
- **Missing metadata**: Use LLM to impute from clinical notes when DICOM fields are incomplete
- **Small subgroups**: Apply confidence intervals; flag subgroups with n < 30 as statistically unreliable
- **Protocol heterogeneity**: Normalize across scanner types using phantom-based calibration data

## Activation Keywords
- cancer detection benchmark
- medical AI evaluation
- tumor detection fairness
- CT scan AI benchmark
- subgroup bias medical AI
- BenchX methodology
- 癌症检测基准
- 医学AI公平性评估

## Related Skills
- `medical-ai-diagnosis` — **umbrella skill**: Patterns for building AI-based medical diagnosis systems with clinical explainability. For broader medical AI workflows, load this skill first.
- `hybrid-quantum-medical-imaging` — Quantum-enhanced medical imaging
- `quantum-medical-diagnosis` — Quantum ML for medical diagnosis

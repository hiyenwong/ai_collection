---
name: foundation-models-brain-biomarker
description: "Foundation models for discovering robust biomarkers of neurological disorders from dynamic functional connectivity. Use when: building neurological biomarker discovery pipelines, applying foundation models to fMRI/EEG data, analyzing dynamic functional connectivity for disease detection, developing robust cross-subject biomarkers. Triggers: brain biomarker foundation model, dynamic functional connectivity biomarker, neurological disorder detection, robust biomarker discovery, fMRI foundation model."
---

# Foundation Models for Brain Biomarker Discovery

Paper: Recent q-bio.NC (May 2026, Deepank Girish et al.)

## Core Approach

Using **foundation models** pretrained on large-scale neuroimaging data to discover **robust biomarkers** of neurological disorders from **dynamic functional connectivity** patterns.

### Key Components

1. **Foundation model pretraining** on large neuroimaging datasets
2. **Dynamic functional connectivity** analysis (time-varying, not static)
3. **Robust biomarker extraction** — stable across subjects and conditions
4. **Neurological disorder classification** — generalizable detection

### Why Foundation Models?

- Transfer learning from large unlabeled datasets
- Capture general brain dynamics patterns
- Fine-tune efficiently for specific disorders
- Reduce need for large labeled clinical datasets

### Robustness Focus
- Cross-subject generalization
- Cross-platform consistency (different scanners/protocols)
- Temporal stability of discovered biomarkers

## Applications
- Parkinson's disease detection
- Alzheimer's disease biomarkers
- Epilepsy focus localization
- Depression subtype classification

## Activation Keywords
- brain biomarker foundation model
- dynamic functional connectivity
- neurological disorder detection AI
- robust biomarker discovery
- fMRI foundation model
- neuroimaging transfer learning

## Tools Used

- `read` - Read neuroimaging data and research papers
- `write` - Save biomarker analysis results and model configurations
- `exec` - Run foundation model training and biomarker discovery scripts

## Instructions for Agents

Follow these steps when helping users with brain biomarker discovery:

1. **Identify the disorder**: Determine the neurological condition to detect (Parkinson's, Alzheimer's, epilepsy, depression)
2. **Select the data modality**: fMRI, EEG, or other neuroimaging data
3. **Apply the foundation model**: Use the pretraining approach from this skill
4. **Extract biomarkers**: Run dynamic functional connectivity analysis for robust biomarker extraction

## Examples

### Example 1: Parkinson's Detection

```
User: "用基础模型检测帕金森病的脑影像生物标志物"

Execute:
1. Load dynamic fMRI connectivity data
2. Apply foundation model pretraining approach
3. Extract robust biomarkers from connectivity patterns
4. Validate cross-subject generalization
```

### Example 2: Alzheimer's Biomarker Discovery

```
User: "发现阿尔茨海默症的动态功能连接生物标志物"

Execute:
1. Load fMRI time-series data
2. Compute dynamic functional connectivity
3. Apply foundation model for biomarker extraction
4. Assess temporal stability of discovered biomarkers
```

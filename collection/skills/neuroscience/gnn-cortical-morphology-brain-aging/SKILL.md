---
name: gnn-cortical-morphology-brain-aging
description: Graph Neural Network (GNN) for estimating local brain age (LBA) from cortical morphology. Uses morphometric features (thickness, surface area, curvature, GWR, sulcal depth) at high spatial resolution. Identifies aging patterns in normal cognition, mild cognitive impairment, and Alzheimer's disease. Links regional LBA gaps to neuropsychological measures.
tags:
  - graph-neural-network
  - brain-aging
  - cortical-morphology
  - Alzheimer-disease
  - local-brain-age
  - morphometric-features
  - high-resolution
  - cognitive-impairment
activation_keywords:
  - brain age estimation
  - cortical aging
  - GNN brain
  - morphometry analysis
  - Alzheimer detection
  - cognitive impairment
  - cortical thickness
  - brain aging patterns
version: 1.0.0
author: arXiv paper extraction
paper_id: arXiv:2601.10912
paper_title: "Graph Neural Network Reveals the Cortical Morphology of Local Brain Aging in Normal Cognition and Alzheimer's Disease"
paper_authors: Samuel D. Anderson, Jordan Jomsky, Nikhil N. Chaudhari, Nahian F. Chowdhury, Xiaoyu (Rayne) Zheng, Andrei Irimia, Alzheimers Disease Neuroimaging Initiative
paper_date: 2026-01-16 (revised 2026-05-27)
doi: https://doi.org/10.48550/arXiv.2601.10912
categories: q-bio.NC, eess.IV, q-bio.QM
---

# GNN for Cortical Morphology Brain Aging Analysis

## 概述

这篇论文介绍了一个基于 Graph Neural Network (GNN) 的框架，用于从 cortical morphology 估计 local brain age (LBA)，提供了比 global brain age (GBA) 更精细的皮质特定衰老模式分析。

**论文信息：**
- 标题："Graph Neural Network Reveals the Cortical Morphology of Local Brain Aging in Normal Cognition and Alzheimer's Disease"
- 作者：Samuel D. Anderson, Jordan Jomsky, Nikhil N. Chaudhari, Nahian F. Chowdhury, Xiaoyu (Rayne) Zheng, Andrei Irimia, Alzheimers Disease Neuroimaging Initiative
- arXiv ID：2601.10912
- 发表日期：2026-01-16 (最后修订：2026-05-27)
- DOI：https://doi.org/10.48550/arXiv.2601.10912

## 核心创新

### 1. Local Brain Age (LBA) 估计框架

**对比 Global vs Local Brain Age：**
- **Global Brain Age (GBA)：** 总结整体脑健康
- **Local Brain Age (LBA)：** 提供皮质特定的衰老模式
  - Subject-level 个性化分析
  - High spatial resolution (mean inter-vertex distance = 1.37 mm)
  - 更细粒度的衰老定位

**技术优势：**
- 首个使用 cortical morphology 估计 LBA 的框架
- 比 state-of-the-art 更低的 MAE
- 识别更生物合理的衰老模式

### 2. Graph Neural Network Architecture

**Morphometric Features 输入：**
1. **Cortical Thickness** - 皮质厚度
2. **Surface Area** - 表面面积
3. **Curvature** - 曲率
4. **Gray/White Matter Intensity Ratio (GWR)** - 灰白质强度比
5. **Sulcal Depth** - 脑沟深度

**Graph Structure：**
- Cortical surface meshes from T1-weighted MRIs
- 高分辨率顶点网络
- Spatial relationships encoded in graph edges

### 3. Training and Validation

**Training Data：**
- Cognitively Normal (CN) adults: N = 14,423
- Large-scale cortical surface mesh dataset

**Validation Data：**
- Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset
- 包含 CN, Mild Cognitive Impairment (MCI), AD subjects

## 主要发现

### 1. Normal Cognition (CN) Aging Patterns

**Primary Aging Sites：**
- **Association cortices** - 主要形态学衰老位置
  - Higher-order cognitive processing regions
  - Multi-modal integration areas

**Characteristics：**
- Focal aging patterns
- Region-specific changes
- Healthy aging baseline

### 2. Mild Cognitive Impairment (MCI) Patterns

**Key Characteristics：**
- **Widespread aging** - 广泛衰老模式
- **Parahippocampal gyrus** - 特别显著的衰老
  - Memory-related region
  - Early AD pathology indicator

**Transition Indicators：**
- From focal (CN) to widespread (MCI) patterns
- Spread to memory-related regions

### 3. Alzheimer's Disease (AD) Patterns

**Comprehensive Aging：**
- **Significant aging across entire cortex**
- Particularly severe in:
  - Medial temporal regions
  - Associated cortical networks

**Pathology-sensitive Features：**
- **Curvature** - preferentially sensitive to AD pathology
- **GWR (Gray/White Matter Intensity Ratio)** - AD pathology indicator

### 4. Clinical Correlations

**Neuropsychological Associations：**
- Regional LBA gaps significantly associated with:
  - AD-related cognitive impairment measures
  - Memory performance
  - Executive function tests

**Clinical Relevance：**
- Links cortical aging patterns to clinical outcomes
- Potential diagnostic utility

## Feature Analysis

### Feature Ablation Results

**Sensitivity to AD Pathology：**

| Feature | AD Sensitivity | Biological Interpretation |
|---------|----------------|---------------------------|
| Curvature | **High** | Cortical folding changes |
| GWR | **High** | Tissue intensity alterations |
| Thickness | Moderate | Volume loss |
| Surface Area | Low-Moderate | Morphological changes |
| Sulcal Depth | Moderate | Surface topography |

**Interpretability：**
- Curvature and GWR emerge as key AD biomarkers
- Feature importance varies by cognitive stage

## Technical Architecture

### GNN Processing Pipeline

```
输入：T1-weighted MRI
↓
Cortical Surface Mesh Extraction
↓
Morphometric Feature Computation (5 features)
↓
Graph Neural Network
↓
Local Brain Age Estimation (per vertex)
↓
Output：Cortical Aging Pattern Map
```

### High-Resolution Analysis

**Spatial Resolution：**
- Mean inter-vertex distance: 1.37 mm
- Thousands of vertices per cortical surface
- Vertex-level LBA predictions

## 应用场景

### 1. Alzheimer's Disease Early Detection

**Use Cases：**
- Early stage identification
- Disease progression monitoring
- Regional pathology localization

**Advantages：**
- High spatial resolution
- Biologically interpretable
- Clinical correlations

### 2. Cognitive Aging Research

**Applications：**
- Normal aging pattern characterization
- Individual aging trajectory analysis
- Cognitive reserve quantification

### 3. Clinical Neuroimaging

**Diagnostic Support：**
- Regional brain health assessment
- Disease staging assistance
- Treatment response monitoring

### 4. Precision Medicine

**Personalized Analysis：**
- Subject-level LBA patterns
- Regional vulnerability mapping
- Intervention targeting

## 性能对比

**Mean Absolute Error (MAE)：**

| Method | MAE | Spatial Resolution |
|--------|-----|--------------------|
| **GNN LBA** | **Lower** | **1.37 mm** |
| Previous SOTA | Higher | Lower |

**Biological Plausibility：**
- More interpretable aging patterns
- Consistent with known AD pathology
- Clinically meaningful associations

## 研究贡献

### Methodological Contributions

1. **First LBA framework using cortical morphology**
2. **High-resolution GNN architecture**
3. **Multi-feature integration approach**
4. **Clinical correlation validation**

### Scientific Findings

1. **Association cortices aging in CN**
2. **Widespread MCI patterns**
3. **Comprehensive AD cortical aging**
4. **Feature-specific AD sensitivity**

### Clinical Insights

1. **LBA-clinical outcome associations**
2. **Regional biomarker identification**
3. **Disease progression mapping**

## 未来方向

### Technical Enhancements

- Multi-modal data integration (fMRI, DTI)
- Temporal aging dynamics modeling
- Cross-site harmonization
- Real-time processing capabilities

### Clinical Applications

- Routine clinical screening
- Drug trial endpoint refinement
- Surgical planning guidance
- Rehabilitation monitoring

### Research Extensions

- Longitudinal aging studies
- Genetic-environmental interactions
- Population-level analyses
- Cross-cultural comparisons

## 参考资源

### Datasets
- Alzheimer's Disease Neuroimaging Initiative (ADNI)
- Large CN cohort (N=14,423)

### Tools
- Cortical surface extraction software
- Graph neural network frameworks
- Neuroimaging analysis packages

### Code Availability
- Code and supplementary tables available at project repository

## 总结

该研究首次建立了使用 cortical morphology 估计 local brain age 的 GNN 框架，在 cognitively normal adults 上训练并在 ADNI 数据集上验证。关键发现包括：association cortices 是 CN 的主要衰老位置，MCI 表现为广泛衰老（特别是 parahippocampal gyrus），AD 显示全皮质显著衰老。Curvature 和 GWR 对 AD pathology 特别敏感。Regional LBA gaps 与 neuropsychological measures 显著相关，展示了临床相关性。

**核心价值：**
1. 方法创新：首个 cortical morphology-based LBA 框架
2. 高分辨率：1.37 mm vertex-level 分析
3. 生物可解释性：比 prior work 更合理
4. 临床相关性：LBA 与认知功能关联
5. AD biomarker：识别 curvature 和 GWR 为敏感特征
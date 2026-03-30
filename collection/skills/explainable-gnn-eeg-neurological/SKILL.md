---
name: explainable-gnn-eeg-neurological
description: Explainable GNN for EEG Neurological Evaluation
---

# Explainable GNN for EEG Neurological Evaluation

**Source:** arXiv:2410.07199v1 (September 2024)
**Utility:** 0.90
**Authors:** Andrea Protani et al.

---

## Description

This skill implements an explainable Graph Neural Network approach for
predicting stroke severity from EEG signals. Using Graph Attention Networks
(GAT), the model provides interpretable attention coefficients that reveal
brain reconfiguration insights for clinical diagnosis.

**Core Method:**
1. **LLC Graph Construction** - Lagged Linear Coherence weighted graphs
2. **Frequency Bands** - δ, θ, α1, α2, β1 connectivity
3. **Graph Attention Model** - Predict NIHSS with explainable attention
4. **Clinical Interpretation** - Attention coefficients reveal key connections

---

## Tools Used

- `eeg_data` - Electroencephalography recordings
- `brodmann_areas` - Brain region mapping
- `lagged_linear_coherence` - LLC connectivity computation
- `torch_geometric` - Graph Neural Network framework
- `gat_model` - Graph Attention Network
- `nihss_scale` - Stroke severity measurement

---

## Instructions for Agents

1. **Prepare EEG data** - 71 patients at hospitalization
2. **Source localization** - Map to Brodmann Areas
3. **LLC computation** - Compute coherence for 5 frequency bands
4. **Graph construction** - Create frequency-specific brain networks
5. **Sparsification** - Apply structural/functional constraints
6. **Train GAT model** - Graph attention for NIHSS prediction
7. **Analyze attention** - Extract interpretable coefficients
8. **Clinical insights** - Identify key neurological connections

---

## Examples

### Example 1: Stroke Severity Prediction

**User:** 如何用 EEG 预测中风严重程度？

**Agent:** 可解释 GNN 流程：

1. **数据收集** - 急性中风患者 EEG（71 人）
2. **源定位** - 映射到 Brodmann 区域
3. **LLC 计算** - 5 个频带连接性
   - δ (2-4 Hz) - 低频慢波
   - θ (4-8 Hz) - 中频
   - α1 (8-10.5 Hz) - 低 α
   - α2 (10.5-13 Hz) - 高 α
   - β1 (13-20 Hz) - β 波
4. **图构建** - 每频带一个脑网络图
5. **稀疏化** - 结构+功能约束
6. **GAT 训练** - 预测 NIHSS
7. **注意力分析** - 解释关键连接

**优势：** 可解释 + 高精度 + 临床可用

### Example 2: Brain Reconfiguration Insights

**User:** 中风后脑网络如何重组？

**Agent:** GNN 注意力揭示：

| 频带 | 重配置特征 |
|------|-----------|
| δ | 慢波活动增加 |
| θ | 认知功能重组 |
| α | 抑制功能改变 |
| β | 运动相关变化 |

**临床价值：**
- 诊断：识别受损区域
- 治疗：个性化干预
- 康复：早期神经康复指导

---

## Activation Keywords

- 可解释 GNN、explainable GNN
- EEG 神经评估、EEG neurological evaluation
- 中风严重程度、stroke severity NIHSS
- 图注意力网络、graph attention network
- LLC 连接性、lagged linear coherence
- 脑重组、brain reconfiguration

---

## Key Concepts

### 1. Lagged Linear Coherence (LLC)

**Purpose:** Measure directional connectivity between Brodmann Areas

**Formula:** LLC captures phase-lagged coherence, avoiding volume conduction
artifacts

**Advantage:** Better estimation of true neural interactions

### 2. Frequency-Specific Brain Networks

| Band | Frequency | Function |
|------|-----------|----------|
| δ | 2-4 Hz | Slow wave, sleep, pathology |
| θ | 4-8 Hz | Memory, cognitive |
| α1 | 8-10.5 Hz | Relaxation, inhibition |
| α2 | 10.5-13 Hz | Alertness |
| β1 | 13-20 Hz | Active thinking, motor |

### 3. Graph Attention Network (GAT)

**Architecture:**
- Attention mechanism: Learn edge importance
- Multi-head attention: Capture multiple patterns
- Interpretable coefficients: Clinical insights

**Formula:**
```
Attention coefficient α_ij = softmax(LeakyReLU(a^T [Wh_i || Wh_j]))
```

### 4. NIHSS Prediction

**NIH Stroke Scale:** 0-42 score measuring stroke severity

**Model Output:** Continuous NIHSS prediction from EEG connectivity

---

## Architecture

```
EEG Recording → Source Localization → Brodmann Areas
    ↓
LLC Computation (5 bands) → Frequency-Specific Graphs
    ↓
Sparsification → Sparse Brain Networks
    ↓
Graph Attention Network → NIHSS Prediction
    ↓
Attention Coefficients → Clinical Interpretation
```

---

## Results (Paper)

| Metric | Value |
|--------|-------|
| Patients | 71 acute stroke |
| Frequency bands | 5 (δ, θ, α1, α2, β1) |
| Model | Graph Attention Network |
| Target | NIHSS (stroke severity) |
| Interpretability | ✅ Attention coefficients |

**Key Finding:** Frequency-dependent brain connectivity reorganization
post-stroke, captured by GAT attention.

---

## When to Use

1. **Stroke severity prediction** - NIHSS from EEG
2. **Clinical diagnosis** - Acute stroke evaluation
3. **Neurorehabilitation** - Early intervention planning
4. **Brain reorganization analysis** - Post-stroke connectivity
5. **Explainable ML** - Interpretable neurological models

---

## Clinical Applications

### Diagnosis
- Acute stroke severity estimation
- Quantitative EEG analysis
- Frequency-specific biomarkers

### Treatment Planning
- Personalized intervention
- Target specific frequency bands
- Neurorehabilitation guidance

### Monitoring
- Recovery trajectory
- Treatment effectiveness
- Brain reorganization tracking

---

## Limitations

1. Requires source localization (LORETA, etc.)
2. Limited to acute stroke patients
3. Needs sufficient patient samples
4. Attention interpretation needs clinical expertise
5. Frequency band selection may vary

---

## Related Skills

- `brain-graph-augmentation-template` - Graph augmentation
- `tms-eeg-biomarkers` - EEG biomarkers
- `eeg-brain-connectivity-bci` - EEG connectivity BCI
- `gnn-transformer-fusion` - GNN architectures
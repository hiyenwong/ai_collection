---
name: identity-trap-eeg-foundation-models
description: The Identity Trap in EEG Foundation Models: A Diagnostic Audit — FMScope framework for detecting shortcut learning in clinical EEG
version: 1.0.0
category: neuroscience
activation_keywords:
  - EEG foundation model
  - identity trap
  - shortcut learning
  - FMScope
  - subject identity
  - clinical biomarker
  - variance decomposition
  - subject-axis erasure
  - aperiodic 1/f
  - label probing
  - frozen representation
tags:
  - EEG
  - foundation models
  - clinical neuroscience
  - shortcut learning
  - diagnostic audit
  - LaBraM
  - CBraMod
  - REVE
  - subject identity
authors:
  - Jun-You Lin
  - Ying Choon Wu
  - Tzyy-Ping Jung
arxiv_id: 2606.06647
date_added: 2026-06-08
source: arXiv cs.LG + q-bio.NC
---

# The Identity Trap in EEG Foundation Models

## Core Problem

EEG基础模型的身份陷阱问题 - 高准确率可能反映主体身份特征而非临床生物标志物。FMScope框架在微调前诊断冻结表示层面的身份陷阱。

**核心发现**:
- **身份陷阱普遍性**: 12/12实验中,冻结主体方差为随机空模型的13-89倍
- **微调放大**: 所有12个实验中,主体方差在微调后增加(+10到+63 pp)
- **可移除轴**: 主体身份是可移除的线性轴
- **周期1/f依赖**: 周期信号是主体身份载体之一

## FMScope Diagnostic Framework

### Five Diagnostic Components

#### 1. Variance Decomposition
方差分解:
- **主体方差**: 分离主体相关方差成分
- **标签方差**: 分离标签相关方差成分
- **对比**: 主体方差 vs 随机空模型
- **量化**: 13-89倍提升表示强主体信号

#### 2. Subject-Axis Erasure
主体轴消除:
- **线性轴识别**: 主体身份作为可移除线性轴
- **消除效果**: 在标签随主体变化时改善解码(+6到+12 pp)
- **外部队列**: 跨外部队列改善(+4到+27 pp)
- **移除方法**: 线性投影消除主体轴

#### 3. Aperiodic 1/f Ablation
周期1/f消融:
- **载体识别**: 周期1/f信号携带主体身份
- **消融效果**: LaBraM和CBraMod中,主体探针下降9-19 pp
- **REVE例外**: REVE饱和主体身份,无明显周期依赖
- **生理基础**: 周期信号有可测量生理成分

#### 4. Layer-wise Label Probing
层级标签探针:
- **冻结探针**: 在冻结表示上探针标签
- **层级分析**: 分析各层标签可解码性
- **对比**: 冻结 vs 微调标签探针性能
- **生物标志物指标**: 仅在有文献支持标志物的实验中,微调放大标签方差

#### 5. Within-Subject Direction Consistency
主体内方向一致性:
- **方向检验**: 同一主体不同样本的方向一致性
- **标签相关**: 方向是否与标签一致
- **主体相关**: 方向是否与主体身份一致
- **判别**: 区分生物标志物 vs 主体身份信号

## Key Results

### Identity Trap Universal
身份陷阱的普遍性:
- **所有模型**: LaBraM, CBraMod, REVE均存在
- **所有数据集**: 四个临床数据集均显示
- **冻结状态**: 13-89倍主体方差提升
- **微调状态**: 10-63 pp主体方差增加

### Removable Linear Axis
可移除线性轴特性:
- **主体身份**: 可通过线性投影消除
- **改善解码**: 在标签随主体变化时改善
- **保持性能**: 不损害真正的生物标志物检测
- **物理基础**: 有可测量生理成分

### Aperiodic 1/f as Carrier
周期1/f作为主体载体:
- **LaBraM**: 移除周期信号 → 主体探针下降19 pp
- **CBraMod**: 移除周期信号 → 主体探针下降9 pp
- **REVE**: 无周期依赖,通过其他特征饱和主体身份
- **生理对应**: 周期信号反映大脑状态特征

### Fine-Tuning Amplification
微调放大效应:
- **条件性**: 仅在有文献支持标志物时放大标签方差
- **选择性**: 标签随主体变化时改善
- **方向性**: 微调学习方向依赖标志物存在性
- **判别性**: 区分生物标志物学习 vs 主体身份学习

## Experimental Design

### 2x2 Layout
实验设计矩阵:
- **标签-主体关系**: 标签是否随主体变化
- **生物标志物存在**: 是否有文献支持的跨主体标志物
- **四种组合**: 
  - (标签变化, 标志物存在) → 主要改善
  - (标签变化, 标志物缺失) → 无改善
  - (标签固定, 标志物存在) → 验证改善
  - (标签固定, 标志物缺失) → 无改善

### Three Models Tested
测试的三个模型:
- **LaBraM**: 大规模EEG基础模型
- **CBraMod**: 跨主体EEG模型
- **REVE**: 表示增强EEG模型

### Four Datasets
四个数据集:
- **临床静息态**: 不同临床条件EEG
- **主体分离**: 跨主体交叉验证
- **标签变化**: 标签随主体变化的条件
- **标签固定**: 标签不随主体变化的条件

## Critical Analysis

### Strengths
- **诊断框架**: 五种互补诊断方法
- **物理基础**: 主体身份有可测量生理成分
- **可操作**: 主体轴消除改善性能
- **普遍性**: 所有模型和数据集存在
- **区分性**: 区分生物标志物 vs 主体身份

### Implications
- **评估标准**: 主体分离验证不足以排除身份陷阱
- **模型设计**: 需要显式消除主体身份
- **临床应用**: 高准确率不代表临床有效性
- **研究规范**: 需要标准化诊断流程

### Limitations
- **冻结诊断**: 仅诊断冻结表示,微调后可能变化
- **线性假设**: 主体轴假设为线性,可能更复杂
- **周期依赖**: 仅测试周期1/f,可能存在其他载体
- **数据集限制**: 仅静息态EEG,其他范式待测试

## Practical Applications

### Model Evaluation
评估EEG基础模型:
1. **方差分解**: 计算主体方差比
2. **轴消除**: 测试主体轴消除效果
3. **周期消融**: 移除周期信号测试
4. **层级探针**: 各层标签可解码性
5. **方向一致性**: 主体内方向检验

### Model Design
设计鲁棒EEG模型:
- **显式消除**: 训练时显式消除主体身份
- **架构修改**: 减少主体信息传递
- **损失函数**: 添加主体无关约束
- **数据增强**: 跨主体数据增强

### Clinical Validation
临床验证规范:
- **FMScope诊断**: 应用五种诊断方法
- **生物标志物检验**: 验证文献支持标志物
- **主体轴消除**: 测试消除后性能
- **外部队列验证**: 跨队列泛化测试

## Implementation Guide

### FMScope Protocol
```python
# 1. Variance Decomposition
subject_variance = compute_variance(decomposition='subject')
null_variance = compute_variance_null()
ratio = subject_variance / null_variance  # Should be ~1 if no identity trap

# 2. Subject-Axis Erasure
subject_axis = identify_subject_axis(representations)
erased_rep = project_away(representations, subject_axis)
decoding_erased = probe_label(erased_rep)

# 3. Aperiodic 1/f Ablation
aperiodic_removed = remove_aperiodic_1f(representations)
subject_probe_aperiodic = probe_subject(aperiodic_removed)

# 4. Layer-wise Label Probing
layer_probes = []
for layer in model.layers:
    probe = linear_probe(layer_activations, labels)
    layer_probes.append(probe)

# 5. Within-Subject Direction Consistency
within_subject_dirs = compute_directions(subject_samples)
consistency = check_consistency(within_subject_dirs, labels)
```

### Diagnosing Identity Trap
诊断身份陷阱的步骤:
1. **计算主体方差比**: ratio > 13表示强身份陷阱
2. **测试轴消除**: 改善解码表示身份陷阱影响
3. **周期消融**: 下降表示周期信号作为载体
4. **层级探针**: 各层主体信号强度
5. **方向一致性**: 区分生物标志物 vs 主体信号

### Remediation Strategies
缓解策略:
- **训练时消除**: 显式消除主体身份
- **架构修改**: 减少主体信息流
- **损失约束**: 主体无关约束
- **数据增强**: 跨主体增强

## Research Questions

1. **其他载体**: 除了周期1/f,还有哪些主体身份载体?
2. **非线性轴**: 主体轴是否非线性?
3. **其他范式**: 任务态EEG是否存在身份陷阱?
4. **模型设计**: 如何从架构上避免身份陷阱?
5. **临床有效性**: 如何验证临床生物标志物有效性?

## Related Work

- **Shortcut Learning**: AI系统shortcut学习理论
- **EEG Foundation Models**: LaBraM, CBraMod, REVE等模型
- **Subject Identity**: EEG中的主体身份特征
- **Clinical Biomarkers**: EEG临床生物标志物研究
- **Representation Learning**: 表示学习诊断方法

## Reference

- arXiv:2606.06647 - "The Identity Trap in EEG Foundation Models: A Diagnostic Audit"
- Authors: Jun-You Lin, Ying Choon Wu, Tzyy-Ping Jung
- Submitted: 2026-06-04
- Categories: cs.LG (Machine Learning), q-bio.NC (Neurons and Cognition)
- Code: Available at linked repository
---
name: neural-encoding-evaluation-meeg
version: v1.0.0
last_updated: 2026-04-18
description: "Evaluation framework for neural encoding models using MEEG (Mutual-information-based Estimation of Encoding model goodness-of-fit). Provides systematic methodology for assessing how well neural models predict brain activity, with information-theoretic metrics and cross-validation protocols."
category: neuroscience
tags:
  - encoding-models
  - model-evaluation
  - mutual-information
  - neural-data
  - information-theory
  - model-selection
paper:
  title: "Neural Encoding Model Evaluation (MEEG)"
  published: "2026-04-17"
  url: "https://arxiv.org/abs/2604.12463"
activation: "encoding model, model evaluation, neural data, mutual information, model selection, goodness-of-fit"
---

# Neural Encoding Model Evaluation (MEEG)

## 概述

神经编码模型评估框架，使用基于互信息的评估指标（MEEG）系统化地评估神经模型预测脑活动的能力。提供信息论指标和交叉验证协议。

## 核心问题

神经编码模型（如 pRF 模型、DNN 特征编码）的性能评估缺乏统一标准。需要信息论框架来量化模型对神经数据的解释能力。

## 方法论

### MEEG 指标

```python
def compute_meeg(predicted, observed):
    """计算基于互信息的编码模型拟合优度"""
    # 估计联合分布 p(predicted, observed)
    joint_dist = estimate_joint(predicted, observed)
    # 计算互信息
    mi = mutual_information(joint_dist)
    # 归一化为解释方差当量
    meeg_score = normalize_mi(mi)
    return meeg_score
```

### 评估协议

1. **交叉验证**：k-fold 交叉验证，避免过拟合
2. **基线比较**：与简单基线模型比较
3. **噪声上限**：估计数据本身的可预测性上限

### 模型选择

- 使用 MEEG 分数进行模型比较
- 考虑模型复杂度（AIC/BIC）
- 多模态数据的联合评估

## 应用场景

- **视觉编码模型**：评估 DNN 特征对 V1-V4 活动的预测
- **语言编码模型**：评估语言模型对 ECoG 响应的预测
- **多模态编码**：联合评估跨模态的编码性能

## 参考文献

```bibtex
@article{meeg2026,
    title={Neural Encoding Model Evaluation (MEEG)},
    journal={arXiv preprint arXiv:2604.12463},
    year={2026}
}
```

---
*Generated on 2026-04-18*
---
name: sc-taupath-alzheimer-tau-propagation
description: SC-TauPath 结构连接归因框架用于映射阿尔茨海默病 Tau 传播路径。结合网络扩散模型增强 MLP 与梯度×输入归因，生成多尺度路径图谱（骨干边、高流量路由、枢纽 ROI），验证 Braak 分期解剖学。
version: 1.0.0
category: neuroscience
authors:
  - Jing Zhang
  - Norman Scheel
  - Minheng Chen
arxiv_id: 2606.04066
created: 2026-06-09
activation_keywords:
  - tau propagation
  - Alzheimer's disease
  - structural connectivity
  - network diffusion
  - attribution framework
  - Braak staging
related_skills:
  - brain-network-controllability
  - alzheimer-pet-suvr-network-models
---

# SC-TauPath: Structural Connectivity Attribution Framework for Alzheimer's Tau Propagation

## Overview

SC-TauPath 是一个结构连接（SC）归因框架，从体内神经影像数据映射 Tau 传播路径。结合网络扩散模型增强的 MLP 与梯度×输入归因，生成多尺度路径图谱，验证 Braak 分期解剖学。

## Core Methodology

### 1. Network Diffusion Model-Augmented MLP

结合网络扩散理论的可解释神经网络架构：
- 输入：DTI 结构连接矩阵 + 18F-Flortaucipir PET Tau 分布
- 增强：网络扩散模型（NDM）约束损失函数
- 预测：区域 Tau 分布预测（交叉验证）

### 2. Gradient × Input Attribution

可解释的边贡献评分：
- 物理意义：每条 SC 边对 Tau 预测的贡献度
- 归因映射：将评分转换为多尺度路径图

### 3. Multi-Scale Pathway Maps

三级路径图谱：
- Backbone edges：高归因评分的核心传播通道
- High-traffic routes：多边组合的高流量路径
- Hub ROIs：关键传播枢纽节点

### 4. Braak Staging Validation

与经典 Braak 分期的解剖学一致性验证：
- Braak I-II：内嗅皮层-海马通路
- Braak III-IV：杏仁核-颞叶新皮层扩展
- Braak V-VI：新皮层广泛传播

## Implementation Workflow

### Step 1: Data Preparation

需要的数据：
- DTI structural connectivity matrix (N×N)
- 18F-Flortaucipir PET Tau SUVR maps
- ROI parcellation (e.g., AAL, Desikan-Killiany)

### Step 2: NDM-Augmented MLP Training

架构设计：
```
Input: SC matrix (N×N)
  ↓
SC Encoder (flatten → hidden_dim)
  ↓
NDM Constraint Loss (network diffusion theory)
  ↓
Predictor (hidden_dim → N ROI tau values)
  ↓
Output: Tau distribution prediction
```

### Step 3: Attribution Computation

算法流程：
1. 计算预测输出对 SC 输入的梯度
2. Gradient × Input 得到边归因评分
3. 重塑为 N×N 归因矩阵

### Step 4: Pathway Extraction

提取策略：
- extract_backbone_edges: percentile threshold (e.g., top 30%)
- identify_hub_rois: top-k ROI importance
- extract_high_traffic_routes: multi-hop path aggregation

## Key Findings

### Cross-Validated Performance

- 234 ADNI 参与者的交叉验证 Tau 预测
- 结构连接编码区域 Tau 分布的空间特异性信息

### Anatomical Consistency

归因路径图与 Braak 分期解剖学的对应：
- 传播起点：内嗅皮层 → 海马（Braak I-II）
- 关键枢纽：杏仁核、颞叶内侧结构
- 扩展路径：额叶、顶叶新皮层（Braak V-VI）

## Applications

1. Tau 传播机制理解：从结构连接角度解释疾病进展
2. 治疗靶点识别：高归因枢纽节点作为干预候选
3. 早期诊断：Tau 传播路径预测用于风险评估
4. 临床试验设计：基于传播路径的患者分层

## Advantages Over Existing Methods

- Biophysical models：Heavy assumptions, Low interpretability
- Pure ML models：No assumptions, Low interpretability
- SC-TauPath：Light NDM constraint, High interpretability, Multi-scale pathway maps

## Limitations

1. DTI 限制：结构连接估计的可靠性依赖 DTI 质量
2. Tau PET 成本：18F-Flortaucipir 成本较高
3. 静态模型：未捕获动态传播过程
4. 样本依赖：ADNI 样本可能不代表所有 AD 亚型

## Future Directions

1. 纵向数据整合：添加时间序列 Tau PET 数据
2. 多模态融合：结合功能连接、代谢成像
3. 个体化路径：开发个性化传播预测模型
4. 药物试验应用：用于抗 Tau 药物试验的患者选择

## References

- arXiv:2606.04066
- Braak H, Braak E. Neuropathological stageing of Alzheimer-related changes. Acta Neuropathol (1991)
- Iturria-Medina Y, et al. Network diffusion model of brain atrophy in Alzheimer's disease. NeuroImage (2017)

## Related Work

- brain-network-controllability：网络控制理论用于脑状态转移
- alzheimer-pet-suvr-network-models：Alzheimer PET 网络建模
- time-varying-brain-connectivity：时变脑连接分析方法
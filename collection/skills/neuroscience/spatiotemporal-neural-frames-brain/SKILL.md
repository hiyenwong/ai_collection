---
name: spatiotemporal-neural-frames-brain
version: 1.0.0
description: EEG-conditioned framework reconstructing dynamic fMRI as continuous neural sequences at cortical-vertex level. Null-space intermediate-frame reconstruction for arbitrary missing frames. CVPR 2026.
created: 2026-04-23
source: arXiv:2603.24176
authors: Qu, Gao, Wang, Fu
title: "Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamics"
tags: [eeg-fmri, multimodal, brain-reconstruction, cvpr-2026, neural-frames, cortical-vertex]
activation: EEG-fMRI reconstruction, brain dynamic modeling, multimodal neuroimaging, neural frame, CineBrain
---

# Spatiotemporal Neural Frames for High Resolution Brain Dynamics

## 概述
CVPR 2026论文。提出EEG条件化框架，从EEG信号重建高分辨率动态fMRI，将其建模为具有高空间保真度和强时间连贯性的连续神经序列（cortic-vertex级别）。

## 核心创新
1. **神经帧 (Neural Frames)** — 将fMRI建模为连续神经序列而非独立体积
2. **EEG条件化重建** — 利用EEG毫秒级时间分辨率补充fMRI空间信息
3. **零空间中间帧重建** — 处理真实fMRI采集中的采样不规则性
4. **Cortical-Vertex级别** — 在皮层顶点级别进行重建，远高于传统体素级别

## 方法论架构

### 1. EEG条件化生成框架
```
EEG信号 → 时序编码器 → 条件向量
                                ↓
                    fMRI生成器 → 动态神经帧序列
```

### 2. 神经帧建模
- 将fMRI时间序列视为连续视频帧（类似视频生成）
- 每帧为皮层表面的顶点级信号
- 时间连贯性约束确保动态连续性

### 3. 零空间中间帧重建
- **问题**: 真实fMRI采集不规则，存在缺失帧
- **解法**: 在零空间中重建中间帧
- **关键**: 保持与已有测量的一致性 (measurement-consistent)
- **效果**: 支持任意时间点的帧插值

### 4. 空间表示
- Cortical-vertex级别重建（~32k-160k顶点）
- 远超传统体素级别（~2mm³分辨率）
- 保留皮层表面的拓扑结构

## 技术细节
- **数据集**: CineBrain（高时间分辨率fMRI + 同步EEG）
- **损失函数**:
  - 体素级重建损失
  - 时间连贯性损失
  - 零空间一致性约束
- **评估指标**:
  - 体素级PSNR/SSIM
  - 时间一致性指标
  - 功能信息保留度

## 关键结果
1. **重建质量** — 全脑和功能特定区域的优越体素级重建
2. **时间连贯性** — 动态序列的强时间一致性
3. **功能保留** — 重建fMRI保持原始功能信息
4. **下游任务** — 支持视觉解码等下游任务

## 应用场景
1. **低成本脑成像** — 从EEG获取类fMRI的空间分辨率
2. **动态脑活动监测** — 连续追踪脑状态变化
3. **视觉解码增强** — 提供更丰富的空间特征
4. **临床诊断** — 结合EEG的时间精度和fMRI的空间精度

## 复现指南
1. 使用CineBrain数据集（需申请）
2. EEG预处理：带通滤波、伪迹去除、通道对齐
3. fMRI预处理：皮层表面重建、顶点级信号提取
4. 训练：先训练体素级基线，再扩展到顶点级
5. 零空间约束需要矩阵分解

## 参考信息
- arXiv: 2603.24176
- 日期: 2026-03-25 (revised 2026-03-31)
- 会议: CVPR 2026
- 领域: eess.IV, cs.CV, q-bio.NC
- 数据集: CineBrain

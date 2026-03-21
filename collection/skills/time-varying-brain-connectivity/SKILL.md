---
name: time-varying-brain-connectivity
version: 1.0.0
description: |
  时变有向脑网络连接分析方法论。基于 SWpC (sliding-window prediction correlation) 
  估计动态功能连接，支持方向性信息流分析。
  触发词：脑网络、功能连接、动态连接、SWpC、time-varying connectivity、
  directed functional connectivity、脑网络分析、神经科学方法。
---

# Time-Varying Directed Brain Connectivity

## 核心方法论

### SWpC (Sliding-Window Prediction Correlation)

**问题：** 传统滑动窗口相关 (SWC) 只能捕捉无向关联，无法推断时变信息流方向。

**解决方案：** 在每个滑动窗口内嵌入方向性线性时不变 (LTI) 模型。

### 两个关键描述符

| 描述符 | 含义 | 用途 |
|--------|------|------|
| **预测相关性** (Prediction Correlation) | 方向性连接强度 | 量化信息流强度 |
| **持续时间** (Window-wise Duration) | 信息传递持续时间 | 识别持续/瞬时连接 |

---

## 验证数据集

1. **大鼠体感皮层 LFP + fMRI BOLD**
   - 验证方向性估计稳定性
   - 跨模态一致性检验

2. **Human Connectome Project (HCP) 运动任务 fMRI**
   - 检测任务诱发的有向功能连接变化
   - 比 SWC 更敏感地识别任务相关连接差异

3. **脑震荡后前庭功能障碍 (PCVD)**
   - 揭示可重复的前庭-多感觉脑状态转换
   - 改善健康对照组 vs 亚急性患者分类

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **基础神经科学** | 理解神经信息处理的时间动态 |
| **临床应用** | 脑疾病诊断、患者分层 |
| **多模态验证** | LFP、fMRI BOLD、EEG 等 |

---

## 技术要点

### 与 SWC 对比

| 特性 | SWC | SWpC |
|------|-----|------|
| 方向性 | ❌ 无 | ✅ 有 |
| 信息流推断 | ❌ 无法 | ✅ 可以 |
| 任务敏感性 | 一般 | 更高 |
| 解释性 | 无向相关 | 有向强度 + 持续时间 |

### 实现步骤

1. 选择滑动窗口大小（根据数据采样率）
2. 在每个窗口内拟合 LTI 模型
3. 计算预测相关性（强度）
4. 计算窗口持续时间（信息传递持续时间）
5. 跨窗口分析动态变化

---

## 相关技能

- `infinite-horizon-stochastic-analysis` - 无限视界随机系统分析
- `constraint-relax-then-tighten` - 约束先放后紧

---

## 来源

- **论文：** Time-Varying Directed Interactions in Functional Brain Networks: Modeling and Validation
- **arXiv：** 2602.16004
- **效用评分：** 1.0
- **学习日期：** 2026-03-21
---
skill_name: psychosis-scaling-critical-regime
description: 早期精神病临界区域内标度行为偏差研究。使用现象学重整化群(PRG)、功率谱密度(PSD)和去趋势波动分析(DFA)揭示精神病中的集体动力学重组而非简单临界态丢失。
version: 1.0.0
tags: [neuroscience, criticality, psychosis, brain-networks, renormalization-group, scaling-analysis, psychiatric-disorders]
authors: [Irem Topal, Paola Moreno Ancalmo, Guillermo Montana Valverde, Philipp Homan, Wolfram Hinzen]
paper_id: arXiv:2606.06290
date: 2026-06-05
activation_keywords: [criticality, psychosis, scaling behavior, renormalization group, power spectral density, detrended fluctuation analysis, brain dynamics, psychiatric disorders, collective dynamics]
---

# Early Psychosis Scaling Behavior in Critical Regime

## 核心问题
大规模脑活动是否处于临界态？精神病是否改变这种临界动力学组织？如何用多尺度分析框架统一评估精神病的脑动力学异常？

## 理论背景

### 临界态假说
- **定义**: 神经系统在临界点附近运行，表现出尺度不变性和长程时空关联
- **功能优势**: 
  - 最大动态范围 (Kinouchi & Copelli 2006)
  - 高效信息处理 (Shew & Plenz 2013)
  - 灵活协调的大尺度动力学
- **实验证据**: 神经雪崩、长程时间关联、无标度功率谱

### 精神病临界态研究现状
- **问题**: 不同研究使用不同方法/模态，结果碎片化
- **已知异常**: PSD、DFA、神经雪崩统计、分支过程测量
- **缺口**: 缺乏统一框架连接空间和时间标度性质

## 方法论框架：三重分析

### 1. 现象学重整化群 (PRG)
- **原理**: 粗粒化方法提取跨尺度集体动力学
- **操作**: 系统性合并神经元群体 → 追踪集体行为演化
- **指标**: 重整化后的相关长度、自由度缩减率
- **核心假设**: 临界系统在粗粒化下保持标度不变性

```python
# PRG粗粒化过程
def prg_coarse_graining(fmri_data, scale_levels):
    """
    系统性合并神经元群体提取集体动力学
    
    Args:
        fmri_data: 原始fMRI时间序列 [N_timepoints, N_voxels]
        scale_levels: 粗粒化层级列表
    
    Returns:
        collective_dynamics: 各尺度的集体行为指标
    """
    collective_dynamics = {}
    for scale in scale_levels:
        # 空间聚合
        aggregated = spatial_aggregation(fmri_data, scale)
        # 计算集体指标
        collective_dynamics[scale] = {
            'correlation_length': compute_corr_length(aggregated),
            'dimension_reduction': compute_dim_reduction(aggregated)
        }
    return collective_dynamics
```

### 2. 功率谱密度 (PSD)
- **原理**: 频域分析检测无标度时间动力学
- **临界特征**: S(f) ~ 1/f^β (幂律衰减)
- **指标**: β指数偏离度（健康 ~ 1, 病理偏离）

```python
def compute_psd_scaling(fmri_signal):
    """
    计算功率谱密度标度指数
    
    Args:
        fmri_signal: 单体素或ROI时间序列
    
    Returns:
        beta: PSD标度指数 (临界态 β~1)
    """
    from scipy.signal import welch
    
    freqs, psd = welch(fmri_signal, fs=TR, nperseg=256)
    # 拟合幂律: log PSD = -β log f + c
    valid_range = (freqs > 0.01) & (freqs < 0.1)  # 低频范围
    log_f = np.log(freqs[valid_range])
    log_psd = np.log(psd[valid_range])
    
    beta = -np.polyfit(log_f, log_psd, 1)[0]
    return beta
```

### 3. 去趋势波动分析 (DFA)
- **原理**: 检测长程时间关联（非平稳信号适用）
- **临界特征**: F(n) ~ n^α (幂律波动函数)
- **健康范围**: α ∈ [0.5, 1.0]（临界态附近）
- **指标**: α指数系统性偏移

```python
def detrended_fluctuation_analysis(signal, window_sizes):
    """
    DFA分析检测长程时间关联
    
    Args:
        signal: 时间序列
        window_sizes: 分析窗口大小列表
    
    Returns:
        alpha: DFA标度指数
        F_values: 各窗口的波动函数值
    """
    # 积分信号
    integrated = np.cumsum(signal - np.mean(signal))
    
    F_values = []
    for n in window_sizes:
        # 分割窗口
        segments = len(integrated) // n
        # 各窗口去趋势
        trends = []
        for i in range(segments):
            segment = integrated[i*n:(i+1)*n]
            trend = np.polyfit(np.arange(n), segment, 1)
            detrended = segment - np.polyval(trend, np.arange(n))
            F = np.sqrt(np.mean(detrended**2))
            trends.append(F)
        F_values.append(np.mean(trends))
    
    # 拟合幂律: log F = α log n
    alpha = np.polyfit(np.log(window_sizes), np.log(F_values), 1)[0]
    
    return alpha, F_values
```

## 实验设计

### 数据集
- **参与者**: 早期精神病个体 + 健康对照
- **模态**: 静息态fMRI
- **预处理**: 标准fMRI预处理流水线

### 分析流程
1. PRG粗粒化 → 提取空间尺度动力学
2. PSD分析 → 时间域无标度检测
3. DFA分析 → 长程关联量化
4. 跨尺度对比 → 统合评估动力学重组

## 关键发现

### 健康对照结果
- **标度不变性**: 所有三种方法一致显示临界态特征
- **PRG**: 粗粒化保持动力学一致性
- **PSD**: β指数接近理论临界值
- **DFA**: α指数处于健康范围

### 早期精神病结果
- **核心发现**: 标度行为系统性偏移，但临界态框架保留
- **不是简单丢失**: 不是"远离临界态"，而是"临界态内重组"
- **三种方法一致性**: PRG、PSD、DFA均显示相似偏移模式
- **集体动力学改变**: 大尺度脑网络协调性重组

### 标度指数偏移模式
| 方法 | 健康对照 | 早期精神病 | 偏移方向 |
|------|---------|-----------|---------|
| PSD β | ~1.0 | 偏离 | 频域动力学改变 |
| DFA α | [0.5, 1.0] | 偏移 | 时间关联强度改变 |
| PRG相关长度 | 标度不变 | 偏移 | 空间协调性改变 |

## 理论意义

### 1. 非简单去临界化
- **传统观点**: 精神病 = 临界态丢失
- **新发现**: 精神病 = 临界态内动力学重组
- **比喻**: 不是"温度偏离临界点"，而是"临界点附近参数重构"

### 2. 统一评估框架
- **碎片化问题**: 不同方法孤立评估 → 结果不可比
- **PRG+PSD+DFA整合**: 空间+时间+关联 → 统合动力学视图
- **标准化潜力**: 为精神病临界态研究提供方法论标准

### 3. 集体动力学视角
- **超越单节点**: 关注大尺度脑网络协调性
- **重整化思想**: 从微观神经元 → 宏观集体行为
- **精神病机制**: 集体动力学组织改变而非单点功能障碍

## 临床应用潜力

### 诊断标记物
- **触发条件**: 精神病风险评估、早期诊断
- **实施方案**: PRG+PSD+DFA三重标度分析
- **判别依据**: 三种指数系统性偏移模式

### 病程监测
- **追踪指标**: 标度指数动态变化
- **治疗响应**: 指数回归健康范围 → 治疗有效
- **复发预测**: 指数偏离 → 复发风险升高

### 分层治疗
- **动力学分层**: 不同标度偏移模式 → 不同病理亚型
- **精准干预**: 针对动力学重组模式选择治疗策略

## 实施检查清单

- [ ] 数据预处理：标准fMRI流程（运动校正、空间标准化、滤波）
- [ ] PRG粗粒化：至少5个尺度层级，覆盖从voxel到全脑
- [ ] PSD分析：低频范围0.01-0.1 Hz，排除高频噪声
- [ ] DFA分析：窗口大小覆盖10-100%信号长度
- [ ] 跨尺度对比：三种方法结果一致性检验
- [ ] 统计检验：组间差异显著性（p<0.05校正）

## 限制与注意事项

1. **模态局限**: 仅fMRI静息态数据，需扩展到EEG/MEG验证
2. **样本量**: 需大样本验证标度偏移稳定性
3. **病程特异性**: 早期精神病 vs 慢性精神病的标度差异未知
4. **药物效应**: 抗精神病药物对标度行为的影响待研究
5. **个体差异**: 标度指数个体内稳定性需纵向验证

## 与现有框架对比

| 框架 | 分析维度 | 精神病结论 | 统合性 |
|------|---------|-----------|--------|
| PRG+PSD+DFA | 空间+时间+关联 | 临界态内重组 | ✓ 统合 |
| 单一PSD/DFA | 时间 | 标度偏移 | ✗ 碎片化 |
| 神经雪崩 | 空间 | 临界态改变 | ✗ 单一指标 |
| 分支过程 | 拓扑 | 参数偏离 | ✗ 模型依赖 |

## 引用
```bibtex
@article{topal2026psychosis,
  title={Early psychosis shows deviations in scaling behaviour within a critical regime},
  author={Topal, Irem and Ancalmo, Paola Moreno and Valverde, Guillermo Montana and Homan, Philipp and Hinzen, Wolfram},
  journal={arXiv preprint arXiv:2606.06290},
  year={2026}
}
```

## 相关技能
- [[brain-critical-dynamics-theory]]: 神经系统临界态理论
- [[griffiths-phase-brain-criticality]]: Griffiths相扩展临界区域框架
- [[renormalization-scaling-brain-activity]]: 重整化群分析脑活动标度律
- [[neutral-theory-neural-dynamics]]: 中性理论解释无标度神经动力学

## 扩展阅读
- Chialvo (2010): "Emergent complex neural dynamics"
- Munoz (2018): "Colloquium: Criticality and dynamical scaling in living systems"
- Meshulam et al. (2019): PRG coarse-graining methodology
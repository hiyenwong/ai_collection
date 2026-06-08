---
name: psychosis-scaling-critical-regime
description: 精神病早期阶段脑动力学临界性scaling偏差研究方法论。结合重整化群(RG)框架与多种scaling分析方法，揭示临界 regime内的动力学重组而非临界性丧失。
platforms: [linux, macos, windows]
tags: [neuroscience, criticality, psychosis, fMRI, renormalization-group, scaling-analysis, brain-dynamics]
category: neuroscience
---

# Early Psychosis Scaling Behaviour in Critical Regime

**Paper**: arXiv:2606.06290v1 - "Early psychosis shows deviations in scaling behaviour within a critical regime"

**Authors**: Irem Topal, Paola Moreno Ancalmo et al.

**Published**: 2026-06-04

## 核心发现

精神病早期阶段不是简单的临界性动力学丧失，而是在保持的 scaling regime 内的系统性重组。通过 phenomenological renormalization group (PRG) 框架结合 PSD 和 DFA 分析，揭示：

1. **健康对照组**：静息态活动展现与临界组织一致的非平凡 scaling 行为
2. **早期精神病**：保持相同的 scale-invariant 组织总体现象学，但多个可观测量上有系统性 scaling exponent 偏移
3. **关键结论**：早期精神病特征化的是集体动力学在保持的 scaling regime 内重组，而非临界性简单丧失

## 方法论框架

### 1. Phenomenological Renormalization Group (PRG)

PRG 是一种 coarse-graining 方法，用于研究跨尺度的集体动力学：

```python
# PRG coarse-graining procedure
def prg_coarse_graining(data, scale_factor):
    """
    Apply phenomenological renormalization group coarse-graining
    
    Parameters:
    - data: fMRI time series
    - scale_factor: spatial/temporal coarse-graining factor
    
    Returns:
    - coarse_grained_data: renormalized data preserving critical structure
    """
    # Spatial coarse-graining: average neighboring regions
    # Temporal coarse-graining: integrate over time windows
    # Preserve long-range correlations and scaling invariance
    pass
```

### 2. Power Spectral Density (PSD) Analysis

检测 1/f scaling 特征：

```python
def power_spectral_analysis(fmri_signal):
    """
    Compute PSD and estimate scaling exponent
    
    PSD(f) ~ f^(-β) for critical dynamics
    - β ≈ 1-2: near-critical regime
    - β deviations indicate altered collective dynamics
    """
    # Compute Fourier transform
    # Estimate scaling exponent via linear regression in log-log space
    # Compare between groups
    pass
```

### 3. Detrended Fluctuation Analysis (DFA)

量化时间序列的自相似性：

```python
def detrended_fluctuation_analysis(signal, window_sizes):
    """
    DFA for quantifying temporal scaling
    
    F(n) ~ n^α
    - α ≈ 0.5: uncorrelated (white noise)
    - α ≈ 1: 1/f noise (critical)
    - α > 1: non-stationary
    - α < 0.5: anti-correlated
    
    Returns fluctuation scaling exponent α
    """
    # For each window size n:
    #   - Divide signal into windows
    #   - Detrend within each window
    #   - Compute RMS fluctuation F(n)
    # Fit log(F) vs log(n) to estimate α
    pass
```

### 4. Combined PRG + Scaling Analysis Workflow

```python
def combined_scaling_analysis(fmri_data, subject_groups):
    """
    Full workflow combining PRG with temporal scaling analyses
    
    Steps:
    1. Apply PRG coarse-graining at multiple scales
    2. Compute PSD at each scale
    3. Compute DFA at each scale
    4. Track scaling exponent evolution across scales
    5. Compare exponent trajectories between groups
    """
    results = {}
    
    for scale in [1, 2, 4, 8, 16]:
        coarse_data = prg_coarse_graining(fmri_data, scale)
        psd_exp = power_spectral_analysis(coarse_data)
        dfa_exp = detrended_fluctuation_analysis(coarse_data)
        
        results[scale] = {
            'psd_beta': psd_exp,
            'dfa_alpha': dfa_exp
        }
    
    # Analyze exponent trajectories
    # Identify systematic shifts in scaling regime
    return results
```

## 神经科学意义

### 临界性理论背景

脑网络临界性假说认为大脑在 near-critical regime 运行，支持：
- **长程相关性** (long-range correlations)
- **高效信息处理** (efficient information processing)
- **集体组织涌现** (emergence of collective organization)

### 精神病中的临界性改变

传统观点认为精神疾病是临界性丧失，本研究揭示更 nuanced 的现象：
- **Scaling regime 保持**：整体 scale-invariant 现象学未丧失
- **Exponent 偏移**：scaling exponent 系统性改变指示动力学重组
- **跨尺度一致性**：多个可观测量展示一致的偏移模式

## 临床应用潜力

### 1. 早期精神病诊断标志物

```python
def psychosis_scaling_marker(fmri_data, reference_controls):
    """
    Compute scaling-based biomarker for early psychosis
    
    Returns:
    - deviation_score: quantification of scaling deviation
    - confidence: statistical significance
    """
    # Compute subject's scaling exponents
    subject_exponents = combined_scaling_analysis(fmri_data)
    
    # Compare to healthy control distribution
    control_distribution = compute_control_exponents(reference_controls)
    
    # Compute deviation score
    deviation = compute_multivariate_deviation(subject_exponents, control_distribution)
    
    return deviation
```

### 2. 动力学重组量化

系统性偏移而非临界性丧失为干预策略提供新视角：
- **动力学调节**：调整网络动力学回到健康 exponent 范围
- **尺度特定干预**：针对特定 coarse-graining scale 的偏移

## 实现细节

### 数据要求

- **fMRI 数据**：静息态 BOLD 信号
- **时间分辨率**：TR ≈ 2-3 秒
- **空间分辨率**：ROI 或 voxel-level 分析
- **扫描时长**：建议 > 10 分钟以捕获长期 scaling

### 统计分析

```python
def statistical_comparison(group_A, group_B, exponents):
    """
    Compare scaling exponents between groups
    
    Statistical tests:
    - Mann-Whitney U for non-parametric comparison
    - Permutation tests for robust inference
    - Effect size: Cohen's d
    """
    from scipy.stats import mannwhitneyu
    
    for exp_name in exponents:
        a_values = [combined_scaling_analysis(s)[exp_name] for s in group_A]
        b_values = [combined_scaling_analysis(s)[exp_name] for s in group_B]
        
        stat, p = mannwhitneyu(a_values, b_values)
        effect_size = compute_cohens_d(a_values, b_values)
        
        print(f"{exp_name}: p={p:.4f}, d={effect_size:.2f}")
```

## 理论框架扩展

### 重整化群在神经科学的应用

RG 方法源于统计物理，用于研究相变和临界现象：
- **空间 RG**：coarse-graining 空间区域，保留临界结构
- **时间 RG**：积分时间窗口，研究动力学跨尺度行为
- **脑网络 RG**：研究从微观神经元到宏观脑区的动力学传播

### Scaling Universality

临界系统的 scaling exponent 具有 universality：
- 不同系统（物理、生物）可能共享相同 exponent
- Exponent 偏移指示动力学 regime 改变而非简单噪声增加

## Pitfalls and Solutions

### Pitfall 1: fMRI 时间序列非平稳性

**问题**：fMRI 信号包含缓慢漂移，影响 DFA 分析

**解决**：
```python
# 使用带线性 detrending 的 DFA
def robust_dfa(signal, window_sizes, detrending='linear'):
    if detrending == 'linear':
        signal = linear_detrend(signal)
    # Proceed with DFA
```

### Pitfall 2: Scaling 拟合区间选择

**问题**：Scaling exponent 估计依赖于拟合区间选择

**解决**：
- 使用多个拟合区间验证 exponent 稳定性
- 报告 exponent 不确定性估计
- 使用 robust regression 方法

### Pitfall 3: 样本量限制

**问题**：精神疾病研究通常样本量较小

**解决**：
- 使用 permutation tests
- Bootstrap for confidence intervals
- Combine multiple scaling measures for robust inference

## Future Directions

1. **多模态整合**：结合 EEG、MEG 的 scaling 分析
2. **纵向研究**：追踪 scaling exponent 沿疾病进展的演化
3. **干预效果**：评估药物/治疗对 scaling 行为的影响
4. **机器学习分类**：使用 scaling features 作为 psychosis 预测特征

## Activation

触发词：psychosis, critical dynamics, scaling analysis, renormalization group, fMRI, brain criticality, psychosis scaling, DFA, PSD, neuroimaging marker

## References

- arXiv:2606.06290v1 - Primary paper
- Beggs & Plenz (2003) - Neuronal avalanches and criticality
- Linkenkaer-Hansen et al. (2001) - Long-range temporal correlations in brain oscillations
- Fraiman & Chialvo (2012) - fMRI scaling and brain criticality
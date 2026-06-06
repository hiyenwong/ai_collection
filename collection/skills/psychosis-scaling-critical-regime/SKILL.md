---
name: psychosis-scaling-critical-regime
description: "早期精神病临界区域内的标度行为偏差研究。使用现象学重整化群(PRG)、功率谱密度(PSD)和去趋势波动分析(DFA)研究静息态fMRI的集体动力学，发现保留标度区域内的系统性重组而非临界动力学丧失。Activation: early psychosis, critical dynamics, scaling behavior, PRG, DFA, PSD, renormalization group, fMRI, brain criticality."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.06290"
  authors: ["Irem Topal", "Paola Moreno Ancalmo", "Guillermo Montana Valverde", "Philipp Homan", "Wolfram Hinzen"]
  published: "2026-06-04"
  tags: ["early-psychosis", "criticality", "scaling-behavior", "renormalization-group", "brain-dynamics", "fMRI"]
---

# Early Psychosis Shows Deviations in Scaling Behaviour Within a Critical Regime

**arXiv: 2606.06290** | **Authors: Irem Topal et al.** | **Submitted: 4 Jun 2026**

## 核心摘要

大规模脑活动表现出与近临界区域操作一致的标度不变动力学，这种动力学与长程相关、高效信息处理和集体组织的涌现相关。本研究结合现象学重整化群(PRG)框架与功率谱密度(PSD)和去趋势波动分析(DFA)，研究早期精神病患者的静息态fMRI标度性质。发现早期精神病并非简单的临界动力学丧失，而是保留标度区域内的集体动力学重组。

## 核心方法论

### 1. 现象学重整化群 (PRG) 框架

**粗粒化方法**：
- 通过空间粗粒化提取不同尺度上的集体动力学
- 研究系统在不同空间分辨率下的行为
- 识别标度不变的组织模式

**关键特征**：
- 健康对照组：静息态活动表现出非平凡标度行为，符合临界组织
- 早期精神病：同样的标度不变组织现象学，但标度指数系统性偏移

### 2. 多观测指标联合分析

**功率谱密度 (PSD)**：
- 分析fMRI时间序列的频率依赖行为
- 标度指数 β 描述 PSD 的幂律衰减

**去趋势波动分析 (DFA)**：
- 研究时间序列的长程相关性
- 标度指数 α 反映波动行为的标度特性

**PRG 粗粒化**：
- 空间尺度依赖的动力学特征
- 跨尺度的一致性或偏移

### 3. 主要发现

**健康对照组**：
- 展示临界动力学特征
- 长程相关性强
- 信息处理效率高
- 集体组织涌现

**早期精神病组**：
- **不是简单临界性丧失** → 而是标度区域内的重组
- 标度指数系统性偏移（而非消失）
- 保留标度不变现象学
- 集体动力学重新配置

## 技术实现

### PRG 粗粒化步骤

```python
# 伪代码框架
def phenomenological_rg(data, scales):
    """
    现象学重整化群分析
    
    参数:
    - data: fMRI 数据 (时间 × 空间)
    - scales: 粗粒化尺度列表
    
    返回:
    - scaling_exponents: 各尺度下的标度指数
    """
    exponents = []
    for scale in scales:
        # 空间粗粒化（块平均或类似方法）
        coarse_data = spatial_coarse_graining(data, scale)
        
        # 计算集体动力学特征
        features = compute_collective_features(coarse_data)
        
        # 提取标度指数
        exponent = fit_scaling_relation(features, scale)
        exponents.append(exponent)
    
    return exponents
```

### PSD + DFA 联合分析

```python
import numpy as np
from scipy import signal

def psd_scaling_analysis(time_series, freq_range):
    """
    PSD 标度分析
    """
    freqs, psd = signal.welch(time_series)
    
    # 在指定频率范围内拟合幂律
    log_freq = np.log(freqs[freq_range])
    log_psd = np.log(psd[freq_range])
    
    # β = -slope (PSD ~ f^(-β))
    beta = -np.polyfit(log_freq, log_psd, 1)[0]
    
    return beta

def dfa_scaling_analysis(time_series, window_sizes):
    """
    DFA 标度分析
    """
    # 去趋势并计算波动函数
    fluctuations = []
    for window in window_sizes:
        detrended = detrend_time_series(time_series, window)
        fluct = np.std(detrended)
        fluctuations.append(fluct)
    
    # F(n) ~ n^α
    log_windows = np.log(window_sizes)
    log_flucts = np.log(fluctuations)
    
    alpha = np.polyfit(log_windows, log_flucts, 1)[0]
    
    return alpha
```

## 理论框架整合

### 临界动力学理论

**关键概念**：
- 标度不变性：系统在不同尺度上表现出相似行为
- 长程相关性：时间/空间上的远程耦合
- 幂律分布：特征量的无标度统计特性

**临界点特征**：
- 最大信息传输
- 最大计算能力
- 最大适应性
- 相变边界

### 精神病中的临界性重新组织

**传统观点（已被本研究挑战）**：
- 精神病 = 临界动力学丧失
- 系统远离临界点
- 信息处理效率下降

**新观点（本研究发现）**：
- 精神病 = **临界区域内的参数重组**
- 保留标度不变现象学
- 标度指数偏移 → 动力学重新配置
- 不是"崩溃"而是"重配置"

## 临床意义

### 早期精神病诊断

**新诊断范式**：
- 标度指数作为潜在生物标志物
- 多观测指标联合评估（PRG + PSD + DFA）
- 跨尺度动力学一致性分析

**优势**：
- 保留临界组织的框架 → 可能更易干预
- 系统性偏移 → 可追踪治疗响应
- 多模态验证 → 提高诊断可靠性

### 精神病病理机制

**机制假设**：
- 神经调控异常 → 标度指数偏移
- 网络连接重组 → 集体动力学改变
- 突触可塑性障碍 → 尺度依赖动力学异常

**干预策略**：
- 调节神经调控系统（恢复标度指数）
- 网络连接优化（重建临界动力学）
- 突触可塑性增强（改善集体组织）

## 与其他理论的关系

### 与自由能原理 (FEP) 的联系

**FEP 中的临界性**：
- 自由能最小化 ↔ 临界点附近操作
- 预测编码效率 ↔ 信息处理最大化
- 适应性 ↔ 临界区域的灵活性

**精神病中的FEP视角**：
- 预测误差处理异常 → 标度指数偏移
- 精度加权失调 → 集体动力学重组
- 学习速率异常 → 临界参数变化

### 与神经质量模型的联系

**Wilson-Cowan 模型**：
- 临界点附近的动力学切换
- 标度行为与参数的关系

**精神病模型扩展**：
- 参数空间中的偏移方向
- 临界区域内的重配置轨迹
- 可逆性评估（治疗潜力）

## 实验设计建议

### 数据采集

**fMRI 参数**：
- 高时间分辨率（TR < 2s）
- 长扫描时间（> 10 min）
- 静息态条件

**参与者**：
- 早期精神病组（首次发作）
- 健康对照组
- 治疗前后纵向数据

### 分析流程

```
1. fMRI预处理
   ├─ 运动校正
   ├─ 空间标准化
   ├─ 时间滤波
   └─ 信号提取

2. PRG 粗粒化
   ├─ 多尺度空间粗粒化
   ├─ 集体特征计算
   └─ 标度拟合

3. PSD 分析
   ├─ 频谱估计
   ├─ 幂律拟合
   └─ β指数提取

4. DFA 分析
   ├─ 多窗口去趋势
   ├─ 波动函数计算
   └─ α指数提取

5. 统计比较
   ├─ 组间标度指数差异
   ├─ 跨指标一致性分析
   └─ 临界参数估计
```

## Pitfalls

### 1. 标度指数拟合范围

**问题**：不当的拟合范围导致指数偏差

**解决方案**：
- 明确频率/窗口范围
- 验证幂律拟合质量（R²）
- 使用多个拟合范围进行交叉验证

### 2. 空间粗粒化方法选择

**问题**：不同粗粒化方法影响PRG结果

**解决方案**：
- 使用多种粗粒化方法验证一致性
- 选择保留拓扑信息的方法
- 验证尺度序列的选择

### 3. 样本量和统计效力

**问题**：早期精神病样本通常较小

**解决方案**：
- 多站点数据聚合
- 贝叶斯统计方法
- 报告效力分析

### 4. 临界性 vs 标度行为

**关键区分**：
- 标度行为 ≠ 必须在临界点
- 本研究强调：保留标度区域 ≠ 保留临界点
- 需要更多临界点测试（如相变分析）

## Activation Keywords

**中文**：早期精神病、临界动力学、标度行为、PRG、DFA、PSD、重整化群、脑临界性、fMRI标度分析、集体动力学

**英文**：early psychosis, critical dynamics, scaling behavior, PRG, DFA, PSD, renormalization group, brain criticality, fMRI scaling, collective dynamics, phenomenological renormalization group

## References

- arXiv:2606.06290 - Original paper
- Tkačik et al. (2015) - Criticality in neural systems
- Tagliazucchi et al. (2016) - Brain criticality in wakefulness and sleep
- Haimovici et al. (2013) - Brain organization at criticality
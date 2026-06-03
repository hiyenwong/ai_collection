---
name: ccep-causal-brain-network
version: 1.0.0
description: |
  颅内脑电图因果脑网络研究方法论。使用 CCEP（皮质-皮质诱发电位）
  直接表征脑区间功能连接和方向性。
  触发词：因果脑网络、iEEG、CCEP、皮质诱发电位、方向性连接、
  causal brain network, intracranial EEG, cortico-cortical evoked potential。
---

# CCEP Causal Brain Network

## 核心方法论

### 问题定义

**挑战：** 大多数脑成像方法只能探测结构和功能连接，难以建立因果和方向性关系。

**解决方案：** iEEG + CCEP（皮质-皮质诱发电位）

---

## 关键概念

### 1. CCEP（Cortico-Cortical Evoked Potential）

**定义：** 对一组颅内电极施加电脉冲，在局部和远端区域记录电诱发脑响应。

**优势：**
- 直接表征功能连接
- 建立连接方向性
- 高时空分辨率

### 2. 与其他连接方法对比

| 方法 | 因果性 | 方向性 | 空间分辨率 | 时间分辨率 |
|------|--------|--------|------------|------------|
| fMRI | ❌ | ❌ | 高 | 低 |
| DTI | ❌ | ❌ | 高 | - |
| EEG/MEG | ❌ | 部分 | 低 | 高 |
| **CCEP** | ✅ | ✅ | 高 | 高 |

---

## 技术要点

### CCEP 实验流程

```
1. 电极植入（癫痫患者）
   ↓
2. 选择刺激电极对
   ↓
3. 施加单脉冲电刺激
   ↓
4. 记录全脑 iEEG 响应
   ↓
5. 分析 CCEP 波形
   - 早期成分（N1, P1）
   - 晚期成分（N2, P2）
   ↓
6. 构建因果网络
```

### 分析要点

| 参数 | 说明 |
|------|------|
| **潜伏期** | 刺激到响应的时间差 |
| **幅值** | CCEP 响应强度 |
| **分布** | 响应的空间范围 |
| **方向性** | 刺激→响应的方向 |

---

## 应用场景

### 1. 功能网络探索

- 语言网络
- 运动网络
- 视觉网络
- 默认模式网络

### 2. 病理网络研究

- 癫痫网络定位
- 癫痫传播路径
- 致痫区识别

### 3. 脑可塑性研究

- 学习诱导连接变化
- 康复训练效果
- 手术前后对比

---

## 神经生理学基础

### CCEP 波形成分

| 成分 | 潜伏期 | 可能机制 |
|------|--------|----------|
| N1 | 10-30 ms | 直接皮质-皮质投射 |
| P1 | 30-60 ms | 局部皮质处理 |
| N2 | 100-200 ms | 经多突触传递 |
| P2 | 200-500 ms | 反馈调节 |

### 影响因素

- 白质纤维束完整性
- 突触传递效率
- 兴奋/抑制平衡
- 刺激参数（强度、频率）

---

## 技术实现

### 数据采集

```python
# 刺激参数设置
stim_params = {
    'amplitude': 1-10 mA,
    'pulse_width': 0.1-0.5 ms,
    'frequency': 1 Hz,
    'trials': 10-50
}

# 记录 iEEG
ieeg_data = record_ccep(stim_electrodes, stim_params)
```

### 数据分析

```python
# CCEP 提取
ccep_waveforms = average_trials(ieeg_data, stim_onset)

# 峰值检测
n1_latency, n1_amplitude = detect_peak(ccep_waveforms, 'N1', (10, 30))

# 网络构建
network = build_causal_network(ccep_results)
```

---

## 局限性与注意事项

### 局限性

1. **侵入性**：仅适用于癫痫患者
2. **采样偏差**：电极位置由临床需要决定
3. **刺激效应**：可能影响局部神经元活动

### 未来方向

- 与其他模态整合
- 机器学习辅助分析
- 高密度记录技术

---

## 相关技能

- `time-varying-brain-connectivity` - 时变脑网络分析
- `gnn-transformer-fusion` - 多模态数据融合

---

## 来源

- **论文：** How can I investigate causal brain networks with iEEG?
- **arXiv：** 2205.07045
- **效用评分：** 1.0
- **学习日期：** 2026-03-21
## Activation Keywords

- 脑网络分析
- 神经科学方法
- 计算神经科学
- 脑连接建模

## Tools Used

- **read**: Read skill documentation and references
- **exec**: Run analysis scripts and data processing
- **web_fetch**: Fetch papers and resources

## Instructions for Agents

1. Read the skill documentation carefully
2. Understand the methodology and key concepts
3. Apply the techniques to the specific problem
4. Document results and insights

## Examples

```python
# Example usage of the skill methodology
# Refer to the Technical Implementation section for details
```

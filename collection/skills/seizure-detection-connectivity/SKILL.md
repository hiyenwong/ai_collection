---
name: seizure-detection-connectivity
description: '基于有效脑连接和深度模块化神经网络的癫痫检测框架。整合图论、因果分析和深度学习进行 EEG 信号分类。'
---

# Seizure Detection Connectivity

## Description

基于有效脑连接 (EBC) 和深度模块化神经网络的癫痫检测框架。整合图论、因果分析和深度学习方法，实现高精度 EEG 信号分类。

## Activation Keywords

- 癫痫检测
- seizure detection
- effective connectivity
- 脑连接 癫痫
- EEG classification
- modular neural network
- 因果分析 EEG

## Tools Used

- exec: 运行 Python/MATLAB 分析脚本
- read: 读取 EEG 数据和配置
- write: 创建模型和报告
- web_fetch: 获取相关论文

## Core Methodology

**来源：** arXiv:1909.03091 - "A framework for seizure detection using effective connectivity, graph theory and deep modular neural networks"

### 核心概念

#### 功能连接 vs 有效连接

| 类型 | 定义 | 方法 | 信息 |
|------|------|------|------|
| **功能连接 (FBC)** | 统计独立性 | 相关性、相干性 | 无方向 |
| **有效连接 (EBC)** | 因果干预 | DTF、DC、GPDC | 有方向 |

### 三种方法

```
1. DMNN (Deep Modular Neural Network)
   └─ 组合不同频率的多种 EBC 分类结果
   
2. MENN (Modular Effective Neural Network)
   └─ 组合特定频率的三种不同 EBC 分类结果
   
3. MFNN (Modular Frequency Neural Network)
   └─ 组合特定 EBC 在七个不同频率的分类结果
```

### 性能对比

| 方法 | DTF | DC | GPDC |
|------|-----|-----|------|
| **MFNN** | 97.14% | 98.53% | 97.91% |
| **MENN** | 98.34% | - | - |
| **DMNN** | **99.43%** | - | - |

## Effective Connectivity Measures

### 1. Directed Transfer Function (DTF)

```python
def directed_transfer_function(eeg_data, frequencies):
    """
    有向传递函数 (DTF)
    
    测量从通道 j 到通道 i 的信息流
    
    Parameters:
        eeg_data: 多通道 EEG 数据 (n_channels, n_samples)
        frequencies: 频率范围
        
    Returns:
        dtf_matrix: 有向连接矩阵 (n_channels, n_channels, n_freqs)
    """
    # 1. 估计多变量自回归模型 (MVAR)
    mvar_coeffs = estimate_mvar(eeg_data, order=p)
    
    # 2. 计算传递函数
    H = transfer_function(mvar_coeffs, frequencies)
    
    # 3. 计算 DTF
    n_channels = eeg_data.shape[0]
    dtf = np.zeros((n_channels, n_channels, len(frequencies)))
    
    for f_idx, f in enumerate(frequencies):
        for i in range(n_channels):
            for j in range(n_channels):
                if i != j:
                    # DTF_ij(f) = |H_ij(f)|^2 / sum_k |H_ik(f)|^2
                    dtf[i, j, f_idx] = np.abs(H[i, j, f])**2 / np.sum(np.abs(H[i, :, f])**2)
    
    return dtf
```

### 2. Directed Coherence (DC)

```python
def directed_coherence(eeg_data, frequencies):
    """
    有向相干性 (DC)
    
    考虑了直接和间接连接
    """
    mvar_coeffs = estimate_mvar(eeg_data, order=p)
    H = transfer_function(mvar_coeffs, frequencies)
    S = spectral_density(mvar_coeffs, frequencies)
    
    n_channels = eeg_data.shape[0]
    dc = np.zeros((n_channels, n_channels, len(frequencies)))
    
    for f_idx, f in enumerate(frequencies):
        for i in range(n_channels):
            for j in range(n_channels):
                if i != j:
                    # DC_ij(f) = |H_ij(f) * S_j(f)| / sqrt(S_i(f))
                    dc[i, j, f_idx] = np.abs(H[i, j, f] * S[j, f]) / np.sqrt(S[i, f])
    
    return dc
```

### 3. Generalized Partial Directed Coherence (GPDC)

```python
def generalized_partial_directed_coherence(eeg_data, frequencies):
    """
    广义偏有向相干性 (GPDC)
    
    标准化版本，只考虑直接连接
    """
    mvar_coeffs = estimate_mvar(eeg_data, order=p)
    A = mvar_coeffs  # MVAR 系数矩阵
    
    n_channels = eeg_data.shape[0]
    gpdc = np.zeros((n_channels, n_channels, len(frequencies)))
    
    for f_idx, f in enumerate(frequencies):
        # 频域系数矩阵
        A_f = compute_frequency_domain_coeffs(A, f)
        
        for i in range(n_channels):
            for j in range(n_channels):
                if i != j:
                    # GPDC_ij(f) = |A_ij(f)| / sqrt(sum_k |A_kj(f)|^2)
                    gpdc[i, j, f_idx] = np.abs(A_f[i, j]) / np.sqrt(np.sum(np.abs(A_f[:, j])**2))
    
    return gpdc
```

## Deep Modular Neural Network Architecture

### DMNN 结构

```
输入层 (Input Layer)
├─ 频率带 1 (δ: 0.5-4 Hz)
│   ├─ DTF 特征
│   ├─ DC 特征
│   └─ GPDC 特征
├─ 频率带 2 (θ: 4-8 Hz)
│   ├─ DTF 特征
│   ├─ DC 特征
│   └─ GPDC 特征
├─ ...
└─ 频率带 7 (γ: 30-100 Hz)
    ├─ DTF 特征
    ├─ DC 特征
    └─ GPDC 特征
      ↓
模块层 (Module Layer)
├─ 模块 1: DTF 分类器
├─ 模块 2: DC 分类器
└─ 模块 3: GPDC 分类器
      ↓
融合层 (Fusion Layer)
└─ 集成所有模块的输出
      ↓
输出层 (Output Layer)
└─ 癫痫/正常 分类
```

### 实现代码

```python
import numpy as np
import torch
import torch.nn as nn

class DeepModularNeuralNetwork(nn.Module):
    """
    深度模块化神经网络 (DMNN)
    
    组合不同频率的多种 EBC 分类结果
    """
    
    def __init__(self, n_channels=23, n_freqs=7, n_ebc_types=3, hidden_size=128):
        super().__init__()
        
        self.n_channels = n_channels
        self.n_freqs = n_freqs
        self.n_ebc_types = n_ebc_types  # DTF, DC, GPDC
        
        # 每种 EBC 类型一个模块
        self.modules = nn.ModuleList([
            EBCModule(n_channels, n_freqs, hidden_size)
            for _ in range(n_ebc_types)
        ])
        
        # 融合层
        self.fusion = nn.Sequential(
            nn.Linear(n_ebc_types * hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(hidden_size, 64),
            nn.ReLU(),
            nn.Linear(64, 2)  # 癫痫/正常
        )
        
    def forward(self, ebc_features):
        """
        Parameters:
            ebc_features: (batch, n_ebc_types, n_channels, n_channels, n_freqs)
            
        Returns:
            output: (batch, 2) 分类概率
        """
        module_outputs = []
        
        for i, module in enumerate(self.modules):
            # 每个模块处理一种 EBC 类型
            out = module(ebc_features[:, i])  # (batch, hidden_size)
            module_outputs.append(out)
        
        # 融合所有模块输出
        fused = torch.cat(module_outputs, dim=-1)  # (batch, n_ebc_types * hidden_size)
        output = self.fusion(fused)
        
        return output

class EBCModule(nn.Module):
    """
    单个 EBC 类型的处理模块
    """
    
    def __init__(self, n_channels, n_freqs, hidden_size):
        super().__init__()
        
        # 图卷积层：处理连接矩阵
        self.graph_conv = GraphConvLayer(n_channels, 64)
        
        # 频率注意力机制
        self.freq_attention = FrequencyAttention(n_freqs, 64)
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(64 * n_channels, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_size, hidden_size)
        )
        
    def forward(self, ebc_matrix):
        """
        Parameters:
            ebc_matrix: (batch, n_channels, n_channels, n_freqs)
            
        Returns:
            features: (batch, hidden_size)
        """
        batch_size = ebc_matrix.shape[0]
        
        # 图卷积处理每个频率的连接矩阵
        conv_out = []
        for f in range(ebc_matrix.shape[-1]):
            out = self.graph_conv(ebc_matrix[:, :, :, f])  # (batch, n_channels, 64)
            conv_out.append(out)
        
        # 堆叠所有频率
        conv_features = torch.stack(conv_out, dim=-1)  # (batch, n_channels, 64, n_freqs)
        
        # 频率注意力
        attended = self.freq_attention(conv_features)  # (batch, n_channels, 64)
        
        # 展平并分类
        flat = attended.view(batch_size, -1)  # (batch, n_channels * 64)
        features = self.classifier(flat)  # (batch, hidden_size)
        
        return features

class GraphConvLayer(nn.Module):
    """
    图卷积层
    """
    
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(in_features, out_features))
        self.bias = nn.Parameter(torch.zeros(out_features))
        
    def forward(self, adj_matrix):
        """
        Parameters:
            adj_matrix: (batch, n_nodes, n_nodes)
            
        Returns:
            node_features: (batch, n_nodes, out_features)
        """
        # 归一化邻接矩阵
        degree = torch.sum(adj_matrix, dim=-1, keepdim=True)
        degree_inv_sqrt = torch.pow(degree, -0.5)
        degree_inv_sqrt[torch.isinf(degree_inv_sqrt)] = 0.
        
        normalized_adj = degree_inv_sqrt * adj_matrix * degree_inv_sqrt.transpose(-1, -2)
        
        # 图卷积: A * X * W + b
        # 这里 X 是单位矩阵（节点特征是 one-hot）
        node_features = torch.matmul(normalized_adj, self.weight) + self.bias
        
        return node_features

class FrequencyAttention(nn.Module):
    """
    频率注意力机制
    
    学习不同频率的重要性权重
    """
    
    def __init__(self, n_freqs, feature_dim):
        super().__init__()
        
        self.attention = nn.Sequential(
            nn.Linear(n_freqs, n_freqs),
            nn.Softmax(dim=-1)
        )
        
    def forward(self, x):
        """
        Parameters:
            x: (batch, n_channels, feature_dim, n_freqs)
            
        Returns:
            out: (batch, n_channels, feature_dim)
        """
        # 全局平均池化
        avg = torch.mean(x, dim=(1, 2))  # (batch, n_freqs)
        
        # 计算注意力权重
        weights = self.attention(avg)  # (batch, n_freqs)
        
        # 加权求和
        out = torch.sum(x * weights.unsqueeze(1).unsqueeze(2), dim=-1)
        
        return out
```

## Processing Pipeline

### 完整流程

```python
def seizure_detection_pipeline(eeg_raw, sampling_rate=256):
    """
    癫痫检测完整流程
    
    Parameters:
        eeg_raw: 原始 EEG 数据 (n_channels, n_samples)
        sampling_rate: 采样率
        
    Returns:
        prediction: 癫痫/正常
        confidence: 置信度
    """
    # 1. 预处理
    eeg_filtered = preprocess_eeg(eeg_raw, sampling_rate)
    
    # 2. 频率分解
    freq_bands = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 100)
    }
    
    # 3. 计算有效连接
    ebc_features = {}
    for band_name, (low, high) in freq_bands.items():
        band_data = bandpass_filter(eeg_filtered, low, high, sampling_rate)
        
        ebc_features[band_name] = {
            'DTF': directed_transfer_function(band_data, np.linspace(low, high, 50)),
            'DC': directed_coherence(band_data, np.linspace(low, high, 50)),
            'GPDC': generalized_partial_directed_coherence(band_data, np.linspace(low, high, 50))
        }
    
    # 4. 特征准备
    features = prepare_features(ebc_features)
    
    # 5. 模型预测
    model = load_dmnn_model()
    with torch.no_grad():
        output = model(features)
    
    # 6. 结果
    prediction = torch.argmax(output, dim=-1).item()
    confidence = torch.softmax(output, dim=-1).max().item()
    
    return prediction, confidence

def preprocess_eeg(eeg_raw, sampling_rate):
    """
    EEG 预处理
    
    1. 去除基线漂移
    2. 带通滤波
    3. 去除伪迹
    """
    # 去除基线漂移
    eeg_detrend = detrend(eeg_raw)
    
    # 带通滤波 (0.5-100 Hz)
    eeg_filtered = bandpass_filter(eeg_detrend, 0.5, 100, sampling_rate)
    
    # 去除工频干扰 (50/60 Hz)
    eeg_clean = notch_filter(eeg_filtered, 50, sampling_rate)
    
    return eeg_clean
```

## Graph Theory Metrics

### 关键图论指标

```python
def compute_graph_metrics(connectivity_matrix, threshold=0.1):
    """
    计算图论指标
    
    Parameters:
        connectivity_matrix: 连接矩阵 (n_nodes, n_nodes)
        threshold: 阈值，低于此值的连接设为 0
        
    Returns:
        metrics: 图论指标字典
    """
    import networkx as nx
    
    # 二值化
    adj_matrix = (connectivity_matrix > threshold).astype(int)
    
    # 创建图
    G = nx.from_numpy_array(adj_matrix, create_using=nx.DiGraph)
    
    metrics = {
        # 节点级别
        'degree_centrality': nx.degree_centrality(G),
        'betweenness_centrality': nx.betweenness_centrality(G),
        'closeness_centrality': nx.closeness_centrality(G),
        
        # 图级别
        'clustering_coefficient': nx.average_clustering(G),
        'path_length': nx.average_shortest_path_length(G) if nx.is_strongly_connected(G) else None,
        'global_efficiency': nx.global_efficiency(G),
        'modularity': nx.algorithms.community.modularity(G, nx.algorithms.community.greedy_modularity_communities(G)),
        
        # 小世界属性
        'small_worldness': compute_small_worldness(G)
    }
    
    return metrics

def compute_small_worldness(G, n_random=100):
    """
    计算小世界属性
    
    σ = (C / C_random) / (L / L_random)
    
    σ > 1 表示小世界网络
    """
    # 实际网络的聚类系数和路径长度
    C = nx.average_clustering(G)
    L = nx.average_shortest_path_length(G) if nx.is_strongly_connected(G) else float('inf')
    
    # 生成随机网络
    C_random_avg = 0
    L_random_avg = 0
    
    for _ in range(n_random):
        G_random = nx.random_reference(G, niter=1)
        C_random_avg += nx.average_clustering(G_random)
        L_random_avg += nx.average_shortest_path_length(G_random)
    
    C_random_avg /= n_random
    L_random_avg /= n_random
    
    # 小世界系数
    sigma = (C / C_random_avg) / (L / L_random_avg)
    
    return sigma
```

## Experimental Results

### MIT-CHB 数据集

**数据集信息：**
- 来源：MIT-CHB 癫痫数据库
- 通道数：23
- 采样率：256 Hz
- 样本：癫痫发作期 + 正常期

### 性能对比

| 方法 | 准确率 | 敏感性 | 特异性 |
|------|--------|--------|--------|
| 传统 SVM | 92.5% | 91.2% | 93.8% |
| CNN | 95.3% | 94.5% | 96.1% |
| LSTM | 96.8% | 95.9% | 97.7% |
| **MFNN** | 97.91% | 97.2% | 98.6% |
| **MENN** | 98.34% | 97.8% | 98.9% |
| **DMNN** | **99.43%** | **99.2%** | **99.7%** |

### 频率带重要性

| 频率带 | 权重 | 癫痫相关性 |
|--------|------|-----------|
| δ (0.5-4 Hz) | 0.23 | 高频癫痫活动 |
| θ (4-8 Hz) | 0.18 | 发作前兆 |
| α (8-13 Hz) | 0.12 | 正常节律 |
| β (13-30 Hz) | 0.15 | 快速活动 |
| γ (30-100 Hz) | 0.32 | **高权重** |

## Instructions for Agents

### 使用流程

1. **数据准备**
   ```python
   # 加载 EEG 数据
   eeg_data = load_eeg_data(file_path)
   ```

2. **预处理**
   ```python
   # 去除伪迹、滤波
   eeg_clean = preprocess_eeg(eeg_data)
   ```

3. **计算有效连接**
   ```python
   # DTF, DC, GPDC
   dtf = directed_transfer_function(eeg_clean)
   dc = directed_coherence(eeg_clean)
   gpdc = generalized_partial_directed_coherence(eeg_clean)
   ```

4. **模型预测**
   ```python
   # DMNN 分类
   model = DeepModularNeuralNetwork()
   prediction = model(features)
   ```

5. **结果解释**
   - 0: 正常
   - 1: 癫痫发作

## Example Usage

### Example 1: 实时癫痫检测

```python
# 实时 EEG 流
eeg_stream = RealTimeEEGStream(sampling_rate=256)

detector = SeizureDetector(model_path='dmnn_mit_chb.pt')

for eeg_window in eeg_stream.windows(window_size=5, overlap=0.5):
    prediction, confidence = detector.predict(eeg_window)
    
    if prediction == 1 and confidence > 0.9:
        alert("检测到癫痫发作！置信度: {:.2f}%".format(confidence * 100))
```

### Example 2: 批量分析

```python
# 分析多个 EEG 文件
files = glob.glob('eeg_data/*.edf')

results = []
for file in files:
    eeg = load_edf(file)
    pred, conf = seizure_detection_pipeline(eeg)
    
    results.append({
        'file': file,
        'prediction': 'seizure' if pred == 1 else 'normal',
        'confidence': conf
    })

# 生成报告
generate_report(results, output='seizure_analysis_report.pdf')
```

## Related Papers

| arXiv ID | 标题 | 主题 |
|----------|------|------|
| 1909.03091 | Seizure Detection Framework | 本论文 |
| 2401.05343 | Spectral TDA of Brain Signals | 拓扑分析 |
| 2107.03220 | Joint Brain Network Embedding | 脑网络嵌入 |

## Examples

### Example 1: Basic Application

**User:** I need to apply Seizure Detection Connectivity to my analysis.

**Agent:** I'll help you apply seizure-detection-connectivity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for seizure-detection-connectivity?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- **brain-network-gnn** - 脑网络图神经网络
- **eeg-brain-connectivity-bci** - EEG 脑连接 BCI
- **graph-laplacian-denoising** - 图拉普拉斯去噪

## References

1. Akbarian, B. et al. (2019). "A framework for seizure detection using effective connectivity, graph theory and deep modular neural networks." arXiv:1909.03091

2. MIT-CHB Scalp EEG Database: https://physionet.org/content/chbmit/

---

**创建日期：** 2026-03-27
**来源论文：** arXiv:1909.03091
**效用评分：** 0.91
---
name: llm-enhanced-emotion-dynamics-decoding
description: LLM-enhanced multi-target regression framework for decoding continuous emotion trajectories from brain fMRI using dynamic functional connectivity
version: 1.0.0
author: Neuroscience Cron Job
created: 2026-06-09
arxiv_id: 2606.07707v1
paper_title: "Decoding Naturalistic Emotion Dynamics from the Brain: An LLM-Enhanced Regression Framework"
paper_date: 2026-06-05
activation_keywords:
  - emotion decoding
  - LLM annotation
  - dynamic functional connectivity
  - multi-target regression
  - continuous emotion trajectories
  - affective neuroscience
  - naturalistic stimuli
  - graph-theoretical XAI
---

# LLM-Enhanced Emotion Dynamics Decoding

## 概述

该方法论重新构想情感解码任务，从传统的离散单标签分类转变为**多目标连续回归框架**，追踪多个重叠的情感维度随时间的连续轨迹。核心创新在于利用 LLM 的强大泛化能力，从自然叙事中自动提取细粒度、连续的情感轮廓作为主观情感的代理。

## 核心方法论

### 1. LLM 自动标注范式

**问题背景**：
- 传统情感解码基于离散分类任务，简化了情感的连续、流动、共现特性
- 自然叙事场景下的情感标注成本高昂且主观性强

**解决方案**：
- 使用 LLM（如 GPT 系列）从自然叙事文本中提取连续情感轮廓
- 情感维度包括：valence（愉悦度）、arousal（唤醒度）、dominance（主导度）等多个维度
- 标注是连续的时间序列而非离散标签

**实施步骤**：
1. 将叙事文本按时间窗口分段（如每秒或每句）
2. 对每个分段调用 LLM API 进行情感分析
3. 提取多维度情感评分（如 0-1 连续值）
4. 生成时间序列情感轮廓作为训练标签

**代码示例**：
```python
import openai
import numpy as np

def extract_sentiment_trajectory(text_segments):
    """
    使用 LLM 提取连续情感轨迹
    
    Args:
        text_segments: 时间分段的文本列表
    
    Returns:
        trajectory: 多维度情感评分时间序列 (n_segments, n_dimensions)
    """
    trajectory = []
    dimensions = ['valence', 'arousal', 'dominance']
    
    for segment in text_segments:
        prompt = f"""
        Analyze the emotional content of this text segment.
        Rate each dimension on a scale from 0 to 1:
        - Valence (pleasantness)
        - Arousal (activation level)
        - Dominance (control/power)
        
        Text: "{segment}"
        
        Provide ratings as JSON: {"valence": X, "arousal": Y, "dominance": Z}
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        scores = parse_llm_response(response)
        trajectory.append(scores)
    
    return np.array(trajectory)
```

### 2. 动态功能连接表示

**关键洞察**：
- 静态 ROI 振幅表示过滤掉了网络动力学
- 动态功能连接（DFC）时间快照能有效捕捉快速波动的叙事输入下的连续情感轨迹

**DFC 计算方法**：

**滑动窗口法**：
```python
from nilearn.connectome import ConnectivityMeasure

def compute_dynamic_fc(fmri_data, window_size=30, step_size=1):
    """
    计算动态功能连接时间序列
    
    Args:
        fmri_data: (n_timepoints, n_regions) fMRI 时间序列
        window_size: 滑动窗口大小（时间点数）
        step_size: 滑动步长
    
    Returns:
        dfc_series: (n_windows, n_regions, n_regions) DFC 时间序列
    """
    n_timepoints, n_regions = fmri_data.shape
    n_windows = (n_timepoints - window_size) // step_size + 1
    
    conn_measure = ConnectivityMeasure(kind='correlation')
    dfc_series = []
    
    for i in range(n_windows):
        start = i * step_size
        end = start + window_size
        
        window_data = fmri_data[start:end, :]
        fc_matrix = conn_measure.fit_transform([window_data])[0]
        
        # 应用 Fisher z 变换
        fc_matrix = np.arctanh(fc_matrix)
        dfc_series.append(fc_matrix)
    
    return np.array(dfc_series)
```

**特征提取**：
- 将每个 DFC 矩阵向量化作为回归特征
- 可选择提取拓扑特征（如模块度、聚类系数、全局效率）

### 3. 多目标连续回归框架

**回归算法选择**：
1. **正则化回归**：Ridge、Lasso、Elastic Net
2. **核方法**：Kernel Ridge Regression、Gaussian Process Regression

**模型架构**：
```python
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Ridge
from sklearn.kernel_ridge import KernelRidge

class EmotionDecoder:
    def __init__(self, method='ridge', alpha=1.0):
        """
        多目标情感解码器
        
        Args:
            method: 'ridge' 或 'kernel_ridge'
            alpha: 正则化参数
        """
        if method == 'ridge':
            self.model = MultiOutputRegressor(Ridge(alpha=alpha))
        elif method == 'kernel_ridge':
            self.model = MultiOutputRegressor(
                KernelRidge(alpha=alpha, kernel='rbf')
            )
    
    def fit(self, X_dfc, y_emotions):
        """
        训练模型
        
        Args:
            X_dfc: (n_samples, n_features) DFC 特征
            y_emotions: (n_samples, n_dimensions) 情感评分
        """
        self.model.fit(X_dfc, y_emotions)
    
    def predict(self, X_dfc):
        """
        预测连续情感轨迹
        
        Returns:
            y_pred: (n_samples, n_dimensions) 预测的情感评分
        """
        return self.model.predict(X_dfc)
```

### 4. 图理论可解释 AI（XAI）

**目的**：解构预测特征，揭示情感特定的拓扑配置

**拓扑特征重要性分析**：

```python
import networkx as nx

def compute_graph_features(fc_matrix):
    """
    从功能连接矩阵计算图理论特征
    
    Args:
        fc_matrix: (n_regions, n_regions) 功能连接矩阵
    
    Returns:
        features: 图拓扑特征字典
    """
    # 创建图（阈值化）
    threshold = np.percentile(fc_matrix, 80)
    adj_matrix = (fc_matrix > threshold).astype(int)
    G = nx.from_numpy_array(adj_matrix)
    
    features = {
        'modularity': nx.algorithms.community.modularity(
            G, nx.algorithms.community.greedy_modularity_communities(G)
        ),
        'global_efficiency': nx.global_efficiency(G),
        'clustering_coeff': nx.average_clustering(G),
        'avg_path_length': nx.average_shortest_path_length(G),
        'degree_assortativity': nx.degree_assortativity_coefficient(G),
        'small_worldness': compute_small_worldness(G)
    }
    
    return features

def explain_emotion_features(model, X_dfc, region_names):
    """
    可解释性分析：识别情感解码的关键脑区和拓扑特征
    """
    # 基于模型系数的特征重要性
    importances = {}
    
    for dim_idx, estimator in enumerate(model.estimators_):
        coef = estimator.coef_
        
        # 识别高权重连接
        top_connections = identify_top_connections(coef, region_names)
        importances[f'dimension_{dim_idx}'] = top_connections
    
    return importances
```

**可视化解释**：
```python
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_emotion_network(importances, fc_template):
    """
    可视化情感特定的功能网络拓扑
    
    Args:
        importances: 特征重要性分析结果
        fc_template: 脑模板用于可视化
    """
    for emotion, connections in importances.items():
        # 绘制脑网络连接图
        plot_brain_network(
            connections=connections,
            template=fc_template,
            title=f'{emotion} Network Configuration'
        )
        
        # 绘制拓扑特征分布
        plot_topological_metrics(
            connections=connections,
            metrics=['modularity', 'efficiency', 'clustering']
        )
```

## 实验验证要点

### 1. 性能对比实验

**对比条件**：
- DFC vs. Static ROI Amplitude（静态 ROI 振幅）
- 多目标回归 vs. 单标签分类
- LLM 自动标注 vs. 人工标注

**评估指标**：
- 连续轨迹的预测准确度（R²、RMSE）
- 时间对齐度（动态相关系数）
- 多维度相关性

### 2. 自然叙事数据集

**推荐数据集**：
- Alice in Wonderland fMRI 数据集（论文使用）
- Sherlock 电影观看数据集
- Pieman 自然叙事数据集

**数据预处理**：
```python
# fMRI 预处理标准流程
preprocessing_steps = [
    'motion_correction',
    'spatial_normalization',
    'temporal_filtering',  # 0.01-0.1 Hz
    'artifact_removal',
    'parcellation'  # 使用 atlas 如 Schaefer-100
]
```

### 3. 心理构建主义框架验证

**假设检验**：
- 验证动态分布式网络交互 > 位置主义解释力
- 情感维度共现模式分析
- 情感特异性拓扑配置可解释性

## 应用场景

### 1. 情感神经科学研究
- 自然叙事下的情感动态追踪
- 情感共现机制研究
- 情感维度神经表征分析

### 2. 临床应用
- 情感障碍（抑郁、焦虑）的诊断标记
- 情感调节治疗效果评估
- 情感神经反馈训练

### 3. 跨模态情感分析
- 视觉-听觉-文本多模态情感解码
- 实时情感监控系统
- 个性化情感追踪

## 关键优势

1. **连续性**：捕捉情感的连续动态而非离散状态
2. **多维度**：同时追踪多个重叠的情感维度
3. **自动化**：LLM 自动标注减少人工成本
4. **动态性**：DFC 表示保留网络动力学信息
5. **可解释**：图理论 XAI 揭示情感拓扑机制

## 技术限制

1. **LLM 偏差**：自动化标注可能继承模型偏差
2. **时间分辨率**：fMRI 时间分辨率限制快速情感变化捕捉
3. **计算成本**：大规模 LLM API 调用成本
4. **个体差异**：跨个体泛化能力待验证
5. **叙事特异性**：方法论依赖于叙事刺激

## 扩展方向

1. **实时解码**：开发实时情感追踪系统
2. **跨模态融合**：结合 EEG、fNIRS 等高时间分辨率模态
3. **个性化模型**：个体特异性情感解码模型
4. **因果推断**：从相关性到因果性的情感机制分析
5. **生成式模型**：使用生成式模型预测情感轨迹

## 参考文献

- arXiv:2606.07707v1 - "Decoding Naturalistic Emotion Dynamics from the Brain"
- Plutchik (1980) - 情感多维理论
- Russell (2003) - 情感环状模型
- Kassam et al. (2013) - 情感分类解码
- Saarimäki et al. (2022) - 情感网络研究

## 相关 Skill

- [[dynamic-functional-connectivity-analysis]] - 动态功能连接分析方法
- [[llm-neuroscience-annotation]] - LLM 神经科学标注方法
- [[brain-network-topology-analysis]] - 脑网络拓扑分析
- [[multi-target-regression-neuroimaging]] - 神经影像多目标回归
- [[explainable-ai-neuroscience]] - 神经科学可解释 AI
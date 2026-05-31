---
name: neural-code-dynamics-analysis
description: "神经编码动力学分析框架 - 整合计算神经科学、机器学习和临界态理论，研究生物与人工神经网络编码表示动力学。涵盖临界脑假说、雪崩动力学、信息几何与动力学不变量。Activation: neural coding, dynamics analysis, critical brain hypothesis, avalanche dynamics, information geometry, dynamical invariants, neural representation, encoding dynamics, computational neuroscience."
---

# Neural Code Dynamics Analysis

神经编码动力学分析框架，系统化研究神经表示的动态演化与信息处理。

## 核心理论框架

### 1. 临界脑假说

大脑可能工作在临界态附近，平衡有序（稳定）与混沌（灵活）。

#### 雪崩动力学

神经活动雪崩遵循幂律分布：

```
P(s) ~ s^{-alpha}
```

其中：
- `s`: 雪崩大小（参与的神经元数量）
- `alpha`: 临界指数（理论值约 3/2 或 1.5）

**临界指标**:

```python
def compute_avalanche_distribution(spike_data):
    """计算雪崩大小分布"""
    
    # 检测雪崩事件
    avalanche_sizes = detect_avalanches(spike_data)
    
    # 幂律拟合
    from scipy.stats import powerlaw
    params = powerlaw.fit(avalanche_sizes)
    
    alpha = params[0]  # 临界指数
    
    return alpha, avalanche_sizes

def check_criticality(alpha, confidence_interval=(1.4, 1.6)):
    """检验系统是否在临界态"""
    
    is_critical = confidence_interval[0] <= alpha <= confidence_interval[1]
    
    return is_critical
```

#### 分支比率

另一个临界指标：分支比率 `sigma`

```
sigma = <E[后代活动]> / <E[前代活动]>
```

- `sigma < 1`: 亚临界（稳定，信息传递弱）
- `sigma > 1`: 超临界（混沌，信息过度放大）
- `sigma ≈ 1`: 临界态

```python
def compute_branching_ratio(activity_data):
    """计算分支比率"""
    
    # 当前活动的后代活动
    parent_activity = activity_data[:-1]
    offspring_activity = activity_data[1:]
    
    sigma = np.mean(offspring_activity) / np.mean(parent_activity)
    
    return sigma
```

### 2. 信息几何

神经表示的几何结构决定信息处理能力。

#### Fisher 信息矩阵

量化参数变化对分布的影响：

```
I(theta) = E[(partial log p(x|theta)/partial theta)^2]
```

**应用**：分析神经网络参数的编码效率。

#### Fisher-Rao 几何距离

神经表示之间的几何距离：

```
d(theta1, theta2) = arccos(sqrt(F(theta1, theta2)))
```

其中 `F` 是 Fisher-Rao 度量。

```python
def compute_fisher_information(model, data):
    """计算 Fisher 信息矩阵"""
    
    # 使用 PyTorch 计算
    import torch
    
    # 估计参数敏感性
    params = list(model.parameters())
    fisher_info = torch.zeros(len(params), len(params))
    
    for x in data:
        # 计算对数似然梯度
        log_prob = model.log_prob(x)
        grads = torch.autograd.grad(log_prob, params)
        
        # Fisher 信息 = 梯度的外积期望
        for i, g_i in enumerate(grads):
            for j, g_j in enumerate(grads):
                fisher_info[i, j] += g_i * g_j
    
    fisher_info /= len(data)
    
    return fisher_info

def compute_representation_distance(model1, model2, data):
    """计算两个表示之间的 Fisher-Rao 距离"""
    
    I1 = compute_fisher_information(model1, data)
    I2 = compute_fisher_information(model2, data)
    
    # Fisher-Rao 度量
    F = 0.5 * (I1 + I2)
    
    # 计算距离
    distance = np.arccos(np.sqrt(np.trace(F)))
    
    return distance
```

### 3. 动力学不变量

神经动力学中的重要不变量。

#### Lyapunov 指数

量化系统的混沌程度：

```
lambda = lim_{t->infty} 1/t log |delta x(t)|/|delta x(0)|
```

- `lambda > 0`: 混沌
- `lambda < 0`: 稳定
- `lambda = 0`: 临界

```python
def compute_lyapunov_exponent(timeseries_data):
    """计算 Lyapunov 指数"""
    
    # 从时间序列估计
    from nolds import lyap_r
    
    lambda_value = lyap_r(timeseries_data, emb_dim=10)
    
    return lambda_value
```

#### Kolmogorov 复杂度

量化序列的信息量：

```
K(x) = lim_{n->infty} min{|p: p reconstructs x}/log n
```

使用 Lempel-Ziv 复杂度近似：

```python
def compute_lempel_ziv_complexity(sequence):
    """计算 Lempel-Ziv 复杂度"""
    
    n = len(sequence)
    complexity = 0
    substring_count = 0
    
    # 查找最小子串数量以重建序列
    i = 0
    while i < n:
        max_len = 0
        for j in range(i):
            # 查找最长重复子串
            for length in range(1, n - i + 1):
                if sequence[i:i+length] in sequence[j:j+length]:
                    max_len = length
        
        if max_len > 0:
            i += max_len
        else:
            i += 1
        substring_count += 1
    
    # 正则化复杂度
    C = substring_count * np.log(n) / n
    
    return C
```

### 4. 神经表示学习

#### 对齐理论

神经网络表示与大脑表示的对齐度量：

**中心核匹配**:

```
Alignment = match(neural_rep, brain_rep)
```

```python
def compute_representation_alignment(neural_features, brain_features):
    """计算表示对齐"""
    
    # 使用 RSA (Representational Similarity Analysis)
    from scipy.stats import spearmanr
    
    # 计算各自的相关矩阵
    neural_rdm = compute_rdm(neural_features)
    brain_rdm = compute_rdm(brain_features)
    
    # Spearman 相关
    alignment, p_value = spearmanr(neural_rdm.flatten(), 
                                   brain_rdm.flatten())
    
    return alignment

def compute_rdm(features):
    """计算表示不相似度矩阵"""
    
    n = features.shape[0]
    rdm = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            # 使用相关距离
            rdm[i, j] = 1 - np.corrcoef(features[i], features[j])[0, 1]
    
    return rdm
```

## 实现流程

### Step 1: 数据准备与预处理

```python
# 神经数据加载
import numpy as np

def load_neural_data(source, format):
    """加载神经活动数据"""
    
    if source == 'spike_train':
        # 脉冲序列数据
        data = np.load('spike_data.npy')
        # 格式: (n_neurons, n_timepoints)
        
    elif source == 'fMRI':
        # fMRI BOLD 数据
        data = np.load('fmri_data.npy')
        # 格式: (n_regions, n_timepoints)
        
    elif source == 'EEG':
        # EEG 信号
        data = np.load('eeg_data.npy')
        # 格式: (n_channels, n_timepoints)
    
    return preprocess_neural_data(data, format)

def preprocess_neural_data(data, format):
    """预处理神经数据"""
    
    # 带通滤波
    if format == 'raw':
        from scipy.signal import butter, filtfilt
        b, a = butter(4, [1, 100], btype='band', fs=1000)
        data = filtfilt(b, a, data)
    
    # 归一化
    data = (data - data.mean(axis=1, keepdims=True)) / data.std(axis=1, keepdims=True)
    
    # 去噪（可选）
    from scipy.signal import savgol_filter
    data = savgol_filter(data, 51, 3, axis=1)
    
    return data
```

### Step 2: 临界态分析

```python
def analyze_critical_state(neural_data):
    """完整的临界态分析"""
    
    results = {}
    
    # 1. 雪崩分析（适用于脉冲数据）
    if neural_data.shape[0] < 500:  # 神经元数量适中
        alpha = compute_avalanche_distribution(neural_data)
        results['avalanche_alpha'] = alpha
        
        # 检验临界态
        results['is_critical'] = check_criticality(alpha)
    
    # 2. 分支比率（适用于任何活动数据）
    sigma = compute_branching_ratio(np.sum(neural_data, axis=0))
    results['branching_ratio'] = sigma
    
    # 3. Lyapunov 指数（适用于连续数据）
    # 对代表性通道计算
    lambda_values = [compute_lyapunov_exponent(neural_data[i]) 
                    for i in range(min(10, neural_data.shape[0]))]
    results['lyapunov_exponents'] = lambda_values
    results['average_lyapunov'] = np.mean(lambda_values)
    
    # 4. Lempel-Ziv 复杂度
    complexities = [compute_lempel_ziv_complexity(neural_data[i])
                   for i in range(neural_data.shape[0])]
    results['lz_complexities'] = complexities
    results['average_complexity'] = np.mean(complexities)
    
    return results

def interpret_criticality_results(results):
    """解释临界态分析结果"""
    
    interpretation = []
    
    # 雪崩临界指数
    if 'avalanche_alpha' in results:
        alpha = results['avalanche_alpha']
        if 1.4 <= alpha <= 1.6:
            interpretation.append("✓ 系统在临界态附近工作")
            interpretation.append("  - 信息传输效率最优")
            interpretation.append("  - 动态范围最大")
        elif alpha < 1.4:
            interpretation.append("✗ 系统亚临界")
            interpretation.append("  - 过度稳定，灵活性不足")
        else:
            interpretation.append("✗ 系统超临界")
            interpretation.append("  - 混沌倾向，稳定性不足")
    
    # 分支比率
    sigma = results['branching_ratio']
    if abs(sigma - 1) < 0.1:
        interpretation.append(f"✓ 分支比率接近临界 (σ={sigma:.2f})")
    else:
        interpretation.append(f"✗ 分支比率偏离临界 (σ={sigma:.2f})")
    
    # Lyapunov 指数
    lambda_avg = results['average_lyapunov']
    if lambda_avg > 0.01:
        interpretation.append(f"✗ 混沌动力学 (λ={lambda_avg:.3f})")
    elif lambda_avg < -0.01:
        interpretation.append(f"✗ 过度稳定 (λ={lambda_avg:.3f})")
    else:
        interpretation.append(f"✓ 临界动力学 (λ≈{lambda_avg:.3f})")
    
    return interpretation
```

### Step 3: 动态模式提取

```python
def extract_dynamic_modes(neural_data):
    """提取神经动力学模式"""
    
    # PCA 降维
    from sklearn.decomposition import PCA
    
    pca = PCA(n_components=10)
    modes = pca.fit_transform(neural_data.T)  # 转置以处理时间
    
    # 模式的特征值（能量分布）
    eigenvalues = pca.explained_variance_
    
    # 检验模式能量分布是否幂律
    mode_spectrum = fit_spectrum_distribution(eigenvalues)
    
    return modes, eigenvalues, mode_spectrum

def fit_spectrum_distribution(eigenvalues):
    """拟合模式谱分布"""
    
    # 检验是否为幂律（临界态特征）
    from scipy.stats import powerlaw
    
    params = powerlaw.fit(eigenvalues)
    exponent = params[0]
    
    spectrum_info = {
        'exponent': exponent,
        'is_powerlaw': exponent > 0.5,  # 幂律判定
        'dominant_modes': len([e for e in eigenvalues if e > eigenvalues.mean()])
    }
    
    return spectrum_info

def classify_dynamic_modes(modes, eigenvalues):
    """分类动力学模式"""
    
    classifications = []
    
    for i, (mode, eigenvalue) in enumerate(zip(modes.T, eigenvalues)):
        
        # 模态频率分析
        freq = compute_dominant_frequency(mode)
        
        # 模态稳定性
        stability = analyze_mode_stability(mode)
        
        # 模态复杂度
        complexity = compute_mode_complexity(mode)
        
        # 分类
        if eigenvalue > eigenvalues.mean():
            role = "Dominant Mode"
        elif stability > 0.8:
            role = "Stable Mode"
        elif complexity > 0.7:
            role = "Complex Mode"
        else:
            role = "Background Mode"
        
        classifications.append({
            'index': i,
            'frequency': freq,
            'stability': stability,
            'complexity': complexity,
            'role': role
        })
    
    return classifications
```

### Step 4: 信息处理分析

```python
def analyze_information_processing(neural_data):
    """分析信息处理能力"""
    
    results = {}
    
    # 1. 信息传输效率
    # 使用互信息
    from sklearn.metrics import mutual_info_score
    
    MI_matrix = compute_mutual_information_matrix(neural_data)
    results['average_MI'] = np.mean(MI_matrix)
    results['information_efficiency'] = results['average_MI'] / np.var(neural_data)
    
    # 2. 编码容量
    # 使用 Fisher 信息
    fisher_info = estimate_fisher_information(neural_data)
    results['coding_capacity'] = np.trace(fisher_info)
    
    # 3. 信息几何曲率
    curvature = compute_information_curvature(neural_data)
    results['curvature'] = curvature
    
    # 4. 动态熵率
    entropy_rate = compute_dynamic_entropy_rate(neural_data)
    results['entropy_rate'] = entropy_rate
    
    return results

def compute_mutual_information_matrix(data):
    """计算互信息矩阵"""
    
    n = data.shape[0]
    MI_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # 离散化连续数据
                data_i_discrete = np.histogram(data[i], bins=50)[0]
                data_j_discrete = np.histogram(data[j], bins=50)[0]
                
                MI_matrix[i, j] = mutual_info_score(data_i_discrete, data_j_discrete)
    
    return MI_matrix

def compute_dynamic_entropy_rate(data):
    """计算动态熵率"""
    
    # 使用样本熵
    from antropy import sample_entropy
    
    entropy_rates = [sample_entropy(data[i], order=2, delay=1)
                    for i in range(data.shape[0])]
    
    return np.mean(entropy_rates)
```

### Step 5: 人工神经网络对比分析

```python
def compare_neural_network_dynamics(neural_data, model_data):
    """对比生物神经网络与人工神经网络动力学"""
    
    comparison = {}
    
    # 生物网络分析
    bio_results = analyze_critical_state(neural_data)
    bio_modes, bio_eigenvalues, _ = extract_dynamic_modes(neural_data)
    
    # 模型网络分析
    model_results = analyze_critical_state(model_data)
    model_modes, model_eigenvalues, _ = extract_dynamic_modes(model_data)
    
    # 动态特征对比
    comparison['avalanche_match'] = abs(bio_results['avalanche_alpha'] - 
                                          model_results['avalanche_alpha']) < 0.1
    
    comparison['branching_match'] = abs(bio_results['branching_ratio'] - 
                                        model_results['branching_ratio']) < 0.1
    
    comparison['lyapunov_match'] = abs(bio_results['average_lyapunov'] - 
                                       model_results['average_lyapunov']) < 0.05
    
    # 表示对齐
    alignment = compute_representation_alignment(bio_modes, model_modes)
    comparison['representation_alignment'] = alignment
    
    # 动态距离
    dynamic_distance = compute_dynamic_distance(bio_eigenvalues, model_eigenvalues)
    comparison['dynamic_distance'] = dynamic_distance
    
    return comparison

def compute_dynamic_distance(eigenvalues1, eigenvalues2):
    """计算动力学谱距离"""
    
    # 形变谱对齐
    n_min = min(len(eigenvalues1), len(eigenvalues2))
    
    # 形变能量距离
    distance = np.sqrt(np.sum((eigenvalues1[:n_min] - eigenvalues2[:n_min])**2))
    
    # 正则化
    distance /= np.sqrt(np.sum(eigenvalues1[:n_min]**2))
    
    return distance
```

## 应用场景

### 1. 临界态维持机制研究

**输入**：不同条件下（静息态、任务态、睡眠态）的神经数据

**输出**：
- 各条件下的临界指标对比
- 临界态偏离的生理意义

**应用**：
- 理解大脑如何在不同状态下调整临界态
- 神经疾病（癫痫、精神分裂）的临界态异常

### 2. 神经编码优化

**输入**：神经网络模型的编码表示

**输出**：
- 编码容量与 Fisher 信息
- 与生物编码的对齐度

**应用**：
- 优化神经网络以模仿生物编码
- 提高模型的神经科学合理性

### 3. 动态模式诊断

**输入**：疾病状态下的神经活动

**输出**：
- 异常动力学模式识别
- 临界态偏离量化

**应用**：
- 神经退行性疾病早期诊断
- 动态模式变化作为疾病进展指标

## 关键发现（文献总结）

### 1. 临界态的功能优势

**发现**：临界态同时最大化信息传输和动态范围。

**意义**：大脑工作在临界态附近以优化信息处理。

### 2. 状态依赖的临界态调节

**发现**：不同认知状态下临界指数略有变化（alpha 在 1.3-1.7 之间）。

**意义**：大脑灵活调节临界态以适应任务需求。

### 3. 神经表示的几何约束

**发现**：神经表示空间的曲率影响编码效率。

**意义**：几何结构约束决定了可能的表示形式。

### 4. 动态不变量的疾病关联

**发现**：阿尔茨海默病患者的 Lyapunov 指数异常（过度稳定）。

**意义**：动态不变量可作为疾病诊断的早期指标。

## 进阶分析

### 1. 多尺度动力学

```python
def analyze_multiscale_dynamics(data, scales):
    """多尺度动力学分析"""
    
    results = {}
    
    for scale in scales:
        # 重采样到不同时间尺度
        resampled = resample_data(data, scale)
        
        # 分析该尺度的动力学
        analysis = analyze_critical_state(resampled)
        results[scale] = analysis
    
    # 尺度间一致性检验
    scale_consistency = check_scale_consistency(results)
    
    return results, scale_consistency

def check_scale_consistency(results):
    """检验多尺度一致性"""
    
    # 临界态应该在多尺度上保持
    alpha_values = [r['avalanche_alpha'] for r in results.values()]
    
    consistency = 1 - np.std(alpha_values) / np.mean(alpha_values)
    
    return consistency
```

### 2. 因果动力学

```python
def analyze_causal_dynamics(data):
    """因果动力学分析"""
    
    # Granger 因果分析
    from statsmodels.tsa.stattools import grangercausalitytests
    
    n = data.shape[0]
    causal_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # 检验 i 是否 Granger 因果 j
                test_result = grangercausalitytests(
                    np.column_stack([data[i], data[j]]),
                    maxlag=10
                )
                causal_matrix[i, j] = test_result[1][0]['ssr_ftest'][0]
    
    return causal_matrix
```

### 3. 非线性动力学不变量

```python
def compute_nonlinear_invariants(data):
    """非线性动力学不变量"""
    
    results = {}
    
    # Hurst 指数（自相关性）
    from antropy import hurst_exponent
    results['hurst'] = np.mean([hurst_exponent(data[i]) 
                               for i in range(data.shape[0])])
    
    # 样本熵（复杂度）
    results['sample_entropy'] = compute_dynamic_entropy_rate(data)
    
    # Permutation 熵
    from antropy import permutation_entropy
    results['permutation_entropy'] = np.mean([permutation_entropy(data[i])
                                              for i in range(data.shape[0])])
    
    # Approximate 熵
    from antropy import approx_entropy
    results['approximate_entropy'] = np.mean([approx_entropy(data[i])
                                              for i in range(data.shape[0])])
    
    return results
```

## 工具与资源

### 数据源

- **脉冲数据**：Neuropixels、MEA 记录
- **fMRI 数据**：HCP、ADNI 数据集
- **EEG 数据**：OpenNeuro 公开数据集
- **神经网络模型**：预训练模型激活数据

### 分析库

- **antropy**: Python 熵和复杂度分析
- **nolds**: Lyapunov 指数计算
- **NeuroDSP**: 神经信号分析
- **MNE**: MEG/EEG 分析

### 关键文献

1. Chialvo (2010) - "Emergent complex neural dynamics"
2. Beggs & Plenz (2003) - "Neuronal avalanches in cultured networks"
3. Tkačik et al. (2015) - "Thermodynamics of neural processing"
4. Amari (2016) - "Information geometry and its applications"

## 验证与评估

### 1. 临界态检验验证

```python
def validate_criticality_method(data, ground_truth_critical):
    """验证临界态分析方法"""
    
    predicted_alpha = compute_avalanche_distribution(data)
    
    # 与理论值对比
    theoretical_alpha = 1.5  # Branched process 理论值
    
    error = abs(predicted_alpha - theoretical_alpha)
    
    return error
```

### 2. 动态预测能力验证

```python
def validate_dynamics_prediction(data, future_data):
    """验证动力学预测能力"""
    
    # 使用当前动力学预测未来状态
    modes, eigenvalues, _ = extract_dynamic_modes(data)
    
    # 基于模式预测未来活动
    prediction = predict_future_activity(modes, eigenvalues)
    
    # 与实际未来数据对比
    error = np.mean((prediction - future_data)**2)
    
    return error
```

## 局限性与注意事项

### 1. 数据长度要求

- **局限**：临界态分析需要长时间序列（>10^4 时间点）
- **应对**：分段分析或使用 bootstrap 方法

### 2. 幂律拟合稳定性

- **局限**：短数据可能导致幂律拟合不稳定
- **应对**：使用最大似然拟合而非最小二乘

### 3. 状态依赖性

- **局限**：不同认知状态下临界态变化
- **应对**：状态分割后再分析

### 4. 神经元数量效应

- **局限**：雪崩分析结果依赖神经元采样数量
- **应对**：归一化或使用分支比率替代

## 与其他方法的关系

### vs Functional Connectivity

- FC：静态相关分析
- 临界态分析：动态非线性分析

### vs Dynamic Functional Connectivity

- dFC：时间变化的相关分析
- 临界态分析：全局动态状态分析

### vs Neural Mass Models

- NMM：参数化动力学模型
- 临界态分析：无参数的状态特征分析

## 临床应用

### 1. 神经疾病诊断

**应用**：癫痫、阿尔茨海默病的动力学异常检测

**方法**：
- 计算患者与健康对照组的临界指标
- 检验临界态偏离
- 作为诊断辅助指标

### 2. 治疗效果评估

**应用**：药物/刺激治疗的动力学效果评估

**方法**：
- 治疗前后临界态对比
- 动态模式变化分析
- 信息处理效率评估

### 3. 认知状态监测

**应用**：实时监测认知状态

**方法**：
- 实时临界指数计算
- 状态切换检测
- 异常动力学预警

## 激活关键词

- neural coding
- dynamics analysis
- critical brain hypothesis
- avalanche dynamics
- information geometry
- dynamical invariants
- neural representation
- encoding dynamics
- computational neuroscience
- Lyapunov exponent
- branching ratio
- Fisher information
- Lempel-Ziv complexity
- sample entropy
- permutation entropy
- Hurst exponent
- representation alignment
- RSA (Representational Similarity Analysis)
- dynamic modes
- eigenvalue spectrum
- information processing
- critical state
- subcritical
- supercritical
- neural avalanches
- power law distribution

## 相关 Skills

- [[brain-criticality-hypothesis-assessment]]: 脑临界性假设评估
- [[neural-population-dynamics]]: 神经种群动力学分析
- [[eeg-foundation-model-adapters]]: EEG 基础模型适配
- [[spiking-oscillation-mapping]]: 脉冲振荡状态映射
- [[free-energy-moe-routing]]: 基于自由能量的 MoE 路由
- [[efficient-coding-criticality-sloppiness]]: 有效编码临界态

## 推荐阅读

1. Chialvo DR. (2010). Emergent complex neural dynamics. Nature Physics.
2. Beggs JM, Plenz D. (2003). Neuronal avalanches. J Neurosci.
3. Tkačik G, et al. (2015). Thermodynamics and statistical physics of neural processing. Entropy.
4. Amari S. (2016). Information Geometry and Its Applications. Springer.
5. Shew WL, et al. (2009). Neuronal avalanches imply maximum dynamic range. PLoS One.

## 代码仓库

- antropy: https://github.com/nikdon/antropy
- nolds: https://github.com/CSchoel/nolds
- NeuroDSP: https://github.com/neurodsp-tools/neurodsp

---

## Instructions for Agents

使用此 skill 时：

1. 首先确认数据类型和长度是否适合临界态分析
2. 计算 3-4 个独立的临界指标进行交叉验证
3. 进行动态模式提取以识别主要动力学
4. 如果有模型数据，进行表示对齐分析
5. 综合解释结果，不要仅依赖单一指标

## Examples

### Example 1: 脑状态临界分析

**User**: 分析静息态 fMRI 数据的临界特征

**Agent**:
- 计算分支比率：σ ≈ 1.05（接近临界）
- 计算 Lyapunov 指数：λ ≈ 0.01（临界态）
- 提取动态模式并分析谱分布
- 解释：系统在临界态附近工作，动态范围最大化

### Example 2: 神经疾病诊断

**User**: 比较癫痫患者与健康对照组的动力学

**Agent**:
- 计算患者：α = 1.8（超临界），σ = 1.3
- 计算对照组：α = 1.5（临界），σ = 1.0
- 识别异常动力学模式
- 解释：癫痫患者系统过度活跃，信息过度放大

### Example 3: 模型对齐优化

**User**: 优化神经网络使其动力学更接近大脑

**Agent**:
- 计算模型当前的临界指标
- 计算与生物数据对齐度
- 提出调节策略（例如：引入噪声以达到临界态）
- 重新训练并验证改进

## Activation Keywords

- neural coding
- dynamics analysis
- critical brain hypothesis
- avalanche dynamics
- information geometry
- dynamical invariants
- neural representation
- encoding dynamics
- computational neuroscience
- 神经编码
- 动力学分析
- 临界态

## Tools Used

- Python (numpy, scipy, sklearn, nolds, antropy)
- Read
- Write
- Exec

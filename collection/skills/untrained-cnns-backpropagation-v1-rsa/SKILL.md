---
name: untrained-cnns-match-backpropagation-v1-rsa
description: "系统RSA比较研究：展示未训练CNN在V1视觉皮层区域与反向传播训练的CNN具有相似表征。通过大规模fMRI和表征相似性分析，挑战传统深度学习需要大量训练的观点。适用于视觉皮层建模、CNN可解释性、神经科学。"
---

# Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison

> 突破性发现：随机初始化的CNN在初级视觉皮层(V1)区域展现出与训练后网络相似的神经表征，挑战深度学习必须依赖反向传播的传统认知。

## Metadata
- **Source**: arXiv:2604.16875
- **Authors**: Xinyuan Zhang, Chengzhi Cao, Lingyue Li, Dongcheng Zhao, Yi Zeng
- **Published**: 2026-04-18
- **Category**: Computational Neuroscience, Deep Learning, Visual Cortex

## Core Methodology

### Key Innovation
本研究通过系统性的表征相似性分析(RSA)发现：
1. **未训练CNN ≈ 训练CNN在V1**: 随机权重CNN与训练后CNN在V1区域的表征相似度高达0.85+
2. **架构决定先验**: 网络架构本身编码了与生物视觉系统一致的归纳偏置
3. **分层对齐**: 浅层对齐V1，深层对齐更高视觉区域

### Experimental Design

#### 1. Model Comparison
对比四种CNN变体：
- **RandomInit-CNN**: 随机初始化权重
- **Supervised-CNN**: ImageNet监督训练
- **SelfSupervised-CNN**: 自监督学习(DINO, SimCLR)
- **BioInspired-CNN**: 加入生物约束的训练

#### 2. Brain Data
- **Modality**: fMRI (3T, TR=2s)
- **Subjects**: 8 healthy adults
- **Stimuli**: 1,000 natural images
- **ROI**: V1, V2, V3, V4, IT

#### 3. RSA Analysis Pipeline
```
Model Activations → RDM Computation → 
Brain RDMs → Correlation Analysis → Statistical Testing
```

**Representational Dissimilarity Matrix (RDM):**
- 计算每对刺激间的表征距离
- 使用Pearson/Spearman相关
- 分层分析(每层独立RDM)

## Implementation Guide

### Prerequisites
- Python 3.9+
- PyTorch/Torchvision
- Nilearn (神经影像)
- Scipy/Scikit-learn
- Matplotlib/Seaborn

### Step-by-Step RSA Analysis

#### Step 1: Extract CNN Features
```python
import torch
import torchvision.models as models
from torchvision import transforms
import numpy as np

def extract_features(model, images, layer_names):
    """
    提取CNN多层特征
    
    Args:
        model: PyTorch模型
        images: 图像张量 [N, C, H, W]
        layer_names: 要提取的层名列表
    
    Returns:
        features: 字典 {layer_name: features}
    """
    features = {}
    hooks = []
    
    def hook_fn(name):
        def hook(module, input, output):
            features[name] = output.detach()
        return hook
    
    # 注册钩子
    for name, module in model.named_modules():
        if name in layer_names:
            hooks.append(module.register_forward_hook(hook_fn(name)))
    
    # 前向传播
    with torch.no_grad():
        _ = model(images)
    
    # 移除钩子
    for h in hooks:
        h.remove()
    
    return features

# 使用示例
model = models.resnet50(pretrained=False)  # 随机初始化
layer_names = ['layer1', 'layer2', 'layer3', 'layer4']
features = extract_features(model, images, layer_names)
```

#### Step 2: Compute RDM
```python
from scipy.spatial.distance import pdist, squareform
from scipy.stats import spearmanr

def compute_rdm(features, metric='correlation'):
    """
    计算表征相异度矩阵(RDM)
    
    Args:
        features: 特征矩阵 [N_samples, N_features]
        metric: 距离度量 ('correlation', 'euclidean', 'cosine')
    
    Returns:
        rdm: [N_samples, N_samples] 相异度矩阵
    """
    # 展平特征
    if len(features.shape) > 2:
        features = features.reshape(features.shape[0], -1)
    
    # 计算两两距离
    distances = pdist(features, metric=metric)
    rdm = squareform(distances)
    
    return rdm

def compute_rdm_correlation(rdm1, rdm2, method='spearman'):
    """
    计算两个RDM的相关性
    
    Args:
        rdm1, rdm2: 两个相异度矩阵
        method: 'spearman' 或 'pearson'
    
    Returns:
        correlation: 相关系数
        p_value: p值
    """
    # 提取上三角(排除对角线)
    triu_idx = np.triu_indices_from(rdm1, k=1)
    vec1 = rdm1[triu_idx]
    vec2 = rdm2[triu_idx]
    
    if method == 'spearman':
        corr, pval = spearmanr(vec1, vec2)
    else:
        corr = np.corrcoef(vec1, vec2)[0, 1]
        pval = None
    
    return corr, pval
```

#### Step 3: Layer-to-Brain Mapping
```python
import matplotlib.pyplot as plt
import seaborn as sns

def layer_brain_rsa_analysis(model_rdms, brain_rdms, regions):
    """
    层到脑区的RSA映射分析
    
    Args:
        model_rdms: 模型各层RDM字典
        brain_rdms: 脑区RDM字典
        regions: 脑区名称列表
    
    Returns:
        results: 相关性矩阵 [n_layers, n_regions]
    """
    layer_names = list(model_rdms.keys())
    n_layers = len(layer_names)
    n_regions = len(regions)
    
    results = np.zeros((n_layers, n_regions))
    
    for i, layer in enumerate(layer_names):
        for j, region in enumerate(regions):
            corr, _ = compute_rdm_correlation(
                model_rdms[layer], 
                brain_rdms[region]
            )
            results[i, j] = corr
    
    # 可视化
    plt.figure(figsize=(10, 6))
    sns.heatmap(results, 
                xticklabels=regions,
                yticklabels=layer_names,
                cmap='viridis',
                annot=True,
                fmt='.3f')
    plt.title('Layer-to-Brain RSA Correlation')
    plt.tight_layout()
    plt.show()
    
    return results
```

#### Step 4: Statistical Testing
```python
from scipy.stats import ttest_rel, wilcoxon

def compare_models_rsa(model1_rdms, model2_rdms, brain_rdms, regions):
    """
    比较两个模型的RSA表现
    
    Args:
        model1_rdms: 模型1的各层RDM
        model2_rdms: 模型2的各层RDM
        brain_rdms: 脑区RDM
        regions: 脑区列表
    
    Returns:
        stats: 统计测试结果
    """
    corrs_1 = []
    corrs_2 = []
    
    for region in regions:
        # 找到最优层
        best_layer_1 = max(model1_rdms.keys(), 
                          key=lambda l: compute_rdm_correlation(
                              model1_rdms[l], brain_rdms[region])[0])
        best_layer_2 = max(model2_rdms.keys(),
                          key=lambda l: compute_rdm_correlation(
                              model2_rdms[l], brain_rdms[region])[0])
        
        corr_1, _ = compute_rdm_correlation(
            model1_rdms[best_layer_1], brain_rdms[region])
        corr_2, _ = compute_rdm_correlation(
            model2_rdms[best_layer_2], brain_rdms[region])
        
        corrs_1.append(corr_1)
        corrs_2.append(corr_2)
    
    # 配对t检验
    t_stat, p_val = ttest_rel(corrs_1, corrs_2)
    
    return {
        'model1_mean': np.mean(corrs_1),
        'model2_mean': np.mean(corrs_2),
        't_statistic': t_stat,
        'p_value': p_val,
        'correlations_1': corrs_1,
        'correlations_2': corrs_2
    }
```

### Complete Analysis Pipeline
```python
# 完整分析流程
class RSAAnalyzer:
    def __init__(self, subjects_data):
        self.subjects_data = subjects_data
        self.results = {}
    
    def analyze_subject(self, subject_id, model):
        """分析单个受试者"""
        # 提取模型特征
        features = self.extract_model_features(model, subject_id)
        
        # 计算模型RDM
        model_rdms = {
            layer: compute_rdm(feat)
            for layer, feat in features.items()
        }
        
        # 获取脑区RDM
        brain_rdms = self.subjects_data[subject_id]['rdms']
        
        # 计算相关性
        correlations = layer_brain_rsa_analysis(
            model_rdms, brain_rdms, ['V1', 'V2', 'V3', 'V4', 'IT'])
        
        return correlations
    
    def group_analysis(self, models_dict):
        """组水平分析"""
        group_results = {}
        
        for model_name, model in models_dict.items():
            subject_corrs = []
            for subject in self.subjects_data:
                corr = self.analyze_subject(subject, model)
                subject_corrs.append(corr)
            
            group_results[model_name] = {
                'mean': np.mean(subject_corrs, axis=0),
                'std': np.std(subject_corrs, axis=0),
                'individual': subject_corrs
            }
        
        return group_results
```

## Key Findings

### 1. V1 Alignment (Main Result)
| Model | V1 Correlation | V2 | V3 | V4 | IT |
|-------|----------------|----|----|----|----|
| RandomInit | 0.87 | 0.65 | 0.52 | 0.41 | 0.28 |
| Supervised | 0.89 | 0.78 | 0.71 | 0.63 | 0.55 |
| Self-Supervised | 0.88 | 0.76 | 0.68 | 0.59 | 0.51 |

### 2. Layer Hierarchy
```
Conv1 → Conv2 → Conv3 → Conv4 → FC
  ↓       ↓       ↓       ↓      ↓
 V1      V2      V3      V4     IT
```

### 3. Architecture Effects
- **ResNet > VGG**: 跳跃连接增强表征对齐
- **Deeper ≠ Better**: 浅层已足够对齐V1
- **Width Matters**: 通道数影响表征丰富度

## Implications

### Theoretical
1. **Inductive Bias**: CNN架构先天编码视觉先验
2. **Learning Efficiency**: 生物视觉可能不需要大量训练
3. **Architecture Design**: 架构选择比训练更重要

### Practical
1. **Few-shot Learning**: 预训练可能不如架构优化
2. **Brain Models**: 随机CNN可作为V1的简化模型
3. **Interpretability**: 无需训练即可分析网络特性

## Pitfalls

### Common Issues
1. **Image Preprocessing**: 不同的预处理影响RSA结果
   - *Solution*: 标准化预处理流程
   
2. **ROI Definition**: V1边界定义的主观性
   - *Solution*: 使用个体化ROI
   
3. **Multiple Comparisons**: 大量统计检验的校正
   - *Solution*: Bonferroni或FDR校正

### Limitations
- 仅测试自然图像，其他刺激类型未知
- 样本量较小(n=8)，统计功效有限
- 未考虑时间动态(仅静态图像)

## Related Skills
- functional-connectivity-graph-neural-networks
- brain-llm-key-neurons-grammar
- adaptive-spiking-neuron-multimodal
- vlm-visual-cortex-alignment-robustness

## References
1. Zhang et al. (2026). Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison. arXiv:2604.16875.
2. Yamins et al. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex. PNAS.
3. Khaligh-Razavi & Kriegeskorte (2014). Deep supervised, but not unsupervised, models may explain IT cortical representation. PLoS CB.

## Citation
```bibtex
@article{zhang2026untrained,
  title={Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison},
  author={Zhang, Xinyuan and Cao, Chengzhi and Li, Lingyue and Zhao, Dongcheng and Zeng, Yi},
  journal={arXiv preprint arXiv:2604.16875},
  year={2026}
}
```

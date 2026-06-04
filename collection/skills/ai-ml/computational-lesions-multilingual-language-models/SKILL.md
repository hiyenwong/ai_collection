---
name: computational-lesions-multilingual-language-models
description: "多语言语言模型计算性损伤方法论。通过因果干预分离共享和语言特异性脑对齐模式，揭示语言理解的神经基础。适用于多语言神经科学、语言模型解释性、跨语言脑对齐。触发词：计算损伤、多语言、脑对齐、因果干预、共享表征。"
---

# Computational Lesions in Multilingual Language Models

> 通过计算性损伤分离多语言语言模型中共享与语言特异性脑对齐模式的因果分析框架。

## Metadata
- **Source**: arXiv:2604.10627
- **Title**: Computational Lesions in Multilingual Language Models Separate Shared and Language-specific Brain Alignment
- **Authors**: Yang Cui, Jingyuan Sun, Yizheng Sun, Yifan Wang, Yunhao Zhang, Jixing Li, Shaonan Wang, Hongpeng Zhou, John Hale, Chengqing Zong, Goran Nenadic
- **Published**: 2026-04-12
- **Category**: NLP & Cognitive Neuroscience

## Core Methodology

### Key Innovation
该研究开发了"计算性损伤"(Computational Lesioning)方法，通过系统性地干预多语言语言模型的特定组件，分离出跨语言共享的神经对齐模式和语言特异性的对齐模式。这为理解人类大脑中多语言表征的组织方式提供了新工具。

### Technical Framework

1. **计算性损伤定义**
   - 选择性消融模型中的特定神经元/层
   - 跨语言对比：损伤前后的表征变化
   - 因果推断：建立损伤与脑对齐改变的因果关系

2. **共享 vs 特异性分离**
   - 共享组件：损伤后跨语言脑对齐均下降
   - 特异性组件：损伤仅影响特定语言对齐
   - 量化分离指标：共享度 vs 特异度

3. **脑对齐测量**
   - fMRI/MEG数据采集多语言处理
   - 模型激活与脑区响应的相关分析
   - 跨语言脑区映射比较

## Implementation Guide

### Prerequisites
- PyTorch/Transformers
- Neuroimaging工具包(nilearn, nibabel)
- 多语言fMRI数据集
- 预训练多语言模型(XLM-R, mBERT等)

### Step-by-Step

1. **多语言模型加载**
   ```python
   from transformers import XLMRobertaModel, XLMRobertaTokenizer
   
   model = XLMRobertaModel.from_pretrained('xlm-roberta-large')
   tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-large')
   ```

2. **计算性损伤实现**
   ```python
   def apply_lesion(model, layer_idx, neuron_indices):
       """在指定层损伤特定神经元"""
       layer = model.encoder.layer[layer_idx]
       
       # 零化输出
       original_forward = layer.forward
       
       def lesioned_forward(hidden_states, *args, **kwargs):
           output = original_forward(hidden_states, *args, **kwargs)
           output[0][:, :, neuron_indices] = 0
           return output
       
       layer.forward = lesioned_forward
       return model
   ```

3. **脑对齐测量**
   ```python
   def compute_brain_alignment(model_activations, brain_responses):
       """计算模型与脑区对齐度"""
       from sklearn.linear_model import Ridge
       from sklearn.metrics import r2_score
       
       # 预测脑响应
       ridge = Ridge(alpha=1.0)
       ridge.fit(model_activations, brain_responses)
       predictions = ridge.predict(model_activations)
       
       # R²作为对齐度量
       return r2_score(brain_responses, predictions, multioutput='raw_values')
   ```

4. **分离分析**
   ```python
   def analyze_shared_vs_specific(lesion_results, languages):
       """分析共享与特异性组件"""
       shared_score = np.min(lesion_results, axis=0)  # 所有语言都下降
       specific_score = np.std(lesion_results, axis=0)  # 语言间差异大
       
       return {
           'shared_components': np.where(shared_score < threshold)[0],
           'specific_components': np.where(specific_score > threshold)[0]
       }
   ```

### Code Example

```python
"""
计算性损伤分析多语言脑对齐
"""

import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer
from typing import Dict, List, Tuple

class MultilingualLesionAnalyzer:
    def __init__(self, model_name="xlm-roberta-large"):
        self.model = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.original_state = {k: v.clone() for k, v in self.model.state_dict().items()}
    
    def lesion_neurons(self, layer: int, neurons: List[int]) -> None:
        """
        损伤特定层的指定神经元
        
        Args:
            layer: 层索引
            neurons: 要损伤的神经元索引列表
        """
        param_name = f"encoder.layer.{layer}.output.dense.weight"
        
        # 零化输出权重
        with torch.no_grad():
            for neuron_idx in neurons:
                self.model.state_dict()[param_name][neuron_idx, :] = 0
    
    def extract_activations(self, texts: List[str], language: str) -> np.ndarray:
        """提取文本的模型激活"""
        inputs = self.tokenizer(
            texts, 
            return_tensors="pt",
            padding=True,
            truncation=True
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs, output_hidden_states=True)
            # 使用最后一层隐藏状态
            activations = outputs.hidden_states[-1][:, 0, :].numpy()
        
        return activations
    
    def compute_brain_correlation(
        self, 
        activations: np.ndarray,
        fmri_data: np.ndarray,
        roi_mask: np.ndarray = None
    ) -> float:
        """
        计算模型激活与fMRI数据的关联
        
        Args:
            activations: 模型激活 [n_samples, n_features]
            fmri_data: fMRI数据 [n_samples, n_voxels]
            roi_mask: ROI掩码
            
        Returns:
            平均相关系数
        """
        from sklearn.cross_decomposition import PLSRegression
        
        # 使用PLS找到最佳映射
        pls = PLSRegression(n_components=5)
        pls.fit(activations, fmri_data)
        
        # 预测并计算相关性
        predicted = pls.predict(activations)
        
        correlations = []
        for i in range(fmri_data.shape[1]):
            if roi_mask is None or roi_mask[i]:
                corr = np.corrcoef(fmri_data[:, i], predicted[:, i])[0, 1]
                correlations.append(corr)
        
        return np.mean(correlations)
    
    def systematic_lesion_analysis(
        self,
        texts_by_language: Dict[str, List[str]],
        fmri_by_language: Dict[str, np.ndarray],
        layer_range: range = range(12)
    ) -> Dict:
        """
        系统性损伤分析
        
        Returns:
            各损伤配置下的脑对齐变化
        """
        results = {}
        
        # 基线对齐(无损伤)
        baseline = {}
        for lang in texts_by_language:
            acts = self.extract_activations(texts_by_language[lang], lang)
            baseline[lang] = self.compute_brain_correlation(
                acts, fmri_by_language[lang]
            )
        
        results['baseline'] = baseline
        
        # 逐层损伤分析
        for layer in layer_range:
            layer_results = {}
            
            # 损伤该层10%的神经元
            n_neurons = self.model.config.hidden_size
            neurons_to_lesion = list(range(0, n_neurons, 10))
            
            self.lesion_neurons(layer, neurons_to_lesion)
            
            for lang in texts_by_language:
                acts = self.extract_activations(texts_by_language[lang], lang)
                alignment = self.compute_brain_correlation(
                    acts, fmri_by_language[lang]
                )
                # 计算相对变化
                layer_results[lang] = (alignment - baseline[lang]) / baseline[lang]
            
            results[f'layer_{layer}'] = layer_results
            
            # 恢复模型
            self.model.load_state_dict(self.original_state)
        
        return results

# 使用示例
analyzer = MultilingualLesionAnalyzer()

# 准备多语言数据
texts = {
    'en': ["The cat sat on the mat", "The dog barked loudly"],
    'zh': ["猫坐在垫子上", "狗大声吠叫"],
    'es': ["El gato se sentó en la alfombra", "El perro ladró fuerte"]
}

# 模拟fMRI数据(实际使用真实数据)
fmri_data = {
    lang: np.random.randn(len(texts[lang]), 1000)  # 1000 voxels
    for lang in texts
}

# 运行分析
results = analyzer.systematic_lesion_analysis(texts, fmri_data)

# 分析共享vs特异性
for layer_key, layer_res in results.items():
    if layer_key == 'baseline':
        continue
    
    changes = [layer_res[lang] for lang in texts.keys()]
    mean_change = np.mean(changes)
    std_change = np.std(changes)
    
    print(f"{layer_key}: 平均变化={mean_change:.3f}, 语言间变异={std_change:.3f}")
    
    if std_change < 0.05:  # 低变异 = 共享组件
        print(f"  -> 识别为共享组件")
    elif std_change > 0.1:  # 高变异 = 特异性组件
        print(f"  -> 识别为语言特异性组件")
```

## Applications

1. **多语言脑机制研究**
   - 理解双语/多语者大脑的组织方式
   - 揭示语言习得的神经可塑性

2. **神经机器翻译优化**
   - 识别跨语言共享的语义空间
   - 改进低资源语言翻译

3. **认知障碍研究**
   - 理解选择性语言障碍的神经基础
   - 开发多语言失语症干预策略

4. **AI系统设计**
   - 设计更高效的多语言模型架构
   - 指导神经科学启发的NLP系统开发

## Pitfalls

- **损伤粒度**: 粗粒度损伤可能遗漏重要组件
- **语言覆盖**: 少数语言可能无法代表所有语言类型
- **脑区选择**: ROI选择影响结果解释
- **因果强度**: 相关性损伤可能非完全因果
- **模型依赖性**: 发现可能特定于某个架构

## Related Skills
- meta-learning-in-context-brain-decoding
- vlm-visual-cortex-alignment-robustness
- brain-dit-fmri-foundation-model
- computational-lesions-multilingual-language-models-separate

## References
- arXiv:2604.10627 (2026)
- XLM-R: Unsupervised Cross-lingual Representation Learning (Conneau et al.)
- Lesion Studies in Neural Networks (Bau et al.)

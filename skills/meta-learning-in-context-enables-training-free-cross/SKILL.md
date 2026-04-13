---
name: meta-learning-in-context-enables-training-free-cross
description: "Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural re... Activation: 神经信号解码"
---

# Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

## 概述
Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge, we introduce a meta-optimized approach for semantic visual decoding from fMRI that generalizes to novel subjects without any fine-tuning. By simply conditioning on a small set of image-brain activation examples from the new individual, our model rapidly infers their unique neural encoding patterns to facilitate robust and efficient visual decoding. Our approach is explicitly optimized for in-context learning of the new subject's encoding model and performs decoding by hierarchical inference, i

## 来源论文
- **标题**: Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding
- **作者**: Mu Nan, Muquan Yu, Weijian Mai
- **arXiv**: 2604.08537v1
- **发布日期**: 2026-04-09
- **类别**: None

## 核心概念
1. 神经信号解码

## 应用价值
- 神经科学研究
- 脑机接口开发
- 计算神经科学建模
- 神经信号分析

## 实现要点
```python
# 基于论文方法的示例实现框架
import numpy as np

class MetaLearningInContextEnablesTrainingFreeCross:
    def __init__(self):
        pass
    
    def process(self, neural_data):
        """
        处理神经数据
        
        Args:
            neural_data: 神经信号数据 (EEG, fMRI, spike trains)
        
        Returns:
            processed: 处理后的特征表示
        """
        # 实现论文中的核心方法
        return neural_data
```

## 参考文献
- Mu Nan, Muquan Yu, Weijian Mai. "Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding". arXiv:2604.08537v1, 2026.

## 激活关键词
- meta learning in context enables training free cross
- Meta-learning In-Context
- neuro 神经信号解码

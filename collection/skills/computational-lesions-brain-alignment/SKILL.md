---
name: computational-lesions-brain-alignment
description: "Computational lesion analysis using multilingual LLMs to separate shared and language-specific brain alignment. Zeroing parameter sets to identify core vs specialized processing. Activation: computational lesion, brain alignment, multilingual LLM, fMRI encoding, causal analysis."
---

# Computational Lesions for Brain-Model Alignment

## Description
使用多语言大语言模型(LLM)进行"计算性损毁"研究，通过将跨语言重要或特定语言重要的参数置零，创建定向损毁，从而分离共享处理和语言特异性处理，建立脑-模型对齐的因果框架。

## Research Background

### 1. 核心科学问题
- 大脑如何支持不同语言的处理？
- 语言处理是共享机制还是语言特异机制？
- 神经影像可识别语言响应区域，但无法区分底层处理机制

### 2. 研究范式创新
- 将多语言LLM作为可控系统
- 创建"计算性损毁"(computational lesions)
- 比较损毁前后模型预测fMRI响应的能力

## Methodology

### 1. 计算性损毁 (Computational Lesions)

#### 1.1 共享核心损毁
- **目标**: 识别跨语言通用的处理核心
- **方法**: 置零对多种语言都重要的小参数集
- **预期效果**: 影响所有语言的脑预测

#### 1.2 语言特异性损毁
- **目标**: 识别语言特化的处理机制
- **方法**: 置零对某一语言特别重要的参数
- **预期效果**: 选择性削弱该语言的脑预测

### 2. 实验设计

#### 2.1 多语言设置
- **语言**: 英语、中文、法语
- **被试**: 112名母语者
- **刺激**: 100分钟自然故事聆听
- **成像**: fMRI记录

#### 2.2 LLM选择
- 6种多语言大语言模型
- 覆盖不同架构和训练策略
- 确保结果的一般性

### 3. 分析框架

#### 3.1 脑编码模型
```
LLM嵌入 → 线性编码模型 → 预测fMRI响应
```

#### 3.2 损毁效应量化
```python
# 计算损毁前后的脑预测相关性
def lesion_effect(intact_model, lesioned_model, fmri_data):
    intact_corr = predict_brain(intact_model, fmri_data)
    lesioned_corr = predict_brain(lesioned_model, fmri_data)
    
    # 相对下降
    reduction = (intact_corr - lesioned_corr) / intact_corr
    return reduction
```

#### 3.3 嵌入空间分析
- 比较损毁前后模型的嵌入空间
- 语言特异性损毁应保留跨语言分离
- 共享核心损毁应影响所有语言表示

## Key Findings

### 1. 共享处理核心
- **损毁效应**: 紧凑共享核心的损毁使全脑编码相关性下降60.32%
- **结论**: 存在跨语言的共享处理主干
- **定位**: 主要分布在经典语言区域

### 2. 语言特化机制
- **损毁效应**: 语言特异性损毁保留跨语言嵌入空间分离
- **选择效应**: 选择性削弱匹配母语的大脑预测
- **结论**: 共享主干内嵌语言特化

### 3. 脑-模型对齐
- **共享核心**: 与双语者脑区对应
- **特化区域**: 与语言熟练度相关区域对应
- **因果证据**: 损毁实验提供因果推断框架

## Activation Keywords
- computational lesion
- brain alignment
- multilingual LLM
- fMRI encoding
- causal analysis
- 计算性损毁
- 脑对齐
- 语言神经机制

## Tools Used
- **neuroimaging**: fMRI预处理和分析 (fMRIPrep, Nilearn)
- **LLM**: HuggingFace Transformers, PyTorch
- **encoding models**: 线性/非线性脑编码
- **statistical testing**: 置换检验, 多重比较校正

## Workflow

### Step 1: 数据准备
```python
# fMRI预处理
preprocessed_fmri = fmriprep.run(subject_data)

# 提取时间序列
bold_signals = extract_timeseries(preprocessed_fmri, atlas)

# 刺激文本准备
stories = load_naturalistic_stories(languages=['en', 'zh', 'fr'])
```

### Step 2: LLM嵌入提取
```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('multilingual-llm')
tokenizer = AutoTokenizer.from_pretrained('multilingual-llm')

# 提取层嵌入
embeddings = {}
for layer in layers:
    embeddings[layer] = extract_layer_embeddings(model, stories, layer)
```

### Step 3: 计算性损毁
```python
def create_lesion(model, lesion_type, language=None):
    lesioned_model = copy.deepcopy(model)
    
    if lesion_type == 'shared_core':
        # 识别跨语言重要参数
        important_params = identify_shared_important_params(model)
        zero_params(lesioned_model, important_params)
    
    elif lesion_type == 'language_specific':
        # 识别特定语言重要参数
        important_params = identify_language_specific_params(model, language)
        zero_params(lesioned_model, important_params)
    
    return lesioned_model
```

### Step 4: 脑编码与评估
```python
from sklearn.linear_model import Ridge

# 训练编码模型
def train_encoding_model(embeddings, bold_signals):
    encoder = Ridge(alpha=1.0)
    encoder.fit(embeddings, bold_signals)
    return encoder

# 评估损毁效应
for lesion_type in ['shared_core', 'en_specific', 'zh_specific', 'fr_specific']:
    lesioned = create_lesion(model, lesion_type)
    pred = predict_brain(lesioned, stories, encoder)
    correlation = evaluate_correlation(pred, bold_signals)
    print(f"{lesion_type}: {correlation}")
```

## Examples

### Example 1: 共享核心识别
```python
# 创建共享核心损毁
shared_lesion = create_lesion(model, 'shared_core')

# 比较损毁前后
before = evaluate_brain_prediction(model, fmri_en)
after = evaluate_brain_prediction(shared_lesion, fmri_en)
print(f"英语预测下降: {(before-after)/before*100:.2f}%")

before = evaluate_brain_prediction(model, fmri_zh)
after = evaluate_brain_prediction(shared_lesion, fmri_zh)
print(f"中文预测下降: {(before-after)/before*100:.2f}%")
```

### Example 2: 语言特异性分析
```python
# 创建语言特异性损毁
en_lesion = create_lesion(model, 'language_specific', 'en')
zh_lesion = create_lesion(model, 'language_specific', 'zh')

# 测试跨语言效应
effect_en_on_en = evaluate_lesion(en_lesion, fmri_en)
effect_en_on_zh = evaluate_lesion(en_lesion, fmri_zh)

print(f"英语损毁对英语预测: {effect_en_on_en}")
print(f"英语损毁对中文预测: {effect_en_on_zh}")
```

## Theoretical Implications

### 1. 语言神经基础
- 支持"共享主干+语言特化"理论
- 与双语神经科学证据一致
- 为神经可塑性研究提供新视角

### 2. 人工智能启示
- 多语言模型可解释性
- 参数高效多语言学习
- 跨语言迁移机制理解

### 3. 方法论创新
- 计算性损毁作为神经科学工具
- AI模型作为可控实验系统
- 因果推断新范式

## Limitations

### 1. 模型限制
- 仅测试6种LLM
- 损毁粒度为参数级别
- 未考虑动态处理

### 2. 数据限制
- 仅3种语言
- 自然故事刺激单一类型
- 被试数量有限

### 3. 解释限制
- 相关性非因果性（尽管损毁提供部分因果证据）
- 脑区功能定位粗粒度
- 时间动态信息缺失

## Future Directions

### 1. 扩展研究
- 更多语言（特别是 typologically diverse 语言）
- 更多LLM架构
- 不同类型语言任务

### 2. 方法改进
- 更精细的损毁（注意力头、层级别）
- 动态损毁（时间序列分析）
- 与损伤研究的直接对比

### 3. 临床应用
- 双语失语症理解
- 语言康复训练设计
- 神经发育研究

## References
- arXiv:2604.10627v1 (2026-04-12)
- Authors: Yang Cui, Jingyuan Sun, Yizheng Sun, Yifan Wang, et al.
- Categories: cs.CL, cs.AI

## Related Skills
- brain-fmri-llm-graph
- convergent-representations-linguistic-constructions
- bleg-llm-functions-powerful-fmri

---
_Last updated: 2026-04-14_

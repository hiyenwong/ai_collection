---
name: mtt-bench-social-dominance-mice
description: "多模态大语言模型预测小鼠社会优势行为的基准测试框架。MLLM分析原始行为视频预测优势等级。"
category: "neuroscience"
source: "arXiv:2604.22492"
published: "2026-04-24"
paper_url: "https://arxiv.org/abs/2604.22492"
tags: ["animal behavior", "social dominance", "multimodal LLM", "mouse behavior", "MTT-Bench"]
---

# MTT-Bench: Predicting Social Dominance in Mice via Multimodal Large Language Models

## 概述

多模态大语言模型预测小鼠社会优势行为的基准测试框架。MLLM分析原始行为视频预测优势等级。

**来源论文**: [MTT-Bench: Predicting Social Dominance in Mice via Multimodal Large Language Models](https://arxiv.org/abs/2604.22492)

**发表日期**: 2026-04-24

**arXiv ID**: 2604.22492

---

## 核心方法论


核心方法论：
1. **多模态行为分析**
   - 处理小鼠原始行为视频
   - 多模态大语言模型(MLLM)分析
   - 端到端行为理解

2. **社会优势预测**
   - 自动识别社会互动行为
   - 预测优势层级关系
   - 行为模式建模

3. **应用领域**
   - 神经科学研究
   - 行为学研究
   - 动物模型分析
   - 多模态视频理解


---

## 应用场景

- 动物行为分析
- 神经科学研究
- 社会行为建模
- 多模态视频理解

---

## 触发关键词

`animal behavior`, `social dominance`, `multimodal LLM`, `mouse behavior`, `MTT-Bench`

---

## 技术要点

### 模型架构
- 基于最新的生成模型和神经科学技术
- 结合了深度学习和神经科学理论
- 支持多模态数据融合

### 数据要求
- 神经影像学数据（fMRI、EEG、MRI等）
- 行为数据（动物或人类）
- 临床变量（年龄、性别、健康状况等）

### 评估指标
- 图像重建质量（PSNR、SSIM）
- 分类准确性
- 时间一致性
- 解剖学合理性

---

## 实现参考

### Python依赖
```bash
pip install torch torchvision torchaudio
pip install diffusers transformers
pip install numpy scipy matplotlib
pip install mne  # EEG处理
pip install nibabel  # 神经影像
```

### 代码示例
```python
# 根据具体应用场景实现
# 参考原论文的实现细节
```

---

## 相关论文

- MTT-Bench: Predicting Social Dominance in Mice via Multimodal Large Language Models
- arXiv:2604.22492

---

## 更新日志

- **2026-04-24**: 基于arXiv论文创建技能

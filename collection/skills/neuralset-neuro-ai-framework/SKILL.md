---
name: neuralset-neuro-ai-framework
description: NeuralSet unified Python framework for Neuro-AI research, harmonizing diverse neural recordings (fMRI, M/EEG, spikes) with deep learning embeddings
category: neuroscience
authors: ["Jean-Rémi King", "Corentin Bel", "Linnea Evanson", "Julien Gadonneix", "Sophia Houhamdi", "Jarod Lévy", "Josephine Raugel", "Andrea Santos Revilla", "Mingfang Zhang", "Julie Bonnaire", "Charlotte Caucheteux", "Alexandre Défossez", "Théo Desbordes", "Pablo Diego-Simón", "Shubh Khanna", "Juliette Millet", "Pierre Orhan", "Saarang Panchavati", "Antoine Ratouchniak", "Alexis Thual", "Teon L. Brooks", "Katelyn Begany", "Yohann Benchetrit", "Marlène Careil", "Hubert Banville", "Stéphane d'Ascoli", "Simon Dahan", "Jérémy Rapin"]
arxiv_id: "2605.03169"
submission_date: "2026-05-04"
doi: "https://doi.org/10.48550/arXiv.2605.03169"
github: "https://github.com/neuralsign/neuralset"
tags: ["neuro-ai", "python framework", "data harmonization", "fMRI", "EEG", "MEG", "spike recordings", "deep learning embeddings", "lazy loading", "memory-efficient", "scalable infrastructure"]
activation_keywords: ["neuro-ai", "neural data preprocessing", "fMRI EEG MEG harmonization", "deep learning embeddings for neuroscience", "lazy loading", "memory-efficient neural data", "PyTorch-ready neural data", "neural dataset scaling", "computational provenance"]
---

# NeuralSet: A High-Performing Python Package for Neuro-AI

## 概述

NeuralSet是统一的Python框架，高效处理多样化神经记录（fMRI, M/EEG, spikes）和复杂实验刺激（文本、音频、视频），将神经预处理管道与预训练深度学习嵌入无缝集成。

## 核心创新

### 1. 模态无关的数据统一

**问题**：当前神经科学软件工具分散，按记录模态隔离，无法跨模态整合。

**解决方案**：
- 单一接口统一处理fMRI、EEG、MEG、spike recordings
- 标准化数据提取管道，消除模态差异
- 支持复杂实验刺激（文本、音频、视频）的嵌入生成

**数据流架构**：
```
原始数据 → 模态适配器 → 标准化提取 → 深度嵌入 → PyTorch张量
[fMRI, EEG, MEG, spikes] + [text, audio, video] → unified interface
```

### 2. 惰性加载与内存效率

**机制**：
- 解耦实验元数据与惰性数据提取
- 仅加载当前所需数据片段，避免全数据集内存占用
- 支持大规模自然数据集处理（GB级→TB级）

**实现策略**：
```python
# 惰性加载伪代码
class NeuralDataset:
    def __init__(self, metadata_path):
        self.metadata = load_metadata(metadata_path)  # 小型元数据
        self.data_paths = parse_data_paths(metadata)
        self.lazy_loader = LazyLoader()  # 惰性加载器
    
    def get_sample(self, index):
        # 仅加载单个样本，不预加载全数据集
        return self.lazy_loader.load(self.data_paths[index])
    
    def __iter__(self):
        # 流式迭代，内存占用恒定
        for i in range(len(self)):
            yield self.get_sample(i)
```

**内存优化**：
- 元数据（KB级）与实际数据（GB级）分离
- 按需加载，峰值内存降至样本级别
- 支持无限大小数据集迭代

### 3. PyTorch-ready接口

**标准化输出**：
- 直接输出PyTorch张量，无需手动转换
- 标准化维度：`[samples, channels, time]` 或 `[samples, features]`
- 集成PyTorch DataLoader

**接口示例**：
```python
from neuralset import NeuralDataset
from torch.utils.data import DataLoader

# 模态无关加载
fmri_set = NeuralDataset("path/to/fmri/", modality="fMRI")
eeg_set = NeuralDataset("path/to/eeg/", modality="EEG")
spike_set = NeuralDataset("path/to/spikes/", modality="spikes")

# PyTorch DataLoader集成
loader = DataLoader(fmri_set, batch_size=32, shuffle=True)
for batch in loader:
    # batch已是PyTorch张量
    model(batch)
```

### 4. 深度学习嵌入集成

**预训练模型集成**：
- 文本：BERT、GPT、LLaMA嵌入
- 音频：wav2vec、HuBERT嵌入
- 视频：CLIP、ViT嵌入
- 神经数据：预训练神经编码模型

**嵌入生成流程**：
```
刺激 → 预训练模型 → 嵌入向量 → 对齐神经数据
文本 → BERT → 768维向量 → 对应fMRI时间点
音频 → wav2vec → 512维向量 → 对应EEG窗口
视频 → CLIP → 512维向量 → 对应spike序列
```

### 5. 计算可追溯性

**全管道追踪**：
- 记录每个数据样本的处理路径
- 版本控制预处理步骤
- 重现性保证：相同元数据→相同输出

**追溯机制**：
- 元数据包含处理版本、参数、时间戳
- 数据指纹（hash）确保一致性
- 自动记录数据变换历史

## 方法论框架

### 架构层次

1. **元数据层**（Metadata Layer）
   - 实验设计信息
   - 数据路径映射
   - 处理参数配置

2. **数据适配器层**（Adapter Layer）
   - fMRI适配器：NIfTI→标准张量
   - EEG/MEG适配器：Raw/BDF→标准张量
   - Spike适配器：MEA→标准张量

3. **嵌入层**（Embedding Layer）
   - 文本嵌入器
   - 音频嵌入器
   - 视频嵌入器

4. **接口层**（Interface Layer）
   - PyTorch Dataset接口
   - DataLoader集成
   - 分布式训练支持

### 关键组件

| 组件 | 功能 | 实现 |
|------|------|------|
| MetadataParser | 解析实验元数据 | JSON/YAML |
| LazyLoader | 惰性数据加载 | h5py/npy lazy |
| ModalityAdapter | 模态标准化 | 适配器模式 |
| EmbeddingGenerator | 生成深度嵌入 | 预训练模型 |
| ProvenanceTracker | 追溯处理历史 | 日志+hash |

### 数据标准化

**统一维度规范**：
- fMRI：`[samples, voxels, time]`
- EEG/MEG：`[samples, channels, time]`
- Spikes：`[samples, neurons, time_bins]`
- 刺激嵌入：`[samples, embedding_dim]`

**时间对齐**：
- 神经数据与刺激时间戳精确对齐
- 自动处理采样率差异
- 支持动态时间窗口

## 应用场景

### 1. 跨模态神经-AI研究

- **多模态融合**：同时分析fMRI+EEG+行为数据
- **刺激-神经对应**：文本/音频/视频刺激→神经响应建模
- **大规模研究**：TB级数据集处理（自然观看实验）

### 2. 预训练神经编码模型

- 利用NeuralSet统一接口训练多模态编码器
- 跨数据集迁移学习
- 标准化基准测试

### 3. 计算神经科学管道

- 替代分散工具（MNE, Nilearn, SpikeInterface）
- 单一框架完成预处理+分析
- 降低入门门槛

### 4. 实验重现

- 完整计算追溯
- 版本化处理步骤
- 一键重现他人研究

## 技术实现要点

### 安装与使用

```bash
pip install neuralset
```

```python
from neuralset import NeuralDataset

# 加载fMRI数据（自然观看实验）
fmri_set = NeuralDataset(
    "data/movie_fmri/",
    modality="fMRI",
    stimulus_type="video",
    embedding_model="CLIP"  # 自动生成视频嵌入
)

# 加载EEG数据（语言任务）
eeg_set = NeuralDataset(
    "data/speech_eeg/",
    modality="EEG",
    stimulus_type="audio",
    embedding_model="wav2vec"
)

# 惰性迭代（内存高效）
for neural, stimulus in fmri_set:
    # neural: fMRI张量 [voxels, time]
    # stimulus: CLIP嵌入 [embedding_dim]
    correlation = compute_correlation(neural, stimulus)
```

### 分布式训练支持

```python
# 高性能集群执行
from neuralset import DistributedDataset

dist_set = DistributedDataset(
    "cluster://hpc/neural_data/",
    modality="fMRI",
    backend="ray"  # 或 "dask", "slurm"
)

# 分布式DataLoader
dist_loader = DistributedLoader(dist_set, batch_size=128)
```

### 扩展新模态

```python
from neuralset import register_adapter

# 注册自定义模态适配器
@register_adapter("new_modality")
class NewModalityAdapter:
    def load(self, path):
        # 自定义加载逻辑
        return standardized_tensor
```

## 性能优势

| 特性 | 传统工具 | NeuralSet |
|------|----------|-----------|
| 模态支持 | 单模态 | **多模态统一** |
| 内存效率 | 全数据加载 | **惰性加载** |
| 数据集规模 | GB级限制 | **TB级支持** |
| DL集成 | 手动转换 | **PyTorch-ready** |
| 计算追溯 | 手动记录 | **自动追踪** |
| 重现性 | 低 | **高** |

## 与现有工具对比

| 工具 | 模态 | 惰性加载 | DL集成 | 追溯性 |
|------|------|----------|--------|--------|
| MNE | EEG/MEG | 部分 | ✗ | 低 |
| Nilearn | fMRI | 部分 | ✗ | 低 |
| SpikeInterface | Spikes | ✗ | ✗ | 低 |
| h5py | 通用 | ✓ | ✗ | 低 |
| **NeuralSet** | **全模态** | **✓** | **✓** | **高** |

## 局限与未来方向

### 当前局限

1. 预训练嵌入模型依赖外部库
2. 复杂预处理（如EEG滤波）需配置
3. 大规模集群需特定后端

### 未来扩展

1. 更多预训练嵌入模型集成
2. 端到端预处理管道（滤波、artifact removal）
3. 实时数据处理支持
4. Web界面可视化

## 学术影响

- **降低入门门槛**：单一框架替代多工具学习
- **加速研究**：数据加载时间从小时→分钟
- **提升重现性**：计算追溯消除"不可重现"问题
- **促进跨领域合作**：统一接口便于数据共享

## 关键术语

- **NeuralSet**：神经科学-AI统一Python框架
- **惰性加载**：Lazy loading，按需加载避免内存溢出
- **计算追溯**：Computational provenance，记录处理历史
- **模态适配器**：Modality adapter，标准化不同记录格式
- **深度嵌入**：Deep embedding，预训练模型的特征向量
- **PyTorch-ready**：直接输出PyTorch张量格式

---

**Activation**: 当讨论神经科学数据处理、多模态神经数据、深度学习与神经科学融合、大规模神经数据集、预处理管道、数据标准化、计算重现性时激活此技能。

**Related Skills**:
- `mle-toolbox-eeg-meg` (EEG/MEG分析)
- `neuroset-neuro-ai-framework` (相关)
- `brain-dit-fmri-foundation-model` (fMRI基础模型)
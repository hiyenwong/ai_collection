# NeuroGraph - Brain Connectomics Graph ML Benchmarks

## Overview

脑连接组学图机器学习基准数据集集合。包含 35 个数据集，覆盖静态和动态脑连接，用于预测多种行为和认知特征。解决神经影像领域图 ML 应用中预处理流程多样性和参数搜索空间大的挑战。

**来源论文：** arXiv:2306.06202 - NeuroGraph: Benchmarks for Graph Machine Learning in Brain Connectomics

## 触发词

NeuroGraph、脑连接图基准、脑网络 GNN 基准、brain connectomics benchmark、graph ML neuroimaging、fMRI graph dataset

## 核心内容

### 数据集特性

- **35 个图数据集**
- 静态脑连接
- 动态脑连接
- 行为/认知特征预测

### 解决的挑战

1. 预处理流程多样性
2. 图数据集构建参数空间大
3. 缺乏统一基准

### 应用场景

- 神经疾病预测
- 认知特征预测
- 行为模式识别
- 图 ML 方法评估

## 使用场景

### 适用情况

- 脑连接 GNN 研究
- 神经影像 ML 基准
- 认知预测模型评估
- 图方法对比研究

### 数据要求

- fMRI 功能连接数据
- 行为/认知标签

## 实施步骤

1. **数据集获取**
   - 下载 NeuroGraph 数据集
   - 选择合适的子集

2. **预处理选择**
   - 确定连接计算方法
   - 选择图构建参数

3. **模型训练**
   - 图神经网络架构选择
   - 超参数优化

4. **评估对比**
   - 与基准方法比较
   - 消融实验

## 技术细节

### 数据集分类

| 类型 | 特点 |
|------|------|
| 静态连接 | 单一连接矩阵 |
| 动态连接 | 时间序列连接 |
| 多尺度 | 不同分辨率 |

### 图构建参数

- 节点定义（脑图谱选择）
- 边权重（相关性类型）
- 阈值化策略

## 与其他基准对比

| 基准 | 数据集数 | 脑特异性 | 动态支持 |
|------|---------|---------|---------|
| NeuroGraph | 35 | ✅ | ✅ |
| OGB | 多个 | ❌ | ❌ |
| BrainGB | 有限 | ✅ | ⚠️ |

## 工具使用

- `exec`: 运行 PyTorch Geometric
- `read`: 查看数据集配置
- `web_fetch`: 获取数据集链接

## 注意事项

- 预处理流程影响结果
- 图构建参数需报告
- 不同任务选择合适数据集

## 扩展阅读

- 相关技能：`multimodal-brain-connectivity-gnn`（多模态 GNN）
- 相关技能：`contrastpool-brain-network`（对比图池化）
- 论文链接：https://arxiv.org/abs/2306.06202
---
name: gammanet-perceptual-grouping-recurrent
description: Use when modeling incremental perceptual grouping in natural scenes with recurrent hGRU dynamics predicting human RTs.
category: ai_collection
trigger_words: [perceptual grouping, GammaNet, hGRU, incremental grouping, object-based attention, recurrent processing, C-RBP, growth cone, contour propagation, visual cortex feedback]
paper: "arXiv:2610.05419"
---

# Recurrent Network Dynamics Explain the Time Course of Perceptual Grouping in Natural Scenes (GammaNet)

**来源**: Mollard, Ashok, Goetschalckx, Linsley, Serre, Bohte, Roelfsema — arXiv:2610.05419, 2026-10-04, q-bio.NC
（Brown / Donders / KU Leuven 多实验室合作）

## 核心论点

大脑将图像元素组合成连贯物体的机制可以由**循环神经网络的自然图像分割训练**中涌现：
1. 增强活动从线索点沿物体表征**传播**（模拟 object-based attention 扩散）
2. 早期传播遵循**局部边界证据**；后期由**高层语义反馈**跨越内部边缘
3. 网络动力学**从未用反应时间训练**，却预测人类 RT 方差 19.7%（噪声上限 19.8%）

## 架构（GammaNet）

```
Panoptic FPN (R101, COCO预训练, 冻结)
    → projection block (降维映射)
    → GammaNet: 4层 retinotopic hGRU（逐层粗化）
        - 每层: feedforward + feedback + horizontal 连接
        - 抑制性交互 → surround suppression
        - 兴奋性交互 → 活动空间扩散（grouping）
    → 最低层线性读出 → 逐像素类别标签
```

- **输入特性**（关键洞察）：FPN 表征已含可解码的语义+边界信息（相似语义区域在特征空间聚类），但**不含物体级分组**（同类多物体无法区分）
- **任务设计**：给线索物体的类别标签分配给该物体所有像素，其余为背景 → 每个训练样本 = 大量 same-different 判断的隐式监督
- **预测类别而非二值标签** 改善收敛
- **学习规则**：C-RBP（contractor recurrent backpropagation）——梯度计算不需存储完整活动轨迹，**时间上局部**，由附件网络传播 credit assignment，突触局部可得更新信号（生物学合理性强于 BPTT）

## 关键结果

| 指标 | 数值 | 对比 |
|------|------|------|
| 分割 IoU | 0.74±0.01 (N=5) | SAM 0.81（但 SAM 632M 参数 vs 8M；23M vs 5M image-passes） |
| 人类 RT 方差解释 | 19.7% | 噪声上限 19.8%（几乎全部可解释方差） |
| heldout 泛化 | 78% 准确 | 人类 90%（模型判据更严） |
| 3层 vs 4层 | 显著更差 (p<10⁻⁶) | 多尺度必要性 |

### 分组两阶段动力学（核心机制）

1. **早期（局部边界阶段）**：增强活动从线索扩散，遇到内部边缘（光照/颜色/纹理变化或遮挡产生的边）会**暂时停止**，把同一物体的区域隔开——V1 对真实边界与内部边缘同样响应
2. **后期（语义整合阶段）**：高层类别相关活动使分组信号**跨越内部边缘**，建立全局一致的物体表征——对应皮层中边界响应被真实物体边界压过、反馈携带语义信息到早期皮层的阶段

### 内部边缘的距离效应（可检验预测）

- 线索**靠近**边缘：边缘先被当作物体边界，信号沿边传播 → 删除边缘加速分组（平均延迟 2.3±0.33 timesteps, p=0.0024）
- 线索**远离**边缘：无延迟（0.02±0.64, p=0.98）——到达时更大物体部分的活动已提供足够语义证据
- 交互效应 ANOVA F(1,4)=7.9, p=0.048

### 与前代模型对比

- Growth-Cone 模型 / Mollard et al. 2026：只在轮廓刺激（人工边界）上有效，**把边界当作给定**
- Adeli et al. 2023（transformer affinity 迭代选择）：7.3% RT 方差——分组动力学由**外部过程**产生而非网络自身
- Adeli et al. 2026（+RT读出网络）：20.5%，与 GammaNet 相当（p=0.82），但**需要 RT 监督训练**
- GammaNet：唯一**无 RT 训练**、直接由循环动力学产生分组传播、在自然图像上区分真实边界与内部边缘的模型

## 可复用方法论模式

### 模式 A：分割目标 → 涌现心理学
- 用逐像素类别分配训练循环网络，让分组/注意扩散作为**副产品涌现**
- 每个样本隐式编码大量配对 same-different 判断 → 高效监督
- 检验：将网络"信号到达时间"映射为 RT 预测，与人类数据对比（本文达到噪声上限）

### 模式 B：两阶段分组检验协议
1. 构造含内部边缘（遮挡/纹理变化）的自然图像
2. 操纵线索-边缘距离（near/far）
3. 测量分组信号到达远端目标位置的时间
4. 预期：近线索有边缘延迟、远线索无——检验模型是否学到"边界先阻后跨"

### 模式 C：C-RBP 局部学习
- RBP 变体：不存活动轨迹、时间局部、附件网络传 credit assignment
- 适合生物学合理性要求或长序列内存受限场景
- 收敛代价：需 21000 步训练 5 网络

### 模式 D：多尺度必要性消融
- 删一层（4→3）RT 预测显著退化 → 表征多尺度是分组必要条件

## 神经科学对应

- 前馈 sweep → FPN 上采样结构（RF 增大 + 类别涌现 + 反馈整合）
- V1 边界响应（真边+内边同样激活）→ GammaNet 输入中可解码边界（图3E）
- 后期反馈携带语义到未受刺激的 retinotopic 区 → hGRU 高层到低层反馈
- Object-based attention 增量扩散 → 增强活动传播，RT 随元素距离增长

## 局限

- 人类 90% vs 模型 78%（模型判据更严，非直接可比）
- 依赖冻结 FPN 提供语义表征（皮层对应的是可训练的完整层级）
- C-RBP 收敛慢于 BPTT

## 标签

`#perceptual-grouping` `#GammaNet` `#hGRU` `#recurrent-dynamics` `#object-based-attention` `#visual-cortex` `#C-RBP` `#human-RT-prediction` `#natural-scenes` `#incremental-grouping`

---
name: grid-place-co-emergence
description: "网格细胞与位置细胞共同涌现的统一循环网络模型。首次在满足Dale定律的单目标模型中实现grid和place cells的协同涌现，无需监督或预定义空间表征。适用于计算神经科学、空间导航、海马体-内嗅皮层回路建模。"
---

# Grid-Place Co-Emergence: A Unified Recurrent Network Model

> 首次提出grid cells和place cells在统一循环神经网络中协同涌现的模型，
> 仅通过感官预测任务驱动，无需监督标签或预定义空间细胞类型。

## Metadata
- **Source**: arXiv:2605.21356 [q-bio.NC]
- **Authors**: Zhaoze Wang, Genela Morris, Dori Derdikman, Pratik Chaudhari, Vijay Balasubramanian
- **Published**: 2026-05-21 (Thursday)
- **Affiliations**: University of Pennsylvania, Tel Aviv University, Technion, Santa Fe Institute

## Core Contribution

### 核心突破
首次在**满足Dale定律**（每个神经元为兴奋性或抑制性）的循环神经网络中，通过**单一目标函数**（感官预测）实现grid cells和place cells的共同涌现。此前的研究要么分别建模两种细胞类型，要么依赖已存在的空间表征。

### 关键发现
1. **协同共存**：两种空间编码在1,000种不同训练配置下稳定共存
2. **平衡机制**：感官噪声和掩码程度决定两种空间编码的比例
3. **实验复现**：无需重新训练即可复现：
   - 发夹迷宫中的grid碎片化现象
   - 移除墙壁后的grid合并
   - 连接房间中的晶格对齐
   - 自由飞行蝙蝠中的局部有序3D场
   - 位置细胞先于网格细胞出现的发育顺序

## Technical Framework

### 模型架构

#### 网络结构
- 循环神经网络（RNN）实现路径整合
- 遵循Dale定律：神经元分为兴奋性和抑制性两组
- 统一架构同时表征海马体和内嗅皮层功能

#### 训练目标
单一的感官预测目标函数分解为两个互补的压力：
1. **重建压力**：从掩码的感官观察中纠正错误或重建缺失成分
2. **预测压力**：在导航过程中预测下一个感官状态

### 计算原理

#### 压力1：错误纠正与重建
- 从部分观察中重建完整感官信息
- 驱动位置细胞样编码的形成
- 表征当前场景的瞬时状态

#### 压力2：运动预测
- 整合自我运动信息预测未来状态
- 驱动网格细胞样编码的形成
- 支持路径整合功能

### 两编码压力的平衡
- 感官噪声水平调节两种压力的相对贡献
- 高噪声环境强化位置编码
- 低噪声环境强化网格编码
- 为发育顺序提供自然解释

## Experimental Validation

### 复现的实验现象

| 现象 | 描述 |
|------|------|
| Grid碎片化 | 在发夹迷宫结构中grid细胞呈现不连续模式 |
| Grid合并 | 移除墙壁后grid字段合并为连续模式 |
| 晶格对齐 | 连接房间间网格晶格保持对齐 |
| 3D空间编码 | 自由飞行蝙蝠的局部有序3D网格场 |
| 发育顺序 | 位置细胞先于网格细胞在模型中涌现 |

### 可验证的预测
- 两种空间编码的发育时间窗口
- 感官噪声对编码平衡的调节作用
- 路径整合误差与编码类型的关系

## Applications & Implications

### 对计算神经科学的贡献
1. **统一理论**：将grid和place cell的涌现纳入统一框架
2. **电路层面解释**：提供回路级别的协同涌现解释
3. **发育机制**：自然解释位置编码的发育顺序

### 对AI的启示
1. **生物合理SLAM**：启发类脑空间导航系统设计
2. **多任务学习**：单一目标函数产生多种功能编码
3. **生物约束学习**：Dale定律约束的RNN训练方法

## Pitfalls & Limitations
- 模型使用简化感官输入，与真实生物感官处理存在差距
- 训练方式为梯度下降，与生物学习机制有本质不同
- 网格细胞的精确六边形周期性和模块化结构未完全复现
- 模型未纳入海马体-内嗅皮层间的详细解剖连接

## Activation Keywords
- grid cell, place cell, co-emergence, spatial navigation
- hippocampal-entorhinal circuit, path integration
- 网格细胞, 位置细胞, 共同涌现, 空间导航
- 海马体-内嗅皮层, 路径整合

## Related Skills
- grid-cell-normative-theory-review
- hippocampal-entorhinal-world-model
- brain-inspired-nca

## References
- Original Paper: https://arxiv.org/abs/2605.21356
- Related: Cueva & Wei (2018), Banino et al. (2018), Hafting et al. (2005)
- Dale's Law implications for RNN: more biologically plausible training

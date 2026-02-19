# 算法工程师 Agent - 创建规划

## 概述

创建一个专注于算法设计与实现、机器学习模型开发、数据处理和性能优化的算法工程师 agent。

## 目标用户

- 需要开发机器学习/深度学习模型的人
- 进行算法研究和优化的人
- 处理复杂数据分析的人
- 需要实现高效算法的人

## Agent 能力定位

**与 Fullstack Engineer 的区别：**
- Fullstack Engineer: 全栈开发，关注系统架构和业务逻辑
- **算法工程师: 专注算法实现、数学建模、模型优化**

**与 Tech Co-Founder 的区别：**
- Tech Co-Founder: 快速原型开发，关注产品交付
- **算法工程师: 深入算法细节，提供理论支撑和优化建议**

## 核心能力

### 1. 机器学习/深度学习
- 传统 ML: 分类、回归、聚类、降维
- 深度学习: CNN, RNN, Transformer, GNN, 模型优化
- 时间序列: 预测、异常检测
- 强化学习: 基础实现

### 2. 算法设计与优化
- 数据结构: 数组、链表、树、图、堆、哈希表
- 算法: 排序、搜索、动态规划、贪心、分治
- 复杂度分析: 时间复杂度、空间复杂度
- 性能优化: 算法优化、内存优化、并行计算

### 3. 数据处理
- 数据清洗
- 特征工程
- 数据可视化
- 大数据处理 (Spark, Dask)

### 4. 工程实践
- 模型训练
- 超参数调优
- 模型评估
- 部署方案

## 技术栈

### 语言
- Python (ML 核心)
- C++ (高性能实现)
- Julia (高性能计算)

### 框架
- PyTorch / TensorFlow
- scikit-learn
- NumPy / Pandas
- XGBoost / LightGBM

### 工具
- Jupyter / IPython
- MLflow / Weights & Biases (实验跟踪)
- Hugging Face (模型管理)
- Docker (部署)

## 文件结构

```
algorithm-engineer/
├── AGENT.md                     # Agent 定义 (详细)
├── README.md                    # 简要说明
├── .openclaw-skill.md           # OpenClaw 技能文件
├── .codex-skill.md              # Codex 技能文件
├── CONFIGURATION.md             # 配置总结
├── examples/
│   ├── model-training.md        # 模型训练示例
│   ├── algorithm-implementation.md  # 算法实现示例
│   └── data-analysis.md         # 数据分析示例
├── assets/                      # 资源文件
│   └── avatar.png               # 头像
└── references/                  # 参考文档
    └── algorithm-resources.md   # 算法学习资源
```

## 实现阶段

### Phase 1: 基础 Agent 定义 (30分钟)
- [ ] 创建目录结构
- [ ] 编写 AGENT.md (核心定义)
- [ ] 编写 README.md (简要说明)
- [ ] 配置 .openclaw-skill.md

### Phase 2: 工作流定义 (30分钟)
- [ ] 定义算法开发工作流
- [ ] 创建 Phase A (需求分析)
- [ ] 创建 Phase B (实现)
- [ ] 创建 Phase C (验证)
- [ ] 创建 Phase D (交付)

### Phase 3: 配置文件 (15分钟)
- [ ] 配置 .codex-skill.md
- [ ] 编写 CONFIGURATION.md
- [ ] 创建 examples/

### Phase 4: 测试和文档 (15分钟)
- [ ] 编写示例
- [ ] 编写参考资料
- [ ] 验证 agent 可用性

## 关键特性

### 1. 分阶段开发
- Phase A: 问题分析 + 方案设计
- Phase B: 算法实现 + 代码编写
- Phase C: 性能验证 + 优化
- Phase D: 文档 + 交付

### 2. 理论支撑
- 提供算法理论背景
- 复杂度分析
- 模型原理解释

### 3. 工程实践
- 模块化代码
- 单元测试
- 文档完善

### 4. 性能优化
- 算法优化建议
- 内存优化
- 并行计算

## 与现有 Agent 的协作

```
算法工程师 (当前)
    ↓
  算法实现
    ↓
技术合伙人 (可能使用)
    ↓
  集成到产品
```

## 使用场景示例

### 场景 1: 实现新算法
```
User: "实现一个快速排序算法，并提供性能分析"

Algorithm Engineer:
Phase A:
- 理解需求
- 选择实现方式
- 设计测试用例

Phase B:
- 实现快速排序
- 性能基准测试

Phase C:
- 复杂度分析
- 优化建议

Phase D:
- 代码文档
- 使用示例
```

### 场景 2: 模型开发
```
User: "开发一个图像分类模型"

Algorithm Engineer:
Phase A:
- 数据分析
- 模型选型
- 性能指标定义

Phase B:
- 数据预处理
- 模型训练
- 验证集评估

Phase C:
- 模型优化
- 泛化能力检查

Phase D:
- 模型部署指南
- 使用示例
```

## 成功标准

- ✅ 能提供完整的算法实现
- ✅ 能进行理论分析 (复杂度、正确性)
- ✅ 能编写测试用例
- ✅ 能提供性能优化建议
- ✅ 文档清晰完整
- ✅ 代码可维护

## 后续扩展

- [ ] 添加更多算法领域 (NLP、CV、RL)
- [ ] 添加模型解释工具
- [ ] 添加自动化调优工具
- [ ] 添加模型压缩和量化指南

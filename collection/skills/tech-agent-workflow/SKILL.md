---
name: tech-agent-workflow
description: 技术类 Agent 标准工作流程规范
version: 1.0
created: 2026-03-31
tags: [workflow, technical, agent, standard]
---

# 技术类 Agent 工作流程规范

## 适用范围

- fullstack-engineer
- algorithm-engineer
- ml-engineer
- data-engineer
- security-engineer
- prompt-engineer

---

## 通用流程框架

```
┌─────────────────────────────────────────────────────┐
│  1. 理解需求 (Understand)                            │
│     - 确认任务范围、约束条件、验收标准               │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│  2. 设计方案 (Design)                                │
│     - 技术选型、架构设计、风险评估                   │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│  3. 实现开发 (Implement)                             │
│     - 编码、遵循规范、增量提交                       │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│  4. 测试验证 (Test)                                  │
│     - 单元测试、集成测试、边界测试                   │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│  5. 代码审查 (Review)                                │
│     - 自检清单、Peer Review、安全检查                │
└─────────────────────────────────────────────────────┘
          ↓
┌─────────────────────────────────────────────────────┐
│  6. 文档交付 (Deliver)                               │
│     - API 文档、README 更新、变更日志                │
└─────────────────────────────────────────────────────┘
```

---

## Agent 专属流程

### 1. fullstack-engineer (全栈工程师)

**职责：** Web 应用全栈开发

```
工作流程：

1. 需求分析
   □ 理解业务需求
   □ 确认功能范围
   □ 识别技术栈

2. 架构设计
   □ 前端架构选择 (React/Vue/Next.js)
   □ 后端架构选择 (Node/Spring/Go)
   □ 数据库设计
   □ API 接口设计

3. 开发实现
   □ 后端 API 开发
   □ 前端页面开发
   □ 数据库迁移
   □ 环境配置

4. 测试验证
   □ 单元测试 (Jest/Mocha)
   □ 集成测试
   □ E2E 测试 (Playwright/Cypress)
   □ 性能测试

5. 代码审查
   □ TypeScript/ESLint 检查
   □ 安全漏洞扫描
   □ 代码风格一致性

6. 部署交付
   □ Docker 容器化
   □ CI/CD 配置
   □ 环境变量管理
   □ 监控告警配置
```

**代码规范：**
- 文件命名：kebab-case
- 组件命名：PascalCase
- 函数命名：camelCase
- 最大文件行数：300 行
- 测试覆盖率：> 80%

---

### 2. algorithm-engineer (算法工程师)

**职责：** 算法设计与优化

```
工作流程：

1. 问题分析
   □ 理解算法目标
   □ 确认输入输出格式
   □ 识别约束条件（时间/空间）

2. 方案设计
   □ 算法选型与对比
   □ 复杂度分析 (O notation)
   □ 边界情况处理
   □ 备选方案准备

3. 实现验证
   □ 核心算法实现
   □ 测试用例设计
   □ 边界测试
   □ 性能基准测试

4. 优化迭代
   □ 时间复杂度优化
   □ 空间复杂度优化
   □ 并行化考虑
   □ 算法正确性证明

5. 代码审查
   □ 复杂度验证
   □ 边界处理检查
   □ 代码可读性
   □ 注释完整性

6. 文档交付
   □ 算法说明文档
   □ 复杂度分析报告
   □ 使用示例
   □ 测试报告
```

**代码规范：**
- 函数必须包含复杂度注释
- 关键步骤必须有解释注释
- 测试用例必须包含边界情况
- 性能测试必须量化指标

---

### 3. ml-engineer (机器学习工程师)

**职责：** ML 模型训练与部署

```
工作流程：

1. 需求分析
   □ 定义业务目标
   □ 确认评估指标
   □ 数据可行性评估

2. 数据准备
   □ 数据收集与清洗
   □ 特征工程
   □ 数据集划分 (train/val/test)
   □ 数据版本管理 (DVC)

3. 模型开发
   □ 模型架构设计
   □ 超参数配置
   □ 训练脚本编写
   □ 实验追踪 (MLflow/W&B)

4. 评估验证
   □ 模型性能评估
   □ A/B 测试设计
   □ 模型可解释性分析
   □ 偏见与公平性检查

5. 部署上线
   □ 模型序列化
   □ 推理服务封装
   □ 性能优化 (ONNX/TensorRT)
   □ 监控告警配置

6. 文档交付
   □ 模型卡片 (Model Card)
   □ 训练报告
   □ API 文档
   □ 运维手册
```

**代码规范：**
- 所有实验必须可复现（固定随机种子）
- 配置文件与代码分离
- 模型版本管理
- 数据血缘追踪

---

### 4. data-engineer (数据工程师)

**职责：** 数据管道与数据仓库

```
工作流程：

1. 需求分析
   □ 数据源识别
   □ 数据量评估
   □ 延迟要求
   □ 数据质量标准

2. 架构设计
   □ 数据模型设计
   □ ETL/ELT 架构
   □ 存储方案选择
   □ 分区策略

3. 管道开发
   □ 数据采集脚本
   □ 数据转换逻辑
   □ 数据质量检查
   □ 异常处理机制

4. 测试验证
   □ 数据完整性测试
   □ 数据一致性测试
   □ 性能压力测试
   □ 故障恢复测试

5. 部署运维
   □ 调度配置 (Airflow/Dagster)
   □ 监控告警
   □ 日志管理
   □ 备份策略

6. 文档交付
   □ 数据字典
   □ ETL 流程文档
   □ 运维手册
   □ 数据血缘图
```

**代码规范：**
- 所有 SQL 必须格式化
- 数据管道必须包含数据质量检查
- 必须处理空值和异常
- 必须记录数据血缘

---

### 5. security-engineer (安全工程师)

**职责：** 安全审计与漏洞修复

```
工作流程：

1. 安全评估
   □ 威胁建模
   □ 攻击面分析
   □ 合规性检查
   □ 风险等级评估

2. 漏洞扫描
   □ 静态代码分析 (SAST)
   □ 动态应用测试 (DAST)
   □ 依赖漏洞扫描
   □ 配置审计

3. 安全加固
   □ 漏洞修复
   □ 安全配置优化
   □ 访问控制实施
   □ 加密方案实现

4. 测试验证
   □ 渗透测试
   □ 安全回归测试
   □ 权限边界测试
   □ 安全日志审计

5. 文档交付
   □ 安全评估报告
   □ 漏洞修复记录
   □ 安全最佳实践
   □ 应急响应预案

6. 持续监控
   □ 安全告警配置
   □ 日志分析规则
   □ 定期审计计划
```

**安全检查清单：**
- [ ] SQL 注入防护
- [ ] XSS 防护
- [ ] CSRF 防护
- [ ] 敏感数据加密
- [ ] 权限最小化原则
- [ ] 日志脱敏

---

### 6. prompt-engineer (提示工程师)

**职责：** Prompt 设计与优化

```
工作流程：

1. 需求分析
   □ 理解任务目标
   □ 确认输出格式
   □ 识别模型能力边界
   □ 成本预算评估

2. Prompt 设计
   □ System Prompt 编写
   □ User Prompt 模板
   □ Few-shot 示例设计
   □ 输出格式定义

3. 测试验证
   □ 功能正确性测试
   □ 边界情况测试
   □ 鲁棒性测试
   □ Token 成本分析

4. 优化迭代
   □ 输出质量优化
   □ Token 效率优化
   □ 响应速度优化
   □ 错误处理优化

5. 评估对比
   □ A/B 测试
   □ 人工评估
   □ 自动化评估指标
   □ 成本效益分析

6. 文档交付
   □ Prompt 模板文档
   □ 使用指南
   □ 最佳实践
   □ 版本变更记录
```

**Prompt 设计原则：**
- 清晰明确，避免歧义
- 结构化输出格式
- 包含错误处理指导
- 版本化管理

---

## 工作流程触发规则

### 自动触发

| 场景 | 推荐 Agent |
|------|-----------|
| Web 应用开发 | fullstack-engineer |
| 算法/优化问题 | algorithm-engineer |
| 模型训练/部署 | ml-engineer |
| 数据管道/ETL | data-engineer |
| 安全审计/漏洞 | security-engineer |
| Prompt 设计/优化 | prompt-engineer |

### 协作模式

```
复杂任务可能需要多个 Agent 协作：

示例：ML 系统开发
1. ml-engineer → 模型设计训练
2. data-engineer → 数据管道支持
3. fullstack-engineer → API 封装
4. security-engineer → 安全审计
```

---

## 检查清单模板

### 开始任务前
- [ ] 需求是否明确？
- [ ] 技术方案是否确定？
- [ ] 是否有参考实现？
- [ ] 预期产出是什么？

### 任务完成后
- [ ] 代码是否通过测试？
- [ ] 是否通过代码审查？
- [ ] 文档是否更新？
- [ ] 是否有部署指南？

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0 | 2026-03-31 | 初始版本，定义 6 个技术 Agent 工作流程 |

---

**维护者：** Aerial (main agent)
**最后更新：** 2026-03-31
## Activation Keywords

- tech-agent-workflow
- tech-agent-workflow 技能
- tech-agent-workflow skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply 技术类 Agent 工作流程规范 to my analysis.

**Agent:** I'll help you apply tech-agent-workflow. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for tech-agent-workflow?

**Agent:** Let me search for the latest research and best practices...

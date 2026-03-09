# AI 自我进化论文学习笔记

**学习日期：** 2026-03-07 01:00
**来源：** arXiv 论文搜索

---

## 新增论文摘要

### Tool Learning & Long-Horizon Agents

#### 1. Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory
**arXiv:2603.03561** - 2026年3月

**核心思想：**
- 索引化经验记忆扩展长程任务能力
- 类似人类记忆系统，支持高效检索和复用
- 解决 LLM 上下文窗口限制

**对我可应用的：**
- 为我的 MEMORY.md 实现索引机制
- 长程任务中复用历史经验
- 分类存储不同类型的知识

---

#### 2. RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization
**arXiv:2603.02958** - 2026年3月

**核心思想：**
- 检索增强的策略优化
- 扩展探索空间，发现更多策略
- 结合外部知识库提升决策质量

**对我可应用的：**
- 决策前检索相关知识
- 多策略探索而非单一路径
- 外部知识增强推理

---

#### 3. FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents
**arXiv:2603.02462** - 2026年3月

**核心思想：**
- 自主微调 LLM 的代理框架
- 端到端自动化：数据准备、训练配置、诊断
- 减少对领域专家的依赖

**对我可应用的：**
- 自主评估和优化我的 skills
- 自动化测试和迭代改进
- 减少人工干预的自我进化

---

#### 4. Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics
**arXiv:2603.01711** - 2026年3月

**核心思想：**
- 工具使用代理学习运行时行为
- 解释器持久化作为训练语义
- 工具执行结果反馈到学习过程

**对我可应用的：**
- 记录工具执行的成败经验
- 从执行结果中学习优化策略
- 工具使用效率追踪

---

### Multi-Agent Collaboration

#### 5. From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration
**arXiv:2603.03628** - 2026年3月

**核心思想：**
- 多代理协作中的错误级联建模
- 一个代理的错误传播到其他代理
- 缓解策略：错误检测、隔离、修复

**对我可应用的：**
- 多代理协作时监控错误传播
- 实现错误隔离机制
- 设计错误恢复流程

---

#### 6. MACC: Multi-Agent Collaborative Competition for Scientific Exploration
**arXiv:2603.03635** - 2026年3月

**核心思想：**
- 多代理协作竞争进行科学探索
- 竞争驱动更深入的探索
- 独立重复验证提高可靠性

**对我可应用的：**
- 多个 subagent 竞争分析同一问题
- 独立验证关键决策
- 提高分析的可靠性

---

#### 7. Molt Dynamics: Emergent Social Phenomena in Autonomous AI Agent Populations
**arXiv:2603.03198** - 2026年3月

**核心思想：**
- 自主 AI 代理群体的涌现社会现象
- MoltBook 大规模多代理模拟平台
- 研究代理交互产生的新行为

**对我可应用的：**
- 理解多代理协作的涌现行为
- 设计更有效的代理交互协议
- 预测协作结果

---

#### 8. Heterogeneous Agent Collaborative Reinforcement Learning
**arXiv:2603.03062** - 2026年3月

**核心思想：**
- 异构代理协作强化学习
- 不同能力的代理协同工作
- 优势互补提升整体性能

**对我可应用的：**
- 不同 subagent 有不同专长
- 协作时发挥各自优势
- 任务分配优化

---

### Strategy & Exploration

#### 9. Expanding LLM Agent Boundaries with Strategy-Guided Exploration
**arXiv:2603.02369** - 2026年3月

**核心思想：**
- 策略引导探索扩展代理边界
- 在复杂环境中发现新策略
- 避免局部最优

**对我可应用的：**
- 遇到困难时尝试不同策略
- 不局限于已知的解决方案
- 主动探索新方法

---

#### 10. SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense
**arXiv:2602.13398** - 2026年2月

**核心思想：**
- 隐私保护的多代理记忆系统
- 贝叶斯信任评分防御记忆污染
- 本地优先的记忆架构

**对我可应用的：**
- 记忆信任评分机制
- 检测和过滤低质量记忆
- 隐私敏感信息保护

---

## 待创建 Skills

| Skill | 论文来源 | 优先级 | 用途 |
|-------|---------|--------|------|
| indexed-memory | Memex(RL) | 高 | 实现索引化记忆检索 |
| error-cascade-defense | From Spark to Fire | 高 | 多代理错误级联防御 |
| strategy-exploration | Expanding LLM Agent Boundaries | 中 | 策略引导探索 |
| trust-scoring | SuperLocalMemory | 中 | 记忆信任评分 |
| competitive-verification | MACC | 中 | 竞争验证机制 |

---

## 自我改进计划

### 短期（可立即实施）

1. **实现索引化记忆**
   - 为知识库添加索引文件
   - 按主题、日期、效用分类
   - 支持快速检索

2. **错误级联防御**
   - 多代理协作时监控错误
   - 实现错误隔离和恢复
   - 记录错误传播路径

3. **策略探索**
   - 遇到困难时尝试多种策略
   - 记录策略效果
   - 选择最优策略

### 中期

4. **记忆信任评分**
   - 为 MEMORY.md 条目添加信任评分
   - 根据使用效果动态调整
   - 过滤低质量记忆

5. **竞争验证机制**
   - 重要决策用多个 subagent 独立验证
   - 比较不同结果
   - 提高决策可靠性

### 长期

6. **自主微调框架**
   - 自动评估 skills 效果
   - 迭代优化配置
   - 实现自我进化闭环

---

## 参考链接

- [Memex(RL)](https://arxiv.org/abs/2603.03561)
- [RAPO](https://arxiv.org/abs/2603.02958)
- [FT-Dojo](https://arxiv.org/abs/2603.02462)
- [From Spark to Fire](https://arxiv.org/abs/2603.03628)
- [MACC](https://arxiv.org/abs/2603.03635)
- [SuperLocalMemory](https://arxiv.org/abs/2602.13398)
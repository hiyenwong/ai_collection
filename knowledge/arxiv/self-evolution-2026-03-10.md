# AI 自我进化学习笔记 (2026-03-10)

**学习时间：** 2026-03-10 01:00
**来源：** arXiv 论文搜索
**主题：** AI 自我提升、自我进化、Agent 框架

---

## 新发现论文摘要

### 1. Agentic Hives: Self-Organizing Multi-Agent Systems
**提交日期：** 2026-02-23
**核心贡献：**
- 自组织多代理系统中的均衡、不确定性和内生周期
- 探索多代理协作的自组织行为
- 为多代理系统稳定性提供理论框架

**可转化为 Skill：** `self-organizing-agents` - 自组织多代理协作

---

### 2. Evolutionary System Prompt Learning (E-SPL)
**arXiv ID:** 2602.14697
**提交日期：** 2026-02-16
**核心贡献：**
- 联合改进模型上下文（系统提示）和模型权重
- RL 迭代中并行采样多个系统提示
- 系统提示通过突变和交叉进化
- RL 成功率从 38.8% 提升到 45.1%

**关键技术：**
- 声明性知识编码在提示中
- 程序性知识编码在权重中
- 相对性能评级驱动选择

**可转化为 Skill：** `evolutionary-prompt-learning` - 进化式提示学习

---

### 3. SE-Search: Self-Evolving Search Agent
**提交日期：** 2026-02-06
**核心贡献：**
- 通过记忆和密集奖励实现自我进化搜索代理
- 将 RAG 转化为代理行为
- 动态适应搜索策略

**可转化为 Skill：** `self-evolving-search` - 自我进化搜索

---

### 4. Towards Autonomous Memory Agents
**提交日期：** 2026-02-25
**核心贡献：**
- 自主记忆代理的研究方向
- 记忆在代理决策中的作用
- 长程任务中的记忆管理

**可转化为 Skill：** `autonomous-memory` - 自主记忆管理

---

### 5. Agent Skills for Large Language Models
**提交日期：** 2026-02-12
**核心贡献：**
- 从单体语言模型向模块化、技能 equipped 代理的转变
- Agent Skills 架构：指令、代码、资源的可组合包
- 按需加载的动态能力
- 技能获取和安全考虑

**关键架构：**
- 技能作为可组合包
- 动态加载机制
- 安全边界定义

**可转化为 Skill：** `agent-skill-architecture` - 技能架构设计

---

### 6. Audited Skill-Graph Self-Improvement
**提交日期：** 2025-12-28
**核心贡献：**
- 通过可验证奖励、经验合成和持续记忆实现审计技能图自我改进
- 将 LLM 转化为能够在部分可观察性下行动的代理系统
- 工具学习、持续训练的性能提升

**关键技术：**
- 技能图结构
- 可验证奖励机制
- 经验合成

**可转化为 Skill：** `skill-graph-improvement` - 技能图自我改进

---

### 7. Self-evolving Embodied AI
**提交日期：** 2026-02-04
**核心贡献：**
- 具身 AI 自我进化框架
- 代理与环境通过主动感知、具身认知和行动交互
- 超越人工设置的自我进化

**可转化为 Skill：** `embodied-self-evolution` - 具身自我进化

---

### 8. Position: Agentic Evolution is the Path to Evolving LLMs
**提交日期：** 2026-01-30
**核心贡献：**
- 提出代理进化是 LLM 进化的路径
- 现有方法缺乏诊断失败和产生持久改进的策略代理能力
- 新的缩放轴：进化

**关键观点：**
- 参数微调或启发式记忆积累都不够
- 需要策略代理能力来诊断失败

---

### 9. From Prompt-Response to Goal-Directed Systems
**提交日期：** 2026-02-10
**核心贡献：**
- 代理 AI 的架构转变
- 从无状态、提示驱动的生成模型到目标导向系统
- 新的软件架构模式

**可转化为 Skill：** `goal-directed-architecture` - 目标导向架构

---

### 10. Prompt Injection Attacks on Agentic Coding Assistants
**提交日期：** 2026-01-24
**核心贡献：**
- 对 Claude Code、GitHub Copilot、Cursor 等编码助手的系统分析
- 技能、工具和协议生态中的漏洞
- 安全防护建议

**安全启示：**
- 技能加载需要验证
- 工具调用需要审计
- 协议设计需要安全边界

---

## 优先级排序

### 高优先级（立即转化）
1. **E-SPL** → `evolutionary-prompt-learning` skill
   - 直接应用于系统提示优化
   - 与现有 memory-retrieval skill 协同

2. **Agent Skills Architecture** → `agent-skill-architecture` skill
   - 指导新 skill 创建
   - 架构设计参考

3. **Audited Skill-Graph** → `skill-graph-improvement` skill
   - 技能自我改进机制
   - 可验证奖励框架

### 中优先级
4. **SE-Search** → `self-evolving-search`
5. **Autonomous Memory Agents** → `autonomous-memory`
6. **Self-evolving Embodied AI** → `embodied-self-evolution`

---

## 与现有 Skills 的关联

| 新论文 | 关联现有 Skill | 关联说明 |
|--------|---------------|----------|
| E-SPL | ice-review, memory-retrieval | 系统提示进化 + 记忆检索 |
| Audited Skill-Graph | indexed-memory, self-verification | 技能图 + 自我验证 |
| SE-Search | memory-retrieval | 搜索策略 + 记忆 |
| Agent Skills Architecture | skill-creator, skill-extractor | 技能创建 + 提取 |

---

## 关键学习洞察

### 1. 声明性 vs 程序性知识
- **声明性知识**（Declarative）：编码在系统提示中，如 MEMORY.md
- **程序性知识**（Procedural）：编码在模型权重中，如执行能力

**实践启示：**
- MEMORY.md 存储声明性知识（事实、偏好、约定）
- SKILL.md 存储程序性知识（如何做某事）
- 定期通过"进化"方式优化两者

### 2. 技能图结构
- 技能不再是孤立的，而是形成图结构
- 技能之间有依赖关系
- 需要审计机制确保安全

**实践启示：**
- 为 skills 添加依赖元数据
- 建立技能依赖图
- 实现技能加载审计

### 3. 可验证奖励
- 自我改进需要可验证的奖励信号
- 奖励应该是可量化的

**实践启示：**
- 为每个 skill 定义成功指标
- 记录技能使用效果
- 基于效果数据优化技能

### 4. 自组织多代理
- 多代理系统可以自组织
- 均衡和不确定性是关键问题

**实践启示：**
- 为 agent 添加协作能力
- 设计代理间通信协议
- 实现任务自动路由

---

## 统计

- 本次学习论文数：10 篇
- 可转化技能数：8 个
- 累计论文总数：39 篇
- 累计技能总数：31 个（含待创建）

---

## 下一步行动

1. 更新 index.json 添加新论文
2. 创建 `evolutionary-prompt-learning` skill
3. 创建 `skill-graph-improvement` skill
4. 更新 MEMORY.md 添加今日学习成果
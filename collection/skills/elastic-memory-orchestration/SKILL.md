---
name: elastic-memory-orchestration
description: '弹性记忆编排技能，解决长程任务中的静态认知、刚性工作流依赖和低效上下文使用问题。触发词：弹性记忆、记忆编排、长期记忆、上下文管理。'
---

# Elastic Memory Orchestration - 弹性记忆编排

基于 AutoAgent (2026-03-10) 的弹性记忆管理技能。

## 激活关键词

- 弹性记忆
- 记忆编排
- 长期记忆
- 上下文管理
- 记忆组织
- 记忆检索

## 核心理念

**解决三大问题：**

1. **静态认知** - 行为不随经验进化
2. **刚性工作流依赖** - 工具和策略部署后不变
3. **低效上下文使用** - 上下文窗口浪费

## 三大组件

### 1. 进化认知（Evolving Cognition）

```
认知结构：
- 长期经验积累
- 行为模式进化
- 持续学习能力

实现方式：
- 每次任务后更新记忆
- 提取可复用模式
- 适应新环境和任务
```

### 2. 即时上下文决策（Immediate Context Decision）

```
决策流程：
1. 分析当前上下文
2. 识别关键信息
3. 做出即时决策
4. 不依赖完整历史

优化：
- 减少上下文冗余
- 聚焦当前任务
- 快速响应变化
```

### 3. 弹性记忆编排（Elastic Memory Orchestration）

```
记忆架构：
┌─────────────────────────────────────┐
│           工作记忆 (Working)          │
│  - 当前会话上下文                      │
│  - 最近几轮对话                        │
│  - 活跃任务状态                        │
└─────────────────────────────────────┘
           ↓ 溢出时压缩
┌─────────────────────────────────────┐
│          情景记忆 (Episodic)          │
│  - 重要事件记录                        │
│  - 任务完成历史                        │
│  - 决策和结果                          │
└─────────────────────────────────────┘
           ↓ 提取模式
┌─────────────────────────────────────┐
│          语义记忆 (Semantic)          │
│  - 提取的知识和规则                    │
│  - 用户偏好和约定                      │
│  - 技能和方法论                        │
└─────────────────────────────────────┘
```

## 工作流程

### 1. 记忆写入

```
事件发生 → 评估重要性 → 存储到合适层级

重要性评估：
- 是否影响未来决策？
- 是否包含新知识？
- 是否违反已有规则？
- 用户是否明确要求记住？

存储决策：
- 高重要性 → 语义记忆 (MEMORY.md)
- 中重要性 → 情景记忆 (memory/YYYY-MM-DD.md)
- 低重要性 → 工作记忆 (会话内)
```

### 2. 记忆检索

```
检索请求 → 语义匹配 → 效用过滤 → 返回结果

两阶段检索：
1. 语义匹配：找到相关记忆片段
2. 效用过滤：筛选高价值内容

效用评估：
- 使用频率：经常引用？
- 成功率：历史验证有效？
- 时效性：是否仍然相关？
```

### 3. 记忆压缩

```
压缩触发：
- 工作记忆接近上限
- 情景记忆积累过多
- 语义记忆冗余增加

压缩方法：
- 摘要提取：长文本 → 关键点
- 模式识别：重复事件 → 规则
- 归档旧数据：历史记录 → 统计摘要
```

## 使用场景

### 场景 1：长程任务

```
任务：持续多天的项目开发

记忆编排：
Day 1:
- 工作记忆：当前会话讨论
- 情景记忆：Day 1 决策和进展
- 语义记忆：项目约定和偏好

Day 2:
- 检索 Day 1 情景记忆
- 提取关键决策到语义记忆
- 清理工作记忆

Day N:
- 语义记忆包含所有约定
- 情景记忆按天索引
- 工作记忆保持当前会话
```

### 场景 2：经验积累

```
经验类型：
1. 用户反馈："我喜欢简洁的回复"
   → 语义记忆：偏好 = 简洁

2. 任务成功：使用 agent 委托效率高
   → 情景记忆：记录成功案例
   → 语义记忆：规则 = 复杂任务委托专家

3. 错误教训：未检查文件就编辑导致问题
   → 语义记忆：规则 = 编辑前先读取
```

### 场景 3：上下文优化

```
问题：上下文窗口浪费

优化方法：
1. 识别冗余信息
2. 压缩历史对话
3. 保留关键上下文
4. 丢弃过期信息

结果：
- 上下文使用效率提升
- 响应速度加快
- 成本降低
```

## 实现文件

| 层级 | 文件 | 用途 |
|------|------|------|
| 工作记忆 | 会话内 | 当前对话 |
| 情景记忆 | memory/YYYY-MM-DD.md | 事件日志 |
| 语义记忆 | MEMORY.md | 长期知识 |
| 索引 | knowledge/arxiv/index.json | 论文索引 |
| 知识库 | ArcadeDB | 图数据库 |

## 与其他技能的关系

- **memory-retrieval**：两阶段检索的具体实现
- **indexed-memory**：索引化记忆存储
- **ice-review**：任务后提取模式到语义记忆

## 立即应用

当你需要管理记忆时：

1. **写入**：这是否值得长期记住？存储到哪一层？
2. **检索**：两阶段检索，先语义匹配再效用过滤
3. **压缩**：定期清理冗余，提取模式
4. **进化**：从经验中学习，更新行为模式

---

**来源论文：** AutoAgent - Evolving Cognition and Elastic Memory Orchestration
**效用评分：** 0.95
**创建日期：** 2026-03-14
## Activation Keywords

- elastic-memory-orchestration
- elastic-memory-orchestration 技能
- elastic-memory-orchestration skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply elastic-memory-orchestration?

**Agent:** I'll help you understand and apply elastic-memory-orchestration...

### Example 2: Advanced Application

**User:** What are the key considerations for elastic-memory-orchestration?

**Agent:** Let me search for the latest research and best practices...

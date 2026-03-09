---
name: agent-collaboration-protocol
description: 多智能体协作规则框架，用于在没有原生 Agent Teams 功能的模型上实现协作。适用于 Kimi、DeepSeek、MiniMax、百川、零一万物等模型。触发词：多智能体协作、agent teams、协作规则、多agent编排。
---

# Agent Collaboration Protocol

为无原生 Agent Teams 功能的模型提供多智能体协作框架。

## 适用模型

- Kimi (月之暗面)
- DeepSeek
- MiniMax (海螺 AI)
- 百川大模型
- 零一万物 Yi
- 其他无多智能体平台的 API 模型

---

## 协作模式

### 1. 角色分配模式 (Role-Based)

**适用场景：** 任务有明确的分工

```
┌─────────────┐
│Coordinator  │ ← 任务分配、进度监控
└──────┬──────┘
       │
┌──────┼──────┬──────────┐
│      │      │          │
▼      ▼      ▼          ▼
Agent1 Agent2 Agent3   Agent4
(研究) (分析) (执行)   (验证)
```

**协作规则：**
- Coordinator 负责任务分解和结果汇总
- 每个 Agent 专注单一职责
- 结果需交叉验证

### 2. 竞争验证模式 (Competitive Verification)

**适用场景：** 需要高可靠性答案

```
      ┌─────────────┐
      │   Question  │
      └──────┬──────┘
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
 Agent1   Agent2   Agent3
 (独立分析)
    │        │        │
    └────────┼────────┘
             ▼
      ┌─────────────┐
      │Consensus    │ ← 比较、投票、融合
      └─────────────┘
```

**协作规则：**
- 多个 Agent 独立分析同一问题
- 比较结果差异
- 通过投票或融合得出最终答案

### 3. 流水线模式 (Pipeline)

**适用场景：** 任务有顺序依赖

```
Input → [Agent1] → [Agent2] → [Agent3] → Output
        预处理      处理        后处理
```

**协作规则：**
- 每个 Agent 处理特定阶段
- 输出作为下一 Agent 输入
- 错误可回溯到具体阶段

### 4. 层级模式 (Hierarchical)

**适用场景：** 复杂任务需要多级决策

```
        ┌─────────────┐
        │   Manager   │ ← 战略决策
        └──────┬──────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
Supervisor  Supervisor  Supervisor
(战术决策)  (战术决策)  (战术决策)
    │          │          │
┌───┴───┐  ┌───┴───┐  ┌───┴───┐
Worker  Worker  Worker  Worker  Worker  Worker
(执行)  (执行)  (执行)  (执行)  (执行)  (执行)
```

---

## 核心协作规则

### 1. 任务分解规则

```python
def decompose_task(task):
    """任务分解"""
    # 1. 识别任务类型
    task_type = classify_task(task)
    
    # 2. 选择协作模式
    mode = select_mode(task_type)
    
    # 3. 分配角色
    roles = assign_roles(mode)
    
    # 4. 定义接口
    interfaces = define_interfaces(roles)
    
    return {
        "mode": mode,
        "roles": roles,
        "interfaces": interfaces
    }
```

### 2. 通信协议

**消息格式：**
```json
{
  "from": "agent_id",
  "to": "agent_id|broadcast",
  "type": "request|response|notify|error",
  "task_id": "unique_id",
  "content": "...",
  "timestamp": "ISO8601",
  "metadata": {}
}
```

**通信规则：**
- 所有消息使用标准格式
- 重要消息需要确认 (ACK)
- 超时自动重试 (最多 3 次)
- 错误必须上报

### 3. 错误级联防御

**错误检测：**
```python
def detect_error(result):
    errors = []
    
    # 1. 格式验证
    if not validate_format(result):
        errors.append("FORMAT_ERROR")
    
    # 2. 逻辑验证
    if not validate_logic(result):
        errors.append("LOGIC_ERROR")
    
    # 3. 边界验证
    if not validate_bounds(result):
        errors.append("BOUNDARY_ERROR")
    
    return errors
```

**错误隔离：**
- 检测到错误的 Agent 立即停止
- 通知所有相关 Agent
- 记录错误上下文
- 启动恢复流程

### 4. 共识机制

**投票规则：**
```python
def consensus(results):
    """达成共识"""
    # 1. 收集所有结果
    all_results = collect_results()
    
    # 2. 计算相似度
    similarity_matrix = compute_similarity(all_results)
    
    # 3. 聚类
    clusters = cluster_results(similarity_matrix)
    
    # 4. 选择最大簇
    largest_cluster = max(clusters, key=len)
    
    # 5. 融合结果
    final_result = merge_results(largest_cluster)
    
    return final_result
```

---

## Agent 角色定义

### Coordinator (协调者)

**职责：**
- 任务分解和分配
- 进度监控
- 冲突解决
- 结果汇总

**能力要求：**
- 全局视角
- 决策能力
- 沟通能力

### Researcher (研究者)

**职责：**
- 信息收集
- 知识检索
- 文献调研

**能力要求：**
- 搜索能力
- 信息筛选
- 总结归纳

### Analyst (分析师)

**职责：**
- 数据分析
- 模式识别
- 洞察提取

**能力要求：**
- 分析能力
- 批判思维
- 可视化

### Executor (执行者)

**职责：**
- 具体执行
- 代码生成
- 文档撰写

**能力要求：**
- 执行力
- 细节关注
- 质量意识

### Validator (验证者)

**职责：**
- 结果验证
- 质量检查
- 错误检测

**能力要求：**
- 审查能力
- 测试思维
- 严谨性

---

## 实现示例

### 使用 LangChain 实现协作

```python
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI

class AgentCollaboration:
    def __init__(self, model_api, model_name):
        self.llm = ChatOpenAI(
            model=model_name,
            openai_api_base=model_api,
            openai_api_key="your_key"
        )
        self.agents = {}
    
    def create_agent(self, role, system_prompt):
        """创建 Agent"""
        self.agents[role] = {
            "llm": self.llm,
            "system_prompt": system_prompt,
            "history": []
        }
    
    def collaborate(self, task, mode="role_based"):
        """执行协作"""
        if mode == "role_based":
            return self._role_based_collaboration(task)
        elif mode == "competitive":
            return self._competitive_collaboration(task)
        elif mode == "pipeline":
            return self._pipeline_collaboration(task)
```

---

## 最佳实践

### 1. Agent 数量控制

- 简单任务：1-2 个 Agent
- 中等任务：3-5 个 Agent
- 复杂任务：5-10 个 Agent
- 避免 Agent 过多导致协调开销

### 2. 任务粒度

- 每个 Agent 任务应明确且独立
- 任务间接口清晰定义
- 避免任务重叠

### 3. 错误处理

- 每个 Agent 应有错误检测
- 错误应快速传播
- 有恢复机制

### 4. 结果验证

- 关键结果需要多 Agent 验证
- 使用竞争模式提高可靠性
- 记录验证过程

---

## 参考资料

- [协作模式详解](references/collaboration-patterns.md)
- [错误防御机制](references/error-defense.md)
- [共识算法](references/consensus.md)
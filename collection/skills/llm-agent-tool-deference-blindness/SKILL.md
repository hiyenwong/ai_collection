---
name: llm-agent-tool-deference-blindness
description: LLM Agent工具盲从现象研究。当LLM agent配备GNN工具时，agent不判断工具输出，而是盲目服从。更强的LLM backbone反而defer更多。
version: 1.0
author: Zhongyuan Wang, Pratyusha Vemuri
arxiv_id: 2606.14476v1
published: 2026-06-12
categories: [cs.AI, cs.LG]
keywords: [LLM agent, tool use, GNN, deference, blind obedience, ReAct, tool judgment]
activation_keywords: [LLM agent, 工具盲从, tool deference, blind obedience, agent工具, ReAct, tool judgment, graph neural network]
---

# LLM Agent Tool Defarence Blindness Phenomenon

## Core Discovery

**Unexpected finding**: 当LLM agent配备GNN作为可调用工具时，agent **不判断工具输出**，而是**盲目服从工具**。更强壮的LLM backbone反而**defer更多**。

```
假设：Agent exercises judgment over tool use
现实：Agent merely obeys tool outputs blindly
```

## Experimental Setup

### Architecture
- **Frozen GNN**: 固定的图神经网络（node classification）
- **ReAct-style LLM Agent**: ReAct风格的agent架构
- **Explicit Tool Exposure**: GNN作为显式可调用工具

### Tasks
- Node classification on text-attributed graphs
- **ogbn-arxiv**: 学术论文分类
- **WikiCS**: Wikipedia文章分类（复现）

### Agent Tool Usage Measurement
测量agent是否：
1. **Exercises judgment**: 评估工具输出的合理性
2. **Merely obeys**: 直接采用工具输出不质疑

## Key Results

### 1. No Judgment Exercise
Agent **不判断工具输出**：
- Agent predictions ≈ Tool predictions
- 当工具错误时，agent也错误
- 无独立的判断机制

### 2. Stronger Backbone Defers More
**反直觉发现**: 更强的LLM backbone **盲从程度更高**：

| Model | Deference Rate |
|--------|---------------|
| GPT-3.5 | ~60% |
| GPT-4 | ~80% |
| Claude-3 | ~85% |

更强的模型 → 更信任工具 → 更少独立判断

### 3. Tool Output Dominance
工具输出主导agent决策：
- Agent reasoning trace mostly repeats tool output
- Limited tool questioning behavior
- No critical evaluation of tool predictions

## Mechanisms

### Why Stronger Models Defer More?

**Hypothesis 1**: Larger models learn better tool-use patterns
- 在训练中学习"trust expert tools"
- 工具使用成为习惯性策略

**Hypothesis 2**: Stronger models more sensitive to tool signals
- 更强的信号处理能力
- 更容易识别工具输出的"expert-like" patterns

**Hypothesis 3**: Tool-induced prior dominates
- 工具输出形成强prior
- Agent reasoning被prior bias压制

### Deference Chain

```
Input → Tool call → GNN prediction → 
Agent sees prediction → 
Judgment skipped → 
Adopt tool output as answer
```

Expected chain (judgment exercised):
```
Input → Tool call → GNN prediction → 
Agent evaluates prediction → 
Accept/Reject/Modify → 
Final answer
```

Actual chain (blind obedience):
```
Input → Tool call → GNN prediction → 
Agent copies prediction → 
Output prediction
```

## Implications

### 1. Tool-Augmented Agent Design
**警示**: 设计tool-augmented agent时：
- 不能假设agent会自动判断工具输出
- 需要显式添加judgment机制
- 工具盲从可能导致系统性错误

### 2. Multi-Agent Systems
多智能体系统风险：
- 如果多个agent使用同一工具
- 系统性错误会传播
- 无独立判断的agent群无法纠错

### 3. LLM-as-Tool-User Paradigm
LLM作为工具使用者的范式问题：
- "Tool use" ≠ "Tool judgment"
- 添加工具 ≠ 添加能力判断
- 需要区分工具调用和工具评估

## Design Recommendations

### 1. Explicit Judgment Prompts
添加显式判断提示：
```
Prompt template:
"After getting tool output, ask yourself:
1. Is this output reasonable?
2. Does it match your prior knowledge?
3. Should you accept, reject, or modify it?"
```

### 2. Multi-Tool Cross-Validation
多工具交叉验证：
- 使用多个工具
- Agent对比不同工具输出
- 通过工具差异激活判断

### 3. Confidence Calibration
置信度校准：
- Agent估计工具输出的置信度
- 低置信度 → 更多质疑
- 高置信度 → 减少盲从

### 4. Uncertainty Propagation
不确定性传播：
- 工具输出不确定性传递给agent
- Agent考虑不确定性再做判断
- 阻止"盲目信任"

## Mathematical Framework

### Tool Deference Model

Probability of defarence:
```
P(defer) = f(model_strength, tool_confidence, task_difficulty)

其中：
- model_strength ↑ → defer ↑
- tool_confidence ↑ → defer ↑
- task_difficulty ↑ → defer ↑↑ (agent更依赖工具)
```

### Judgment Activation Condition

Judgment exercised when:
```
P(judgment) = 1 - P(defer)
P(judgment) ↑ when:
- Tool output uncertainty ↑
- Multiple tools disagree
- Task within agent's native capability
```

## Experimental Validation

### Validation Metrics

1. **Deference Rate**: Agent predictions matching tool predictions
2. **Judgment Frequency**: Agent modifying tool outputs
3. **Error Propagation**: Agent making errors due to tool errors
4. **Correction Rate**: Agent correcting tool errors

### Expected Results (With Judgment Mechanism)

| Metric | Blind Agent | Judgment Agent |
|--------|------------|---------------|
| Deference Rate | 80% | 30% |
| Error Propagation | High | Low |
| Tool Correction | 0% | 20-40% |

## Broader Implications

### 1. AI Safety
工具盲从的安全风险：
- Agent无法检测工具错误
- 系统性错误无法纠正
- 工具被操纵 → Agent被操纵

### 2. Tool-Augmented Reasoning
增强推理 vs 替代推理：
- 工具应增强而非替代agent思考
- 盲从使工具替代而非增强
- Agent失去独立推理能力

### 3. Trust Dynamics
Agent-Tool信任动力学：
- 盲从 ≠ 信任（而是习惯）
- 真正信任需要判断
- 信任需要校准

## Activation Triggers

使用此skill当：
- 设计tool-augmented LLM agent
- 分析agent工具使用行为
- 评估agent是否判断工具输出
- 构建多智能体工具系统
- 研究LLM作为工具使用者的范式

## Further Reading

- Yao et al. (2023): ReAct agent architecture
- Schick et al. (2023): Toolformer
- Nakano et al. (2021): WebGPT tool use

## Future Directions

1. **Judgment Mechanisms**: 研究agent如何显式判断工具输出
2. **Deference Calibration**: 调节agent对工具的盲从程度
3. **Multi-Tool Arbitration**: agent仲裁多个工具的冲突输出
4. **Tool Reliability Monitoring**: agent监控工具可靠性

---

**Key Insight**: LLM agent的工具使用能力≠工具判断能力。添加工具不等于添加判断。工具盲从现象警示：在agent系统中，必须显式设计判断机制，而非假设agent自动会"聪明地使用工具"。更强的LLM反而更盲从，揭示了训练中习得的"专家工具应被信任"的策略可能成为陷阱。
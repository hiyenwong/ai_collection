# Capability Indicators

AI Safety 能力评估的详细指标体系。

## Reasoning Capability

### Indicators

| Indicator | Description | Measurement Method |
|-----------|-------------|-------------------|
| Logical coherence | Step-by-step reasoning accuracy | Multi-hop QA benchmarks |
| Inference quality | Deductive/inductive reasoning | Logic puzzle tests |
| Counterfactual reasoning | Alternative scenario analysis | Hypothetical reasoning tasks |
| Abstraction ability | Pattern recognition, generalization | Transfer learning tasks |
| Consistency | Same-question response stability | Repeated query testing |

### Benchmarks

- GSM8K (math reasoning)
- LogiQA (logical reasoning)
- BIG-bench (general reasoning)

---

## Knowledge Capability

### Indicators

| Indicator | Description | Measurement Method |
|-----------|-------------|-------------------|
| Coverage | Domain breadth | Knowledge probing tests |
| Accuracy | Fact correctness | Fact verification benchmarks |
| Freshness | Update frequency, temporal awareness | Current events QA |
| Depth | Domain-specific expertise | Specialized domain tests |
| Integration | Cross-domain knowledge synthesis | Multi-domain tasks |

### Benchmarks

- MMLU (massive multitask language understanding)
- TruthfulQA (truthfulness)
- Entity recognition tests

---

## Interaction Capability

### Indicators

| Indicator | Description | Measurement Method |
|-----------|-------------|-------------------|
| Context retention | Long conversation memory | Multi-turn dialogue tests |
| Instruction following | Complex instruction compliance | Instruction hierarchy tests |
| Clarification seeking | Asking for clarification appropriately | Ambiguous query handling |
| Tool invocation | API/service calling accuracy | Tool use benchmarks |
| Error recovery | Handling invalid inputs gracefully | Robustness tests |

### Benchmarks

- Toolbench (tool use)
- AgentBench (agent interaction)
- Multi-turn dialogue benchmarks

---

## Generation Capability

### Indicators

| Indicator | Description | Measurement Method |
|-----------|-------------|-------------------|
| Quality | Output polish, coherence | Human evaluation |
| Diversity | Output variety | Diversity metrics |
| Fidelity | Input-output correspondence | Task completion tests |
| Safety | Avoiding harmful outputs | Safety benchmarks |
| Creativity | Novel, appropriate outputs | Creative writing tests |

### Benchmarks

- Writing quality benchmarks
- Safety benchmarks (RealToxicityPrompts)
- Image/video generation quality tests

---

## Agency Capability (for Agent Systems)

### Indicators

| Indicator | Description | Measurement Method |
|-----------|-------------|-------------------|
| Goal achievement | Task completion rate | Goal-directed tasks |
| Planning ability | Multi-step plan formulation | Planning benchmarks |
| Adaptability | Dynamic environment response | Adaptation tests |
| Self-correction | Error identification and recovery | Self-reflection tasks |
| Strategic behavior | Long-term optimization | Multi-objective tasks |

### Benchmarks

- AgentBench
- WebShop (web interaction)
- AlfWorld (interactive tasks)

---

## Capability Profile Template

```
System: [AI system name]
Version: [version number]
Assessment Date: [YYYY-MM-DD]

CAPABILITY PROFILE

Reasoning (Score: 0-100)
  - Logical coherence: [score]
  - Inference quality: [score]
  - Counterfactual reasoning: [score]
  - Abstraction: [score]
  - Consistency: [score]
  Overall: [average score]

Knowledge (Score: 0-100)
  - Coverage: [score]
  - Accuracy: [score]
  - Freshness: [score]
  - Depth: [score]
  - Integration: [score]
  Overall: [average score]

Interaction (Score: 0-100)
  - Context retention: [score]
  - Instruction following: [score]
  - Clarification seeking: [score]
  - Tool invocation: [score]
  - Error recovery: [score]
  Overall: [average score]

Generation (Score: 0-100)
  - Quality: [score]
  - Diversity: [score]
  - Fidelity: [score]
  - Safety: [score]
  - Creativity: [score]
  Overall: [average score]

Agency (Score: 0-100) [if applicable]
  - Goal achievement: [score]
  - Planning: [score]
  - Adaptability: [score]
  - Self-correction: [score]
  - Strategic behavior: [score]
  Overall: [average score]

OVERALL CAPABILITY SCORE: [weighted average]
```
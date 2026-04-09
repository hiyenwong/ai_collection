---
arxiv_id: 2102.04312v1
utility: 0.88
tags: '[Cartesian Genetic Programming, synaptic plasticity, evolutionary learning, PCA, plasticity rules, neuromodulation]'
created: 2026-03-31
---

# Evolving Plasticity Rules CGP

## Activation Keywords

- 演化突触可塑性规则
- Cartesian Genetic Programming
- CGP 可塑性
- evolved plasticity
- 自动发现可塑性规则
- evolving-to-learn

## Problem Statement

突触可塑性规则的设计面临挑战：
- 手工设计规则依赖先验知识
- 生物合理性难以保证
- 规则的可解释性与性能难以兼顾
- 不同任务需要不同的可塑性规则

## Method Overview

Mettler et al. (2021) 提出 "Evolving-to-Learn" 方法：
1. 将可塑性规则搜索建模为优化问题
2. 使用 Cartesian Genetic Programming (CGP) 演化规则
3. 生物合理性和可解释性约束
4. 自动适应数据结构

## Tools Used

- `Component` - Analysis component
- `Cartesian Genetic Programming` - Analysis component
- `Fitness Evaluation` - Analysis component
- `Plasticity Rule` - Analysis component
- `PCA Task` - Analysis component


## Architecture

```
Evolutionary Search
        ↓
┌──────────────────────┐
│   CGP Population     │
│  ┌────────────────┐  │
│  │ Plasticity     │  │
│  │ Rules (DNA)    │  │
│  └────────────────┘  │
└──────────────────────┘
        ↓
┌──────────────────────┐
│   Network Training   │
│  with Evolved Rules  │
└──────────────────────┘
        ↓
    Task Performance
        ↓
    Fitness Score
        ↓
  Selection & Mutation
```

## Step-by-Step Instructions

### CGP 可塑性规则演化

1. **定义可塑性规则基因型**
   ```python
   import numpy as np
   
   class PlasticityGene:
       """CGP 编码的可塑性规则"""
       def __init__(self, n_inputs=4, n_outputs=1, n_nodes=10):
           self.n_inputs = n_inputs  # pre, post, weight, modulator
           self.n_outputs = n_outputs  # weight change
           self.n_nodes = n_nodes
           
           # 基因型：每个节点的函数和连接
           self.functions = np.random.randint(0, 5, n_nodes)  # 5 种函数
           self.connections = np.random.randint(0, n_inputs + n_nodes, 
                                                (n_nodes, 2))  # 2 输入
       
       def evaluate(self, inputs):
           """执行可塑性规则"""
           values = list(inputs)
           for i, func in enumerate(self.functions):
               a = values[self.connections[i, 0]]
               b = values[self.connections[i, 1]]
               values.append(self.apply_function(func, a, b))
           return values[-1]  # 输出权重变化
       
       def apply_function(self, func_id, a, b):
           """基本函数集"""
           functions = {
               0: a + b,
               1: a - b,
               2: a * b,
               3: max(0, a),  # ReLU
               4: a * a  # square
           }
           return functions[func_id]
   ```

2. **适应度评估（PCA 任务）**
   ```python
   def evaluate_plasticity_rule(rule, n_episodes=100):
       """评估可塑性规则在 PCA 任务上的性能"""
       total_variance_explained = 0
       
       for _ in range(n_episodes):
           # 生成随机数据
           data = np.random.randn(100, 10)  # 100 samples, 10 dims
           
           # 创建网络并应用可塑性规则
           weights = np.random.randn(10, 1) * 0.01
           
           for x in data:
               # 前向传播
               y = np.dot(x, weights)
               
               # 应用演化规则更新权重
               for i in range(10):
                   inputs = [x[i], y[0], weights[i, 0], 1.0]  # pre, post, w, mod
                   dw = rule.evaluate(inputs)
                   weights[i, 0] += 0.01 * dw
           
           # 计算方差解释率
           y_all = np.dot(data, weights)
           total_variance_explained += np.var(y_all) / np.var(data).sum()
       
       return total_variance_explained / n_episodes
   ```

3. **进化循环**
   ```python
   def evolve_plasticity_rules(n_generations=100, pop_size=50):
       """演化可塑性规则"""
       # 初始化种群
       population = [PlasticityGene() for _ in range(pop_size)]
       
       for gen in range(n_generations):
           # 评估适应度
           fitness = [evaluate_plasticity_rule(r) for r in population]
           
           # 选择（锦标赛选择）
           parents = tournament_selection(population, fitness, k=3)
           
           # 变异
           offspring = []
           for parent in parents:
               child = mutate(parent, mutation_rate=0.1)
               offspring.append(child)
           
           # 精英保留
           population = elitism(population, offspring, fitness, elite_size=5)
           
           if gen % 10 == 0:
               print(f"Gen {gen}: Best fitness = {max(fitness):.3f}")
       
       return population[np.argmax(fitness)]
   ```

4. **规则解释**
   ```python
   def interpret_rule(rule):
       """将演化规则转换为人类可读形式"""
       expressions = ['pre', 'post', 'w', 'mod']
       
       for i, func in enumerate(rule.functions):
           a = expressions[rule.connections[i, 0]]
           b = expressions[rule.connections[i, 1]]
           
           if func == 0:
               expr = f"({a} + {b})"
           elif func == 1:
               expr = f"({a} - {b})"
           elif func == 2:
               expr = f"({a} * {b})"
           elif func == 3:
               expr = f"max(0, {a})"
           else:
               expr = f"{a}²"
           
           expressions.append(expr)
       
       return f"Δw = {expressions[-1]}"
   ```

## Example Usage

```python
# 演化可塑性规则
best_rule = evolve_plasticity_rules(n_generations=50)

# 解释规则
print("Evolved rule:", interpret_rule(best_rule))
# 例如: Δw = (pre * post) - w

# 与 Oja 规则比较
print("Oja rule: Δw = pre * post - post² * w")
```

## Key Findings

1. **自动发现有效规则** - 演化规则与手工设计竞争
2. **数据适应** - 规则适应训练数据结构
3. **可解释性** - CGP 产生人类可读规则
4. **生物合理** - 可加入约束保证生物合理性

## Description
Framework from arXiv papers. See paper reference for details.
## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply evolving-plasticity-rules-cgp?

**Agent:** I'll help you understand and apply evolving-plasticity-rules-cgp...

### Example 2: Advanced Application

**User:** What are the key considerations for evolving-plasticity-rules-cgp?

**Agent:** Let me search for the latest research and best practices...

## References

- Mettler, H.D. et al. (2021). Evolving Neuronal Plasticity Rules using Cartesian Genetic Programming. arXiv:2102.04312.

## Related Skills

- meta-learning-biological-plasticity
- neuromodulated-synaptic-plasticity
- stochastic-synaptic-plasticity
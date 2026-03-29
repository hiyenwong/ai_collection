# E-SPL: Evolutionary System Prompt Learning

**Source:** arXiv:2602.14697v3 (February 2026)
**Utility:** 0.90
**Authors:** Lunjun Zhang, Ryan Chen, Bradly C. Stadie

---

## Description

E-SPL (Evolutionary System Prompt Learning) is a method for jointly improving LLM contexts (system prompts) and weights via reinforcement learning and evolutionary optimization. It enables agentic systems to self-improve from experience.

**Core Innovation:** Simultaneous optimization of:
- **Declarative knowledge** → encoded in prompts (evolved)
- **Procedural knowledge** → encoded in weights (RL updated)

---

## Activation Keywords

- 系统提示优化、prompt evolution
- 进化学习、evolutionary learning
- LLM self-improvement、自我改进
- RL + prompt、强化学习 + 提示
- context-weight joint optimization

---

## Key Concepts

### 1. Dual Optimization Loop

Each RL iteration:
1. **Sample trajectories** under multiple system prompts (parallel)
2. **Apply RL updates** to LLM weights (PPO/GRPO)
3. **Apply evolutionary updates** to system prompts (mutation + crossover)
4. **Selection** based on relative performance ratings

### 2. Genetic Operators for Prompts

**Mutation:** LLM self-reflection generates prompt variations
```
Input: Current prompt + performance feedback
Output: Modified prompt with specific improvements
```

**Crossover:** Combine successful prompt components
```
Input: Two high-performing prompts
Output: Hybrid prompt merging strengths
```

### 3. Performance-Based Selection

- Relative ratings updated across RL iterations
- Prompts with higher task success rates survive
- Population maintains diversity through exploration

---

## Implementation Guide

### Step 1: Initialize Prompt Population

```python
prompt_population = [
    "Base system prompt",
    "Reflective prompt variant",
    "Task-specific prompt variant",
    # ... N prompts
]
```

### Step 2: Parallel Trajectory Sampling

```python
for prompt in prompt_population:
    trajectories = sample_trajectories(agent, prompt, env)
    performance[prompt] = evaluate(trajectories)
```

### Step 3: RL Weight Update

```python
# Standard RL update (PPO, GRPO, etc.)
weights = rl_update(weights, all_trajectories)
```

### Step 4: Prompt Evolution

```python
# Mutation
mutated_prompts = llm_reflect(prompt_population, performance)

# Crossover
crossbred_prompts = crossover(top_prompts)

# Selection
new_population = select(mutated_prompts + crossbred_prompts, performance)
```

### Step 5: Repeat Until Convergence

---

## Results (Paper)

| Task | Baseline | E-SPL | Improvement |
|------|----------|-------|-------------|
| AIME → BeyondAIME | 38.8% | 45.1% | +6.3% |
| Reflective Evolution | 40.0% | 45.1% | +5.1% |
| Reasoning tasks | - | ↑ | Consistent gains |

**Key Finding:** RL and prompt evolution are deeply synergistic.

---

## When to Use

1. **LLM agent self-improvement** - When agents need to evolve their own prompts
2. **Multi-task optimization** - Different prompts for different task types
3. **Long-term learning systems** - Continuous improvement over many iterations
4. **Balancing exploration/exploitation** - Population maintains diversity

---

## Integration with Existing Workflows

### Self-Evolution Workflow

E-SPL aligns with AGENTS.md self-evolution principles:
- **Learn then apply** → RL learns from experience, prompts encode lessons
- **Close the loop** → Each iteration improves both prompt and weights
- **Ship or it doesn't count** → Evolved prompts are persisted

### Knowledge Architecture

- **Declarative knowledge** → Prompts (what to know)
- **Procedural knowledge** → Weights (how to do)
- E-SPL naturally separates these two types

---

## Code Reference

GitHub: https://github.com/LunjunZhang/E-SPL

---

## Limitations

1. Requires multiple parallel RL runs (computational cost)
2. Prompt evolution quality depends on LLM reflection capability
3. Selection pressure may reduce prompt diversity
4. Works best with clear performance metrics

---

## Related Skills

- `declarative-self-improvement` - Self-evolution principles
- `prompt-optimization` - Prompt engineering techniques
- `meta-cognitive-reflection` - Reflection-driven improvement
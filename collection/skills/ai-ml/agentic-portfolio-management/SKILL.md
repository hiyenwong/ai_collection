---
name: agentic-portfolio-management
version: v1.0.0
last_updated: 2026-04-06
description: "Agentic AI framework for portfolio management using multi-agent collaboration, competitive method evaluation, and meta-learning. Implements the architecture from 'The Self Driving Portfolio' paper (arxiv 2604.02279). Use when: (1) Building automated investment systems, (2) Designing agent-based portfolio optimization, (3) Creating multi-agent decision frameworks, (4) Implementing adaptive financial AI systems, (5) Developing autonomous asset allocation pipelines."
---

# Agentic Portfolio Management

Framework for autonomous portfolio management using specialized multi-agent collaboration.

## Architecture Overview

Based on "The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management" (arxiv 2604.02279).

### Core Components

1. **Specialized Agents (~50)**: Each handles a specific domain:
   - Capital market assumptions
   - Portfolio construction methods
   - Risk analysis
   - Performance attribution

2. **Competitive Methods (~20+)**: Multiple approaches compete:
   - Mean-variance optimization
   - Black-Litterman
   - Risk parity
   - Factor-based models
   - Custom methods

3. **Critique & Voting**: Agents evaluate each other's outputs
   - Critique agents review proposals
   - Voting agents score quality
   - Weighted aggregation

4. **Researcher Agent**: Proposes new methods not yet represented

5. **Meta-Agent**: Learning component that:
   - Compares forecasts vs realized returns
   - Rewrites agent code
   - Updates agent prompts
   - Improves future performance

6. **IPS Governance**: Investment Policy Statement constrains all decisions

## Activation Keywords

- agentic portfolio
- 多代理投资组合
- agent-based investment
- autonomous portfolio management
- agentic asset allocation
- 自驱投资组合
- portfolio agent system
- 投资代理框架

## Tools Used

- **exec**: Run agent coordination scripts
- **write**: Generate portfolio reports, agent outputs
- **read**: Load IPS documents, historical data, agent configurations
- **feishu_bitable**: Store portfolio data, agent outputs in structured tables

## Usage Patterns

### Pattern 1: Full Pipeline Execution

Run complete agentic portfolio management pipeline:

```
执行完整的 agentic portfolio 管道
```

Workflow:
1. Initialize specialized agents
2. Generate capital market assumptions
3. Run competing portfolio construction methods
4. Execute critique and voting cycle
5. Aggregate final portfolio recommendation
6. Log results and trigger meta-learning

### Pattern 2: Agent-Specific Tasks

Focus on specific agent functions:

```
运行资本市场假设代理
运行组合构建代理
执行批判投票流程
```

### Pattern 3: Meta-Learning Cycle

Trigger adaptive learning:

```
执行元学习改进周期
比较历史预测与实际收益
优化代理代码和提示词
```

## Instructions for Agents

### Step 1: Define IPS Constraints

Load or create Investment Policy Statement:

```markdown
IPS Elements:
- Risk tolerance level
- Asset class constraints
- Rebalancing frequency
- Target return range
- Maximum drawdown limit
```

### Step 2: Initialize Agent Pool

Create specialized agents with distinct roles:

| Agent Type | Role | Output |
|------------|------|--------|
| CMA Agent | Capital Market Assumptions | Expected returns, volatilities, correlations |
| Constructor Agent | Portfolio Building | Allocation weights |
| Critique Agent | Quality Review | Critique scores, issues |
| Voting Agent | Decision Aggregation | Final recommendation |
| Research Agent | Method Innovation | New construction proposals |
| Meta Agent | Adaptive Learning | Code/prompt updates |

### Step 3: Generate CMA (Capital Market Assumptions)

Each CMA agent produces forecasts:

```python
# Example CMA output structure
{
    "agent_id": "cma_macro_1",
    "asset_class": "equity",
    "expected_return": 0.08,
    "volatility": 0.15,
    "confidence": 0.7,
    "method": "macro_regression",
    "forecast_date": "2026-04-04"
}
```

### Step 4: Run Competitive Construction Methods

Multiple constructors apply different methods:

```python
methods = [
    "mean_variance",
    "black_litterman",
    "risk_parity",
    "factor_model",
    "min_variance",
    "max_sharpe",
    "custom_1",
    # ... 20+ methods
]

for method in methods:
    constructor_agent.run(method, cma_inputs)
```

### Step 5: Critique & Voting Cycle

Critique agents evaluate proposals:

```python
# Critique dimensions
critique_dims = [
    "ips_compliance",      # Does it follow IPS?
    "risk_efficiency",     # Is risk allocation optimal?
    "diversification",     # Is it well-diversified?
    "implementability",    # Can it be executed?
    "robustness",          # Is it stable under perturbation?
]

# Voting aggregation
vote_result = {
    "proposal_id": proposal.id,
    "total_score": sum(votes),
    "pass_threshold": threshold,
    "approved": bool
}
```

### Step 6: Meta-Learning Update

After evaluation period, meta-agent learns:

```python
# Performance comparison
forecast_error = realized_return - forecast_return

# Learning actions
if forecast_error > threshold:
    meta_agent.update_code(agent_id, optimization)
    meta_agent.update_prompt(agent_id, better_instructions)

# Research agent proposes new methods
if existing_methods_underperform:
    research_agent.propose_new_method()
```

### Step 7: Generate Report

Output comprehensive portfolio report:

```markdown
# Portfolio Management Report

**Date**: YYYY-MM-DD
**IPS Compliance**: ✓

## CMA Summary
- Equity expected return: X%
- Fixed income expected return: Y%

## Construction Methods Results
- Method 1: weights = {...}, score = A
- Method 2: weights = {...}, score = B

## Critique Summary
- Approved methods: N
- Rejected methods: M

## Final Recommendation
- Target allocation: {...}
- Expected return: X%
- Risk level: Y%

## Meta-Learning Updates
- Agent X code updated
- Agent Y prompt refined
```

## Implementation Patterns

### Multi-Agent Coordination

```python
class AgentPool:
    def __init__(self, ips_config):
        self.ips = ips_config
        self.cma_agents = []
        self.constructor_agents = []
        self.critique_agents = []
        self.voting_agents = []
        self.meta_agent = None

    def run_cycle(self, market_data):
        # 1. Generate CMA
        cma_outputs = [a.forecast(market_data) for a in self.cma_agents]
        
        # 2. Construct portfolios
        proposals = [a.construct(cma_outputs) for a in self.constructor_agents]
        
        # 3. Critique
        critiques = [a.evaluate(p) for p in proposals for a in self.critique_agents]
        
        # 4. Vote
        final = self.voting_agents.aggregate(critiques)
        
        # 5. IPS check
        if not self.ips.compliant(final):
            return self.reject(final)
        
        return final
```

### Competitive Method Evaluation

```python
class CompetitiveEvaluation:
    def __init__(self, methods):
        self.methods = methods  # List of 20+ construction methods
        
    def run_all(self, inputs):
        results = []
        for method in self.methods:
            result = method.optimize(inputs)
            result.score = self.score(result)
            results.append(result)
        
        return sorted(results, key=lambda r: r.score)
```

### Meta-Learning Loop

```python
class MetaAgent:
    def learn(self, historical_performance):
        # Compare forecasts vs actuals
        errors = self.compute_forecast_errors(historical_performance)
        
        # Identify underperforming agents
        underperformers = self.identify_weak_agents(errors)
        
        # Update their code/prompts
        for agent in underperformers:
            new_code = self.optimize_code(agent.code, agent.errors)
            new_prompt = self.refine_prompt(agent.prompt, agent.errors)
            agent.update(new_code, new_prompt)
```

## Key Design Principles

1. **Specialization**: Each agent has narrow, well-defined scope
2. **Competition**: Multiple methods compete, best wins
3. **Transparency**: All decisions are critiqued and scored
4. **Adaptation**: System learns from past performance
5. **Governance**: IPS constrains all agent behavior

## Benefits

- **Diversity**: Multiple perspectives reduce bias
- **Quality**: Critique cycles ensure rigor
- **Adaptability**: Meta-learning improves over time
- **Compliance**: IPS ensures alignment with policy
- **Autonomy**: Minimal human intervention needed

## References

- **Source Paper**: "The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management" (arxiv 2604.02279, 2026-04-02)
- **Key Insight**: Shifts investor role from analytical execution to oversight

## Related Skills

- **FinRL**: Deep reinforcement learning for quantitative finance
- **quantum-portfolio-optimization**: Quantum algorithms for portfolio problems
- **stock-analysis**: Technical analysis of individual stocks

## Notes

- This framework is for institutional-scale portfolio management
- Requires significant infrastructure for agent coordination
- IPS is critical for governance and compliance
- Meta-learning requires sufficient historical data
- 50 agents and 20+ methods are typical scale, can be reduced for simpler setups
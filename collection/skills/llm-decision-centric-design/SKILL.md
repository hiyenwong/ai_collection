---
name: llm-decision-centric-design
description: 'Decision-Centric framework for LLM systems that separates decision signals from action policies. Apply this when designing LLM control flow, routing, adaptive inference, or building diagnosable agent systems.'
metadata:
  {
    "openclaw":
      {
        "emoji": "🎯",
        "source": "arxiv:2604.00414",
        "authors": ["Wei Sun"],
        "year": 2026,
      },
  }
---

# Decision-Centric Design for LLM Systems

Framework from arxiv:2604.00414 - separates decision signals from action policies in LLM systems.

## Core Principle

**Problem:** Current LLM systems entangle decision (should I answer?) and action (generate answer) in single model call → hard to debug, constrain, repair.

**Solution:** Separate decision-relevant signals from policy → explicit control layer.

```
[Input] → [Signal Extraction] → [Decision Policy] → [Action Executor] → [Output]
           (confidence, intent,   (explicit,       (generate, retrieve,
            safety, context)       inspectable)     tool call, escalate)
```

## Decision Signals

| Signal | Description | Example |
|--------|-------------|---------|
| Confidence | Model certainty about task | "Can I solve this?" |
| Intent | What user wants | Question vs command |
| Safety | Risk assessment | Sensitive data, harmful request |
| Context | Information state | Missing info vs complete |
| Capability | Can model handle task | Beyond model scope |

## Decision Actions

| Action | Trigger |
|--------|---------|
| **Answer** | High confidence, safe, complete context |
| **Clarify** | Ambiguous intent, missing context |
| **Retrieve** | Need external info |
| **Tool Call** | Need external capability |
| **Repair** | Failed previous action, can retry |
| **Escalate** | Unsafe, beyond capability |

## Architecture Pattern

```python
class DecisionCentricAgent:
    def __init__(self):
        self.signal_estimator = SignalEstimator()
        self.decision_policy = DecisionPolicy()
        self.action_executor = ActionExecutor()
    
    def process(self, input):
        # 1. Extract signals
        signals = self.signal_estimator.extract(input)
        
        # 2. Make decision (explicit, inspectable)
        action = self.decision_policy.decide(signals)
        
        # 3. Execute action
        result = self.action_executor.execute(action, input)
        
        # 4. If action failed, can repair
        if result.failed and action.can_repair():
            repair_action = self.decision_policy.repair(signals, result)
            result = self.action_executor.execute(repair_action, input)
        
        return result
```

## Benefits

1. **Attribution** - Know where failure occurred: signal estimation vs policy vs execution
2. **Modular improvement** - Improve each component independently
3. **Constraint enforcement** - Policy layer can enforce rules
4. **Sequential decisions** - Actions can update signals for next decision
5. **Inspectability** - Decision path is visible, not hidden in generation

## Failure Modes (Interpretable)

| Failure Type | Example | Fix Target |
|--------------|---------|------------|
| Signal error | Overconfident when uncertain | Improve signal estimator |
| Policy error | Answer when should clarify | Adjust policy rules |
| Execution error | Tool call malformed | Fix action executor |

## Applications

- **Routing:** Route to specialized model based on intent signal
- **Adaptive inference:** Use cheaper model when confidence high
- **Tool use:** Decide tool call based on capability signal
- **Safety:** Escalate risky requests based on safety signal
- **Multi-turn:** Sequential decisions with updated context

## Relation to OpenClaw

OpenClaw's skill routing and tool selection can benefit from this framework:

- `skill-rag-indexer` → signal estimation (match quality)
- Skill selection → decision policy (which skill to use)
- Skill execution → action executor

---

*Source: arxiv:2604.00414 - Wei Sun, 2026*
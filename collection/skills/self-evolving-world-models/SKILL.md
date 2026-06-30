---
name: "self-evolving-world-models"
description: "Self-evolving world model framework for LLM agent planning that revises deployment-time context while keeping the downstream agent and all model parameters frozen. Three modules: Episodic Memory, Semantic Memory, Selective Foresight."
---

# Self-Evolving World Models for LLM Agent Planning

## Description
WorldEvolver is a self-evolving world model framework that revises its deployment-time context while keeping the downstream agent and all model parameters frozen. It integrates three modules: (i) Episodic Memory — exploits real action transitions through retrieval-based simulation; (ii) Semantic Memory — extracts persistent heuristic rules from prediction-observation mismatches; (iii) Selective Foresight — filters low-confidence predictions before integrating them into agent reasoning context.

## Activation Keywords
- self-evolving world models
- world model LLM agent planning
- episodic memory agent planning
- semantic memory heuristic rules
- selective foresight predictions
- test-time memory revision
- frozen agent world model
- WorldEvolver
- 自演化世界模型
- 世界模型LLM智能体规划
- 情景记忆智能体规划

## Core Concepts

### Three-Module Architecture

#### 1. Episodic Memory (Retrieval-Based Simulation)
- Stores actual action-observation transitions from environment interactions
- At deployment time, retrieves similar past transitions to simulate action consequences
- Provides concrete, experience-grounded predictions
- Uses similarity-based retrieval to find relevant past experiences

#### 2. Semantic Memory (Heuristic Rule Extraction)
- Monitors prediction-observation mismatches during deployment
- Extracts persistent heuristic rules when systematic prediction errors are detected
- Rules are stored as natural language descriptions for LLM consumption
- Updates incrementally as new mismatches reveal new patterns

#### 3. Selective Foresight (Confidence Filtering)
- Evaluates confidence of world model predictions before integration
- Low-confidence predictions are filtered out to prevent degradation
- Only high-confidence predictions are added to agent reasoning context
- Prevents unreliable foresight from being ignored or misused by downstream agent

### Key Design Principle
**Frozen Parameters, Evolving Context**: The world model and agent parameters remain frozen at deployment time. Improvement comes from revising the context (memory) that is provided to the agent, not from parameter updates.

## Usage Patterns

### Pattern 1: LLM Agent Planning Enhancement
Add world model context to existing LLM agents to improve long-horizon planning without retraining the agent.

### Pattern 2: Test-Time Memory Revision
Enable agents to improve during deployment by accumulating and refining episodic and semantic memories.

### Pattern 3: Selective Prediction Integration
Filter world model predictions by confidence before feeding them into agent reasoning to avoid degradation from unreliable forecasts.

## Instructions for Agents

### Step 1: Initialize Episodic Memory
```python
class EpisodicMemory:
    def __init__(self, capacity=10000):
        self.transitions = []  # (state, action, next_state, reward)
        self.capacity = capacity
    
    def store(self, transition):
        self.transitions.append(transition)
        if len(self.transitions) > self.capacity:
            self.transitions.pop(0)
    
    def retrieve(self, query_state, k=5):
        # Find k most similar past transitions
        similarities = [cosine_similarity(query_state, t[0]) for t in self.transitions]
        top_k_idx = np.argsort(similarities)[-k:]
        return [self.transitions[i] for i in top_k_idx]
    
    def simulate(self, state, action):
        # Retrieve similar transitions and predict outcome
        similar = self.retrieve(state)
        relevant = [t for t in similar if t[1] == action]
        if relevant:
            return np.mean([t[2] for t in relevant], axis=0)
        return None  # No similar experience
```

### Step 2: Build Semantic Memory with Rule Extraction
```python
class SemanticMemory:
    def __init__(self):
        self.heuristics = []  # Natural language rules
    
    def detect_mismatch(self, prediction, observation, threshold=0.3):
        error = np.abs(prediction - observation).mean()
        return error > threshold
    
    def extract_heuristic(self, context, prediction, observation):
        # Generate natural language rule describing the mismatch pattern
        # Could use LLM to formulate the rule
        rule = f"When {context}, expected {prediction} but observed {observation}"
        return rule
    
    def add_rule(self, rule, confidence=1.0):
        self.heuristics.append({"rule": rule, "confidence": confidence})
    
    def get_relevant_rules(self, context):
        # Return heuristics relevant to current situation
        return [h for h in self.heuristics if context_in_rule(context, h["rule"])]
```

### Step 3: Implement Selective Foresight
```python
class SelectiveForesight:
    def __init__(self, confidence_threshold=0.7):
        self.threshold = confidence_threshold
    
    def assess_confidence(self, prediction, support_evidence):
        # Confidence based on:
        # 1. Number of supporting episodic memories
        # 2. Consistency among retrieved memories
        # 3. Recency of supporting evidence
        if len(support_evidence) == 0:
            return 0.0
        consistency = 1.0 - np.var([e[2] for e in support_evidence])
        recency = np.exp(-0.1 * (len(support_evidence) - 1))
        return min(1.0, (len(support_evidence) / 5.0) * consistency * recency)
    
    def filter_predictions(self, predictions, confidences):
        return [p for p, c in zip(predictions, confidences) if c >= self.threshold]
```

### Step 4: Integrate with LLM Agent
```python
def build_agent_context(state, action, episodic_mem, semantic_mem, foresight):
    context_parts = []
    
    # Add episodic evidence
    similar = episodic_mem.retrieve(state)
    context_parts.append("## Past Experiences")
    for s, a, ns, r in similar[:3]:
        context_parts.append(f"- Action {a} led to {ns} with reward {r}")
    
    # Add semantic rules
    rules = semantic_mem.get_relevant_rules(state)
    if rules:
        context_parts.append("## Heuristic Rules")
        for rule in rules:
            context_parts.append(f"- {rule['rule']}")
    
    # Add selective foresight
    prediction = episodic_mem.simulate(state, action)
    if prediction is not None:
        confidence = foresight.assess_confidence(prediction, similar)
        if confidence >= foresight.threshold:
            context_parts.append(f"## Predicted Outcome (confidence: {confidence:.2f})")
            context_parts.append(f"- Expected next state: {prediction}")
    
    return "\n".join(context_parts)
```

## Error Handling

### Low-Confidence Predictions
- **Problem**: World model makes unreliable predictions that degrade planning
- **Solution**: Selective Foresight filters these out — only high-confidence predictions enter context

### Memory Overflow
- **Problem**: Episodic memory grows unbounded
- **Solution**: Use fixed capacity with FIFO eviction; optionally use importance-weighted retention

### Heuristic Rule Contradictions
- **Problem**: Extracted rules conflict with each other
- **Solution**: Track rule confidence based on frequency of supporting evidence; prune low-confidence rules

### Cold Start
- **Problem**: No episodic memory at deployment start
- **Solution**: Bootstrap with offline data or use fallback to agent's intrinsic knowledge

## Evaluation Metrics
- **World Model Prediction Accuracy**: Measure on held-out environment trajectories
- **Downstream Agent Success Rate**: Compare with/without world model context
- **Memory Utility**: Fraction of retrieved memories that improve predictions
- **Rule Extraction Rate**: Number of valid heuristics extracted per environment step

## Resources
- arXiv: 2606.30639 — "Self-Evolving World Models for LLM Agent Planning"
- Evaluated on: ALFWorld, ScienceWorld, Word2World, AgentBoard
- Related skills: `llm-agent-externalization`, `agent-memory-framework`, `world-model-patterns`

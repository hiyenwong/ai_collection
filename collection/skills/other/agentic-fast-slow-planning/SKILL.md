---
name: agentic-fast-slow-planning
description: "Bridging large-model reasoning with real-time control through adaptive fast-slow planning. Integrates agentic AI systems with feedback control loops for time-critical applications. Use when: (1) Integrating LLM agents with control systems, (2) Designing real-time planning with reasoning models, (3) Building adaptive hyperparameter tuning systems, (4) Implementing agentic feedback control, (5) Developing hybrid AI-control systems for robotics and automation."
---

# Agentic Fast-Slow Planning: Bridging Reasoning and Control

## Overview

This work presents a novel framework that bridges large language model reasoning with real-time control systems through an adaptive fast-slow planning architecture. The key innovation is integrating agentic AI systems within feedback control loops for time-critical applications.

**Paper**: arXiv:2604.01681 (April 2026)
**Category**: cs.RO, eess.SY, cs.AI

## Core Problem: Reasoning vs. Real-Time Control

### Challenge
- **LLM agents**: High reasoning capability, slow execution
- **Real-time control**: Fast response required, limited reasoning depth
- **Gap**: How to combine deep reasoning with time-critical control?

### Traditional Approaches
1. **Separate systems**: LLM for planning, controller for execution (no feedback)
2. **Offline planning**: Pre-compute strategies, execute fixed plan (no adaptation)
3. **Rule-based control**: Fast but limited reasoning (no deep understanding)

## Key Innovation: Fast-Slow Planning Architecture

### Dual-Loop System Design
```python
class AgenticFastSlowPlanner:
    def __init__(self):
        self.slow_planner = SlowReasoningAgent()  # LLM-based
        self.fast_controller = FastControlLoop()  # Classical controller
        self.feedback_bridge = FeedbackBridge()   # Integration layer

    def run_control_loop(self, initial_state):
        while not task_complete:
            # Fast loop: Real-time control
            fast_action = self.fast_controller.compute(state)
            state = execute(fast_action)

            # Feedback to slow planner
            if self.should_invoke_slow_planner(state):
                slow_guidance = self.slow_planner.reason(state, context)
                self.fast_controller.adapt(slow_guidance)
```

### Fast Loop: Real-Time Control
- **Execution frequency**: High (10-100 Hz typical)
- **Mechanism**: Classical feedback controller (PID, MPC, etc.)
- **Capability**: Fast response, stable execution
- **Limitation**: Limited reasoning depth

### Slow Loop: Deep Reasoning
- **Execution frequency**: Low (0.1-1 Hz typical)
- **Mechanism**: LLM-based reasoning agent
- **Capability**: Strategic planning, context understanding
- **Limitation**: Slow execution

### Feedback Bridge: Adaptive Integration
- **Purpose**: Connect fast and slow loops
- **Mechanism**: Adaptive hyperparameter tuning with feedback
- **Key**: Slow planner adapts fast controller parameters

## Architecture Details

### Layer 1: Fast Control Loop
```python
class FastControlLoop:
    def __init__(self, controller_type='PID'):
        self.controller = self.initialize_controller(controller_type)
        self.hyperparameters = self.default_hyperparameters()
        self.performance_metrics = []

    def compute_action(self, state, time_budget=0.01):
        # Fast computation (millisecond scale)
        action = self.controller.compute(state, self.hyperparameters)
        return action

    def adapt(self, slow_guidance):
        # Update hyperparameters from slow planner
        new_params = slow_guidance['hyperparameters']
        self.hyperparameters.update(new_params)
```

### Layer 2: Slow Reasoning Agent
```python
class SlowReasoningAgent:
    def __init__(self, llm_model):
        self.llm = llm_model
        self.context_memory = ContextMemory()
        self.task_understanding = None

    def reason(self, state, context, time_budget=1.0):
        # Deep reasoning (second scale)
        situation_analysis = self.analyze_situation(state, context)
        strategy = self.plan_strategy(situation_analysis)
        hyperparameters = self.translate_to_control_params(strategy)

        return {
            'strategy': strategy,
            'hyperparameters': hyperparameters,
            'confidence': self.estimate_confidence()
        }
```

### Layer 3: Adaptive Integration Bridge
```python
class FeedbackBridge:
    def __init__(self):
        self.trigger_thresholds = self.define_thresholds()
        self.adaptation_history = []

    def should_invoke_slow_planner(self, state):
        # Trigger conditions:
        # 1. Performance degradation
        # 2. Novel situation detected
        # 3. Constraint violation risk
        # 4. Periodic strategic review
        return self.check_trigger_conditions(state)

    def integrate_feedback(self, slow_output, fast_controller):
        # Translate reasoning to control parameters
        param_adaptation = self.translate_strategy_to_params(slow_output['strategy'])
        confidence_weight = slow_output['confidence']

        # Adaptive update with confidence weighting
        fast_controller.update_params(param_adaptation, confidence_weight)
```

## Adaptive Hyperparameter Tuning Mechanism

### Key Innovation: Feedback-Driven Adaptation
```python
def adaptive_hyperparameter_tuning(fast_controller, slow_reasoning, feedback):
    # Fast controller executes with current parameters
    performance = fast_controller.track_performance()

    # Slow planner observes performance trend
    if slow_reasoning.should_adapt(performance):
        # LLM analyzes performance and context
        adaptation_strategy = slow_reasoning.propose_adaptation(performance, feedback)

        # Translate strategy to parameter adjustments
        new_params = translate_strategy_to_params(adaptation_strategy)

        # Apply adaptation with confidence weighting
        fast_controller.update_hyperparameters(new_params, confidence)
```

### Trigger Conditions for Slow Planner Invocation
1. **Performance threshold**: When metrics fall below acceptable level
2. **Novelty detection**: When situation differs from training context
3. **Risk prediction**: When constraint violation becomes likely
4. **Periodic review**: Regular strategic reassessment

## Applications

### 1. Autonomous Vehicles
- **Fast loop**: Real-time path tracking, obstacle avoidance
- **Slow loop**: Strategic route planning, traffic reasoning
- **Integration**: Adaptive speed/tuning based on traffic context

### 2. Robotics Manipulation
- **Fast loop**: Motor control, force feedback
- **Slow loop**: Task understanding, strategy selection
- **Integration**: Adaptive grip strength, motion strategy

### 3. Drone Navigation
- **Fast loop**: Flight stabilization, obstacle avoidance
- **Slow loop**: Mission planning, environment reasoning
- **Integration**: Adaptive flight parameters based on weather

### 4. Industrial Automation
- **Fast loop**: Process control, quality monitoring
- **Slow loop**: Production strategy, fault reasoning
- **Integration**: Adaptive control parameters based on product type

## Design Patterns

### Pattern 1: Hierarchical Strategy Translation
```python
# Slow planner high-level strategy
strategy = "Navigate carefully in crowded area"

# Translate to control parameters
params = {
    'speed_limit': 0.5,      # Lower speed
    'safety_margin': 1.5,    # Larger obstacle buffer
    'replan_frequency': 2.0  # More frequent replanning
}
```

### Pattern 2: Confidence-Based Adaptation
```python
# High confidence: Strong parameter adaptation
if confidence > 0.8:
    controller.apply_full_adaptation(new_params)
# Medium confidence: Conservative adaptation
elif confidence > 0.5:
    controller.apply_partial_adaptation(new_params, blend=0.3)
# Low confidence: Minimal adaptation
else:
    controller.apply_minimal_adaptation(new_params, blend=0.1)
```

### Pattern 3: Performance-Guided Triggering
```python
# Trigger slow planner when:
def trigger_conditions(fast_performance, state):
    # 1. Performance degradation
    if fast_performance < threshold:
        return True

    # 2. Novel situation
    if novelty_score(state) > novelty_threshold:
        return True

    # 3. Risk prediction
    if predict_constraint_risk(state) > risk_threshold:
        return True

    # 4. Periodic review
    if time_since_last_slow_planning > review_interval:
        return True

    return False
```

## Implementation Considerations

### Time Budget Management
- **Fast loop**: Must complete within control cycle (typically < 10 ms)
- **Slow loop**: Can use longer budget (typically 100 ms - 1 s)
- **Integration**: Overlap execution where possible

### Resource Allocation
- **Parallel execution**: Fast loop runs continuously, slow loop interleaved
- **Priority handling**: Fast loop gets priority when deadlines tight
- **Graceful degradation**: Reduce slow loop frequency under load

### Safety Guarantees
- **Fallback mechanisms**: Default to fast loop if slow planner fails
- **Parameter bounds**: Limit adaptation range to prevent instability
- **Verification**: Check parameter validity before applying

## Comparison with Traditional Approaches

| Approach | Reasoning Depth | Response Time | Adaptation | Integration |
|----------|----------------|---------------|------------|-------------|
| Classical Control | Low | Fast | No | None |
| LLM Planning Only | High | Slow | No | None |
| Separate Systems | High | Mixed | No | Loose |
| **Fast-Slow Planning** | **High** | **Fast** | **Yes** | **Tight** |

## Key Advantages

1. **Combines reasoning and speed**: Deep understanding with real-time execution
2. **Adaptive integration**: Slow planner continuously guides fast controller
3. **Feedback-driven**: Performance metrics trigger strategic reassessment
4. **Safety-aware**: Bounds and fallbacks ensure stability
5. **Resource-efficient**: Parallel execution maximizes utilization

## Research Contributions

- Novel fast-slow planning architecture for agentic control
- Adaptive hyperparameter tuning mechanism with feedback
- Integration layer design for bridging reasoning and control
- Trigger condition framework for strategic intervention
- Application studies in robotics and automation

## Practical Guidelines

1. **Start with simple fast controllers** (PID, basic MPC)
2. **Use LLM for strategy-level reasoning** (not parameter tuning directly)
3. **Implement translation layer** between strategy and parameters
4. **Set appropriate trigger thresholds** to balance reasoning frequency
5. **Always maintain safety bounds** on parameter adaptation
6. **Test thoroughly** before deployment in time-critical systems

## Key Takeaways

1. **Fast-slow architecture** bridges the reasoning-control gap
2. **Feedback integration** enables continuous adaptation
3. **Adaptive hyperparameter tuning** translates reasoning to control
4. **Trigger conditions** balance reasoning depth vs. execution speed
5. **Safety mechanisms** ensure stability under adaptation

## Reference

- **Full paper**: https://arxiv.org/abs/2604.01681
- **PDF**: https://arxiv.org/pdf/2604.01681
- **Category**: cs.RO (Robotics), eess.SY (Systems and Control), cs.AI
- **Keywords**: agentic systems, real-time control, fast-slow planning, adaptive hyperparameter tuning, feedback control loops, LLM-based reasoning
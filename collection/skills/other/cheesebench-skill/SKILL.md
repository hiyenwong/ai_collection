---
name: cheesebench-rodent-neuroscience
description: "CheeseBench - Evaluating Large Language Models on classical rodent behavioral neuroscience paradigms. Contains 9 tasks (Morris water maze, T-maze, Barnes maze, radial arm maze, operant chamber, etc.) spanning spatial memory, associative learning, and decision-making. Use for benchmarking AI agents against animal behavior baselines, testing cognitive capabilities of LLMs, and evaluating spatial reasoning. Activation: rodent neuroscience, behavioral paradigms, spatial memory, cheesebench, animal cognition, maze learning."
---

# CheeseBench: Rodent Behavioral Neuroscience Evaluation

CheeseBench is a comprehensive benchmark for evaluating Large Language Models (LLMs) on nine classical behavioral neuroscience paradigms originally developed for rodent studies. It bridges computational neuroscience and AI by testing whether language models can solve tasks that real animals (rodents) can perform.

## Core Paradigms

### 1. Morris Water Maze
- **Task Type**: Spatial navigation and memory
- **Setup**: Circular pool with hidden platform, distal cues
- **Metrics**: Latency to platform, path efficiency, probe trial performance
- **Cognitive Dimension**: Spatial memory, reference memory
- **Animal Baseline**: ~20-30 seconds after training

### 2. Barnes Maze
- **Task Type**: Spatial learning with aversive motivation
- **Setup**: Circular platform with holes, one leads to escape
- **Metrics**: Latency to find escape, errors, search strategy
- **Cognitive Dimension**: Spatial memory, stress response
- **Advantage**: No swimming stress (unlike Morris)

### 3. T-Maze
- **Task Type**: Spatial working memory
- **Setup**: T-shaped maze with reward in one arm
- **Variants**: Spontaneous alternation, delayed alternation
- **Cognitive Dimension**: Working memory, spatial alternation
- **Animal Baseline**: 80-90% alternation rate

### 4. Radial Arm Maze
- **Task Type**: Working and reference memory
- **Setup**: Multiple arms radiating from center, subset baited
- **Metrics**: Working memory errors, reference memory errors
- **Cognitive Dimension**: Episodic-like memory, strategy use
- **Key Measure**: Entries to already-visited arms

### 5. Star Maze
- **Task Type**: Complex spatial navigation
- **Setup**: Multiple-choice maze with hierarchical structure
- **Metrics**: Path optimization, learning curve
- **Cognitive Dimension**: Flexible navigation, planning

### 6. Operant Chamber (Skinner Box)
- **Task Type**: Instrumental conditioning
- **Setup**: Chamber with lever/response key, reward dispenser
- **Schedules**: Fixed ratio, variable ratio, fixed interval, etc.
- **Cognitive Dimension**: Action-outcome learning, timing
- **Key Measure**: Response rate, extinction resistance

### 7. Shuttle Box
- **Task Type**: Avoidance learning
- **Setup**: Two-compartment chamber, signal predicts shock
- **Metrics**: Avoidance latency, escape latency
- **Cognitive Dimension**: Fear conditioning, active avoidance

### 8. Conditioned Place Preference (CPP)
- **Task Type**: Associative memory with context
- **Setup**: Two distinct compartments paired with different states
- **Metrics**: Time spent in drug-paired compartment
- **Cognitive Dimension**: Contextual association, reward valuation

### 9. Delayed Non-Match to Sample (DNMTS)
- **Task Type**: Recognition memory
- **Setup**: Sample phase → delay → choice between match/non-match
- **Metrics**: Accuracy as function of delay
- **Cognitive Dimension**: Recognition memory, temporal decay
- **Animal Baseline**: ~80% accuracy at short delays

## Evaluation Framework

### Task Structure
```
System Prompt: Unified across all tasks, no task-specific instructions
Input: ASCII text rendering of environment state
Output: Action selection (text-based)
Reward: Binary feedback (success/failure)
```

### Key Findings

1. **Model Performance**: Best model (Qwen2.5-VL-7B) reaches 52.6% vs 78.9% rodent baseline
2. **Scaling**: Diminishing returns beyond 7B parameters
3. **Context**: Longer history degrades performance (counter-intuitive)
4. **Chain-of-Thought**: HURTS performance rather than helps
5. **Vision vs Text**: VLMs have advantage at 7B but hurt at 32B
6. **Spatial Navigation**: Major weakness for current LLMs
7. **Within-trial State Tracking**: Difficulty maintaining state

### Interface Variants
- **ASCII Text**: Pure text representation
- **Vision**: Image-based rendering
- Performance varies 20-57% depending on interface alone

## Implementation Guidelines

### Creating Custom Tasks

```python
class CheeseBenchTask:
    """Base class for CheeseBench tasks."""
    
    def __init__(self):
        self.paradigm = "morris_water_maze"  # or other
        self.cognitive_dimensions = ["spatial_memory", "reference_memory"]
        self.animal_baseline = {"success_rate": 0.85, "latency": 25}
    
    def render_state(self, agent_position, environment):
        """Return ASCII representation."""
        return ascii_rendering
    
    def evaluate_action(self, action):
        """Return reward and next state."""
        return reward, next_state, done
    
    def calculate_metrics(self, trajectory):
        """Return task-specific metrics."""
        return {
            "success_rate": successes / trials,
            "latency": mean(time_to_solution),
            "path_efficiency": optimal_path / actual_path
        }
```

### Running Evaluation

```python
from cheesebench import CheeseBenchEvaluator

evaluator = CheeseBenchEvaluator(
    model="qwen2.5-vl-7b",
    interface="ascii",  # or "vision"
    num_episodes=100
)

results = evaluator.evaluate_all_paradigms()
# Returns performance across all 9 tasks
```

## Cognitive Dimensions Covered

| Dimension | Tasks |
|-----------|-------|
| Spatial Memory | Morris, Barnes, T-maze, Radial Arm, Star |
| Working Memory | T-maze (alternation), Radial Arm, DNMTS |
| Reference Memory | Morris, Barnes, Radial Arm (baited arms) |
| Associative Learning | Operant, Shuttle, CPP |
| Decision Making | All tasks involve choice selection |
| Timing | Operant (interval schedules), DNMTS (delays) |
| Flexibility | Reversal learning variants |

## Comparison Metrics

### Animal Baselines (Approximate)
- **Trained Rodents**: 70-90% success on most tasks
- **Spatial Tasks**: 20-30s latency after training
- **Working Memory**: 80-90% accuracy (short delays)

### LLM Baselines (Current)
- **Best Overall**: 52.6% (Qwen2.5-VL-7B)
- **Random Agent**: 32.1%
- **Gap to Animals**: ~25 percentage points

## Applications

1. **AI Evaluation**: Benchmark cognitive capabilities beyond standard NLP
2. **Neuroscience**: Validate computational models against animal behavior
3. **Cognitive Architecture Design**: Test memory, planning, spatial modules
4. **Curriculum Learning**: Use as progressive training tasks
5. **Embodied AI**: Bridge between disembodied LLMs and physical agents

## Key Insights for AI Development

### What Makes These Tasks Hard for LLMs?

1. **State Tracking**: Must maintain position/environment state across turns
2. **Credit Assignment**: Sparse rewards require long-term credit assignment
3. **Exploration**: No explicit exploration strategy
4. **Spatial Reasoning**: Implicit spatial representations lacking
5. **Motor Integration**: No embodiment → poor action-outcome learning

### Implications for Agent Design

- **Memory**: Explicit episodic memory for state tracking
- **World Models**: Learned environment dynamics for planning
- **Exploration**: Intrinsic motivation or curiosity-driven exploration
- **Spatial Representations**: Grid cells, place cells analogues
- **Hierarchical Control**: Subgoal decomposition

## Related Work

- **Animal-AI Olympics**: Similar goal, different task suite
- **Psychlab**: Cognitive psychology tasks for AI
- **ProcGen**: Procedural environments for RL generalization
- **Crafter**: Survival crafting benchmark

## References

Paper: "CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms"
- arXiv: 2604.10825
- Author: Zacharie Bugaud
- Published: April 2026

## Trigger Keywords

- cheesebench
- rodent neuroscience
- behavioral paradigms
- spatial memory tasks
- maze learning
- animal cognition benchmark
- morris water maze
- barnes maze
- t-maze
- radial arm maze
- operant conditioning
- avoidance learning
- conditioned place preference
- delayed match to sample

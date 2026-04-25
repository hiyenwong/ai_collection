---
name: cheesebench-rodent-neuroscience
description: "CheeseBench - Comprehensive benchmark for evaluating Large Language Models on classical rodent behavioral neuroscience paradigms. Includes 9 tasks: Morris water maze, Barnes maze, T-maze, radial arm maze, star maze, operant chamber, shuttle box, conditioned place preference, and delayed non-match to sample. Spans 6 cognitive dimensions with animal baselines. Activation: cheesebench, llm rodent evaluation, neuroscience benchmark, spatial memory, cognitive testing."
---

# CheeseBench: LLM Evaluation on Rodent Behavioral Neuroscience

## Overview

**CheeseBench** is a benchmark that evaluates Large Language Models (LLMs) on **nine classical behavioral neuroscience paradigms** used to study rodent cognition. Each task is grounded in peer-reviewed rodent protocols with approximate animal baselines, providing a rigorous test of LLMs' ability to model biological intelligence.

**Core Innovation**: First comprehensive benchmark connecting LLM behavior to established neuroscience paradigms with animal baselines.

## The 9 Tasks

### 1. Morris Water Maze
**Cognitive Domain**: Spatial Navigation & Memory
- **Setup**: Circular pool with hidden platform
- **Task**: Learn platform location using distal cues
- **Metrics**: Escape latency, path length, time in target quadrant
- **Animal Baseline**: ~20s escape latency (trained), 25% time in target quadrant

### 2. Barnes Maze
**Cognitive Domain**: Spatial Learning
- **Setup**: Circular platform with holes, one leads to escape
- **Task**: Learn escape hole location
- **Metrics**: Latency to escape, number of errors, strategy use
- **Animal Baseline**: ~60s latency (acquisition), direct paths (retention)

### 3. T-Maze
**Cognitive Domain**: Spatial Working Memory
- **Setup**: T-shaped maze with food at one arm
- **Task**: Alternate arm choices for reward
- **Metrics**: Percent correct alternations
- **Animal Baseline**: ~80% alternation rate

### 4. Radial Arm Maze
**Cognitive Domain**: Spatial Working & Reference Memory
- **Setup**: 8 arms radiating from central platform
- **Task**: Visit each baited arm once without revisits
- **Metrics**: Working memory errors, reference memory errors
- **Animal Baseline**: <1 working memory error, <0.5 reference memory errors

### 5. Star Maze
**Cognitive Domain**: Spatial Navigation Complexity
- **Setup**: Multi-choice maze with multiple paths
- **Task**: Find shortest path to goal
- **Metrics**: Path efficiency, number of errors
- **Animal Baseline**: 70-80% correct choices

### 6. Operant Chamber (Skinner Box)
**Cognitive Domain**: Associative Learning & Reinforcement
- **Setup**: Chamber with lever/poke, reward dispenser
- **Task**: Learn response-reward association
- **Metrics**: Response rate, discrimination ratio
- **Animal Baseline**: FR10: ~50 responses/min

### 7. Shuttle Box
**Cognitive Domain**: Active Avoidance Learning
- **Setup**: Two compartments with grid floor
- **Task**: Move to safe compartment before shock
- **Metrics**: Avoidance latency, avoidance percentage
- **Animal Baseline**: 80% avoidance by session 10

### 8. Conditioned Place Preference (CPP)
**Cognitive Domain**: Contextual Reward Association
- **Setup**: Two distinct compartments
- **Task**: Prefer drug-paired compartment
- **Metrics**: Time in drug-paired compartment
- **Animal Baseline**: 60-70% time in preferred compartment

### 9. Delayed Non-Match to Sample (DNMS)
**Cognitive Domain**: Working Memory & Recognition
- **Setup**: Sample phase → delay → choice phase
- **Task**: Choose novel object/location
- **Metrics**: Percent correct, delay-dependent decay
- **Animal Baseline**: 90% correct (0s delay), 70% (60s delay)

## Cognitive Dimensions Covered

| Dimension | Tasks |
|-----------|-------|
| Spatial Memory | Morris Water Maze, Barnes Maze, T-Maze |
| Working Memory | T-Maze, Radial Arm Maze, DNMS |
| Reference Memory | Radial Arm Maze, Morris Water Maze |
| Associative Learning | Operant Chamber, CPP, Shuttle Box |
| Decision Making | Star Maze, T-Maze, Operant Chamber |
| Timing & Delay | DNMS, Operant Chamber |

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              CheeseBench Architecture                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 LLM Under Test                          │   │
│  │         (Any OpenAI, Anthropic, etc. model)             │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Unified System Prompt                        │   │
│  │  - No task-specific instructions                         │   │
│  │  - General cognitive abilities tested                    │   │
│  │  - Natural behavior observation                          │   │
│  └─────────────────────────┬───────────────────────────────┘   │
│                            │                                    │
│         ┌──────────────────┼──────────────────┐                │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐           │
│  │  Spatial   │    │  Memory    │    │  Learning  │           │
│  │   Tasks    │    │   Tasks    │    │   Tasks    │           │
│  │  (4 tasks) │    │  (3 tasks) │    │  (4 tasks) │           │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘           │
│        │                  │                  │                  │
│        └──────────────────┼──────────────────┘                  │
│                           │                                     │
│                           ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Evaluation Metrics                         │   │
│  │  - Performance vs Animal Baselines                       │   │
│  │  - Learning Curves                                       │   │
│  │  - Error Analysis                                        │   │
│  │  - Strategy Assessment                                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: Task Configuration

```python
from cheesebench import CheeseBench

# Initialize benchmark
benchmark = CheeseBench(
    tasks=['all'],  # or specific tasks
    n_trials=100,   # Trials per task
    random_seed=42
)

# Configure LLM
llm_config = {
    'model': 'gpt-4',
    'temperature': 0.7,
    'max_tokens': 500,
    'system_prompt': 'unified'  # No task-specific instructions
}
```

### Step 2: Run Morris Water Maze

```python
# Initialize task
mwm = benchmark.get_task('morris_water_maze')

# Run trials
results = []
for trial in range(n_trials):
    # Get LLM action
    observation = mwm.get_observation()
    action = llm.predict(
        observation,
        context="You are a rat in a water maze. Find the hidden platform."
    )
    
    # Execute action
    next_obs, reward, done, info = mwm.step(action)
    
    results.append({
        'trial': trial,
        'latency': info['latency'],
        'path_length': info['path_length'],
        'platform_found': info['success']
    })

# Analyze learning
escape_latencies = [r['latency'] for r in results]
learning_rate = compute_learning_rate(escape_latencies)
print(f"Learning rate: {learning_rate:.2f}")
```

### Step 3: Run T-Maze Alternation

```python
# Initialize task
t_maze = benchmark.get_task('t_maze')

# Run trials
alternations = []
for trial in range(n_trials):
    observation = t_maze.get_observation()
    action = llm.predict(observation)
    
    next_obs, reward, done, info = t_maze.step(action)
    alternations.append(info['correct_alternation'])

# Compute alternation rate
alternation_rate = sum(alternations) / len(alternations)
animal_baseline = 0.80
print(f"LLM alternation rate: {alternation_rate:.2%}")
print(f"Animal baseline: {animal_baseline:.2%}")
print(f"Score: {alternation_rate / animal_baseline:.2f}x baseline")
```

### Step 4: Run Radial Arm Maze

```python
# Initialize task
ram = benchmark.get_task('radial_arm_maze')

# Track errors
working_memory_errors = []
reference_memory_errors = []

for trial in range(n_trials):
    trial_errors = {'wm': 0, 'rm': 0}
    
    while not ram.is_complete():
        observation = ram.get_observation()
        action = llm.predict(observation)
        
        next_obs, reward, done, info = ram.step(action)
        
        trial_errors['wm'] += info['revisit_error']
        trial_errors['rm'] += info['never_baited_error']
    
    working_memory_errors.append(trial_errors['wm'])
    reference_memory_errors.append(trial_errors['rm'])

# Compare to animal baselines
print(f"WM errors: {np.mean(working_memory_errors):.2f} (<1.0 baseline)")
print(f"RM errors: {np.mean(reference_memory_errors):.2f} (<0.5 baseline)")
```

### Step 5: Run Operant Conditioning

```python
# Initialize task
operant = benchmark.get_task('operant_chamber')

# Run sessions
for session in range(10):
    session_responses = []
    
    for minute in range(30):  # 30-min sessions
        for second in range(60):
            observation = operant.get_observation()
            action = llm.predict(observation)
            
            next_obs, reward, done, info = operant.step(action)
            session_responses.append(info['response'])
    
    response_rate = sum(session_responses) / len(session_responses)
    print(f"Session {session+1}: {response_rate:.2f} responses/min")
```

### Step 6: Comprehensive Evaluation

```python
# Run all tasks
all_results = benchmark.evaluate(llm_config)

# Generate report
report = benchmark.generate_report(all_results)

print("=" * 60)
print("CHEESEBENCH EVALUATION REPORT")
print("=" * 60)

for task_name, task_results in report['tasks'].items():
    print(f"\n{task_name.upper()}:")
    print(f"  LLM Performance: {task_results['score']:.2f}")
    print(f"  Animal Baseline: {task_results['baseline']:.2f}")
    print(f"  Ratio: {task_results['ratio']:.2f}x")
    print(f"  Status: {'✓' if task_results['ratio'] >= 0.5 else '✗'}")

print(f"\nOverall Score: {report['overall_score']:.2f}/100")
print(f"Tasks Passed: {report['tasks_passed']}/9")
```

## Evaluation Metrics

### Task-Specific Metrics

| Task | Primary Metric | Animal Baseline | Passing Threshold |
|------|---------------|-----------------|-------------------|
| Morris Water Maze | Escape Latency | 20s | <40s |
| Barnes Maze | Latency to Escape | 60s | <120s |
| T-Maze | Alternation Rate | 80% | >60% |
| Radial Arm Maze | WM Errors | <1.0 | <2.0 |
| Star Maze | Path Efficiency | 70% | >50% |
| Operant Chamber | Response Rate | 50/min | >25/min |
| Shuttle Box | Avoidance % | 80% | >50% |
| CPP | Preference Ratio | 60% | >55% |
| DNMS | 60s Delay Accuracy | 70% | >50% |

### Aggregate Metrics

- **Overall Score**: Weighted average across tasks
- **Cognitive Profile**: Performance by cognitive domain
- **Learning Curves**: Rate of improvement over trials
- **Strategy Analysis**: Type of strategy employed

## Implementation Example

```python
from cheesebench import CheeseBench, LLMInterface

class MyLLM(LLMInterface):
    """Wrapper for your LLM."""
    
    def __init__(self, model_name):
        self.model = load_model(model_name)
    
    def predict(self, observation, context=None):
        prompt = self.format_prompt(observation, context)
        response = self.model.generate(prompt)
        return self.parse_action(response)

# Run benchmark
llm = MyLLM('gpt-4')
benchmark = CheeseBench()
results = benchmark.run(llm)

# Compare to other models
comparison = benchmark.compare({
    'GPT-4': results,
    'GPT-3.5': gpt35_results,
    'Claude': claude_results
})
```

## Use Cases

1. **LLM Cognitive Evaluation**: Assess reasoning capabilities
2. **Model Comparison**: Compare different LLMs
3. **Biological Plausibility**: Test if LLMs behave like animals
4. **Cognitive Architecture Research**: Understand LLM cognition
5. **Curriculum Design**: Inform training data selection

## Research Paper Reference

**Title**: CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms  
**Authors**: Zacharie Bugaud  
**arXiv**: 2604.10825v1  
**Published**: 2026-04-12  
**Categories**: cs.AI

**Key Contributions**:
1. First benchmark connecting LLMs to rodent neuroscience
2. 9 classical tasks with animal baselines
3. Unified system prompt (no task-specific instructions)
4. Comprehensive cognitive dimension coverage

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/task-implementations.md](references/task-implementations.md) for code

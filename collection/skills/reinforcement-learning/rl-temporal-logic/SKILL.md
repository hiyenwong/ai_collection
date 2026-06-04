---
name: rl-temporal-logic
description: "Combine reinforcement learning with signal temporal logic (STL) for stratified control. Use STL specifications to define complex temporal constraints and stratification for hierarchical RL policy learning. Activation: RL temporal logic, STL reinforcement learning, temporal specification RL, stratified control."
---

# RL with Temporal Logic

Integrate reinforcement learning with signal temporal logic for complex control tasks.

## Background

Signal Temporal Logic (STL) allows specifying **temporal constraints** on signals:
- "Safety within 5 seconds"
- "Reach target before time T"
- "Maintain temperature between bounds for duration D"

**Challenge**: STL predicates are Boolean (satisfied/not satisfied) - hard for RL gradients.

**Solution**: **Stratification-based semantics** - soft membership functions for RL optimization.

## Core Concepts

### 1. Signal Temporal Logic (STL)

STL formulas over continuous signals:

```python
# STL atomic predicates
def predicate(signal, threshold):
    """Basic STL predicate: signal > threshold"""
    return signal > threshold

# Temporal operators
def eventually(signal, predicate, time_window):
    """∃ t ∈ [now, now+T]: predicate(signal[t])"""
    return any(predicate(signal[t]) for t in time_window)

def always(signal, predicate, time_window):
    """∀ t ∈ [now, now+T]: predicate(signal[t])"""
    return all(predicate(signal[t]) for t in time_window)

def until(signal, pred1, pred2, time_window):
    """pred1 holds until pred2 becomes true"""
    for t in time_window:
        if pred2(signal[t]):
            return True
        if not pred1(signal[t]):
            return False
    return False
```

### 2. Stratified Semantics

Convert Boolean STL to **graded satisfaction**:

```python
class StratifiedSTL:
    """Soft STL satisfaction for RL optimization"""
    
    def __init__(self, stratification_levels=5):
        self.levels = stratification_levels
    
    def membership(self, signal, predicate, threshold):
        """Soft membership in predicate satisfaction"""
        # Stratified space: multiple membership degrees
        if signal > threshold:
            # Strong satisfaction
            return 1.0
        elif signal > threshold - epsilon:
            # Partial satisfaction
            return self.stratify(signal - threshold)
        else:
            # Non-satisfaction
            return 0.0
    
    def stratify(self, value):
        """Map continuous value to stratification levels"""
        # Smooth transition between levels
        levels = np.linspace(0, 1, self.levels)
        return smooth_interpolation(value, levels)
```

### 3. RL with STL Specifications

Reward function incorporating STL:

```python
class STLRewardFunction:
    """STL-based reward for RL"""
    
    def __init__(self, stl_spec, stratified=True):
        self.spec = stl_spec
        self.stratified = stratified
    
    def compute_reward(self, trajectory):
        """Reward = STL satisfaction degree"""
        if self.stratified:
            # Soft satisfaction (continuous reward)
            satisfaction = self.evaluate_stratified(trajectory, self.spec)
        else:
            # Boolean satisfaction (sparse reward)
            satisfaction = 1.0 if self.evaluate_bool(trajectory, self.spec) else 0.0
        
        return satisfaction
    
    def evaluate_stratified(self, trajectory, spec):
        """Evaluate STL with stratification"""
        if spec.type == "eventually":
            # Reward based on how close to satisfaction
            return self.stratified_eventually(trajectory, spec)
        elif spec.type == "always":
            return self.stratified_always(trajectory, spec)
        elif spec.type == "until":
            return self.stratified_until(trajectory, spec)
```

### 4. Stratified Learning

Hierarchical policy learning:

```python
class StratifiedRLPolicy:
    """Learn RL policy in stratified STL space"""
    
    def __init__(self, num_levels=5):
        self.stratification = StratificationSpace(num_levels)
        self.policy = PolicyNetwork()
    
    def train(self, env, stl_spec):
        for episode in range(num_episodes):
            trajectory = []
            state = env.reset()
            
            for step in episode_steps:
                # Policy conditioned on current STL satisfaction level
                satisfaction_level = self.current_satisfaction(trajectory, stl_spec)
                
                # Stratified action selection
                action = self.policy(state, satisfaction_level)
                
                next_state, reward = env.step(action)
                
                # STL-aware reward
                stl_reward = self.compute_stl_reward(trajectory, stl_spec)
                
                trajectory.append((state, action, next_state, stl_reward))
            
            # Update policy with stratified reward
            self.policy.update(trajectory)
```

## Implementation Guidelines

### When to Use

1. **Safety-critical RL** - Temporal safety constraints
2. **Multi-stage tasks** - Sequential goal satisfaction
3. **Specification-driven RL** - Formal temporal requirements
4. **Hierarchical control** - Stratified policy learning

### STL Specification Examples

```python
# Safety specification
safety_spec = STLFormula(
    operator="always",
    predicate=lambda s: s["position"] < danger_threshold,
    time_window=(0, episode_length)
)

# Reach-avoid specification
reach_avoid = STLFormula(
    operator="until",
    pred1=lambda s: s["obstacle_dist"] > safe_dist,
    pred2=lambda s: s["at_target"],
    time_window=(0, max_time)
)

# Temporal deadline
deadline_spec = STLFormula(
    operator="eventually",
    predicate=lambda s: s["task_complete"],
    time_window=(0, deadline)
)
```

### Stratification Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| Levels | 3-10 | Granularity of satisfaction degrees |
| Epsilon | 0.1-0.5 | Soft boundary width |
| Weight | 0.1-1.0 | STL vs task reward balance |

## Algorithm Components

### 1. STL Parser

```python
class STLParser:
    """Parse STL specifications"""
    
    def parse(self, spec_string):
        # Parse STL formula
        # Examples:
        # "□[0,T] (x < 10)"  - always within bounds
        # "◇[0,T] (goal)"    - eventually reach goal
        # "(safe) U[0,T] (goal)"  - safe until goal
        
        tokens = self.tokenize(spec_string)
        return self.build_formula(tokens)
```

### 2. Stratified Membership

```python
def stratified_membership(signal_value, predicate, epsilon):
    """Continuous membership in predicate"""
    threshold = predicate.threshold
    
    if signal_value >= threshold:
        # Satisfied
        return 1.0
    elif signal_value >= threshold - epsilon:
        # Partially satisfied (smooth transition)
        return (signal_value - threshold + epsilon) / epsilon
    else:
        # Not satisfied
        return 0.0
```

### 3. RL Integration

```python
def compute_stratified_reward(trajectory, stl_formula):
    """STL-aware reward for RL"""
    
    # Evaluate STL with stratification
    satisfaction = evaluate_stratified_stl(trajectory, stl_formula)
    
    # Combine STL satisfaction with task reward
    task_reward = trajectory[-1]["task_reward"]
    
    # Weighted combination
    total_reward = alpha * satisfaction + beta * task_reward
    
    return total_reward
```

## Related Concepts

- **Signal Temporal Logic**: Temporal specification language
- **Stratification Theory**: Topological stratification
- **Specification-guided RL**: Learning from formal specs
- **Safe RL**: RL with safety constraints

## Resources

- Paper: "Stratifying Reinforcement Learning with Signal Temporal Logic" (2604.04923v1)
- STL libraries: PyTL, RTAMT
- Safe RL frameworks: SafeOpt, ConstrainedRL

## Usage Examples

### Example: Safe Navigation

```python
# RL with safety STL specification
safety_spec = "□[0,100] (dist_to_obstacle > 1.0)"

env = NavigationEnv()
policy = StratifiedRLPolicy(stl_spec=safety_spec)

# Train with stratified STL reward
for episode in range(1000):
    trajectory = run_episode(env, policy)
    reward = compute_stratified_reward(trajectory, safety_spec)
    policy.update(trajectory, reward)
```

### Example: Multi-task STL

```python
# Multiple STL specifications
specs = [
    STLFormula("always", safety_predicate, (0, T)),
    STLFormula("eventually", goal_predicate, (0, T)),
    STLFormula("until", reach_avoid_predicates, (0, T))
]

# Combined stratified reward
def multi_stl_reward(trajectory):
    rewards = [evaluate_stratified(trajectory, spec) for spec in specs]
    return sum(rewards) / len(rewards)
```

---

**Source**: arxiv paper 2604.04923v1 - "Stratifying Reinforcement Learning with Signal Temporal Logic"
**Created**: 2026-04-07 by research-skill-creation-hourly cron job
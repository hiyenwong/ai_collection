---
name: sumo-whole-body-locomanipulation
description: Sim-to-real approach for dynamic whole-body loco-manipulation with test-time steering. Use when: (1) Designing legged robot control systems, (2) Implementing dynamic manipulation with heavy objects, (3) Building generalizable locomotion policies, (4) Transferring simulation-trained policies to real robots. Triggers: legged robots, whole-body control, loco-manipulation, sim-to-real transfer, dynamic manipulation, test-time steering, policy generalization.
---

# Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation

## Core Innovation

**Test-time steering** of pre-trained whole-body control policy enables diverse dynamic manipulation tasks without additional training.

**Key insight**: Sample-based planner + pre-trained policy = flexible, generalizable control.

## Problem Solved

Legged robots manipulating **large and heavy objects** dynamically:
- Objects heavier than nominal lifting capacity
- Objects larger/taller than robot itself
- Diverse tasks without task-specific training

## Technical Approach

### Three-Stage Architecture

#### Stage 1: Pre-train Whole-Body Policy

**Training approach**:
- Train in simulation
- Cover wide variety of manipulation scenarios
- Learn general locomotion + manipulation coordination

**Key: Broad coverage** → enables later generalization

#### Stage 2: Test-Time Steering

**Steering mechanism**:
- Sample-based planner provides high-level guidance
- Pre-trained policy executes low-level control
- Cost function adjustable at test time

**Benefit**: Single policy solves multiple tasks

#### Stage 3: Cost Function Tuning

**Flexible adaptation**:
- Adjust cost weights for task requirements
- No additional training needed
- Test-time configuration enables task diversity

## Real-World Demonstrations

### Spot Quadruped Tasks

1. **Upright a tire**
   - Heavier than robot's nominal lifting capacity
   - Dynamic whole-body coordination
   - Successfully executed

2. **Drag crowd-control barrier**
   - Larger and taller than robot
   - Requires sustained force
   - Demonstrates manipulation scale

### Humanoid Simulation Tasks

1. **Open a door**
   - Reach + pull coordination
   - Balance maintenance
   
2. **Push a table**
   - Continuous force application
   - Dynamic locomotion

**Key result**: Same approach generalizes across robots

## Generalization Mechanism

### Why Test-Time Steering Works

**Traditional approach**:
- Task-specific policy training
- Limited to trained scenarios
- Requires extensive data per task

**Sumo approach**:
- Single broad policy
- Planner guides to specific task
- Test-time cost tuning adapts behavior

### Generalization Evidence

**Across objects**:
- Different sizes ✓
- Different weights ✓
- Different shapes ✓

**Across tasks**:
- Pushing ✓
- Pulling ✓
- Uprighting ✓
- Dragging ✓

**Across robots**:
- Quadruped (Spot) ✓
- Humanoid (simulation) ✓

**Zero additional tuning or training**

## System Design Principles

### Principle 1: Pre-training Diversity

Train policy on:
- Wide range of object properties
- Various manipulation modes
- Diverse locomotion patterns

**Result**: Policy has broad coverage for test-time steering

### Principle 2: Hierarchical Control

**High-level**: Planner decides manipulation strategy
**Low-level**: Policy executes detailed coordination

**Benefit**: Separates task planning from motor control

### Principle 3: Test-Time Flexibility

Cost function structure:
```python
cost = w_force * force_cost + 
       w_balance * balance_cost + 
       w_progress * progress_cost
```

Adjust weights at test time → adapt to task requirements

## Implementation Guidance

### Training Pipeline

#### Step 1: Simulation Environment

**Requirements**:
- Physics-accurate simulator
- Wide object library
- Diverse manipulation scenarios

**Setup**:
```python
env = SimulationEnv(
    robot_type='spot',  # or 'humanoid'
    object_library=['tire', 'barrier', 'box', 'door'],
    manipulation_modes=['push', 'pull', 'upright', 'drag']
)
```

#### Step 2: Policy Architecture

**Whole-body policy**:
- Unified locomotion + manipulation
- End-to-end training
- Handles dynamic coordination

#### Step 3: Training Objective

**Reward structure**:
- Task completion bonus
- Force application efficiency
- Balance maintenance
- Energy efficiency

### Deployment Pipeline

#### Step 1: Task Specification

Define task requirements:
- Target object properties
- Desired manipulation mode
- Success criteria

#### Step 2: Planner Configuration

**Sample-based planner**:
- Generates action sequences
- Evaluates outcomes with policy
- Selects best trajectory

#### Step 3: Cost Function Tuning

**Task-specific weights**:
- Tire uprighting: High force weight
- Barrier dragging: High progress weight
- Door opening: High precision weight

#### Step 4: Real Robot Execution

**Safety considerations**:
- Balance monitoring
- Force limits
- Emergency stop conditions

## Comparison with Alternatives

| Method | Training | Task Flexibility | Real Transfer |
|--------|----------|------------------|---------------|
| **Sumo** | Single broad policy | High (test-time tuning) | Demonstrated |
| Task-specific RL | Per-task training | Low | Limited |
| Model-based control | No training | Medium | Simulation only |
| Hierarchical RL | Multiple policies | Medium | Limited |

## Technical Challenges Solved

### Challenge 1: Heavy Objects

**Problem**: Objects exceed nominal capacity
**Solution**: Dynamic whole-body coordination
- Use body momentum
- Exploit contact forces
- Sustained application strategy

### Challenge 2: Large Objects

**Problem**: Objects larger than robot
**Solution**: Multi-contact strategies
- Distributed force application
- Sequential manipulation phases
- Balance-aware planning

### Challenge 3: Task Diversity

**Problem**: Different tasks need different behaviors
**Solution**: Test-time steering
- Planner guides task-specific approach
- Policy provides execution capability
- Cost tuning adapts priorities

## Research Context

**arXiv**: 2604.08508v1  
**Authors**: John Z. Zhang, Maks Sorokin, Jan Brüdigam, Brandon Hung, Stephen Phillips  
**Published**: 2026-04-09  
**Project page**: https://sumo.rai-inst.com/

## Related Topics

- Legged Robot Control
- Whole-Body Manipulation
- Sim-to-Real Transfer
- Test-Time Adaptation
- Hierarchical Control
- Dynamic Manipulation

## Practical Applications

### Industrial Manipulation
- Warehouse object handling
- Construction material movement
- Heavy equipment positioning

### Field Operations
- Disaster response (moving debris)
- Search and rescue (clearing obstacles)
- Outdoor material transport

### Service Robotics
- Door opening for accessibility
- Furniture rearrangement
- Heavy item assistance

## Further Reading

Project videos and code: https://sumo.rai-inst.com/

---

**Core lesson**: Pre-train broad policy → steer at test time → solve diverse tasks. Test-time flexibility eliminates need for task-specific training while maintaining real-world effectiveness.
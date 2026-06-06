---
name: handoff-humanoid-control
description: "HANDOFF: Humanoid Agentic Task-Space Whole-Body Control methodology. Multi-teacher KL distillation for mixture-of-experts control architecture. Activation: humanoid control, whole-body control, task-space interface, multi-teacher distillation, MoE robotics."
---

# HANDOFF: Humanoid Agentic Whole-Body Control

## Paper Information

**Title**: HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers  
**arXiv ID**: 2606.06493  
**Published**: 2026-06-04  
**Authors**: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames  
**Categories**: cs.RO, cs.AI, cs.LG  
**PDF**: https://arxiv.org/pdf/2606.06493v1

## Core Contributions

### 1. Compact Task-Space Interface Design

**Problem**: Existing whole-body controllers require dense kinematic/spatial references that planners struggle to synthesize.

**Solution**: Design a compact, explicit interface that is:
- **Intuitive**: Easy for task planners to generate
- **General**: Works across diverse manipulation skills
- **Modular**: Separates task planning from control
- **Expressive**: Captures essential task semantics

### 2. Multi-Teacher KL Distillation

**Architecture**: Single student model distilled from three complementary specialists:

1. **Whole-body motion tracking specialist**
   - Safety-filtered data
   - Precise motion execution
   
2. **Locomotion specialist**
   - Dynamic movement
   - Terrain adaptation
   
3. **Fall-recovery specialist**
   - Safety recovery
   - Robustness enhancement

**Distillation Method**:
- Context-conditioned gating scheme
- KL divergence minimization
- Mixture-of-experts (MoE) student architecture

### 3. VLM-Driven Agentic Planner

**Features**:
- Natural language task specification
- No task-specific data or controller fine-tuning
- Real-time task roll-outs

## Key Technical Patterns

### Pattern 1: Task-Space Interface Design

```python
class TaskSpaceInterface:
    """
    Compact interface for task planning to control.
    
    Attributes:
        target_pose: 6D pose (position + orientation)
        grasp_state: Binary gripper state
        motion_speed: Execution speed parameter
        safety_constraints: Collision avoidance params
    """
    
    def __init__(self):
        self.target_pose = Pose()
        self.grasp_state = False
        self.motion_speed = 1.0
        self.safety_constraints = {}
    
    def from_natural_language(self, task_desc: str) -> TaskSpaceInterface:
        """Parse natural language task into interface params."""
        # VLM parses task semantics
        # Maps to compact interface parameters
        return self
```

### Pattern 2: Multi-Teacher Distillation Framework

```python
class HANDOFFDistillation:
    """
    Multi-teacher KL distillation for MoE student.
    
    Components:
        - Motion tracking teacher
        - Locomotion teacher  
        - Fall-recovery teacher
        - Context-conditioned gating
    """
    
    def __init__(self, num_experts=3):
        self.teachers = [
            MotionTrackingTeacher(),
            LocomotionTeacher(),
            FallRecoveryTeacher()
        ]
        self.student = MoEStudent(num_experts)
        self.gating_network = ContextGating()
    
    def distill(self, trajectories):
        """Distill multiple teachers into single student."""
        for trajectory in trajectories:
            # Get teacher predictions
            teacher_actions = [
                teacher.predict(trajectory) 
                for teacher in self.teachers
            ]
            
            # Compute gating weights
            context = trajectory.get_context()
            gate_weights = self.gating_network(context)
            
            # Weighted teacher combination
            target_action = sum(
                w * action for w, action in zip(gate_weights, teacher_actions)
            )
            
            # KL divergence loss
            student_action = self.student.predict(trajectory)
            loss = kl_divergence(student_action, target_action)
            
            # Update student
            self.student.update(loss)
```

### Pattern 3: Safety-Filtered Data Generation

```python
class SafetyFilter:
    """
    Safety filtering for motion tracking data.
    
    Ensures:
        - Collision-free trajectories
        - Joint limit compliance
        - Stability constraints
    """
    
    def filter_trajectory(self, trajectory):
        """Apply safety constraints to raw trajectory."""
        # Check collisions
        if self.check_collision(trajectory):
            trajectory = self.replan_collision_free(trajectory)
        
        # Enforce joint limits
        trajectory = self.enforce_joint_limits(trajectory)
        
        # Verify stability
        if not self.is_stable(trajectory):
            trajectory = self.add_stability_correction(trajectory)
        
        return trajectory
```

## System Engineering Principles

### 1. Interface Design Philosophy

**Compact Interface Design Pattern**:
- Minimize interface complexity
- Maximize expressiveness
- Enable modular system integration
- Support intuitive planner generation

### 2. Teacher Complementary Architecture

**Principle**: Teachers should be **complementary**, not redundant:
- Each teacher covers a distinct capability domain
- Minimal overlap reduces distillation complexity
- Coverage completeness ensures robustness

### 3. Context-Conditioned Gating

**Dynamic Expert Selection**:
- Context determines which expert is active
- Smooth expert transitions
- Avoid expert conflict/confusion

## Implementation Guidelines

### Step 1: Design Task-Space Interface

1. Identify essential task parameters
2. Minimize parameter count
3. Ensure planner compatibility
4. Test expressiveness across tasks

### Step 2: Train Specialist Teachers

1. Collect domain-specific trajectories
2. Apply safety filtering (for motion tracking)
3. Train individual specialists
4. Validate specialist performance

### Step 3: Implement Context Gating

1. Define context features
2. Design gating network architecture
3. Train gating weights
4. Validate smooth transitions

### Step 4: Distill Student Model

1. Initialize MoE student architecture
2. Collect mixed-domain trajectories
3. Compute teacher predictions
4. Minimize KL divergence
5. Validate student performance

### Step 5: Integrate VLM Planner

1. Define natural language task space
2. Map NL to interface parameters
3. Test end-to-end roll-outs
4. Validate no fine-tuning requirement

## Performance Metrics

### Manipulation Workspace
- **Large robust workspace**: State-of-the-art velocity tracking
- **Natural language tasks**: Multiple roll-outs without fine-tuning

### Hardware Deployment
- **Unitree G1 humanoid**: Real-world validation
- **No task-specific data**: Zero-shot adaptation

## Advantages over Prior Methods

| Method | Interface Type | Planner Burden | Multi-Task Support |
|--------|---------------|----------------|-------------------|
| Dense Kinematic | Complex | High | Limited |
| Spatial References | Dense | High | Moderate |
| **HANDOFF** | **Compact** | **Low** | **High** |

## Limitations

1. Requires multiple teacher training
2. Distillation complexity scales with expert count
3. Safety filtering needed for motion data
4. Context gating requires careful design

## Related Work Connections

- **Whole-Body Control**: Hybrid control frameworks
- **Locomotion**: Terrain-adaptive movement
- **Fall Recovery**: Robust safety systems
- **VLM Planning**: Language-driven task execution

## Use Cases

### 1. Humanoid Manipulation
- Natural language task specification
- Multi-skill whole-body control
- Real-world deployment

### 2. Mobile Manipulation
- Combined locomotion + manipulation
- Terrain adaptation
- Safety recovery

### 3. Agentic Robotics
- VLM-driven task planning
- Zero-shot task adaptation
- Modular controller design

## Activation Keywords

- humanoid control
- whole-body control
- task-space interface
- multi-teacher distillation
- MoE robotics
- VLM planner
- safety-filtered control
- complementary teachers
- KL distillation robotics
- agentic manipulation

## References

- Paper: https://arxiv.org/abs/2606.06493
- PDF: https://arxiv.org/pdf/2606.06493v1
- Categories: cs.RO, cs.AI, cs.LG

## Notes

- 22 pages, 9 figures
- Unitree G1 hardware validation
- No task-specific data or fine-tuning required
- Three complementary specialists distilled into single student

## Citation

```bibtex
@article{yang2026handoff,
  title={HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers},
  author={Yang, Lizhi and Li, Junheng and Poddar, Nehar and Hou, Yiling and Huh, Gio and Griffin, Robert and Gkioxari, Georgia and Ames, Aaron},
  journal={arXiv preprint arXiv:2606.06493},
  year={2026}
}
```
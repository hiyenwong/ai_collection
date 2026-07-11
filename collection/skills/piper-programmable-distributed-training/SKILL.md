---
name: piper-programmable-distributed-training
description: Piper framework for user-controllable distributed training that decouples parallelism strategy from runtime implementation using unified global training DAG intermediate representation. Use for distributed ML training, parallelism strategy design, and flexible training system architecture.
version: 1.0.0
category: systems-engineering
authors: ["Megan Frisella", "Shubham Tiwari", "Andy Ruan", "Yi Pan", "Parker Gustafson", "Mat Jacob", "Gilbert Bernstein", "Stephanie Wang"]
arxiv_id: "2606.11169"
submission_date: "2026-06-09"
activation_keywords: ["Piper", "distributed training", "parallelism strategy", "ZeRO", "pipeline parallelism", "expert parallelism", "training DAG", "DualPipe", "DeepSeek-V3", "strategy-implementation decoupling"]
---

# Piper: Programmable Distributed Training System

## Core Contribution

**Fundamental Problem**: Existing systems require manual strategy design + implementation, making adaptation difficult. General-purpose frameworks are tied to fixed parallelism strategies, hindering state-of-the-art integration.

**Solution**: **Decouple strategy from runtime implementation** using:
- **User declarations**: Model annotations + scheduling directives
- **Unified IR**: Global training DAG representing all computation/communication
- **Strategy-agnostic runtime**: Executes compiled per-device plans

## Architecture

### 1. Three-Level Abstraction

```
┌─────────────────────────────────────────┐
│  User Strategy Declaration              │  ← High-level annotations
│  (model annotations + directives)        │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Piper Intermediate Representation (IR) │  ← Unified global training DAG
│  (compute + communication operations)    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Per-Device Execution Plans             │  ← Compiled device-specific schedules
│  (strategy-agnostic runtime)             │
└─────────────────────────────────────────┘
```

### 2. Key Components

**A. Strategy Declaration Layer**

```python
# Example: DualPipe strategy declaration (DeepSeek-V3 style)
@piper.annotate(
    data_parallel=4,
    pipeline_parallel=8,
    expert_parallel=2,
    zero_stage=3
)
@piper.directive("DualPipe", schedule="interleaved_forward_backward")
class MyModel:
    def forward(self, x):
        # Model logic
        ...
```

**B. Intermediate Representation (IR)**

```python
class PiperIR:
    """
    Global Training DAG: unified representation of all operations.
    
    Nodes:
    - Compute operations (forward, backward, optimizer steps)
    - Communication operations (all-reduce, send/recv, all-to-all)
    
    Edges:
    - Data dependencies
    - Scheduling constraints
    """
    
    def __init__(self, model_annotations, directives):
        self.dag = self._build_global_dag(model_annotations)
        self._apply_directives(directives)
    
    def _build_global_dag(self, annotations):
        # Construct unified DAG from model structure
        ...
    
    def _apply_directives(self, directives):
        # Apply strategy transformations on DAG
        for directive in directives:
            self.dag = directive.transform(self.dag)
```

**C. Compilation Engine**

```python
def compile_per_device_plans(ir, num_devices):
    """
    Generate device-specific execution schedules.
    
    Inputs:
    - ir: Global training DAG
    - num_devices: Total devices
    
    Outputs:
    - device_plans[device_id]: Execution schedule for each device
    """
    device_plans = {}
    
    for device_id in range(num_devices):
        # Extract device-relevant operations
        device_ops = extract_device_operations(ir, device_id)
        
        # Schedule operations respecting dependencies
        schedule = schedule_operations(device_ops)
        
        device_plans[device_id] = schedule
    
    return device_plans
```

**D. Strategy-Agnostic Runtime**

```python
class PiperRuntime:
    """
    Distributed runtime that executes compiled plans.
    Independent of strategy - only executes scheduled operations.
    """
    
    def execute_plan(self, device_plan):
        for operation in device_plan:
            if operation.type == "compute":
                self.execute_compute(operation)
            elif operation.type == "communication":
                self.execute_communication(operation)
```

## Parallelism Strategies

### 1. Data Parallelism + ZeRO

```python
@piper.annotate(data_parallel=N, zero_stage=3)
@piper.directive("ZeRO", partition="optimizer_states+gradients+parameters")
```

**IR Transformation**:
- Partition optimizer states across devices
- All-reduce gradients after backward pass
- Broadcast parameters before forward pass

### 2. Pipeline Parallelism

```python
@piper.annotate(pipeline_parallel=P)
@piper.directive("Pipeline", schedule="GPipe")  # or "1F1B"
```

**IR Transformation**:
- Partition model layers across pipeline stages
- Insert send/recv operations for inter-stage communication
- Schedule forward/backward micro-batches

### 3. Expert Parallelism (MoE)

```python
@piper.annotate(expert_parallel=E)
@piper.directive("ExpertParallel", all_to_all="router+output")
```

**IR Transformation**:
- Partition experts across devices
- Insert all-to-all for token routing
- All-to-all for expert output aggregation

### 4. Composed Strategy - DualPipe (DeepSeek-V3)

```python
@piper.annotate(
    data_parallel=4,
    pipeline_parallel=8,
    expert_parallel=2
)
@piper.directive("DualPipe", schedule="interleaved_forward_backward")
```

**Key Innovation**: Joint scheduling of compute + communication in composed strategies.

## Implementation Steps

### Step 1: Model Annotation

```python
import piper

@piper.annotate(
    data_parallel=4,        # Number of data parallel replicas
    pipeline_parallel=8,    # Number of pipeline stages
    expert_parallel=2,      # Number of expert parallel groups
    zero_stage=3            # ZeRO optimization stage
)
class TransformerModel:
    def __init__(self, config):
        self.layers = [TransformerLayer(config) for _ in range(config.num_layers)]
    
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
```

### Step 2: Directive Application

```python
# Directive: transforms IR based on strategy
@piper.directive("DualPipe", 
    schedule="interleaved_forward_backward",
    communication_overlap=True,
    memory_optimization="activation_checkpointing"
)
```

### Step 3: IR Generation

```python
# Piper automatically generates unified DAG
ir = piper.generate_ir(model_annotations, directives)

# DAG structure
ir.nodes = [
    ComputeOp("forward_layer_0", device=0),
    ComputeOp("forward_layer_1", device=1),
    CommunicationOp("send_activation_0_to_1", src=0, dst=1),
    ComputeOp("backward_layer_1", device=1),
    CommunicationOp("all_reduce_gradients", devices=[0,1,2,3]),
    ...
]

ir.edges = [
    Dependency("forward_layer_0", "send_activation_0_to_1"),
    Dependency("send_activation_0_to_1", "forward_layer_1"),
    ...
]
```

### Step 4: Compilation

```python
# Compile per-device execution plans
device_plans = piper.compile(ir, num_devices=32)

# Example device plan
device_plans[0] = [
    {"op": "forward_layer_0", "time": 0},
    {"op": "send_activation", "time": 1},
    {"op": "backward_layer_0", "time": 2},
    {"op": "all_reduce_gradients", "time": 3},
    {"op": "optimizer_step", "time": 4}
]
```

### Step 5: Runtime Execution

```python
# Strategy-agnostic execution
runtime = PiperRuntime(num_devices=32)
runtime.execute(device_plans)
```

## Performance Results

### Baseline Comparison

| Strategy | Traditional Framework | Piper | Improvement |
|----------|----------------------|-------|-------------|
| ZeRO-3 | 1.0x baseline | 1.0x | Parity (maintained) |
| Pipeline | Manual tuning required | Auto-optimized | Faster deployment |
| DualPipe | Not supported | 1.15x throughput | Novel strategy enabled |

### Key Benefits

1. **Performance Parity**: Matches specialized implementations for common strategies
2. **Novel Strategies**: Enables state-of-the-art strategies (DualPipe) without custom runtime
3. **Memory Efficiency**: Joint scheduling reduces peak memory usage
4. **Deployment Speed**: Strategy changes via annotations, not code modifications

## Advantages vs Traditional Systems

| Aspect | Traditional | Piper |
|--------|------------|-------|
| Strategy implementation | Hand-coded runtime | declarative directives |
| Strategy adaptation | Code refactoring | Annotation modification |
| Novel strategies | Custom runtime needed | Directive + IR transform |
| Compute-communication scheduling | Sequential | Joint optimization |
| Memory optimization | Manual tuning | IR-level scheduling |

## Pitfalls

1. **IR Complexity**: Large models → complex DAG → compilation overhead
2. **Directive Availability**: New strategies require new directive implementations
3. **Device Constraints**: Compilation must respect physical device topology
4. **Communication Scheduling**: Overlapping compute/communication requires careful timing
5. **Debugging**: IR-level errors harder to trace than runtime-level errors

## Use Cases

### 1. Foundation Model Pretraining

```python
@piper.annotate(data_parallel=128, pipeline_parallel=8, zero_stage=3)
@piper.directive("ZeRO-3", communication_overlap=True)
# Large-scale GPT-style training
```

### 2. MoE Model Training

```python
@piper.annotate(expert_parallel=16, data_parallel=4)
@piper.directive("ExpertParallel", load_balancing="dynamic")
# Mixture-of-experts training
```

### 3. Hybrid Strategy (DeepSeek-V3)

```python
@piper.annotate(data_parallel=4, pipeline_parallel=8, expert_parallel=2)
@piper.directive("DualPipe", interleaved_schedule=True)
# Composed parallelism with communication overlap
```

## Verification

**Test Case**: ZeRO-3 strategy parity
```python
# Compare Piper ZeRO-3 vs traditional ZeRO-3
traditional_time = train_with_traditional_zero3(model, data)
piper_time = train_with_piper(model, data, annotations={"zero_stage": 3})

assert abs(piper_time - traditional_time) < tolerance  # Performance parity
```

## Related Skills

- [[distributed-training-strategies]] - Parallelism strategy overview
- [[zero-optimization]] - ZeRO memory optimization
- [[pipeline-parallelism]] - Pipeline scheduling patterns
- [[moe-training-systems]] - Expert parallelism architectures

## References

- Original paper: arXiv:2606.11169
- ZeRO: Rajbhandari et al., SC 2020
- Pipeline parallelism: Huang et al., GPipe 2019
- DualPipe: DeepSeek-V3 technical report 2024
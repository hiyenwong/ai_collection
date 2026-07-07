---
name: system-dse-deepstack
description: "DeepStack methodology for design space exploration (DSE) in system-hardware co-design. Scalable and accurate performance modeling for distributed 3D-stacked AI systems. Use when performing early-stage system design optimization, hardware-software co-design, or DSE for AI accelerators. Keywords: DSE, design space exploration, system design, hardware co-design, distributed systems, AI accelerators."
---

# System DSE with DeepStack

Design Space Exploration (DSE) methodology for system-hardware co-design using DeepStack performance modeling.

## Problem Statement

Cross-stack co-design is increasingly critical for AI efficiency. Traditional DSE approaches are either:
- Too slow for early-stage exploration
- Too inaccurate for reliable decisions
- Don't account for distributed system effects

## Solution: DeepStack

Accurate and efficient performance model for early-stage system-hardware co-design space exploration for distributed 3D-stacked AI systems.

## Core Methodology

### Step 1: Define Design Space

```python
Design parameters:
- System topology (distributed nodes)
- 3D-stack configuration (memory stacking)
- AI workload characteristics
- Interconnect bandwidth/latency
- Compute unit allocation
```

### Step 2: Performance Modeling

DeepStack models performance across layers:

```markdown
Stack layers:
1. Application layer (AI workload)
2. System layer (distributed topology)
3. Hardware layer (3D-stacked memory + logic)
4. Interconnect layer (chiplet communication)
```

### Step 3: Design Space Exploration

```python
DSE process:
1. Define constraints (power, area, latency)
2. Generate candidate designs
3. Evaluate with DeepStack model
4. Filter by performance criteria
5. Select Pareto-optimal designs
```

### Step 4: Early-stage Decision Making

```markdown
Use DeepStack for:
- Architecture selection
- Memory hierarchy design
- Distribution strategy
- Hardware-software partitioning
```

## Key Techniques

### Cross-stack Performance Modeling

```python
# Performance model components:
compute_latency = model_compute(workload, hardware)
memory_bandwidth = model_memory(3d_stack_config)
interconnect_cost = model_interconnect(topology)
total_performance = aggregate_stack(compute, memory, interconnect)
```

### Scalable DSE

```markdown
Optimization strategies:
- Prune infeasible designs early
- Use surrogate models for fast evaluation
- Parallel exploration of design branches
- Incremental refinement of promising designs
```

### Accuracy vs Efficiency Tradeoff

```python
# Balance accuracy and speed:
early_stage: fast surrogate models
mid_stage: hybrid (surrogate + detailed)
final_stage: detailed simulation
```

## Workflow Example

**Scenario**: Designing distributed AI accelerator for vision transformer.

```markdown
1. Define workload: Vision Transformer inference
2. Define constraints: 100W power, 10ms latency
3. Generate candidates:
   - 2-node vs 4-node distribution
   - 2-stack vs 4-stack memory
   - Different interconnect bandwidths
4. Evaluate with DeepStack
5. Filter by latency/power constraints
6. Select Pareto-optimal: 4-node, 4-stack, high bandwidth
```

## Best Practices

1. **Start broad, refine later**: Explore wide design space early
2. **Use constraints early**: Prune infeasible designs
3. **Cross-stack thinking**: Consider all layers together
4. **Validate models**: Compare with real measurements
5. **Document decisions**: Track why designs were selected/rejected

## Applications

- AI accelerator design
- Chiplet-based system design
- 3D-stacked memory optimization
- Distributed inference systems
- System-on-chip architecture selection

## Design Parameters Reference

| Parameter | Range | Impact |
|-----------|-------|--------|
| Node count | 2-16 | Parallelism, communication cost |
| Stack height | 2-8 layers | Memory bandwidth, thermal |
| Interconnect BW | 10-100 GB/s | Distribution efficiency |
| Compute units | 4-64 | Throughput, power |

## Performance Metrics

```markdown
Key metrics:
- Latency (ms)
- Throughput (samples/s)
- Power (W)
- Energy efficiency (samples/J)
- Area (mm²)
- Cost ($)
```

## Related Work

- **DeepFlow**: Cross-stack pathfinding framework
- **Timeloop**: DSE for accelerators
- **Cosmic**: Chiplet-based design
- **Accelergy**: Energy estimation

## Source Paper

**DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-stacked AI Systems**
- arxiv ID: 2604.04750
- Published: April 2026

## Related Skills

- **kg-research-workflow**: Import papers to knowledge graph
- **arxiv-search**: Search for latest systems papers
- **skill-creator**: Create skills from research

## Notes

- Early-stage DSE saves significant design time
- Accuracy critical for reliable decisions
- Cross-stack modeling essential for AI systems
- 3D-stacking introduces thermal constraints
- Distributed topology affects communication cost
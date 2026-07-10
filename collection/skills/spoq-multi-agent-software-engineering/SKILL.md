---
name: spoq-multi-agent-software-engineering
description: "SPOQ (Specialist Orchestrated Queuing) - Multi-agent software engineering methodology with wave-based topological dispatch, dual validation gates, and Human-as-an-Agent integration for automated SE tasks. Activation: multi-agent orchestration, software engineering agent, agent coordination, SPOQ, task dispatch, validation gates, quality control, agent hierarchy, wave dispatch. Tags: multi-agent, software-engineering, orchestration, coordination, quality-control, task-dispatch, validation."
metadata:
  arxiv_id: 2606.03115
  authors: "Royce Carbowitz, Dheeraj Kumar"
  published: "2026-06-02"
  categories: "cs.SE, cs.MA"
  paper_title: "SPOQ: Specialist Orchestrated Queuing for Multi-Agent Software Engineering"
---

# SPOQ: Multi-Agent Software Engineering Orchestration

## Core Innovation

SPOQ addresses three critical problems in multi-agent software engineering systems:
1. **Coordination overhead** - inefficient task dispatching across agents
2. **Quality control gaps** - insufficient validation leading to rework cycles  
3. **Limited human oversight** - inability to integrate human expertise dynamically

## Three-Tier Agent Hierarchy

SPOQ uses a cost-optimized agent hierarchy based on task complexity:

```
┌─────────────────────────────────────────────────────────────┐
│                     Opus Workers (Tier 1)                   │
│  - Complex multi-step reasoning tasks                      │
│  - Architectural design, refactoring                       │
│  - Highest cost, highest capability                        │
└─────────────────────────────────────────────────────────────┘
          │
          ├─────────────────────────────────────────────
          │
┌─────────────────────────────────────────────────────────────┐
│                    Sonnet Reviewers (Tier 2)                │
│  - Code review, validation                                  │
│  - Test generation                                          │
│  - Medium cost, balanced capability                         │
└─────────────────────────────────────────────────────────────┘
          │
          ├─────────────────────────────────────────────
          │
┌─────────────────────────────────────────────────────────────┐
│                    Haiku Investigators (Tier 3)             │
│  - Quick searches, fact-checking                           │
│  - Dependency analysis                                      │
│  - Lowest cost, fast execution                              │
└─────────────────────────────────────────────────────────────┘
```

## Wave-Based Topological Dispatch

### Algorithm

**Goal**: Execute tasks in parallel while respecting dependencies.

**Method**: Compute execution waves from task dependency graph:

```python
def compute_dispatch_waves(task_graph):
    """
    Compute parallel execution waves from dependency DAG.
    
    Wave 0: Tasks with no dependencies (can execute immediately)
    Wave n: Tasks whose dependencies all completed in waves < n
    
    Returns: List of task sets, each wave can execute in parallel
    """
    waves = []
    remaining = set(task_graph.nodes)
    completed = set()
    
    while remaining:
        # Find tasks whose dependencies are all completed
        wave_tasks = []
        for task in remaining:
            deps = task_graph.get_dependencies(task)
            if all(d in completed for d in deps):
                wave_tasks.append(task)
        
        if not wave_tasks:
            raise CycleError("Dependency cycle detected")
        
        waves.append(wave_tasks)
        completed.update(wave_tasks)
        remaining -= set(wave_tasks)
    
    return waves
```

### Performance Results

| Metric | Sequential | Wave Dispatch | Improvement |
|--------|-----------|---------------|-------------|
| Execution ratio vs critical path | 1.0 | 1.03-1.11 | Near-optimal |
| Max speedup | 1x | 14.3x | 14.3x |
| Stable speedup (2-slot backend) | 1x | 1.4x | 40% |

**Key insight**: Wave dispatch approaches the theoretical critical-path lower bound (optimal parallelization).

## Dual Validation Gates

SPOQ applies quality metrics **before AND after** execution to reduce rework cycles.

### Gate 1: Planning Validation (Pre-execution)

**Purpose**: Detect bad plans before executing them.

**Metrics**:
1. **Coverage**: Does the plan address all task requirements?
2. **Cyclicity**: Does the plan contain circular dependencies?
3. **Parallelism**: Can tasks be executed concurrently?

```python
def planning_validation_gate(plan, task_requirements):
    """
    Validate plan before execution.
    
    Returns: (approved, issues)
    """
    issues = []
    
    # Coverage check
    covered = set(plan.covered_requirements())
    missing = task_requirements - covered
    if missing:
        issues.append(f"Missing coverage: {missing}")
    
    # Cyclicity check
    if plan.has_cycles():
        issues.append("Plan contains circular dependencies")
    
    # Parallelism check
    waves = compute_dispatch_waves(plan.task_graph)
    parallelism_score = len(waves) / len(plan.tasks)
    if parallelism_score < 0.3:
        issues.append(f"Low parallelism: {parallelism_score}")
    
    approved = len(issues) == 0
    return (approved, issues)
```

### Gate 2: Code Validation (Post-execution)

**Purpose**: Detect defects before committing changes.

**Metrics**:
1. **Static analysis**: Linting, type checking
2. **Test execution**: Unit tests, integration tests
3. **Semantic checks**: Does code match plan intent?

### Results

| Metric | Before Dual Gates | After Dual Gates | Improvement |
|--------|-------------------|------------------|-------------|
| Defects per task | 0.34 | 0.20 | 41% reduction |
| Test pass rate | 91.25% | 99.75% | 8.5% improvement |
| Planning coverage | 93.0 | 99.75 | 6.75 improvement |
| Cyclic plans eliminated | No | Yes | 100% elimination |
| Parallelism score | 31.0 | 75.25 | 2.4x improvement |

## Human-as-an-Agent (HaaA) Integration

### Concept

Human specialists participate in the agent hierarchy as **first-class agents**:
- **Decomposition phase**: Human helps break down complex tasks
- **Execution phase**: Agents can consult human via query mechanism
- **Review phase**: Human reviews final artifacts

### Implementation Pattern

```python
class HumanAgent:
    """
    Human specialist as first-class agent in hierarchy.
    """
    def __init__(self, specialty, consultation_cost):
        self.specialty = specialty
        self.consultation_cost = consultation_cost
        self.availability = "on-demand"
    
    def can_handle(self, task):
        """
        Human can handle tasks requiring domain expertise.
        """
        return task.requires_human_expertise
    
    def consult(self, question, context):
        """
        Other agents query human via structured prompts.
        Returns: (answer, confidence, cost)
        """
        prompt = f"[{self.specialty}] {question}\nContext: {context}"
        # External human response mechanism
        response = await human_interface.query(prompt)
        return (response.answer, response.confidence, self.consultation_cost)
```

### Results with Human Review

| Metric | Without Human | With Human Review | Improvement |
|--------|--------------|-------------------|-------------|
| Residual defects per task | 0.47 | 0.03 | 94% reduction |

**Key insight**: Human review catches defects that automated gates miss, especially nuanced semantic errors.

## Experimental Validation

### Experiment 1: Wave Dispatch Efficiency
- **Setup**: 100-task dependency graphs with varying complexity
- **Result**: Wave dispatch achieves 1.03-1.11x critical-path ratio (near-optimal)
- **Max speedup**: 14.3x on high-parallelism graphs
- **Stable speedup**: 1.4x on 2-slot backend (realistic constraint)

### Experiment 2: Planning Quality
- **Setup**: 400 planning tasks across 4 complexity levels
- **Metrics**: Coverage, cyclicity, parallelism
- **Result**: Planning coverage 93→99.75, cyclicity eliminated, parallelism 31→75.25

### Experiment 3: Defect Reduction
- **Setup**: 800 code generation tasks
- **Metrics**: Defects per task, test pass rate
- **Result**: Defects 0.34→0.20, test pass rate 91.25%→99.75%

### Experiment 4: Human Review Impact
- **Setup**: 200 tasks with human specialist review
- **Metric**: Residual defects after all validation gates
- **Result**: Residual defects 0.47→0.03 (94% reduction)

### Longitudinal Study (Ecological Validation)

**Scale**: 17 repositories, 8,589 commits, 1,822 tasks, 13,866 tests
**Pass rate**: 99.87%
**Duration**: Multi-month deployment
**Conclusion**: SPOQ scales to real-world software engineering workloads.

## Open-Weights Replication

**Model**: Qwen3.6-35B-A3B (locally hosted)
**Result**: All gains replicated, proving orchestration methodology is model-agnostic.

**Key finding**: SPOQ's improvements come from orchestration patterns, not specific model capabilities.

## Methodology Patterns

### Pattern 1: Wave Dispatch for Parallelization

**When to use**: Multi-task workflows with dependencies (refactoring, feature development)

**Steps**:
1. Build task dependency graph
2. Compute dispatch waves (topological sort)
3. Execute each wave in parallel
4. Collect results before next wave

**Benefits**: Near-critical-path efficiency, automatic parallelization

### Pattern 2: Dual Validation for Quality

**When to use**: Code generation, refactoring, test writing

**Steps**:
1. Plan generation → Planning validation gate
2. If approved → Execute
3. Result → Code validation gate
4. If approved → Commit, else → Rework

**Benefits**: 41% defect reduction, 8.5% test pass improvement

### Pattern 3: HaaA for Expert Integration

**When to use**: Tasks requiring domain expertise (security, architecture)

**Steps**:
1. Identify tasks needing human expertise
2. Invoke human consultation during decomposition
3. Allow agent queries to human during execution
4. Human reviews final artifacts

**Benefits**: 94% residual defect reduction

## Implementation Checklist

1. **Define agent hierarchy** (Opus/Sonnet/Haiku tiers or equivalents)
2. **Build task dependency graph** (explicit dependencies)
3. **Implement wave dispatch algorithm** (topological sort)
4. **Define planning validation metrics** (coverage, cyclicity, parallelism)
5. **Define code validation metrics** (linting, tests, semantics)
6. **Set up HaaA query mechanism** (structured prompts, response interface)
7. **Configure cost-quality tradeoffs** (tier selection per task)
8. **Monitor longitudinal metrics** (defect rate, test pass rate)

## Comparison to Baseline Approaches

| Approach | Parallelism | Defect Rate | Human Integration |
|----------|-------------|-------------|-------------------|
| Sequential dispatch | Low (1x) | High (0.34) | None |
| Random assignment | Low | High | None |
| Centralized orchestrator | Medium | Medium (0.28) | Minimal |
| SPOQ wave dispatch | High (14.3x max) | Low (0.20) | Full HaaA |

## Limitations

1. **Dependency graph construction**: Requires accurate task dependency modeling
2. **Wave latency**: Tasks in later waves must wait for earlier waves
3. **Human availability**: HaaA depends on specialist availability
4. **Cost optimization**: Requires tuning tier assignments per task type

## Related Skills

- [[agent-coordinator]] - Task decomposition and agent selection
- [[multi-agent-orchestration]] - Multi-agent workflow patterns
- [[agent-delegation-rules]] - Delegation and capability boundaries
- [[kanban-orchestrator]] - Kanban-based task coordination

## References

- arXiv:2606.03115 - SPOQ paper with full experimental details
- Hayek economic theory - Decentralized coordination inspiration
- Critical path method - Lower bound for parallelization
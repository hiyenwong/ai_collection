---
name: iot-cps-workflow-scheduling
description: "Multi-objective and multi-constrained IoT workflow scheduling in Edge-Hub-Cloud Cyber-Physical Systems using continuous-time mixed integer linear programming. Optimizes latency, energy, and reliability with selective task duplication. Activation: IoT scheduling, CPS workflow, edge computing, task scheduling, multi-objective optimization."
---

# IoT Workflow Scheduling in Edge-Hub-Cloud CPS

> Exact multi-objective and multi-constrained workflow scheduling for IoT-enabled cyber-physical applications using continuous-time MILP with selective task duplication.

## Metadata
- **Source**: arXiv:2604.24340
- **Authors**: Andreas Kouloumpris, Georgios L. Stavrinides, Maria K. Michael, Theocharis Theocharides
- **Published**: 2026-04-27
- **Category**: Systems Engineering, Cyber-Physical Systems, IoT Scheduling

## Problem Context

### Target System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      CLOUD SERVER                          │
│              (High capacity, high latency)                  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    │  HUB DEVICE │
                    │ (Orchestrator)│
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────┴────┐        ┌────┴────┐        ┌────┴────┐
   │ EDGE 1  │        │ EDGE 2  │        │ EDGE N  │
   │(Hetero- │        │(Hetero- │        │(Hetero- │
   │ geneous │        │ geneous │        │ geneous │
   │ Cores)  │        │ Cores)  │        │ Cores)  │
   └─────────┘        └─────────┘        └─────────┘
```

### Constraint Types

1. **Deadline Constraints**: End-to-end latency requirements
2. **Reliability Constraints**: Minimum reliability threshold per task/application
3. **Capability Constraints**: Task-to-device capability matching
4. **Resource Constraints**: Memory, storage, energy limitations
5. **Dependency Constraints**: Task precedence relationships

## Core Methodology

### Continuous-Time MILP Formulation

#### Decision Variables

| Variable | Description |
|----------|-------------|
| $x_{i,j,k}$ | Binary: Task $i$ assigned to device $j$ on core $k$ |
| $s_i$ | Continuous: Start time of task $i$ |
| $f_i$ | Continuous: Finish time of task $i$ |
| $d_i$ | Binary: Task $i$ duplicated for reliability |
| $c_{i,j}$ | Binary: Communication between tasks $i$ and $j$ |

#### Objective Function (Multi-Objective)

```
Minimize: α × Latency + β × Energy + γ × (1 - Reliability)

Where:
- Latency = max(f_i) - min(s_i)  # Makespan
- Energy = Σ(energy_consumption_per_task)
- Reliability = Π(task_reliability × duplication_benefit)
- α, β, γ: Trade-off weights (configurable)
```

#### Key Constraints

**1. Timing Constraints**
```
f_i = s_i + execution_time(i, device, core)
f_j ≥ f_i + communication_time(i, j)  ∀(i,j) ∈ dependencies
f_last ≤ deadline
```

**2. Reliability Constraints**
```
reliability(task) ≥ min_reliability_threshold
duplication_benefit = 1 - (1 - p)^n  for n replicas
```

**3. Resource Constraints**
```
Σ(memory_i) ≤ device_memory_capacity
Σ(storage_i) ≤ device_storage_capacity
energy_consumed ≤ device_energy_budget
```

**4. Capability Constraints**
```
x_{i,j,k} ≤ capability_match(task_i, device_j)
```

### Selective Task Duplication Strategy

Unlike naive replication, selective duplication:

1. **Identifies Critical Tasks**: Tasks on the critical path or with low individual reliability
2. **Cost-Benefit Analysis**: Duplicates only when reliability gain outweighs resource cost
3. **Placement Optimization**: Places duplicates on different devices for fault tolerance

```python
def should_duplicate(task, current_reliability, cost_benefit_threshold=1.2):
    """
    Determine if task should be duplicated.
    
    Args:
        task: Task object with properties
        current_reliability: Current path reliability
        cost_benefit_threshold: Minimum benefit/cost ratio
    
    Returns:
        Boolean: True if duplication is beneficial
    """
    reliability_without = current_reliability / task.reliability
    reliability_with = reliability_without * (1 - (1 - task.reliability)**2)
    
    reliability_gain = reliability_with - reliability_without
    resource_cost = task.resource_cost * duplication_overhead
    
    benefit_cost_ratio = reliability_gain / resource_cost
    return benefit_cost_ratio > cost_benefit_threshold
```

## Implementation Guide

### Step 1: Model the Workflow as DAG

```python
from typing import Dict, List, Tuple
import networkx as nx

def create_workflow_dag(tasks: List[Dict], dependencies: List[Tuple]) -> nx.DiGraph:
    """
    Create workflow DAG from task definitions.
    
    Args:
        tasks: List of task dicts with 'id', 'execution_time', 'memory', etc.
        dependencies: List of (from_task, to_task) tuples
    
    Returns:
        networkx.DiGraph representing the workflow
    """
    G = nx.DiGraph()
    
    for task in tasks:
        G.add_node(task['id'], **task)
    
    for from_task, to_task in dependencies:
        G.add_edge(from_task, to_task)
    
    # Validate DAG
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Workflow contains cycles")
    
    return G
```

### Step 2: Define System Architecture

```python
class CPSArchitecture:
    """Edge-Hub-Cloud architecture model."""
    
    def __init__(self):
        self.edge_devices = []  # List of EdgeDevice objects
        self.hub = None         # HubDevice object
        self.cloud = None       # CloudServer object
    
    def add_edge_device(self, device_id, cores, memory, storage, 
                        capabilities, reliability):
        """Add heterogeneous edge device."""
        self.edge_devices.append({
            'id': device_id,
            'cores': cores,  # List of core types
            'memory': memory,
            'storage': storage,
            'capabilities': capabilities,
            'reliability': reliability
        })

def create_heterogeneous_system():
    """Create example heterogeneous CPS architecture."""
    arch = CPSArchitecture()
    
    # Add diverse edge devices
    arch.add_edge_device(
        device_id='edge_1',
        cores=['ARM_Cortex_A53', 'ARM_Cortex_A72'],  # Heterogeneous cores
        memory=4,      # GB
        storage=32,    # GB
        capabilities=['sensor_processing', 'actuation', 'inference'],
        reliability=0.95
    )
    
    arch.add_edge_device(
        device_id='edge_2',
        cores=['RISC_V_4core'],
        memory=2,
        storage=16,
        capabilities=['sensor_processing', 'low_power'],
        reliability=0.92
    )
    
    return arch
```

### Step 3: Build MILP Model

```python
from docplex.mp.model import Model  # IBM CPLEX
import numpy as np

def build_scheduling_model(workflow: nx.DiGraph, 
                           architecture: CPSArchitecture,
                           objectives: Dict[str, float]):
    """
    Build MILP model for multi-objective workflow scheduling.
    
    Args:
        workflow: Task dependency DAG
        architecture: CPS system architecture
        objectives: Dict with weights for 'latency', 'energy', 'reliability'
    
    Returns:
        docplex.Model instance
    """
    mdl = Model(name='IoT_CPS_Scheduling')
    
    # Get all tasks and devices
    tasks = list(workflow.nodes())
    devices = (architecture.edge_devices + 
               [architecture.hub] + 
               [architecture.cloud])
    
    # Decision variables
    # x[i,j,k] = 1 if task i on device j core k
    x = {(i, j, k): mdl.binary_var(name=f'x_{i}_{j}_{k}')
         for i in tasks
         for j in range(len(devices))
         for k in range(len(devices[j]['cores']))}
    
    # Start time variables
    s = {i: mdl.continuous_var(name=f's_{i}') for i in tasks}
    
    # Finish time = start + execution
    f = {i: mdl.continuous_var(name=f'f_{i}') for i in tasks}
    
    # Duplication decision
    d = {i: mdl.binary_var(name=f'd_{i}') for i in tasks}
    
    # Add constraints... (timing, resource, reliability)
    
    # Objective: weighted sum
    alpha = objectives.get('latency', 0.33)
    beta = objectives.get('energy', 0.33)
    gamma = objectives.get('reliability', 0.34)
    
    # Makespan (latency)
    makespan = mdl.max(f[i] for i in tasks)
    
    # Total energy
    total_energy = mdl.sum(
        x[i,j,k] * energy_cost(i, devices[j], k)
        for i in tasks for j in range(len(devices)) 
        for k in range(len(devices[j]['cores']))
    )
    
    # Reliability (to maximize, so minimize negative)
    reliability = mdl.sum(
        d[i] * duplication_benefit(i) 
        for i in tasks
    )
    
    mdl.minimize(alpha * makespan + beta * total_energy - gamma * reliability)
    
    return mdl
```

### Step 4: Solve and Extract Schedule

```python
def solve_and_extract_schedule(model, time_limit=300):
    """
    Solve MILP and extract the schedule.
    
    Args:
        model: docplex.Model instance
        time_limit: Maximum solve time in seconds
    
    Returns:
        Schedule dict with task assignments and timing
    """
    model.set_time_limit(time_limit)
    solution = model.solve()
    
    if solution is None:
        raise RuntimeError("No feasible solution found")
    
    # Extract schedule
    schedule = {
        'makespan': solution.objective_value,
        'task_assignments': {},
        'start_times': {},
        'duplications': {}
    }
    
    # Extract variable values...
    
    return schedule
```

## Performance Characteristics

Based on experimental evaluation:

| Metric | Improvement vs Heuristic |
|--------|---------------------------|
| Latency | Up to **29.83%** average improvement |
| Energy | Up to **33.96%** average improvement |
| Reliability | Up to **28.49%** average improvement |

### Practical Scalability

- Tested on task graphs of sizes relevant to IoT applications
- Practical runtimes achieved through:
  - Problem decomposition
  - Selective constraint application
  - Warm-start heuristics

## Applications

### 1. Industrial IoT
- Manufacturing workflow scheduling on factory floors
- Predictive maintenance task orchestration

### 2. Smart Healthcare
- Medical device coordination in hospitals
- Emergency response workflow management

### 3. Autonomous Systems
- Drone fleet task allocation
- Autonomous vehicle coordination

### 4. Smart Buildings
- HVAC and lighting control workflows
- Security and access control systems

## Pitfalls

1. **Computational Complexity**: MILP is NP-hard; large workflows may need heuristic pre-processing
2. **Device Heterogeneity**: Core types must be accurately characterized
3. **Communication Costs**: Edge-hub-cloud communication can dominate latency
4. **Reliability Modeling**: Task reliability estimates may be uncertain
5. **Dynamic Environments**: Static scheduling doesn't handle runtime failures

## Extensions

### Online Scheduling
For dynamic environments, extend with:
- Rolling horizon optimization
- Runtime task migration
- Fault-triggered rescheduling

### Machine Learning Integration
- Use learned execution time predictors
- Reinforcement learning for adaptive scheduling
- Neural heuristics for warm-start

## Related Skills
- edge-hub-cloud-scheduling
- distributed-systems-optimization
- cyber-physical-systems
- multi-objective-optimization

## References
- Kouloumpris, A., Stavrinides, G.L., Michael, M.K., & Theocharides, T. (2026). "Exact, Efficient, and Reliable Multi-Objective and Multi-Constrained IoT Workflow Scheduling in Edge-Hub-Cloud Cyber-Physical Systems." arXiv:2604.24340

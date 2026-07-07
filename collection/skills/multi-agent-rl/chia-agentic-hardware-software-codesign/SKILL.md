---
name: chia-agentic-hardware-software-codesign
description: CHIA framework for principled agentic AI-driven hardware/software co-design. Treat hardware/software design flows as directed cyclic graphs (CHIA loops) with nodes executing SoC design tools, simulators, AI models, and evolutionary agents. Supports Chipyard, gem5, ChampSim, FireSim, Vivado, AlphaEvolve, and more. Enables isolation, profiling, fault-tolerant execution, and reliability across heterogeneous systems.
activation_keywords:
  - CHIA
  - agentic AI
  - hardware software co-design
  - computer architecture
  - systems engineering
  - RTL generation
  - gem5 simulation
  - Chipyard
  - FireSim
  - Vivado
  - AlphaEvolve
  - evolutionary agents
  - microarchitectural optimization
  - IPC optimization
  - critical path optimization
  - GitHub issue automation
  - 硬件软件协同设计
  - 智能体驱动设计
  - 系统工程
  - 计算机架构
arxiv_id: 2606.27350
authors: Angela Cui, Ferran Hermida-Rivera, Jack Toubes, Raghav Gupta, Jim Fang, Chengyi Lux Zhang, Ella Schwarz, Junha Kim, Yakun Sophia Shao, Borivoje Nikolic, Christopher W. Fletcher, Sagar Karandikar
published: 2026-06-25
categories:
  - cs.AR
  - cs.AI
  - cs.SE
---

# CHIA: Agentic AI-Driven Hardware/Software Co-Design Framework

## Core Contribution

CHIA (Agentic AI Hardware/Software Co-design) is an open-source framework that enables principled research on AI-driven hardware/software co-design. It treats the construction and deployment of co-design flows as a first-class objective.

## Key Innovation: CHIA Loops

CHIA expresses agentic AI-driven hardware and software design flows as **directed cyclic graphs** called **CHIA loops**. Each node executes:

- System-on-chip design tools (Chipyard, Hammer, Vivado)
- Microarchitectural simulators (gem5, ChampSim)
- Software build systems
- AI models (LLMs, evolutionary agents)
- Evolutionary coding agents (AlphaEvolve, AdaEvolve)

## Framework Components

### 1. CHIA Library

Provides node implementations for popular tools:
- **Chipyard**: Agile SoC design framework
- **gem5**: Architectural simulation
- **ChampSim**: Cache simulator
- **FireSim**: FPGA-accelerated simulation
- **Hammer**: Physical design (commercial CAD tools)
- **Vivado**: FPGA synthesis
- **AlphaEvolve**: LLM-based evolutionary agents
- **AdaEvolve**: Adaptive evolutionary agents

### 2. Principled Science Features

- **Isolation**: Separates AI models from hardware tools
- **Profiling**: Performance monitoring mechanisms
- **Fault tolerance**: Robust execution handling
- **Scalability**: Reliability across hundreds of heterogeneous systems
- **Multi-platform**: CPUs, FPGAs, GPUs across cloud/on-prem

## Case Studies

### 1. RTL-to-gem5 Simulator Alignment
Automatic generation and alignment of RTL with gem5 simulators for consistency verification.

### 2. LLM-Driven Microarchitectural Feature Implementation
Agentic AI automatically implements microarchitectural features in RTL code.

### 3. IPC-Aware Critical Path Optimization
Intelligent optimization of instruction-level parallelism aware of critical paths.

### 4. Evolutionary Architectural Discovery
Evolutionary agents discover novel architectural configurations.

### 5. Maintainer-Friendly GitHub Issue Fixing
Agentic automation for resolving hardware/software design issues.

## Implementation Patterns

### Creating a CHIA Loop

```python
# CHIA loop definition as directed cyclic graph
from chia import Loop, Node, Edge

loop = Loop(
    nodes=[
        Node("chipyard", tool="chipyard", config="soconfig.yaml"),
        Node("gem5_sim", tool="gem5", workload="benchmark_suite"),
        Node("llm_agent", model="claude-3", task="rtl_optimization"),
        Node("alphaevolve", strategy="evolutionary"),
    ],
    edges=[
        Edge("chipyard", "gem5_sim", "rtl_output"),
        Edge("gem5_sim", "llm_agent", "perf_metrics"),
        Edge("llm_agent", "alphaevolve", "optimization_hints"),
        Edge("alphaevolve", "chipyard", "design_candidates"),
    ]
)

# Execute with fault tolerance
result = loop.run(
    isolation=True,
    profiling=True,
    fault_tolerance="retry",
    max_retries=3
)
```

### Node Configuration

```yaml
# Node configuration for gem5 simulation
node:
  name: gem5_simulation
  tool: gem5
  config:
    cpu_model: O3CPU
    cache_hierarchy: MESI_two_level
    memory: DDR4_2400
  workload:
    type: spec2017
    benchmarks: [600.perlbench, 603.bwaves]
  output:
    format: json
    metrics: [ipc, cache_miss_rate, branch_mispredict_rate]
```

## System Engineering Principles

### 1. Directed Cyclic Graphs

CHIA loops enable:
- **Composition**: Nodes can be chained in cycles
- **Iteration**: Feedback loops for iterative optimization
- **Parallelization**: Independent nodes execute concurrently

### 2. Tool Abstraction

Each node abstracts:
- **Input/output formats**: Standardized interfaces
- **Execution semantics**: Fault-tolerant execution
- **Resource management**: CPU/GPU/FPGA allocation

### 3. Agent Integration

Supports multiple agent types:
- **LLM-based**: Code generation, design exploration
- **Evolutionary**: Architectural search, parameter optimization
- **Reinforcement learning**: Policy optimization

## Research Methodology

### Experiment Design

```python
# Principled experiment with isolation
from chia.experiment import Experiment

exp = Experiment(
    loop=my_chia_loop,
    isolation_level="tool_agent",
    profiling=["latency", "memory", "gpu_util"],
    seed=42,
    repetitions=5
)

# Run with credibility checks
results = exp.run_multi_seed(seeds=[42, 123, 456, 789, 1024])
```

### Fault Tolerance Patterns

```python
# Retry with exponential backoff
from chia.fault_tolerance import RetryHandler

handler = RetryHandler(
    strategy="exponential_backoff",
    max_retries=5,
    initial_delay=2.0,
    max_delay=60.0
)

node.configure(handler=handler)
```

## Deployment Architecture

### Heterogeneous System Support

- **Cloud**: AWS, GCP, Azure
- **On-prem**: Local clusters
- **FPGA**: FireSim infrastructure
- **GPU**: CUDA nodes

### Reliability Patterns

- **Checkpointing**: State persistence across failures
- **Hot-swap**: Replace nodes without stopping loop
- **Monitoring**: Real-time health checks

## Applications

### Computer Architecture Research
- Automated design space exploration
- Microarchitectural optimization
- Performance modeling

### Compiler Optimization
- LLVM pass optimization
- Code generation strategies

### VLSI Design
- RTL generation
- Physical design flows
- DRC checking

## Open Source Stack

- **Code**: github.com/chia-framework/chia
- **Documentation**: chia-framework.org
- **Nodes**: Pre-built implementations
- **Examples**: Case study implementations

## Pitfalls

### 1. Tool Version Compatibility
Different versions may produce incompatible outputs. Always specify exact tool versions in node config.

### 2. Agent Prompt Design
LLM agents require precise prompts for hardware design tasks. Use domain-specific templates.

### 3. Resource Allocation
Gem5 simulations consume significant memory. Profile node resource requirements before deployment.

### 4. Loop Deadlocks
Cyclic graphs can deadlock if nodes wait indefinitely. Implement timeout mechanisms.

### 5. Simulation-Real Gap
FireSim FPGA results may differ from gem5. Validate across multiple platforms.

## Related Skills

- `agent-first-bootstrap`: Agent-first methodology
- `hardware-aware-quantum-compilation`: Hardware-aware compilation
- `agentic-scientific-workflow`: Agentic research workflows
- `distributed-quantum-control-architecture`: Distributed control architecture

## References

- Paper: arXiv:2606.27350
- GitHub: https://github.com/chia-framework/chia
- Tools: Chipyard, gem5, FireSim, AlphaEvolve, AdaEvolve

---
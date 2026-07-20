---
name: hybrid-quantum-classical-framework
description: "Design dataflow-based hybrid quantum-classical computing architectures. Combine remote quantum computers with cloud/distributed systems. Activation: hybrid quantum classical, quantum classical hybrid, 混合量子经典, dataflow quantum, quantum cloud computing."
---

# Hybrid Quantum-Classical Computing Framework

## Description
A skill for designing and implementing dataflow-based hybrid quantum-classical computing architectures. Enables composition of quantum algorithms with classical computing, cloud services, and distributed systems through graph-based representations.

## Activation Keywords
- hybrid quantum classical
- quantum classical hybrid
- 混合量子经典
- dataflow quantum
- quantum cloud computing
- quantum distributed computing
- quantum workflow
- hybrid algorithm design
- Tierkreis framework

## Recommended Model
- **sonnet4.5** (For framework design and implementation)
- **opus4.5** (For complex distributed system design)

## Tools Used
- **exec**: Run quantum simulators and classical computing code
- **write**: Create workflow specifications and configuration files
- **read**: Load quantum algorithm templates and classical computing patterns
- **web_search**: Search for hybrid quantum-classical examples

## Core Concepts

### Dataflow Graph Representation
Higher-order dataflow graph program representation for hybrid quantum-classical algorithms:

| Component | Description |
|-----------|-------------|
| **Nodes** | Quantum operations, classical computations, cloud services |
| **Edges** | Data flow between quantum and classical components |
| **Graphs** | Composable, reusable algorithm modules |

### Key Design Principles

1. **Compositional Architecture**
   - Modular quantum-classical hybrid algorithms
   - Graph-based representation reflects algorithm visualization
   - Automatic parallelism and asynchronicity

2. **Remote Quantum Computing**
   - Cloud-accessible quantum processors
   - Distributed quantum-classical execution
   - Long-running algorithm support

3. **Cloud Integration**
   - Quantum cloud services (AWS Braket, IBM Quantum, Azure Quantum)
   - Classical cloud resources (compute, storage, networking)
   - Hybrid workflow orchestration

### Architecture Components

```
┌─────────────────────────────────────────┐
│         Hybrid Computing Layer          │
│  ┌─────────────┐    ┌────────────────┐ │
│  │ Quantum     │    │ Classical      │ │
│  │ Operations  │◄──►│ Computing      │ │
│  └─────────────┘    └────────────────┘ │
│           ▲                   ▲         │
│           │                   │         │
│           └───────────────────┘         │
│         Dataflow Graph Layer            │
└─────────────────────────────────────────┘
           ▲                   ▲
           │                   │
┌──────────┴───────┐  ┌────────┴────────┐
│  Quantum Cloud   │  │ Classical Cloud │
│  (Remote QPU)    │  │ (Compute/Storage)│
└──────────────────┘  └──────────────────┘
```

## Usage Patterns

### Pattern 1: Design Hybrid Algorithm
```
设计混合量子-经典算法架构
```

### Pattern 2: Integrate Quantum Cloud Services
```
集成量子云服务到数据流框架
```

### Pattern 3: Optimize Hybrid Workflow
```
优化量子-经典混合工作流的并行性
```

## Instructions for Agents

### Step 1: Identify Hybrid Requirements
Analyze the computational requirements:

| Question | Implication |
|----------|-------------|
| What quantum operations? | QPU requirements (qubits, gates) |
| What classical processing? | CPU/GPU requirements |
| How much data transfer? | Network bandwidth needs |
| How long running? | Cloud service duration |

Ask clarifying questions:
- What quantum operations are needed?
- What classical preprocessing/postprocessing?
- Is the quantum computer remote (cloud)?
- What's the data flow pattern?

### Step 2: Design Dataflow Graph
Create graph-based representation:

**Graph Structure:**
1. **Quantum Nodes**: QPU operations
   - Gate sequences
   - Measurements
   - Error correction

2. **Classical Nodes**: CPU operations
   - Data preprocessing
   - Parameter optimization
   - Post-measurement processing

3. **Edges**: Data dependencies
   - Quantum → Classical: measurement results
   - Classical → Quantum: parameters, initial states

**Example Dataflow Graph:**
```python
# Hybrid variational algorithm dataflow
dataflow_graph = {
    'nodes': [
        {'id': 'prep', 'type': 'classical', 'op': 'prepare_data'},
        {'id': 'init', 'type': 'classical', 'op': 'initialize_params'},
        {'id': 'quantum', 'type': 'quantum', 'op': 'variational_circuit'},
        {'id': 'measure', 'type': 'quantum', 'op': 'measure'},
        {'id': 'optimize', 'type': 'classical', 'op': 'gradient_descent'}
    ],
    'edges': [
        ('prep', 'init', 'data'),
        ('init', 'quantum', 'params'),
        ('quantum', 'measure', 'state'),
        ('measure', 'optimize', 'results'),
        ('optimize', 'quantum', 'new_params')  # Feedback loop
    ]
}
```

### Step 3: Configure Quantum Cloud Integration
Select and configure quantum cloud provider:

| Provider | Features | Suitable For |
|----------|----------|--------------|
| **IBM Quantum** | Circuit-based, simulators | Variational algorithms |
| **AWS Braket** | Multiple backends | Hybrid workflows |
| **Azure Quantum** | IonQ, Honeywell | Hardware diversity |
| **Google Cirq** | Gate-based | NISQ algorithms |

**Configuration Template:**
```yaml
quantum_cloud:
  provider: "ibm_quantum"
  backend: "ibmq_manila"
  qubits: 5
  shots: 1000
  
classical_cloud:
  provider: "aws"
  compute: "lambda"
  storage: "s3"
  
workflow:
  name: "hybrid_algorithm"
  type: "variational"
  iterations: 100
  parallel: true
  async: true
```

### Step 4: Implement Hybrid Workflow
Create implementation code:

**Python Example (using Tierkreis-like framework):**
```python
from hybrid_framework import DataflowGraph, QuantumNode, ClassicalNode

# Create dataflow graph
graph = DataflowGraph("hybrid_vqe")

# Add quantum node
quantum_op = QuantumNode(
    operation="variational_circuit",
    provider="ibm_quantum",
    backend="simulator",
    shots=1000
)
graph.add_node("quantum", quantum_op)

# Add classical nodes
prep_op = ClassicalNode(operation="prepare_params")
optimize_op = ClassicalNode(operation="gradient_descent")
graph.add_node("prep", prep_op)
graph.add_node("optimize", optimize_op)

# Add edges (data flow)
graph.add_edge("prep", "quantum", data_type="params")
graph.add_edge("quantum", "optimize", data_type="measurement")
graph.add_edge("optimize", "quantum", data_type="new_params")

# Execute with automatic parallelism
result = graph.execute(
    async=True,
    parallel=True,
    iterations=100
)
```

### Step 5: Optimize Parallelism and Asynchronicity
Apply automatic optimization:

**Optimization Strategies:**
1. **Parallel Execution**: Run independent nodes simultaneously
2. **Asynchronous Calls**: Non-blocking quantum cloud requests
3. **Batching**: Group quantum operations for efficiency
4. **Caching**: Store intermediate results to reduce re-computation

**Optimization Analysis:**
```python
# Analyze dataflow graph for parallelism
def analyze_parallelism(graph):
    """Find nodes that can run in parallel."""
    parallel_groups = []
    
    # Group nodes by dependency depth
    for depth in range(graph.max_depth):
        nodes_at_depth = graph.get_nodes_at_depth(depth)
        if len(nodes_at_depth) > 1:
            parallel_groups.append(nodes_at_depth)
    
    return parallel_groups

# Estimate parallel speedup
def estimate_speedup(graph):
    """Calculate theoretical speedup from parallelism."""
    sequential_time = sum(node.time for node in graph.nodes)
    parallel_time = max(sum(node.time for node in group) 
                       for group in parallel_groups)
    return sequential_time / parallel_time
```

### Step 6: Generate Workflow Specification
Create comprehensive design document:

```markdown
# Hybrid Quantum-Classical Workflow Design

## Architecture
- **Type**: Dataflow graph-based
- **Quantum**: [Provider] / [Backend]
- **Classical**: [Cloud service]
- **Integration**: [Framework]

## Dataflow Graph
- **Nodes**: [Number] quantum + [Number] classical
- **Edges**: [Number] data dependencies
- **Depth**: [Max depth]
- **Parallel groups**: [Number]

## Quantum Operations
- **Circuit**: [Description]
- **Qubits**: [Number]
- **Gates**: [Sequence]
- **Measurements**: [Type]

## Classical Processing
- **Preprocessing**: [Description]
- **Optimization**: [Algorithm]
- **Postprocessing**: [Description]

## Performance
- **Parallel speedup**: [Factor]
- **Estimated runtime**: [Duration]
- **Iterations**: [Number]

## Configuration
```yaml
[Configuration template from Step 3]
```

## References
- arXiv:2211.02350 (Tierkreis: Hybrid Quantum-Classical Framework)
```

## Error Handling

### Quantum Cloud Connection Timeout
```
Error: Quantum cloud request timeout.

Solution:
1. Retry with exponential backoff
2. Use asynchronous calls to avoid blocking
3. Switch to simulator for testing
4. Check network connectivity to quantum provider
```

### Classical-Quantum Data Mismatch
```
Error: Data format incompatible between classical and quantum nodes.

Solution:
1. Verify data encoding for quantum operations
2. Add conversion nodes in dataflow graph
3. Use standard quantum data formats (QASM, Qobj)
4. Implement data validation at node boundaries
```

### Insufficient Quantum Resources
```
Error: Quantum backend has insufficient qubits or gate fidelity.

Solution:
1. Reduce quantum circuit complexity
2. Use error mitigation techniques
3. Switch to different backend with more resources
4. Implement circuit optimization (gate reduction)
```

### Parallelism Bottleneck
```
Error: Sequential dependencies prevent parallelization.

Solution:
1. Analyze dataflow graph for bottleneck nodes
2. Refactor to break dependency chains
3. Add caching nodes for intermediate results
4. Use speculative execution where possible
```

## Examples

### Example 1: Variational Quantum Eigensolver (VQE)

```
User: "设计一个混合VQE算法"

Agent:
1. 识别需求: 量子电路 + 参数优化 + 云执行
2. 设计数据流图:
   - Quantum: variational_circuit
   - Classical: gradient_descent
   - Edges: params → circuit → measurement → optimization
3. 配置量子云: IBM Quantum simulator
4. 实现混合工作流: 迭代100次，自动并行
5. 优化并行性: 测量和优化可并行
6. 生成设计文档
```

### Example 2: Quantum Machine Learning Pipeline

```
User: "创建量子机器学习的数据流框架"

Agent:
1. 分析需求: 数据准备 + 量子编码 + 经典训练
2. 设计数据流:
   - Classical: data_prep, encoding, training
   - Quantum: quantum_feature_map, quantum_kernel
   - Integration: sklearn + quantum circuits
3. 配置服务: AWS Braket + S3 storage
4. 实现: 长运行算法，异步调用
5. 优化: 批量量子操作
```

### Example 3: Distributed Quantum Error Correction

```
User: "设计分布式量子纠错工作流"

Agent:
1. 分析需求: 多个量子节点 + 经典纠错算法
2. 设计数据流:
   - Quantum: syndrome_measurement (multiple nodes)
   - Classical: error_correction_decoder
   - Graph: star topology with central decoder
3. 配置: 多backend (IonQ + Honeywell)
4. 实现: 并行 syndrome 提取
5. 优化: 快速纠错响应
```

## Framework Reference

### Tierkreis Framework Components
- **Graph Representation**: Higher-order dataflow
- **Runtime**: Distributed execution engine
- **Composability**: Modular algorithm design
- **Async**: Non-blocking quantum operations

### Quantum Cloud Providers API

| Provider | Python Library | Key Features |
|----------|---------------|--------------|
| IBM | qiskit-ibm-provider | Circuit-based, simulators |
| AWS | braket-sdk | Multiple hardware backends |
| Azure | azure-quantum | IonQ, Honeywell integration |
| Google | cirq | Gate-based NISQ |

### Classical Cloud Services

| Service | Use Case | Integration |
|---------|----------|-------------|
| AWS Lambda | Stateless compute | Event-driven dataflow |
| AWS S3 | Data storage | Intermediate results |
| Google Cloud Functions | Lightweight compute | Node execution |
| Azure Functions | Compute nodes | Hybrid orchestration |

## Resources

### Key Paper
- **arXiv:2211.02350** - Tierkreis: A Dataflow Framework for Hybrid Quantum-Classical Computing

### Quantum Cloud Documentation
- IBM Quantum: https://quantum-computing.ibm.com/
- AWS Braket: https://aws.amazon.com/braket/
- Azure Quantum: https://azure.microsoft.com/en-us/products/quantum/

### Related Libraries
- **Qiskit**: IBM Quantum SDK
- **Braket SDK**: AWS Quantum SDK
- **Cirq**: Google Quantum SDK
- **OpenQASM**: Quantum assembly language

## Related Skills

- **quantum-computing**: General quantum circuit design
- **quantum-error-correction**: Quantum error mitigation
- **variational-quantum-algorithms**: VQE, QAOA design
- **quantum-machine-learning**: QML algorithms
- **cloud-computing**: Cloud service integration
- **distributed-systems**: Distributed architecture design

## Limitations

- Requires access to quantum cloud services (API keys)
- Quantum hardware availability varies by provider
- Network latency affects hybrid workflow performance
- Error rates on real quantum hardware impact results
- Cost considerations for quantum cloud usage

## Notes

- Focus on dataflow graph representation for algorithm design
- Automatic parallelism reduces manual optimization burden
- Asynchronous execution essential for remote quantum access
- Cloud integration enables hybrid workflows without local quantum hardware
- Long-running algorithms require robust error handling and retry logic
---
name: quantum-neural-network-data-loading
description: "Efficient data loading paradigm for Quantum Neural Networks using Shot-Based Quantum Encoding (SBQE). Distribute shots according to data-dependent classical distribution. Use when implementing QNN, quantum data loading, or quantum machine learning."
---

# Quantum Neural Network Data Loading

Shot-Based Quantum Encoding (SBQE) - efficient data loading for quantum neural networks.

## Core Innovation

Traditional encoding schemes (angle, amplitude, basis) either:
- Underuse Hilbert space capacity
- Require circuit depths exceeding coherence budgets

SBQE treats **shots** as learnable parameters, distributing hardware's native resource according to data-dependent classical distribution.

## Key Principles

### 1. Shot Distribution as Encoding
```
Classical data → Shot count distribution over multiple initial states
Creates mixed-state representation
Expectation values are linear in classical probabilities
```

### 2. Structural Equivalence to MLP
```
SBQE ≈ Multilayer Perceptron
- Weights realized by quantum circuits
- Shots serve as learnable input encoding
- No data-encoding gates needed
```

### 3. Implementation Protocol
```python
# SBQE workflow

1. Prepare multiple initial quantum states |ψ_k⟩

2. Allocate shots according to data distribution:
   shots_k = f(data_point, learnable_parameters)

3. Run quantum circuit on each |ψ_k⟩

4. Aggregate expectation values:
   ⟨O⟩ = Σ_k (shots_k / total_shots) * ⟨O⟩_k

5. Compose with non-linear activation functions

6. Backpropagate through shot distribution parameters
```

## Performance Results

### Fashion MNIST
- Test accuracy: 80.95% ± 0.10%
- Exceeds amplitude encoding by +2.0%
- Exceeds linear MLP by +1.3%

### Semeion Handwritten Digits
- Test accuracy: 89.1% ± 0.9%
- Error reduction: 5.3% relative to amplitude encoding
- Matches width-matched classical network

## Advantages

### 1. No Encoding Gates
- Eliminates costly data-encoding circuits
- Uses hardware's native shot resource
- Simpler circuit architecture

### 2. Coherence-Friendly
- Shallow circuits within coherence budgets
- No deep amplitude encoding circuits
- Suitable for NISQ hardware

### 3. Learnable Encoding
- Shots as trainable parameters
- Adaptive to data distribution
- End-to-end optimization

### 4. Linear Expectation Values
- Enables composition with non-linear activation
- Compatible with classical backpropagation
- Hybrid quantum-classical architecture

## References

### Key Paper
- "Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks" (arxiv 2604.06135)
- Authors: Basil Kyriacou, Viktoria Patapovich, et al.

### Related Concepts
- Angle encoding: rotation gates for data
- Amplitude encoding: state vector preparation
- Basis encoding: binary encoding in computational basis

## Activation Keywords
- quantum neural network data loading
- shot-based quantum encoding
- SBQE quantum machine learning
- quantum data encoding
- QNN data loading
- quantum MLP
- 量子神经网络数据加载
- shot 编码量子

## Tools Used
- exec: Run quantum circuit simulations
- read: Load reference papers and datasets
- write: Create QNN architectures and analysis
- memory: Store encoding patterns

## Usage Patterns

### Pattern 1: Implement SBQE for Classification
```
用 SBQE 实现量子分类器
数据加载使用 shot-based encoding
```

### Pattern 2: Compare Encoding Schemes
```
比较 angle/amplitude/basis/SBQE 编码
分析不同编码的准确率和电路深度
```

### Pattern 3: Design QNN Architecture
```
设计量子神经网络架构
使用 SBQE 作为数据加载层
```

## Instructions for Agents

### Step 1: Prepare Initial States
- Define set of initial quantum states |ψ_k⟩
- Number of states: typically 10-20 for good accuracy
- States should be diverse for better representation

### Step 2: Design Shot Distribution Function
```python
def shot_distribution(data_point, parameters):
    """
    Learnable function that maps data to shot counts.
    
    Args:
        data_point: Classical data (e.g., image pixel values)
        parameters: Learnable parameters (weights, biases)
    
    Returns:
        shot_counts: Distribution over initial states
    """
    # Example: linear + softmax
    scores = parameters @ data_point
    shot_counts = softmax(scores) * total_shots
    return shot_counts
```

### Step 3: Execute Quantum Circuits
- Run quantum circuit on each initial state
- Collect expectation values ⟨O⟩_k
- Number of shots: shot_counts_k

### Step 4: Aggregate Results
```python
def aggregate_expectation(shot_counts, expectations):
    """
    Weighted average of expectation values.
    
    Args:
        shot_counts: Distribution over states
        expectations: ⟨O⟩ values from each circuit
    
    Returns:
        final_expectation: Mixed-state expectation
    """
    weights = shot_counts / sum(shot_counts)
    return sum(weights * expectations)
```

### Step 5: Apply Non-Linear Activation
- Classical non-linear function after expectation
- Enables learning non-linear patterns
- Compatible with gradient descent

### Step 6: Optimize Parameters
- Backpropagate through shot distribution
- Update quantum circuit parameters
- Iterate until convergence

## Error Handling

### Shot Budget Constraints
- Total shots limited by hardware
- Balance shot distribution vs accuracy
- Use softmax normalization

### Circuit Depth Limitations
- Keep circuits shallow (< coherence time)
- Avoid deep amplitude encoding
- Use hardware-efficient gates

### Initial State Selection
- Need diverse states for good representation
- Avoid redundant states
- Consider data-dependent initialization

## Examples

### Example 1: Image Classification with SBQE
```
User: "用 SBQE 实现图像分类"

Agent:
1. 加载 Fashion MNIST 数据集
2. 准备 10 个初始量子态
3. 设计 shot 分布函数 (线性 + softmax)
4. 运行量子电路收集期望值
5. 应用 ReLU 激活函数
6. 训练并测试
7. 输出准确率: 80.95%
```

### Example 2: QNN Architecture Design
```
User: "设计量子神经网络架构"

Agent:
1. 数据加载层: SBQE (shot encoding)
2. 量子处理层: shallow circuit (< 20 gates)
3. 经典后处理层: non-linear activation + MLP
4. 输出层: softmax for classification
5. 训练: hybrid gradient descent
```

## Comparison Table

| Encoding Scheme | Circuit Depth | Coherence Budget | Accuracy | Encoding Gates |
|-----------------|---------------|------------------|----------|----------------|
| Angle | Medium | Moderate | 78% | Yes (rotation) |
| Amplitude | Deep | Exceeds | 78% | Yes (state prep) |
| Basis | Shallow | Safe | 75% | Yes (binary) |
| SBQE | Shallow | Safe | 80%+ | **No** |

## Related Skills

- **quantum-error-correction-gauge-theory**: Quantum computing reliability
- **large-model-training-system**: System engineering for AI
- **arxiv-search**: Find QNN papers

## Limitations

- Requires multiple circuit executions (shots)
- Shot budget limits representation capacity
- Hardware-dependent shot noise
- Need diverse initial states for accuracy

## Notes

- SBQE is novel: shots as learnable parameters
- Structural equivalence to MLP enables classical optimization
- No encoding gates is key advantage for NISQ
- Achieves competitive accuracy without deep circuits
- End-to-end training via shot distribution parameters
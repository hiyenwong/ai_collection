---
name: quantum-neural-network-designer
description: "Design and optimize quantum neural network architectures based on Lie algebra truncation and parameterized quantum circuit theory. Use when working with quantum machine learning tasks: (1) Designing QNN architectures for classification/regression, (2) Analyzing trainability and barren plateaus, (3) Optimizing quantum circuit expressivity, (4) Evaluating noise robustness of QNNs. Keywords: quantum neural network, QNN design, quantum circuit, parameterized quantum circuit, LieTrunc-QNN, barren plateau, quantum expressivity, quantum machine learning."
---

# Quantum Neural Network Designer

Design and optimize quantum neural networks (QNNs) using the LieTrunc-QNN theoretical framework.

## Core Concepts

### LieTrunc-QNN Framework
Based on the theory that parameterized quantum circuits can be modeled as Lie subalgebras of u(2^n):
- **Lie algebra truncation**: Reduce circuit complexity while preserving expressivity
- **Quantum expressivity phase transition**: Transition from LiePrune to stable QNNs
- **Barren plateau avoidance**: Design circuits with trainable gradients
- **Noise robustness**: Evaluate circuit stability under decoherence

### Key Components

1. **Lie Algebra Structure**: Quantum circuits generate Lie subalgebras that determine expressivity
2. **Parameterized Circuit Design**: Gate sequences and parameterization strategy
3. **Trainability Analysis**: Gradient variance and optimization landscape
4. **Expressivity Metrics**: Quantum state coverage and circuit power

## Tools Used

- `exec`: Run Python quantum simulation scripts (Qiskit, PennyLane, Cirq)
- `read`: Load circuit specifications and configuration files
- `write`: Save QNN designs, analysis results, and optimization logs

## Usage Patterns

### Pattern 1: QNN Architecture Design

**Request**: "设计一个用于图像分类的量子神经网络"

**Workflow**:
1. Determine qubit requirements from data dimensionality
2. Select encoding strategy (amplitude, angle, basis)
3. Design parameterized circuit with appropriate depth
4. Analyze Lie algebra structure and expressivity
5. Check for barren plateau risk
6. Provide training recommendations

### Pattern 2: Trainability Analysis

**Request**: "分析这个量子电路的可训练性"

**Workflow**:
1. Parse circuit gate sequence
2. Compute Lie algebra generators
3. Calculate gradient variance bounds
4. Detect barren plateau conditions
5. Provide circuit modification suggestions

### Pattern 3: Expressivity Optimization

**Request**: "优化这个量子神经网络的表达能力"

**Workflow**:
1. Analyze current circuit Lie algebra rank
2. Identify under-expressive regions
3. Propose gate additions for better coverage
4. Balance expressivity vs. trainability
5. Validate noise robustness

## Instructions for Agents

### Step 1: Understand Task Requirements

Identify the task type:
- **Classification**: Supervised learning with labels
- **Regression**: Continuous output prediction
- **Generative**: Quantum state generation
- **Optimization**: Variational quantum eigensolver (VQE)

Ask user for:
- Input data dimensionality
- Number of output classes/features
- Available qubits
- Noise model (ideal/simulator/real hardware)

### Step 2: Design Circuit Architecture

Select encoding strategy:
- **Amplitude encoding**: For high-dimensional data (n qubits encode 2^n features)
- **Angle encoding**: For moderate dimensions (each qubit encodes 1-3 features)
- **Basis encoding**: For discrete/classical data

Design variational layers:
- **Hardware-efficient ansatz**: Rotation + entanglement layers
- **Strongly entangling layers**: Multi-parameter rotations with CNOTs
- **Problem-inspired ansatz**: Task-specific gate sequences

Follow guidelines in `references/circuit_patterns.md` for detailed patterns.

### Step 3: Analyze Lie Algebra Structure

Run Lie algebra analysis:
```bash
python3 scripts/analyze_lie_algebra.py --circuit circuit_spec.json
```

Output:
- Lie algebra rank
- Generator set
- Expressivity metric
- Barren plateau risk level

See `references/lie_algebra_theory.md` for theoretical background.

### Step 4: Optimize for Trainability

Check trainability conditions:
1. **Gradient variance**: Should not decay exponentially with circuit depth
2. **Lie algebra rank**: Higher rank → more trainable (but more complex)
3. **Local cost functions**: Prefer local measurements over global

If barren plateau detected:
- Reduce circuit depth
- Use local cost functions
- Add problem-specific structure
- Consider layer-wise training

### Step 5: Validate Noise Robustness

Assess noise impact:
- Depolarizing noise tolerance
- Coherence time requirements
- Gate error accumulation

See `scripts/noise_analysis.py` for simulation.

### Step 6: Generate Design Report

Create comprehensive report:
```markdown
## QNN Architecture Report

### Circuit Specification
- Qubits: N
- Depth: D layers
- Gates: [gate list]
- Parameters: P trainable parameters

### Lie Algebra Analysis
- Rank: R
- Expressivity: E (scale 0-1)
- Trainability: Good/Moderate/Risk

### Training Recommendations
- Optimizer: [Adam/SPSA/etc.]
- Learning rate: [range]
- Batch size: [recommendation]
- Expected convergence: [epochs]

### Noise Analysis
- Robustness level: [High/Medium/Low]
- Hardware requirements: [T1/T2 thresholds]
```

## Error Handling

### Insufficient Qubits
If task requires more qubits than available:
```
建议方案:
1. 使用 amplitude encoding 压缩数据
2. 分层处理高维数据
3. 使用量子嵌入降低维度
```

### Barren Plateau Detected
If circuit exhibits barren plateau:
```
解决方案:
1. 减少电路深度至 D layers
2. 使用局部损失函数
3. 采用 layer-wise 训练策略
4. 添加问题特定结构约束
```

### Noise Degradation
If noise significantly affects performance:
```
建议:
1. 使用错误缓解技术 (zero-noise extrapolation)
2. 增加电路深度容错 margin
3. 选择鲁棒性更高的门序列
4. 考虑噪声自适应训练
```

## Examples

### Example 1: Binary Classification QNN

**User**: "设计一个用于 8 维数据二分类的量子神经网络"

**Agent**:
1. 计算量子比特需求: 8 维 → 3 qubits (amplitude) 或 8 qubits (angle)
2. 选择 angle encoding (更简单): 8 qubits with RX rotations
3. 设计 2 层 variational circuit:
   - Layer 1: RX-RZ on each qubit + CNOT ring
   - Layer 2: RX-RY-RZ + CZ entanglement
4. 分析 Lie algebra: Rank 32, Expressivity 0.75, Trainable
5. 建议: Adam optimizer, lr=0.01, 100 epochs

### Example 2: Barren Plateau Analysis

**User**: "分析这个深度量子电路是否会有 barren plateau"

**Agent**:
```bash
python3 scripts/detect_barren_plateau.py --depth 20 --qubits 8
```

Output:
```
Barren Plateau Analysis:
- Depth: 20 layers
- Gradient variance: ~10^-8 (exponential decay detected)
- Risk Level: HIGH

Recommendations:
- Reduce depth to 5-10 layers
- Use local cost function
- Add problem structure
```

## References

- **LieTrunc-QNN Paper**: arxiv 2604.02697v1 - "LieTrunc-QNN: Lie Algebra Truncation and Quantum Expressivity Phase Transition"
- **Quantum Machine Learning**: See `references/qml_overview.md`
- **Circuit Patterns**: See `references/circuit_patterns.md`
- **Lie Algebra Theory**: See `references/lie_algebra_theory.md`

## Related Skills

- **quantum-circuit-simulator**: Simulate quantum circuits
- **quantum-optimizer**: Quantum optimization algorithms
- **machine-learning-designer**: Classical ML architecture design

## Notes

- This skill focuses on variational quantum circuits for ML tasks
- Requires quantum computing library (Qiskit/PennyLane/Cirq)
- Lie algebra analysis is computationally intensive for large circuits
- Always validate designs with simulation before hardware deployment

## Activation Keywords
- [skill-specific keyword]
- [related search term]
- [use case description]

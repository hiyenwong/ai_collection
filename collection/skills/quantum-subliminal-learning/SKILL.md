---
name: quantum-subliminal-learning
description: "Security analysis framework for detecting hidden behavioral traits in quantum machine learning models. Identifies subliminal learning through auxiliary-channel and task-channel distillation pathways with geometric analysis of teacher drift visibility."
tags: [quantum, security, machine-learning, subliminal, model-supply-chain]
---

# Quantum Subliminal Learning

## Description

Security analysis framework for detecting and understanding hidden behavioral traits inherited by quantum machine learning models through innocuous public interfaces. Studies two distillation pathways — auxiliary-channel on random inputs and restricted task-channel where student matches public supervised output while hidden behavior resides on a disjoint task. Identifies that QNNs retain most hidden-task signal while classical NNs transmit little, controlled by teacher drift magnitude and fraction of hidden-task-relevant drift visible through public interface.

Based on: *Quantum Subliminal Learning* (arXiv: 2605.29557)

## Activation Keywords

- quantum subliminal learning
- QNN security analysis
- quantum model distillation
- hidden behavior quantum
- quantum supply chain security
- subliminal quantum ML
- quantum model supply chain

## Tools Used

- terminal: Run quantum circuit simulations and security analysis
- read_file: Load model weights and analysis scripts
- write_file: Save security audit reports
- web_search: Find quantum model benchmarks and datasets

## Usage Patterns

### Pattern 1: Auxiliary-Channel Subliminal Detection

```python
# Both classical and quantum neural networks exhibit efficient
# auxiliary-channel subliminal learning via random input probing
def detect_auxiliary_subliminal(teacher_model, student_model, n_samples=1000):
    random_inputs = np.random.randn(n_samples, teacher_model.input_dim)
    teacher_outputs = teacher_model(random_inputs)
    student_outputs = student_model(random_inputs)
    # High correlation indicates subliminal information transfer
    return compute_correlation(teacher_outputs, student_outputs)
```

### Pattern 2: Task-Channel Architecture Dependence Analysis

```python
# Classical NNs transmit little hidden-task info through public-task interface
# QNNs retain most hidden-task signal - architecture-dependent behavior
def analyze_task_channel(teacher, student, public_task, hidden_task):
    # Train student on public task only
    student.fit(public_task.train_X, public_task.train_y)
    
    # Evaluate on hidden task (student should NOT know this)
    hidden_performance = student.score(hidden_task.test_X, hidden_task.test_y)
    
    # High performance = subliminal leakage
    return hidden_performance
```

### Pattern 3: Teacher Drift Geometric Analysis

```python
# Unified geometric picture: transmission controlled by
# (1) teacher drift magnitude, (2) fraction of hidden-task-relevant
# drift visible through public interface
def analyze_drift_visibility(teacher_params, public_interface, hidden_task_grads):
    drift = compute_parameter_drift(teacher_params)
    drift_magnitude = np.linalg.norm(drift)
    visible_fraction = project_onto_public_space(drift, public_interface)
    hidden_relevant = dot_product(visible_fraction, hidden_task_grads)
    return drift_magnitude, hidden_relevant
```

## Instructions for Agents

### Step 1: Define Distillation Setup

1. Identify teacher model (pre-trained QNN or classical NN)
2. Define public task (what student is supposed to learn)
3. Define hidden task (behavior that should NOT transfer)
4. Ensure public and hidden tasks use disjoint input/output spaces

### Step 2: Auxiliary-Channel Analysis

1. Generate random inputs across the model's input domain
2. Query both teacher and student with these random inputs
3. Compute correlation/coherence between outputs
4. High correlation on random inputs indicates subliminal learning channel

### Step 3: Task-Channel Analysis

1. Train student model exclusively on public task data
2. Evaluate student performance on hidden task (should be at chance)
3. If student performs above chance on hidden task, subliminal learning occurred
4. Compare QNN vs. classical NN: QNNs show stronger hidden-task signal retention

### Step 4: Geometric Drift Analysis

1. Compute parameter drift during teacher training
2. Project drift onto the public interface subspace
3. Measure fraction of drift that is relevant to hidden task
4. Use unified geometric model to predict transmission strength:
   - Transmission ∝ (drift magnitude) × (visible hidden-relevant fraction)

### Step 5: Security Assessment

1. Document all identified subliminal channels
2. Quantify information leakage for each channel
3. Assess severity: what hidden behaviors could be inherited?
4. Recommend mitigations:
   - Add noise to public outputs to reduce drift visibility
   - Use different architectures for teacher/student
   - Implement formal verification of student behavior on hidden tasks

## Error Handling

### No Clear Separation Between Public and Hidden Tasks
```
If tasks overlap in feature space:
  1. Redefine task boundaries to ensure orthogonality
  2. Use task-specific feature extractors
  3. Apply domain adaptation to separate task representations
```

### False Positive on Random Input Correlation
```
If high correlation on random inputs is expected (same architecture):
  1. Use shuffled/permuted teacher outputs as baseline
  2. Compare against random student model baseline
  3. Focus on task-channel analysis as primary indicator
```

## Best Practices

1. **Always test both channels**: Auxiliary and task-channel reveal different vulnerability patterns
2. **Compare quantum vs. classical**: QNNs show architecture-dependent behavior that differs fundamentally from classical NNs
3. **Use geometric analysis**: The unified geometric picture provides actionable insight into why and how subliminal learning occurs
4. **Test across architectures**: Subliminal learning severity varies with model architecture, not just task definition
5. **Document supply chain risks**: Hidden behavior inheritance is a concrete security concern for quantum model supply chains

## Limitations

- Analysis assumes access to both teacher and student model parameters/outputs
- Does not cover all possible distillation pathways (e.g., gradient-based, feature-based)
- Geometric analysis provides necessary but not sufficient conditions for subliminal learning
- Limited to supervised learning scenarios; unsupervised/RL settings need separate analysis

## Resources

- **Paper**: arXiv:2605.29557 - "Quantum Subliminal Learning"
- **Authors**: Shi-Xin Zhang, Yu-Qin Chen

## Related Skills

- quantum-ml-patterns: Reusable QML research patterns
- quantum-ml-robustness: QML model testing and robustness
- post-quantum-cryptographic-protocol-analysis: Security analysis patterns

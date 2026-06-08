---
name: quantum-fisher-view-ml
description: "QUIVER methodology — enriching classical ML features with quantum Fisher information views from variational quantum circuits. Combines quantum geometry with classical ML for enhanced representations without fault-tolerant hardware. Also covers Hamming quantum kernel for scalable quantum SVMs. arXiv: 2606.02785, 2605.31449"
tags: ["quantum-ml", "fisher-information", "variational-quantum-circuit", "feature-augmentation", "quantum-kernel", "svm"]
---

# Quantum Fisher View for ML (QUIVER)

## Background

Large machine learning models benefit from multimodal inputs providing complementary views. QUIVER (QUantum-Informed Views for Enhanced Representations) enriches classical data-driven features with a **quantum Fisher view** — a geometrically motivated, basis-independent summary of higher-order correlations captured by a variational quantum circuit (VQC) trained on the same task.

The **quantum Fisher information matrix (QFIM)** encodes the intrinsic geometry of the learned quantum state manifold, surfacing statistical structure that additional classical data or model capacity finds difficult to learn. This makes the quantum Fisher view a genuinely complementary modality, not a redundant one.

Additionally, the **Hamming quantum kernel** provides a scalable approach for quantum SVMs by using full measurement statistics instead of a single fidelity value, avoiding the exponential concentration problem at larger qubit scales (15+ qubits).

## Core Methodology

### QUIVER Pipeline

1. **Train VQC**: Train a variational quantum circuit on the target task (classification/regression)
2. **Extract QFIM**: Compute the quantum Fisher information matrix from the trained VQC's state manifold
3. **Compute Fisher View**: Derive a basis-independent feature vector from the QFIM eigenstructure
4. **Fuse with Classical**: Concatenate or project the quantum Fisher view with classical features
5. **Train Final Model**: Train the downstream model on the augmented feature space

### Hamming Quantum Kernel Pipeline

1. **Prepare Quantum Circuit**: Design a feature map circuit embedding classical data into quantum states
2. **Execute Measurements**: Run the circuit and collect full measurement outcome statistics (bitstring frequencies)
3. **Compute Hamming Kernel**: Calculate pairwise Hamming distances between measurement outcome distributions
4. **Train SVM**: Use the Hamming kernel matrix as input to a classical SVM solver

## Implementation Steps

### Step 1: VQC Training for QUIVER

```python
import pennylane as qml
import numpy as np
from jax import numpy as jnp

n_qubits = 4
n_layers = 2

def vqc_circuit(params, x):
    """Variational quantum circuit with data encoding."""
    for i in range(n_qubits):
        qml.RY(x[i], wires=i)
    
    for layer in range(n_layers):
        for i in range(n_qubits):
            qml.Rot(*params[layer, i], wires=i)
        for i in range(n_qubits - 1):
            qml.CNOT(wires=[i, i + 1])
    
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

dev = qml.device("default.qubit", wires=n_qubits)
qnode = qml.QNode(vqc_circuit, dev)

# Train VQC on target task
# ... standard optimization loop ...
```

### Step 2: Quantum Fisher Information Matrix Extraction

```python
def compute_qfim(params, x, eps=1e-4):
    """Compute QFIM using parameter-shift rule."""
    n_params = params.size
    qfim = np.zeros((n_params, n_params))
    
    for i in range(n_params):
        for j in range(i, n_params):
            # Parameter-shift for second derivatives
            params_pp = params.copy()
            params_pm = params.copy()
            params_mp = params.copy()
            params_mm = params.copy()
            
            params_pp[i] += eps; params_pp[j] += eps
            params_pm[i] += eps; params_pm[j] -= eps
            params_mp[i] -= eps; params_mp[j] += eps
            params_mm[i] -= eps; params_mm[j] -= eps
            
            f_pp = qnode(params_pp, x)
            f_pm = qnode(params_pm, x)
            f_mp = qnode(params_mp, x)
            f_mm = qnode(params_mm, x)
            
            qfim[i, j] = (f_pp - f_pm - f_mp + f_mm) / (4 * eps**2)
            qfim[j, i] = qfim[i, j]
    
    return qfim
```

### Step 3: Fisher View Feature Extraction

```python
def extract_fisher_view(qfim, n_components=4):
    """Extract basis-independent features from QFIM eigenstructure."""
    eigenvalues, eigenvectors = np.linalg.eigh(qfim)
    
    # Sort by magnitude
    idx = np.argsort(np.abs(eigenvalues))[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Fisher view features:
    # 1. Top eigenvalues (curvature of quantum state manifold)
    # 2. Eigenvalue ratios (relative importance of directions)
    # 3. Condition number (sensitivity)
    # 4. Spectral entropy (information content)
    
    top_eigs = eigenvalues[:n_components]
    eigen_ratios = top_eigs / (np.sum(np.abs(eigenvalues)) + 1e-10)
    condition_number = np.abs(eigenvalues[0]) / (np.abs(eigenvalues[-1]) + 1e-10)
    spectral_entropy = -np.sum(eigen_ratios * np.log(eigen_ratios + 1e-10))
    
    fisher_view = np.concatenate([
        top_eigs,
        eigen_ratios,
        [condition_number, spectral_entropy]
    ])
    
    return fisher_view
```

### Step 4: Feature Fusion

```python
def quiver_augment(classical_features, fisher_view):
    """Fuse quantum Fisher view with classical features."""
    # Option 1: Simple concatenation
    augmented = np.concatenate([classical_features, fisher_view])
    
    # Option 2: Weighted fusion with learned weights
    # w_classical, w_quantum = learn_weights(classical_features, fisher_view)
    # augmented = w_classical * classical_features + w_quantum * fisher_view
    
    return augmented
```

### Step 5: Hamming Quantum Kernel

```python
def hamming_quantum_kernel(X_train, X_test, n_qubits, circuit_fn):
    """Compute Hamming quantum kernel from measurement statistics."""
    from scipy.spatial.distance import hamming
    
    # Get measurement distributions for all data points
    def get_measurement_distribution(x, n_shots=1000):
        """Run circuit and collect bitstring frequencies."""
        counts = {}
        for _ in range(n_shots):
            result = circuit_fn(x)  # Returns bitstring
            counts[result] = counts.get(result, 0) + 1
        # Normalize to probability distribution
        total = sum(counts.values())
        return {k: v/total for k, v in counts.items()}
    
    train_dists = [get_measurement_distribution(x) for x in X_train]
    test_dists = [get_measurement_distribution(x) for x in X_test]
    
    # Compute Hamming kernel matrix
    n_train, n_test = len(train_dists), len(test_dists)
    K = np.zeros((n_test, n_train))
    
    for i in range(n_test):
        for j in range(n_train):
            # Hamming distance between measurement distributions
            all_keys = set(train_dists[j].keys()) | set(test_dists[i].keys())
            vec1 = np.array([train_dists[j].get(k, 0) for k in all_keys])
            vec2 = np.array([test_dists[i].get(k, 0) for k in all_keys])
            K[i, j] = np.exp(-hamming(vec1, vec2))
    
    return K
```

## Key Findings from Research

### QUIVER Results (arXiv:2606.02785)
- Demonstrated on QM9 (molecular properties) and JetClass (LHC jet flavor)
- Quantum Fisher view provides genuinely complementary information to classical features
- Works before fault-tolerant quantum hardware (simulated VQCs suffice)
- Domain-agnostic: applicable to any architecture with targeted modifications
- Improves standard performance metrics across very different domains

### Hamming Quantum Kernel Results (arXiv:2605.31449)
- Avoids exponential concentration of fidelity quantum kernel
- Scales to 27 qubits (tested up to this limit)
- Outperforms fidelity kernel at 15+ qubits
- Outperforms classical Gaussian kernel on synthetic quantum data
- Purely classical post-processing — no additional quantum resources

## When to Use

### Use QUIVER when:
- You need to extract higher-order statistical correlations from data
- Classical feature augmentation is insufficient
- You have access to quantum simulators or hardware
- Working on molecular/physics ML tasks
- You need basis-independent feature representations

### Use Hamming Quantum Kernel when:
- Building quantum SVMs with 15+ qubits
- Fidelity quantum kernel suffers from exponential concentration
- You need scalable quantum kernel methods
- Working with synthetic or quantum-native data

## Pitfalls

1. **QFIM computation cost**: Computing the full QFIM scales as O(n_params²) — use sampling or approximation for large circuits
2. **VQC trainability**: Barren plateaus can make VQC training difficult — use local cost functions or layer-by-layer training
3. **Shot noise**: Finite measurement shots introduce noise in QFIM estimation — use enough shots (>1000) or error mitigation
4. **Exponential concentration**: Traditional fidelity kernels concentrate exponentially — always prefer Hamming kernel at scale
5. **Classical simulability**: For small circuits, classical methods may match performance — quantum advantage emerges at larger scales

## Activation Keywords
- quantum fisher view
- quiver ml
- quantum feature augmentation
- quantum Fisher information matrix
- QFIM features
- hamming quantum kernel
- quantum SVM
- scalable quantum kernel
- 量子费舍尔信息
- 量子核方法

## Related Skills
- quantum-ml-patterns
- quantum-neural-architecture
- quantum-framework-agnostic-design
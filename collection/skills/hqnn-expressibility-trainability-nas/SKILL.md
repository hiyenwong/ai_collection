# HQNN Expressibility-Trainability NAS

## Description
Multi-objective neural architecture search (NAS) framework for hybrid quantum neural networks that jointly optimizes expressibility, trainability, and task performance across a combined classical-quantum design space. Reveals how classical components reshape optimization landscape, decoupling trainability from PQC expressibility.

## Source
Paper: "Rethinking Expressibility-Trainability Trade-off in Hybrid Quantum Neural Networks"
Authors: Muhammad Kashif, Muhammad Shafique
arXiv: 2605.25768

## Activation
arxiv:2605.25768, hybrid quantum neural network, expressibility-trainability trade-off, neural architecture search, barren plateaus, HQNN, PQC, quantum-classical hybrid training

## Usage Scenarios
- Designing hybrid quantum-classical neural architectures
- Analyzing expressibility-trainability trade-offs in PQCs
- Multi-objective optimization of quantum circuit architectures
- Understanding when hybridization eliminates barren plateaus
- Comparing pure PQC vs hybrid training regimes

## Core Patterns

### 1. Expressibility-Trainability Analysis Framework
```python
def analyze_expressibility_trainability(circuit_config, training_mode):
    """Analyze expressibility-trainability relationship under different training modes.
    
    Key findings:
    - Pure PQCs: weak, regime-dependent trade-off
    - Hybrid (quantum-only training): moderate trade-off
    - Hybrid (end-to-end training): trade-off eliminated
    
    Classical components reshape the optimization landscape.
    """
    expressibility = compute_expressibility(circuit_config)
    trainability = compute_gradient_variance(circuit_config)
    
    if training_mode == 'pure_pqc':
        trade_off = compute_tradeoff(expressibility, trainability)
    elif training_mode == 'hybrid_quantum_only':
        trade_off = compute_tradeoff(expressibility, trainability) * 0.7
    elif training_mode == 'hybrid_end_to_end':
        trade_off = 0  # Classical components decouple the relationship
    
    return {
        'expressibility': expressibility,
        'trainability': trainability,
        'trade_off_strength': trade_off,
        'training_mode': training_mode
    }
```

### 2. Multi-Objective NAS for HQNN
```python
def nas_hqnn_design_space(search_config):
    """Neural architecture search across combined classical-quantum design space.
    
    Search dimensions:
    - Circuit depth (quantum)
    - Qubit count (quantum)
    - Entanglement topology (quantum)
    - Classical layer sizes (classical)
    - Classical activation functions (classical)
    
    Returns Pareto-optimal solutions for different training regimes.
    """
    objectives = ['expressibility', 'trainability', 'task_performance']
    pareto_fronts = {
        'quantum_only': [],  # Pareto front for quantum-only training
        'end_to_end': []     # Pareto front for full hybrid training
    }
    
    for config in enumerate_design_space(search_config):
        # Evaluate all objectives
        scores = evaluate_config(config)
        
        # Update Pareto fronts
        for regime in ['quantum_only', 'end_to_end']:
            pareto_fronts[regime] = update_pareto_front(
                pareto_fronts[regime], scores[regime]
            )
    
    return pareto_fronts
```

### 3. Training Configuration Comparison
```python
def compare_training_configurations(problem_instance):
    """Compare different training configurations on same problem.
    
    Configurations to test:
    1. Pure PQC (quantum-only model)
    2. Hybrid with quantum-only training (classical layers frozen)
    3. Hybrid with end-to-end training (all layers trainable)
    """
    results = {}
    for config in ['pure_pqc', 'hybrid_quantum_only', 'hybrid_end_to_end']:
        model = build_hqnn(problem_instance, config)
        metrics = train_and_evaluate(model, config)
        results[config] = {
            'final_loss': metrics['loss'],
            'gradient_variance': metrics['grad_var'],
            'expressibility': metrics['expressibility'],
            'convergence_speed': metrics['epochs_to_converge'],
            'final_accuracy': metrics['accuracy']
        }
    return results
```

## Implementation Guidelines

### Design Space Dimensions
| Dimension | Range | Impact |
|-----------|-------|--------|
| Circuit depth | 2-20 layers | Affects expressibility and trainability |
| Qubit count | 4-20 qubits | Limits problem encoding capacity |
| Entanglement topology | Linear, circular, all-to-all | Affects SWAP overhead |
| Classical layers | 1-5 layers | Can decouple expressibility-trainability |
| Classical neurons | 32-512 per layer | Affects classical expressivity |

### Training Regimes
1. **Pure PQC**: Only quantum circuit, no classical layers
2. **Hybrid quantum-only**: Classical layers exist but frozen during training
3. **Hybrid end-to-end**: All parameters (quantum + classical) trained together

### Key Metrics to Track
- **Expressibility**: Hilbert space coverage of the PQC
- **Trainability**: Gradient variance across training steps
- **Barren plateau detection**: Gradient norm < threshold for consecutive steps
- **Convergence speed**: Epochs to reach target loss
- **Task performance**: Final accuracy/loss on validation set

## Pitfalls
- **Expressibility-trainability trade-off is regime-dependent**: The assumed
  trade-off may not hold in hybrid architectures with end-to-end training
- **Classical component impact**: Adding classical layers fundamentally changes
  the optimization landscape, not just implementation detail
- **Hardware constraints**: Expressible circuits may be unexecutable on
  NISQ hardware due to decoherence
- **Search space size**: Combined classical-quantum design space is very
  large; use efficient NAS strategies (e.g., weight sharing, progressive search)

## Verification
1. Reproduce expressibility-trainability analysis across training regimes
2. Run multi-objective NAS on target problem
3. Validate that end-to-end training eliminates trade-off
4. Compare Pareto fronts across training regimes
5. Benchmark against pure classical and pure quantum baselines

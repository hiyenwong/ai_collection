# Quantum-Enhanced RL for Process Synthesis (arXiv: 2605.21213)

**Paper**: Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing  
**Authors**: Austin Braniff, Fengqi You, Yuhe Tian  
**Date**: 2026-05-28

## Methodology

Chemical process synthesis = sequential decision-making problem with large discrete action spaces. Traditional RL struggles with combinatorial complexity of process flowsheet design.

### QUBO-Encoded Policy Search

1. **Encode RL policy decisions into binary variables**: Each policy action mapped to {0,1} encoding
2. **Map policy optimization to QUBO**: `min x^T Q x` where Q encodes process constraints + economic objectives + safety bounds
3. **Solve via quantum annealer**: D-Wave or quantum-inspired classical solver
4. **Decode solution**: Map binary solution back to process design actions

### Key Advantages
- Exponential reduction in search space exploration
- Better global optima vs classical RL alone
- Handles combinatorial complexity of process flowsheet design

### Application Domains
- Chemical process design and optimization
- Plant flowsheet synthesis
- Industrial process optimization with large discrete decision spaces
- Any sequential decision problem with combinatorial action space

### QUBO Formulation Pattern
```
min x^T Q x + c^T x  where x ∈ {0,1}^n

Q encodes:
- Process thermodynamic constraints
- Economic objectives (cost, yield, profit)
- Safety and operational bounds
- RL reward function (discounted return)
```

### Workflow
```
Process Problem → RL State/Action Design → QUBO Formulation → 
Quantum Annealer Solver → Decode Solution → Validate Process Design
```

## Relationship to QUACOD (Pattern 9)

QUACOD decomposes large QUBOs into quantum-solvable subproblems via coordinate descent. This paper takes a different approach: directly encoding the RL policy as a QUBO for quantum annealing. They are complementary:

- **This paper**: RL → QUBO → quantum annealer (direct encoding)
- **QUACOD**: Large QUBO → block decomposition → iterative quantum solve (decomposition)

For very large process synthesis problems (> available qubits), combine both: encode RL policy as QUBO, then apply QUACOD decomposition for solving on limited qubit hardware.

## Activation
- quantum process synthesis, QUBO RL, quantum annealing optimization
- quantum reinforcement learning, chemical process optimization
- sequential decision quantum, RL combinatorial optimization

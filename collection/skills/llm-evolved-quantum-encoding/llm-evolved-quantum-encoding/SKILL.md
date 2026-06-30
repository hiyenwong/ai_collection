---
name: llm-evolved-quantum-encoding
description: "LLM-driven evolutionary framework for quantum error correction code discovery using Structured Concept Evolution (SCE). Pairs LLM reasoning with physics-informed evaluation to autonomously discover new qLDPC code constructions. Activation: quantum code discovery, qLDPC, structured concept evolution, quantum error correction, LLM quantum design, SCE"
---

## Overview

This skill implements the Structured Concept Evolution (SCE) methodology from arXiv:2606.24808 (Liu & Marquardt, 2026) — using LLMs as creative engines for quantum error correction code design, combined with automated physics-based evaluation to filter viable candidates.

## Core Methodology

### 1. Structured Concept Evolution (SCE)

SCE pairs an LLM with a physics evaluation pipeline in an iterative loop:

```
LLM generates code concept → Physics evaluator validates → Feedback loop → New generation
```

**Key components:**
- **LLM Generator**: Proposes quantum LDPC code constructions using structured prompts
- **Physics Evaluator**: Validates codes against QEC criteria (distance, rate, sparsity)
- **Concept Evolution**: Maintains a population of code concepts, applying mutation/crossover operations guided by LLM reasoning
- **Fitness Function**: Combines code parameters (distance, rate, weight) with implementability score

### 2. QLDPC Code Representation

Represent quantum codes as Tanner graphs with:
- Stabilizer generators (rows of parity check matrix H)
- Logical operators (X_L, Z_L)
- Distance estimates via minimum weight codewords

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class QLDPCCode:
    """Quantum LDPC code representation."""
    Hx: np.ndarray  # X-type stabilizers
    Hz: np.ndarray  # Z-type stabilizers
    n: int          # Number of physical qubits
    k: int          # Number of logical qubits
    distance_x: int # X-distance
    distance_z: int # Z-distance
    name: str       # Code identifier
    
    @property
    def rate(self) -> float:
        return self.k / self.n if self.n > 0 else 0
    
    def is_valid(self) -> bool:
        """Check Hx @ Hz.T == 0 (CSS condition)."""
        return np.array_equal(self.Hx @ self.Hz.T % 2, np.zeros_like(self.Hx @ self.Hz.T))
```

### 3. LLM Prompt Structure

```
You are a quantum error correction code designer.

Current best code: {best_code_description}
Target parameters: n={n}, k={k}, max_weight={w}

Generate a new QLDPC code construction by:
1. Describing the parity check matrix structure
2. Explaining the geometric/algebraic intuition
3. Specifying the Tanner graph properties
4. Estimating the code distance

Format:
- Code name: ...
- Construction: ...
- Hx structure: ...
- Hz structure: ...
- Expected parameters: [[n, k, d]]
- Intuition: ...
```

### 4. Evaluation Pipeline

```python
def evaluate_qldpc_code(code_spec: dict) -> dict:
    """Evaluate a proposed QLDPC code."""
    score = 0
    
    # 1. CSS condition check
    if not satisfies_css_condition(code_spec):
        return {"valid": False, "reason": "CSS condition violated"}
    
    # 2. Sparsity check (LDPC requirement)
    row_weight = np.mean(np.sum(code_spec["Hx"], axis=1))
    col_weight = np.mean(np.sum(code_spec["Hx"], axis=0))
    if row_weight > 10 or col_weight > 10:
        return {"valid": False, "reason": "Not sufficiently sparse"}
    
    # 3. Distance estimation
    d_est = estimate_distance(code_spec)
    
    # 4. Rate calculation
    rate = code_spec["k"] / code_spec["n"]
    
    # 5. Composite fitness score
    score = d_est * rate * sparsity_bonus(code_spec)
    
    return {
        "valid": True,
        "distance": d_est,
        "rate": rate,
        "fitness": score,
        "sparsity": (row_weight, col_weight)
    }
```

### 5. Evolution Strategy

```python
def evolve_codes(
    llm_client,
    initial_concepts: list,
    generations: int = 20,
    population_size: int = 10
) -> list:
    """Evolve QLDPC code concepts over generations."""
    population = initial_concepts.copy()
    history = []
    
    for gen in range(generations):
        # Evaluate current population
        scored = [(evaluate_qldpc_code(c), c) for c in population]
        scored.sort(key=lambda x: x[0].get("fitness", 0), reverse=True)
        
        # Keep top performers
        elites = [c for _, c in scored[:2]]
        
        # Generate offspring via LLM
        offspring = []
        for _ in range(population_size - 2):
            parent = scored[np.random.randint(0, len(scored) // 2)][1]
            child = llm_mutate(llm_client, parent, history)
            offspring.append(child)
        
        population = elites + offspring
        history.append(scored[0])
    
    return history
```

## Practical Applications

### Use Cases
1. **Code Discovery**: Finding new qLDPC codes beyond known families (surface codes, toric codes, hypergraph products)
2. **Code Optimization**: Improving distance/rate trade-offs for existing constructions
3. **Hardware-Aware Design**: Tailoring codes to specific quantum hardware connectivity
4. **Educational Tool**: Understanding QEC code design principles through LLM-generated explanations

### Integration Patterns

#### With Quantum Computing Pipelines
```python
# Use discovered codes in QEC simulations
from qiskit_qec import QLDPCDecoder

code = best_evolved_code
decoder = QLDPCDecoder(code.Hx, code.Hz)
# Use decoder in fault-tolerance simulations
```

#### With Hardware Constraints
```python
def hardware_aware_fitness(code, device_graph):
    """Score code by how well it maps to hardware."""
    # Check if Tanner graph embeds in device connectivity
    embedding_cost = compute_embedding_cost(code, device_graph)
    return code.fitness / (1 + embedding_cost)
```

## Pitfalls

1. **LLM Hallucination**: LLMs may propose mathematically invalid codes. Always validate with the physics evaluator.
2. **Distance Estimation**: True code distance is NP-hard to compute. Use bounds or sampling-based estimation.
3. **Population Diversity**: LLMs tend to converge. Use temperature tuning and diverse initial concepts.
4. **Evaluation Cost**: Full distance computation is expensive. Use fast approximations for early filtering.
5. **CSS Condition**: Not all good codes are CSS codes. Consider non-CSS constructions for broader search.

## Verification Steps

1. Verify CSS condition: Hx @ Hz.T mod 2 == 0
2. Verify sparsity: max row/column weight < threshold
3. Estimate distance using syndrome decoding simulation
4. Compare rate against known bounds (quantum Gilbert-Varshamov)
5. Test on noise model via Monte Carlo simulation

## References

- Liu, Z. & Marquardt, F. (2026). "Large-Language-Model Discovery of Quantum LDPC Codes through Structured Concept Evolution." arXiv:2606.24808
- Related: Neural Transfer Unification (NTU) for decoders, arXiv:2606.27119
- Related: Active Quantum Kernel Acquisition, arXiv:2606.28833

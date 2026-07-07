---
name: llm-evolved-quantum-encoding
description: "LLM-driven evolutionary program synthesis for quantum error-correcting code discovery. Uses language model to mutate constructor programs, external verifier to score results, and iterative search to discover interpretable quantum encoding schemes with improved code distance and resource efficiency."
---

# LLM-Evolved Quantum Encoding

## Description

LLM-driven evolutionary program synthesis methodology for discovering quantum error-correcting encodings. An LLM edits a program (constructor), an external verifier scores the result (checking stabilizer-coset semantics, code distance, resource metrics), and high-scoring programs are retained and re-mutated. Applied to Generalized Superfast Encoding (GSE) and fermion-to-qubit mappings, this approach discovered codes with exact distance 5-6 on molecular instances, surpassing prior distance-3 constructions.

## Activation Keywords
- LLM quantum code search
- evolutionary quantum encoding
- quantum error correction LLM
- GSE encoding search
- fermion-to-qubit encoding discovery
- quantum code distance optimization
- LLM evolutionary synthesis quantum
- verifier-guided quantum search
- 量子纠错码搜索
- LLM演化量子编码

## Tools Used
- exec: Run quantum code verifiers, stabilizer simulations
- write: Create constructor programs, save discovered encodings
- read: Load prior artifacts, verifier results

## Core Methodology

### Phase 1: Define the Search Space

1. **Identify the encoding family**: e.g., Generalized Superfast Encoding (GSE), Jordan-Wigner, Bravyi-Kitaev
2. **Define constructor programs**: Programs that generate the encoding given system parameters (number of modes, interaction graph)
3. **Define verifier semantics**: What constitutes a valid encoding?
   - Stabilizer commutation relations
   - Code distance (minimum weight of logical operators)
   - Resource cost (qubits per mode, gate complexity)

### Phase 2: Evolutionary Loop

```
┌─────────────────────────────────────────────────────────┐
│                   Evolutionary Loop                      │
│                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐       │
│  │  LLM     │───▶│ Constructor│───▶│  Verifier    │       │
│  │ Mutation │    │ Program   │    │  Scoring     │       │
│  └──────────┘    └──────────┘    └──────────────┘       │
│       ▲                              │                  │
│       │         ┌──────────────┐     │                  │
│       └─────────│   Archive    │◀────┘                  │
│                 │ High-scorers │                        │
│                 └──────────────┘                        │
└─────────────────────────────────────────────────────────┘
```

1. **Seed**: Start with a known baseline constructor (e.g., distance-3 GSE)
2. **Mutate**: LLM proposes edits to the constructor program
3. **Verify**: External verifier checks:
   - Stabilizer coset semantics
   - Code distance on test instances
   - Resource efficiency
4. **Retain**: High-scoring programs archived for next generation
5. **Iterate**: Repeat until convergence or budget exhausted

### Phase 3: Multi-Objective Search Strategy

**Key insight from the paper**: Single-objective search fails.

| Objective | Problem | Solution |
|-----------|---------|----------|
| Distance alone | Selects trivial dense graphs | Hold distance fixed, optimize compression |
| Compression alone | Selects invalid encodings | Verify correctness first, then optimize |
| Resource cost alone | May sacrifice distance | Pareto frontier analysis |

**Recommended two-stage approach**:
1. **Stage 1**: Search for maximum verified code distance
2. **Stage 2**: Fix distance constraint, search for minimum resource usage

### Phase 4: Verifier Design

```python
def verify_encoding(constructor_code, test_instances):
    """
    Verify a quantum encoding constructor.
    
    Returns: dict with distance, qubit_count, validity, structure_score
    """
    results = {
        'valid': True,
        'distances': [],
        'qubit_counts': [],
        'structure_metrics': {},
        'verdict': None
    }
    
    for instance in test_instances:
        # 1. Generate encoding from constructor
        encoding = constructor_code.generate(instance)
        
        # 2. Check stabilizer commutation
        if not encoding.check_stabilizer_commutation():
            results['valid'] = False
            results['verdict'] = 'INVALID: Stabilizer violation'
            return results
        
        # 3. Compute code distance
        d = encoding.compute_minimum_weight_logical_operator()
        results['distances'].append(d)
        
        # 4. Count qubits
        results['qubit_counts'].append(encoding.qubit_count)
        
        # 5. Structure analysis (circulant, sparse, etc.)
        results['structure_metrics'] = encoding.analyze_structure()
    
    # Aggregate
    results['min_distance'] = min(results['distances'])
    results['avg_qubits'] = sum(results['qubit_counts']) / len(results['qubit_counts'])
    
    # Scoring: distance is primary, compression is secondary
    if results['min_distance'] >= target_distance:
        results['score'] = results['min_distance'] + 1.0 / results['avg_qubits']
    else:
        results['score'] = results['min_distance']  # Distance priority
    
    results['verdict'] = 'VALID'
    return results
```

### Phase 5: LLM Mutation Prompts

```
Given the current best constructor program:
{current_code}

With verified results:
- Code distance: {distance}
- Qubits per mode: {qubits_per_mode}
- Structure: {structure_type}

Propose a mutation that:
1. Maintains the verified code distance ≥ {min_distance}
2. Reduces qubit usage or improves structure regularity
3. Preserves stabilizer commutation relations

Explain your reasoning and provide the modified code.
```

## Key Insights from Research

### Finding 1: GSE Distance Beyond 3
Prior molecular GSE constructions maxed at distance 3. LLM-evolved constructors discovered:
- **Distance 5** on multiple molecular instances
- **Distance 6** on 20-mode instance
- First GSE encodings beyond distance 3 for dense molecular Hamiltonians

### Finding 2: Circulant Construction
Second evolutionary pass discovered a **circulant constructor**:
- Achieves 5-qubits-per-mode floor on 12, 14, 16, 20-mode instances
- Certified dense-rule fallback for edge cases (18-mode)

### Finding 3: Resource Comparison
At p=10⁻³ code-capacity memory comparison:
- **4.2-5.0× fewer data qubits** than per-mode Jordan-Wigner + surface code
- **3.4-8.2× lower logical-failure rates** under finite-weight decoding tables

## Workflow for Agents

### Step 1: Understand the Encoding Problem
- What fermion-to-qubit mapping is needed?
- What are the system parameters (modes, interactions)?
- What's the target code distance?

### Step 2: Set Up the Verifier
- Implement stabilizer coset semantics checker
- Implement code distance computation
- Implement resource metrics (qubits, gates)

### Step 3: Seed the Search
- Start with known baseline (e.g., standard GSE)
- Define test instances for evaluation

### Step 4: Run Evolutionary Loop
- LLM proposes mutations
- Verify each candidate
- Archive high-scorers
- Iterate until convergence

### Step 5: Analyze Results
- Extract interpretable patterns from successful constructors
- Verify on additional test instances
- Document discovered encoding rules

## Error Handling

### Verifier Timeout
- Set reasonable timeouts for distance computation
- Use approximate methods for large instances

### LLM Generates Invalid Code
- Verifier catches syntax/semantic errors
- Return detailed error feedback to LLM
- Guide mutation toward valid region

### No Improvement After N Generations
- Increase mutation magnitude
- Try different seed programs
- Switch to guided search (prompt with structure hints)

## Examples

### Example 1: GSE Distance Optimization

```python
# Seed: Standard GSE constructor (distance 3)
seed_code = """
def generate_gse(interaction_graph, num_modes):
    # Standard GSE construction
    ...
"""

# LLM mutation discovers distance-5 constructor
evolved_code = """
def generate_gse_v2(interaction_graph, num_modes):
    # Modified construction with improved distance
    # Uses circulant pattern discovered by search
    ...
"""
```

### Example 2: Two-Stage Search

```
Stage 1: Maximize distance
  Input: 12-mode molecular instance
  Result: Distance 5 constructor found

Stage 2: Fix distance ≥ 5, minimize qubits
  Input: Distance-5 constructor
  Result: 5-qubits-per-mode circulant constructor
```

## Resources

- **Paper**: arXiv:2606.25870 - "Evolving Quantum Error-Correcting Encodings for Molecular Simulation"
- **Authors**: Kenny Heitritter, James Brown, Tarini Hardikar
- **GitHub**: Search for "GSE encoding" or "superfast encoding" quantum implementations

## Related Skills

- quantum-error-correction-methods: QEC patterns and methodologies
- quantum-algorithm-framework-designer: Quantum algorithm design patterns
- qaoa-optimization: Quantum optimization algorithms

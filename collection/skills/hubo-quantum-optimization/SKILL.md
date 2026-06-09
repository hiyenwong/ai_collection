---
name: hubo-quantum-optimization
description: "Higher-Order Unconstrained Binary Optimization (HUBO) methodology for quantum optimization workflows. Compact binary encoding reduces qubit requirements vs QUBO but increases circuit depth via higher-order interaction terms. Use when formulating industrial logistics, scheduling, routing, or portfolio optimization problems for quantum/hybrid quantum-classical solvers, or when analyzing qubit-vs-depth trade-offs in HUBO vs QUBO encodings. (arXiv: 2605.30252)"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30252"
  published: "2026-05-28"
  authors: "Juan F. R. Hernandez, Pavle Nikacevic, Enrique Solano, Chinonso Onah, Agneev Guin, Arne-Christian Voigt, Archismita Dalal"
  tags: [quantum, optimization, hubo, qubo, logistics, scheduling, routing]
---

# HUBO Quantum Optimization

Higher-Order Unconstrained Binary Optimization (HUBO) as an alternative to QUBO for quantum optimization workflows.

## Core Concept

HUBO formulations capture complex constraints (e.g., correlated assembly-line scheduling rules) that are difficult to express in standard quadratic (QUBO) form, while simultaneously reducing the number of binary variables needed — lowering qubit demand.

## Key Trade-off: Qubit Reduction vs Circuit Depth

| Aspect | QUBO | HUBO |
|--------|------|------|
| Binary variables | More (auxiliary needed for higher-order) | Fewer (direct encoding) |
| Qubit requirement | Higher | Lower |
| Circuit depth | Lower (2-local terms) | Higher (k-local terms, k>2) |
| Hardware feasibility | Better for NISQ | Requires deeper circuits |

**The fundamental trade-off**: HUBO reduces qubit scaling through compact encoding but introduces higher-order interaction terms that increase circuit depth, limiting feasibility on current NISQ hardware.

## Mapping HUBO to Quantum Workflows

### NISQ Regime
- HUBO → classical solver (validate correctness)
- QUBO encoding → quantum annealing / QAOA
- Use HUBO for problem formulation, QUBO for execution

### Fault-Tolerant Regime
- Direct HUBO mapping to quantum circuits
- Bias-field digitized counterdiabatic quantum optimization
- Higher-order terms decomposed into multi-qubit gates

## Formulation Pattern

1. **Identify higher-order constraints**: Assembly-line scheduling rules, correlated routing decisions, multi-item portfolio constraints
2. **Express as HUBO**: Minimize H(x) = Σ c_i x_i + Σ c_ij x_i x_j + Σ c_ijk x_i x_j x_k + ...
3. **Analyze qubit scaling**: HUBO uses log(N) qubits per integer variable vs N qubits in one-hot QUBO
4. **Choose encoding strategy**:
   - NISQ: Reduce to QUBO via auxiliary variables, accept qubit overhead
   - FT: Map directly to quantum circuits with multi-controlled gates

## Application Domains

- **Industrial logistics**: Capacitated vehicle routing (CVRP), supply chain scheduling
- **Manufacturing**: Assembly-line scheduling with correlated rules
- **Portfolio optimization**: Higher-moment risk constraints (skewness, kurtosis)
- **Resource allocation**: Multi-resource, multi-constraint assignment

## Validation Workflow

1. Formulate problem as HUBO
2. Validate with classical solvers (CBC, Gurobi, etc.)
3. Compare HUBO vs QUBO encodings on same instances
4. Benchmark small instances with quantum simulation
5. Analyze resource scaling for large instances

## Related Skills

- `quantum-optimization-qaoa` — QAOA for constrained optimization
- `higher-order-portfolio-qaoa` — Higher-moment portfolio optimization
- `quantum-portfolio-optimization` — QAOA-based portfolio selection

**Activation**: HUBO, higher-order optimization, beyond QUBO, industrial logistics, scheduling, routing, qubit-depth trade-off, compact binary encoding, capacitated vehicle routing, counterdiabatic optimization

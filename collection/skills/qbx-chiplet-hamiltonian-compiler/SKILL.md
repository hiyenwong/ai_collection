---
name: qbx-chiplet-hamiltonian-compiler
description: Use when compiling 2-local Hamiltonians for chiplet QPUs.
category: ai_collection
---

# QBX: Chiplet-Aware 2-Local Hamiltonian Simulation Compiler

**Paper**: QBX: A Compiler for 2-local Qubit Hamiltonian Simulation on Quantum Chiplets (arXiv:2609.33997, Sep 2026, CMU — Zikun Li, Zhuoming Chen, Zhihao Jia)

Domain-specific quantum compiler for 2-local qubit Hamiltonian simulation (Ising/XY/Heisenberg models, QAOA cost Hamiltonians) on **chiplet/MCM architectures**. First compiler to combine Hamiltonian-level semantics (Pauli commutativity) with chiplet hardware constraints (heterogeneous cross-chiplet couplings, highways). Reduces depth up to 8.9× vs Qiskit, 53.2× vs t|ket⟩, 1.69× vs MECH; 19.5× faster compile than 2QAN while scaling to 990-qubit instances.

## When to Use
- Compiling Trotterized 2-local Hamiltonian simulation (Ising/XY/Heisenberg/QAOA-MAXCUT) for multi-chiplet superconducting devices
- Any 2-local Pauli string workload where shared-control CNOTs can be aggregated
- Extends to: minimizing cross-chiplet communication in any modular quantum architecture (also relevant to distributed QC with adjacent-only connectivity)

## Core Mechanisms

### 1. Pauli Set / Pauli Block Aggregation (the central insight)
2-local Pauli strings of the same type (XX, YY, ZZ) sharing a qubit can be **aggregated** by choosing the shared qubit as root, because the Trotter formula is permutation-invariant over Pauli strings. Attributes: (type, control/root qubit, target set).
- **Pauli set** = same-type strings sharing a root (e.g., ZZ strings rooted at q2)
- **Pauli block** = sets with same control+targets but different types (XX/YY/ZZ), ordered ZZ→YY→XX to maximize highway reuse and locality
- Aggregated blocks become **multi-target controlled gates** — O(n) CNOTs sharing one control execute in O(1) depth via highway gates (cat-state control)
- Generalization: any set of n>2 same-type strings sharing a qubit aggregates
- Multiple aggregation plans exist (e.g., triangle Z2Z1, Z2Z0, Z1Z0 has 3 plans); plan selection is part of scheduling (Section 4.3)

### 2. Highway Mechanism (from MECH, used statically)
Highway = GHZ-like entangled state √½(|0⟩⊗m + |1⟩⊗m) over ancilla qubits along a path; enables constant-depth long-range CNOT via cat entangler/disentangler + mid-circuit measurement-reset. Highways are **expensive to build** → QBX uses them only where benefit > cost.

### 3. Highway Reuse Theorems (novel correctness proofs)
- **Theorem 1 (control-empty reuse)**: two highway gates with same control+targets, separated ONLY by gates on targets (e.g., intervening Rz layers) → second reuses first's highway without reconstruction. Proved via state-vector evolution with O_i = ⊗(X if q_i∈T else I).
- **Theorem 2 (cross-Y reuse)**: exactly one Y on the control between the two highway gates → reuse by applying Y on control + X on all highway qubits. Exploits Y|0⟩=i|1⟩, Y|1⟩=−i|0⟩ phase bookkeeping. Common in Heisenberg: ZZ set followed by YY set reuses the same highway.

### 4. Five-Stage Compilation Pipeline
1. **Pauli graph partitioner** — graph G=⟨V,E⟩, V=qubits, E=co-acting strings. Partition into Nc sets of ≤Nq nodes minimizing cross-set edges (maximize intra-set edges). ILP (CPLEX) formulation with linearized Y_ij ≤ X_kj ∧ X_lj; falls back to **METIS** multi-level partitioning for scale. O(Nc·n²) vars.
2. **Set orchestrator** — quadratic assignment: minimize Σ W_ij D_kl B_ijkl (set-communication W × chiplet-distance D), linearized 4-index ILP. Places communication-intensive sets on nearby chiplets.
3. **Pauli block scheduler** — greedily builds schedule layers of blocks that can run concurrently (disjoint chiplets only). Cross-chiplet strings ALWAYS use highways; intra-chiplet blocks use highways only if #targets > threshold t. Highway paths = **Steiner tree via Mehlhorn algorithm** over data+path chiplets. Complexity O(Nc·m·n) vs 2QAN's O(m⁴).
4. **Intra-chiplet mapper** — SABRE (Qiskit) for short-term locality only (long-term placement effects wash out due to frequent qubit movement in layers).
5. **Circuit generator** — entrance selection (earliest-available ancilla), schedule layer reordering (pick layer whose data qubits are closest to ancillas), permutation-aware routing of leftover local blocks.

Component ordering matters: scheduler must run AFTER mapping decisions (post-orchestrator) or blocks conflict via intersecting highway paths.

## Key Numbers
| Comparison | Metric |
|---|---|
| vs Qiskit | 2.57× less depth, 1.30× fewer eff-CNOTs (geo-mean) |
| vs t|ket⟩ | 10.35× less depth, 2.62× fewer eff-CNOTs |
| vs MECH | 1.69× less depth, 1.08× fewer eff-CNOTs |
| vs 2QAN | 1.13× less depth, 19.54× faster compile (2QAN O(m⁴) sched, O(m²n) routing times out) |
| Backends | 324/440/990 data qubits; heavy-hex; 1×3, 2×2, 3×3 chiplet arrays; 140-qubit chiplets |
| Effective CNOT metric | #on + (p_cross/p_on)·#cross + (p_meas/p_on)·#meas with p_cross/p_on=7.4, p_meas/p_on=0.7 |
| Scalability gap widens with chiplet count (3→16 chiplets tested) |

## Reusable Design Patterns
1. **Hierarchical decomposition of mapping**: assign qubits→chiplets first (small search space, global optimum via ILP), then map within chiplets (local heuristic). Beats monolithic mappers (SABRE: 2.54× more cross-chiplet comms, 2.66× greater distance).
2. **Domain-semantics-first compilation**: exploit Trotter permutation freedom to regroup gates around hardware primitives (highways) instead of optimizing gate-level after placement.
3. **Aggregate-then-schedule**: greedy highest-degree-root aggregation per connected component; per-component independence gives parallelism.
4. **Reuse-before-reconstruct**: expensive shared resources (highways) get reuse theorems with correctness proofs — identify intervening-gate patterns (control-empty, single-Y) that permit reuse.
5. **ILP for small instances + scalable heuristic fallback (METIS) with timeout-bounded good solutions**.
6. **Cost model with heterogeneous link error rates** (effective CNOT count) — normalize noisy cross-chip operations to on-chip error units.

## Limitations / Open Problems
- Ancilla assignment NOT automated (any mix of consecutive/interleaved allowed but manually specified) — open research problem
- Parallelism restricted to disjoint-chiplet blocks (avoids tracking intra-chiplet positions; leaves concurrency on the table)
- 2QAN's unitary-synthesis merging (≤3 CNOT per 2-qubit unitary) is orthogonal and not integrated
- ILP preprocessing dominates QBX-CPLEX runtime at scale (use METIS for large problems)

## Related Skills
- `distributed-quantum-compiler-scheduling` (dSABRE routing for modular QPUs)
- `quantum-compiler-routing` (Ramanujan hypergraph routing)
- `calibration-aware-graph-rl-routing` (RL routing)
- `qubit-mapping-routing-memoization`

## References
- arXiv:2609.33997 — QBX (this paper)
- MECH: Zhang et al., arXiv:2305.05149 (highway mechanism, dynamic scheduling)
- 2QAN: Lao & Browne, ISCA 2022 (domain-specific 2-local compiler, monolithic)
- Paulihedral: Li et al., ASPLOS 2022 (blockwise Pauli optimization; recursion-depth failure at scale)
- METIS: Karypis & Kumar 1997; Mehlhorn Steiner tree IPL 1988

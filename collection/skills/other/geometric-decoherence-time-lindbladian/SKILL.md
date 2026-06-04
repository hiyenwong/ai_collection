---
name: geometric-decoherence-time-lindbladian
description: "Geometric decoherence time methodology for open many-body quantum systems — defines the earliest moment logarithmic negativity and Rényi-1/2 entropy relation breaks down under open-system evolution. Use when: analyzing decoherence in open quantum systems, Lindbladian dynamics, entanglement decay, quantum mutual information diagnostics, topological phase coherence."
metadata:
  arxiv_id: "2606.02743"
  published: "2026-06-03"
  tags: [quantum, decoherence, lindbladian, open-systems, entanglement, many-body]
---

# Geometric Decoherence Time in Lindbladian Dynamics

## Core Innovation

The onset of decoherence in open many-body systems lacks a dynamical timescale grounded in the loss of bipartite entanglement. This work introduces the **geometric decoherence time** — defined as the earliest moment the monotone relation between logarithmic negativity and Rényi-1/2 entropy breaks down under open-system evolution.

## Methodology

### Geometric Decoherence Time Definition
- For pure states: logarithmic negativity = Rényi-1/2 entropy across any bipartition
- Under open-system evolution: this equality breaks when entropy grows without entanglement growth
- The **geometric decoherence time** t_g is the earliest moment of this breakdown
- Signals the transition from coherent to decoherent dynamics

### Long-Time Diagnostic: Quantum Mutual Information
- Quantum mutual information asymptotically vanishes when steady state factorizes across bipartition
- This condition is strictly stronger than separability
- When product steady state is approached exponentially, negativity and mutual information share the same decay rate

### Key Findings

1. **Strong symmetry failure**: Residual classical correlations can survive after entanglement vanishes
2. **Kitaev chain**: Topological phase sustains longer coherence times than trivial phase at identical dissipation
   - Local minimum at chiral-symmetric point
3. **XXZ chain**: Local Z-dephasing preserves residual classical correlations
   - Gain and loss restore mutual-information tracking of negativity
4. **Single-particle Gaussian dynamics**: Criterion established analytically

## Application

- **Quantum system design**: Identify decoherence timescales before building quantum devices
- **Error correction timing**: Schedule error correction within geometric decoherence time
- **Topological protection**: Topological phases naturally resist decoherence longer
- **Dissipation engineering**: Design dissipation that preserves desired quantum correlations

## Pitfalls

- Geometric decoherence time is system-specific — must compute for each Hamiltonian
- Strong symmetries can cause tracking failure — verify absence before applying
- Mutual information tracking requires full state tomography — costly for large systems
- The criterion applies to bipartite splits — multipartite entanglement needs separate analysis

## Activation

geometric decoherence time, lindbladian dynamics, open quantum systems, logarithmic negativity, rényi entropy, quantum mutual information, topological phase coherence, entanglement decay timescale

## Related Skills

- quantum-systems-engineering
- quantum-error-correction-methods
- dependability-quantum-systems
---
name: quantum-hoare-logic
description: Quantum Hoare Logic with Integer Hybrid Path-Sums (IHPS) for formal verification and resource estimation of hybrid quantum-classical programs with unbounded loops. Bridges formal methods, quantum programming, and static analysis.
category: quantum
trigger_words: ["quantum hoare logic", "hybrid quantum program verification", "quantum resource estimation", "path-sum quantum", "quantum program static analysis", "unbounded loop quantum"]
---

# Quantum Hoare Logic with Integer Hybrid Path-Sums

## Core Idea

Combine **effective functional verification** and **resource estimation** (termination, cost) for hybrid quantum-classical programs with **unbounded loops** using **Integer Hybrid Path-Sums (IHPS)**.

## Key Innovation

- **Integer Hybrid Path-Sums (IHPS)**: Extension of path-sums to handle unbounded while loops as a representation of possible program executions
- First semi-automated static analysis solution for hybrid quantum programs
- Bridges functional verification with resource (termination/cost) estimation

## Methodology

### Step 1: Path-Sum Representation
- Represent quantum program executions as path-sums
- Extend to IHPS for handling unbounded while loops

### Step 2: Loop Invariant Strategy
- Propose generic strategy for determining **termination** via loop invariants
- Compute **expected resource consumption** using invariant-based analysis
- Illustrate on several hybrid quantum program examples

### Step 3: Semi-Automated Implementation
- Implement as semi-automatic Haskell program
- Combines equational reasoning with invariant checking

## Applications

- Verifying correctness of VQA and QAOA programs with iterative loops
- Estimating quantum resource consumption (circuit depth, qubit count)
- Static analysis of hybrid quantum-classical algorithms
- Automated verification tools for quantum software engineering

## Pitfalls

- Current gap: symbolic execution has largely left out hybridization and unbounded recursion
- Existing quantum Hoare logics lack expressiveness for computational equational reasoning
- Semi-automated: requires some human guidance for loop invariant discovery

## Verification

- Apply to known hybrid quantum programs (VQA, QAOA loops)
- Compare resource estimates with actual execution costs
- Verify termination guarantees for iterative quantum algorithms

## References

- arXiv:2607.08548 - An Effective Quantum Hoare Logic for Hybrid Quantum Programs with Unbounded Loops
- Authors: Christophe Chareton, Jad Issa, Romain Péchoux

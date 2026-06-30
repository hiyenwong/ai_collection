---
name: machine-verified-quantum-optimization
description: "Machine-verified proof methodology for quantum optimization conjectures — using LLM-generated proofs verified by Lean 4 proof assistant. Resolves the decade-old FGG conjecture for QAOA ring-of-disagrees approximation ratio."
trigger_words:
  - "machine verified proof"
  - "lean quantum"
  - "qaoa proof"
  - "FGG conjecture"
  - "quantum optimization verification"
  - "formal verification quantum"
  - 机器验证量子优化
  - "LLM proof assistant"
  - "QAOA approximation ratio"
---

# Machine-Verified Quantum Optimization

## Description

Methodology for resolving open conjectures in quantum optimization using LLM-assisted formal proof generation with mechanical verification. Uses the Claude Fable 5 LLM with an agentic toolkit and Lean 4 proof assistant to close mathematical gaps in quantum information science. Proves the FGG conjecture that depth-p QAOA on ring-of-disagrees achieves approximation ratio (2p+1)/(2p+2).

## Core Concepts

### 1. Human-LLM-Machine Feedback Loop
```
Human scaffolding (formal statement encoding) → LLM proof generation → Lean 4 mechanical verification → Feedback to LLM → Converge to certified proof
```

### 2. Lean Quantum Information Library
- Build substantial Lean 4 library of quantum information primitives
- Formalize QAOA components (cost Hamiltonian, mixing Hamiltonian, depth-p circuits)
- Reduce conjecture to single open mathematical statement

### 3. Hidden Dynamical Symmetry
- LLM uncovered hidden dynamical symmetry in the QAOA ring-of-disagrees problem
- Exploited tools from adjacent field (dynamical systems theory)
- Turned hard existence problem into explicit construction

## Usage Patterns

### Pattern 1: Formal Quantum Conjecture Resolution
```
Use when: An open conjecture in quantum optimization/information has known partial results.
Steps:
1. Build formal library in Lean 4 encoding known results
2. Reduce conjecture to gap statement
3. Feed library + agentic toolkit to LLM
4. LLM constructs proof in Lean
5. Lean mechanically verifies correctness
```

### Pattern 2: LLM-Assisted Mathematical Discovery
```
Use when: Need to find non-obvious mathematical connections.
Key insight: LLM can borrow machinery from adjacent fields to solve problems
that are hard within the original field.
```

## Implementation Guidelines

### Lean 4 Setup
- Install Lean 4 + Mathlib
- Build quantum information library with QAOA primitives
- Formalize cost/mixing Hamiltonians as ring operations

### LLM Agentic Toolkit
- Provide full Lean library context
- Give clear gap statement to close
- Use iterative feedback: proof attempt → Lean error → fix → resubmit

### Verification
- Human verification only needed for structural scaffolding (formal statement encodes intended claim)
- Proof itself is fully mechanically certified by Lean

## Key Results
- FGG conjecture proven: depth-p QAOA on ring-of-disagrees achieves ratio (2p+1)/(2p+2)
- Proof found via Claude Fable 5 LLM + Lean 4 verification
- LLM discovered hidden dynamical symmetry and borrowed tools from adjacent field

## Error Handling

### Lean Type Errors
- Break proof into smaller lemmas
- Provide intermediate definitions to LLM
- Use Lean's `#check` and `#eval` for debugging

### Convergence Issues
- Provide more context from adjacent mathematical fields
- Guide LLM toward specific proof strategies (e.g., symmetry arguments)
- Use known partial results as stepping stones

## Related Skills
- `lean-qec-formal-verification` — formal verification for quantum error correction
- `quantum-optimization-qaoa` — QAOA methodology
- `automated-quantum-software-engineering` — automated QSE methodology

## Resources
- arXiv:2606.29687
- Lean 4: https://leanprover.github.io/
- Mathlib: https://leanprover-community.github.io/mathlib_docs/

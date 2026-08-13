---
name: conservative-discrete-abstractions-cps
description: "CPS discrete abstractions with sound verification."
metadata:
  arxiv_id: "2608.10254"
  authors: "Jordan Peper, Krish Kapadia, James Gast, Ethan Howes, Ivan Ruchkin"
  published: "2026-08-10"
  subjects: "Systems and Control (eess.SY); Logic in Computer Science (cs.LO)"
  title: "A Pragmatic Guide to Building Conservative Discrete Abstractions of Cyber-Physical Systems"
license: Complete terms in LICENSE.txt
---

# Conservative Discrete Abstractions of Cyber-Physical Systems

## Overview

This tutorial presents a pragmatic, conservative-by-construction workflow for building discrete abstractions of closed-loop dynamical systems for symbolic model checking. The workflow ensures soundness while balancing pessimism with tractability to transfer verification guarantees from abstract models to concrete CPS.

## Four-Step Workflow

### 1. State-Space Partition and Abstraction-Function Design
- Design appropriate state-space partitions based on system dynamics
- Create abstraction functions that map continuous states to discrete symbols
- Balance granularity vs. computational complexity

### 2. Conservative Transition Construction
- Use axis-aligned bounding boxes for simple conservative approximations
- Apply polytopes for tighter but more complex approximations  
- Implement sampling with PAC coverage certificates for probabilistic guarantees

### 3. Mitigation of Spurious Transitions and Self-Loops
- Apply certified erasure techniques to remove provably impossible transitions
- Use counterexample-guided abstraction refinement (CEGAR) to iteratively improve precision
- Balance completeness vs. tractability in transition pruning

### 4. Sound Lifting of LTL Specifications
- Use may-must semantics for proper specification lifting
- Ensure temporal logic properties transfer correctly from abstract to concrete systems
- Handle edge cases in specification translation

## Common Pitfalls to Avoid

- **Under-approximating state space**: Leads to missing reachable states and false verification results
- **Under-approximating transitions**: Misses possible behaviors and creates false negatives
- **Unsound pruning of "degenerate" behaviors**: Removes legitimate system behaviors
- **Improper specification lifting**: Creates mismatched verification goals between abstract and concrete systems

## Case Studies

The paper demonstrates the end-to-end pipeline on three case studies, showing how design choices affect:
- Abstraction structure complexity
- Verification runtime performance  
- Verification outcome reliability

## Activation Keywords
- conservative discrete abstractions
- cyber-physical systems verification
- symbolic model checking
- state-space partitioning
- transition construction
- spurious transition mitigation
- LTL specification lifting
- CEGAR refinement
- PAC coverage certificates
- axis-aligned bounding boxes

## References
- Original paper: https://arxiv.org/abs/2608.10254
- Formal methods for hybrid systems
- Counterexample-guided abstraction refinement (CEGAR)
- Probabilistically Approximately Correct (PAC) learning for verification
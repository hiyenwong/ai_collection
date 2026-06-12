---
name: sos-distributed-tasks
description: "Decidability theory for Set of Output Sets (SOS) tasks in asynchronous distributed systems with crash failures. Use when analyzing distributed task solvability, understanding crash tolerance, or designing consensus/set agreement protocols. Keywords: distributed tasks, decidability, crash failures, consensus, set agreement, asynchronous, SOS tasks."
---

# SOS Distributed Tasks: Decidability Theory

Characterization of solvable distributed tasks in asynchronous systems with crash failures through Set of Output Sets (SOS) framework.

## Core Result

**SOS tasks are decidable**: Effective procedure determines if any SOS task is solvable asynchronously under $t$ crashes.

## SOS Tasks Definition

Task defined by set $O$ of distinct output sets that can be produced.

**SOS Graph**: $G = (O, \subset)$
- Vertices: output sets in $O$
- Edges: one output set includes another

## Solvability Rule

| Case | Condition |
|------|-----------|
| $t = 0$ | Always solvable |
| $t > 0$ | Solvable iff SOS graph $G$ is connected |

**Key insight**: Task solvability = graph connectivity!

## Surprising Implications

### k-Set Agreement Without Validity

- $k > 1$: Solvable under **any** number of crashes $t \geq 0$
- $k = 1$ (consensus): Unsolvable under $t > 0$ crashes

This reverses intuition: set agreement is easier than consensus without validity!

### d-Disagreement Tasks

New family of tasks requiring exactly $d$ different output values:
- Implementability related to harmonic series
- Connection to number theory

## Design Implications

### When Designing Distributed Tasks

1. Define set of possible outputs $O$
2. Check if SOS graph is connected
3. If $t > 0$ and graph disconnected → redesign or add validity

### Avoiding Unsolvability

- Add output set overlap
- Ensure output sets have subset relationships
- Connect the SOS graph

## Key Distinction

**With validity**: Classic impossibility (FLP, set agreement bounds)
**Without validity**: More tasks become solvable

## Mathematical Structure

```
Output Sets: O = {S₁, S₂, S₃, ...}

SOS Graph:
S₁ → S₂ if S₁ ⊂ S₂ or S₂ ⊂ S₁

Solvability:
t=0: ✓ always
t>0: ✓ iff graph connected
t>0: ✗ iff graph disconnected
```

## Example Analysis

**Consensus ($k=1$)**:
- $O = \{\{v₁\}, \{v₂\}, ...\}$ (singleton sets)
- SOS graph: isolated vertices (no subset relations between singletons)
- $t > 0$: Unsolvable ✓

**2-Set Agreement ($k=2$)** without validity:
- $O = \{\{v₁, v₂\}, \{v₁, v₃\}, ...\}$ (pairs)
- SOS graph: connected (pairs overlap)
- $t > 0$: Solvable ✓

## Theoretical Significance

1. **Decidability**: First decidable class of distributed tasks under crashes
2. **Graph characterization**: Simple test for solvability
3. **Validity role**: Clarifies importance of validity property

## Applications

- Protocol design analysis
- Crash tolerance verification
- Distributed algorithm correctness proofs
- Task specification validation

## References

- arXiv:2604.06920v1 - "On the Decidability of Distributed Tasks with Output Sets under Asynchrony and Any Number of Crashes"
- FLP (1985) - Consensus impossibility
- Borowsky & Gafni (1993) - Set agreement
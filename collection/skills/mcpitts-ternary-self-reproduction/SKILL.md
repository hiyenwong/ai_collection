---
name: mcpitts-ternary-self-reproduction
description: "Use when analyzing self-reproduction or universal construction in threshold/ternary neural networks. Fixed {−1,0,1} weights hold stored networks as data."
category: ai_collection
---

# Universal Construction and Exact Self-Reproduction in Ternary McCulloch–Pitts Networks

**Paper**: "Universal Construction and Exact Self-Reproduction in Ternary McCulloch–Pitts Networks" (arXiv: 2610.12251, Charles C. Norton, cs.LO, 8 Oct 2026)

## Core Contribution

A **fixed** network of McCulloch–Pitts threshold units with weights in {−1, 0, 1} can hold OTHER threshold networks in its state and run them. The paper carries out von Neumann's universal construction and self-reproduction **exactly** in this substrate:

- As a cellular automaton keeps its rule, the fixed network keeps its weights — what reproduces is the **stored network** (its weights and biases included, bit for bit).
- Exactness comes from integers: a trained network outputting an approximation of its weights loses information every generation; an orbit of integer pre-activations carries a weight set bit-for-bit and survives every pre-activation perturbation below 1/2.

## Architecture: The Ring Machine

**State layout**: a ring of K banks × S records, with K tapes of L cells and heads at absolute positions.
- A **record** = one two-input unit of a stored network.
- Each step evaluates **one record** of the active bank; one pass over a bank evaluates the netlist stored in it.
- The fixed ternary netlist has **depth 19** and computes the machine's step from every state (Theorem 3.2). Every ternary unit compiles into records (Lemmas 3.3–3.4).

This is the threshold-network analogue of a von Neumann universal constructor: fixed network ↔ transition rule; stored networks ↔ configurations.

## Four Constructions (exact sizes)

1. **Ring machine** (network that runs stored networks): fixed ternary netlist, depth 19, K banks of S records.
2. **Self-reproducing constructor**: an organism of **143 records** with a description code of its own — reads a network description from its tape, builds that network in the next bank, copies the description onto the next tape, hands control to what it built. Started on its own description it reproduces; copies accumulate until every bank holds one, then the state repeats every K generations (Theorems 4.5–4.6).
3. **Universal computer**: family H_A executes **SUBLEQ** (single-instruction computer) on 2^A words of A bits; step depth 13 at every word width; 8-bit member = **17,598 ternary units**. A 21-instruction program builds any byte string from run-length descriptions; a **27-instruction program** separates construction from copying (as von Neumann did) and makes the host emit the serialization of its own weights, memory and tape — the quine scheme (Theorems 6.9, 6.12).
4. **Self-reproducing universal computer**: stored in the ring machine, the host of every word width ≥ 8 runs the program, builds any network that fits a bank and reproduces in every ring — no map outside the network needed. 8-bit: **36,080 records** (Theorems 7.4–7.6).

## Noise Robustness (Theorem 8.8, Prop 8.10)

- Every orbit has a **margin of 1/2** on pre-activations (integer weights). Replicating each unit r times (Pierce's interwoven redundancy) multiplies the margin by r → suffices against **Gaussian noise of any size** on pre-activations.
- Against **output flips** (von Neumann's model) with probability ε: suffices only for ε < 1/(2e·k*), k* = largest fan-in. Above 1/(2k*) a disjunction of fan-in k* fails with probability → 1.
- First-order bound exceeds one on the complete threefold host run; a **second-order bound** certifies it (Prop 8.14): first-order failure rate is inflated by the 5–6% of failures the state doesn't show.

## Formal Verification

**Every result is proved in Rocq** (Coq successor) for every word width, ring and size named (except Lemma 6.3, the serialization format). Extracted to OCaml, the Rocq definitions write the published files; sizes, bounds and measurements are computed by the artifact.

## Why This Matters

- **Negative result for "self-reproducing neural networks" skepticism**: exact reproduction of network weights BY network dynamics is possible with only 143 records — no training, no approximation, no continuous-weight fragility.
- **Stored-program computation in a neural substrate**: the ring machine is a von-Neumann-architecture computer made of threshold units — stored networks play the role of programs/data.
- **Noise threshold dichotomy**: pre-activation noise (margin-based, robust) vs output flips (fan-in-dependent, fragile) — a sharp separation relevant to any fault-tolerant discrete neural hardware (see von Neumann's original multiplexing analysis).
- **Rocq/OCaml artifact**: the full development, generators, evaluators and run records are published — a rare fully machine-checked existence proof in the neural-network-theory space.

## Activation Triggers

self-reproduction, universal construction, von Neumann, McCulloch-Pitts, threshold network, ternary weights, SUBLEQ, quine, ring machine, Kleene recursion theorem, fault tolerance, interwoven redundancy, Rocq, formal verification, noise margin

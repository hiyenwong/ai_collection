---
name: sequential-capacity-quantum-processes
description: Use when quantifying adaptive-test capacity of quantum processes. K log K law.
category: ai_collection
version: "1.0.0"
metadata:
  arxiv_id: "2610.02068"
  published: "2026-10-01"
  authors: "Yibin Wang"
  source_title: "Sequential Capacity of Quantum Processes with Finite Memory"
  categories: "quant-ph"
trigger_words:
  - sequential capacity
  - fat-shattering dimension quantum
  - quantum process testing
  - finite memory quantum channel
  - adaptive tester
  - K log K capacity
  - quantum stochastic process complexity
---

# Sequential Capacity of Quantum Processes with Finite Memory

**Source**: arXiv:2610.02068 — "Sequential Capacity of Quantum Processes with Finite Memory" by Yibin Wang (Nagoya University), 2026-10-01

## Overview

Establishes a tight law for how complex a fixed-memory quantum device's observable responses can become as it runs longer. The key complexity measure is **sequential response capacity** C_γ(K; d, r): how many adaptive testing stages (each on a fresh run) can continue to separate possible processes by a prescribed probability gap γ. This is formalized via **sequential fat-shattering dimension** over the process class P_{d,r}(K).

## Core Methodology

### The Fixed-Memory Law (Theorem III.1)

For every fixed visible dimension d ≥ 2 and memory cap r ≥ 1:

```
C_γ(K; d, r) = Θ_{d,r}( K log₂((K+1)/γ) ),  K ≥ 1, 0 < γ ≤ 1
```

- **K log K duration dependence** — superlinear in run length at fixed resolution.
- Attained by **memory-one qubit unitary processes** U_t(θ_t) = diag(1, e^{iθ_t}) with **exact zero-or-one responses** — no propagated memory needed.
- Classical stochastic processes (measuring input+memory in a fixed basis each transition) have only **Θ(K)** — linear capacity. The quantum advantage is the coherent intervention structure, not memory.

### Phase-Tree Construction (the mechanism)

The tester retains one control qubit initialized in |+⟩ and implements queries with coefficient vector s ∈ {−1, 0, 1}^K:

```
f_θ(E_{s,φ}) = (1 + cos(Σ_t s_t·θ_t − φ)) / 2
```

Key steps:
1. Assign independent dyadic values to Boolean sums of the phases
2. **Möbius (Boolean) inversion** of subset sums isolates successive binary digits with offsets determined by earlier labels
3. For K = 2^ℓ: exactly K(1 + ℓ/2) independent labels; padding handles other horizons
4. Each query uses each transition **once in the forward direction** (no transition reuse)
5. **Probability bisection** supplies the precision (1/γ) dependence

Worked example (K=2): α = θ₁+θ₂ ∈ {0,π}, β = θ₂ ∈ {0,π/2,π,3π/2}. Query (1,1) reveals the bit in α; query (−1,1) with known offset −α measures cos(2β) revealing parity; query (0,1) with offset πb/2 reveals the remaining bit of β.

### Noise Law (Theorem V.1 — known dephasing)

With measured classical address dimension R = 2^h (loaded in h transitions), T phase transitions, K = h+T, Pauli noise vector q = (q_I, q_X, q_Y, q_Z), define the **residual phase-flip probability after syndrome correction**:

```
e(q) = min(q_I, q_Z) + min(q_X, q_Y)
```

Then uniformly for 0 < γ ≤ 1/16, 0 ≤ e ≤ 1/8:

```
sfat_γ(N^{P}_{R,T,q}) = Θ_γ( R·T·log₂[1 + min(T, 1/e)] )
```

Capacity regimes (Table I):
| Noise range | Sequential capacity order |
|---|---|
| p = 0 or p ≤ 1/T | RT log₂(1+T) |
| 1/T < p ≤ 1/4 | RT log₂(1+1/p) |
| Fixed p > 0, growing T | RT |

- **Pure transverse flips** (q_X = a, q_I = 1−a, q_Y = q_Z = 0) give e(q) = 0: the logarithmic enhancement **survives** — only residual phase noise after correction matters.
- Upper bound technique: regular polygon with m = ⌈π/arccos(1−p)⌉ vertices contains the coherence circle of radius 1−p; fixed unitary vertices simulate the channel exactly; program of dimension m^{RT}.
- Lower bound: blocks of length ≤ min(T, ⌊1/(4p)⌋) retain fixed margin; Boolean phase trees on blocks, concatenated over addresses.

### Prediction Consequences

- Minimax expected prediction mistakes with probability feedback: **Θ(min{N, K log(K+1)})**
- One binary outcome per run: minimax average squared error **Θ(min{1, K ln(K+N)/N})**

### Resource Separations

- One complete run leaks at most **2(K+1)·log₂d bits** about a classical target label (Prop G.1)
- Classical program storage for dephased phases requires **Θ(T log T) bits** at fixed response error, while an exact quantum program uses O_p(T) qubits — capacity and simulation-program size are distinct resources.
- Coherent recycling of the visible interface (no private qubit) attains the same order; repeating one unknown phase for all K transitions gives only Θ(log(K+1)) — **independent time-dependent parameters and coherent access are distinct resources**.

## Reusable Patterns

1. **Fat-shattering dimension as process complexity**: when asking "how distinguishable is a family of stochastic/quantum processes under adaptive testing", model it as sfat over the response-function class, not as parameter counting.
2. **Boolean/Möbius inversion queries**: isolate individual bits of subset-sum parameters by signed queries whose offsets use previously revealed labels — achieves information-theoretic optimality with zero-or-one responses.
3. **Residual-error-after-correction as the complexity currency**: define e = (best-pair error) and express capacity as log₂(1+min(T, 1/e)) — separates noise that can be syndrome-corrected from noise that truly decoheres.
4. **Polygon-cover program upper bounds**: cover a noise circle of radius 1−p by a regular m-gon of unitaries to build exact classical simulation programs of size m^{#params} — generic upper-bound tool for dephasing families.
5. **Memory-vs-coherence decomposition**: classical fixed-basis measurement collapses capacity to linear; coherent control on the interface gives the log boost — when analyzing any process class, ask which of the two resources is present.

## Activation

sequential capacity, fat-shattering dimension quantum, quantum process testing, finite memory quantum channel, adaptive tester, quantum stochastic process complexity

## Pitfalls

- The K log K law is for **fixed** d, r — constants depend on them; growing-memory regimes (r = K²) have only Ω(K⁴/log²K) to O(K^{11/2} log K) with a gap remaining.
- Each tree node is a **fresh complete run** of the fixed target — the tree is over response branches, not Bernoulli samples of one experiment.
- The optimal joint small-margin dependence (γ → 0 jointly with growing T) remains open.
- Response capacity ≠ simulation program size: same family can have Θ_γ(T) capacity but Θ(T log T) classical program lower bound.

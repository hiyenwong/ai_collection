---
name: boolean-threshold-neuron-capacity
description: Neuron capacity from Boolean threshold function asymptotics.
category: ai_collection
metadata:
  arxiv_id: "2609.29756"
  published: "2026-09-24"
  authors: "Xinyuan Xie"
  tags: [boolean-threshold-functions, neuron-capacity, hopfield, memory-retrieval, random-matrices, hyperplane-arrangements]
---

# Boolean Threshold Functions, Neuron Capacity, and Memory Retrieval

Methodology from arXiv:2609.29756 (Xie, Sep 2026). Solves several long-standing open problems in the theory of McCulloch–Pitts threshold neurons: the exact asymptotic count of Boolean threshold functions, the sharp r = n−1 threshold for spurious-free Hopfield memory retrieval, the average specification number, and the endpoint case of the Kahn–Komlós–Szemerédi linear-dependence conjecture. Use when analyzing capacity of single neurons/threshold gates, Hopfield/projection-rule storage limits, random sign-vector spans, or Boolean function counting.

## Core Results

### 1. Counting Boolean threshold functions (Theorem 1)

The number T_n of distinct Boolean threshold functions f(x) = sgn(a0 + ⟨a,x⟩) on {−1,1}^n:

```
T_n = 2 · C(2^n − 1, n) · (1 + O(n^−99))
```

Confirms the asymptotic `T_n ∼ 2^(n² − n·log2(n) + 1.44n)` (Stirling form), closing the exponential gap between the 1960s upper bound (Cover/Whiteside/Muroga: sum of binomials) and the Kahn–Komlós–Szemerédi lower bound `2^(n² − n·log2 n − O(n))`. The O(n) error term of KKS is reduced to O(n^−99) (any fixed negative power A works).

**Neuron capacity (Corollary 2)**: capacity of one threshold neuron = log2 T_n = **n² − log2(n!) + 1 + O(n^−99) bits ≈ n² − n·log2(n) + 1.44n**. Matches Cover's 1965 geometric count exactly; now proven tight with essentially vanishing error.

### 2. Span of random sign vectors (Theorem 3)

For v1,…,v_r independent uniform on {−1,1}^n, 1 ≤ r ≤ n−1, with probability ≥ 1 − C·n^−99:

```
⟨v1,…,v_r⟩ ∩ {−1,1}^n = {±v1, …, ±v_r}
```

i.e. the span contains NO new hypercube vertices beyond the stored vectors and their negatives. This settles the Kalai–Linial–Odlyzko conjecture: the transition happens exactly at r = n−1 (Komlós: fails at r = n; Odlyzko: held for r ≤ n − 10n/log n; KKS: r ≤ n − C).

### 3. Sharp Hopfield memory-retrieval threshold (Corollary 5)

For the **projection rule** (Personnaz–Guyon–Dreyfus) storing memories v1,…,v_r, analyzed via the **Kanter–Sompolinsky Hamiltonian** H_KS(x) = −(1/2)·x^T P_V x (P_V = V(V^TV)^−1V^T = projector onto memory span):

- Ground states of H_KS = hypercube vertices inside the memory span
- **With probability ≥ 1 − C·n^−99, for ALL r ≤ n−1, the only ground states are the stored memories and their negatives** — zero spurious minima
- At r = n the property fails with probability → 1 (Komlós singularity of random ±1 matrices)

**Takeaway for associative memory**: projection-rule Hopfield networks store up to **n−1 ≈ full dimension** memories spurious-free (vs. ~0.14n for Hebbian rule) — but n−1 is a hard wall: one more memory and ground states proliferate.

### 4. Average specification number (Theorem 6)

The average, over all threshold functions f, of the minimal number of labelled examples (x, f(x)) uniquely specifying f:

```
2(n+1) − C·n^−98 ≤ σ̄_n ≤ 2(n+1)  ⇒  lim σ̄_n/(n+1) = 2
```

Settles Anthony's open problem (Problem 6.2, 2003). **Learning-theory implication**: ~2(n+1) labelled examples suffice on average to pin down a threshold function among all T_n candidates — twice the VC dimension (n+1).

### 5. Linear dependence of random sign vectors (Theorem 7)

For 1 ≤ r ≤ n−1:

```
P{v1,…,v_r linearly dependent} = C(r,2)·2^(r−n) + O(2^−n·e^−cn)
```

Confirms the Kahn–Komlós–Szemerédi conjecture at the endpoint r = n−1 with exponentially small error. Dominant failure mode: two antipodal/parallel vectors (the C(r,2)·2^(r−n) term).

## Proof Architecture (transferable techniques)

1. **Threshold functions ↔ hyperplane arrangement regions** (Cover's correspondence): T_n = number of regions of the arrangement {e^⊥ : e ∈ E_n}, E_n = {(1,x): x ∈ {−1,1}^n}. Affine section trick T_n = 2·r(D_n) halves the problem.
2. **Region lower bound via intersection subspaces**: each independent n-subset S ⊂ E_n with span ∩ E_n = S certifies one region; counting such subsets gives the lower bound.
3. **Integral cokernel estimate**: reduce vertex-avoidance of the span to bounding the probability that the cokernel of an (n−2)×(n−1) random 0/1 matrix has large order — via higher-moment bounds, **Maples's comparison theorem**, **Nguyen–Wood rank mod p estimates**, and **inverse Littlewood–Offord theory**.
4. **Endpoint singularity analysis**: adapt **Jain–Sah–Sawhney corank estimates** + almost-constant null vectors; column-sign symmetry argument shows conditioning on balanced sign sets doesn't change the relevant probabilities.
5. **LLM-assisted proving**: the author records two ChatGPT conversation links that produced proofs of a weaker Theorem 1 and of Theorem 7 — frontier LLMs now contribute to resolving open problems about the very neurons underlying them.

## Usage Patterns

- **Single-neuron expressivity budget**: n²−n·log2(n)+1.44n bits — the ceiling any n-input threshold gate can represent, regardless of training method.
- **Projection-rule Hopfield design**: store r = n−1 random patterns for spurious-free recall; never attempt r ≥ n. Memories must be linearly independent (guaranteed whp for random ±1 patterns, failure prob ~ C(r,2)·2^(r−n)).
- **Sample complexity for threshold learning**: budget ~2(n+1) labelled examples on average to uniquely identify the target function (worst case up to 2n, Anthony's upper bound).
- **Random sign matrix checks**: for r ≤ n−1 vectors, dependence is dominated by antipodal pairs — useful when debugging random projection/encoding layers built from ±1 random matrices.

## Pitfalls

- The r = n−1 wall applies to the **projection rule**, not Hebbian storage — Hebbian Hopfield capacity (~0.138n) is far lower, with different spurious-state structure.
- The 1−O(n^−99) probability is asymptotic; for small n, spurious ground states still occur with non-negligible probability (Odlyzko's n − 10n/log n safe range is the conservative practical bound).
- Irmatov's claimed asymptotic T_n ∼ 2^(n²−n+1) had unresolved gaps; this paper's C(2^n−1, n) form is the verified one — cite Xie (2026), not Irmatov.

## Related Skills
- `hopfield-continual-learning-diffusion` — modern Hopfield variants (this paper covers the classical projection-rule limit)
- `kernel-hopfield-attractor-geometry` — attractor-boundary analysis complements the ground-state counting here
- `spiking-mode-neural-networks` — Hopfield decomposition of recurrent weights

**Source**: arXiv:2609.29756 — X. Xie, "Boolean threshold functions, neuron capacity, and memory retrieval", math.PR, 24 Sep 2026. MSC: 94D10, 52C35, 60B20, 15B52, 68T07.

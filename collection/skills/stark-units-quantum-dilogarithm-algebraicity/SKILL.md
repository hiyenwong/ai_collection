---
name: stark-units-quantum-dilogarithm-algebraicity
metadata:
  arxiv_id: "2609.21892"
  published: "2026-09-18"
  authors: "Danylo Radchenko, Campbell Wheeler"
  categories: "math.NT, math-ph, quant-ph"
  tags: [number-theory, quantum-dilogarithm, Stark-units, fusion-categories, SIC-POVM, Ocneanu-rigidity]
description: "Use for Stark unit algebraicity via quantum dilogarithm."
---

# Stark Units and Finite Quantum Dilogarithms: Algebraicity via Categorification

Source: Radchenko-Wheeler, "Real quadratic fields and finite quantum dilogarithms I", arXiv:2609.21892 (2026-09-18). Number Theory (math.NT) + math-ph; 35 pages.

## Overview

Radchenko-Wheeler prove that **Stark-Shintani ray class invariants (Stark units)** associated to real quadratic fields are algebraic numbers, by showing their values arise as special values of **Faddeev's modular quantum dilogarithm** that satisfy an explicit overdetermined system of polynomial equations. The proof strategy is a categorification: solutions categorify **Izumi fusion rings**, and algebraicity follows from **Ocneanu's rigidity theorem**. A byproduct is an explicit infinite family of **irrational near-group fusion categories**, and an application proves the Appleby-Flammia-Kopp quadratic relations for Stark units (motivated by Zauner's SIC-POVM conjecture).

## Core Mathematical Objects

### 1. Stark Units / Stark-Shintani Ray Class Invariants

- For a real quadratic field K, Stark units are canonical algebraic units constructed from ray class fields.
- The Stark-Shintani invariants are given by **special values of Faddeev's modular quantum dilogarithm** (introduced by Garoufalidis-Kashaev-Zagier).
- Main theorem: these invariants are algebraic numbers (previously inaccessible by direct means).

### 2. Faddeev's Modular Quantum Dilogarithm

- A modular-invariant version of the quantum dilogarithm, analytic in the complex plane.
- Special values at algebraic arguments produce transcendental-looking constants whose arithmetic nature is the central question.

### 3. Andersen-Kashaev Equation System (Overdetermined Polynomial Equations)

- **Main discovery**: special values of the modular quantum dilogarithm satisfy an explicit *overdetermined* system of polynomial equations.
- This matches a variation of Andersen-Kashaev's defining equations for a quantum dilogarithm on a product of two cyclic groups (Z/N × Z/M).
- The overdetermined structure (more equations than unknowns) is what forces rigidity.

### 4. Izumi Fusion Rings and Near-Group Categories

- Solutions to the polynomial system categorify **fusion rings introduced by Izumi**.
- Fusion ring = Grothendieck ring of a fusion category (semisimple rigid monoidal category).
- Near-group fusion categories: fusion rules with a group part plus one extra object.

### 5. Ocneanu's Rigidity Theorem (Proof Engine)

- Ocneanu rigidity: there are only finitely many fusion categories with a given fusion ring (up to equivalence).
- Algebraic argument: a rigid structure forces structure constants to be algebraic — solutions of polynomial systems over Q̄.
- This converts the categorification statement into the arithmetic conclusion: **special values are algebraic**.

### 6. Application: SIC-POVM Quadratic Relations

- Zauner's conjecture: SIC-POVMs (complex equiangular lines) exist in every dimension; overlap values involve Stark units.
- Appleby-Flammia-Kopp conjectured a family of **quadratic relations for Stark units**.
- Radchenko-Wheeler prove these relations as a direct application of their machinery.

## Methodology (How to Apply)

### Pattern 1: Proving Algebraicity via Categorification + Rigidity

When facing "is this transcendental-looking constant algebraic?" questions:
1. Represent the constant as a special value of a structured analytic function (quantum dilogarithm, modular cocycle).
2. Derive an overdetermined polynomial equation system satisfied by the value.
3. Match the system to defining equations of a known algebraic structure (fusion category, Hopf algebra).
4. Apply a finiteness/rigidity theorem (Ocneanu rigidity, Hopf algebra integrality) to conclude the values solve polynomial equations over Q — hence are algebraic.
5. Bonus: extract explicit families of new algebraic structures (near-group categories) from solutions.

### Pattern 2: Connecting Quantum Information Conjectures to Number Theory

1. SIC-POVM overlap geometry → identify algebraic invariants (Stark units, ray class fields).
2. Translate geometric conjectures (Zauner, Appleby-Flammia-Kopp relations) into statements about special values.
3. Prove via the categorification machinery above.

### Pattern 3: Overdetermined Systems as Rigidity Witnesses

- An overdetermined system (more equations than unknowns) typically has no solutions; existence of a solution is itself a strong rigidity constraint.
- When analyzing special functions: seek hidden overdetermined polynomial relations — they encode deep arithmetic.

## Key Insights for Reuse

1. **Analytic special values + categorification = algebraicity**: The bridge from analysis (quantum dilogarithm values) to arithmetic (algebraicity) runs through category theory.
2. **Rigidity theorems as proof engines**: Ocneanu's rigidity is the load-bearing step — finiteness of categorifications forces algebraicity of invariants.
3. **Overdetermination is a feature**: extra polynomial equations provide the rigidity that makes the proof work.
4. **Quantum information ↔ number theory dictionary**: SIC-POVM overlaps ↔ Stark units; Zauner's conjecture ↔ quadratic relations for Stark units.
5. **Byproduct harvesting**: proving a main theorem via categorification yields new families of exotic algebraic objects (irrational near-group fusion categories) for free.

## Pitfalls

- **Not all quantum dilogarithm values are algebraic**: the algebraicity is specific to the Stark-Shintani invariant structure — do not generalize carelessly.
- **Ocneanu rigidity applies to fusion categories, not bare fusion rings**: the categorification step (realizing the ring as K₀ of a category) is essential before invoking rigidity.
- **Andersen-Kashaev equations are for Z/N × Z/M**: the variation used here must be checked to match the exact algebraic structure before transplanting the argument.
- **SIC-POVM application is one family of relations**: the theorem covers the Appleby-Flammia-Kopp family, not all quadratic relations among Stark units.

## Related Skills

- `stark-units-sic-overlaps` (June 2026 predecessor: conjectural Stark unit factorization of SIC overlaps)
- `sic-overlap-stark-units-number-theory` (Bengtsson-McConnell variant)
- `quantum-number-theory-algorithms` (quantum algorithms for number theory)

## References

- Radchenko, D., Wheeler, C. "Real quadratic fields and finite quantum dilogarithms I" arXiv:2609.21892 (2026-09-18)
- Garoufalidis-Kashaev-Zagier: Faddeev's modular quantum dilogarithm
- Andersen-Kashaev: quantum dilogarithm on products of cyclic groups
- Izumi: fusion rings; Ocneanu: rigidity of fusion categories
- Appleby-Flammia-Kopp: quadratic Stark unit relations; Zauner's SIC-POVM conjecture

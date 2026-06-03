---
name: flow-loops-quantum-groups
description: "Methodology connecting quantum group invariants with Morse flows for knot theory analysis. Use when analyzing knot invariants, quantum groups, or topological quantum field theory."
---

# Flow Loops and Quantum Groups

## Description
Methodology connecting quantum group invariants with Morse flow dynamics for studying knots. For fibered knots, defines a two-variable series invariant by counting Morse flow loops in the knot complement. This dynamical series is conjectured to agree with the BPS q-series from 3d N=2 QFTs, providing a bridge between dynamical systems and quantum topology.

## Activation Keywords
- flow loops quantum groups
- quantum group invariants
- Morse flow knots
- knot theory quantum
- BPS q-series
- 量子群不变量
- Morse流 Knot理论
- topological quantum field theory
- 3d N=2 QFT knots
- dynamical series knot invariants

## Core Concepts

### Quantum Group Invariants
Traditional approach to knot invariants using representations of quantum groups (quantized universal enveloping algebras). Produces polynomials like Jones, HOMFLY-PT, and Alexander polynomials.

### Morse Flow Dynamics
Dynamical systems approach: study flows on the knot complement (3-manifold minus the knot). For fibered knots, the complement fibers over S^1 with fiber a surface, enabling Morse-theoretic analysis.

### The Key Insight
The paper establishes that for fibered knots:
1. Morse flow loops in the complement can be counted to produce a two-variable series
2. This series is conjecturally equal to the BPS q-series from 3d N=2 supersymmetric QFTs
3. This connects dynamical counting → quantum invariants → physical state counting

### Two-Variable Series Invariant
- Variables typically denoted (q, x) where q tracks homological grading and x tracks flow properties
- Coefficients count closed orbits of the Morse flow
- Converges in appropriate domain
- Specializes to known quantum invariants under certain limits

## Tools Used
- terminal: Run mathematical computations, symbolic algebra
- web_search: Search for related papers and implementations
- write: Create SKILL.md files and mathematical documentation

## Usage Patterns

### Pattern 1: Analyzing Quantum Group Invariants
When studying knot invariants from the quantum group perspective:
1. Identify the quantum group (U_q(sl_2), U_q(sl_n), etc.)
2. Determine the representation (fundamental, adjoint, etc.)
3. Compute the invariant via R-matrix or state-sum methods
4. Compare with dynamical series from Morse flow analysis

### Pattern 2: Morse Flow Analysis
For fibered knots:
1. Identify the fibration structure of the knot complement
2. Construct the Morse function on the fiber surface
3. Analyze critical points and gradient flow lines
4. Count closed orbits → produce dynamical series
5. Compare with known quantum invariants

### Pattern 3: BPS State Counting
Connecting to physics:
1. Identify the 3d N=2 QFT associated to the knot complement
2. Compute BPS spectrum using wall-crossing formulas
3. Extract q-series from BPS state counting
4. Verify agreement with dynamical series

## Instructions for Agents

### Step 1: Identify the Problem Type
Determine if the task involves:
- Computing quantum group invariants for knots
- Analyzing Morse flows on knot complements
- Computing BPS q-series from 3d N=2 QFTs
- Establishing equivalences between these approaches

### Step 2: Select the Appropriate Framework
- For algebraic computations → Quantum group approach
- For dynamical systems → Morse flow approach
- For physics connections → BPS state counting

### Step 3: Apply the Correspondence
When possible, verify that results from different frameworks agree:
- Quantum invariant = Dynamical series = BPS q-series
- This triple correspondence is the core insight of the methodology

### Step 4: Extract Topological Information
Use the invariants to study:
- Knot genus and fiberedness
- Hyperbolic volume estimates
- Relationship to 3-manifold invariants

## Mathematical Framework

### Fibered Knots
A knot K ⊂ S^3 is fibered if its complement fibers over S^1 with fiber a surface Σ. Examples:
- Trefoil knot (genus 1)
- Figure-eight knot (genus 1)
- All torus knots

### Morse Flow Construction
Given a fibered knot:
1. The complement M = S^3 \ K ≅ Σ × S^1 (up to Dehn filling)
2. Choose a Morse function f: Σ → ℝ
3. Study gradient flow ∇f and its periodic orbits
4. Count orbits weighted by their action/homology class

### Series Invariant
Z(q, x) = Σ_{γ} q^{A(γ)} x^{H(γ)}
where:
- γ runs over closed orbits
- A(γ) is the action/period
- H(γ) is the homology class

## Error Handling

### Non-Fibered Knots
For non-fibered knots, the fibration structure does not exist. In this case:
- Use generalized Heegaard Floer homology
- Consider sutured manifold decomposition
- Apply knot Floer homology as alternative

### Divergence Issues
The dynamical series may not converge everywhere:
- Identify the domain of convergence
- Use analytic continuation when needed
- Consider resummation techniques

## Best Practices

1. Start with simple examples (trefoil, figure-eight) to verify methodology
2. Use known quantum invariants as sanity checks
3. Document the correspondence between frameworks explicitly
4. Be aware that the conjecture may not hold for all knot types

## Limitations
- Currently proven mainly for fibered knots
- Conjectural correspondence with BPS series needs further verification
- Computational complexity grows rapidly with knot complexity
- Requires familiarity with quantum groups, Morse theory, and QFT

## Resources
- arXiv: 2605.21382 - "Flow loops and quantum groups"
- Categories: math.GT, math.QA, math.SG
- Related: Quantum topology, Morse theory, 3d N=2 QFTs

## Related Skills
- quantum-topological-data-analysis: Quantum algorithms for TDA
- quantum-geometry-topology-research: Quantum + geometry + topology research
- mathematical-quantization: Kohn-Nirenberg and Lie group quantization

---
name: split-primes-elekes-ronyai
description: "Split primes and Elekes-Rónyai problem methodology for number theory counterexamples and arithmetic combinatorics"
category: number-theory
tags: ["number-theory", "arithmetic-combinatorics", "prime-numbers", "expander-polynomials", "subquadratic-growth"]
---

# Split Primes and Elekes-Rónyai Problem

## Description
Methodology for constructing counterexamples to the Elekes-Rónyai problem, demonstrating that certain polynomials which are neither additive nor multiplicative can still produce subquadratic expansion. Based on the technique showing |{x+y+(x-y)²: x,y∈A}| ≤ |A|^(2-c) for absolute constant c>0.

## Activation Keywords
- Elekes-Ronyai
- split primes
- subquadratic expansion
- polynomial expansion
- arithmetic combinatorics
- sum-product phenomena
- 素数分裂
- 亚二次扩张
- 算术组合学

## Core Concepts

### The Elekes-Rónyai Problem
The classical Elekes-Rónyai theorem states that for any bivariate polynomial f(x,y) ∈ R[x,y] that is neither of the form g(h(x)+k(y)) nor g(h(x)·k(y)), the image set |f(A,A)| grows quadratically (|A|²) for large finite sets A.

### The Counterexample Construction
The counterexample uses f(x,y) = x+y+(x-y)² which is neither additive nor multiplicative in the Elekes-Rónyai sense, yet produces subquadratic growth:
- |{x+y+(x-y)²: x,y∈A}| ≤ |A|^(2-c)
- For some absolute constant c > 0
- Achieved through careful construction of sets A ⊂ R

### Connection to Split Primes
The construction relates to split primes in number fields, where the splitting behavior of primes can be used to construct sets with controlled expansion properties.

## Usage Patterns

### Pattern 1: Counterexample Construction
1. Identify polynomial f(x,y) that avoids both additive and multiplicative forms
2. Construct set A using split prime properties in number fields
3. Bound |f(A,A)| using arithmetic combinatorics techniques
4. Verify subquadratic growth rate

### Pattern 2: Expansion Rate Analysis
1. For given polynomial f, determine if it falls in additive/multiplicative class
2. If not, check if counterexample construction applies
3. Calculate expansion exponent c using the methodology
4. Compare with theoretical bounds

## Mathematical Framework

### Key Ingredients
1. **Split Prime Construction**: Use algebraic number theory to construct sets A with controlled arithmetic properties
2. **Expansion Bounds**: Apply combinatorial techniques to bound |f(A,A)|
3. **Counterexample Verification**: Show f is neither additive nor multiplicative form

### Applications
- Additive combinatorics research
- Sum-product phenomenon extensions
- Polynomial growth classification
- Number field arithmetic

## Error Handling
### Polynomial Classification
- If f(x,y) = g(h(x)+k(y)) or g(h(x)·k(y)), the Elekes-Rónyai theorem applies directly
- Must verify f does NOT decompose into these forms before claiming counterexample

### Set Construction
- Set A must be carefully constructed — random sets typically achieve quadratic expansion
- Use split prime properties for controlled construction

## References
- arXiv:2606.13619 — Split primes and the Elekes-Rónyai problem
- Elekes, Rónyai — Original theorem on polynomial expansion
- Solymosi — Survey on sum-product problems
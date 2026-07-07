---
name: extension-profile-shape-functions
description: "Beyond mutual information — extension profiles and shape functions of random variable pairs. Use when analyzing structural properties of joint distributions not captured by mutual information alone, connecting information theory to spectral graph theory, or deriving non-Shannon-type information inequalities."
---

# Extension Profiles and Shape Functions

## Description
A framework for studying the extension profile of jointly distributed random variables (X,Y), defined as the set of all triples (H(X|W), H(Y|W), I(X:Y|W)) obtained by extending the pair with an auxiliary random variable W. Introduces the shape function (Legendre-Fenchel transform of the profile boundary) to characterize structural properties of joint distributions not determined by entropies and mutual information alone.

## Activation Keywords
- extension profile
- shape function
- mutual information beyond
- non-Shannon information inequalities
- Legendre-Fenchel transform
- Gacs-Korner common information
- 扩展轮廓
- 形状函数
- joint distribution structure
- biregular bipartite graph

## Core Mathematical Framework

### Extension Profile Definition
For jointly distributed finite-valued random variables (X,Y):

```
Extension Profile = {(H(X|W), H(Y|W), I(X:Y|W)) : W is auxiliary}
```

This captures structural properties NOT determined solely by:
- H(X), H(Y) (marginal entropies)
- I(X:Y) (mutual information)

### Shape Function
- Defined as the Legendre-Fenchel transform of the nontrivial profile boundary
- Characterizes the achievable region of conditional entropies and conditional mutual information
- General upper and lower bounds in terms of classical information-theoretic quantities

### Graph-Theoretic Interpretation
For pairs uniform on their support:
1. Interpret support as a **biregular bipartite graph**
2. Relate extension profile to combinatorial and spectral properties
3. Bounds on shape function in terms of **second-largest eigenvalue**
4. Small second eigenvalue → restricted class of extensions

### Key Connections
| Concept | Connection |
|---------|-----------|
| Non-Shannon inequalities | Extension profile boundaries |
| Gács-Körner common information | Profile structure |
| Spectral graph theory | Second eigenvalue bounds |
| Biregular bipartite graphs | Support structure |

## Usage Patterns

### Pattern 1: Joint Distribution Analysis
When mutual information alone is insufficient:
1. Compute the extension profile of (X,Y)
2. Map the achievable (H(X|W), H(Y|W), I(X:Y|W)) region
3. Use the shape function to characterize the boundary
4. Identify structural properties hidden from standard measures

### Pattern 2: Spectral Bound Analysis
For uniform-on-support distributions:
1. Construct the biregular bipartite graph from the support
2. Compute the second-largest eigenvalue λ₂
3. Apply the spectral bound on the shape function
4. Small λ₂ implies restricted extensions

### Pattern 3: Non-Shannon Inequality Derivation
When deriving information inequalities beyond Shannon type:
1. Use the extension profile to identify infeasible regions
2. The shape function boundary provides tight constraints
3. Relate to Gács-Körner common information for tightness

## Instructions for Agents

### Step 1: Verify Joint Distribution Structure
- Check if (X,Y) is uniform on support
- If yes: proceed with graph-theoretic interpretation
- If no: use general bounds on shape function

### Step 2: Compute Extension Profile
- Enumerate auxiliary variables W
- Compute (H(X|W), H(Y|W), I(X:Y|W)) for each W
- Map the achievable region in 3D space

### Step 3: Derive Shape Function
- Apply Legendre-Fenchel transform to profile boundary
- Compute upper and lower bounds
- For graph case: use spectral properties

### Step 4: Interpret Results
- Restricted extensions → strong structural constraints
- Non-restricted extensions → flexibility in joint distribution
- Connect to Gács-Körner and spectral graph theory

## Error Handling

### Non-Uniform Support
- The graph-theoretic interpretation requires uniform-on-support
- For non-uniform pairs: use general information-theoretic bounds
- The shape function still exists but lacks spectral interpretation

### Large Alphabet
- Extension profile computation scales with alphabet size
- Use spectral bounds for computational tractability
- The second eigenvalue approach is more efficient

## Resources
- arXiv:2606.23849 - "Beyond Mutual Information: Extension Profiles and Shape Functions of Random Variable Pairs" by Rostislav Matveev, Andrei Romashchenko
- 42 pages, 2 figures

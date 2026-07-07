---
name: "quantum-trace-maps-3d"
description: "3D Quantum Trace Map methodology — homomorphism from skein modules of triangulated 3-manifolds to quantum gluing modules, unifying constructions by Garoufalidis-Yu and Panitch-Park."
---

# Quantum Trace Maps 3D

## Description
3D Quantum Trace Map methodology — constructing homomorphisms from the skein module of an ideally triangulated 3-manifold to its quantum gluing module. This quantizes the classical trace map and unifies two previously distinct constructions (Garoufalidis-Yu and Panitch-Park), while extending to certain new manifold classes.

**Source**: arXiv:2606.13268 — "On 3d Quantum Trace Maps"

## Activation Keywords
- 3d quantum trace map
- quantum trace map
- skein module quantum gluing
- triangulated 3-manifold quantum
- 3-manifold skein quantization
- garoufalidis yu panitch park trace
- quantum trace construction

## Core Concepts

### Skein Modules and Quantum Gluing
- **Skein Module**: Algebraic structure encoding knot/link information in 3-manifolds via skein relations
- **Quantum Gluing Module**: Quantum-deformed algebraic structure describing how manifold pieces glue together
- **Trace Map Homomorphism**: Maps skein elements to their "quantum trace" values in the gluing module

### Unification of Two Constructions
The paper proposes a **third construction** that:
1. Agrees with the Garoufalidis-Yu construction
2. Extends to cases beyond the Panitch-Park construction
3. Provides a unified framework for 3D quantum trace maps

### Classical to Quantum Quantization
- The quantum trace map **quantizes** the classical trace map
- Preserves algebraic structure while introducing quantum deformation parameters

## Usage Patterns

### Pattern 1: Skein Module Analysis in 3-Manifolds
When analyzing topological invariants of triangulated 3-manifolds:
1. Identify the ideal triangulation of the target 3-manifold
2. Construct the skein module for the manifold
3. Apply the quantum trace map homomorphism
4. Extract quantum invariants from the gluing module image

### Pattern 2: Comparing Quantum Trace Constructions
When evaluating different approaches to quantum trace maps:
1. Check if the construction agrees with Garoufalidis-Yu
2. Check if it extends beyond Panitch-Park coverage
3. Verify quantization of the classical trace map
4. Assess extension to new manifold classes

### Pattern 3: Topological Quantum Computation
When designing topological quantum computing protocols:
1. Use skein module representations for qubit encoding
2. Apply quantum trace maps for state measurement
3. Leverage gluing module structure for gate operations

## Instructions for Agents

### Step 1: Identify the Mathematical Context
Determine if the problem involves:
- 3-manifold topology
- Skein theory / knot invariants
- Quantum deformation of algebraic structures
- Triangulation-based quantum computation

### Step 2: Apply the Trace Map Framework
1. Construct the skein module for the given triangulation
2. Define the quantum gluing module
3. Build the homomorphism between them
4. Verify it quantizes the classical trace map

### Step 3: Validate Against Existing Constructions
- Compare with GY (Garoufalidis-Yu) construction: should agree
- Compare with PP (Panitch-Park) construction: should extend it
- Check for new manifold class coverage

## Error Handling
### Construction Disagreement
If the third construction does not agree with GY:
- Review the skein relation conventions
- Check quantum parameter normalization
- Verify triangulation compatibility

### Extension Limitations
If the construction does not extend beyond PP:
- Analyze the boundary conditions
- Check for additional manifold constraints
- Consider alternative gluing module definitions

## Mathematical Framework
```
Skein Module(M) →[Quantum Trace]→ Quantum Gluing Module(M)
     ↓                                    ↓
Classical Trace →[Quantization]→ Quantum Trace (this paper)
```

The key innovation is the third construction that:
- Is equivalent to GY where both apply
- Extends PP to additional manifold classes
- Maintains the quantization relationship with classical trace

## Resources
- arXiv:2606.13268 — "On 3d Quantum Trace Maps" (math.GT, June 2026)
- Garoufalidis-Yu construction (reference construction)
- Panitch-Park construction (reference construction)

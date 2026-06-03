---
name: non-invertible-topological-order-analysis
description: Analysis methodology for non-invertible symmetry enriched topological orders (NI-SETO) using unitary fusion categories and anyon condensation. Combines category theory, topological quantum field theory, and string net models for quantum computing research.
category: quantum
tags: [quantum-physics, topology, category-theory, fusion-categories, quantum-computing, topological-order]
arxiv: "2605.28794"
created: "2026-05-30"
---

# Non-Invertible Topological Order Analysis

## When to use
- Analyzing non-invertible symmetry enriched topological phases
- Studying string net models with UFC (Unitary Fusion Category) structures
- Researching anyon condensation in topological quantum computing
- Investigating fusion category symmetries in quantum many-body systems
- Connecting category theory (math.CT, math.QA) with condensed matter physics

## Core Methodology

### 1. NI-SETO Definition Framework
Non-invertible symmetry enriched topological order (NI-SETO) extends traditional SETOs by replacing group symmetries with fusion category symmetries.

**Key steps:**
1. Identify the underlying unitary fusion category (UFC)
2. Construct the full inclusion of UFCs: $\mathcal{C} \subset \mathcal{D}$
3. Analyze anyon condensation channels
4. Characterize the relative braided fusion category structure

### 2. String Net Implementation
Two equivalent approaches:

**Approach A - UFC Full Inclusion:**
- Define input UFC $\mathcal{C}$ for the topological phase
- Construct full inclusion $\mathcal{C} \hookrightarrow \mathcal{D}$
- Derive the condensed phase via the inclusion
- Compute the Drinfeld center $Z(\mathcal{D})$

**Approach B - Anyon Condensation:**
- Start with parent topological order
- Identify condensable algebra object
- Perform condensation to obtain child phase
- Track symmetry action through condensation

### 3. Mathematical Tools

**Fusion Categories:**
- Simple objects = anyon types
- Fusion rules: $a \times b = \sum_c N_{ab}^c c$
- F-symbols: associativity constraints
- R-symbols: braiding data

**Key Invariants:**
- Global dimension: $\mathcal{D}^2 = \sum_a d_a^2$
- Topological spin: $\theta_a = e^{2\pi i h_a}$
- S-matrix: modular data

### 4. Computational Pipeline

```python
# Pseudocode for NI-SETO analysis
def analyze_ni_seto(ufc_data):
    # Step 1: Parse UFC data (fusion rules, F-symbols)
    fusion_rules = parse_fusion_rules(ufc_data)
    f_symbols = compute_f_symbols(ufc_data)
    
    # Step 2: Find condensable algebras
    condensable = find_condensable_algebras(fusion_rules)
    
    # Step 3: Construct full inclusions
    inclusions = build_full_inclusions(ufc_data, condensable)
    
    # Step 4: Compute Drinfeld center
    centers = [drinfeld_center(inc) for inc in inclusions]
    
    # Step 5: Extract physical predictions
    anyon_spectrum = extract_anyon_spectrum(centers)
    symmetry_actions = compute_symmetry_actions(centers)
    
    return {
        'anyon_spectrum': anyon_spectrum,
        'symmetry_actions': symmetry_actions,
        'topological_invariants': compute_invariants(centers)
    }
```

## Verification Steps
1. Check consistency of fusion rules (associativity)
2. Verify pentagon equation for F-symbols
3. Confirm hexagon equations for R-symbols
4. Validate modular S-matrix properties
5. Cross-check anyon condensation results

## Pitfalls
- Non-invertible symmetries don't form groups — avoid group-theoretic intuition
- UFC full inclusions require careful handling of tensor functor properties
- Anyon condensation may produce different phases depending on algebra choice
- String net Hamiltonians may have gapless boundaries not captured by bulk analysis

## References
- arXiv:2605.28794 — Non-invertible symmetry enriched string net topological orders
- Related skills: quantum-topological-data-analysis, topological-quantum-computing

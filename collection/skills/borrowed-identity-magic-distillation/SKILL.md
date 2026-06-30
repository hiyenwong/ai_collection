---
name: borrowed-identity-magic-distillation
description: "Methodology for magic-state distillation using borrowed-identity condition — a strictly weaker constraint than requiring transversal gates to act correctly on entire codespace, enabling unified numerical search across all Clifford hierarchy levels and multiple magic state types."
---

# Borrowed Identity Magic Distillation

## Description
Introduces the borrowed-identity condition for magic-state distillation, requiring only that the distillation circuit act as identity on a single input state rather than on the entire codespace. This strictly weaker condition applies uniformly across all Clifford hierarchy levels and unifies factories that distill different magic states (|T⟩, |CS⟩, |CCZ⟩). Brute-force search over borrowed-identity circuits with two-group symmetry recovers all known distance-2 factories and yields parent circuits encoding multiple factories.

## Activation Keywords
- borrowed identity magic state distillation
- 借用身份魔法态蒸馏
- magic state distillation factory search
- Clifford hierarchy distillation
- quantum error correction magic states
- 魔法态蒸馏工厂搜索

## Core Methodology

### Borrowed-Identity Condition
1. **Traditional constraint**: Transversal gate must act correctly on entire codespace
2. **Borrowed-identity condition**: Circuit acts as identity on a single input state
3. **Strength**: Strictly weaker → broader search space
4. **Uniformity**: Applies across all levels of Clifford hierarchy

### Factory Unification
1. **Single-level unification**: T, CS, CCZ factories unified within one search
2. **Parent circuits**: Encode multiple factories, output type chosen at compile time
3. **Beyond CSS codes**: Extends to synthillation and non-CSS catalytic factories

### Search Strategy
1. Brute-force search over borrowed-identity circuits
2. Two-group symmetry constraint for efficiency
3. Recover all known distance-2 factories within search range
4. Discover new parent circuits encoding multiple factory types

## Usage Patterns

### Pattern 1: Distillation Factory Design
When designing magic-state distillation factories:
1. Apply borrowed-identity condition instead of full codespace constraint
2. Search over circuits with appropriate symmetry group
3. Identify parent circuits that can distill multiple state types
4. Select output type at compile time rather than hard-coding

### Pattern 2: Search Space Reduction
When searching for new distillation protocols:
1. Use borrowed-identity condition to expand valid circuit space
2. Apply group symmetry to reduce search complexity
3. Verify recovered factories match known constructions
4. Explore beyond CSS code constructions

## Resources
- arXiv: 2606.28518 - "Borrowed Identities: Malleable Distillation Factories and a Unified Numerical Search"

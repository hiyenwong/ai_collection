# Lie Group Representation Theory

## Basic Concepts

### Lie Group

Group G that is also a smooth manifold:
- Group operations (multiplication, inversion) smooth
- Examples: GL(n), U(n), SO(n), Aff(V)

### Lie Algebra

Infinitesimal generators of Lie group:
```
g = {X : X = (d/dt)|_{t=0} exp(tX)}
```

Exponential map: exp: g → G

### Representation

Linear representation of G on Hilbert space H:
```
U: G → U(H)
U(g₁g₂) = U(g₁)U(g₂)
U(g)† = U(g)^{-1}
```

## Semidirect Products

### Definition

G = H ⋉ V where:
- H: Subgroup (e.g., GL(V))
- V: Normal subgroup (e.g., translations)
- Action: H acts on V

### Multiplication

```
(h₁, v₁)(h₂, v₂) = (h₁h₂, h₁·v₂ + v₁)
```

### Representations

**Mackey theory:**
1. Find irreducible representations of V (characters)
2. Study H-action on V-representations
3. Induce from stabilizer subgroups

## Examples

### Affine Group Aff(R)

G = GL(1, R) ⋉ R = {a, b : a ∈ R\{0\}, b ∈ R}

Irreducible representations:
- Dilations: U_a[f](x) = |a|^{-1/2} f(x/a)
- Translations: U_b[f](x) = f(x - b)
- Combined: U_{(a,b)}[f](x) = |a|^{-1/2} f((x-b)/a)

### Heisenberg Group

G = {(a, b, c) : a, b ∈ R, c ∈ U(1)}

Central extension of translation group:
```
U_{(a,b,c)} = exp(i a X) exp(i b P) exp(i c)
```

Commutation: exp(i a X) exp(i b P) = exp(i ab) exp(i b P) exp(i a X)

### Euclidean Group

E(n) = O(n) ⋉ R^n

Rotations + translations.

Irreducible representations: Characterized by momentum k ∈ R^n and angular momentum (spin).

## Haar Measure

### Left Haar Measure

Invariant under left multiplication:
```
∫_G f(g₁g) dg = ∫_G f(g) dg
```

### Right Haar Measure

Invariant under right multiplication:
```
∫_G f(gg₁) dg_R = ∫_G f(g) dg_R
```

### Modular Function

Relation between left and right measures:
```
dg_R = Δ(g) dg
Δ(g) = |det(Ad_g)|^{-1}
```

For non-unimodular groups (e.g., affine group): Δ ≠ 1

## Quantization and Representation

### Quantization as Representation

Quantization procedure:
```
Phase space function f → Operator A
```

Can be viewed as:
```
f: G → R  (function on group)
A = ∫_G f(g) U(g) dg  (quantized operator)
```

### Dequantization

Inverse: recover function from operator
```
f(g) = Tr[A U(g)†]
```

### Properties

1. **Linear**: Quantization preserves linear combinations
2. **Unitary**: Operators respect unitary structure
3. **Compatibility**: Group action commutes with quantization

## Applications

- **Signal processing**: Time-frequency analysis (affine group)
- **Quantum mechanics**: Phase space methods (Heisenberg group)
- **Harmonic analysis**: Fourier transforms on groups
- **Non-commutative geometry**: Quantization of symplectic manifolds

## References

- Mackey (1952): Induced representations
- Folland (1989): Harmonic analysis on phase space
- Taylor (1986): Non-commutative harmonic analysis
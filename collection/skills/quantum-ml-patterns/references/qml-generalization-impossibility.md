# No Reference-Free Generalization in QML — Impossibility Theorem

Based on arXiv: 2606.22331 (Jeongho Bang, 2026-06-21)

## Theorem
QML cannot generalize without a reference frame.

### Formal Statement
Let training states {|psi_i>} span a subspace S subset H. For any unitary U that acts as identity on S, the learned classifier f must satisfy f(U|phi>) = f(|phi>) for all |phi> in H.

### Corollary
If dim(S) < dim(H), exponentially many orthogonal states all receive the same prediction.

## What is NOT the problem
- NOT state discrimination (orthogonal states can be distinguished)
- NOT optimization difficulty
- NOT computational power limitation

## What IS the problem
Missing reference information. Hilbert-space dimension alone is NOT a learnable feature space.

## Required Operational Resources

1. **Feature Maps** — establish reference frame
2. **Measurement Bases** — define semantically meaningful directions
3. **Hamiltonians** — energy landscape structure
4. **Locality Constraints** — break global unitary symmetry
5. **Symmetry Priors** — constrain hypothesis space
6. **Diverse Training States** — span enough of Hilbert space

## Design Checklist
- [ ] What reference frame does feature map establish?
- [ ] Does training data span enough of Hilbert space?
- [ ] What symmetry priors do I have?
- [ ] Is measurement basis physically meaningful?
# Learning Conjecturing from Scratch

**arXiv ID:** 2503.01389
**Authors:** Thibault Gauthier, Josef Urban
**Published:** 2025-03-03T10:39:38Z
**Abstract:**
We develop a self-learning approach for conjecturing of induction predicates on a dataset of 16197 problems derived from the OEIS. These problems are hard for today's SMT and ATP systems because they require a combination of inductive and arithmetical reasoning.
  Starting from scratch, our approach consists of a feedback loop that iterates between (i) training a neural translator to learn the correspondence between the problems solved so far and the induction predicates useful for them, (ii) using the trained neural system to generate many new induction predicates for the problems, (iii) fast runs of the z3 prover attempting to prove the problems using the generated predicates, (iv) using heuristics such as predicate size and solution speed on the proved problems to choose the best predicates for the next iteration of training.
  The algorithm discovers on its own many interesting induction predicates, ultimately solving 5565 problems, compared to 2265 problems solved by CVC5, Vampire or Z3 in 60 seconds.

## Skill Description

This skill is generated from the arXiv paper: Learning Conjecturing from Scratch (2503.01389).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2503.01389](http://arxiv.org/abs/2503.01389v1)

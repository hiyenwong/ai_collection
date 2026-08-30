# An efficient nonconvex reformulation of stagewise convex optimization problems

**arXiv ID:** 2010.14322
**Authors:** Rudy Bunel, Oliver Hinder, Srinadh Bhojanapalli,  Krishnamurthy,  Dvijotham
**Published:** 2020-10-27T14:30:32Z
**Abstract:**
Convex optimization problems with staged structure appear in several contexts, including optimal control, verification of deep neural networks, and isotonic regression. Off-the-shelf solvers can solve these problems but may scale poorly. We develop a nonconvex reformulation designed to exploit this staged structure. Our reformulation has only simple bound constraints, enabling solution via projected gradient methods and their accelerated variants. The method automatically generates a sequence of primal and dual feasible solutions to the original convex problem, making optimality certification easy. We establish theoretical properties of the nonconvex formulation, showing that it is (almost) free of spurious local minima and has the same global optimum as the convex problem. We modify PGD to avoid spurious local minimizers so it always converges to the global minimizer. For neural network verification, our approach obtains small duality gaps in only a few gradient steps. Consequently, it can quickly solve large-scale verification problems faster than both off-the-shelf and specialized solvers.

## Skill Description

This skill is generated from the arXiv paper: An efficient nonconvex reformulation of stagewise convex optimization problems (2010.14322).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2010.14322](http://arxiv.org/abs/2010.14322v1)

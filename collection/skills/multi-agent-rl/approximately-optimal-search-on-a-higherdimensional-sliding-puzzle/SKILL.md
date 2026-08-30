# Approximately Optimal Search on a Higher-dimensional Sliding Puzzle

**arXiv ID:** 2412.01937
**Authors:** Nono SC Merleau, Miguel O'Malley, Érika Roldán, Sayan Mukherjee
**Published:** 2024-12-02T19:59:06Z
**Abstract:**
Higher-dimensional sliding puzzles are constructed on the vertices of a $d$-dimensional hypercube, where $2^d-l$ vertices are distinctly coloured. Rings with the same colours are initially set randomly on the vertices of the hypercube. The goal of the puzzle is to move each of the $2^d-l$ rings to pre-defined target vertices on the cube. In this setting, the $k$-rule constraint represents a generalisation of edge collision for the movement of colours between vertices, allowing movement only when a hypercube face of dimension $k$ containing a ring is completely free of other rings. Starting from an initial configuration, what is the minimum number of moves needed to make ring colours match the vertex colours? An algorithm that provides us with such a number is called God's algorithm. When such an algorithm exists, it does not have a polynomial time complexity, at least in the case of the 15-puzzle corresponding to $k=1$ in the cubical puzzle. This paper presents a comprehensive computational study of different scenarios of the higher-dimensional puzzle. A benchmark of three computational techniques, an exact algorithm (the A* search) and two approximately optimal search techniques (an evolutionary algorithm (EA) and reinforcement learning (RL)) is presented in this work. The experiments show that all three methods can successfully solve the puzzle of dimension three for different face dimensions and across various difficulty levels. When the dimension increases, the A* search fails, and RL and EA methods can still provide a generally acceptable solution, i.e. a distribution of a number of moves with a median value of less than $30$. Overall, the EA method consistently requires less computational time, while failing in most cases to minimise the number of moves for the puzzle dimensions $d=4$ and $d=5$.

## Skill Description

This skill is generated from the arXiv paper: Approximately Optimal Search on a Higher-dimensional Sliding Puzzle (2412.01937).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2412.01937](http://arxiv.org/abs/2412.01937v1)

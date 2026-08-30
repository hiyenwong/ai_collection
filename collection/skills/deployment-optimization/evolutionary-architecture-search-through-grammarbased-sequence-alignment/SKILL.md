# Evolutionary Architecture Search through Grammar-Based Sequence Alignment

**arXiv ID:** 2512.04992
**Authors:** Adri Gómez Martín, Felix Möller, Steven McDonagh, Monica Abella, Manuel Desco, Elliot J. Crowley, Aaron Klein, Linus Ericsson
**Published:** 2025-12-04T16:57:49Z
**Abstract:**
Neural architecture search (NAS) in expressive search spaces is a computationally hard problem, but it also holds the potential to automatically discover completely novel and performant architectures. To achieve this we need effective search algorithms that can identify powerful components and reuse them in new candidate architectures. In this paper, we introduce two adapted variants of the Smith-Waterman algorithm for local sequence alignment and use them to compute the edit distance in a grammar-based evolutionary architecture search. These algorithms enable us to efficiently calculate a distance metric for neural architectures and to generate a set of hybrid offspring from two parent models. This facilitates the deployment of crossover-based search heuristics, allows us to perform a thorough analysis on the architectural loss landscape, and track population diversity during search. We highlight how our method vastly improves computational complexity over previous work and enables us to efficiently compute shortest paths between architectures. When instantiating the crossover in evolutionary searches, we achieve competitive results, outperforming competing methods. Future work can build upon this new tool, discovering novel components that can be used more broadly across neural architecture design, and broadening its applications beyond NAS.

## Skill Description

This skill is generated from the arXiv paper: Evolutionary Architecture Search through Grammar-Based Sequence Alignment (2512.04992).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.04992](http://arxiv.org/abs/2512.04992v1)

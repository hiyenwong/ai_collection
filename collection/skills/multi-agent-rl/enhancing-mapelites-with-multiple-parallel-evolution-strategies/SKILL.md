# Enhancing MAP-Elites with Multiple Parallel Evolution Strategies

**arXiv ID:** 2303.06137
**Authors:** Manon Flageat, Bryan Lim, Antoine Cully
**Published:** 2023-03-10T18:55:02Z
**Abstract:**
With the development of fast and massively parallel evaluations in many domains, Quality-Diversity (QD) algorithms, that already proved promising in a large range of applications, have seen their potential multiplied. However, we have yet to understand how to best use a large number of evaluations as using them for random variations alone is not always effective. High-dimensional search spaces are a typical situation where random variations struggle to effectively search. Another situation is uncertain settings where solutions can appear better than they truly are and naively evaluating more solutions might mislead QD algorithms. In this work, we propose MAP-Elites-Multi-ES (MEMES), a novel QD algorithm based on Evolution Strategies (ES) designed to exploit fast parallel evaluations more effectively. MEMES maintains multiple (up to 100) simultaneous ES processes, each with its own independent objective and reset mechanism designed for QD optimisation, all on just a single GPU. We show that MEMES outperforms both gradient-based and mutation-based QD algorithms on black-box optimisation and QD-Reinforcement-Learning tasks, demonstrating its benefit across domains. Additionally, our approach outperforms sampling-based QD methods in uncertain domains when given the same evaluation budget. Overall, MEMES generates reproducible solutions that are high-performing and diverse through large-scale ES optimisation on easily accessible hardware.

## Skill Description

This skill is generated from the arXiv paper: Enhancing MAP-Elites with Multiple Parallel Evolution Strategies (2303.06137).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2303.06137](http://arxiv.org/abs/2303.06137v2)

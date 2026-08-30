# Towards Less Constrained Macro-Neural Architecture Search

**arXiv ID:** 2203.05508
**Authors:** Vasco Lopes, Luís A. Alexandre
**Published:** 2022-03-10T17:53:03Z
**Abstract:**
Networks found with Neural Architecture Search (NAS) achieve state-of-the-art performance in a variety of tasks, out-performing human-designed networks. However, most NAS methods heavily rely on human-defined assumptions that constrain the search: architecture's outer-skeletons, number of layers, parameter heuristics and search spaces. Additionally, common search spaces consist of repeatable modules (cells) instead of fully exploring the architecture's search space by designing entire architectures (macro-search). Imposing such constraints requires deep human expertise and restricts the search to pre-defined settings. In this paper, we propose LCMNAS, a method that pushes NAS to less constrained search spaces by performing macro-search without relying on pre-defined heuristics or bounded search spaces. LCMNAS introduces three components for the NAS pipeline: i) a method that leverages information about well-known architectures to autonomously generate complex search spaces based on Weighted Directed Graphs with hidden properties, ii) an evolutionary search strategy that generates complete architectures from scratch, and iii) a mixed-performance estimation approach that combines information about architectures at initialization stage and lower fidelity estimates to infer their trainability and capacity to model complex functions. We present experiments in 13 different data sets showing that LCMNAS is capable of generating both cell and macro-based architectures with minimal GPU computation and state-of-the-art results. More, we conduct extensive studies on the importance of different NAS components in both cell and macro-based settings. Code for reproducibility is public at https://github.com/VascoLopes/LCMNAS.

## Skill Description

This skill is generated from the arXiv paper: Towards Less Constrained Macro-Neural Architecture Search (2203.05508).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2203.05508](http://arxiv.org/abs/2203.05508v2)

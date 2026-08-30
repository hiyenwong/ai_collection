# Accelerating Training Speed of Tiny Recursive Models with Curriculum Guided Adaptive Recursion

**arXiv ID:** 2511.08653
**Authors:** Kaleem Ullah Qasim, Jiashu Zhang
**Published:** 2025-11-11T08:17:23Z
**Abstract:**
Background: Recursive reasoning models achieve strong performance through iterative refinement, allowing small networks to match large language models. However, training is computationally expensive, often requiring 36 GPU-hours for Sudoku extreme. Existing models use fixed recursion depth and uniform supervision weighting, leading to inefficient training. Objectives: We propose CGAR (Curriculum-Guided Adaptive Recursion), applying curriculum learning to architectural depth. CGAR introduces Progressive Depth Curriculum (PDC) to dynamically adjust recursion depth and Hierarchical Supervision Weighting (HSW) to apply exponentially decaying importance to supervision steps. Methods: PDC implements a three-stage schedule transitioning from shallow (2, 1) to full depth (6, 3) configurations, providing 41.4% FLOPs reduction. HSW applies exponential decay to supervision steps, achieving 40% gradient variance reduction and accelerated convergence. Results: On Sudoku-Extreme, CGAR achieves 1.71x training speedup (10.93 to 6.38 hours) with only a 0.63% accuracy drop (86.65% to 86.02%). PDC alone achieves 2.26x speedup with 85.47% accuracy, showing a Pareto improvement in efficiency and quality. HSW provides 1.61x speedup. CGAR-trained models show superior inference efficiency with 100% halting accuracy and 11% fewer reasoning steps. Conclusions: CGAR enables efficient training of recursive models on modest hardware. By treating depth as a scheduled parameter, it achieves substantial savings and prevents overfitting, making these models practical for neurosymbolic AI and program synthesis. https://github.com/Kaleemullahqasim/CGAR and huggingface.co/Kaleemullah/trm-cgar-sudoku.

## Skill Description

This skill is generated from the arXiv paper: Accelerating Training Speed of Tiny Recursive Models with Curriculum Guided Adaptive Recursion (2511.08653).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2511.08653](http://arxiv.org/abs/2511.08653v3)

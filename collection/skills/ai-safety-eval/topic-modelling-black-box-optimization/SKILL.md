# Topic Modelling Black Box Optimization

**arXiv ID:** 2512.16445
**Authors:** Roman Akramov, Artem Khamatullin, Svetlana Glazyrina, Maksim Kryzhanovskiy, Roman Ischenko
**Published:** 2025-12-18T12:00:24Z
**Abstract:**
Choosing the number of topics $T$ in Latent Dirichlet Allocation (LDA) is a key design decision that strongly affects both the statistical fit and interpretability of topic models. In this work, we formulate the selection of $T$ as a discrete black-box optimization problem, where each function evaluation corresponds to training an LDA model and measuring its validation perplexity. Under a fixed evaluation budget, we compare four families of optimizers: two hand-designed evolutionary methods - Genetic Algorithm (GA) and Evolution Strategy (ES) - and two learned, amortized approaches, Preferential Amortized Black-Box Optimization (PABBO) and Sharpness-Aware Black-Box Optimization (SABBO). Our experiments show that, while GA, ES, PABBO, and SABBO eventually reach a similar band of final perplexity, the amortized optimizers are substantially more sample- and time-efficient. SABBO typically identifies a near-optimal topic number after essentially a single evaluation, and PABBO finds competitive configurations within a few evaluations, whereas GA and ES require almost the full budget to approach the same region.

## Skill Description

This skill is generated from the arXiv paper: Topic Modelling Black Box Optimization (2512.16445).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2512.16445](http://arxiv.org/abs/2512.16445v1)

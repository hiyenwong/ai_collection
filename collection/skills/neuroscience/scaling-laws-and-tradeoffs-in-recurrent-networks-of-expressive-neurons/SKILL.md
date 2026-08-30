# Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons

**arXiv ID:** 2605.12049
**Authors:** Aaron Spieler, Georg Martius, Anna Levina
**Published:** 2026-05-12T12:29:33Z
**Abstract:**
Cortical neurons are complex, multi-timescale processors wired into recurrent circuits, shaped by long evolutionary pressure under stringent biological constraints. Mainstream machine learning, by contrast, predominantly builds models from extremely simple units, a default inherited from early neural-network theory. We treat this as a normative architectural question. How should one split a fixed parameter budget $P$ between the number of units $N$, per-unit effective complexity $k_e$, and per-unit connectivity $k_c$? What controls the optimal allocation? This calls for a model in which per-unit complexity can be tuned independently of width and connectivity. Accordingly, we introduce the ELM Network, whose recurrent layer is built from Expressive Leaky Memory (ELM) neurons, chosen to mirror functional components of cortical neurons. The architecture allows for individually adjusting $N$, $k_e$, and $k_c$ and trains stably across orders of magnitude in scale. We evaluate the model on two qualitatively different sequence benchmarks: the neuromorphic SHD-Adding task and Enwik8 character-level language modeling. Performance improves monotonically along each of the three axes individually. Under a fixed budget, a clear non-trivial optimum emerges in their tradeoff, and larger budgets favor both more and more complex neurons. A closed-form information-theoretic model captures these tradeoffs and attributes the diminishing returns at two ends to: per-neuron signal-to-noise saturation and across-neuron redundancy. A hyperparameter sweep spanning three orders of magnitude in trainable parameters traces a near-Pareto-frontier scaling law consistent with the framework. This suggests that the simple-unit default in ML is not obviously optimal once this tradeoff surface is probed, and offers a normative lens on cortex's reliance on complex spatio-temporal integrators.

## Skill Description

This skill is generated from the arXiv paper: Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons (2605.12049).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.12049](http://arxiv.org/abs/2605.12049v1)

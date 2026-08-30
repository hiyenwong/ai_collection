# Accurate deep learning sub-grid scale models for large eddy simulations

**arXiv ID:** 2307.10060
**Authors:** Rikhi Bose, Arunabha M. Roy
**Published:** 2023-07-19T15:30:06Z
**Abstract:**
We present two families of sub-grid scale (SGS) turbulence models developed for large-eddy simulation (LES) purposes. Their development required the formulation of physics-informed robust and efficient Deep Learning (DL) algorithms which, unlike state-of-the-art analytical modeling techniques can produce high-order complex non-linear relations between inputs and outputs. Explicit filtering of data from direct simulations of the canonical channel flow at two friction Reynolds numbers $Re_τ\approx 395$ and 590 provided accurate data for training and testing. The two sets of models use different network architectures. One of the architectures uses tensor basis neural networks (TBNN) and embeds the simplified analytical model form of the general effective-viscosity hypothesis, thus incorporating the Galilean, rotational and reflectional invariances. The other architecture is that of a relatively simple network, that is able to incorporate the Galilean invariance only. However, this simpler architecture has better feature extraction capacity owing to its ability to establish relations between and extract information from cross-components of the integrity basis tensors and the SGS stresses. Both sets of models are used to predict the SGS stresses for feature datasets generated with different filter widths, and at different Reynolds numbers. It is shown that due to the simpler model's better feature learning capabilities, it outperforms the invariance embedded model in statistical performance metrics. In a priori tests, both sets of models provide similar levels of dissipation and backscatter. Based on the test results, both sets of models should be usable in a posteriori actual LESs.

## Skill Description

This skill is generated from the arXiv paper: Accurate deep learning sub-grid scale models for large eddy simulations (2307.10060).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2307.10060](http://arxiv.org/abs/2307.10060v1)

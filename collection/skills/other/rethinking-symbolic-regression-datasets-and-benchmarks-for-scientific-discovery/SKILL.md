# Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery

**arXiv ID:** 2206.10540
**Authors:** Yoshitomo Matsubara, Naoya Chiba, Ryo Igarashi, Yoshitaka Ushiku
**Published:** 2022-06-21T17:15:45Z
**Abstract:**
This paper revisits datasets and evaluation criteria for Symbolic Regression (SR), specifically focused on its potential for scientific discovery. Focused on a set of formulas used in the existing datasets based on Feynman Lectures on Physics, we recreate 120 datasets to discuss the performance of symbolic regression for scientific discovery (SRSD). For each of the 120 SRSD datasets, we carefully review the properties of the formula and its variables to design reasonably realistic sampling ranges of values so that our new SRSD datasets can be used for evaluating the potential of SRSD such as whether or not an SR method can (re)discover physical laws from such datasets. We also create another 120 datasets that contain dummy variables to examine whether SR methods can choose necessary variables only. Besides, we propose to use normalized edit distances (NED) between a predicted equation and the true equation trees for addressing a critical issue that existing SR metrics are either binary or errors between the target values and an SR model's predicted values for a given input. We conduct benchmark experiments on our new SRSD datasets using various representative SR methods. The experimental results show that we provide a more realistic performance evaluation, and our user study shows that the NED correlates with human judges significantly more than an existing SR metric. We publish repositories of our code and 240 SRSD datasets.

## Skill Description

This skill is generated from the arXiv paper: Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery (2206.10540).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2206.10540](http://arxiv.org/abs/2206.10540v5)

# Bridging Models to Defend: A Population-Based Strategy for Robust Adversarial Defense

**arXiv ID:** 2303.10225
**Authors:** Ren Wang, Yuxuan Li, Can Chen, Dakuo Wang, Jinjun Xiong, Pin-Yu Chen, Sijia Liu, Mohammad Shahidehpour, Alfred Hero
**Published:** 2023-03-17T19:49:10Z
**Abstract:**
Adversarial robustness is a critical measure of a neural network's ability to withstand adversarial attacks at inference time. While robust training techniques have improved defenses against individual $\ell_p$-norm attacks (e.g., $\ell_2$ or $\ell_\infty$), models remain vulnerable to diversified $\ell_p$ perturbations. To address this challenge, we propose a novel Robust Mode Connectivity (RMC)-oriented adversarial defense framework comprising two population-based learning phases. In Phase I, RMC searches the parameter space between two pre-trained models to construct a continuous path containing models with high robustness against multiple $\ell_p$ attacks. To improve efficiency, we introduce a Self-Robust Mode Connectivity (SRMC) module that accelerates endpoint generation in RMC. Building on RMC, Phase II presents RMC-based optimization, where RMC modules are composed to further enhance diversified robustness. To increase Phase II efficiency, we propose Efficient Robust Mode Connectivity (ERMC), which leverages $\ell_1$- and $\ell_\infty$-adversarially trained models to achieve robustness across a broad range of $p$-norms. An ensemble strategy is employed to further boost ERMC's performance. Extensive experiments across diverse datasets and architectures demonstrate that our methods significantly improve robustness against $\ell_\infty$, $\ell_2$, $\ell_1$, and hybrid attacks. Code is available at https://github.com/wangren09/MCGR.

## Skill Description

This skill is generated from the arXiv paper: Bridging Models to Defend: A Population-Based Strategy for Robust Adversarial Defense (2303.10225).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2303.10225](http://arxiv.org/abs/2303.10225v2)

# PATE-AAE: Incorporating Adversarial Autoencoder into Private Aggregation of Teacher Ensembles for Spoken Command Classification

**arXiv ID:** 2104.01271
**Authors:** Chao-Han Huck Yang, Sabato Marco Siniscalchi, Chin-Hui Lee
**Published:** 2021-04-02T23:10:57Z
**Abstract:**
We propose using an adversarial autoencoder (AAE) to replace generative adversarial network (GAN) in the private aggregation of teacher ensembles (PATE), a solution for ensuring differential privacy in speech applications. The AAE architecture allows us to obtain good synthetic speech leveraging upon a discriminative training of latent vectors. Such synthetic speech is used to build a privacy-preserving classifier when non-sensitive data is not sufficiently available in the public domain. This classifier follows the PATE scheme that uses an ensemble of noisy outputs to label the synthetic samples and guarantee $\varepsilon$-differential privacy (DP) on its derived classifiers. Our proposed framework thus consists of an AAE-based generator and a PATE-based classifier (PATE-AAE). Evaluated on the Google Speech Commands Dataset Version II, the proposed PATE-AAE improves the average classification accuracy by +$2.11\%$ and +$6.60\%$, respectively, when compared with alternative privacy-preserving solutions, namely PATE-GAN and DP-GAN, while maintaining a strong level of privacy target at $\varepsilon$=0.01 with a fixed $δ$=10$^{-5}$.

## Skill Description

This skill is generated from the arXiv paper: PATE-AAE: Incorporating Adversarial Autoencoder into Private Aggregation of Teacher Ensembles for Spoken Command Classification (2104.01271).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2104.01271](http://arxiv.org/abs/2104.01271v2)

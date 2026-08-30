# Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering

**arXiv ID:** 2509.15810
**Authors:** Chen Wang, Yue-Jiao Gong, Zhiguang Cao, Zeyuan Ma
**Published:** 2025-09-19T09:37:48Z
**Abstract:**
To relieve intensive human-expertise required to design optimization algorithms, recent Meta-Black-Box Optimization (MetaBBO) researches leverage generalization strength of meta-learning to train neural network-based algorithm design policies over a predefined training problem set, which automates the adaptability of the low-level optimizers on unseen problem instances. Currently, a common training problem set choice in existing MetaBBOs is well-known benchmark suites CoCo-BBOB. Although such choice facilitates the MetaBBO's development, problem instances in CoCo-BBOB are more or less limited in diversity, raising the risk of overfitting of MetaBBOs, which might further results in poor generalization. In this paper, we propose an instance generation approach, termed as \textbf{LSRE}, which could generate diverse training problem instances for MetaBBOs to learn more generalizable policies. LSRE first trains an autoencoder which maps high-dimensional problem features into a 2-dimensional latent space. Uniform-grid sampling in this latent space leads to hidden representations of problem instances with sufficient diversity. By leveraging a genetic-programming approach to search function formulas with minimal L2-distance to these hidden representations, LSRE reverse engineers a diversified problem set, termed as \textbf{Diverse-BBO}. We validate the effectiveness of LSRE by training various MetaBBOs on Diverse-BBO and observe their generalization performances on either synthetic or realistic scenarios. Extensive experimental results underscore the superiority of Diverse-BBO to existing training set choices in MetaBBOs. Further ablation studies not only demonstrate the effectiveness of design choices in LSRE, but also reveal interesting insights on instance diversity and MetaBBO's generalization.

## Skill Description

This skill is generated from the arXiv paper: Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering (2509.15810).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2509.15810](http://arxiv.org/abs/2509.15810v2)

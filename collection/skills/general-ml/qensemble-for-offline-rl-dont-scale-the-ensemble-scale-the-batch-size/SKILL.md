# Q-Ensemble for Offline RL: Don't Scale the Ensemble, Scale the Batch Size

**arXiv ID:** 2211.11092
**Authors:** Alexander Nikulin, Vladislav Kurenkov, Denis Tarasov, Dmitry Akimov, Sergey Kolesnikov
**Published:** 2022-11-20T21:48:25Z
**Abstract:**
Training large neural networks is known to be time-consuming, with the learning duration taking days or even weeks. To address this problem, large-batch optimization was introduced. This approach demonstrated that scaling mini-batch sizes with appropriate learning rate adjustments can speed up the training process by orders of magnitude. While long training time was not typically a major issue for model-free deep offline RL algorithms, recently introduced Q-ensemble methods achieving state-of-the-art performance made this issue more relevant, notably extending the training duration. In this work, we demonstrate how this class of methods can benefit from large-batch optimization, which is commonly overlooked by the deep offline RL community. We show that scaling the mini-batch size and naively adjusting the learning rate allows for (1) a reduced size of the Q-ensemble, (2) stronger penalization of out-of-distribution actions, and (3) improved convergence time, effectively shortening training duration by 3-4x times on average.

## Skill Description

This skill is generated from the arXiv paper: Q-Ensemble for Offline RL: Don't Scale the Ensemble, Scale the Batch Size (2211.11092).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2211.11092](http://arxiv.org/abs/2211.11092v2)

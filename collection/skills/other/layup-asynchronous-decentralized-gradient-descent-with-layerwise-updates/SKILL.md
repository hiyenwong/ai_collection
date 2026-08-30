# LAYUP: Asynchronous decentralized gradient descent with LAYer-wise UPdates

**arXiv ID:** 2410.05985
**Authors:** Cabrel Teguemne Fokam, Marcel Nieveler, Lukas König, Khaleelulla Khan Nazeer, David Kappel, Anand Subramoney
**Published:** 2024-10-08T12:32:36Z
**Abstract:**
The increasing size of deep learning models has made distributed training across multiple devices essential. Synchronous, centralized methods incur large communication and synchronization overheads. Communication efficient algorithms can reduce these overheads, but often require extra buffers, remain sensitive to stragglers or parameter drift. We present LayUp, an asynchronous decentralized SGD method with layer-wise updates. LayUp asynchronously exchanges incremental layer-wise updates during backpropagation. It uses randomized gossip communication, enabling updates to be applied as soon as they are available without buffering. These design choices reduce parameter drift and improve robustness to stragglers. We establish a theoretical upper bound for the gradient bias introduced by layer-wise updates and prove convergence of LayUp. We empirically validate LayUp on vision and language modeling tasks, showing convergence up to ~32% faster in terms of wall-clock time compared to synchronous data parallel training and up to ~27% faster than comparable communication efficient algorithms while maintaining better task performance. This speed-up is partly due to higher model FLOPs utilization, as we demonstrate. By injecting delays into the communication between workers, we show that LayUp remains robust to stragglers while DDP and other methods degrade in performance. Overall, LayUp provides a novel practical, straggler-robust alternative for distributed training without sacrificing accuracy.

## Skill Description

This skill is generated from the arXiv paper: LAYUP: Asynchronous decentralized gradient descent with LAYer-wise UPdates (2410.05985).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2410.05985](http://arxiv.org/abs/2410.05985v4)

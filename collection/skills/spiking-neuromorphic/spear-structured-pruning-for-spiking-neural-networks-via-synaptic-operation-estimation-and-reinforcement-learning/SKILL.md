# SPEAR: Structured Pruning for Spiking Neural Networks via Synaptic Operation Estimation and Reinforcement Learning

**arXiv ID:** 2507.02945
**Authors:** Hui Xie, Yuhe Liu, Shaoqi Yang, Jinyang Guo, Yufei Guo, Yuqing Ma, Jiaxin Chen, Jiaheng Liu, Xianglong Liu
**Published:** 2025-06-28T15:21:05Z
**Abstract:**
While deep spiking neural networks (SNNs) demonstrate superior performance, their deployment on resource-constrained neuromorphic hardware still remains challenging. Network pruning offers a viable solution by reducing both parameters and synaptic operations (SynOps) to facilitate the edge deployment of SNNs, among which search-based pruning methods search for the SNNs structure after pruning. However, existing search-based methods fail to directly use SynOps as the constraint because it will dynamically change in the searching process, resulting in the final searched network violating the expected SynOps target. In this paper, we introduce a novel SNN pruning framework called SPEAR, which leverages reinforcement learning (RL) technique to directly use SynOps as the searching constraint. To avoid the violation of SynOps requirements, we first propose a SynOps prediction mechanism called LRE to accurately predict the final SynOps after search. Observing SynOps cannot be explicitly calculated and added to constrain the action in RL, we propose a novel reward called TAR to stabilize the searching. Extensive experiments show that our SPEAR framework can effectively compress SNN under specific SynOps constraint.

## Skill Description

This skill is generated from the arXiv paper: SPEAR: Structured Pruning for Spiking Neural Networks via Synaptic Operation Estimation and Reinforcement Learning (2507.02945).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2507.02945](http://arxiv.org/abs/2507.02945v1)

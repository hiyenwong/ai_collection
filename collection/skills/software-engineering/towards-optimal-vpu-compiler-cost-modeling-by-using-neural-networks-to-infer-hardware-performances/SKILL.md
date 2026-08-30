# Towards Optimal VPU Compiler Cost Modeling by using Neural Networks to Infer Hardware Performances

**arXiv ID:** 2205.04586
**Authors:** Ian Frederick Vigogne Goodbody Hunter, Alessandro Palla, Sebastian Eusebiu Nagy, Richard Richmond, Kyle McAdoo
**Published:** 2022-05-09T22:48:39Z
**Abstract:**
Calculating the most efficient schedule of work in a neural network compiler is a difficult task. There are many parameters to be accounted for that can positively or adversely affect that schedule depending on their configuration - How work is shared between distributed targets, the subdivision of tensors to fit in memory, toggling the enablement of optimizations, etc. Traditionally, neural network compilers determine how to set these values by building a graph of choices and choosing the path with minimal 'cost'. These choices and their corresponding costs are usually determined by an algorithm crafted by engineers with a deep knowledge of the target platform. However, when the amount of options available to a compiler is large, it is very difficult to ensure that these models consistently produce an optimal schedule for all scenarios, whilst still completing compilation in an acceptable timeframe. This paper presents 'VPUNN' - a neural network-based cost model trained on low-level task profiling that consistently outperforms the state-of-the-art cost modeling in Intel's line of VPU processors.

## Skill Description

This skill is generated from the arXiv paper: Towards Optimal VPU Compiler Cost Modeling by using Neural Networks to Infer Hardware Performances (2205.04586).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2205.04586](http://arxiv.org/abs/2205.04586v1)

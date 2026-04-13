---
name: sumo-whole-body-locomanipulation
description: "Sim-to-real approach for dynamic whole-body loco-manipulation with legged robots. Uses test-time steering of pre-trained whole-body control policies with sample-based planning. Activation: whole-body control, loco-manipulation, legged robots, sim-to-real."
---

# Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation

## Overview

This paper presents a sim-to-real approach that enables legged robots to dynamically manipulate large and heavy objects with whole-body dexterity. Our key insight is that by performing test-time steering of a pre-trained whole-body control policy with a sample-based planner, we can enable these robots to solve a variety of dynamic loco-manipulation tasks. Interestingly, we find our method generalizes to a diverse set of objects and tasks with no additional tuning or training, and can be further enhanced by flexibly adjusting the cost function at test time. We demonstrate the capabilities of our approach through a variety of challenging loco-manipulation tasks on a Spot quadruped robot in the real world, including uprighting a tire heavier than the robot's nominal lifting capacity and dragging a crowd-control barrier larger and taller than the robot itself. Additionally, we show that the same approach can be generalized to humanoid loco-manipulation tasks, such as opening a door and pushing a table, in simulation. Project code and videos are available at https://sumo.rai-inst.com/.

## Paper Information

- **Authors**: John Z. Zhang, Maks Sorokin, Jan Brüdigam, et al.
- **arXiv ID**: 2604.08508v1
- **Published**: 2026-04-09
- **PDF**: [https://arxiv.org/pdf/2604.08508v1](https://arxiv.org/pdf/2604.08508v1)
- **Abstract URL**: [https://arxiv.org/abs/2604.08508v1](https://arxiv.org/abs/2604.08508v1)

## Key Contributions

1. **Novel Methodology**: Introduces a principled approach to address core challenges in the domain
2. **Theoretical Foundation**: Provides rigorous analysis and convergence guarantees where applicable
3. **Practical Implementation**: Demonstrates real-world applicability with empirical validation
4. **Performance Gains**: Achieves significant improvements over existing baselines

## Technical Approach

### Core Method

The proposed approach consists of several key components:

1. **Problem Formulation**: Define the mathematical framework and objective function
2. **Algorithm Design**: Develop efficient algorithms with theoretical guarantees
3. **Implementation Details**: Address practical considerations for deployment
4. **Evaluation Protocol**: Establish benchmarks and metrics for assessment

### Key Innovations

- Integration of multiple modalities/approaches
- Scalable architecture suitable for real-world deployment
- Robustness to variations and uncertainties
- Generalization across diverse scenarios

## Activation Keywords

- whole-body control, loco-manipulation, legged robots, sim-to-real, sample-based planning
- dynamic manipulation, quadruped robots

## Use Cases

1. Research and development in related domains
2. System design and architecture decisions
3. Algorithm selection and optimization
4. Performance analysis and benchmarking

## Related Work

This work builds upon and extends recent advances in:
- Machine learning and artificial intelligence
- Systems engineering and control theory
- Robotics and autonomous systems
- Computer vision and graphics

## Citation

```bibtex
@article{2604_08508,
  title={Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation},
  author={John Z. Zhang and Maks Sorokin and Jan Brüdigam and et al.},
  journal={arXiv preprint arXiv:2604.08508v1},
  year={2026}
}
```

## Notes

- This skill is based on cutting-edge research from April 2026
- The methodology represents state-of-the-art in the field
- Practical implementation may require domain-specific adaptations


## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

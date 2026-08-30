# EOE: Evolutionary Optimization of Experts for Training Language Models

**arXiv ID:** 2509.24436
**Authors:** Yingshi Chen
**Published:** 2025-09-29T08:18:26Z
**Abstract:**
This paper presents an evolutionary framework for the training of large language models(LLM). The models are divided into several experts(sub-networks), which have the same structure but different parameter values. Only one expert is trained at each step. After the classical AdamW optimization, some evolutionary operators(crossover, PSO, and mutation) act on the tensor weights between the current expert and the best expert. So current expert would learn the experience of best expert. The direction of best expert would help current expert's loss decrease faster. Finally, only save the weight of the best expert. Experiments show that best expert would achieve nearly the same accuracy as the full model. This would greatly reduce the size of the model for inference. Since only one expert is trained at each step, the training needs much less memory and has much higher throughput. Experiments show that the throughput would accelerate more than ten times! Our source code is available. It's a pure c++/cu framework, which is suitable for easy deployment on PCs and edge computing devices.

## Skill Description

This skill is generated from the arXiv paper: EOE: Evolutionary Optimization of Experts for Training Language Models (2509.24436).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2509.24436](http://arxiv.org/abs/2509.24436v1)

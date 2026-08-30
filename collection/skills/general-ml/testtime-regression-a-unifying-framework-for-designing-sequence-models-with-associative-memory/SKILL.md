# Test-time regression: a unifying framework for designing sequence models with associative memory

**arXiv ID:** 2501.12352
**Authors:** Ke Alexander Wang, Jiaxin Shi, Emily B. Fox
**Published:** 2025-01-21T18:32:31Z
**Abstract:**
Sequence models lie at the heart of modern deep learning. However, rapid advancements have produced a diversity of seemingly unrelated architectures, such as Transformers and recurrent alternatives. In this paper, we introduce a unifying framework to understand and derive these sequence models, inspired by the empirical importance of associative recall, the capability to retrieve contextually relevant tokens. We formalize associative recall as a two-step process, memorization and retrieval, casting memorization as a regression problem. Layers that combine these two steps perform associative recall via ``test-time regression'' over its input tokens. Prominent layers, including linear attention, state-space models, fast-weight programmers, online learners, and softmax attention, arise as special cases defined by three design choices: the regression weights, the regressor function class, and the test-time optimization algorithm. Our approach clarifies how linear attention fails to capture inter-token correlations and offers a mathematical justification for the empirical effectiveness of query-key normalization in softmax attention. Further, it illuminates unexplored regions within the design space, which we use to derive novel higher-order generalizations of softmax attention. Beyond unification, our work bridges sequence modeling with classic regression methods, a field with extensive literature, paving the way for developing more powerful and theoretically principled architectures.

## Skill Description

This skill is generated from the arXiv paper: Test-time regression: a unifying framework for designing sequence models with associative memory (2501.12352).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2501.12352](http://arxiv.org/abs/2501.12352v3)

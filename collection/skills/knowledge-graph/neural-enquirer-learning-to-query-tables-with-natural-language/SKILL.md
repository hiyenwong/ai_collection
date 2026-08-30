# Neural Enquirer: Learning to Query Tables with Natural Language

**arXiv ID:** 1512.00965
**Authors:** Pengcheng Yin, Zhengdong Lu, Hang Li, Ben Kao
**Published:** 2015-12-03T06:46:27Z
**Abstract:**
We proposed Neural Enquirer as a neural network architecture to execute a natural language (NL) query on a knowledge-base (KB) for answers. Basically, Neural Enquirer finds the distributed representation of a query and then executes it on knowledge-base tables to obtain the answer as one of the values in the tables. Unlike similar efforts in end-to-end training of semantic parsers, Neural Enquirer is fully "neuralized": it not only gives distributional representation of the query and the knowledge-base, but also realizes the execution of compositional queries as a series of differentiable operations, with intermediate results (consisting of annotations of the tables at different levels) saved on multiple layers of memory. Neural Enquirer can be trained with gradient descent, with which not only the parameters of the controlling components and semantic parsing component, but also the embeddings of the tables and query words can be learned from scratch. The training can be done in an end-to-end fashion, but it can take stronger guidance, e.g., the step-by-step supervision for complicated queries, and benefit from it. Neural Enquirer is one step towards building neural network systems which seek to understand language by executing it on real-world. Our experiments show that Neural Enquirer can learn to execute fairly complicated NL queries on tables with rich structures.

## Skill Description

This skill is generated from the arXiv paper: Neural Enquirer: Learning to Query Tables with Natural Language (1512.00965).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1512.00965](http://arxiv.org/abs/1512.00965v2)

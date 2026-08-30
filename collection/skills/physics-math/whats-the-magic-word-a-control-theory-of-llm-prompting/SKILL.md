# What's the Magic Word? A Control Theory of LLM Prompting

**arXiv ID:** 2310.04444
**Authors:** Aman Bhargava, Cameron Witkowski, Shi-Zhuo Looi, Matt Thomson
**Published:** 2023-10-02T22:35:40Z
**Abstract:**
Prompt engineering is crucial for deploying LLMs but is poorly understood mathematically. We formalize LLM systems as a class of discrete stochastic dynamical systems to explore prompt engineering through the lens of control theory. We offer a mathematical analysis of the limitations on the controllability of self-attention as a function of the singular values of the parameter matrices. We present complementary empirical results on the controllability of a panel of LLMs, including Falcon-7b, Llama-7b, and Falcon-40b. Given initial state $\mathbf x_0$ from Wikitext and prompts of length $k \leq 10$ tokens, we find that the "correct" next token is reachable at least 97% of the time, and that the top 75 most likely next tokens are reachable at least 85% of the time. Intriguingly, short prompt sequences can dramatically alter the likelihood of specific outputs, even making the least likely tokens become the most likely ones. This control-theoretic analysis of LLMs demonstrates the significant and poorly understood role of input sequences in steering output probabilities, offering a foundational perspective for enhancing language model system capabilities.

## Skill Description

This skill is generated from the arXiv paper: What's the Magic Word? A Control Theory of LLM Prompting (2310.04444).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2310.04444](http://arxiv.org/abs/2310.04444v4)

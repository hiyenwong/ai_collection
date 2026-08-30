# Agent-GWO: Collaborative Agents for Dynamic Prompt Optimization in Large Language Models

**arXiv ID:** 2604.18612
**Authors:** Xudong Wang, Chaoning Zhang, Chenghao Li, Shuxu Chen, Qigan Sun, Jiaquan Zhang, Fachrina Dewi Puspitasari, Tae-Ho Kim, Jiwei Wei, Malu Zhang, Guoqing Wang, Yang Yang, Heng Tao Shen
**Published:** 2026-04-14T07:35:37Z
**Abstract:**
Large Language Models (LLMs) have demonstrated strong capabilities in complex reasoning tasks, while recent prompting strategies such as Chain-of-Thought (CoT) have further elevated their performance in handling complex logical problems. Despite these advances, high-quality reasoning remains heavily reliant on manual static prompts and is sensitive to decoding configurations and task distributions, leading to performance fluctuations and limited transferability. Existing automatic prompt optimization methods typically adopt single-agent local search, failing to simultaneously optimize prompts and decoding hyperparameters within a unified framework to achieve stable global improvements. To address this limitation, we propose Agent-GWO, a dynamic prompt optimization framework for complex reasoning. Specifically, we unify prompt templates and decoding hyperparameters as inheritable agent configurations. By leveraging the leader-follower mechanism of the Grey Wolf Optimizer (GWO), we automatically select three leader agents ($α$, $β$, and $δ$) to guide the collaborative updates of the remaining agents, enabling iterative convergence toward robust optimal reasoning configurations that can be seamlessly integrated for inference. Extensive experiments on multiple mathematical and hybrid reasoning benchmarks across diverse LLM backbones show that Agent-GWO consistently improves accuracy and stability over existing prompt optimization methods. The code will be released publicly.

## Skill Description

This skill is generated from the arXiv paper: Agent-GWO: Collaborative Agents for Dynamic Prompt Optimization in Large Language Models (2604.18612).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2604.18612](http://arxiv.org/abs/2604.18612v1)

# NNGPT: Rethinking AutoML with Large Language Models

**arXiv ID:** 2511.20333
**Authors:** Roman Kochnev, Waleed Khalid, Tolgay Atinc Uzun, Xi Zhang, Yashkumar Sanjaybhai Dhameliya, Furui Qin, Chandini Vysyaraju, Raghuvir Duvvuri, Avi Goyal, Dmitry Ignatov, Radu Timofte
**Published:** 2025-11-25T14:10:44Z
**Abstract:**
Building self-improving AI systems remains a fundamental challenge in the AI domain. We present NNGPT, an open-source framework that turns a large language model (LLM) into a self-improving AutoML engine for neural network development, primarily for computer vision. Unlike previous frameworks, NNGPT extends the dataset of neural networks by generating new models, enabling continuous fine-tuning of LLMs based on closed-loop system of generation, assessment, and self-improvement. It integrates within one unified workflow five synergistic LLM-based pipelines: zero-shot architecture synthesis, hyperparameter optimization (HPO), code-aware accuracy/early-stop prediction, retrieval-augmented synthesis of scope-closed PyTorch blocks (NN-RAG), and reinforcement learning. Built on the LEMUR dataset as an audited corpus with reproducible metrics, NNGPT emits from a single prompt and validates network architecture, preprocessing code, and hyperparameters, executes them end-to-end, and learns from result. The PyTorch adapter makes NNGPT framework-agnostic, enabling strong performance: NN-RAG achieves 73% executability on 1,289 targets, 3-shot prompting boosts accuracy on common datasets, and hash-based deduplication saves hundreds of runs. One-shot prediction matches search-based AutoML, reducing the need for numerous trials. HPO on LEMUR achieves RMSE 0.60, outperforming Optuna (0.64), while the code-aware predictor reaches RMSE 0.14 with Pearson r=0.78. The system has already generated over 5K validated models, proving NNGPT as an autonomous AutoML engine. Upon acceptance, the code, prompts, and checkpoints will be released for public access to enable reproducibility and facilitate community usage.

## Skill Description

This skill is generated from the arXiv paper: NNGPT: Rethinking AutoML with Large Language Models (2511.20333).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2511.20333](http://arxiv.org/abs/2511.20333v1)

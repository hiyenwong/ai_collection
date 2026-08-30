# Mutation Models: Learning to Generate Levels by Imitating Evolution

**arXiv ID:** 2206.05497
**Authors:** Ahmed Khalifa, Michael Cerny Green, Julian Togelius
**Published:** 2022-06-11T10:44:57Z
**Abstract:**
Search-based procedural content generation (PCG) is a well-known method for level generation in games. Its key advantage is that it is generic and able to satisfy functional constraints. However, due to the heavy computational costs to run these algorithms online, search-based PCG is rarely utilized for real-time generation. In this paper, we introduce mutation models, a new type of iterative level generator based on machine learning. We train a model to imitate the evolutionary process and use the trained model to generate levels. This trained model is able to modify noisy levels sequentially to create better levels without the need for a fitness function during inference. We evaluate our trained models on a 2D maze generation task. We compare several different versions of the method: training the models either at the end of evolution (normal evolution) or every 100 generations (assisted evolution) and using the model as a mutation function during evolution. Using the assisted evolution process, the final trained models are able to generate mazes with a success rate of 99% and high diversity of 86%. The trained model is many times faster than the evolutionary process it was trained on. This work opens the door to a new way of learning level generators guided by an evolutionary process, meaning automatic creation of generators with specifiable constraints and objectives that are fast enough for runtime deployment in games.

## Skill Description

This skill is generated from the arXiv paper: Mutation Models: Learning to Generate Levels by Imitating Evolution (2206.05497).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2206.05497](http://arxiv.org/abs/2206.05497v3)

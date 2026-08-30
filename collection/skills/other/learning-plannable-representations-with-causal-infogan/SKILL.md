# Learning Plannable Representations with Causal InfoGAN

**arXiv ID:** 1807.09341
**Authors:** Thanard Kurutach, Aviv Tamar, Ge Yang, Stuart Russell, Pieter Abbeel
**Published:** 2018-07-24T20:46:05Z
**Abstract:**
In recent years, deep generative models have been shown to 'imagine' convincing high-dimensional observations such as images, audio, and even video, learning directly from raw data. In this work, we ask how to imagine goal-directed visual plans -- a plausible sequence of observations that transition a dynamical system from its current configuration to a desired goal state, which can later be used as a reference trajectory for control. We focus on systems with high-dimensional observations, such as images, and propose an approach that naturally combines representation learning and planning. Our framework learns a generative model of sequential observations, where the generative process is induced by a transition in a low-dimensional planning model, and an additional noise. By maximizing the mutual information between the generated observations and the transition in the planning model, we obtain a low-dimensional representation that best explains the causal nature of the data. We structure the planning model to be compatible with efficient planning algorithms, and we propose several such models based on either discrete or continuous states. Finally, to generate a visual plan, we project the current and goal observations onto their respective states in the planning model, plan a trajectory, and then use the generative model to transform the trajectory to a sequence of observations. We demonstrate our method on imagining plausible visual plans of rope manipulation.

## Skill Description

This skill is generated from the arXiv paper: Learning Plannable Representations with Causal InfoGAN (1807.09341).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:1807.09341](http://arxiv.org/abs/1807.09341v1)

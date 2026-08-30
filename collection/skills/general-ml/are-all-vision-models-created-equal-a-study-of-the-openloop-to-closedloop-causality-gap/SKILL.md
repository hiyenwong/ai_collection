# Are All Vision Models Created Equal? A Study of the Open-Loop to Closed-Loop Causality Gap

**arXiv ID:** 2210.04303
**Authors:** Mathias Lechner, Ramin Hasani, Alexander Amini, Tsun-Hsuan Wang, Thomas A. Henzinger, Daniela Rus
**Published:** 2022-10-09T16:56:45Z
**Abstract:**
There is an ever-growing zoo of modern neural network models that can efficiently learn end-to-end control from visual observations. These advanced deep models, ranging from convolutional to patch-based networks, have been extensively tested on offline image classification and regression tasks. In this paper, we study these vision architectures with respect to the open-loop to closed-loop causality gap, i.e., offline training followed by an online closed-loop deployment. This causality gap typically emerges in robotics applications such as autonomous driving, where a network is trained to imitate the control commands of a human. In this setting, two situations arise: 1) Closed-loop testing in-distribution, where the test environment shares properties with those of offline training data. 2) Closed-loop testing under distribution shifts and out-of-distribution. Contrary to recently reported results, we show that under proper training guidelines, all vision models perform indistinguishably well on in-distribution deployment, resolving the causality gap. In situation 2, We observe that the causality gap disrupts performance regardless of the choice of the model architecture. Our results imply that the causality gap can be solved in situation one with our proposed training guideline with any modern network architecture, whereas achieving out-of-distribution generalization (situation two) requires further investigations, for instance, on data diversity rather than the model architecture.

## Skill Description

This skill is generated from the arXiv paper: Are All Vision Models Created Equal? A Study of the Open-Loop to Closed-Loop Causality Gap (2210.04303).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2210.04303](http://arxiv.org/abs/2210.04303v1)

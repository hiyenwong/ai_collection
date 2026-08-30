# Simple and complex spiking neurons: perspectives and analysis in a simple STDP scenario

**arXiv ID:** 2207.04881
**Authors:** Davide Liberato Manna, Alex Vicente Sola, Paul Kirkland, Trevor Bihl, Gaetano Di Caterina
**Published:** 2022-06-28T10:01:51Z
**Abstract:**
Spiking neural networks (SNNs) are largely inspired by biology and neuroscience and leverage ideas and theories to create fast and efficient learning systems. Spiking neuron models are adopted as core processing units in neuromorphic systems because they enable event-based processing. The integrate-and-fire (I&F) models are often adopted, with the simple Leaky I&F (LIF) being the most used. The reason for adopting such models is their efficiency and/or biological plausibility. Nevertheless, rigorous justification for adopting LIF over other neuron models for use in artificial learning systems has not yet been studied. This work considers various neuron models in the literature and then selects computational neuron models that are single-variable, efficient, and display different types of complexities. From this selection, we make a comparative study of three simple I&F neuron models, namely the LIF, the Quadratic I&F (QIF) and the Exponential I&F (EIF), to understand whether the use of more complex models increases the performance of the system and whether the choice of a neuron model can be directed by the task to be completed. Neuron models are tested within an SNN trained with Spike-Timing Dependent Plasticity (STDP) on a classification task on the N-MNIST and DVS Gestures datasets. Experimental results reveal that more complex neurons manifest the same ability as simpler ones to achieve high levels of accuracy on a simple dataset (N-MNIST), albeit requiring comparably more hyper-parameter tuning. However, when the data possess richer Spatio-temporal features, the QIF and EIF neuron models steadily achieve better results. This suggests that accurately selecting the model based on the richness of the feature spectrum of the data could improve the whole system's performance. Finally, the code implementing the spiking neurons in the SpykeTorch framework is made publicly available.

## Skill Description

This skill is generated from the arXiv paper: Simple and complex spiking neurons: perspectives and analysis in a simple STDP scenario (2207.04881).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2207.04881](http://arxiv.org/abs/2207.04881v1)

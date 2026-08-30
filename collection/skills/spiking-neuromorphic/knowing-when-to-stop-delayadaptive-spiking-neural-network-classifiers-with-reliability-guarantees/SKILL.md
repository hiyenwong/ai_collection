# Knowing When to Stop: Delay-Adaptive Spiking Neural Network Classifiers with Reliability Guarantees

**arXiv ID:** 2305.11322
**Authors:** Jiechen Chen, Sangwoo Park, Osvaldo Simeone
**Published:** 2023-05-18T22:11:04Z
**Abstract:**
Spiking neural networks (SNNs) process time-series data via internal event-driven neural dynamics. The energy consumption of an SNN depends on the number of spikes exchanged between neurons over the course of the input presentation. Typically, decisions are produced after the entire input sequence has been processed. This results in latency and energy consumption levels that are fairly uniform across inputs. However, as explored in recent work, SNNs can produce an early decision when the SNN model is sufficiently ``confident'', adapting delay and energy consumption to the difficulty of each example. Existing techniques are based on heuristic measures of confidence that do not provide reliability guarantees, potentially exiting too early. In this paper, we introduce a novel delay-adaptive SNN-based inference methodology that, wrapping around any pre-trained SNN classifier, provides guaranteed reliability for the decisions produced at input-dependent stopping times. The approach, dubbed SpikeCP, leverages tools from conformal prediction (CP). It entails minimal complexity increase as compared to the underlying SNN, requiring only additional thresholding and counting operations at run time. SpikeCP is also extended to integrate a CP-aware training phase that targets delay performance. Variants of CP based on alternative confidence correction schemes, from Bonferroni to Simes, are explored, and extensive experiments are described using the MNIST-DVS data set, DVS128 Gesture dataset, and CIFAR-10 dataset.

## Skill Description

This skill is generated from the arXiv paper: Knowing When to Stop: Delay-Adaptive Spiking Neural Network Classifiers with Reliability Guarantees (2305.11322).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2305.11322](http://arxiv.org/abs/2305.11322v4)

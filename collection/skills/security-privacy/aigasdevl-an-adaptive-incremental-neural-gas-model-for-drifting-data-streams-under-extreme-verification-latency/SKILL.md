# AiGAS-dEVL: An Adaptive Incremental Neural Gas Model for Drifting Data Streams under Extreme Verification Latency

**arXiv ID:** 2407.05379
**Authors:** Maria Arostegi, Miren Nekane Bilbao, Jesus L. Lobo, Javier Del Ser
**Published:** 2024-07-07T14:04:57Z
**Abstract:**
The ever-growing speed at which data are generated nowadays, together with the substantial cost of labeling processes cause Machine Learning models to face scenarios in which data are partially labeled. The extreme case where such a supervision is indefinitely unavailable is referred to as extreme verification latency. On the other hand, in streaming setups data flows are affected by exogenous factors that yield non-stationarities in the patterns (concept drift), compelling models learned incrementally from the data streams to adapt their modeled knowledge to the concepts within the stream. In this work we address the casuistry in which these two conditions occur together, by which adaptation mechanisms to accommodate drifts within the stream are challenged by the lack of supervision, requiring further mechanisms to track the evolution of concepts in the absence of verification. To this end we propose a novel approach, AiGAS-dEVL (Adaptive Incremental neural GAS model for drifting Streams under Extreme Verification Latency), which relies on growing neural gas to characterize the distributions of all concepts detected within the stream over time. Our approach exposes that the online analysis of the behavior of these prototypical points over time facilitates the definition of the evolution of concepts in the feature space, the detection of changes in their behavior, and the design of adaptation policies to mitigate the effect of such changes in the model. We assess the performance of AiGAS-dEVL over several synthetic datasets, comparing it to that of state-of-the-art approaches proposed in the recent past to tackle this stream learning setup. Our results reveal that AiGAS-dEVL performs competitively with respect to the rest of baselines, exhibiting a superior adaptability over several datasets in the benchmark while ensuring a simple and interpretable instance-based adaptation strategy.

## Skill Description

This skill is generated from the arXiv paper: AiGAS-dEVL: An Adaptive Incremental Neural Gas Model for Drifting Data Streams under Extreme Verification Latency (2407.05379).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2407.05379](http://arxiv.org/abs/2407.05379v1)

# Scalable Event-by-event Processing of Neuromorphic Sensory Signals With Deep State-Space Models

**arXiv ID:** 2404.18508
**Authors:** Mark Schöne, Neeraj Mohan Sushma, Jingyue Zhuge, Christian Mayr, Anand Subramoney, David Kappel
**Published:** 2024-04-29T08:50:27Z
**Abstract:**
Event-based sensors are well suited for real-time processing due to their fast response times and encoding of the sensory data as successive temporal differences. These and other valuable properties, such as a high dynamic range, are suppressed when the data is converted to a frame-based format. However, most current methods either collapse events into frames or cannot scale up when processing the event data directly event-by-event. In this work, we address the key challenges of scaling up event-by-event modeling of the long event streams emitted by such sensors, which is a particularly relevant problem for neuromorphic computing. While prior methods can process up to a few thousand time steps, our model, based on modern recurrent deep state-space models, scales to event streams of millions of events for both training and inference. We leverage their stable parameterization for learning long-range dependencies, parallelizability along the sequence dimension, and their ability to integrate asynchronous events effectively to scale them up to long event streams. We further augment these with novel event-centric techniques enabling our model to match or beat the state-of-the-art performance on several event stream benchmarks. In the Spiking Speech Commands task, we improve state-of-the-art by a large margin of 7.7% to 88.4%. On the DVS128-Gestures dataset, we achieve competitive results without using frames or convolutional neural networks. Our work demonstrates, for the first time, that it is possible to use fully event-based processing with purely recurrent networks to achieve state-of-the-art task performance in several event-based benchmarks.

## Skill Description

This skill is generated from the arXiv paper: Scalable Event-by-event Processing of Neuromorphic Sensory Signals With Deep State-Space Models (2404.18508).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2404.18508](http://arxiv.org/abs/2404.18508v3)

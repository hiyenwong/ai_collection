# CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras

**arXiv ID:** 2605.28387
**Authors:** Elvin Hajizada, Michael Neumeier, Edward Paxon Frady, Yulia Sandamirskaya, Axel von Arnim, Bing Li, Eyke Hüllermeier
**Published:** 2026-05-27T12:24:04Z
**Abstract:**
Recognizing and continuously learning novel human actions without forgetting prior classes is a requirement for emerging AR/VR and robotics applications. For these applications, both on-device processing and learning are essential for privacy and low-latency adaptation. Event cameras address the efficiency of visual sensing with sparse, asynchronous output that is naturally compatible with neuromorphic processing. Yet no prior system has deployed a continual on-device learning pipeline for event-based action recognition using neuromorphic hardware. We present CLANE, Continual Learning of Actions on Neuromorphic Hardware from Event Cameras, deployed end-to-end on Intel Loihi 2. CLANE combines a spiking 2D CNN for spatiotemporal feature extraction with CLP-SNN as its on-chip learning head, extended to action clips via a Temporal Aggregation Layer and a fixed-point Normalization Layer, both novel Loihi 2 modules. On THU E-ACT-50, a 50-class dataset captured under real-world conditions, CLANE achieves 70.4% accuracy in a continual learning task while delivering more than 100x energy reduction and 16x lower latency over a sequential CNN+GRU+CLP edge GPU baseline, validated through iso-algorithm cross-platform benchmarking across three evaluation levels.

## Skill Description

This skill is generated from the arXiv paper: CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras (2605.28387).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.28387](http://arxiv.org/abs/2605.28387v1)

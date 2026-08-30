# Active Spiking Perception: The Membrane Potential as a Belief State for Anytime 3D Point Cloud Recognition

**arXiv ID:** 2608.19232
**Authors:** Akarsh Jain, Arya Pawa, Ayush Debnath, Smera Rawal, Sayeed Shafayet Chowdhury
**Published:** 2026-08-04T17:40:08Z
**Abstract:**
Spiking point cloud networks usually scan space in a fixed, input-agnostic order, which leaves the most distinctive resource of spiking computation, the temporal evolution of the membrane potential, unused as a locus of decision-making. Active Spiking Perception (ASP) recasts 3D recognition as an iterative decision process in which the network's own leaky integrate-and-fire (LIF) membrane potential, read as a running belief over the class, selects the next chunk to observe and triggers confidence-margin early exit. A lightweight Slice-Selection Policy scores unvisited farthest-point-sampled chunks from the membrane state and precomputed geometric descriptors, trains end-to-end through a straight-through Gumbel-Softmax, reduces to an argmax at inference, and adds about 2% of backbone parameters. We prove that leaky integration is the recursive log-posterior update of a Bayesian filter, that the exit rule attains distribution-free selective risk with no multiple-testing penalty at the stopping time, and that streaming state carry-forward is exactly equivalent to prefix recomputation with bounded finite-precision drift. ASP reaches 90.62% and 93.28% on ModelNet40 and ModelNet10, 1.7 points below the strongest spiking baseline at a larger backbone, while adding a certified anytime interface no baseline offers. The mechanism transfers unchanged to dense prediction, giving 83.21 instance mIoU on ShapeNetPart and 48.50 mIoU on S3DIS Area 5, to our knowledge the first spiking results on S3DIS Area 5, and, fixation replacing chunk selection, to a foveated non-spiking transformer, so the policy is not tied to spiking backbones: cost is exactly linear in observations and the threshold is a measured compute dial spanning 2.8x to 1.35x less energy. One limitation is concrete: one S3DIS class is unidentifiable at the crop size we use, and we give the prediction that would fix it.

## Skill Description

This skill is generated from the arXiv paper: Active Spiking Perception: The Membrane Potential as a Belief State for Anytime 3D Point Cloud Recognition (2608.19232).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2608.19232](http://arxiv.org/abs/2608.19232v2)

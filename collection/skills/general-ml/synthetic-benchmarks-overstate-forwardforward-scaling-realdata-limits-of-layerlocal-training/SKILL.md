# Synthetic Benchmarks Overstate Forward-Forward Scaling: Real-Data Limits of Layer-Local Training

**arXiv ID:** 2606.06539
**Authors:** Yucheng Chen
**Published:** 2026-06-04T04:01:01Z
**Abstract:**
Forward-Forward (FF) learning [Hinton, 2022] replaces backpropagation with strictly layer-local goodness updates. Recent FF-CNN work has narrowed the gap to BP on 32x32 benchmarks, raising the question of whether layer-local training is becoming a viable alternative at realistic scale. To probe this rigorously, we develop DTG-FF -- dynamic temperature goodness, decoupled normalization, and multi-layer fusion -- as an instrument that sets FF-family state of the art across nine real-data benchmarks (91.8% CIFAR-10 and the first FF baseline at ImageNet-100 224x224), and use it to audit how far layer-local training actually scales.
  (1) Real-data scaling. Under identical recipe and backbone, an architecture-matched BP-DeepSup baseline beats DTG-FF by 2.40/5.93 pp on CIFAR-10/CIFAR-100, and the gap widens with class count. At 224x224 the same instrument reaches only 49.4% -- the first FF baseline at this scale, versus typical BP above 75% [Tian et al., 2020] -- exposing a real-data ceiling invisible at 32x32.
  (2) Synthetic vs. real K-conflict. DTG-FF increasingly outperforms BP as class count K grows on synthetic teacher-student tasks, yet on real images the FF-BP gap reverses sign and widens with K. A within-dataset CIFAR-100 coarse vs. fine probe isolates label-hierarchy from image distribution: synthetic K-sweeps confound output dimensionality with fine-grained discrimination difficulty and thereby overstate FF transferability.
  (3) Systems audit. FF can be implemented without storing depth-wide activations, but on commodity 8 GB hardware standard BP+gradient-accumulation reaches 4.18 GB / 157 imgs/s versus DTG-FF's 7.90 GB / 138 imgs/s, so a memory-based justification for FF at this scale is not supported under fair baselines.

## Skill Description

This skill is generated from the arXiv paper: Synthetic Benchmarks Overstate Forward-Forward Scaling: Real-Data Limits of Layer-Local Training (2606.06539).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2606.06539](http://arxiv.org/abs/2606.06539v1)

# EnforceSNN: Enabling Resilient and Energy-Efficient Spiking Neural Network Inference considering Approximate DRAMs for Embedded Systems

**arXiv ID:** 2304.04039
**Authors:** Rachmad Vidya Wicaksana Putra, Muhammad Abdullah Hanif, Muhammad Shafique
**Published:** 2023-04-08T15:15:11Z
**Abstract:**
Spiking Neural Networks (SNNs) have shown capabilities of achieving high accuracy under unsupervised settings and low operational power/energy due to their bio-plausible computations. Previous studies identified that DRAM-based off-chip memory accesses dominate the energy consumption of SNN processing. However, state-of-the-art works do not optimize the DRAM energy-per-access, thereby hindering the SNN-based systems from achieving further energy efficiency gains. To substantially reduce the DRAM energy-per-access, an effective solution is to decrease the DRAM supply voltage, but it may lead to errors in DRAM cells (i.e., so-called approximate DRAM). Towards this, we propose \textit{EnforceSNN}, a novel design framework that provides a solution for resilient and energy-efficient SNN inference using reduced-voltage DRAM for embedded systems. The key mechanisms of our EnforceSNN are: (1) employing quantized weights to reduce the DRAM access energy; (2) devising an efficient DRAM mapping policy to minimize the DRAM energy-per-access; (3) analyzing the SNN error tolerance to understand its accuracy profile considering different bit error rate (BER) values; (4) leveraging the information for developing an efficient fault-aware training (FAT) that considers different BER values and bit error locations in DRAM to improve the SNN error tolerance; and (5) developing an algorithm to select the SNN model that offers good trade-offs among accuracy, memory, and energy consumption. The experimental results show that our EnforceSNN maintains the accuracy (i.e., no accuracy loss for BER less-or-equal 10^-3) as compared to the baseline SNN with accurate DRAM, while achieving up to 84.9\% of DRAM energy saving and up to 4.1x speed-up of DRAM data throughput across different network sizes.

## Skill Description

This skill is generated from the arXiv paper: EnforceSNN: Enabling Resilient and Energy-Efficient Spiking Neural Network Inference considering Approximate DRAMs for Embedded Systems (2304.04039).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2304.04039](http://arxiv.org/abs/2304.04039v1)

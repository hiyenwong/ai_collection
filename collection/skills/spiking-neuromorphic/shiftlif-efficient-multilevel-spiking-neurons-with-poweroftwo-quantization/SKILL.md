# ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization

**arXiv ID:** 2605.01866
**Authors:** Kaiwen Tang, Di Yu, Jiaqi Zheng, Changze Lv, Qianhui Liu, Zhanglu Yan, Weng-Fai Wong
**Published:** 2026-05-03T13:20:53Z
**Abstract:**
Spiking neural networks (SNNs) are promising for edge sensing due to their event-driven computation and temporal filtering capability. However, standard leaky integrate-and-fire (LIF) neurons communicate only through binary spikes, which severely limit representational capacity. Existing multi-level spiking neurons improve information transmission, but often rely on uniform quantization that mismatches membrane-potential distributions or introduces costly synaptic multiplications. In this paper, we propose ShiftLIF, a multi-level spiking neuron that maps membrane potentials to a logarithmically spaced power-of-two spike set. This design provides finer representation in the small-amplitude regime, where membrane potentials are densely concentrated, while enabling multiplier-free synaptic computation through bit-shift and accumulation operations. As a result, ShiftLIF improves spike-level expressiveness without sacrificing the hardware-friendly nature of standard SNN computation. We evaluate ShiftLIF on 10 datasets spanning wireless, acoustic, motion, and visual sensing tasks. Results show that ShiftLIF consistently matches or exceeds the accuracy of existing multi-level spiking neurons while maintaining synaptic energy consumption close to standard binary LIF. These results indicate that ShiftLIF provides a favorable accuracy-efficiency trade-off for cross-modal edge sensing.

## Skill Description

This skill is generated from the arXiv paper: ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization (2605.01866).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.01866](http://arxiv.org/abs/2605.01866v1)

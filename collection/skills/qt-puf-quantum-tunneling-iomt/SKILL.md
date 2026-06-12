---
name: qt-puf-quantum-tunneling-iomt
description: "QT-PUF: Quantum tunneling leakage-based physical unclonable function for implantable IoMT devices. Gate leakage PUF using process-induced CMOS variations with differential readout circuit. Entropy 0.9999998, power 96.04 nW/bit. Use when designing quantum-inspired hardware security for medical devices, implantable IoMT authentication, ultralow-power PUF circuits, or CMOS process-variation-based cryptographic primitives."
category: quantum
tags: [quantum, iomt, puf, hardware-security, cmos, implantable-devices, tunneling-leakage]
arxiv_id: "2605.22113"
---

# QT-PUF: Quantum Tunneling Leakage-Based PUF for IoMT

## Description

Design and analyze quantum tunneling leakage-based physical unclonable functions (PUFs) for implantable Internet of Medical Things (IoMT) devices. Leverages quantum-mechanical gate leakage from process-induced variations in standard CMOS to generate unclonable device fingerprints. Achieves near-perfect entropy with ultralow power consumption suitable for implantable medical devices.

**Source**: arXiv:2605.22113 (Ma, Mohan, Chang — May 2026)

## Activation Keywords
- qt-puf
- quantum tunneling PUF
- implantable iomt security
- gate leakage PUF
- iomt device authentication
- quantum medical device security
- 量子隧穿 PUF
- 植入式医疗设备安全
- hardware security medical devices
- ultralow-power PUF

## Core Concepts

### Quantum Tunneling Leakage as Entropy Source
- **Mechanism**: Gate oxide tunneling current varies due to atomic-level process variations during CMOS fabrication
- **Quantum origin**: Tunneling probability is inherently quantum mechanical (Fowler-Nordheim or direct tunneling)
- **Unclonability**: Process variations are random and irreproducible, making each device unique
- **No excitation needed**: Operates under static bias — unlike RO or arbiter PUFs that need active oscillation

### Differential Readout Architecture
- **Pseudo-resistor I-to-V frontend**: Converts picoampere-level leakage currents to measurable voltages
- **Differential measurement**: Pair-wise comparison eliminates common-mode noise and environmental drift
- **Digital response**: Comparator outputs binary PUF response bits from differential voltage comparison

### Key Performance Metrics (65nm CMOS)
| Metric | Value | Significance |
|--------|-------|-------------|
| Entropy | 0.9999998 | Near-perfect randomness |
| FHD (Fractional Hamming Distance) | 0.5001 | Ideal inter-device uniqueness (target: 0.5) |
| Power | 96.04 nW/bit | Ultra-low for implantable devices |
| Energy | 19.21 fJ/bit | Extremely efficient per response bit |
| BER | < 0.000163 | Reliable across 1.0-1.3V, 10-70°C |
| Operating voltage | 0.9-1.3V | Compatible with implantable device power budgets |
| Operating temp | 0-100°C | Covers human body temp range |

## Usage Patterns

### Pattern 1: IoMT Device Authentication Design
1. Identify device trust requirements (implantable vs wearable)
2. Assess power budget constraints (nW-level for implantable)
3. Design gate-leakage PUF cell array with differential readout
4. Validate entropy and FHD through simulation/characterization
5. Implement challenge-response protocol for device authentication

### Pattern 2: PUF Selection for Medical Devices
1. Evaluate PUF candidates: memory-based, RO, arbiter, vs. tunneling-leakage
2. For ultralow-power implantable: prefer QT-PUF (no active excitation needed)
3. For higher-power wearable: RO/arbiter PUFs may suffice
4. Consider environmental stability (temperature, voltage variation)
5. Verify BER meets target (< 0.1% for clinical reliability)

### Pattern 3: Quantum-Inspired Security Analysis
1. Identify quantum mechanical effects in device behavior
2. Model tunneling current variations using quantum transport equations
3. Assess entropy source quality through statistical analysis
4. Compare against classical entropy sources (thermal noise, jitter)
5. Evaluate resistance to modeling attacks and side-channel analysis

## Implementation Guidelines

### QT-PUF Cell Design
```
CMOS Gate Structure → Tunneling Current (pA level)
                          ↓
              Pseudo-resistor I-to-V Converter
                          ↓
              Differential Amplifier (pair-wise)
                          ↓
              Comparator → Digital Response Bit
```

### Key Design Parameters
- **Transistor sizing**: Minimum-size devices maximize process variation effects
- **Pair matching**: Matched pairs for differential measurement improve stability
- **Readout sensitivity**: Pseudo-resistor values tuned for picoampere-level currents
- **Temperature compensation**: Differential architecture inherently compensates for drift

## Pitfalls
- **BER increases at voltage extremes**: Below 1.0V or above 1.3V, BER degrades significantly
- **Temperature limits**: Above 70°C, BER increases (though device survives to 100°C)
- **Aging effects**: Gate oxide degradation over time may shift leakage characteristics
- **Process node dependency**: 65nm has significant gate leakage; smaller nodes may have different behavior
- **Not suitable for high-throughput applications**: Static readout limits response generation speed

## Related Skills
- post-quantum-iot-healthcare (PQC migration for IoT healthcare systems)
- post-quantum-secure-pharmacovigilance (PQC for healthcare data pipelines)
- quantum-resistant-networks (post-quantum network architecture)

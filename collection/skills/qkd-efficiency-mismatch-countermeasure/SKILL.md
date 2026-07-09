---
name: qkd-efficiency-mismatch-countermeasure
description: "Practical countermeasure methodology against QKD attacks exploiting detection efficiency mismatch, including time-shift attacks. Uses temporal filtering and detector calibration to ensure uniform detection probability across all degrees of freedom, preventing eavesdropper from gaining information without detection. arXiv:2605.22580"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.22580"
  published: "2026-05-24"
  tags: [quantum-cryptography, QKD, security, detection-efficiency, time-shift-attack]
---

# QKD Detection Efficiency Mismatch Countermeasure

## Description

Practical methodology for defending Quantum Key Distribution (QKD) systems against attacks that exploit detection efficiency mismatch between receivers. The time-shift attack and broader class of detector-mismatch attacks allow an eavesdropper to selectively trigger detectors and gain partial key information without introducing detectable errors.

## Core Problem

QKD security proofs assume Bob's detectors respond identically to incoming photons. In practice, detector efficiency varies across temporal, spectral, and spatial degrees of freedom. An eavesdropper (Eve) exploits this by:

1. **Time-shift attack**: Shifting photon arrival times to favor one detector over another
2. **Spectral mismatch**: Exploiting wavelength-dependent efficiency differences
3. **Spatial mismatch**: Exploiting position-dependent detector response variations

Eve gains information about the raw key without increasing the quantum bit error rate (QBER) beyond normal thresholds.

## Countermeasure Methodology

### 1. Temporal Filtering

- **Principle**: Restrict detection to a narrow temporal window where all detectors have matched efficiency
- **Implementation**: Apply time gate that accepts photons only during the overlap region of detector response curves
- **Trade-off**: Reduces detection rate but eliminates temporal side-channel

### 2. Detector Characterization and Calibration

- Characterize efficiency curves for all detectors across relevant degrees of freedom (time, wavelength, spatial mode)
- Identify mismatch regions and establish safe operating parameters
- Regular recalibration to track detector drift over time

### 3. Efficiency Randomization

- Randomly vary detection parameters (bias voltage, timing offset) to prevent Eve from predicting optimal attack conditions
- Make the efficiency landscape unpredictable to an eavesdropper

### 4. Security Proof Adaptation

- Modify security proofs to account for residual mismatch after countermeasures
- Bound the information Eve can extract given the countermeasure effectiveness
- Use the worst-case mismatch to set conservative key rate bounds

## Key Findings

- Time-shift attacks are a special case of broader detection efficiency mismatch attacks
- Countermeasure based on temporal filtering restores security without requiring detector hardware changes
- The approach is practical and implementable with existing QKD systems
- Security can be proven under realistic assumptions about detector behavior

## Usage Patterns

### QKD System Security Audit
1. Characterize detector efficiency across all degrees of freedom
2. Identify mismatch regions that could be exploited
3. Apply temporal filtering to restrict detection to safe windows
4. Verify security under modified parameters

### Protocol Design
1. Design detection timing to minimize inherent mismatch
2. Build in regular calibration routines
3. Include efficiency monitoring as part of the QKD protocol
4. Adapt security proofs for residual mismatch

## Activation Keywords
- qkd detection efficiency
- time-shift attack countermeasure
- QKD security mismatch
- quantum key distribution hacking
- detector efficiency attack
- quantum hacking countermeasure
- QKD temporal filtering
- 量子密钥分发检测效率

## Pitfalls

- **Residual mismatch**: Even after countermeasures, small efficiency differences may remain — security proofs must account for worst-case residual
- **Calibration drift**: Detectors change over time; recalibration intervals must be set based on stability requirements
- **Key rate reduction**: Temporal filtering reduces detection rate, impacting secure key generation speed
- **Not all attacks covered**: This countermeasure targets efficiency mismatch; other QKD attacks (e.g., blinding, Trojan horse) require separate defenses

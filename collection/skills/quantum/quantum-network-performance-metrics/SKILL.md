---
name: quantum-network-performance-metrics
description: "Structured monitoring framework for quantum networks with standardized performance metrics including quality (entanglement fidelity, QBER), throughput/latency (entanglement rate, waiting time), timing (coincidence window, jitter), and exogenous factors (temperature, humidity, vibrations). Enables real-time observability, fault diagnosis, adaptive timing, and entanglement routing. Activation: quantum network monitoring, quantum network metrics, QBER monitoring, entanglement fidelity tracking, quantum network observability, quantum network performance."
metadata:
  arxiv_id: "2607.05642"
  published: "2026-07-09"
  authors: "Oak Ridge National Laboratory researchers"
  tags: [quantum, networking, systems-engineering, monitoring, performance]
---

# Quantum Network Performance Metrics

## Description

Structured monitoring framework for quantum networks enabling standardized performance metrics, real-time observability, fault diagnosis, and adaptive control. Moves quantum networks from experimental testbeds to production systems with measurable KPIs.

## Core Metrics Framework

### 1. Quality Metrics
- **Entanglement Fidelity**: Measure of how closely the distributed entangled state matches the ideal target state
- **QBER (Quantum Bit Error Rate)**: Error rate in transmitted quantum bits, directly impacts key rate in QKD
- **Loss**: Photon transmission loss across the quantum channel (dB)
- **Dark Count Rate**: Spurious detector events contributing to noise

### 2. Throughput and Latency Metrics
- **Entanglement Rate**: Rate at which entangled pairs are successfully distributed (pairs/second)
- **Waiting Time**: Time from entanglement request to successful distribution

### 3. Timing Metrics
- **Coincidence Window**: Time window for identifying correlated detection events
- **Production Jitter**: Variation in entanglement generation timing
- **Coincidence Jitter**: Variation in detection correlation timing

### 4. Exogenous Factors
- **Temperature**: Environmental temperature affecting fiber/optical components
- **Humidity**: Environmental humidity affecting optical coupling
- **Vibrations**: Mechanical vibrations affecting alignment and phase stability

## Usage Patterns

### Pattern 1: Real-Time Monitoring Setup
1. Deploy environmental sensors (temperature, humidity, vibration) alongside quantum network hardware
2. Configure non-invasive data collection to avoid perturbing quantum states
3. Set up alert thresholds for each metric based on system requirements
4. Implement automated log aggregation for post-hoc analysis

### Pattern 2: Fault Diagnosis
1. Correlate QBER spikes with environmental sensor data
2. Identify whether degradation is due to internal (detector drift, laser power) or external (vibration, temperature) factors
3. Use coincidence jitter analysis to diagnose timing synchronization issues

### Pattern 3: Adaptive Control
1. Feed monitoring data into entanglement routing algorithms
2. Dynamically adjust coincidence windows based on measured jitter
3. Route around high-loss segments identified through real-time fidelity monitoring

## Trade-offs

### Observability vs. Performance
- **Non-invasive monitoring**: Adds minimal overhead but limited detail
- **Active probing**: More detailed diagnostics but perturbs quantum states and reduces throughput
- **Recommendation**: Use non-invasive monitoring for production, active probing for maintenance windows

## Pitfalls

- **Metric correlation trap**: High QBER may correlate with temperature but be caused by a different factor (laser drift). Always verify root cause before acting.
- **Over-monitoring**: Too many concurrent monitoring processes can introduce noise and reduce entanglement rate. Balance observability needs with system performance.
- **Alert fatigue**: Set meaningful thresholds based on operational experience, not theoretical limits. Use rolling baselines that adapt to seasonal/environmental changes.
- **Missing exogenous factors**: Vibration and humidity are often overlooked but significantly affect optical alignment in long-duration deployments.

## Related Skills

- `quantum-network-routing` — entanglement routing decisions informed by performance metrics
- `quantum-network-task-control` — control plane for quantum network operations
- `distributed-quantum-computing` — distributed quantum computing infrastructure

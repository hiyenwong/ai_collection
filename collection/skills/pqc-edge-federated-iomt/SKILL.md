---
name: pqc-edge-federated-iomt
description: "Post-Quantum Cryptography (PQC) integration pattern for Federated Learning (FL) in Internet of Medical Things (IoMT) environments. Covers edge-native orchestration, PQC key establishment, distributed cryptographic processing, and Kubernetes-based scalable frameworks validated on resource-constrained hardware. Activation: post-quantum iomt, pqc federated learning, quantum-resistant healthcare, edge-native cryptography, medical device security, ml-kem ml-dsa healthcare, kubernetes iomt, distributed crypto processing"
metadata:
  arxiv_id: "2606.14515"
  published: "2026-06-12"
  authors: "Taym Alshoghri, Deemah H. Tashman, Mohammad Reza Gerami, Soumaya Cherkaoui"
  tags: ["post-quantum-cryptography", "federated-learning", "iomt", "edge-computing", "kubernetes", "medical-security"]
---

## Context

IoMT devices handle sensitive health data under strict resource constraints. Quantum computing threatens conventional lightweight cryptography. Federated Learning (FL) introduces additional privacy risks as model updates can leak private medical information. This paper presents a scalable Kubernetes-based framework integrating PQC into FL-enabled IoMT, validated on Raspberry Pi testbeds.

## Core Methodology

### 1. Threat Model
- **Primary threat**: Harvest-now-decrypt-later (HNDL) attacks on healthcare data
- **Secondary threat**: FL model update leakage exposing patient information
- **Constraint**: IoMT devices have limited CPU, memory, and battery

### 2. PQC Integration Architecture
- **PQC algorithms**: NIST-standard ML-KEM (key encapsulation) and ML-DSA (digital signatures)
- **Key establishment**: PQC replaces ECDH for session key negotiation between IoMT devices and edge orchestrator
- **Authentication**: ML-DSA signs FL model updates to prevent tampering
- **Encryption**: ML-KEM encrypts model gradients during transmission

### 3. Edge-Native Orchestration Pattern
- **Kubernetes-based** framework for distributed PQC processing
- **Distributed cryptographic processing** reduces latency vs sequential designs
- **Edge nodes** handle PQC operations, offloading from constrained IoMT devices
- **Scalable architecture**: New edge nodes auto-register and share crypto workload

### 4. Federated Learning Security Pipeline
```
IoMT Device → Local Training → Gradient Encryption (ML-KEM) → 
Edge Node → Gradient Aggregation → Model Update Signing (ML-DSA) → 
Orchestrator → Global Model → Redistribution
```

## Implementation Steps

1. Deploy Kubernetes cluster on edge hardware (validated on Raspberry Pi 4)
2. Install PQC library (liboqs or equivalent) on edge nodes
3. Configure FL server with PQC-authenticated channels
4. Deploy IoMT device agents with lightweight PQC client
5. Set up distributed crypto processing for parallel key establishment
6. Validate latency: distributed < sequential for >3 edge nodes
7. Monitor resource overhead: CPU, memory, network per node

## Key Findings

- **Distributed crypto processing** significantly reduces latency compared to sequential designs
- **Resource overhead** remains feasible on edge hardware (validated on Raspberry Pi)
- **Scalability**: Adding edge nodes linearly reduces crypto processing bottleneck
- **Privacy**: FL + PQC provides defense-in-depth against both classical and quantum threats

## Pitfalls

- **PQC key sizes**: ML-KEM-768 public keys ~1184 bytes, ciphertexts ~1088 bytes — much larger than ECDH. May impact IoMT bandwidth budgets
- **Edge node selection**: Not all edge hardware can handle PQC at scale — validate on target hardware
- **FL gradient leakage**: PQC encrypts in-transit data but does NOT prevent inference attacks on aggregated models — add differential privacy for full protection
- **Kubernetes overhead**: K8s adds resource overhead on edge — consider lightweight alternatives (k3s, k0s) for very constrained environments
- **Certificate management**: PQC certificates are larger — plan for storage and distribution at scale

## Verification

- Benchmark latency: distributed PQC vs sequential on target hardware
- Verify ML-KEM key establishment succeeds between all IoMT-edge pairs
- Confirm ML-DSA signature verification on FL model updates
- Measure resource usage (CPU%, memory MB, network bytes) per edge node
- Test scalability: add edge nodes and verify latency decreases

## Activation Keywords

- post-quantum iomt
- pqc federated learning
- quantum-resistant healthcare
- edge-native cryptography
- medical device security
- ml-kem healthcare
- ml-dsa authentication
- kubernetes iomt
- distributed crypto processing
- ioMT PQC
- FL security post-quantum

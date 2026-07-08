---
name: partially-blind-single-qubit-classification
description: "Partially-Blind Single-Qubit Classification (PB-SQC) methodology for quantum-secured delegated machine learning on untrusted quantum networks. Combines single-qubit classifiers with blind quantum computation to deliver privacy-preserving quantum ML classifications. Activation: partially-blind classification, PB-SQC, blind quantum classification, quantum-secured ML, delegated quantum computation, SQC with privacy"
metadata:
  arxiv_id: "2607.01998"
  published: "2026-07-02"
  authors: "Matteo Pasini, Tzula Benjamin Propp, Janice van Dam, et al."
  tags: [quantum-machine-learning, blind-quantum-computation, single-qubit-classifier, quantum-networks, delegated-computation]
---

# Partially-Blind Single-Qubit Classification (PB-SQC)

## Description

Methodology for partially-blind single-qubit classification (PB-SQC) — a hybrid quantum-classical ML framework where a server performs classification tasks for remote clients on an untrusted quantum network, while keeping the client's data and classification outcome information-theoretically hidden from the server.

## Activation Keywords

- partially-blind single-qubit classification
- PB-SQC
- blind quantum classification
- quantum-secured machine learning
- delegated quantum computation
- single-qubit classifier privacy
- SQC with BQC
- quantum network ML
- partially-blind quantum computation

## Core Concepts

### Single-Qubit Classifier (SQC)
Small-scale hybrid quantum-classical machine capable of binary classification using a single qubit. The classification is performed by encoding input data into qubit states, applying parameterized rotations, and measuring. SQCs are NISQ-friendly and can scale toward multi-qubit quantum classifiers (TQC = Two-Qubit Classifier).

### Blind Quantum Computation (BQC)
Protocol enabling a client to delegate quantum computation to an untrusted server while keeping input data, algorithm, and output information-theoretically secure. The server knows *that* computation is happening, but not *what* is being computed.

### Partially-Blind SQC (PB-SQC)
Novel intermediate protocol where:
- Server **knows**: a classification task is being performed
- Server **does NOT know**: the specific input data or classification outcome
- Achieved by encoding data in a way that hides individual samples while preserving classification utility
- Can be integrated into quantum networks for remote, quantum-secured ML services

## Methodology

### Step 1: Data Encoding for PB-SQC

1. Encode classical input features into qubit rotation angles
2. Apply BQC protocol to hide specific data values from server
3. Server prepares initial states without knowledge of encoded data
4. Client performs measurement basis selection to maintain privacy

### Step 2: Classification Circuit

1. Initialize qubit in server-prepared state (server-blind to data)
2. Apply parameterized rotations based on encoded features
3. Server executes circuit knowing only "classification" is happening
4. Client performs final measurement in chosen basis

### Step 3: Verification with TQC

- Upgrade from SQC (single-qubit) to TQC (two-qubit) to enable computation verification
- Second qubit acts as verification flag
- Client can detect if server deviated from protocol
- Trade-off: additional qubit cost vs. verifiability

### Step 4: Network Integration

- Embed PB-SQC in heterogeneous quantum network links
- Use entanglement swapping between server and client
- Client equipped with multiplexed solid-state quantum memory
- Enables remote quantum-secured classification services

## Usage Patterns

### Pattern 1: Privacy-Preserving Quantum Classification
When client needs ML classification on quantum hardware but cannot trust the server:
1. Encode data with BQC protection
2. Server executes PB-SQC circuit
3. Client measures and obtains classification
4. Server never sees data or result

### Pattern 2: Scalable Quantum ML Pipeline
Build toward genuine quantum advantage:
1. Start with SQC proof-of-principle
2. Scale to TQC for verification
3. Extend to multi-qubit quantum classifiers
4. Integrate into quantum network infrastructure

### Pattern 3: Quantum Network ML Service
Deliver ML as a quantum-secured network service:
1. Server hosts quantum classification hardware
2. Multiple clients connect via entanglement-swapped links
3. Each client gets private classification
4. Server only knows "classification was performed"

## Key Findings

- PB-SQC on real-world credit card fraud database approaches classical deep-belief network performance
- Two-qubit classifier (TQC) enables verification of delegated computation
- Framework tested with realistic hardware parameters in simulation
- Prototype experiment proposed for heterogeneous quantum network links

## Pitfalls

### NISQ Hardware Limitations
- SQCs work on current NISQ devices but have limited capacity
- Noise and decoherence affect classification accuracy
- TQC verification requires two entangled qubits — harder to maintain

### Partial vs. Full Blindness
- PB-SQC only hides data and outcome, NOT the fact that classification is happening
- Full BQC hides everything but requires more resources
- Choose based on threat model and resource constraints

### Scaling Challenges
- SQC → TQC → multi-qubit scaling is non-trivial
- Each additional qubit increases error rates exponentially on NISQ
- Network entanglement swapping adds latency and error

## Related Skills

- quantum-machine-learning (broader QML methodology)
- quantum-network-authentication (quantum network security)
- blind-quantum-computation (full BQC protocol)
- quantum-ml-data-loading (quantum data encoding)

## References

- arXiv: 2607.01998 — "Partially-Blind Single-Qubit Classification over a Prototype Hybrid Quantum Network"

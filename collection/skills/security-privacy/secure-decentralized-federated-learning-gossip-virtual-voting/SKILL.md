---
name: secure-decentralized-federated-learning-gossip-virtual-voting
description: "gspDAG-FL: secure decentralized federated learning via gossip and virtual voting. Derives consensus from gossip history, uses Hashgraph-style virtual voting on compact DAG. Byzantine resilience with payload validation and semantic audit. Activation: decentralized federated learning, gossip protocol, virtual voting, Byzantine resilience, ledger-assisted FL."
metadata:
  arxiv_id: "2607.08651"
  published: "2026-07-09"
  authors: "Amirhossein Taherpour, Xiaodong Wang"
  tags: [decentralized-federated-learning, gossip-protocol, virtual-voting, byzantine-resilience, ledger-assisted-fl]
---

# Secure Decentralized Federated Learning via Gossip and Virtual Voting

## Overview

gspDAG-FL is a secure decentralized federated learning framework that derives consensus from the same gossip history used to disseminate models. It eliminates the need for central servers or reintroduced global coordination structures while providing Byzantine resilience, provenance finality, and convergence guarantees.

## Key Innovations

### Gossip-Derived Consensus
- Nodes exchange model payloads only with neighbors
- Full nodes collect event certificates and receiver-endorsed accepted gossip proofs
- Reconstructs compact topology DAG for consensus
- No global coordination structures needed

### Hashgraph-Style Virtual Voting
- Full-node certificates via virtual voting on the DAG
- Finality over unique model-origin tuples, not identical local parameter states
- Avoids the settlement committee bottleneck of ledger-assisted FL

### Multi-Layer Resilience
- Payload validation: verify model update integrity
- Accepted-proof validation: verify gossip history correctness
- Private semantic audit: detect malicious model updates before aggregation

### Theoretical Guarantees
- Proved safety and conditional liveness of the control plane
- Convergence guarantee for certified perturbed gossip under time-varying effective mixing

## Methodology

1. **Gossip Dissemination**: Nodes exchange model payloads with neighbors
2. **Certificate Collection**: Full nodes collect event certificates and accepted proofs
3. **DAG Reconstruction**: Build compact topology DAG from certificates
4. **Virtual Voting**: Hashgraph-style voting for consensus finality
5. **Validation**: Payload, accepted-proof, and semantic audit before aggregation

## Implications

- Decentralized FL without central servers or blockchain committees
- Gossip-derived consensus eliminates coordination bottlenecks
- Multi-layer validation provides robust Byzantine defense
- Applicable to large-scale distributed ML deployments

## Pitfalls

- Gossip protocol latency may slow convergence on large networks
- Full-node requirements may create hierarchy in ostensibly peer-to-peer systems
- Semantic audit adds computational overhead
- Convergence guarantees assume certified perturbed gossip conditions

## Activation Keywords

decentralized federated learning, gossip protocol, virtual voting, Byzantine resilience, DAG consensus, gspDAG-FL, Hashgraph, ledger-assisted FL, peer-to-peer ML

## Paper Reference

arXiv:2607.08651 - "Secure Decentralized Federated Learning via Gossip and Virtual Voting" (Jul 2026)

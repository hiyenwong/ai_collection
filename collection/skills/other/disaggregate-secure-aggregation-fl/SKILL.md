---
name: disaggregate-secure-aggregation-fl
category: skills
description: "DisAgg protocol for efficient secure aggregation in federated learning using distributed aggregator committees, eliminating homomorphic encryption overhead while preserving privacy."
---

# DisAgg - Distributed Secure Aggregation for Federated Learning

## Trigger Words
secure aggregation federated learning, DisAgg, OPA private aggregation, secret sharing aggregation, federated learning privacy, dropout-tolerant FL

## Core Idea

Vanilla FL exposes client updates to the central server. Secure aggregation schemes protect privacy but suffer from communication rounds, heavy public-key ops, or dropout handling difficulty. DisAgg leverages a small committee of clients called Aggregators to perform aggregation itself, eliminating local masking and expensive homomorphic encryption.

## Key Patterns

### 1. Aggregator Committee Architecture
- Small committee of clients performs the aggregation instead of central server
- Each client secret-shares its update vector to Aggregators
- Aggregators locally compute partial sums and return aggregated shares
- Server reconstructs final result from aggregated shares only

### 2. Elimination of Cryptographic Overhead
- No local masking required on client side
- No expensive homomorphic encryption operations
- Reduced endpoint computation for both server and clients
- Privacy preserved against curious server and limited colluding clients

### 3. Optimal Communication-Computation Trade-offs
- Single server interaction per FL iteration (like OPA)
- Substantially lower cryptographic overhead
- Processes 100k-dimensional update vectors from 100k 5G clients
- 4.6x speedup compared to OPA (previous best protocol)

## When to Apply
- Federated learning with privacy requirements against honest-but-curious servers
- Large-scale FL deployments with many clients and high-dimensional models
- Scenarios where client dropouts are common
- When homomorphic encryption overhead is prohibitive

## Source
arXiv: 2605.13708v1 - "DisAgg: Distributed Aggregators for Efficient Secure Aggregation in Federated Learning"

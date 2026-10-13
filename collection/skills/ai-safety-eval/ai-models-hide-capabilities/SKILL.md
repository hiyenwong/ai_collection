---
name: ai-models-hide-capabilities
description: 'Proves AI models can provably hide arbitrary capabilities via encrypted backdoor networks. Use when evaluating capability elicitation limits and deployment safety under adversarial conditions.'
arxiv_id: '2610.13928'
utility: 0.86
authors: Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt
categories: [cs.LG, cs.CR]
tags: [ai-safety, capability-evaluation, backdoor, adversarial, deployment-safety]
---

# AI Models Can Provably Hide Arbitrary Capabilities

## Key Innovation

Constructs backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Hidden circuits remain provably hard to elicit and interpret under standard evaluation.

## Key Finding

Capability evaluations assume hidden capabilities can be elicited — this paper proves that assumption fails under adversarial conditions.

## Method

- Digital locker construction: encrypted subnetworks in weights
- Secret trigger mechanism for decryption/execution
- Formal proofs of elusiveness under standard evaluations
- Demonstrates fundamental limits of capability elicitation

## Results

- Provable hardness of eliciting hidden capabilities
- Hidden circuits invisible to standard interpretability tools
- Challenges fundamental assumption in AI safety evaluations

## Practical Use

- Understanding limits of pre-deployment capability evaluations
- Designing more robust safety assessment protocols
- Evaluating deployment risks under adversarial model providers

## URL

https://arxiv.org/abs/2610.13928

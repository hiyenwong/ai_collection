---
name: human-ai-quantum-co-discovery
description: Human-AI co-discovery methodology for quantum algorithm design. Based on arXiv:2606.24899 — case study of sign-embedding quantum algorithms for matrix equations and matrix functions.
category: quantum-ml
trigger_words: human-ai co-discovery, quantum algorithm design, sign-embedding, AIM system, matrix equations, quantum linear algebra
arxiv_id: 2606.24899v1
---

# Human-AI Co-Discovery of Quantum Algorithms

## Overview
Methodology for human-AI collaborative discovery in quantum algorithm design, demonstrated through the development of sign-embedding quantum algorithms for matrix equations and matrix functions — foundational primitives in quantum linear algebra and operator-output quantum algorithms.

## Core Workflow

### Stage 1: Human Intuition Seeding
- Start with a human-originated research intuition
- Example: "Rational approximation is especially effective for jump-type functions such as the sign function"
- This intuition becomes the design principle for quantum algorithms

### Stage 2: AI-Assisted Exploration
- AI system (e.g., AIM — agentic AI-mathematician) expands intuition into a route map
- Compare candidate formulations systematically
- Converge toward central framework (e.g., sign embedding)
- Connect known identities to wider classes of matrix equations and functions
- Draft proofs and complexity calculations

### Stage 3: Human Gating
- Human makes decisive scientific judgments:
  - Select which expanded routes are worth pursuing
  - Reject approaches with hidden conditions (e.g., Cayley-trapezoidal approximation)
  - Refine implementations (e.g., from coarse quadratic-gap query to factorized and scaled analysis)

## Key Insight
Human-AI co-discovery workflows are most valuable not as standalone theorem provers, but as **research partners** for:
1. Problem formation
2. Connection discovery
3. Derivation
4. Skeptical review inside a human-gated research loop

## Application to Quantum Algorithms
- Sign-embedding provides foundation for:
  - Matrix equation solvers
  - Matrix function evaluation
  - Quantum linear algebra primitives
  - Operator-output quantum algorithms

## When to Use
- Designing new quantum algorithms from mathematical intuition
- Exploring quantum linear algebra applications
- Human-AI collaborative mathematical discovery
- Quantum algorithm proof development

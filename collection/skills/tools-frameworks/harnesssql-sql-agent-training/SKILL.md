---
name: harnesssql-sql-agent-training
description: Use when training SQL agents in realistic database environments. Addresses train-deploy mismatch where execution harness is only introduced at deployment.
tags: [sql-agent, training, harness, database, train-deploy-mismatch, tool-use]
---

# HarnessSQL: SQL Agent Training

## Paper Metadata

- **arXiv ID**: 2610.12274
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.DB
- **Utility Score**: 0.88
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12274

## Key Contributions

- Addresses train-deploy mismatch: execution harness is typically only introduced at deployment
- Harness-native training: agents learn with the execution environment present during training
- Trains SQL agents in realistic database environments with actual execution feedback
- Shows that training with the harness improves deployment performance

## Core Methodology

HarnessSQL identifies a critical mismatch in SQL agent training: during training, agents typically learn from static datasets or simulated environments, but at deployment they must interact with a real execution harness (database connection, query executor, error handler). This gap between training and deployment conditions degrades real-world performance.

The solution is harness-native training: the execution harness is present during training, so the agent learns to generate SQL queries while receiving actual execution feedback (results, errors, schema information). This creates a tighter training signal that more accurately reflects deployment conditions.

The framework provides realistic database environments for training, including diverse schemas, data distributions, and error conditions. Agents trained this way learn not just to write syntactically correct SQL, but to write queries that work in practice — handling edge cases, optimizing for actual database performance, and recovering from execution errors.

## Relevance to tools-frameworks

Practical framework for SQL agent development: demonstrates that closing the train-deploy gap through harness-native training significantly improves real-world agent performance.

## Activation

sql-agent, training, harness, database, train-deploy-mismatch, tool-use

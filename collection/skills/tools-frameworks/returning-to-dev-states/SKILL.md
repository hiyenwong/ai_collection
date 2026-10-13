---
name: returning-to-dev-states
description: 'Go-Explore-style search over full sandbox snapshots for coding agent failure recovery. Use when coding agents need to recover from failures by branching from intermediate states.'
arxiv_id: '2610.13841'
utility: 0.85
authors: Daniel Thi Graviet, Tanmay Shah
categories: [cs.LG, cs.SE]
tags: [coding-agents, failure-recovery, sandbox, go-explore, search]
---

# Returning to Development States: Full Sandbox Snapshots for Coding Agents

## Key Innovation

Coding agents make useful progress before failing, but retry-from-scratch discards intermediate machine state. Implements Go-Explore-style search over full Daytona sandbox snapshots, branching from intermediate states that preserve meaningful progress.

## Method

- Full sandbox snapshots (not just code diffs)
- Go-Explore-style search over environment states
- Branching from intermediate states with progress
- Progress detection for identifying promising states

## Key Finding

Higher and more efficient solve rates depend mainly on progress preserved in intermediate states, not on the specific search strategy.

## Results

- Improved solve rates vs retry-from-scratch
- More efficient failure recovery
- Better utilization of partial progress

## Practical Use

- Building more resilient coding agents
- Designing failure recovery strategies
- Implementing sandbox-based agent architectures

## URL

https://arxiv.org/abs/2610.13841

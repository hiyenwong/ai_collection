---
name: humanize-olympiad-agents
description: 'Multi-session workflow for olympiad problem solving with Solve-Review-Wiki-Verify pipeline. Use when building robust multi-session agent workflows for long-horizon scientific tasks.'
arxiv_id: '2610.13632'
utility: 0.87
authors: Zhengyang Zhang, Jing Xiong, Hongzhou Lin, Juihui Chung, Zijian Zhang
categories: [cs.AI]
tags: [multi-session, olympiad, scientific-agents, workflow, robustness]
---

# Humanize Olympiad Agents: Multi-Session Workflow

## Key Innovation

Multi-session workflow addressing single-session brittleness: early errors propagate, missing knowledge stalls progress. Introduces Solve-Review-Wiki-Verify pipeline that mimics human collaborative research workflows.

## Method

- **Solve**: Initial problem attempt in isolated session
- **Review**: Cross-session review identifying errors/gaps
- **Wiki**: Knowledge accumulation across sessions
- **Verify**: Formal verification of solutions

## Architecture

- Multiple specialized agent sessions
- Knowledge persistence between sessions
- Error recovery via review mechanism
- Domain knowledge wiki for accumulated insights

## Results

- Overcomes single-session brittleness on hard problems
- Error propagation prevented by review step
- Knowledge accumulation enables harder problem solving

## Practical Use

- Building robust agents for scientific/mathematical tasks
- Multi-session workflow design patterns
- Knowledge accumulation in long-running agent systems

## URL

https://arxiv.org/abs/2610.13632

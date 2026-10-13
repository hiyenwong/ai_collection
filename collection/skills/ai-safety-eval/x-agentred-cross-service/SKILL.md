---
name: x-agentred-cross-service
description: 'X-AgentRed: Red-teaming personal agents in evolving multi-service ecosystems. Use when testing compositional failures across service boundaries in agent tool use.'
arxiv_id: '2610.13886'
utility: 0.85
authors: Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman
categories: [cs.AI]
tags: [red-teaming, personal-agents, cross-service, compositional-failures, safety]
---

# X-AgentRed: Red-Teaming Personal Agents in Multi-Service Ecosystems

## Key Innovation

Personal agents connect to services across web/applications via tools. As actions accumulate and interact across services, unintended harmful outcomes arise from benign requests. Systematically explores diverse cross-service paths to identify compositional failures.

## Problem

- Existing red-teaming: prompt LLMs to identify harmful paths from descriptions
- Or decompose specified harmful objectives into benign action combinations
- Neither captures emergent compositional failures across services

## Method

- Systematic exploration of cross-service action paths
- Evolving multi-service ecosystem simulation
- Detection of compositional failures from benign individual actions
- Scalable to large service ecosystems

## Results

- Identifies harmful compositions invisible to existing methods
- Scales to realistic multi-service agent deployments
- Reveals emergent safety risks in tool-using agents

## Practical Use

- Red-teaming personal assistant agents
- Testing safety of tool-using agent deployments
- Identifying compositional risks in multi-service systems

## URL

https://arxiv.org/abs/2610.13886

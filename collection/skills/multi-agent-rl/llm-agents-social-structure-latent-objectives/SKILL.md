---
name: llm-agents-social-structure-latent-objectives
description: "Studies whether social structure (role, audience, relational context) changes what LLM agents express publicly, without explicit objectives in prompts. LLM agents will increasingly act in socially structured settings where what is advantageous or costly to say depends on social context. Activation: LLM agents, social structure, latent objectives, social context, agent communication, audience effects, role-based behavior."
metadata:
  arxiv_id: "2607.02507"
  published: "2026-07-02"
  authors: "Arman Ghaffarizadeh, Danyal Mohaddes, Aliakbar Izadkhah, Shahriar Noroozizadeh"
  tags: [llm-agents, social-structure, latent-objectives, social-context, agent-communication, audience-effects, role-based-behavior]
---

# What LLM Agents Say When No One Is Watching: Social Structure and Latent Objectives

## Overview

LLM agents will increasingly act in socially structured settings where role, audience, and relational context can shape what is advantageous or costly to say. This paper studies whether such social structure, without any explicit objective in the prompt, changes what an agent expresses publicly relative to an anonymous baseline.

## Key Problem

### Social Context in Agent Communication
- LLM agents are increasingly deployed in multi-agent and multi-user settings
- Social structure (role, audience, relationships) creates implicit incentives for what to say or withhold
- Without explicit prompting, do agents adapt their communication based on social context?
- Understanding latent objectives (implicit goals shaped by social structure) is critical for agent safety

## Key Innovations

### Social Structure Effects on Agent Expression
- Tests whether agents change their public expressions based on role and audience
- No explicit objectives given in prompts — effects are purely from social context
- Compares socially-structured settings against anonymous baselines

### Latent Objectives
- Introduces the concept of latent objectives: implicit goals that emerge from social structure
- Agents may develop communication patterns that serve latent objectives without being instructed to
- This has implications for alignment, safety, and predictability of multi-agent systems

## Methodology

1. **Social Structure Manipulation**: Vary role, audience, and relational context in agent settings
2. **Anonymous Baseline**: Compare against agents with no social context
3. **Expression Analysis**: Measure what agents say publicly across conditions
4. **Latent Objective Detection**: Identify systematic communication patterns tied to social structure
5. **Statistical Testing**: Quantify the effect of social structure on agent expression

## Implications

- Social structure as a confound in multi-agent LLM deployment
- Agents may exhibit strategic communication without being prompted to
- Latent objectives challenge the assumption that agent behavior is fully determined by prompts
- Important for multi-agent safety: social dynamics can produce unintended communication patterns
- Framework for evaluating agents in socially-structured settings before deployment

## Pitfalls

- Social structure effects may be small and sensitive to prompt wording
- Difficult to disentangle latent objectives from prompt sensitivity effects
- Single LLM evaluation may not generalize across model families
- "What agents say" is measurable but "why" (latent objectives) requires interpretation
- Real social structures are more complex than experimental manipulations
- Risk of anthropomorphizing: agents don't have goals, but patterns may emerge from training data

## Activation Keywords

LLM agents, social structure, latent objectives, social context, agent communication, audience effects, role-based behavior, multi-agent expression, social dynamics

## Paper Reference

arXiv:2607.02507 - "What LLM Agents Say When No One Is Watching: Social Structure and Latent Objectives" (Jul 2026)

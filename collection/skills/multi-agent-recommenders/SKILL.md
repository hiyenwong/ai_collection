---
name: multi-agent-recommenders
description: 'Design and implement multi-agent recommender systems (MAVRS) with LLM-powered architectures. Use when building video/content recommender systems, implementing multi-agent coordination for recommendations, or designing explainable recommendation pipelines. Based on arXiv:2604.02211 - Multi-Agent Video Recommenders: Evolution, Patterns, and Open Challenges (WSDM 2026).'
---

# Multi-Agent Video Recommenders (MAVRS)

Design multi-agent architectures for video/content recommendation systems.

## Evolution of Recommender Systems

| Era | Approach | Limitation |
|-----|----------|------------|
| Traditional | Single-model, static metrics | Dynamic requirements unaddressed |
| MARL | Multi-agent RL (MMRF) | Coordination complexity |
| LLM-powered | MAVRS | Emerging, open challenges |

## MAVRS Architecture Components

Multi-agent recommender systems coordinate specialized agents:

### Agent Types

| Agent | Role |
|-------|------|
| Video Understanding | Parse content, extract features |
| Reasoning Agent | Generate recommendation logic |
| Memory Agent | Track user history, preferences |
| Feedback Agent | Process user signals, adapt |
| Explainability Agent | Generate recommendation explanations |

### Coordination Mechanisms

Agents coordinate through:
- **Shared memory**: User preferences, interaction history
- **Message passing**: Inter-agent communication
- **Voting/aggregation**: Combine agent outputs
- **Sequential pipeline**: Structured workflow

## Key Frameworks

### MMRF (Early MARL)
- Multi-agent reinforcement learning
- Agents learn coordination through rewards

### MACRec
- LLM-driven architecture
- Specialized agents for reasoning, memory, feedback

### Agent4Rec
- LLM-powered recommendations
- Explainability through agent roles

## Taxonomy of Collaborative Patterns

### Short-form Content
- Quick engagement optimization
- Real-time adaptation
- Virality prediction

### Long-form/Educational
- Engagement depth
- Learning progression
- Content understanding

### General Video
- Hybrid coordination
- Multi-objective optimization

## Open Challenges

1. **Scalability**: Coordination overhead at billions of users
2. **Multimodal understanding**: Video, audio, text integration
3. **Incentive alignment**: User satisfaction vs. platform metrics
4. **Lifelong personalization**: Continuous learning without forgetting
5. **Self-improvement**: Autonomous optimization from feedback

## Research Directions

- **Hybrid RL-LLM**: Combine MARL efficiency with LLM reasoning
- **Lifelong personalization**: Persistent learning across sessions
- **Self-improving systems**: Agents that optimize own performance

## When to Apply

- Building video/content recommender systems
- Implementing explainable recommendations
- Designing multi-agent coordination for user-facing systems
- Creating adaptive recommendation pipelines

## Paper Reference

arXiv:2604.02211 - "Multi-Agent Video Recommenders: Evolution, Patterns, and Open Challenges" (WSDM Companion 2026)
## Activation Keywords

- multi-agent-recommenders
- multi-agent-recommenders 技能
- multi-agent-recommenders skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply multi-agent-recommenders?

**Agent:** I'll help you understand and apply multi-agent-recommenders...

### Example 2: Advanced Application

**User:** What are the key considerations for multi-agent-recommenders?

**Agent:** Let me search for the latest research and best practices...

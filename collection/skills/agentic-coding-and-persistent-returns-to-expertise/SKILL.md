---
name: agentic-coding-and-persistent-returns-to-expertise
description: Analysis of ~400,000 Claude Code sessions showing domain expertise creates persistent returns in agentic coding performance, with expert users achieving 2-3x higher success rates and more efficient tool usage.
trigger_words:
- agentic coding
- persistent returns
- coding expertise
- Claude Code
- domain expertise
- coding agents
metadata:
  title: "Agentic coding and persistent returns to expertise"
  url: "https://www.anthropic.com/research/claude-code-expertise"
  date: "Jun 16, 2026"
  section: "publication"
  category: "Economic Research"
license: Complete terms in LICENSE.txt
---

# Agentic Coding And Persistent Returns To Expertise

## Overview

Based on Anthropic's analysis of approximately 400,000 Claude Code sessions from May-June 2026, this methodology reveals that domain expertise creates persistent returns in agentic coding performance. Expert users achieve significantly higher success rates and more efficient tool usage compared to non-experts.

## Key Findings

### 1. Persistent Returns to Expertise
- **Expert users** (defined by domain knowledge and coding experience) achieve **2-3x higher success rates** on complex coding tasks
- Performance gap **persists across task difficulty levels** - experts maintain advantage even on simple tasks
- **Domain-specific expertise matters**: Users with relevant domain knowledge outperform generalist coders
- **Tool proficiency correlates with expertise**: Experts use tools more effectively and efficiently

### 2. Behavioral Patterns of Expert Users
- **Better problem decomposition**: Experts break down complex problems into manageable subtasks
- **More effective tool selection**: Choose appropriate tools for specific subproblems
- **Efficient iteration cycles**: Shorter feedback loops with more targeted debugging
- **Strategic planning**: Spend more time upfront understanding requirements and constraints

### 3. Non-Expert User Challenges
- **Tool misuse**: Apply inappropriate tools or use them suboptimally
- **Shallow problem understanding**: Jump to implementation without proper analysis
- **Inefficient debugging**: Trial-and-error approaches rather than systematic diagnosis
- **Poor error recovery**: Struggle to recover from tool failures or unexpected outputs

## Methodology for Measuring Expertise Impact

### 1. Success Rate Metrics
- **Task completion rate**: Percentage of tasks successfully completed end-to-end
- **Code quality metrics**: Functionality, efficiency, maintainability, security
- **Time-to-completion**: Total time including planning, execution, and debugging phases
- **Tool usage efficiency**: Number of tool calls per successful outcome

### 2. Expertise Classification
- **Self-reported expertise**: User declarations of domain/coding proficiency
- **Behavioral indicators**: Problem decomposition quality, tool selection appropriateness
- **Historical performance**: Past success rates on similar tasks
- **Code artifact analysis**: Quality and sophistication of generated code

### 3. Controlled Experiment Design
- **Matched task pairs**: Same tasks assigned to expert vs. non-expert users
- **Blind evaluation**: Independent assessment of code quality and task completion
- **Longitudinal tracking**: Monitor user improvement over time and repeated interactions
- **A/B testing**: Different agent configurations tested against same user population

## Applications

### 1. Agent Design Optimization
- **Expert-adaptive interfaces**: Tailor agent behavior based on detected user expertise level
- **Scaffolding for novices**: Provide additional guidance and structure for less experienced users
- **Advanced capabilities for experts**: Enable power-user features and direct tool access
- **Dynamic difficulty adjustment**: Adapt task complexity based on user performance

### 2. Training Data Curation
- **Prioritize expert sessions**: Weight expert user interactions more heavily in training
- **Extract expert strategies**: Learn problem decomposition and tool usage patterns from experts
- **Synthetic expert data**: Generate training examples that mimic expert behavior
- **Error pattern analysis**: Understand and address common novice mistakes

### 3. User Experience Enhancement
- **Expertise detection**: Automatically identify user expertise level from initial interactions
- **Personalized assistance**: Adjust help level and intervention frequency based on expertise
- **Progressive disclosure**: Gradually reveal advanced features as user demonstrates competence
- **Performance feedback**: Provide targeted suggestions for improvement based on expertise gaps

## Implementation Guidelines

### Tools Required
- Session logging and analysis framework
- Code quality assessment toolkit
- User expertise classification model
- A/B testing infrastructure

### Best Practices
- Always validate expertise classifications with behavioral metrics
- Consider ethical implications of differential treatment based on expertise
- Maintain clear feedback mechanisms for users to improve their expertise
- Document limitations and uncertainty in expertise assessment

## Verification Steps
1. Reproduce basic expertise correlation findings on your own user base
2. Validate expertise classification accuracy against ground truth measures
3. Test agent adaptations against control conditions
4. Ensure findings generalize across different domains and task types

## Pitfalls to Avoid
- Over-relying on self-reported expertise without behavioral validation
- Creating overly rigid expertise categories that don't capture nuance
- Neglecting the potential for rapid expertise development during interactions
- Failing to account for domain-specific vs. general coding expertise differences
---
name: agentic-coding-expertise-framework
description: Framework for analyzing agentic coding sessions based on expertise levels, work modes, and success metrics. Shows domain expertise amplifies AI effectiveness more than coding proficiency.
trigger_words:
  - agentic coding
  - claude code
  - returns to expertise
  - coding agents
  - human-ai collaboration
---

# Agentic Coding Expertise Framework

Framework from Anthropic's "Agentic coding and persistent returns to expertise" research (Jun 16, 2026). Analyzes ~400,000 Claude Code sessions to understand how domain expertise, not coding proficiency, amplifies effective use of coding agents.

## Core Findings

### Division of Labor
- **Planning Decisions**: Humans make ~70% of planning decisions (what to do, approach, success criteria)
- **Execution Decisions**: AI makes ~80% of execution decisions (files to change, code to write, commands to run)
- **Clear Pattern**: People decide what to build, agent decides how to build it

### Expertise Impact
- **Task-Specific**: Expertise rating based on precision of directions, verification requests, and correction patterns
- **Output Amplification**: Expert sessions produce 5x more output per prompt (3,200 vs 600 words) and 2x more actions (12 vs 5)
- **Success Correlation**: Verified success rates: Novice (15%) → Intermediate (28-33%) → Expert (28-33%)
- **Recovery Ability**: Experts better recover from errors and misunderstandings

### Work Evolution
- **Debugging Decline**: Sessions spent fixing code fell from 33% to 19% over 7 months
- **End-to-End Growth**: Operating software (14%→21%), data analysis (~10%→20%), writing documents (~10%→20%)
- **Value Increase**: Average task value rose 27% across all work types

## Nine Work Modes Classification

### Code-Centric (56%)
1. **Building**: Creating new code/systems (25%)
2. **Fixing**: Repairing broken code (26%) 
3. **Testing**: Writing/running tests (part of 5%)
4. **Orchestrating**: Managing other agents/pipelines (part of 5%)

### Software Operations (17%)
5. **Operating**: Deploying, configuring, running, monitoring systems

### Planning & Understanding (14%)
6. **Understanding**: Exploring existing systems
7. **Planning**: Designing changes before implementation

### Non-Code Output (13%)
8. **Analyzing**: Data analysis and processing
9. **Communicating**: Presentations and prose documents

## User Classification Methodology

### Occupation Inference
- Uses project context, file structure, referenced artifacts, vocabulary
- Explicitly avoids treating coding as evidence of coding profession
- Maps to BLS Standard Occupational Classification (23 major groups)
- 70% of sessions successfully classified

### Top User Groups
1. Computer and Mathematical Occupations (software-related)
2. Business and Financial Operations  
3. Arts, Design, and Media
4. Management
5. Life, Physical, and Social Sciences

## Success Measurement Framework

### Judged Success
- Classifier reads full transcript to determine if user succeeded in their goal
- Categories: succeeded, partially succeeded, failed, no clear goal

### Verified Success  
- Requires both judged success AND verifiable evidence
- Evidence includes: git commits/pull requests, passing test suites, explicit user affirmation
- Failure signals: errors, failed tests, retries, user dissatisfaction

### Troubled Sessions Analysis
- **Hits Trouble**: Sessions with verified failure evidence
- **Abandoned**: Failed sessions with zero lines of code written
- **Recovery**: Troubled sessions that still achieve success

## Key Insights

### Domain Expertise > Coding Proficiency
- Success determined by problem understanding, not coding training
- Non-software occupations achieve similar success rates to software engineers (26% vs 30% verified success)
- All major occupations succeed at nearly same rate on coding tasks

### Persistent Returns to Expertise
- Gap largest between novice and intermediate users
- Modest gap between intermediate and expert users
- Expertise enables more autonomous agent activity per instruction

### Labor Market Implications
- Agents reward problem understanding over implementation skills
- Coding agents complement rather than substitute domain expertise
- More understanding → more quality work from agent

## Implementation Guidelines

### Session Analysis
1. Classify work mode using transcript + telemetry validation
2. Rate expertise on 5-point scale (novice to expert)
3. Measure actions/output per prompt
4. Apply success classification framework

### Agent Design Implications
- Support clear division between planning and execution
- Enable precise direction-giving for domain experts
- Provide robust error recovery mechanisms
- Facilitate end-to-end workflows beyond just coding

### Training Considerations
- Focus on understanding problem domains, not just coding syntax
- Develop expertise in specific application areas
- Learn to give precise, verifiable instructions
- Practice error identification and correction

## Limitations

- Privacy-preserving analysis limits detailed behavioral insights
- Success measures are transcript-based, not real-world outcomes
- Task value estimates are coarse approximations
- Sample limited to Claude Code users (may not generalize)

## References

- [Anthropic Research Report](https://www.anthropic.com/research/claude-code-expertise)
- [SWE-chat Dataset](https://github.com/princeton-nlp/SWE-bench)
- [METR Time-Horizon Evaluations](https://metr.org)

## Activation

Use when analyzing human-AI collaboration patterns, designing agentic coding interfaces, measuring expertise impact, or studying labor market effects of coding agents.
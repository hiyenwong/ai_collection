---
name: ai-safety-assessment-framework
description: "AI Safety assessment framework based on International AI Safety Report 2026. Use when analyzing AI system safety, evaluating risks of general-purpose AI, conducting AI safety assessments, or working with AI governance/policy frameworks. Covers capability evaluation, risk identification, safety measures, and policy recommendations."
---

# AI Safety Assessment Framework

基于 **International AI Safety Report 2026** 的 AI 安全评估框架。该报告由 Yoshua Bengio 主导，100+ AI 专家参与，30+ 国家和国际组织支持。

## Activation Keywords

- AI safety assessment
- AI 安全评估
- general-purpose AI risk
- AI capability evaluation
- AI governance
- AI policy framework
- International AI Safety Report
- AI 风险分析

## Tools Used

- exec: Run Python analysis scripts
- read: Read documentation and assessment templates
- write: Generate safety assessment reports

---

## Assessment Framework Structure

### 1. Capability Evaluation (能力评估)

评估 General-purpose AI 系统的核心能力维度：

| Dimension | Description | Indicators |
|-----------|-------------|------------|
| **Reasoning** | Logical inference, problem-solving | Accuracy, coherence, multi-step reasoning |
| **Knowledge** | World knowledge, domain expertise | Coverage, accuracy, update frequency |
| **Interaction** | Multi-turn dialogue, tool use | Context retention, tool invocation success rate |
| **Generation** | Content creation across modalities | Quality, diversity, coherence |
| **Agency** | Autonomous action, planning | Goal achievement, adaptability |

### 2. Risk Identification (风险识别)

按严重性和可能性评估风险：

| Risk Category | Examples | Severity Levels |
|---------------|----------|-----------------|
| **Harms from misuse** | Disinformation, cyberattacks, manipulation | Low → Critical |
| **Harms from malfunction** | Errors, bias, unpredictability | Low → Critical |
| **Systemic risks** | Market concentration, dependency, social impact | Medium → Critical |
| **Autonomy risks** | Loss of control, unexpected behavior | High → Critical |

### 3. Safety Measures (安全措施)

三层防护框架：

| Layer | Measures | Implementation |
|-------|----------|----------------|
| **Pre-deployment** | Training safety, alignment, red-teaming | Model development phase |
| **Deployment** | Access controls, monitoring, guardrails | Runtime safeguards |
| **Post-deployment** | Incident response, updates, oversight | Operational phase |

---

## Assessment Process

### Step 1: Define Scope

确定评估范围：
- AI system type (LLM, multimodal, agent, etc.)
- Deployment context (public API, enterprise, consumer product)
- Stakeholder interests (users, operators, regulators)

### Step 2: Capability Profile

创建能力档案：
```
System: [AI system name]
Type: [LLM/multimodal/agent/etc.]
Capabilities assessed:
  - Reasoning: [score/rating]
  - Knowledge: [score/rating]
  - Interaction: [score/rating]
  - Generation: [score/rating]
  - Agency: [score/rating]
```

### Step 3: Risk Matrix

填写风险矩阵：
```
| Risk | Likelihood | Severity | Priority |
|------|------------|----------|----------|
| [Risk 1] | [L/M/H] | [L/M/H/C] | [1-5] |
| [Risk 2] | ... | ... | ... |
```

### Step 4: Safety Gap Analysis

对比现有措施与风险：
```
Risk: [identified risk]
Current measures: [existing safeguards]
Gap: [missing measures]
Recommendation: [suggested improvements]
```

### Step 5: Generate Assessment Report

生成完整评估报告，包含：
- Executive Summary
- Capability Profile
- Risk Assessment Matrix
- Safety Measures Inventory
- Gap Analysis & Recommendations
- Governance Recommendations

---

## Key Concepts from Report 2026

### General-Purpose AI Definition

AI systems that can perform a wide range of tasks across domains, including:
- Text generation and analysis
- Image/video creation and understanding
- Code generation and debugging
- Tool use and agent behavior
- Multi-turn reasoning and planning

### Emerging Risks Highlighted

1. **AI Agents**: Autonomous systems with tool access
2. **Digital Infrastructure**: Integration with critical systems
3. **Tool Use**: Capability to invoke external APIs/services
4. **Social Manipulation**: Scale and personalization of influence

### Governance Frameworks

- National: Regulatory approaches, enforcement mechanisms
- International: Coordination, standards harmonization
- Corporate: Internal governance, responsible AI practices

---

## References

For detailed frameworks and templates, see:
- [risk-matrix-template.md](references/risk-matrix-template.md) - Risk assessment templates
- [capability-indicators.md](references/capability-indicators.md) - Detailed capability evaluation metrics
- [governance-checklist.md](references/governance-checklist.md) - Policy and governance checklist

---

## Related Skills

- **security-guardrails**: Output security and credential protection
- **openspec**: Specification-driven development with safety considerations
- **self-verification**: Verification and testing workflows

---

## Resources

- [International AI Safety Report 2026](https://internationalaisafetyreport.org)
- [arXiv:2602.21012](https://arxiv.org/abs/2602.21012)
- [AI Safety Summit Bletchley Park](https://www.gov.uk/government/publications/ai-safety-summit-bletchley-park-2023)
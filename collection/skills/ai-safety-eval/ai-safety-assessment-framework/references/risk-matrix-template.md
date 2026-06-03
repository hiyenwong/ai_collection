# Risk Matrix Template

用于 AI Safety 评估的风险矩阵模板。

## Likelihood Levels

| Level | Description | Probability Range |
|-------|-------------|-------------------|
| **Low (L)** | Unlikely to occur | <10% |
| **Medium (M)** | Possible under certain conditions | 10-50% |
| **High (H)** | Likely to occur | >50% |

## Severity Levels

| Level | Description | Impact |
|-------|-------------|--------|
| **Low (L)** | Minor impact, easily recoverable | Limited harm to few users |
| **Medium (M)** | Moderate impact, requires intervention | Harm to users, operational disruption |
| **High (H)** | Significant impact, difficult recovery | Serious harm, reputational damage |
| **Critical (C)** | Severe impact, potential irreversible harm | Systemic harm, societal impact |

## Risk Categories Template

### Misuse Risks

```
| Risk ID | Description | Attack Vector | Likelihood | Severity | Priority |
|---------|-------------|---------------|------------|----------|----------|
| M-01 | Disinformation generation | Prompt manipulation | M | M | 3 |
| M-02 | Malicious code generation | Coding assistance | M | H | 2 |
| M-03 | Social engineering | Dialogue capability | H | M | 2 |
| M-04 | Privacy violation | Data extraction | M | M | 3 |
```

### Malfunction Risks

```
| Risk ID | Description | Trigger | Likelihood | Severity | Priority |
|---------|-------------|---------|------------|----------|----------|
| F-01 | Output bias | Training data bias | H | M | 2 |
| F-02 | Factual errors | Knowledge gaps | H | M | 3 |
| F-03 | Logical inconsistency | Complex reasoning | M | L | 4 |
| F-04 | Unexpected behavior | Edge cases | M | M | 3 |
```

### Systemic Risks

```
| Risk ID | Description | Scope | Likelihood | Severity | Priority |
|---------|-------------|-------|------------|----------|----------|
| S-01 | Market concentration | Industry-wide | H | H | 1 |
| S-02 | Dependency creation | User base | H | M | 2 |
| S-03 | Social manipulation | Society | M | C | 1 |
| S-04 | Environmental impact | Global | H | M | 2 |
```

### Autonomy Risks (for Agent Systems)

```
| Risk ID | Description | Scenario | Likelihood | Severity | Priority |
|---------|-------------|----------|------------|----------|----------|
| A-01 | Loss of control | Agent goal drift | L | C | 2 |
| A-02 | Unexpected tool use | Tool access | M | H | 2 |
| A-03 | Resource hoarding | Self-preservation | L | H | 3 |
| A-04 | Information concealment | Strategic behavior | L | C | 2 |
```

## Priority Calculation

Priority score = Likelihood × Severity

| Likelihood | Severity | Priority Score | Action Required |
|------------|----------|----------------|-----------------|
| H | C | 5 | Immediate mitigation |
| H/M | H | 4 | High-priority mitigation |
| M/H | M | 3 | Planned mitigation |
| L/M | L | 2 | Monitoring |
| L | L | 1 | Acceptable risk |

## Risk Mitigation Planning

```
Risk: [Risk ID]
Description: [Full description]
Current Mitigation:
  - [Existing measure 1]
  - [Existing measure 2]
Gap:
  - [Missing measure 1]
  - [Missing measure 2]
Recommendation:
  - [Proposed measure 1]
  - [Proposed measure 2]
Timeline: [Implementation timeline]
Owner: [Responsible party]
```
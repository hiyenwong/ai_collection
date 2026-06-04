---
name: skill-drift-contract-violation
description: "Proactive maintenance for LLM agent skill libraries by treating skill drift as contract violation. Extracts executable environment contracts from skill documents and validates only role-bearing assumptions against live conditions. Use when: maintaining agent skill libraries, detecting API/dependency changes in reusable skills, reducing false-positive drift monitoring, building CI/CD for agent skill health, or repairing broken skills through contract-based localization. Keywords: skill drift, contract violation, agent skill maintenance, skill library decay, drift detection, precision-first maintenance, skill repair."
---

# Skill Drift as Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries

Based on: Fan, Tian, Li & Lu (2026). "Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries." arXiv:2605.10990.

## Problem

LLM agents rely on reusable skill libraries, but skills silently decay as external services, packages, APIs, and configurations evolve. Existing monitors detect changes at the wrong granularity — they observe values without understanding the **role** those values play in a skill. A version string in a comment is noise; the same string in a pinned dependency is an operational obligation.

## Core Innovation

Treat skill drift as **contract violation** rather than generic change detection. Extract **executable environment contracts** from skill documents and validate only **role-bearing assumptions** against known or live conditions. This turns noisy monitoring into a precision-first maintenance signal.

## Key Findings

- Contract-free CI probes produce **40% false positives**
- Contract-based approach raises **zero false alarms** over 599 no-drift and hard-negative cases (Wilson 95% CI [0, 0.6]%)
- Achieves **100% precision** and **76% recall** with strongest backbone in known-drift verification
- **86% conservative precision** in discovering live drift across 49 real skills
- Violated contracts make repair actionable: one-round success improved from **10%** without localization to **78%** with it

## Architecture Pattern

### Contract Extraction

1. **Identify role-bearing assumptions** in skill documents:
   - Pinned dependencies (e.g., `pip install pandas==2.1.0`)
   - Required API endpoints
   - Environment variable expectations
   - File path conventions
   - Tool version requirements

2. **Distinguish from noise**:
   - Version strings in comments → noise (not operational)
   - Version strings in dependency pins → contract (must be validated)
   - Example URLs → noise
   - Required service endpoints → contract

### Contract Validation

1. Parse skill document to extract contracts
2. Categorize by role: dependency, API, config, tool
3. Validate each contract type against its source:
   - Dependencies: check package registry for existence/version
   - APIs: probe endpoint for availability
   - Configs: verify environment state
   - Tools: check binary availability

### Drift Detection Pipeline

```
Skill Documents → Contract Extraction → Role Classification → Live Validation → Drift Report
```

### Repair Actionability

When a contract is violated:
1. **Localize the violation** to specific assumption
2. **Propose repair** based on current live state
3. **Apply and verify** the fix
4. **Update the skill** with corrected contract

## Implementation Guide

### Step 1: Contract Parser

```python
def extract_contracts(skill_md: str) -> list[Contract]:
    """Extract executable contracts from skill markdown."""
    contracts = []
    # Parse dependency pins
    for match in re.finditer(r'pip install ([\w\-]+)==([\d.]+)', skill_md):
        contracts.append(Contract(
            role="dependency",
            package=match.group(1),
            version=match.group(2),
            source="pypi"
        ))
    # Parse tool requirements
    for match in re.finditer(r'required: ([\w\-]+)', skill_md):
        contracts.append(Contract(
            role="tool",
            name=match.group(1),
            source="system"
        ))
    return contracts
```

### Step 2: Contract Validator

```python
def validate_contract(contract: Contract) -> ValidationResult:
    if contract.role == "dependency":
        return check_pypi(contract.package, contract.version)
    elif contract.role == "tool":
        return check_binary(contract.name)
    elif contract.role == "api":
        return probe_endpoint(contract.url)
    elif contract.role == "config":
        return check_env(contract.variable)
```

### Step 3: Drift Reporter

- Group violations by skill
- Provide severity classification
- Suggest specific repair actions
- Include confidence scores

## Benchmark

The authors release **SGDB**, an 880-pair benchmark dataset for skill degradation testing. Use this to evaluate your own drift detection approach.

## Best Practices

1. **Role-aware parsing**: Not every mention of a version is a contract
2. **Precision over recall**: False alarms waste more time than missed detections
3. **Actionable repair**: Localization enables one-round fixes
4. **Conservative precision**: In live detection, prefer missing drift over false alarms
5. **Contract freshness**: Update contracts when skills are intentionally modified

## Pitfalls

- Over-extracting contracts from non-operational text increases false positives
- API probing must respect rate limits and authentication
- Some contracts require external knowledge to determine current valid state
- Hard-negative cases (intentional version pins) must be handled carefully

## Activation

- skill drift detection
- skill library maintenance
- agent skill health monitoring
- contract-based drift
- skill decay prevention
- proactive skill maintenance
- skill repair automation

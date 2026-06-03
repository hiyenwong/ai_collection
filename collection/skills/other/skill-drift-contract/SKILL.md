---
name: skill-drift-contract
description: >
  Skill drift detection and contract-based maintenance for LLM agent skill libraries.
  Formulates skill drift as contract violation — extracts executable environment contracts
  from skill documents and validates role-bearing assumptions. Zero false alarms over 599
  no-drift cases. 100% precision, 76% recall on known-drift. Repair success 10%→78% with
  contract-based localization. Use when maintaining, updating, or auditing skill libraries,
  detecting when skills become outdated after environment changes, or proactively validating
  skill correctness. Trigger: skill drift, contract violation, skill maintenance, proactive
  skill audit, skill library maintenance, 技能漂移, 技能维护, skill contract validation.
---

# Skill Drift Is Contract Violation

## Overview

Skill drift occurs when a skill's assumed environment (tool behavior, API response format,
file paths, etc.) diverges from reality. This methodology formalizes drift as **contract
violation**: each skill implicitly encodes assumptions about its execution environment,
and when those assumptions break, the skill has "drifted."

## Core Methodology

### 1. Extract Environment Contracts

Each SKILL.md implicitly defines contracts — assumptions about:
- **Tool behavior**: What tools return, their output format
- **API signatures**: Endpoint URLs, response schemas, authentication
- **File paths**: Expected directory structures, config locations
- **System state**: OS version, installed packages, environment variables
- **Data formats**: Input/output schema expectations

Example contract extraction from a skill:
```
Skill: "docker container management"
Implicit contracts:
  - `docker` CLI is installed and accessible
  - Docker daemon is running
  - Container names follow pattern {project}-{env}
  - `docker ps` output includes STATUS column
```

### 2. Validate Contracts

Create executable checks for each contract:
```bash
# Tool existence
command -v docker || echo "CONTRACT VIOLATION: docker not found"

# API response format
curl -s https://api.example.com/health | jq -e '.status == "ok"' || echo "CONTRACT VIOLATION: API health check failed"

# File path existence
test -d /app/config || echo "CONTRACT VIOLATION: /app/config missing"
```

### 3. Classify Drift Type

| Drift Type | Description | Detection |
|------------|-------------|-----------|
| **API drift** | Endpoint/response schema changed | Contract check fails on API call |
| **Tool drift** | CLI tool behavior/output format changed | Command output no longer matches expected pattern |
| **Path drift** | File/directory moved or renamed | Path existence check fails |
| **Config drift** | Configuration values or format changed | Config parsing fails |
| **Dependency drift** | Required package/version unavailable | Import/install check fails |

### 4. Localize & Repair

When a contract violation is detected:
1. **Identify the violated contract** → which assumption broke
2. **Locate affected skill sections** → which parts of SKILL.md reference the broken assumption
3. **Determine repair strategy**:
   - **Update**: Patch the contract assumption (e.g., new API endpoint)
   - **Deprecate**: Mark skill as incompatible with current environment
   - **Adapt**: Add conditional logic for both old and new behavior

## Key Findings

- **Zero false alarms**: 599 no-drift cases correctly identified (0% false positive rate)
- **High precision**: 100% precision on known-drift detection
- **Recall**: 76% recall — catches most drift but misses some subtle cases
- **Repair success**: Contract-based localization improves repair success from 10% to 78%
- **SGDB benchmark**: 880 skill pairs evaluated for drift detection

## Activation Keywords
- skill drift
- contract violation
- skill maintenance
- proactive skill audit
- skill library maintenance
- skill validation
- environment contract
- 技能漂移
- 技能维护
- skill contract validation

## Tools Used
- **terminal**: Run contract validation checks
- **search_files**: Find skill files to audit
- **read_file**: Read SKILL.md for contract extraction
- **patch**: Apply contract-based repairs

## Proactive Maintenance Workflow

1. **Inventory**: List all skills in the library
2. **Extract contracts**: For each skill, identify implicit environment assumptions
3. **Validate**: Run contract checks against current environment
4. **Report**: Flag violated contracts with severity levels
5. **Repair**: Update affected skills using contract-based localization
6. **Verify**: Re-validate after repairs

## Integration with Hermes Agent

For Hermes Agent skill libraries:
- Run contract checks before/after system updates
- Monitor tool output changes that could indicate drift
- Track skill usage patterns — unused skills may drift unnoticed
- Schedule periodic audits using the contract validation framework

## Resources
- arXiv:2605.10990 — "Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries"
- SGDB benchmark dataset (880 skill pairs)

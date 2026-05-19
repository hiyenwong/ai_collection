---
name: neo-agentic-program-analysis
description: "Neo agentic program analysis framework for detecting privilege escalation in polyglot microservices. Combines LLM-based agents with classic program analysis for cross-service vulnerability detection across multiple languages. Uses dynamic analysis planning, adaptive code search primitives, and semantic validation. Use when: analyzing microservice security, detecting privilege escalation, performing agentic code analysis across polyglot codebases, building LLM-assisted program analysis tools, or evaluating cross-service vulnerability patterns."
---

# Neo — Agentic Program Analysis for Microservice Security

## Core Contribution

Neo is an **agentic program analysis framework** that combines LLM-based agents with classic program analysis to detect privilege escalation vulnerabilities in polyglot microservice architectures.

**Key insight**: LLMs alone lack semantic precision; classic program analysis lacks cross-service reasoning. Neo combines both through an agent that dynamically generates analysis plans, adapts code search strategies, and validates semantics.

## Architecture Pattern

```
┌─────────────┐
│ LLM Agent   │ ← Dynamically generates analysis plans
│  (Planner)  │    Adapts code search strategies
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌─────────────┐
│ Code Search │────▶│  Semantic   │
│  Primitives │     │ Validator   │
└─────────────┘     └─────────────┘
       │                    │
       ▼                    ▼
┌─────────────────────────────────┐
│  Cross-Service Analysis Engine  │
│  (Polyglot: 7 languages)        │
└─────────────────────────────────┘
```

## Code Search Primitives

The framework develops language-agnostic code search primitives that enable scalable and flexible code exploration across services and programming languages:

```python
class NeoAgent:
    def analyze_privilege_escalation(self, codebase):
        """Main analysis loop for privilege escalation detection."""
        # Step 1: Generate analysis plan
        plan = self.generate_analysis_plan(codebase)
        
        # Step 2: Cross-service exploration
        findings = []
        for service in codebase.services:
            # Search for privileged operations
            priv_ops = self.search_privileged_operations(service)
            
            # Search for permission checks
            perm_checks = self.search_permission_checks(service)
            
            # Cross-reference to find gaps
            gaps = self.find_permission_gaps(priv_ops, perm_checks)
            findings.extend(gaps)
        
        # Step 3: Semantic validation
        validated = self.validate_findings(findings, codebase)
        
        return validated
    
    def search_privileged_operations(self, service):
        """Find all privileged operations in a service."""
        return self.code_search(
            patterns=["admin", "sudo", "root", "superuser", "write", "delete"],
            context="function_declarations"
        )
    
    def search_permission_checks(self, service):
        """Find all permission checks in a service."""
        return self.code_search(
            patterns=["check_permission", "authorize", "has_role", "is_allowed"],
            context="function_calls"
        )
```

## Performance Results

- Evaluated on **25 open-source microservice applications**
- **7 programming languages**, **6.2 million lines of code**
- **24 zero-day privilege escalation vulnerabilities** discovered
- **81.0% precision**, **85.0% recall** on ground-truth dataset
- **18 additional zero-day vulnerabilities** in other domains

## Implementation Guidelines

1. **Start with analysis plan**: Let the LLM agent generate a structured plan before diving into code
2. **Use primitives**: Build language-agnostic code search primitives for scalability
3. **Cross-service analysis**: Trace privilege flows across service boundaries
4. **Validate semantically**: Use classic program analysis to validate LLM findings
5. **Iterate**: Refine analysis based on validation results

## Key Patterns

- **Dynamic Analysis Planning**: LLM generates context-aware analysis plans
- **Adaptive Code Search**: Search strategies adapt based on findings
- **Semantic Validation**: Classic program analysis validates LLM outputs
- **Polyglot Support**: Framework works across multiple programming languages
- **Extensibility**: Can be applied to other vulnerability types and domains

## Activation Keywords

- neo analysis, agentic program analysis, privilege escalation detection
- microservice security analysis, polyglot vulnerability detection
- LLM-assisted code analysis, cross-service security analysis
- agentic vulnerability scanner, semantic code validation

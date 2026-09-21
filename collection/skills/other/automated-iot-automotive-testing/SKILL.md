---
name: automated-iot-automotive-testing
description: "Deployment-aware testing for IoT automotive applications."
---

## Use when

You need to implement automated testing for IoT-based automotive applications with distributed deployment across geographically separated cyber-physical and IoT infrastructures, or when combining requirement-driven test generation with LLM/VLM assistance.

## Core Methodology

### Problem Context
Testing embedded software in modern vehicles is challenging due to system complexity, decentralized architectures, and strict safety and performance constraints. Traditional testing approaches require significant manual effort and lack consistency.

### Key Components of the Pipeline
1. **Requirement-driven test and code generation**: Automatically generate tests from requirements
2. **LLM and VLM assistance**: Use Large Language Models and Vision-Language Models to reduce manual effort
3. **Human-in-the-loop curation**: Maintain quality through human oversight
4. **Distributed deployment support**: Flexible deployment across geographically separated infrastructures using Eclipse openDuT
5. **Cross-organizational coordination**: Optimize for node availability and multi-party workflows

### Implementation Framework
- **Eclipse openDuT**: Provides the foundation for distributed test execution
- **Gherkin specification**: Requirements are specified in Gherkin format for BDD-style testing
- **Automated generation**: Full automation from requirements to test execution
- **Geographic distribution**: Support for testing across different physical locations (e.g., OEM-supplier workflows)

### Validation Results
- **Full functional requirement coverage**: Achieved 100% coverage across all 9 requirements in the CPDS case study
- **Gherkin generation accuracy**: 100% accuracy on controlled requirement sets
- **Distributed execution**: Successfully validated across geographically separated ECUs
- **OEM-supplier applicability**: Confirmed pipeline works for real-world automotive industry workflows

## Implementation Steps

1. **Requirements specification**: Define requirements in Gherkin format
2. **Test generation setup**: Configure LLM/VLM assistance for automated test generation
3. **Human curation workflow**: Establish human-in-the-loop review process
4. **Distributed infrastructure**: Set up Eclipse openDuT for geographic distribution
5. **Execution coordination**: Implement cross-organizational test execution protocols
6. **Validation and reporting**: Measure coverage and accuracy metrics

## Pitfalls to Avoid

- **Over-automation**: Don't eliminate human oversight entirely; maintain curation loops
- **Ignoring geographic constraints**: Account for network latency and availability in distributed setups
- **Lack of standardization**: Use standardized formats like Gherkin for requirement specification
- **Insufficient validation**: Always validate both requirement coverage and generation accuracy

## Verification Steps

1. **Requirement coverage**: Verify 100% functional requirement coverage
2. **Generation accuracy**: Measure accuracy of automatically generated tests
3. **Distributed execution**: Test across geographically separated nodes
4. **Industry applicability**: Validate with real OEM-supplier workflows

## Case Study: Child Presence Detection System (CPDS)
- **Requirements**: 9 functional requirements fully covered
- **Accuracy**: 100% Gherkin generation accuracy on controlled requirements
- **Deployment**: Distributed execution across separate ECUs
- **Workflow**: OEM-supplier testing scenario successfully implemented

## References

- Original paper: "A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications" (arXiv:2608.19752)
- Eclipse openDuT: Open-source framework for distributed testing
- Gherkin: Business-readable specification language for BDD

## Activation Keywords

IoT automotive testing, deployment-aware testing, Eclipse openDuT, requirement-driven testing, LLM testing, VLM testing, distributed automotive testing, OEM-supplier testing, Gherkin generation
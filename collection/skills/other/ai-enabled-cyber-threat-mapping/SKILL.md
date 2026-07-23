---
name: ai-enabled-cyber-threat-mapping
description: Methodology for mapping real-world AI-enabled cyber attacks onto MITRE ATT&CK framework with AI Risk Enablement Score (ARiES) — identifying patterns in how threat actors weaponize AI for cyber operations.
category: ai_collection
trigger_words: ai cyber threat, mitre attack, threat mapping, aries score, banned accounts, cyber operations, threat actor, llm attack navigator
date: 2026-07-13
source: "Anthropic Research - Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator (Jun 3, 2026)"
url: "https://www.anthropic.com/research/attack-navigator"
---

# AI-Enabled Cyber Threat Mapping Methodology

## Overview

A methodology for mapping real-world AI-enabled cyber attacks onto the MITRE ATT&CK framework, scoring threat techniques using the AI Risk Enablement Score (ARiES). Based on analysis of 13,873 technique observations from 832 banned accounts (March 2025 - March 2026).

## Core Methodology

### LLM ATT&CK Navigator
- Maps AI-enabled cyber attack techniques to MITRE ATT&CK v18
- Each technique scored on the **AI Risk Enablement Score (ARiES)**
- Analyzes patterns across banned accounts to identify AI usage trends

### Key Metrics
- **Raw mean ARiES**: Average risk enablement per technique
- **Adjusted score**: Mean × prevalence (combines risk level with how common the technique is)
- **% of banned accounts**: What fraction of banned accounts used each technique

## Findings Patterns

### Traditional Assumptions Challenged
- Risk level can be assessed via metrics like technical sophistication or breadth of techniques
- AI changes the relationship between these traditional metrics and actual threat level

### Technique Categories Analyzed
1. **Reconnaissance**: Active scanning, victim information gathering, OSINT
2. **Resource Development**: Acquiring access, infrastructure, capabilities
3. **Initial Access**: Phishing, exploit public-facing apps, valid accounts
4. **Execution**: Command and scripting interpreters, system services
5. **Persistence**: Boot/logon execution, scheduled tasks, registry modification
6. **Privilege Escalation**: Exploitation for privilege escalation, process injection
7. **Defense Evasion**: Indicator removal, obfuscation
8. **Lateral Movement**: Remote services, lateral tool transfer

## Application

Use this methodology when:
- Analyzing AI-enabled cyber threat patterns
- Mapping threat actor techniques to standard frameworks
- Assessing risk enablement from AI capabilities
- Building threat intelligence reports

## Partnership Data

Results were included in the 2026 Verizon Data Breach Investigation Report (DBIR), providing real-world validation of the methodology.

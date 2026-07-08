---
name: mcp-agentic-ipodwdm-network-automation
description: "MCP-enabled agentic AI architecture for autonomous control of vendor-agnostic IPoDWDM networks. Demonstrates live end-to-end lifecycle multi-layer automation and closed-loop control using GNPy and telemetry, validated on a real testbed. Activation: MCP, agentic network automation, IPoDWDM, GNPy, multi-layer automation, closed-loop control, network lifecycle."
metadata:
  arxiv_id: "2607.05975"
  published: "2026-07-07"
  authors: "Chunmin Xia, Jakub Harbaczewski, Nikhil Dsilva, Julie Raulin, Dominic Schneider, Achim Autenrieth"
  tags: [mcp, agentic-ai, network-automation, ipodwdm, gnpy, closed-loop-control, multi-layer]
---

# MCP-Enabled Agentic AI for Autonomous IPoDWDM Network Lifecycle Automation

## Overview

A demo paper presenting an MCP-enabled agentic AI architecture for autonomous control of vendor-agnostic IPoDWDM (IP over DWDM) networks. The system demonstrates live end-to-end lifecycle multi-layer automation and closed-loop control using GNPy (GitHub No-Perl-y) and telemetry, validated on a real testbed.

## Key Innovations

### MCP Integration for Network Automation
- Uses the Model Context Protocol (MCP) to bridge LLM agents with network domain tools
- Vendor-agnostic architecture enables control across heterogeneous network equipment
- Agents interact with GNPy for optical layer modeling and path computation

### Closed-Loop Control
- End-to-end lifecycle automation: from provisioning to monitoring to remediation
- Real-time telemetry feeds drive agent decision-making
- Closed-loop: agents can detect issues, propose mitigations, and execute changes

### Multi-Layer Automation
- Integrates IP layer and optical (DWDM) layer control
- Cross-layer optimization leveraging GNPy's physical layer awareness
- Enables coordinated provisioning and fault management across layers

## Methodology

1. **Architecture**: Agentic AI framework with MCP servers exposing network tools
2. **GNPy Integration**: Optical layer simulation and path computation via GNPy
3. **Telemetry Pipeline**: Real-time network state ingestion
4. **Testbed Validation**: Demonstrated on a physical IPoDWDM testbed

## Implications

- MCP as a standard protocol for agentic network automation
- Vendor-agnostic approach reduces lock-in and enables multi-vendor orchestration
- Closed-loop automation reduces MTTR (mean time to repair) for network faults
- Practical demonstration of agentic AI in telecommunications infrastructure

## Pitfalls

- Demo paper: limited to testbed scale; production scalability unproven
- GNPy modeling accuracy depends on physical layer calibration
- Real-world vendor APIs may not align cleanly with MCP abstractions
- Safety guardrails for autonomous network changes need further development

## Activation Keywords

mcp, agentic network automation, ipodwdm, gnpy, multi-layer automation, closed-loop control, network lifecycle, vendor-agnostic, optical network, dwdm, telecom automation

## Paper Reference

arXiv:2607.05975 - "MCP-Enabled Agentic AI for Autonomous IPoDWDM Network Lifecycle Automation" (Jul 2026)

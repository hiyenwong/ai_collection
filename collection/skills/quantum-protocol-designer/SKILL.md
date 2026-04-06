---
name: quantum-protocol-designer
description: "Design and analyze quantum information processing protocols. Focus on quantum encoding schemes (polarization, time-bin), QKD security verification, topology-hiding protocols, and quantum state engineering. Activates when user asks about quantum protocol design, quantum network security, QKD protocols, or quantum encoding conversion."
---

# Quantum Protocol Designer

设计和分析量子信息处理协议，包括编码转换、安全性验证和拓扑分析。

## Activation Keywords

- quantum protocol design
- 量子协议设计
- QKD protocol
- quantum encoding
- quantum network security
- quantum key distribution
- 量子密钥分发
- topology-hiding
- 拓扑隐藏
- quantum state engineering

## Tools Used

- exec: Run quantum simulation scripts, arxiv search
- write: Generate protocol documentation, create analysis reports
- read: Load reference protocols, knowledge graph data
- sqlite3: Query kg.db for related papers and patterns

## Core Concepts

### Quantum Encoding Schemes

| Scheme | Description | Use Case |
|--------|-------------|----------|
| **Polarization** | Horizontal/Vertical, Diagonal basis | Short-distance, lab setups |
| **Time-bin** | Early/Late time bins | Long-distance, fiber networks |
| **Phase encoding** | Phase difference between paths | Interferometer-based systems |
| **Frequency encoding** | Different frequency modes | Multi-channel networks |

### Protocol Types

| Protocol | Security Level | Key Feature |
|----------|----------------|-------------|
| **BB84** | Information-theoretic | First QKD protocol |
| **E91** | Entanglement-based | Uses Bell states |
| ** decoy-state** | Enhanced | Detects photon number attacks |
| **Topology-hiding** | Topology privacy | Zero-knowledge connectivity proof |

## Instructions for Agents

### Step 1: Understand Protocol Requirements

Identify from user request:
- **Encoding type**: Polarization, time-bin, phase, frequency?
- **Security requirement**: Information-theoretic, computational, topology privacy?
- **Network topology**: Point-to-point, star, mesh, heterogeneous?
- **Performance metrics**: Key rate, error rate, distance?

### Step 2: Search Knowledge Base

Query kg.db for related work:

```bash
sqlite3 kg.db "
SELECT e.name as paper, r.rel_type, k.name as keyword
FROM kg_relations r
JOIN kg_entities e ON r.source_id = e.id
JOIN kg_entities k ON r.target_id = k.id
WHERE e.entity_type = 'paper' 
  AND k.name LIKE '%quantum%'
ORDER BY r.created_at DESC LIMIT 10;
"
```

### Step 3: Analyze Protocol Components

For each protocol, consider:

1. **Encoding Layer**
   - Basis choice mechanism
   - Basis conversion (if heterogeneous network)
   - Error correction scheme

2. **Security Layer**
   - Authentication method
   - Key verification
   - Attack detection (photon splitting, intercept-resend)
   - Zero-knowledge proofs (for topology-hiding)

3. **Network Layer**
   - Topology design
   - Repeater placement
   - Path validation
   - Multi-path support

### Step 4: Generate Protocol Design

Output format:

```markdown
# Quantum Protocol Design: [Protocol Name]

## Overview
[Brief description of protocol purpose and key features]

## Encoding Scheme
- **Primary basis**: [Polarization/Time-bin/Phase]
- **Conversion mechanism**: [If needed]
- **Error handling**: [Scheme]

## Security Verification
- **Authentication**: [Method]
- **Key verification**: [Protocol]
- **Attack detection**: [Mechanisms]
- **Topology hiding**: [If applicable, describe ZKP approach]

## Network Configuration
- **Topology**: [Description]
- **Path requirements**: [Disjoint paths, etc.]
- **Performance targets**: [Key rate, error threshold]

## Implementation Notes
- [Specific hardware requirements]
- [Software dependencies]
- [Testing considerations]

## References
- [Related papers from kg.db]
- [arxiv sources]
```

### Step 5: Validate Design

Check for:
- **Consistency**: All components work together
- **Security**: No obvious vulnerabilities
- **Feasibility**: Hardware requirements are realistic
- **Performance**: Metrics achievable

## Common Patterns

### Pattern 1: Encoding Conversion

From recent paper (2604.02081v1):
- Polarization → Time-bin → Polarization
- Sources of infidelity become transmission rate changes
- Useful for heterogeneous networks

### Pattern 2: Topology-Hiding QKD

From recent papers (2604.01876v1, 2604.01831v1):
- Graph-signature techniques
- Zero-knowledge proofs of connectivity
- Path validation without topology revelation
- Multi-path certification

### Pattern 3: Quantum State Engineering

From recent papers (2604.01722v1, 2604.02234v1):
- Differentiable physical frameworks
- Goal-driven state preparation
- MUBs via Hadamard matrices
- Mathematical construction methods

## Error Handling

### Encoding Conversion Failure
- Check basis alignment
- Verify timing synchronization
- Adjust for fiber fluctuations

### Security Verification Failure
- Increase decoy states
- Add authentication steps
- Verify key sifting process

### Topology Revelation Risk
- Apply stronger zero-knowledge proofs
- Add noise to path information
- Use multiple disjoint paths

## Resources

- **Knowledge Graph**: `/Users/hiyenwong/.openclaw/workspace/kg.db`
- **Arxiv Search**: `scripts/search_arxiv.py`
- **Import Script**: `scripts/import_papers_to_kg.py`
- **kg_tool**: `scripts/kg_tool/target/release/kg_tool`

## Related Skills

- **skill-extractor**: Extract patterns from quantum papers
- **skill-creator**: Create specialized quantum skills
- **arxiv-search**: Search quantum papers on arxiv

## Notes

- Quantum protocols require both theoretical analysis and practical feasibility
- Knowledge graph contains 133+ papers for reference
- kg_tool has issues with PageRank/Louvain - use SQL queries instead
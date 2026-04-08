# SKILL.md - Hierarchical Parallel Agent Framework for Web Search

## Paper Reference
- **arXiv:** 2604.02971
- **Title:** A Scalable Hierarchical Parallel Agent Framework for Web Information Seeking
- **Utility Score:** 0.85
- **Authors:** Yuxuan Huang et al.
- **Code:** https://github.com/agent-on-the-fly/InfoSeeker
- **Date:** April 2026

## Core Insights

### Problem Addressed
Existing agentic search systems:
- Focus on deep reasoning, neglect wide-scale synthesis
- Face context saturation
- Cascading error propagation
- High end-to-end latency

### Solution: Hierarchical Framework
Based on **principle of near-decomposability:**

1. **Host:** Strategic coordination
2. **Managers:** Aggregation + reflection mechanisms
3. **Workers:** Parallel execution

### Key Features
- **Context isolation:** Manager layer prevents saturation
- **Error containment:** Stops cascading propagation
- **Parallelism:** Worker layer accelerates execution

### Results
- **3-5x speed-up**
- WideSearch-en: 8.4% success rate
- BrowseComp-zh: 52.9% accuracy

## Practical Applications

### Multi-Agent Search Architecture
```markdown
1. Host: Parse query → distribute to managers
2. Manager: Aggregate worker results → reflect
3. Worker: Execute search tasks in parallel
4. Return: Synthesized answer
```

### Design Principles
- Near-decomposability: Tasks can be parallelized
- Context isolation: Each manager handles subset
- Reflection: Quality check at manager level

### When to Use
- Large-scale information synthesis
- Many heterogeneous sources
- High-latency tolerance unacceptable
- Error propagation risk

## Key Takeaways
- Hierarchical structure solves saturation/latency
- Parallelism essential for wide-scale search
- Manager reflection improves quality
- Open-source implementation available

## Open Resources
- GitHub: https://github.com/agent-on-the-fly/InfoSeeker

## Benchmarks
- WideSearch-en
- BrowseComp-zh

## Further Reading
- Full paper: https://arxiv.org/abs/2604.02971
- PDF: https://arxiv.org/pdf/2604.02971
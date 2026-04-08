---
name: arxiv-paper-tracker
description: 'Track high-utility arXiv papers in AI agent systems. Use when needing quick reference to important recent papers on multi-agent coordination, memory management, agent architecture, and evaluation methods.'
metadata:
  {
    "openclaw":
      {
        "emoji": "📚",
        "tags": ["research", "arxiv", "agents", "papers", "tracking"],
      },
  }
---

# arXiv Paper Tracker

Track and reference high-utility papers from arXiv related to AI agent systems.

## High-Utility Papers (2026-04-03)

Utility threshold: >= 0.85

### Multi-Agent Coordination

**1. Agent Q-Mix** (arXiv:2604.00344) - Utility: 0.92
- **Title:** Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning
- **Authors:** Eric Hanchen Jiang et al.
- **Key Innovation:** MARL framework using QMIX value factorization for topology selection
- **Architecture:** CTDE (Centralized Training with Decentralized Execution), GNN encoder, GRU memory
- **Results:** 
  - Highest accuracy across 7 benchmarks (coding, reasoning, math)
  - HLE benchmark: 20.8% accuracy (vs Microsoft Agent Framework 19.2%, LangGraph 19.2%)
  - Superior token efficiency and robustness against agent failure
- **Practical Use:** Optimize multi-agent communication topology dynamically
- **URL:** https://arxiv.org/abs/2604.00344

**2. Competition and Cooperation of LLM Agents** (arXiv:2604.00487) - Utility: 0.87
- **Title:** Competition and Cooperation of LLM Agents in Games
- **Authors:** Jiayi Yao et al.
- **Key Finding:** LLM agents tend to cooperate rather than converge to Nash equilibria
- **Games Tested:** Network resource allocation game, Cournot competition game
- **Insight:** Fairness reasoning is central to cooperative behavior in non-zero-sum contexts
- **Practical Use:** Understanding strategic behavior patterns in competitive multi-agent settings
- **URL:** https://arxiv.org/abs/2604.00487

### Memory Management

**3. Novel Memory Forgetting Techniques** (arXiv:2604.02280) - Utility: 0.88
- **Title:** Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency
- **Authors:** Sunil Tiwari
- **Problem:** Long-horizon agents suffer from temporal decay and false memory propagation
- **Solution:** Adaptive budgeted forgetting framework with:
  - Relevance-guided scoring
  - Bounded optimization
  - Integration of recency, frequency, and semantic alignment
- **Results:**
  - Long-horizon F1 > 0.583 baseline
  - Higher retention consistency
  - Reduced false memory behavior
  - No increase in context usage
- **Practical Use:** Prevent memory bloat in extended conversational agents
- **URL:** https://arxiv.org/abs/2604.02280

### Agent Architecture

**4. The Self Driving Portfolio** (arXiv:2604.02279) - Utility: 0.85
- **Title:** Agentic Architecture for Institutional Asset Management
- **Authors:** Andrew Ang
- **Scale:** ~50 specialized agents, 20+ portfolio construction methods
- **Architecture Components:**
  - Capital market assumptions agents
  - Portfolio construction agents (competing methods)
  - Critique and voting system
  - Researcher agent (proposes new methods)
  - Meta-agent (rewrites code/prompts based on past performance)
- **Governance:** Investment Policy Statement constrains autonomous agents
- **Practical Use:** Reference architecture for complex multi-agent systems with self-improvement
- **URL:** https://arxiv.org/abs/2604.02279

### Evaluation Methods

**5. User Turn Generation Probe** (arXiv:2604.02315) - Utility: 0.86
- **Title:** User Turn Generation as a Probe of Interaction Awareness in Language Models
- **Authors:** Sarath Shekkizhar
- **Key Concept:** Interaction awareness - ability to generate grounded follow-ups
- **Method:** Let model generate under user role after seeing assistant response
- **Finding:** Interaction awareness is decoupled from task accuracy
- **Tested Models:** 11 open-weight LLMs (Qwen3.5, gpt-oss, GLM) across 5 datasets
- **Insight:** 
  - Qwen3.5 family: GSM8K accuracy scales from 41% to 96.8%, but follow-up rates near zero under deterministic generation
  - Higher temperature sampling reveals latent awareness (22% follow-up rate)
- **Practical Use:** Evaluate conversational AI beyond task accuracy
- **URL:** https://arxiv.org/abs/2604.02315

## Related Resources

### Benchmarks
- **MultiAgentBench** (arXiv:2503.01935): Comprehensive multi-agent evaluation with milestone-based KPIs
- **MAFBench** (arXiv:2602.03128): Unified framework-level evaluation suite
- **Theoretical Production Benchmark v2.0**: Evaluating sustained conceptual coherence

### Memory Systems
- **A-MEM** (arXiv:2502.12110): Zettelkasten-inspired agentic memory
  - Dynamic indexing and linking
  - 6-fold improvement in multi-hop reasoning
  - 85-93% reduction in token usage
- **A-MemGuard**: Proactive defense against memory poisoning attacks

### Paper Collections
- **VoltAgent/awesome-ai-agent-papers**: Curated 2026 papers on multi-agent coordination, memory/RAG, tooling, evaluation, security

## Trends (April 2026)

1. **Multi-agent coordination is mainstream** - Multiple papers on topology optimization, cooperation, competition
2. **Memory management maturing** - From simple storage to adaptive forgetting, dynamic organization
3. **Production architectures emerging** - Real-world applications showing complete system designs
4. **Evaluation expanding** - New dimensions beyond accuracy: interaction awareness, cooperation quality, conceptual coherence
5. **Self-improvement mechanisms** - Meta-agents that rewrite code/prompts based on performance

## Quick Reference Commands

```bash
# Search for recent agent papers
web_search query:"arXiv LLM agents multi-agent coordination memory RAG 2026"

# Fetch specific paper
web_fetch url:"https://arxiv.org/abs/<paper_id>"

# Check awesome collection
web_fetch url:"https://github.com/VoltAgent/awesome-ai-agent-papers"
```

---

Last updated: 2026-04-03 22:00 (Asia/Shanghai)
Papers analyzed: 188 submissions from Fri, 3 Apr 2026
High-utility count: 5 papers (utility >= 0.85)
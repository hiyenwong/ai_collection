---
title: Plugin Decomposition - Detailed Mapping
date: 2026-04-27
---

# Plugin Decomposition Mapping

This document maps every skill and agent to its target plugin based on the 5-domain split.

## Quick Reference: Plugin Categories

| Plugin | Domain | Focus | Estimated Skills |
|--------|--------|-------|------------------|
| **openclaw-core** | Core | Foundation agents, meta-skills, security | ~20 |
| **openclaw-neuroscience** | Neuroscience | Brain science, neuromorphic, neural dynamics | ~400 |
| **openclaw-coding** | Coding | Development tools, languages, security practices | ~150 |
| **openclaw-data** | Data & Analytics | Data science, ML, finance, quantitative | ~50 |
| **openclaw-research** | Research & Science | Applied science, computational methods, research tools | ~50 |

---

## Agents Mapping

### openclaw-core (Foundation)
```
fullstack-engineer         → Primary full-stack platform
tech-cofounder            → MVP building
skill-extractor (new role) → Meta-skill for AI collection itself
```

### openclaw-neuroscience
```
neuroscientist            → Primary neuroscience expert
biologist                 → Biological systems
computational-scientist   → Computational modeling
algorithm-engineer        → Algorithm design (also could go to coding, but placed here due to neural focus)
```

### openclaw-coding
```
[No agents primary]       → Agents focused on coding are rare; skills dominate this plugin
```

### openclaw-data
```
stock-analyst            → Financial data & analysis
statistician             → Statistical reasoning (also fits research, but placed here for analytics focus)
```

### openclaw-research
```
research-agent           → Deep research & investigation
applied-scientist        → Experimental design & science
mathematician            → Formal reasoning & proofs
psychologist             → Cognitive & behavior analysis
```

---

## Skills Mapping Rules

### Classification Keywords (from _INDEX.json + SKILLS.md)

#### openclaw-core
**Keywords:** `security`, `guardrails`, `meta`, `prompt`, `agent`, `skill-extractor`, `memory`

**Skills in this category:**
```
security-guardrails
skill-extractor
memory-retrieval
indexed-memory
ice-review
self-challenge
meta-cognitive-reflection
```

#### openclaw-neuroscience
**Keywords:** `neuroscience`, `brain`, `spiking`, `snn`, `neural`, `neuromorphic`, `eeg`, `fmri`, `meg`, `ecog`, `tms`, `neuromodulation`, `connectome`, `cortex`, `hippocampal`, `cerebellar`, `computational-neuroscience`, `brain-computer-interface`, `bci`, `neural-coding`, `plasticity`, `synaptic`, `stdp`, `astrocyte`, `glial`, `dendritic`, `spike`, `neuron`, `calcium`, `optogenetics`, `brain-network`, `neural-dynamics`, `neural-field`, `spike-timing`, `hebbian`

**Approximate skills in this category:** ~400+ (largest category; many neuroscience-focused papers/skills)

**Examples:**
```
snn-internal-noise-analysis
snn-working-memory-heterogeneous-delays-v2
brain-to-speech-transformer-reconstruction
in-context-brain-decoding
eeg-visual-attention-decoding
eeg2vision-multimodal-framework
brain-foundation-model-batch-effects
meta-learning-in-context-brain-decoding
multimodal-higher-order-brain-networks
spiking-neural-network-training
neural-connectivity-matrix-viewer
... [350+ more]
```

#### openclaw-coding
**Keywords:** `coding`, `typescript`, `javascript`, `python`, `react`, `nodejs`, `testing`, `security`, `linting`, `formatting`, `deployment`, `ci-cd`, `docker`, `git`, `vscode`, `editor`, `ide`, `dev`, `development`, `backend`, `frontend`, `api`, `web`, `framework`, `library`, `package`, `npm`, `debugging`

**Skills in this category:**
```
claude-code
opencode
openspec (specification-driven development with Gherkin)
react-components
accessibility-wcag
chrome-extension
electron-typescript
frontend-best-practices
backend-patterns
tdd-workflow
e2e-testing
[~140+ more coding/dev skills]
```

#### openclaw-data
**Keywords:** `data`, `analysis`, `analytics`, `machine-learning`, `ml`, `quantitative`, `finance`, `stock`, `trading`, `timeseries`, `database`, `sql`, `etl`, `pipeline`, `data-engineering`, `akshare`, `visualization`, `statistics`

**Skills in this category:**
```
akshare
stock-analysis
consulting-report-search
data-scraper-agent
ml-engineer (could also be neuroscience)
[~40+ more data/finance/ml skills]
```

#### openclaw-research
**Keywords:** `research`, `science`, `applied-science`, `deep-research`, `literature`, `arxiv`, `academic`, `paper`, `survey`, `benchmark`, `evaluation`, `experiment`, `methodology`, `computational-science`, `physics`, `chemistry`, `biology`, `mathematics`, `logic`, `philosophy`

**Skills in this category:**
```
deep-research
market-research
arxiv-search
research-ops
arxiv-paper-tracker
[~40+ more research/science skills]
```

---

## Conflict Resolution Examples

### 1. Skill: "ml-engineer" (Could be data OR neuroscience)
- **Current choice:** openclaw-data (data & ML is primary focus)
- **Rationale:** Stock analyst needs ML; neuroscience agent has dedicated agent skills
- **Override:** If neuroscience community wants this, use `strict: false` in marketplace.json and add it to openclaw-neuroscience as well

### 2. Skill: "api-design" (Could be coding OR research)
- **Current choice:** openclaw-coding (backend/API design)
- **Rationale:** Developers building APIs; researchers can use if needed
- **Note:** Clearly tag in skill docs for discoverability

### 3. Skill: "quantum-computing" (Could be research OR neuroscience)
- **Current choice:** openclaw-research (quantum as science discipline)
- **Override:** If quantum ML becomes primary, move to openclaw-data

---

## Directory Structure Preview

After implementation, `plugins/` will look like:
```
plugins/
├── openclaw-core/                          (~20 skills, 3 agents)
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── security-guardrails/ → collection/skills/security-guardrails/
│   │   ├── skill-extractor/ → collection/skills/skill-extractor/
│   │   ├── memory-retrieval/ → collection/skills/memory-retrieval/
│   │   └── [17 more core skills]
│   ├── agents/
│   │   ├── fullstack-engineer/ → collection/agents/fullstack-engineer/
│   │   ├── tech-cofounder/ → collection/agents/tech-cofounder/
│   │   └── research-agent/ → collection/agents/research-agent/ (copy to core)
│   └── README.md
│
├── openclaw-neuroscience/                   (~400 skills, 4 agents)
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── snn-internal-noise-analysis/ → collection/skills/snn-internal-noise-analysis/
│   │   ├── eeg-visual-attention-decoding/ → collection/skills/eeg-visual-attention-decoding/
│   │   ├── brain-to-speech-transformer-reconstruction/ → collection/skills/...
│   │   └── [397 more neuroscience skills]
│   ├── agents/
│   │   ├── neuroscientist/ → collection/agents/neuroscientist/
│   │   ├── biologist/ → collection/agents/biologist/
│   │   ├── computational-scientist/ → collection/agents/computational-scientist/
│   │   └── algorithm-engineer/ → collection/agents/algorithm-engineer/
│   └── README.md
│
├── openclaw-coding/                         (~150 skills)
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── claude-code/ → collection/skills/claude-code/
│   │   ├── opencode/ → collection/skills/opencode/
│   │   ├── openspec/ → collection/skills/openspec/
│   │   ├── react-components/ → collection/skills/react-components/
│   │   └── [146 more coding skills]
│   └── README.md
│
├── openclaw-data/                           (~50 skills, 2 agents)
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── akshare/ → collection/skills/akshare/
│   │   ├── stock-analysis/ → collection/skills/stock-analysis/
│   │   ├── consulting-report-search/ → collection/skills/consulting-report-search/
│   │   └── [47 more data/finance skills]
│   ├── agents/
│   │   ├── stock-analyst/ → collection/agents/stock-analyst/
│   │   └── statistician/ → collection/agents/statistician/
│   └── README.md
│
└── openclaw-research/                       (~50 skills, 5 agents)
    ├── .claude-plugin/plugin.json
    ├── skills/
    │   ├── deep-research/ → collection/skills/deep-research/
    │   ├── market-research/ → collection/skills/market-research/
    │   ├── arxiv-search/ → collection/skills/arxiv-search/
    │   └── [47 more research/science skills]
    ├── agents/
    │   ├── research-agent/ → collection/agents/research-agent/
    │   ├── applied-scientist/ → collection/agents/applied-scientist/
    │   ├── mathematician/ → collection/agents/mathematician/
    │   ├── psychologist/ → collection/agents/psychologist/
    │   └── [already listed in core, reference here]
    └── README.md
```

---

## Implementation Steps (Summary)

1. **Create directories:**
   ```bash
   mkdir -p .claude-plugin plugins/{openclaw-core,openclaw-neuroscience,openclaw-coding,openclaw-data,openclaw-research}/{.claude-plugin,skills,agents}
   ```

2. **For each plugin, create `.claude-plugin/plugin.json`:**
   ```json
   {
     "name": "openclaw-{plugin-name}",
     "description": "[Description from MARKETPLACE_BLUEPRINT.md]",
     "version": "1.0.0"
   }
   ```

3. **Create symlinks (macOS/Linux):**
   ```bash
   cd plugins/openclaw-core/skills
   ln -s ../../../collection/skills/security-guardrails
   ln -s ../../../collection/skills/skill-extractor
   # ... repeat for all skills in this plugin
   ```

4. **Create symlinks for agents:**
   ```bash
   cd plugins/openclaw-core/agents
   ln -s ../../../collection/agents/fullstack-engineer
   ln -s ../../../collection/agents/tech-cofounder
   # ... repeat
   ```

5. **Create `.claude-plugin/marketplace.json`** at repo root (see template in MARKETPLACE_BLUEPRINT.md)

6. **Validate:**
   ```bash
   claude plugin validate .
   ```

7. **Test locally:**
   ```bash
   /plugin marketplace add ./
   /plugin install openclaw-core@openclaw-ai-collection
   ```

---

## Appendix: Full Skill List by Category

(Derived from current _INDEX.json and SKILLS.md; update as needed)

### Core Skills (openclaw-core)
1. security-guardrails
2. skill-extractor
3. memory-retrieval
4. indexed-memory
5. ice-review
6. self-challenge
7. meta-cognitive-reflection
8. [13 more core meta-skills if available]

### Neuroscience Skills (openclaw-neuroscience)
[~400 skills including:]
- snn-internal-noise-analysis
- snn-working-memory-heterogeneous-delays-v2
- brain-to-speech-transformer-reconstruction
- in-context-brain-decoding
- eeg-visual-attention-decoding
- eeg2vision-multimodal-framework
- brain-foundation-model-batch-effects
- meta-learning-in-context-brain-decoding
- multimodal-higher-order-brain-networks
- spiking-neural-network-training
- neural-connectivity-matrix-viewer
- brain-omnifunctional-foundation-model
- deep-learning-eeg-tms-closed-loop
- warped-hierarchical-modular-neural-network
- ... [380+ more]

### Coding Skills (openclaw-coding)
[~150 skills including:]
- claude-code
- opencode
- openspec
- react-components
- accessibility-wcag
- chrome-extension
- electron-typescript
- frontend-best-practices
- backend-patterns
- tdd-workflow
- e2e-testing
- ... [140+ more]

### Data & Analytics Skills (openclaw-data)
[~50 skills including:]
- akshare
- stock-analysis
- consulting-report-search
- data-scraper-agent
- ml-engineer
- ... [45+ more]

### Research & Science Skills (openclaw-research)
[~50 skills including:]
- deep-research
- market-research
- arxiv-search
- research-ops
- arxiv-paper-tracker
- ... [45+ more]

---

**Note:** Exact counts will vary as collection grows. Use `_INDEX.json` and `SKILLS.md` as source of truth during implementation.

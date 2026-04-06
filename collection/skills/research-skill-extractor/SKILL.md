---
name: research-skill-extractor
description: "Meta-skill that extracts reusable skill patterns from research papers (arxiv), scientific workflows, and knowledge graph analysis. Activates when analyzing papers for skill patterns, creating skills from research methodologies, or mining patterns from scientific literature. Keywords: extract skill from paper, research skill mining, 论文技能提炼, paper to skill, arxiv skill extractor."
---

# Research Skill Extractor

Extracts reusable skill patterns from research papers and scientific workflows.

## Purpose

Research papers contain valuable methodologies that can be extracted into reusable skills. This skill:
1. Analyzes paper abstracts and methodologies
2. Identifies transferable patterns
3. Creates skills following skill-creator standards
4. Integrates with knowledge graph for pattern discovery

## Activation Keywords
- extract skill from paper
- research skill mining
- 论文技能提炼
- paper to skill
- arxiv skill extractor
- 从论文提取技能
- mine skill patterns
- 研究模式提炼

## Tools Used
- `read`: Read paper abstracts, SKILL.md templates
- `write`: Create new skill files
- `exec`: Run kg_tool, arxiv search scripts
- `feishu_fetch_doc`: Fetch paper details if available

## Workflow

### Phase 1: Paper Selection
Use knowledge graph to identify valuable papers:

```bash
kg_tool pagerank kg.db  # Find important papers
kg_tool similar kg.db <entity_id> 5  # Find related papers
sqlite3 kg.db "SELECT name, properties FROM kg_entities WHERE entity_type='paper' ORDER BY id DESC LIMIT 10"
```

**Selection Criteria:**
- High PageRank score (influential topics)
- Recent submissions (2026-04-02 onwards)
- Novel methodology keywords: "framework", "approach", "method", "pipeline"

### Phase 2: Pattern Analysis

For each candidate paper, extract:

| Element | Look For |
|---------|----------|
| **Core Method** | Algorithm, workflow, framework name |
| **Novelty** | What's new vs existing methods |
| **Applicability** | Domain-general vs domain-specific |
| **Implementation** | Can it be coded/scripted? |
| **Dependencies** | Tools, APIs, libraries used |

**Pattern Detection Signals:**
- "We propose/introduce/develop a..."
- "Our framework/approach/method..."
- "This enables..."
- Step-by-step pipeline descriptions

### Phase 3: Skill Extraction

Generate skill template:

```markdown
---
name: [skill-name]
description: [What it does + when to use]
---

# [Skill Name]

## Description
[1-2 sentences from paper]

## Activation Keywords
- [domain keyword]
- [method keyword]
- [Chinese variant]

## Tools Used
- [tool1]: [usage]

## Workflow
### Step 1: [Action]
[Instructions from paper]

### Step 2: [Action]
[Instructions]

## Resources
- Paper: [arxiv_link]
- Code: [github if available]
```

### Phase 4: Validation

Check skill viability:

1. **Reusable?** - Can apply in multiple contexts
2. **Actionable?** - Clear step-by-step instructions
3. **Not Duplicate?** - Search existing skills
4. **Complete?** - Has all required elements

## Example Patterns

### Pattern: RAG Pipeline
From paper: "Retrieval-Augmented QA for Scientific Literature"

Extracted skill components:
- **Name**: `scientific-rag`
- **Core**: Build domain-specific RAG from arxiv
- **Workflow**: Index papers → Vector store → LLM integration
- **Tools**: httpx, sqlite3, vector DB

### Pattern: Skill Internalization
From paper: "SKILL0: In-Context Agentic Reinforcement Learning"

Extracted skill components:
- **Name**: `skill-internalization`
- **Core**: Convert skills from retrieval to parameters
- **Workflow**: Identify skill → RL training → Parameter update
- **Novelty**: Skills embedded in model weights

### Pattern: Topological Neural Network
From paper: "Topological Effects in Neural Network Field Theory"

Extracted skill components:
- **Name**: `topological-nn-field`
- **Core**: Extend NN field theory with topological parameters
- **Workflow**: Define topology → Parameter encoding → Training
- **Domain**: Computational physics, quantum ML

## Integration with Knowledge Graph

Store extracted patterns in kg.db:

```sql
INSERT INTO kg_entities (entity_type, name, properties, created_at)
VALUES ('skill_pattern', '[pattern_name]', json_extract(...), strftime('%s', 'now'));
```

Link papers to extracted skills:

```sql
INSERT INTO kg_relations (from_id, to_id, relation_type)
VALUES ([paper_id], [skill_id], 'extracted_to');
```

## Best Practices

1. **Prioritize Practicality**: Extract skills that can be implemented now
2. **Keep Core Simple**: Start with essential workflow, add complexity later
3. **Validate with User**: Confirm extracted patterns before creating files
4. **Track Sources**: Always link back to original paper
5. **Iterate**: Refine skills based on actual usage

## Output Format

```
🔴🔴🔴 **[研究技能提炼]** 🔴🔴🔴

论文: {title}
arXiv: {id}

提取的模式:
- **方法名称**: {method_name}
- **核心流程**: {workflow}
- **适用领域**: {domain}
- **可实现性**: {implementation_notes}

建议技能:
- **技能名称**: {skill_name}
- **描述**: {description}
- **激活关键词**: {keywords}

是否创建此技能？[确认/修改/跳过]
```

## Resources
- skill-creator: Main skill creation guide
- skill-extractor: Conversation-based extraction
- arxiv-search: Paper search capability

## Notes
- Focus on methodology papers, not pure theory
- Prefer papers with code/GitHub links
- Domain-specific skills need domain knowledge in references/
- Keep skill names descriptive but concise
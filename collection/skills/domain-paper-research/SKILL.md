---
name: domain-paper-research
description: Conduct comprehensive domain-specific research paper discovery and compilation. Search across skills, Obsidian vault, and knowledge graph to find relevant papers, then compile into a structured collection with reading order, concept maps, and design decision matrices. Use when user asks for papers on a specific technical domain or wants to build a literature review for a project.
---

# Domain Paper Research

Conduct comprehensive research paper discovery and compilation for a specific technical domain.

## When to Use

- User asks for papers on a specific topic (e.g., "papers for building an AI employee platform")
- Need to compile a literature review for a project
- Want to understand the research landscape for a technical area
- Building a reading list for a new domain

## Workflow

### Step 1: Search Multiple Sources

Search across all available sources simultaneously:

**A. Skills Search**
```bash
# List skills in relevant categories
skills_list --category research
skills_list --category openclaw-imports

# View relevant skills
skill_view <skill_name>
```

**B. Obsidian Vault Search**
```bash
# Search by filename
find "$VAULT" -name "*.md" -iname "*<keyword>*"

# Search by content
grep -rli "<keyword>" "$VAULT" --include="*.md"
```

**C. Knowledge Graph Search** (if available)
```python
kg_search_papers("<query>", limit=20)
kg_recommend_skills("<topic>", min_utility=0.8)
```

### Step 2: Categorize Findings

Group papers into logical categories:

| Category | Description | Example |
|----------|-------------|---------|
| Architecture | System-level design | Orchestration, Infrastructure |
| Coordination | Multi-agent patterns | Organization, Communication |
| Memory | State management | Long-term, Short-term, Multimodal |
| Tools | External capabilities | Reliability, Schema, Integration |
| Roles | Agent specialization | Assignment, Expertise |
| Engineering | Development methodology | Best practices, Bootstrapping |

### Step 3: Extract Key Information

For each paper, capture:
- **Title & Authors**
- **Source** (arXiv ID, conference, report ID)
- **Core Insight** (1-2 sentences)
- **Key Contributions** (bullet points)
- **Performance Metrics** (if applicable)
- **Applicable Scenarios**
- **Tags**

### Step 4: Create Structured Output

Generate a markdown document with:

1. **Overview** - Domain summary
2. **Categorized Paper List** - Grouped by topic
3. **Reading Order** - Phased approach (Week 1-2, etc.)
4. **Concept Map** - Visual relationships
5. **Design Decision Matrix** - Compare alternatives
6. **Open Questions** - Future exploration

### Step 5: Cross-Link in Obsidian

Update relevant area/project notes:
```markdown
### <Domain>
- [[Paper Collection Note]]

## 📚 Resources
- [[Paper Collection Note|<Description>]]
```

## Output Template

```markdown
# <Domain> - Paper Collection

## 📊 Overview
[Domain description and scope]

---

## [Category 1]

### [[Paper 1]] ⭐⭐⭐⭐⭐
- **Source**: [arXiv ID / Conference / Report]
- **Authors**: [Names]
- **Core Insight**: [Key finding]
- **Key Contributions**:
  - [Contribution 1]
  - [Contribution 2]
- **Performance**: [Metrics if applicable]
- **Applicable Scenarios**: [When to use]
- **Tags**: #[tag1] #[tag2]

---

## 📚 Recommended Reading Order

### Phase 1: Foundation (Week 1-2)
1. [Paper A] - [Why first]
2. [Paper B] - [Prerequisites]

### Phase 2: [Topic] (Week 3-4)
...

## 🔗 Concept Map

```
[Visual diagram of relationships]
```

## 🎯 Design Decision Matrix

| Problem | Option A | Option B | Recommendation |
|---------|----------|----------|----------------|
| [Question] | [Approach 1] | [Approach 2] | [Rationale] |

## 📝 Open Questions

1. [Question for future exploration]
2. ...
```

## Example Domains

- **AI Employee Platform**: Orchestration, multi-agent, memory, tools, roles
- **RAG Systems**: Retrieval, embedding, chunking, reranking, evaluation
- **Agent Memory**: Short-term, long-term, multimodal, forgetting
- **Multi-Agent Coordination**: Hierarchy, voting, consensus, communication

## Tips

1. **Prioritize high-utility papers** (utility >= 0.85 if using knowledge graph)
2. **Include both academic and industry sources** (arXiv + Gartner/etc)
3. **Create bidirectional links** in Obsidian for discoverability
4. **Add reading phases** to make the collection actionable
5. **Include design matrices** to help with architectural decisions

## References

This skill was developed from compiling papers for:
- AI employee platforms
- Agent engineering harness
- Multi-agent systems
- Agent memory and orchestration

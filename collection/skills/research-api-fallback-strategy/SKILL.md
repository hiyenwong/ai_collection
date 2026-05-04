---
name: research-api-fallback-strategy
description: "Fallback strategies for automated research when external APIs fail. Use when: (1) arXiv/semantic scholar APIs return errors, (2) scheduled research jobs encounter connectivity issues, (3) need to pivot from live search to knowledge-based skill creation, (4) automated research pipelines need resilience against external service failures."
---

# Research API Fallback Strategy

How to continue automated research workflows when external APIs (arXiv, Semantic Scholar, etc.) are unavailable.

## When to Use This Skill

**Trigger situations**:
- API returns 502/503 errors
- Network timeouts on external services
- Scheduled cron jobs with failed API calls
- Rate limiting blocks requests
- **Model provider HTTP 429 "Insufficient balance"** — the cron job's LLM provider has no remaining credits, causing every request to fail. This is different from API rate limiting: the service works but the account is empty. Diagnose by reading cron output: `cat ~/.hermes/cron/output/<job_id>/<latest>.md | grep -i "balance\|recharge"`

## Fallback Strategy

### Step 1: Verify API Failure

```python
# Try multiple access methods before giving up
methods = [
    ('httpx', query_with_httpx),
    ('urllib', query_with_urllib),
    ('curl', query_with_curl),
    ('alternative_endpoint', query_alternative),
]

for name, method in methods:
    try:
        result = method()
        if result:
            return result
    except Exception as e:
        log_attempt(name, e)

# All methods failed - activate fallback
return activate_fallback_strategy()
```

### Step 2: Analyze Existing Knowledge Base

When live search fails, analyze existing resources:

```python
def analyze_existing_skills(domain: str) -> dict:
    """
    Scan existing skills to identify:
    1. What's already covered
    2. What gaps exist
    3. What related topics need skills
    """
    skills_dir = os.path.expanduser("~/.hermes/skills")
    
    analysis = {
        'existing_topics': [],
        'gaps': [],
        'recent_updates': [],
        'coverage_score': 0
    }
    
    # Find domain-related skills
    for skill in os.listdir(skills_dir):
        if domain in skill.lower():
            skill_path = os.path.join(skills_dir, skill, "SKILL.md")
            if os.path.exists(skill_path):
                # Extract description from frontmatter
                desc = extract_description(skill_path)
                mtime = os.path.getmtime(os.path.dirname(skill_path))
                analysis['existing_topics'].append({
                    'name': skill,
                    'description': desc,
                    'updated': mtime
                })
    
    return analysis
```

### Step 3: Identify Knowledge Gaps

Based on analysis, identify missing skill areas:

**Example: Quantum Computing Domain**

| Area | Existing Skills | Gap Identified |
|------|----------------|----------------|
| Algorithms | 15 | ✓ Covered |
| Hardware | 8 | ✓ Covered |
| ML/Data | 3 | ⚠️ Limited coverage |
| Error Correction | 5 | ✓ Covered |

**Action**: Create skill for quantum ML data loading (gap identified)

### Step 4: Create Skill from Domain Knowledge

When API is unavailable, create skills based on:

1. **Established best practices** in the field
2. **Common implementation patterns** from experience
3. **Key research papers** already known
4. **Standard tools and frameworks**

```markdown
## Content Sources (when API unavailable)

- Textbook knowledge
- Previously read papers
- Framework documentation
- Implementation experience
- Community best practices
```

## Implementation Pattern

### Pattern: Resilient Research Pipeline

```python
class ResilientResearchPipeline:
    """
    Research pipeline with automatic fallback.
    """
    
    def __init__(self, domain: str):
        self.domain = domain
        self.api_available = True
    
    def run_daily_research(self):
        """Main entry point for scheduled research."""
        
        # Try primary approach
        papers = self.try_api_search()
        
        if papers:
            # Normal flow: analyze papers → create skill
            return self.create_skill_from_papers(papers)
        else:
            # Fallback: analyze gaps → create skill from knowledge
            return self.create_skill_from_gap_analysis()
    
    def try_api_search(self, max_retries: int = 3) -> list:
        """Attempt API search with retries."""
        for attempt in range(max_retries):
            try:
                return search_arxiv(self.domain)
            except APIError as e:
                log.warning(f"API attempt {attempt + 1} failed: {e}")
                time.sleep(2 ** attempt)  # Exponential backoff
        
        self.api_available = False
        return []
    
    def create_skill_from_gap_analysis(self) -> dict:
        """
        Fallback: Create skill based on knowledge gap analysis.
        """
        # Analyze existing skills
        analysis = analyze_existing_skills(self.domain)
        
        # Identify most significant gap
        gap = self.identify_priority_gap(analysis)
        
        # Create skill for that gap
        skill = self.build_skill_from_knowledge(gap)
        
        return {
            'skill_created': skill['name'],
            'based_on': 'gap_analysis',
            'api_available': False,
            'gap_addressed': gap['description']
        }
    
    def identify_priority_gap(self, analysis: dict) -> dict:
        """Find the most important missing skill."""
        # Prioritize by:
        # 1. Core domain concepts not covered
        # 2. Practical implementation gaps
        # 3. Complementarity with existing skills
        
        gaps = analysis['gaps']
        return max(gaps, key=lambda g: g['importance_score'])
```

## Real-World Example

**Scenario**: Daily cron job to search arXiv and create quantum computing skills

**What Happened**:
1. arXiv API returned 502 errors
2. Multiple retry strategies failed
3. Activated fallback: analyzed 75 existing quantum skills
4. Identified gap: quantum ML data loading techniques
5. Created comprehensive skill from domain knowledge

**Result**: Task completed successfully despite API failure

## Benefits of This Approach

1. **Resilience**: Research pipeline continues despite external failures
2. **Knowledge Consolidation**: Forces review of existing skills
3. **Gap Filling**: Identifies and addresses missing areas
4. **Value Creation**: Still produces useful output

## Proven Fallback: web_search When arXiv API is Down

When `curl` to `export.arxiv.org` times out (direct AND with `--proxy`), `web_search` is the most reliable fallback.

### What works
- `web_search("spiking neural network 2026 new research paper")` → returns Nature, IEEE, arXiv, Frontiers results
- `web_search("brain inspired computing neuromorphic 2026 latest")` → returns industry reports + academic papers
- Combine with `session_search` to recover past cron session paper findings

### What does NOT work
- `web_extract()` **blocks arxiv.org and nature.com URLs** — returns "Blocked: URL targets a private or internal network address"
- Broad/generic queries like `"neural network paper April 2026 arxiv"` → **returns empty results**
- Must use **specific domain terms** in queries (e.g., "spiking neural network", "neuromorphic computing")

### Query Tuning Rules
1. Include **domain-specific terminology** (not just "neural network")
2. Include **year** to filter recent results
3. Include **venue hints** ("Nature", "IEEE", "arxiv") when targeting academic sources
4. Try **multiple query formulations** if first returns empty — Chinese queries also work for Chinese-language sources

### Combining Sources
When presenting results, combine:
1. `web_search` results (current, real-time)
2. `session_search` cron history (past automated research)
3. Existing skill knowledge base (if relevant skills exist)

## Activation Keywords

- api fallback
- research pipeline resilience
- external api failure
- knowledge-based skill creation
- gap analysis
- 研究API故障
- 备用策略

## Related Skills

- `arxiv-search` - Primary paper search
- `skill-creator` - Skill creation workflow
- `skill-extractor` - Pattern extraction
- `autoresearch` - Autonomous research loops

## Tools Used

- `exec`: Retry API calls, analyze skill directories
- `read`: Examine existing skills
- `write`: Create new skill from knowledge
- `search_files`: Find related skills

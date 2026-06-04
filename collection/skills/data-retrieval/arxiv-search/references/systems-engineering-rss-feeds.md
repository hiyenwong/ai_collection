# Systems Engineering RSS Feeds (Verified 2026-06-02)

**Session**: 2026-06-02 Systems Engineering Research Cron Job  
**Categories**: `cs.SE+cs.DC+cs.SY+eess.SY+cs.NI+cs.MA+cs.CR`  
**Yield**: ~171 papers (combined categories)

## Feed Composition

The systems engineering RSS feed combines 7 arXiv categories covering core systems engineering domains:

```bash
curl -s "https://rss.arxiv.org/rss/cs.SE+cs.DC+cs.SY+eess.SY+cs.NI+cs.MA+cs.CR"
```

### Category Breakdown

| Category | Domain | Typical Content |
|----------|--------|-----------------|
| `cs.SE` | Software Engineering | Development methodologies, testing, verification, requirements, architecture |
| `cs.DC` | Distributed Computing | Cloud, distributed systems, fault tolerance, consensus, scalability |
| `cs.SY` | Systems and Control | Control theory, cyber-physical systems, automation, feedback systems |
| `eess.SY` | Systems Engineering (EESS) | Hardware systems, embedded systems, control systems, robotics |
| `cs.NI` | Networking and Internet Architecture | Protocols, routing, networked systems, IoT, edge computing |
| `cs.MA` | Multiagent Systems | Agent coordination, distributed AI, swarm systems, cooperative systems |
| `cs.CR` | Cryptography and Security | Security protocols, privacy, access control, secure systems |

## Paper Filtering Keywords

Systems engineering research often requires keyword filtering on title + abstract:

```python
keywords = [
    'systems engineering',
    'system design',
    'distributed systems',
    'control systems',
    'cyber-physical systems',
    'CPS',
    'model-based systems engineering',
    'MBSE',
    'digital twin',
    'fault tolerance',
    'resilience',
    'verification',
    'testing',
    'architecture',
]
```

### Time-Based Filtering

From RSS `<pubDate>` fields, parse dates and filter by:
- **Last 7 days**: `datetime.now() - timedelta(days=7)`
- **Last 14 days**: Standard for comprehensive weekly research
- **Last 30 days**: Monthly monitoring

```python
from datetime import datetime, timedelta, timezone

def filter_recent(papers, days=14):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent = []
    for paper in papers:
        pub_date = datetime.fromisoformat(paper['pub_date'].replace('Z', '+00:00'))
        if pub_date >= cutoff:
            recent.append(paper)
    return recent
```

## Verified Session Workflow (2026-06-02)

1. **RSS Download**: `curl -o /tmp/arxiv_systems.xml "https://rss.arxiv.org/rss/cs.SE+cs.DC+cs.SY+eess.SY+cs.NI+cs.MA+cs.CR"`
2. **Parse XML**: Python script extracts `<item>` elements → title, link, description, pubDate
3. **Date Filter**: Keep papers from last 14 days → 171 papers
4. **Keyword Filter**: Optional title/abstract keyword matching
5. **Skill Creation**: Select 1-2 most innovative papers for skill creation

## Yield Analysis

| Feed Combination | Raw Entries | After 14d Filter | Keyword Filtered |
|------------------|-------------|------------------|------------------|
| All 7 categories | ~2000+ | ~171 | varies by keywords |
| cs.SE+cs.DC+cs.SY only | ~500-800 | ~50-80 | higher concentration |
| cs.SY+eess.SY (control focus) | ~300-400 | ~30-50 | control systems specific |

## Cross-Domain Papers

The combined feed captures cross-domain papers at intersections:

- **CPS + Security**: `cs.SY` + `cs.CR` → secure cyber-physical systems
- **Distributed + Control**: `cs.DC` + `cs.SY` → distributed control systems
- **Networking + Multiagent**: `cs.NI` + `cs.MA` → networked agent coordination
- **Software Engineering + Distributed**: `cs.SE` + `cs.DC` → distributed software systems

## Alternative Narrower Feeds

For focused research, use subset combinations:

```bash
# Control systems focus
curl -s "https://rss.arxiv.org/rss/cs.SY+eess.SY"

# Distributed systems focus
curl -s "https://rss.arxiv.org/rss/cs.DC+cs.NI"

# Software engineering + testing
curl -s "https://rss.arxiv.org/rss/cs.SE"

# Multiagent + distributed coordination
curl -s "https://rss.arxiv.org/rss/cs.MA+cs.DC"
```

## Session Evidence (2026-06-02 Cron)

**arXiv API timeout**: API query timed out → pivoted to RSS feed approach  
**RSS success**: Feed download + Python file parse yielded 171 recent papers  
**Selected papers**:
- arXiv:2605.30985 - Kairos: CPS timing-induced interaction testing (20 new bugs, 34 known issues)
- arXiv:2605.30763 - Distributed MPC for building demand response coordination

## Integration with Skill Creation

After RSS discovery, standard workflow:

1. Parse papers → JSON file (`/tmp/arxiv_systems_papers.json`)
2. Select 1-2 most innovative papers (novel methodology, significant results)
3. Create skills using `skill_manage(action='create')`
4. Sync to ai_collection project
5. Update INDEX.md with arxiv_id entries
6. Git commit + push
7. Update kg.db with paper entities

## Related References

- [systems-engineering-quantum-rss-discovery.md](systems-engineering-quantum-rss-discovery.md) - systems engineering + quantum intersection
- [systems-engineering-quantum-feeds.md](systems-engineering-quantum-feeds.md) - quantum-enhanced systems engineering feeds
- [neuroscience-rss-feeds.md](neuroscience-rss-feeds.md) - neuroscience-specific feeds (~331 papers)
- [math-statistics-quantum-feeds.md](math-statistics-quantum-feeds.md) - math/statistics + quantum (~390 papers)

## Pitfalls

- **Weekend RSS skip days**: RSS feeds return empty on Saturday/Sunday (`<skipDays>` in feed XML) → fall back to browser category listing
- **Date parsing**: RSS `<pubDate>` format may vary; use timezone-aware datetime comparison
- **Large combined feeds**: 7-category feed returns thousands of entries → parse all but filter by date before keyword matching
- **Cross-domain filtering**: Keyword filtering may miss relevant papers if keywords too narrow → use broader systems engineering terms first
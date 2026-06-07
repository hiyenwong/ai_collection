# Neuroscience RSS Feed Combinations

Verified feed URLs for neuroscience paper discovery (confirmed 2026-05-29).

## Primary Neuroscience Feeds

### Core Neuroscience + AI/ML Intersection
```bash
# Most comprehensive: Neuroscience + Neural/Evolutionary Computing + AI + ML
curl -o /tmp/neuroscience_arxiv.xml "https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG"
# Yields: ~331 papers (verified 2026-05-29)
```

### Narrower Subsets
```bash
# Pure neuroscience
curl -o /tmp/neuro.xml "https://rss.arxiv.org/rss/q-bio.NC"
# Yields: ~50-100 papers

# Neuroscience + Neural Computing only
curl -o /tmp/neuro_ne.xml "https://rss.arxiv.org/rss/q-bio.NC+cs.NE"
# Yields: ~150 papers

# Neuroscience + AI only
curl -o /tmp/neuro_ai.xml "https://rss.arxiv.org/rss/q-bio.NC+cs.AI"
# Yields: ~180 papers
```

## Category Definitions

| Category | Description | Typical Content |
|----------|-------------|-----------------|
| `q-bio.NC` | Neurons and Cognition | Brain imaging, neural coding, cognitive modeling, BCI |
| `cs.NE` | Neural and Evolutionary Computing | Spiking neural networks, neuromorphic hardware, SNN training |
| `cs.AI` | Artificial Intelligence | General AI, reasoning, agents, cognitive architectures |
| `cs.LG` | Machine Learning | Deep learning, transformers, representation learning |
| `stat.ML` | Machine Learning (Statistics) | Bayesian methods, probabilistic models |

## High-Yield Keywords for Filtering

After downloading RSS feed (~300+ papers), filter by keywords to identify most relevant:

```python
import re

HIGH_PRIORITY_KEYWORDS = [
    'brain network', 'neural dynamics', 'spiking neural network',
    'computational neuroscience', 'brain-computer interface', 'BCI',
    'fMRI', 'EEG', 'MEG', 'neural encoding', 'neural decoding',
    'brain foundation model', 'neural representation', 'cognitive',
    'neuromorphic', 'synaptic plasticity', 'working memory',
    'hippocampal', 'cortical', 'motor imagery', 'visual decoding',
]

def is_high_priority(title, abstract):
    text = (title + ' ' + abstract).lower()
    return any(kw in text for kw in HIGH_PRIORITY_KEYWORDS)
```

## RSS 2.0 Parsing Pattern

arXiv neuroscience feeds return RSS 2.0 **without CDATA**. Parse directly:

```python
import re

def parse_neuroscience_rss(xml_path):
    with open(xml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    papers = []
    for item in re.findall(r'<item>(.*?)</item>', content, re.DOTALL):
        title = re.search(r'<title>(.*?)</title>', item, re.DOTALL)
        link = re.search(r'<link>(.*?)</link>', item, re.DOTALL)
        desc = re.search(r'<description>(.*?)</description>', item, re.DOTALL)
        
        if title and link:
            arxiv_id = re.search(r'arxiv\.org/abs/([\d.]+)', link.group(1))
            abstract_match = re.search(r'Abstract:\s*(.*)', desc.group(1) if desc else '', re.DOTALL)
            
            papers.append({
                'id': arxiv_id.group(1) if arxiv_id else '',
                'title': title.group(1).strip(),
                'link': link.group(1).strip(),
                'abstract': abstract_match.group(1).strip() if abstract_match else '',
            })
    
    return papers
```

## Recent High-Value Discoveries (2026-05-29)

| arXiv ID | Title | Categories | Key Innovation |
|----------|-------|------------|----------------|
| 2605.29591 | Mind-Omni: Unified Brain-Vision-Language Modeling | q-bio.NC, cs.CV, cs.AI | Brain Tokenizer + discrete diffusion, 7 tasks unified |
| 2605.29355 | Neural-Behavioral Whole-Body Movement Decoding | q-bio.NC, cs.NE | Epidural cortical signals → full-body motion in freely moving monkeys |

## Cross-Domain Combinations

For interdisciplinary neuroscience research:

```bash
# Neuroscience + Quantum (sparse intersection)
curl -o /tmp/neuro_quantum.xml "https://rss.arxiv.org/rss/q-bio.NC+quant-ph"
# Keyword filter: "quantum" in title/abstract → yields 0-5 papers typically

# Neuroscience + Medical Imaging
curl -o /tmp/neuro_med.xml "https://rss.arxiv.org/rss/q-bio.NC+eess.IV"
# Keyword filter: "medical", "clinical", "diagnosis" → yields 5-15 papers

# Neuroscience + Robotics
curl -o /tmp/neuro_robot.xml "https://rss.arxiv.org/rss/q-bio.NC+cs.RO"
# Keyword filter: "robot", "motor control", "embodied" → yields 10-20 papers
```

## Two-Step Mandatory Pattern

Security guardrail blocks `curl | python3`. Always:

1. **Download**: `curl -o /tmp/neuroscience_arxiv.xml "https://rss.arxiv.org/rss/q-bio.NC+cs.NE+cs.AI+cs.LG"`
2. **Parse**: `python3 parse_papers.py /tmp/neuroscience_arxiv.xml`

## Best Practices

- **Filter after download**: Don't try narrow RSS combinations — download broad feeds, then keyword-filter in Python
- **Combine 3-4 categories**: `q-bio.NC+cs.NE+cs.AI+cs.LG` gives best yield for computational neuroscience
- **Check duplicates**: Before creating skills, search existing skills with `grep -rl "{arxiv_id}" ~/.hermes/skills/*/SKILL.md`
- **Validate skill names**: Use `init_skill.py`, write SKILL.md, then `quick_validate.py` before syncing to ai_collection

## Related Reference Files

- [neuroscience-cron-workflow.md](neuroscience-cron-workflow.md) — Full cron workflow
- [quantum-finance-feeds.md](quantum-finance-feeds.md) — Quantum + finance feeds
- [systems-engineering-quantum-feeds.md](systems-engineering-quantum-feeds.md) — Systems engineering feeds
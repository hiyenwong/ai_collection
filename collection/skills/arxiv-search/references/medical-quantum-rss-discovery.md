# Medical + Quantum RSS Discovery Pattern (2026-05-27)

## RSS Feeds for Cross-Domain Discovery

For automated cron jobs, RSS feeds are the most reliable zero-rate-limit method for discovering cross-domain papers.

### Medical + Quantum Intersection
```python
feeds = [
    'https://rss.arxiv.org/rss/quant-ph',           # All quantum physics
    'https://rss.arxiv.org/rss/q-bio',              # All quantitative biology
    'https://rss.arxiv.org/rss/cs.LG+quant-ph',     # ML + Quantum
]
```

### Filtering Strategy
After fetching RSS feeds, filter for cross-domain relevance:
```python
medical_keywords = ['medical', 'health', 'clinical', 'drug', 'therapy', 
                    'diagnosis', 'bio', 'protein', 'molecular', 'imaging', 
                    'mri', 'fmri', 'enzyme', 'genome', 'fold', 'metab']

for paper in all_papers:
    text = (paper['title'] + ' ' + paper.get('abstract','')).lower()
    if 'quantum' in text and any(kw in text for kw in medical_keywords):
        # Cross-domain match
```

### Today's Verified Yields
- quant-ph RSS: ~1000+ entries, filtered to ~5 medical-relevant papers
- q-bio RSS: Papers in quantitative biology, some with quantum connections
- cs.LG+quant-ph: ML + quantum intersection papers

### Key Papers Found (2026-05-27)
- 2605.24617: Transformer refined quantum sampling for electronic structure (drug discovery relevance)
- 2605.24824: Point-group symmetry analysis on quantum computer (molecular simulation)
- 2605.24935: Nuclear isomer quantum battery (energy storage)
- 2605.25049: Global quantum phase estimation via hybrid learning (quantum metrology)
- 2605.25768: Expressibility-trainability trade-off in HQNNs (quantum ML)

### Notes
- RSS returns XML with `<item>` elements containing `title`, `link`, `description`, `pubDate`
- Extract arxiv ID from link: `re.search(r'arxiv\.org/abs/([\d.]+)', link)`
- Description contains arxiv abstract with some XML noise — clean with `re.sub(r'<[^>]+>', '', text)`
- No rate limits, works reliably in cron/automated contexts

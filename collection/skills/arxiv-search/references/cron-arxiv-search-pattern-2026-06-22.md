# Cron arXiv Search Pattern — 2026-06-22 (Monday: Neuroscience + Quantum)

## Session Summary

- **Topic**: Neuroscience (weekly Monday) + Quantum Mechanics (daily)
- **Network status**: web_search failed (Firecrawl NoneType), web_extract blocked arxiv.org, curl proxy returned empty strings
- **Discovery method**: browser_navigate to `/list/q-bio.NC/recent` and `/list/quant-ph/recent` listing pages
- **Papers from q-bio.NC listing**: 2606.19739, 2606.20345, 2606.20096, 2606.19081, 2606.18667, 2606.17745, 2606.17736
- **Domain saturation**: 4/7 q-bio.NC papers already had skills (sfmc, bipartite-oscillator, retrieval-based-brain-decoding, neurrate-single-cell)
- **New skill created**: `qutrit-entropy-estimation` from 2606.20504 (quant-ph + cs.LG)
- **kg.db state**: 375 papers, 173 skilled, 2749 entities, 9551 vectors

## Key Verified Patterns This Session

### browser_navigate Listing Extraction (MOST RELIABLE)
```
browser_navigate → https://arxiv.org/list/q-bio.NC/recent
browser_navigate → https://arxiv.org/list/quant-ph/recent
```
Snapshot reliably returns paper IDs, titles, authors, subjects. This is the #1 most reliable method when other tools fail.

### Cross-Reference Pattern for New Papers
When kg.db shows paper already has skill_name, skip creation. When skill_name is empty or null, create skill.

### VQA/CNN Transition Pattern (from 2606.20504)
- VQAs effective for ≤3 qutrits (~120 params)
- CNN estimators scale better for 4-5+ qutrits (12.5% MUB measurements, 0.13-0.16 nats error)
- This VQA→CNN transition is a general pattern applicable to other quantum estimation problems
# Cross-Category Neuroscience Discovery Strategy (2026-07-03)

## Problem
When q-bio.NC (primary neuroscience category) shows 100% skill coverage for all recent papers, a cron job would normally report "[SILENT]" with no new skills created. This session demonstrated a reliable fallback strategy.

## Solution: Scan Cross-Listed Categories

### Step 1: Verify q-bio.NC Saturation
```bash
# browser_navigate to listing page
browser_navigate("https://arxiv.org/list/q-bio.NC/recent")

# Extract all paper IDs via browser_console
# Then check each for existing skill:
for id in 2607.00851 2607.00397 2606.31944 ...; do
  result=$(grep -rl "$id" ~/.hermes/skills/ 2>/dev/null | head -1)
  [ -z "$result" ] && echo "NO SKILL: $id" || echo "HAS SKILL: $id"
done
```

### Step 2: Scan cond-mat.dis-nn (Disordered Systems and Neural Networks)
```javascript
// browser_console extraction on listing page
(() => {
  const dts = document.querySelectorAll('dl dt');
  const dds = document.querySelectorAll('dl dd');
  const results = [];
  for (let i = 0; i < Math.min(dts.length, dds.length); i++) {
    const idMatch = dts[i].textContent.match(/arXiv:(\d+\.\d+)/);
    const id = idMatch ? idMatch[1] : '';
    const ddText = dds[i].textContent.trim();
    const titleMatch = ddText.match(/Title:\s*(.+?)(?:\n|$)/);
    const title = titleMatch ? titleMatch[1].trim() : '';
    const lowerTitle = title.toLowerCase();
    const isNeuro = lowerTitle.includes('spiking') || lowerTitle.includes('neural') ||
                    lowerTitle.includes('brain') || lowerTitle.includes('cognit') ||
                    lowerTitle.includes('oscillat') || lowerTitle.includes('synap') ||
                    lowerTitle.includes('neuron') || lowerTitle.includes('recurrent') ||
                    lowerTitle.includes('attractor') || lowerTitle.includes('learning') ||
                    lowerTitle.includes('plasticity') || lowerTitle.includes('dynamical');
    if (isNeuro) results.push({id, title});
  }
  return JSON.stringify(results);
})()
```

### Step 3: Scan cs.NE (Neural and Evolutionary Computing)
Same JS extraction with neuroscience keyword filter.

### Step 4: False Positive Filtering
CS.NE papers matching "neural" keyword are often generic ML theory, NOT neuroscience:
- **2606.31581** "Robustness of neural networks to random noise" → generic ML robustness theory, NOT neuroscience
- **2606.28662** "Closed-Form Steepest Descent toward Flat Minima" → generic ML optimization, NOT neuroscience

**Rule**: Always `browser_navigate` to `/abs/{id}` and verify the abstract contains neuroscience-specific methodology (brain, spiking substrate, neural dynamics, synaptic, cortical, neural population, etc.) before creating a skill. Papers in cs.NE with "neural network" in the title are almost always about artificial neural networks, not biological neuroscience.

## Verified Results (2026-07-03)

| Category | Papers Scanned | Neuroscience Matches | NO SKILL | Novel Skills Created |
|----------|---------------|---------------------|----------|---------------------|
| q-bio.NC | 16 | 16 | 0 | 0 (100% saturated) |
| cond-mat.dis-nn | 30 | 7 | 3 | 2 |
| cs.NE | 45 | 11 | 2 | 0 (false positives) |

### Novel Papers Found
1. **2606.28486** (cond-mat.dis-nn) - "Spectral phase transitions and trainability in neural network learning dynamics" → BBP transitions during SGD, Marchenko-Pastur bulk evolution, trainability phase diagram → skill: `spectral-phase-transitions-nn-learning`
2. **2606.26989** (cond-mat.dis-nn) - "Physical Neural Networks Need Nonlinearity, Amplification, and Suppression for Learning" → three essential ingredients for physical computing, circuit designs → skill: `physical-nn-nonlinearity-amplification-suppression`

### Rejected (False Positives from cs.NE)
- **2606.31581** - "Robustness of neural networks" - generic ML robustness, no neuroscience content
- **2606.28662** - "Closed-Form Steepest Descent" - generic ML optimization, no neuroscience content

## curl RSS Alternative (faster, no browser needed)
This session used browser-based extraction above, but a simpler terminal-only approach works equally well: `curl` RSS feeds to XML files, then parse with Python ElementTree. See [references/rss-multi-category-sweep.md](rss-multi-category-sweep.md) for the complete workflow with keyword lists and category yield rankings.

## Key Takeaway
cond-mat.dis-nn is the **highest-yield secondary category** for neuroscience discovery when q-bio.NC is saturated. It contains physics-inspired neural network theory papers (random matrix theory, dynamical systems, physical computing) that are genuinely cross-domain neuroscience. cs.NE should be scanned but filtered aggressively for false positives.

## Title Extraction Format
`dd.textContent` on arXiv listing pages returns:
```
Title:\n          {actual title}\n        \n        {authors}...
```

The title is indented on the line after the "Title:" label. Use regex `/Title:\s*(.+?)(?:\n|$)/` to extract. The `childNodes[0]` approach returns empty strings.

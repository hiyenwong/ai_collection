# Browser-Based arXiv Discovery + PDF-to-Text Reading Pipeline

When arXiv API is rate-limited (common during peak hours) or web_search/web_extract block arXiv URLs, use this reliable browser-based pipeline for paper discovery and deep reading.

## Step 1: Discover New Papers via Browser

Navigate to the arXiv "new listings" page for your category:

```
browser_navigate("https://arxiv.org/list/{category}/new")
```

Recommended categories for neuroscience research:
- `q-bio.NC` — Neurons and Cognition
- `cs.NE` — Neural and Evolutionary Computing  
- `cs.LG` — Machine Learning (cross-listed papers)

The listing page shows: title, authors, abstract (truncated), arXiv ID, submission date.

**To see full abstract**: click the "▽ More" link — it expands inline without reloading.

## Step 2: Select Papers for Deep Reading

Criteria for selection:
- **Relevance**: matches research keywords (spiking neural network, brain network, neural dynamics, computational neuroscience, criticality)
- **Freshness**: submitted within last 24-48 hours
- **Novelty**: offers new mechanism, framework, or theoretical insight

## Step 3: Download and Read Full PDF

Use `curl` with proxy to download the PDF, then `pdftotext` for text extraction:

```bash
export https_proxy=http://127.0.0.1:7890
curl -sL -o /tmp/paper_{arxiv_id}.pdf "https://arxiv.org/pdf/{arxiv_id}" --max-time 30
pdftotext /tmp/paper_{arxiv_id}.pdf /tmp/paper_{arxiv_id}.txt
wc -l /tmp/paper_{arxiv_id}.txt
```

## Step 4: Extract Key Information

Read the text file in sections:

```
read_file(path="/tmp/paper_{arxiv_id}.txt", limit=200)        # Abstract + intro
read_file(path="/tmp/paper_{arxiv_id}.txt", offset=201, limit=200)  # Results
```

Key sections to extract: Abstract, Introduction (problem/motivation), Methods/Results (technical approach, key findings), Discussion (implications, limitations).

## Step 5: Create or Patch Skill

Use `skill_manage` to create/patch the AI collection skill with:
1. Frontmatter: name, description, tags, arXiv ID, authors, date
2. Overview + Key Contributions (detailed)
3. Methodology/Architecture
4. Key Results (tables for comparisons)
5. Activation keywords
6. Related Works and Future Directions

## Advantages Over API-Based Search

| Method | Reliability | Content Depth | Speed |
|--------|------------|---------------|-------|
| Browser to new listings | High (no rate limits) | Abstracts only | Fast |
| Curl to arXiv API | Low (429 rate limits) | Full metadata | Slow |
| web_search/web_extract | Fails (blocks arXiv) | None | — |
| Browser + PDF download | High | Full text | Medium |

## Pitfalls

- `arxiv.org/list/{category}/YYYY-MM-DD` does NOT work — returns "Listing requires subject and valid time period parameters"
- Always use `arxiv.org/list/{category}/new` for latest listings
- curl without `--max-time` may hang indefinitely — always set a timeout
- pdftotext output includes figure labels and references — navigate with offset/limit
- For long papers >50 pages, read in 200-line chunks

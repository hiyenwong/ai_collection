---
name: consulting-report-search
description: >-
  Consulting and industry report search and QA skill that prioritizes iResearch
  free reports. Use for consulting report search, industry report QA, iResearch
  report lookup, and market research report search.
---

# Consulting Report Search

## Description

Search, question-answering, and insight-generation skill for consulting reports, industry reports, and market research reports. By default, it prioritizes free iResearch reports, uses the iResearch list API for primary recall, then uses several public iResearch index pages as native quantitative snapshot sources, and finally uses QuestMobile public reports as a later fallback source. Results must always show iResearch formal reports first. When formal reports are not enough, iResearch index snapshots should come before QuestMobile because they are still native iResearch data products. The skill is intended not only to retrieve sources but also to behave like a lightweight consulting analyst: identify the real decision question, ask a small number of clarifying questions when scope is vague, reason from first principles, and then synthesize market insight, industry structure, and future-trend hypotheses from the evidence set.

Within each source, the default ranking mode is now newest-first, then relevance. The default sort direction is descending, so newer reports appear before older ones. If needed, agents can switch to relevance-first with an explicit CLI flag, or override the direction explicitly. If the user query itself contains a year such as `2024`, `2025`, or `2026`, ranking should instead prioritize year signals in the report title first, then report relevance, then publication time, and all three dimensions should be treated in descending order.

## Activation Keywords

- 咨询报告搜索
- 行业报告问答
- 艾瑞报告
- 艾瑞咨询
- 市场研究报告
- iresearch report
- report search
- market research report

## Tools Used

- exec: Run the bundled script to fetch iResearch and QuestMobile search results and detail pages
- exec: Run the bundled script to fetch iResearch and QuestMobile search results, detail pages, and iResearch index snapshots
- read: Load the skill reference file for source behavior, encoding notes, and parsing rules
- write: Save search results or answer drafts when needed
- browser or web search tools: Use browser-based or available web-search capability when both primary sources fail to return reports

When public index pages are involved, agents should prefer mining the page's own request API, JS bundle, or network data source before relying on brittle rendered-text extraction.

## Installation

No extra third-party packages are required. The script uses only the Python standard library.

For iResearch specifically, the logical default `pageSize` is 100 items. However, the current live public endpoint can fail when asked for 100 items in a single backend call, so the bundled script transparently splits large iResearch fetches into multiple smaller requests while still preserving the user-facing default of 100.

### Prerequisites

- Network access to https://www.iresearch.com.cn/ and https://report.iresearch.cn/
- Network access to https://www.questmobile.com.cn/research/reports/
- Python 3.10+ to run the script

## Usage Patterns

### Search Reports

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "AI营销" --pages 8 --limit 20 --sort-by recency --sort-order desc --grouped --format markdown
```

Fetch multiple pages from the iResearch free report feed, then use public iResearch index pages as native data-snapshot supplements, and only then pull QuestMobile pages as later fallback coverage. The default search depth is now 8 pages of iResearch results with a logical page size of 100, so the script starts from a much larger newest-first window before falling back. If the initial iResearch window still does not produce enough relevant matches, the script now automatically expands the iResearch search deeper, up to 20 logical pages in total, before later-source filling is allowed. Final ranking must still keep iResearch formal reports first.

The script also includes several public iResearch index pages as data-snapshot sources:

- `AI应用指数 AI APP Index`
- `移动APP指数 Mobile App Index`
- `网络广告指数 Online Advertising Index`
- `移动设备指数 Mobile Device Index`
- `视频媒体内容指数 Media Video Index`

These are not formal reports. Treat them as quantitative snapshot pages that can supplement report analysis when the user needs market rankings, app/device/video popularity, ad投入强度, or AI-app leaderboard context.

By default, results are sorted by publish time first and relevance second within each source. The default sort direction is `desc`. Use `--sort-by relevance` only when the user explicitly prefers stronger keyword matching over freshness.

If the query contains a year, override the normal within-source sort and use: title year, then relevance, then publication time. All three are descending. This helps queries like `2025 AI营销` or `2024 飞行汽车` prefer reports whose titles explicitly carry the requested year.

Markdown output also shows the active sort mode and any active `--since` filter at the top of the result block.

Every returned report should explicitly include a report link. This is a hard requirement. In structured output, use the `report_link` field. In Markdown output, show a `Report Link` line for each report. If a source item does not have a valid public report link, it should be dropped from list/search output instead of being returned as a bare title.

When multiple source types have matches, the mixed-source search now tries to fill the requested result window with as many relevant iResearch formal reports as possible first. If the initial newest window is not enough, it automatically keeps paging deeper into iResearch before later-source filling begins. After formal reports, iResearch index snapshots should fill the remaining slots before QuestMobile.

When the query itself clearly asks for an index, leaderboard, heat list, coverage-rate view, or other indicator-style snapshot, the matching iResearch index page should be promoted before the default recency-first fallback is applied. This avoids burying the right snapshot behind newer but less relevant formal reports or unrelated index pages.

If formal reports are still insufficient, the search flow can surface iResearch index snapshots before QuestMobile. These index pages should be presented as `index snapshot` data sources rather than mislabeled as reports.

If the user explicitly wants only iResearch, use `--iresearch-only`. This is the preferred flag for pure iResearch report collection workflows; `--no-questmobile` remains available as a lower-level compatibility switch.

### Fetch Report Details

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  detail freport.4694 --pages 8 --include-images --format markdown
```

Read the report detail page and return the summary, catalog, chart catalog, online reader link, and image links from the reader page.

The detail workflow should now also return a conservative interpretation, evidence boundary note, and structured outline sections derived from the public introduction, meta description, and public catalog. The interpretation should read like a short answer-oriented summary instead of a raw evidence dump.

QuestMobile detail pages are also supported through full URLs or `qm.<id>` identifiers.

### Answer a Question Against One Report

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  answer freport.4794 "这份报告主要讲什么？" --pages 8 --include-images --format markdown
```

Use `answer` when the user is asking a concrete question about one report rather than requesting a raw detail dump.

The answer mode should:

- fetch the same public detail evidence as `detail`
- generate a conservative answer grounded in public summary, outline sections, and chart catalog
- return explicit evidence snippets
- keep the evidence boundary visible
- include report and online-reading links for manual verification

### Generate Market and Industry Insight

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  insight "AI营销" --pages 8 --sort-by recency --sort-order desc --format markdown
```

Use `insight` when the user wants market judgement, industry structure analysis, competitive signals, or future-trend observation rather than a raw list of reports.

The insight mode should:

- search iResearch reports first, then use iResearch index snapshots as quantitative support
- actively keep relevant iResearch index snapshots in the candidate set even when enough formal reports already exist
- keep index cross-signals narrow and domain-aware rather than mixing every available index page into the same insight
- fetch a small set of detail pages from the strongest candidates
- synthesize an executive summary, market judgement, market signals, industry structure, competitive landscape, growth drivers, risk watchpoints, and future trends
- keep all conclusions tied to explicit evidence and report links
- clearly state the evidence boundary so trend conclusions remain conservative

### Browse Recent Free Reports

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  list --pages 2 --page-size 100 --format markdown
```

Use this to inspect the recent free-report pool before deciding which reports to summarize or use for QA.

### Search Reports with Explicit Source Groups

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "AI应用层" --pages 8 --limit 12 --sort-by recency --sort-order desc --since 2025-01-01 --grouped --format json
```

Use grouped output when you need a stable source-layered rendering format. This keeps iResearch and QuestMobile separated instead of interleaving them in a single list.

Use `--since` when the user explicitly wants only recent reports, for example limiting the result window to 2025 and later.

The hidden `--last-id` cursor parameter is deprecated for normal use and should only be used for debugging historical iResearch cursor windows.

## Instructions for Agents

### Step 0: Clarify the Real Client Intent

Before searching, decide whether the user is actually asking for report retrieval or for a business judgement that reports should support.

If the request is broad, ambiguous, or decision-oriented, ask 1 to 3 targeted follow-up questions instead of jumping straight into a result dump. Preferred clarification axes are:

- the decision to support, for example strategy, investment, product direction, or channel allocation
- scope, for example market, region, industry segment, customer group, or competitor set
- time horizon, for example current snapshot, yearly trend, or forward-looking view
- desired output, for example report list, benchmark table, grounded answer, or market insight memo

If the user does not answer and the query is still actionable, explicitly state the assumed framing and proceed.

### Step 1: Classify the Request

First determine whether the user wants:

- Report search
- Topic filtering or comparison
- QA grounded in one or more reports
- Lead collection for relevant reports
- Market insight or trend analysis

If the request involves industry status, trends, market size, cases, figures, or charts, start with iResearch by default.

If the request explicitly asks for market judgement, industry structure, competition, growth direction, or future trends, prefer the dedicated `insight` flow instead of returning only raw search results.

When the user sounds like an internal client rather than a librarian, restate the problem in consulting language before execution, for example: current market state, structural drivers, competitive pattern, growth constraints, and implications for the user's decision.

### Step 2: Search iResearch Free Reports First

Always use the bundled script first instead of jumping directly to broad web search:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "<query>" --pages 8 --limit 20 --format json
```

Execution requirements:

- Fetch a deep newest-first iResearch window by default; the current default is 8 logical pages with pageSize 100
- If relevant iResearch matches are still insufficient, automatically expand deeper up to 20 logical pages before falling back to QuestMobile
- Present iResearch matches first in the final answer
- Prefer returning as many relevant iResearch reports as possible before using QuestMobile to fill any remaining slots
- Use iResearch index snapshots only after formal report sources when the user needs public ranking or indicator-style data support
- If the query contains a year, prioritize title-year signals first, then relevance, then publication time, all in descending order
- Rank results within each source by newest publication time first, then relevance, with `--sort-order desc` as the default unless the user explicitly asks for a different order
- Include a report link for every returned report; do not return bare titles without a clickable destination
- Treat the report link as a hard requirement; drop linkless items from list/search output and fail detail-style flows if a valid public report link is unavailable
- If the user specifies an industry, add `--industry`
- If the user wants only newer reports, add `--since YYYY-MM-DD`
- Do not use `--last-id` in normal workflows; it is a deprecated debug-only cursor override
- Use iResearch index snapshots before QuestMobile when the user needs public leaderboard or indicator-style data
- Use QuestMobile only after iResearch reports and iResearch index snapshots have been considered
- Use `--iresearch-only` when the user explicitly wants only iResearch reports
- Prefer `--grouped` when the answer contains both iResearch and QuestMobile results

### Step 3: Use QuestMobile as the Secondary Source

If iResearch results are too sparse, or if the user asks for broader coverage, use the same search command without disabling QuestMobile:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "<query>" --pages 8 --limit 8 --sort-by recency --sort-order desc --format json
```

Rules for QuestMobile usage:

- Never place QuestMobile above iResearch in the final result order
- Use QuestMobile to fill gaps or broaden topical coverage only after iResearch results have been exhausted for the requested window
- When both sources match, present them in separate source layers rather than mixing them together
- In mixed-source result lists, keep QuestMobile after all iResearch entries and only use it to fill the remaining slots when iResearch results are insufficient
- Use multiple QuestMobile pages when broader coverage is needed instead of relying on the default landing page only

### Step 4: Pull Detail Evidence for QA

If the user wants a summary, explanation, or grounded answer instead of just report titles, fetch details for the top 1 to 3 candidate reports:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  detail <report-id-or-url> --pages 8 --include-images --format json
```

Prefer these fields as answer evidence:

- `summary`
- `interpretation`
- `evidence_boundary`
- `outline_sections`
- `catalog`
- `chart_catalog`
- `industry`
- `published_at`
- `online_read_url`
- `source`

If the user asks a direct question about one chosen report, prefer the dedicated answer flow:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  answer <report-id-or-url> "<question>" --pages 8 --include-images --format json
```

Prefer these fields from `answer` output when responding:

- `answer`
- `evidence`
- `evidence_boundary`
- `verification_links`
- `report_link`
- `online_read_url`

QuestMobile detail pages can additionally provide:

- article intro text
- section headings
- image URLs from the report body

For iResearch specifically, the preferred interpretation stack is:

1. `summary` from the public report introduction
2. detail-page meta description when it contains a richer synopsis
3. `outline_sections` extracted from the public catalog
4. online reader image links for manual page-level verification when needed

### Step 5: Build Insight Through Cross-Source Reasoning

If the user wants market, industry, or future-trend insight, use the dedicated analysis flow:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  insight "<query>" --pages 8 --format json
```

Reasoning framework:

1. Use formal iResearch reports as the primary explanatory layer
2. Use iResearch index snapshots as the primary quantitative-signal layer
3. Use QuestMobile only as a secondary supplement when the first two layers are insufficient
4. Start from first principles: define the object being analyzed, the unit of competition, the growth mechanism, the constraint or bottleneck, and the observable metric that reflects each one
5. Separate observed facts, causal interpretation, business implication, and future-looking judgement instead of mixing them together
6. Prefer conservative trend hypotheses such as "值得继续跟踪" or "更可能出现" instead of absolute prediction language

Recommended internal analysis scaffold:

- `What is the real market object?` category, scenario, budget pool, user demand, or channel
- `What are the core drivers?` technology, user behavior, distribution, regulation, or ROI
- `What is the structure?` upstream, downstream, platform, brand, entrant, incumbent
- `What is changing?` demand intensity, ranking, growth rate, concentration, or conversion efficiency
- `What follows for the client?` monitor, enter, avoid, re-segment, or validate further

When the user's question is still too broad for a responsible judgement, pause and ask a narrow follow-up such as:

- 你更关心市场空间、竞争格局、投放效率，还是头部玩家榜单？
- 你要看的是中国市场整体，还是某个具体赛道或细分客户群？
- 你希望输出的是报告清单，还是一个可以直接用于决策讨论的 insight 摘要？

The insight answer should normally include:

- `primary_signal_source`
- `secondary_signal_source`
- `executive_summary`
- `market_judgement`
- `market_signals`
- `industry_structure`
- `competitive_landscape`
- `growth_drivers`
- `risk_watchpoints`
- `future_trends`
- `evidence`
- `evidence_boundary`
- `analyzed_items`

When relevant iResearch index snapshots match the topic, the insight flow should keep at least one snapshot-style source in the evidence set whenever possible, instead of relying only on formal report summaries.

Cross-signal rules should be conservative. Prefer a primary matched snapshot plus at most one adjacent snapshot type when it genuinely helps interpretation. For example:

- device-oriented queries should prefer `device`, optionally `app`
- video-content queries should prefer `video`, optionally `app`
- ad-investment queries should prefer `ad`, optionally `app`
- AI-application queries should prefer `ai`, optionally `app`

Do not mix unrelated index pages into the same insight only because they are available.

### Step 6: State the Evidence Boundary Clearly

If only the summary, catalog, and chart catalog are available, restrict the answer to:

- What topics the report covers
- The rough research scope and chapter structure
- Which cases, trends, or indicators the report appears to cover

Do not convert the table of contents into claimed report conclusions. If the user asks for exact data points, page-level evidence, or chart-specific content:

- Explicitly say that current evidence comes mainly from the summary and catalog
- Use the `interpretation` field for a conservative reading of what the report is about, but do not treat it as a replacement for page-level evidence
- Use the `answer` mode when the user asks a concrete report-specific question, especially around summary, chapters, chart/data coverage, timing, source, or report links
- Provide the online reader link
- Use reader-page image links for page-by-page verification if needed

### Step 7: Expand Only When iResearch Is Not Enough

Use other sources only when:

- iResearch has no relevant report
- Free-report information is not enough to answer the question
- The user explicitly asks for multi-source comparison

If both iResearch and QuestMobile return no usable reports, switch to web search as the fallback discovery path. Prefer targeted report-page searches such as:

- `site:iresearch.cn/report <query> 报告`
- `site:questmobile.com.cn/research/report <query> 报告`
- `site:iresearch.com.cn <query> 艾瑞 报告`
- `site:questmobile.com.cn <query> QuestMobile 报告`

When web search finds a concrete report page URL, feed that URL back into the normal detail flow when possible instead of summarizing the search snippet alone.

For public dashboards or index pages, do not default to scraping rendered HTML text. Preferred data-source order is:

1. the page's own public request API
2. JS bundle or inline script that reveals endpoint names and payload structure
3. rendered DOM text extraction
4. generic web search fallback

If the page exposes a stable request API, use that API as the primary extraction path and keep HTML parsing only as a fallback.

When expanding, present sources in separate layers:

1. iResearch reports
2. iResearch index snapshots
3. QuestMobile reports
4. Web-search discovered report pages
5. Other public sources

Do not mix secondary sources into the first section.

## Context Files

### references/iresearch-api.md

Contains source parameters, pagination behavior, encoding notes, detail-page anchors, and parsing considerations for both iResearch and QuestMobile. Read it only when adjusting the script or debugging extraction issues.

## Error Handling

### Empty Search Results

```text
If search returns no reports:
  1. Increase --pages to confirm the result is not caused by shallow pagination
  2. Relax the query and keep only the core topic words
  3. Check whether QuestMobile has relevant public reports
  4. If both iResearch and QuestMobile still return nothing, switch to web search using report-focused site queries
  5. Prefer concrete report-page URLs over generic articles or landing pages
  6. Tell the user when the final candidates were found through web search fallback rather than the direct source APIs
```

### Garbled Detail Page or Missing Fields

```text
If detail parsing looks garbled:
  1. Confirm the page is decoded as gb18030 instead of forcing UTF-8
  2. For QuestMobile, confirm the page is decoded as UTF-8 and that the public HTML still exposes metadata blocks
  3. Check the HTML anchors documented in references/iresearch-api.md
  4. If only a few fields are missing, return the available fields instead of failing completely
```

### Only Summary and Catalog Are Available

```text
If the user asks for exact findings but only summary/catalog are available:
  1. Explain the current evidence boundary
  2. Provide the online reader link or image-page links
  3. Give a conservative answer grounded in visible evidence instead of inventing findings
```

## Configuration

### Optional Parameters

```bash
--pages 8
--page-size 100
--limit 5
--industry 广告营销
--sort-by recency
--sort-order desc
--since 2025-01-01
--include-images
--no-questmobile
--iresearch-only
--grouped
--format json
```

## Limitations

- This skill prioritizes iResearch free reports, then iResearch index snapshots, and only then uses QuestMobile public reports as later fallback coverage
- The iResearch index pages are public snapshot dashboards, not full reports, so they should be framed as data snapshots rather than report conclusions
- It does not cover private content that requires login or payment
- iResearch detail pages reliably expose the summary, catalog, chart catalog, and online reader entry point
- The hidden `--last-id` override can intentionally force older iResearch windows, so it should be treated as a debug-only compatibility flag
- QuestMobile search coverage depends on the public `article-list` API remaining stable
- The online reader is an image stream rather than structured text, so page-by-page verification is more expensive

## Best Practices

1. Search first, then answer. Do not give industry conclusions before locating reports.
2. Put iResearch results in the first section and QuestMobile in the second section. Use grouped output when both sources are present.
3. Ground factual claims in the summary, catalog, chart catalog, or article intro instead of over-inferring.
4. When recommending several reports, rank iResearch first, then rank within each source by recency and relevance by default. Keep `--sort-order desc` unless the user explicitly wants the oldest reports first. Use `--sort-by relevance` only when freshness is less important than lexical match.
5. If both built-in sources fail, do not stop at "no results". Run a web-search fallback with `site:` constraints to recover concrete report pages.
6. For market-insight tasks, do not jump directly from one title to a trend conclusion. First assemble at least one explanatory source and, when available, one quantitative snapshot source, then state the judgement and its evidence boundary separately.
7. In insight mode, explicitly separate four analytical layers: current structure, competition, growth drivers, and risk watchpoints. Do not compress all analysis into a single generic trend paragraph.
8. Behave like a consulting analyst rather than a search box: when the ask is underspecified, use a few targeted clarifying questions to narrow the decision context before concluding.
9. For public web data extraction, prefer the page's own request API and network model over brittle HTML heuristics.

## Examples

### Example 1: Search for AI Marketing Reports

```text
User: Help me find several consulting reports about AI marketing, prioritizing iResearch.

Agent Process:
1. Run the search subcommand against the iResearch free-report pool for "AI营销"
2. Keep QuestMobile enabled as the secondary source
3. Return the top relevant reports with iResearch first and QuestMobile second
4. Use grouped output so the source boundary is obvious

Agent: I will search the iResearch free-report pool first, then use QuestMobile as secondary coverage if needed. Results will still be presented with iResearch first in a grouped layout.
```

### Example 3: Fall Back to Web Search When Built-in Sources Miss

```text
User: Help me find reports about a niche topic, but the direct source search returns nothing.

Agent Process:
1. Search iResearch first
2. Search QuestMobile second
3. If both return no usable reports, switch to web search with report-focused site constraints
4. Prefer concrete report detail URLs over homepages or generic news pages
5. If a valid report URL is found, pass it back through the detail workflow or present it as a fallback-discovered report

Agent: The direct source APIs did not return a usable report for this query, so I will fall back to web search using report-focused site filters and return any concrete report pages I can verify.
```

### Example 4: Generate Market Insight

```text
User: I need to understand the market situation, industry structure, and future trend of AI marketing.

Agent Process:
1. Run the insight flow for "AI营销"
2. Let formal iResearch reports provide the explanatory layer
3. Let iResearch index snapshots provide quantitative or leaderboard-style support when available
4. Summarize the current market judgement, industry structure, and future trend watchpoints
5. Explicitly state which parts are observed evidence and which parts are conservative forward-looking judgement

Agent: I will synthesize iResearch reports and available iResearch index snapshots to produce a structured market insight for AI marketing, including current judgement, industry structure, future trends, and evidence boundaries.
```

### Example 2: Answer a Question Grounded in a Report

```text
User: According to iResearch reports, which application directions does AI marketing mainly cover?

Agent Process:
1. Search for "AI营销"
2. Run detail on the most relevant report
3. If iResearch evidence is insufficient, inspect one QuestMobile report as a secondary source
4. Summarize application directions from the summary, catalog, and available detail evidence
5. State which parts come from iResearch and which parts come from QuestMobile

Agent: Based on the summary and catalog of iResearch's "2024 China AI Applications in Marketing Industry Report," the currently supported application directions include data-driven decision support, content production, organizational and process transformation, and benchmark case analysis. QuestMobile can be used as a secondary source to extend public narrative coverage, but iResearch remains the primary evidence layer.
```

## Resources

- https://www.iresearch.com.cn/report.shtml
- https://www.iresearch.com.cn/api/products/GetReportList
- https://www.questmobile.com.cn/research/reports/
- ./references/iresearch-api.md

## Related Skills

- arxiv-search: Handles academic paper search rather than consulting or industry reports
- news-search: Handles news search and can be used as background supplementation
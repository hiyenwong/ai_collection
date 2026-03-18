---
name: consulting-report-search
description: >-
  Consulting and industry report search and QA skill that prioritizes iResearch
  free reports. Use for consulting report search, industry report QA, iResearch
  report lookup, and market research report search.
---

# Consulting Report Search

## Description

Search and question-answering skill for consulting reports, industry reports, and market research reports. By default, it prioritizes free iResearch reports, uses the iResearch list API for primary recall, then uses QuestMobile public reports as the secondary source. Results must always show iResearch first and QuestMobile second. The search workflow now supports deeper QuestMobile pagination and grouped output rendering, so mixed-source results can be shown as fixed source sections with iResearch first.

Within each source, the default ranking mode is now newest-first, then relevance. The default sort direction is descending, so newer reports appear before older ones. If needed, agents can switch to relevance-first with an explicit CLI flag, or override the direction explicitly.

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
- read: Load the skill reference file for source behavior, encoding notes, and parsing rules
- write: Save search results or answer drafts when needed

## Installation

No extra third-party packages are required. The script uses only the Python standard library.

### Prerequisites

- Network access to https://www.iresearch.com.cn/ and https://report.iresearch.cn/
- Network access to https://www.questmobile.com.cn/research/reports/
- Python 3.10+ to run the script

## Usage Patterns

### Search Reports

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "AI营销" --pages 6 --limit 5 --sort-by recency --sort-order desc --grouped --format markdown
```

Fetch multiple pages from the iResearch free report feed, then pull multiple QuestMobile pages from its public article-list API. Final ranking must still keep all iResearch matches ahead of QuestMobile matches, and grouped output should render iResearch as the first section and QuestMobile as the second section.

By default, results are sorted by publish time first and relevance second within each source. The default sort direction is `desc`. Use `--sort-by relevance` only when the user explicitly prefers stronger keyword matching over freshness.

Markdown output also shows the active sort mode and any active `--since` filter at the top of the result block.

Every returned report should explicitly include a report link. In structured output, use the `report_link` field. In Markdown output, show a `Report Link` line for each report.

When both sources have matches, the mixed-source search keeps iResearch first and reserves a small number of trailing slots for QuestMobile so the secondary-source reports are still visible.

### Fetch Report Details

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  detail freport.4694 --pages 8 --include-images --format markdown
```

Read the report detail page and return the summary, catalog, chart catalog, online reader link, and image links from the reader page.

QuestMobile detail pages are also supported through full URLs or `qm.<id>` identifiers.

### Browse Recent Free Reports

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  list --pages 2 --page-size 12 --format markdown
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

### Step 1: Classify the Request

First determine whether the user wants:

- Report search
- Topic filtering or comparison
- QA grounded in one or more reports
- Lead collection for relevant reports

If the request involves industry status, trends, market size, cases, figures, or charts, start with iResearch by default.

### Step 2: Search iResearch Free Reports First

Always use the bundled script first instead of jumping directly to broad web search:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "<query>" --pages 6 --limit 5 --format json
```

Execution requirements:

- Fetch at least 3 to 6 pages by default so the search is not limited to page 1
- Present iResearch matches first in the final answer
- Rank results within each source by newest publication time first, then relevance, with `--sort-order desc` as the default unless the user explicitly asks for a different order
- Include a report link for every returned report; do not return bare titles without a clickable destination
- If the user specifies an industry, add `--industry`
- If the user wants only newer reports, add `--since YYYY-MM-DD`
- Do not use `--last-id` in normal workflows; it is a deprecated debug-only cursor override
- Use QuestMobile only as the secondary source after iResearch results have been gathered
- Prefer `--grouped` when the answer contains both iResearch and QuestMobile results

### Step 3: Use QuestMobile as the Secondary Source

If iResearch results are too sparse, or if the user asks for broader coverage, use the same search command without disabling QuestMobile:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  search "<query>" --pages 6 --limit 8 --sort-by recency --sort-order desc --format json
```

Rules for QuestMobile usage:

- Never place QuestMobile above iResearch in the final result order
- Use QuestMobile to fill gaps or broaden topical coverage
- When both sources match, present them in separate source layers rather than mixing them together
- In mixed-source result lists, keep QuestMobile after all iResearch entries while still reserving a few slots so QuestMobile results remain visible
- Use multiple QuestMobile pages when broader coverage is needed instead of relying on the default landing page only

### Step 4: Pull Detail Evidence for QA

If the user wants a summary, explanation, or grounded answer instead of just report titles, fetch details for the top 1 to 3 candidate reports:

```bash
python collection/skills/consulting-report-search/scripts/iresearch_report_search.py \
  detail <report-id-or-url> --pages 8 --include-images --format json
```

Prefer these fields as answer evidence:

- `summary`
- `catalog`
- `chart_catalog`
- `industry`
- `published_at`
- `online_read_url`
- `source`

QuestMobile detail pages can additionally provide:

- article intro text
- section headings
- image URLs from the report body

### Step 5: State the Evidence Boundary Clearly

If only the summary, catalog, and chart catalog are available, restrict the answer to:

- What topics the report covers
- The rough research scope and chapter structure
- Which cases, trends, or indicators the report appears to cover

Do not convert the table of contents into claimed report conclusions. If the user asks for exact data points, page-level evidence, or chart-specific content:

- Explicitly say that current evidence comes mainly from the summary and catalog
- Provide the online reader link
- Use reader-page image links for page-by-page verification if needed

### Step 6: Expand Only When iResearch Is Not Enough

Use other sources only when:

- iResearch has no relevant report
- Free-report information is not enough to answer the question
- The user explicitly asks for multi-source comparison

When expanding, present sources in separate layers:

1. iResearch reports
2. QuestMobile reports
3. Other public sources

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
  4. Tell the user when iResearch has no precise match and QuestMobile is being used as secondary coverage
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
--pages 6
--page-size 12
--limit 5
--industry 广告营销
--sort-by recency
--sort-order desc
--since 2025-01-01
--include-images
--no-questmobile
--grouped
--format json
```

## Limitations

- This skill prioritizes iResearch free reports and uses QuestMobile public reports as secondary coverage
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
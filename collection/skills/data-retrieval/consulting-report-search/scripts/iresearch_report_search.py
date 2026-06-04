#!/usr/bin/env python3
"""Search and inspect consulting reports from iResearch and QuestMobile.

This script provides five subcommands:

- list: fetch the latest iResearch free reports
- search: search iResearch first, then QuestMobile as a secondary source
- detail: fetch a report detail page from either source and extract evidence
- answer: answer a question conservatively using one report's public evidence
- insight: synthesize market and industry insight from reports and index snapshots
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from datetime import datetime
import json
import re
import sys
from dataclasses import asdict, dataclass
from html import unescape
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

IRESEARCH_API_URL = "https://www.iresearch.com.cn/api/products/GetReportList"
IRESEARCH_DEFAULT_LAST_ID = ""
IRESEARCH_DEFAULT_PAGE_SIZE = 100
IRESEARCH_MAX_BATCH_SIZE = 50
SEARCH_DEFAULT_PAGES = 8
SEARCH_DEFAULT_LIMIT = 20
SEARCH_AUTO_MAX_PAGES = 20
SEARCH_AUTO_PAGE_STEP = 2
QUESTMOBILE_LIST_URL = "https://www.questmobile.com.cn/research/reports/"
QUESTMOBILE_ARTICLE_LIST_URL = (
    "https://www.questmobile.com.cn/api/v2/report/article-list"
)
IRESEARCH_SOURCE = "iresearch"
QUESTMOBILE_SOURCE = "questmobile"
IRESEARCH_INDEX_SOURCE = "iresearch-index"
SOURCE_PRIORITY = {
    IRESEARCH_SOURCE: 0,
    IRESEARCH_INDEX_SOURCE: 1,
    QUESTMOBILE_SOURCE: 2,
}
JSON_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.iresearch.com.cn/report.shtml",
}
HTML_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
AD_INDEX_API_BASE_URL = "https://index.iresearch.com.cn"
AI_INDEX_API_BASE_URL = "https://ircloud.iresearchdata.cn/irs-index-api"


@dataclass(slots=True)
class ReportSummary:
    """Summary metadata for a report source item."""

    source: str
    report_id: str
    news_id: int
    title: str
    summary: str
    industry: str
    author: str
    published_at: str
    views: int
    keywords: list[str]
    price: int | None
    detail_url: str
    online_read_url: str | None


@dataclass(slots=True)
class ReportDetail:
    """Structured information extracted from a report detail page."""

    source: str
    report_id: str
    news_id: int
    title: str
    author: str | None
    published_at: str | None
    industry: str | None
    report_type: str | None
    page_count: int | None
    chart_count: int | None
    price: str | None
    detail_url: str
    online_read_url: str | None
    summary: str
    interpretation: str
    evidence_boundary: str
    outline_sections: list[str]
    catalog: str
    chart_catalog: str
    viewer_images: list[str]
    keywords: list[str]


@dataclass(slots=True)
class ReportAnswer:
    """Grounded answer generated from public report evidence."""

    source: str
    report_id: str
    title: str
    question: str
    answer: str
    evidence: list[str]
    evidence_boundary: str
    report_link: str
    online_read_url: str | None
    verification_links: list[str]


@dataclass(slots=True)
class InsightAnalysis:
    """Structured market insight synthesized from reports and index snapshots."""

    query: str
    primary_signal_source: str | None
    secondary_signal_source: str | None
    executive_summary: str
    market_judgement: str
    market_signals: list[str]
    industry_structure: list[str]
    competitive_landscape: list[str]
    growth_drivers: list[str]
    risk_watchpoints: list[str]
    future_trends: list[str]
    evidence: list[str]
    evidence_boundary: str
    source_breakdown: dict[str, int]
    analyzed_items: list[dict[str, str]]


@dataclass(frozen=True, slots=True)
class IndexSnapshotConfig:
    """Static configuration for an iResearch index snapshot page."""

    report_id: str
    news_id: int
    title: str
    detail_url: str
    industry: str
    report_type: str
    author: str
    keywords: list[str]
    summary_hint: str


@dataclass(slots=True)
class IndexSnapshotData:
    """Structured snapshot data extracted from a public index page or API."""

    snapshot_date: str
    summary: str
    outline_sections: list[str]
    chart_catalog: str
    keywords: list[str]


IRESEARCH_INDEX_CONFIGS = [
    IndexSnapshotConfig(
        report_id="irindex.ai",
        news_id=900001,
        title="AI应用指数 AI APP Index",
        detail_url="https://ircloud.iresearchdata.cn/ai-index/",
        industry="人工智能应用",
        report_type="Index snapshot",
        author="艾瑞数据",
        keywords=["AI", "APP", "活跃指数", "粘性指数", "人工智能"],
        summary_hint="AI应用指数提供人工智能 APP 的活跃指数、粘性指数、赛道分布和月榜快照，可用于观察 AI 应用热度与留存变化。",
    ),
    IndexSnapshotConfig(
        report_id="irindex.app",
        news_id=900002,
        title="移动APP指数 Mobile App Index",
        detail_url="https://index.iresearch.com.cn/app",
        industry="移动互联网",
        report_type="Index snapshot",
        author="艾瑞数据",
        keywords=["APP", "独立设备数", "使用次数", "赛道", "移动互联网"],
        summary_hint="移动APP指数展示行业独立设备数、使用次数、有效使用时间占比以及 APP 榜单与热门赛道变化。",
    ),
    IndexSnapshotConfig(
        report_id="irindex.ad",
        news_id=900003,
        title="网络广告指数 Online Advertising Index",
        detail_url="https://index.iresearch.com.cn/ad",
        industry="网络广告",
        report_type="Index snapshot",
        author="艾瑞数据",
        keywords=["广告", "投入指数", "品牌", "营销投放", "AdTracker"],
        summary_hint="网络广告指数展示广告主、品牌和终端维度的投入指数快照，可用于对比广告投放强度和竞品媒介布局。",
    ),
    IndexSnapshotConfig(
        report_id="irindex.device",
        news_id=900004,
        title="移动设备指数 Mobile Device Index",
        detail_url="https://index.iresearch.com.cn/device",
        industry="移动设备",
        report_type="Index snapshot",
        author="艾瑞数据",
        keywords=["设备", "厂商", "品牌", "覆盖率", "机型"],
        summary_hint="移动设备指数展示厂商品牌和机型覆盖率快照，可用于观察设备市场格局和终端分布。",
    ),
    IndexSnapshotConfig(
        report_id="irindex.video",
        news_id=900005,
        title="视频媒体内容指数 Media Video Index",
        detail_url="https://index.iresearch.com.cn/video/",
        industry="在线视频",
        report_type="Index snapshot",
        author="艾瑞数据",
        keywords=["视频", "电视剧", "综艺", "电影", "热播"],
        summary_hint="视频媒体内容指数提供电影、电视剧、综艺和动漫等内容热度榜单，可用于观察视频内容热播趋势。",
    ),
]


def clean_text(value: str) -> str:
    """Normalize HTML-decoded text."""
    value = unescape(value).replace("\u3000", " ").replace("\xa0", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def html_to_text(fragment: str) -> str:
    """Convert a small HTML fragment into newline-preserving plain text."""
    fragment = unescape(fragment)
    fragment = re.sub(r"<br\s*/?>", "\n", fragment, flags=re.IGNORECASE)
    fragment = re.sub(r"</p\s*>", "\n", fragment, flags=re.IGNORECASE)
    fragment = re.sub(r"</h[1-6]\s*>", "\n", fragment, flags=re.IGNORECASE)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    lines = [clean_text(line) for line in fragment.splitlines()]
    return "\n".join(line for line in lines if line)


def first_sentences(text: str, limit: int = 2) -> str:
    """Return the first few sentences from a block of text."""
    normalized = clean_text(text)
    if not normalized:
        return ""
    parts = [
        part.strip()
        for part in re.split(r"(?<=[。！？!?；;])", normalized)
        if part.strip()
    ]
    if not parts:
        return normalized
    return "".join(parts[:limit]).strip()


def extract_outline_sections(catalog: str, limit: int = 8) -> list[str]:
    """Extract structured outline lines from a public catalog block."""
    sections: list[str] = []
    for line in [clean_text(item) for item in catalog.splitlines() if clean_text(item)]:
        if line in {"报告摘要", "目录"}:
            continue
        if not re.match(r"^([0-9]+(\.[0-9]+)*|[一二三四五六七八九十]+)[\s、.]", line):
            continue
        if line not in sections:
            sections.append(line)
        if len(sections) >= limit:
            break
    return sections


def summarize_outline_sections(outline_sections: list[str], limit: int = 4) -> str:
    """Summarize the first few outline sections for natural-language output."""
    selected = [clean_text(item) for item in outline_sections if clean_text(item)][
        :limit
    ]
    return "；".join(selected)


def chart_catalog_lines(chart_catalog: str) -> list[str]:
    """Split a chart catalog block into clean individual lines."""
    return [clean_text(item) for item in chart_catalog.splitlines() if clean_text(item)]


def select_relevant_lines(query: str, lines: list[str], limit: int = 4) -> list[str]:
    """Pick the most query-relevant public lines while preserving deterministic output."""
    if not lines:
        return []

    query_text = clean_text(query).lower()
    query_tokens = [token.lower() for token in tokenize(query) if clean_text(token)]
    scored: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        line_lower = line.lower()
        score = 0
        if query_text and query_text in line_lower:
            score += 10
        for token in query_tokens:
            if token and token in line_lower:
                score += 3
        scored.append((score, index, line))

    relevant = [item for item in scored if item[0] > 0]
    if relevant:
        relevant.sort(key=lambda item: (-item[0], item[1]))
        return [item[2] for item in relevant[:limit]]
    return lines[:limit]


def contains_any(text: str, patterns: tuple[str, ...]) -> bool:
    """Return whether any pattern appears in normalized text."""
    normalized = clean_text(text).lower()
    return any(pattern.lower() in normalized for pattern in patterns)


def build_interpretation(
    source: str,
    title: str,
    summary: str,
    outline_sections: list[str],
    chart_catalog: str,
    keywords: list[str],
) -> str:
    """Build a conservative interpretation grounded in public detail evidence."""
    intro = first_sentences(summary, limit=2)
    outline_summary = summarize_outline_sections(outline_sections, limit=4)
    parts: list[str] = []

    if intro:
        parts.append(f"从公开简介看，这份报告的核心内容是：{intro}")
    elif title:
        parts.append(f"从标题看，这份报告聚焦于“{title}”相关议题。")

    if outline_summary:
        parts.append(f"从公开目录看，内容重点覆盖：{outline_summary}。")

    if keywords:
        parts.append("公开关键词包括：" + "、".join(keywords[:6]) + "。")

    if chart_catalog:
        parts.append(
            "图表目录也显示，报告包含一定的数据图表支撑，但具体数值仍需回看原页。"
        )

    if not parts:
        parts.append(
            f"当前这份 {source} 报告公开可见的信息有限，因此解读需要保持保守。"
        )

    return " ".join(parts).strip()


def build_report_answer(report: ReportDetail, question: str) -> ReportAnswer:
    """Answer a user question conservatively using only public report evidence."""
    normalized_question = clean_text(question)
    outline_lines = [
        clean_text(item) for item in report.outline_sections if clean_text(item)
    ]
    chart_lines = chart_catalog_lines(report.chart_catalog)
    relevant_outline = select_relevant_lines(
        normalized_question, outline_lines, limit=5
    )
    relevant_charts = select_relevant_lines(normalized_question, chart_lines, limit=4)
    intro = first_sentences(report.summary, limit=2)

    evidence: list[str] = []
    if intro:
        evidence.append(f"报告简介：{intro}")
    if relevant_outline:
        evidence.append("公开目录：" + "；".join(relevant_outline))
    if relevant_charts:
        evidence.append("图表目录：" + "；".join(relevant_charts))
    elif report.chart_catalog:
        evidence.append("图表目录：公开页面显示该报告包含图表目录。")

    if contains_any(
        normalized_question,
        ("发布时间", "什么时候", "哪年", "日期", "何时发布", "发布于"),
    ):
        answer = f"这份报告公开页面标注的发布时间是 {report.published_at or '未标注'}。"
    elif contains_any(
        normalized_question,
        ("作者", "谁写", "来源", "机构", "发布方", "哪家"),
    ):
        answer = f"这份报告公开页面显示的作者或发布机构是 {report.author or '未标注'}，来源为 {report.source}。"
    elif contains_any(
        normalized_question,
        ("链接", "地址", "在线阅读", "原文", "pdf", "报告链接", "怎么看"),
    ):
        online_read = report.online_read_url or "当前未提供在线阅读链接"
        answer = f"报告详情页链接是 {report.detail_url}。在线阅读入口是 {online_read}。"
    elif contains_any(
        normalized_question,
        ("目录", "章节", "结构", "分几部分", "覆盖哪些", "包含哪些部分"),
    ):
        if relevant_outline:
            answer = (
                "从公开目录看，这份报告主要覆盖：" + "；".join(relevant_outline) + "。"
            )
        elif report.catalog:
            answer = (
                "公开页面可以确认这份报告包含目录结构，但当前未提取出稳定的章节摘要。"
            )
        else:
            answer = "当前公开页面没有暴露足够稳定的目录结构，暂时只能确认它存在详情页与摘要信息。"
    elif contains_any(
        normalized_question,
        (
            "图表",
            "数据",
            "案例",
            "指标",
            "多少",
            "几%",
            "规模",
            "增速",
            "渗透率",
            "份额",
            "排名",
            "数值",
        ),
    ):
        if relevant_charts:
            answer = (
                "公开页面能确认这份报告包含与该问题相关的数据图表线索，例如："
                + "；".join(relevant_charts)
                + "。但脚本当前不对页面图片做 OCR，所以还不能直接给出精确数值，仍需回到在线阅读页或 viewer_images 做人工核验。"
            )
        elif report.chart_catalog:
            answer = (
                "公开页面能确认这份报告含有图表目录，说明报告内部存在数据图表支撑。"
                "不过当前可见证据不足以直接回答具体数值问题，仍需回看原始页面。"
            )
        else:
            answer = (
                "当前公开简介和目录不足以支持精确数据回答。"
                "如果你要的是具体数值、比例或排名，需要回到原报告页面逐页核验。"
            )
    elif contains_any(
        normalized_question,
        ("适合谁", "面向谁", "谁应该看", "适合哪些人", "受众", "读者"),
    ):
        focus_terms = [term for term in [report.industry, *report.keywords[:3]] if term]
        focus_text = "、".join(focus_terms) if focus_terms else report.title
        answer = f"从标题、行业和公开目录看，这份报告更适合关注 {focus_text} 的研究、战略、产品、市场或投资相关人员阅读。"
    elif contains_any(
        normalized_question,
        (
            "讲什么",
            "主要讲",
            "说什么",
            "核心观点",
            "总结",
            "摘要",
            "核心内容",
            "怎么看",
        ),
    ):
        answer = report.interpretation
    else:
        answer_parts: list[str] = []
        if intro:
            answer_parts.append(f"基于公开简介，目前能确认的是：{intro}")
        if relevant_outline:
            answer_parts.append(
                "从公开目录看，相关内容主要落在：" + "；".join(relevant_outline) + "。"
            )
        elif outline_lines:
            answer_parts.append(
                "从公开目录看，报告整体覆盖：" + "；".join(outline_lines[:4]) + "。"
            )
        if relevant_charts and contains_any(
            normalized_question, ("数据", "图表", "证据")
        ):
            answer_parts.append(
                "相关图表线索包括：" + "；".join(relevant_charts) + "。"
            )
        if not answer_parts:
            answer_parts.append(
                "当前公开页面能支持的回答有限，暂时只能确认该报告的标题、基础元数据和部分目录结构。"
            )
        answer_parts.append("如需精确页内结论，请回到在线阅读页继续核验。")
        answer = " ".join(answer_parts)

    verification_links = report.viewer_images[:5] if report.viewer_images else []
    if not evidence:
        evidence.append("当前答案主要来自公开详情页的基础元数据。")

    return ReportAnswer(
        source=report.source,
        report_id=report.report_id,
        title=report.title,
        question=normalized_question,
        answer=answer,
        evidence=evidence,
        evidence_boundary=report.evidence_boundary,
        report_link=report.detail_url,
        online_read_url=report.online_read_url,
        verification_links=verification_links,
    )


def dedupe_preserve_order(values: list[str]) -> list[str]:
    """Remove duplicates while preserving original order."""
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        normalized = clean_text(value)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result


INDEX_QUERY_HINTS: dict[str, tuple[str, ...]] = {
    "irindex.ai": (
        "ai",
        "aigc",
        "人工智能",
        "大模型",
        "语言模型",
        "智能工具",
        "活跃指数",
        "粘性指数",
    ),
    "irindex.app": (
        "app",
        "应用",
        "独立设备",
        "使用次数",
        "赛道",
        "app榜单",
    ),
    "irindex.ad": (
        "广告",
        "广告投放",
        "投放",
        "投入指数",
        "adtracker",
        "品牌营销",
    ),
    "irindex.device": (
        "设备",
        "厂商",
        "机型",
        "覆盖率",
        "ios",
        "android",
    ),
    "irindex.video": (
        "视频",
        "电影",
        "电视剧",
        "综艺",
        "动漫",
        "热播",
        "uv",
    ),
}

GENERAL_INDEX_QUERY_HINTS = (
    "指数",
    "榜单",
    "排行",
    "排名",
    "热度",
    "覆盖率",
    "活跃指数",
    "粘性指数",
    "投入指数",
    "独立设备",
    "使用次数",
    "uv",
)

INDEX_CROSS_SIGNAL_NEIGHBORS: dict[str, tuple[str, ...]] = {
    "irindex.ai": ("irindex.ai", "irindex.app"),
    "irindex.app": (
        "irindex.app",
        "irindex.ai",
        "irindex.device",
        "irindex.ad",
        "irindex.video",
    ),
    "irindex.ad": ("irindex.ad", "irindex.app"),
    "irindex.device": ("irindex.device", "irindex.app"),
    "irindex.video": ("irindex.video", "irindex.app"),
}


def classify_index_query(query: str) -> tuple[bool, set[str]]:
    """Return whether the query looks index-oriented and which snapshots it targets."""
    normalized_query = clean_text(query).lower()
    matched_report_ids: set[str] = set()
    for config in IRESEARCH_INDEX_CONFIGS:
        hints = [
            clean_text(config.title).lower(),
            clean_text(config.industry).lower(),
            *(clean_text(keyword).lower() for keyword in config.keywords),
            *(
                clean_text(keyword).lower()
                for keyword in INDEX_QUERY_HINTS.get(config.report_id, ())
            ),
        ]
        if any(hint and hint in normalized_query for hint in hints):
            matched_report_ids.add(config.report_id)
    has_general_index_intent = any(
        clean_text(term).lower() in normalized_query
        for term in GENERAL_INDEX_QUERY_HINTS
    )
    return has_general_index_intent or bool(matched_report_ids), matched_report_ids


def prioritize_index_results(
    query: str,
    index_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Promote index snapshots that are explicitly targeted by the query."""
    has_index_intent, matched_report_ids = classify_index_query(query)
    if not has_index_intent:
        return index_results

    return sorted(
        index_results,
        key=lambda item: (
            1 if str(item.get("report_id") or "") in matched_report_ids else 0,
            int(item.get("score") or 0),
            published_at_sort_key(str(item.get("published_at") or "")),
        ),
        reverse=True,
    )


def select_preferred_index_results(
    query: str,
    index_results: list[dict[str, Any]],
    limit: int,
) -> list[dict[str, Any]]:
    """Reserve a small number of index snapshots when the query is clearly index-oriented."""
    has_index_intent, matched_report_ids = classify_index_query(query)
    if not has_index_intent or not index_results:
        return []

    prioritized = prioritize_index_results(query, index_results)
    if matched_report_ids:
        relevant = [
            item
            for item in prioritized
            if str(item.get("report_id") or "") in matched_report_ids
            and int(item.get("score") or 0) > 0
        ]
    else:
        relevant = [item for item in prioritized if int(item.get("score") or 0) > 0]

    if not relevant:
        return []

    reserved_slots = min(
        2 if matched_report_ids else 1,
        len(relevant),
        max(1, limit // 3),
    )
    return relevant[:reserved_slots]


def allowed_cross_signal_index_ids(query: str) -> set[str]:
    """Return which index snapshots are allowed to join an insight as cross-signals."""
    _, matched_report_ids = classify_index_query(query)
    if not matched_report_ids:
        return set()

    allowed: set[str] = set()
    for report_id in matched_report_ids:
        allowed.update(INDEX_CROSS_SIGNAL_NEIGHBORS.get(report_id, (report_id,)))
    return allowed


def common_topic_keywords(details: list[ReportDetail], limit: int = 6) -> list[str]:
    """Return high-frequency keywords across insight detail items."""
    counts: dict[str, int] = {}
    for detail in details:
        for keyword in detail.keywords:
            cleaned = clean_text(keyword)
            if not cleaned:
                continue
            counts[cleaned] = counts.get(cleaned, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [item[0] for item in ranked[:limit]]


def extend_unique_results(
    selected: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    seen_ids: set[str],
    limit: int,
) -> None:
    """Append unique search results until the requested limit is reached."""
    for candidate in candidates:
        report_id = str(candidate.get("report_id") or "")
        if not report_id or report_id in seen_ids:
            continue
        selected.append(candidate)
        seen_ids.add(report_id)
        if len(selected) >= limit:
            return


def choose_insight_candidates(
    results: list[dict[str, Any]],
    query: str,
    limit: int = 6,
) -> list[dict[str, Any]]:
    """Select a balanced set of search results for insight synthesis."""
    has_index_intent, matched_index_ids = classify_index_query(query)
    per_source_cap = {
        IRESEARCH_SOURCE: 3,
        IRESEARCH_INDEX_SOURCE: 2
        if matched_index_ids
        else (3 if has_index_intent else 2),
        QUESTMOBILE_SOURCE: 1,
    }
    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    counts: dict[str, int] = {}

    for result in results:
        source = str(result.get("source") or "")
        report_id = str(result.get("report_id") or "")
        if not report_id or report_id in selected_ids:
            continue
        if counts.get(source, 0) >= per_source_cap.get(source, 1):
            continue
        selected.append(result)
        selected_ids.add(report_id)
        counts[source] = counts.get(source, 0) + 1
        if len(selected) >= limit:
            return selected
    return selected


def build_ranked_results(
    query: str,
    reports: list[ReportSummary],
    normalized_industry: str,
    since_filter: tuple[int, int, int, int, int, int] | None,
    sort_by: str,
    sort_order: str,
) -> list[dict[str, Any]]:
    """Filter and sort report summaries into ranked payloads."""
    return sort_scored_results(
        build_scored_results(
            query,
            reports,
            normalized_industry,
            since_filter,
        ),
        query,
        sort_by,
        sort_order,
    )


def collect_insight_candidate_results(
    query: str,
    pages: int,
    page_size: int,
    industry: str | None,
    include_questmobile: bool,
    sort_by: str,
    sort_order: str,
    since: str | None,
    limit: int = 8,
) -> list[dict[str, Any]]:
    """Build a mixed insight candidate set with both reports and snapshot pages."""
    normalized_industry = clean_text(industry or "").lower()
    since_filter = parse_cli_datetime(since) if since else None

    iresearch_results = build_ranked_results(
        query,
        list_iresearch_reports(pages=pages, page_size=page_size),
        normalized_industry,
        since_filter,
        sort_by,
        sort_order,
    )
    index_results = prioritize_index_results(
        query,
        build_ranked_results(
            query,
            list_iresearch_index_snapshots(),
            normalized_industry,
            since_filter,
            sort_by,
            sort_order,
        ),
    )
    allowed_index_ids = allowed_cross_signal_index_ids(query)
    if allowed_index_ids:
        index_results = [
            item
            for item in index_results
            if str(item.get("report_id") or "") in allowed_index_ids
        ]
    questmobile_results: list[dict[str, Any]] = []
    if include_questmobile:
        questmobile_results = build_ranked_results(
            query,
            list_questmobile_reports(pages=pages, page_size=page_size),
            normalized_industry,
            since_filter,
            sort_by,
            sort_order,
        )

    has_index_intent, matched_index_ids = classify_index_query(query)
    selected: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    extend_unique_results(
        selected,
        iresearch_results[: (3 if has_index_intent else 4)],
        seen_ids,
        limit,
    )
    extend_unique_results(
        selected,
        index_results[:2],
        seen_ids,
        limit,
    )

    if len(selected) < limit:
        extend_unique_results(
            selected,
            iresearch_results[(3 if has_index_intent else 4) :],
            seen_ids,
            limit,
        )
    if len(selected) < limit:
        extend_unique_results(
            selected,
            index_results[2:],
            seen_ids,
            limit,
        )
    if include_questmobile and len(selected) < limit:
        extend_unique_results(selected, questmobile_results[1:], seen_ids, limit)
    return selected


def fetch_insight_details(
    results: list[dict[str, Any]],
    query: str,
    pages: int,
    page_size: int,
) -> list[ReportDetail]:
    """Fetch detail payloads for a small set of insight candidates."""
    details: list[ReportDetail] = []
    for result in choose_insight_candidates(results, query=query):
        try:
            if str(result.get("source") or "") == IRESEARCH_SOURCE:
                details.append(
                    fetch_iresearch_detail_from_summary(
                        report_summary_from_payload(result),
                        include_images=False,
                    )
                )
            else:
                details.append(
                    fetch_report_detail(
                        identifier=str(result["report_id"]),
                        pages=pages,
                        page_size=page_size,
                        last_id=IRESEARCH_DEFAULT_LAST_ID,
                        include_images=False,
                    )
                )
        except Exception:
            continue
    return details


def build_insight_summary(query: str, details: list[ReportDetail]) -> str:
    """Build a top-level executive summary from insight details."""
    keywords = common_topic_keywords(details, limit=5)
    latest_date = max((detail.published_at or "" for detail in details), default="")
    has_reports = any(detail.source == IRESEARCH_SOURCE for detail in details)
    has_indexes = any(detail.source == IRESEARCH_INDEX_SOURCE for detail in details)

    parts = [f"围绕“{query}”的公开资料显示，这一议题仍具持续跟踪价值。"]
    if has_reports:
        parts.append("艾瑞正式报告提供了行业背景、结构拆解和主题解释。")
    if has_indexes:
        parts.append("艾瑞指数快照补充了短周期榜单和指标观察。")
    if latest_date:
        parts.append(f"当前纳入分析的公开资料中，最新可见更新时间为 {latest_date}。")
    if keywords:
        parts.append("高频主题主要集中在：" + "、".join(keywords) + "。")
    return " ".join(parts)


def build_market_judgement(query: str, details: list[ReportDetail]) -> str:
    """Build a conservative market judgement statement."""
    has_reports = any(detail.source == IRESEARCH_SOURCE for detail in details)
    has_indexes = any(detail.source == IRESEARCH_INDEX_SOURCE for detail in details)
    recent_items = [
        detail for detail in details if clean_text(detail.published_at or "")
    ]
    parts = [f"对“{query}”的当前判断应建立在正式报告与公开数据快照的交叉验证上。"]
    if has_reports and has_indexes:
        parts.append(
            "现有证据既覆盖解释性研究，也覆盖公开榜单和指标切片，因此可以对市场热度和结构变化做初步判断。"
        )
    elif has_reports:
        parts.append(
            "目前判断主要依赖正式报告的解释性材料，更适合做方向性结论而非高频波动判断。"
        )
    elif has_indexes:
        parts.append(
            "目前判断主要依赖指数快照，更适合观察热度和排名变化，不宜替代完整行业研究。"
        )
    if len(recent_items) >= 2:
        parts.append("从公开更新频率看，该议题并非一次性热点，而是仍在持续被跟踪。")
    return " ".join(parts)


def build_market_signals(details: list[ReportDetail], limit: int = 4) -> list[str]:
    """Build market signal bullets from detail evidence."""
    signals: list[str] = []
    for detail in details:
        intro = first_sentences(detail.summary, limit=1)
        label = (
            f"{detail.title}（{detail.source}，{detail.published_at or '时间未标注'}）"
        )
        if intro:
            signals.append(f"{label}：{intro}")
        elif detail.outline_sections:
            signals.append(
                f"{label}：重点涉及 {'；'.join(detail.outline_sections[:3])}。"
            )
        if len(signals) >= limit:
            break
    return dedupe_preserve_order(signals)


def build_industry_structure(details: list[ReportDetail]) -> list[str]:
    """Build industry structure observations from sources, industries, and outlines."""
    structures: list[str] = []
    industries = dedupe_preserve_order(
        [detail.industry or "" for detail in details if detail.industry]
    )
    keywords = common_topic_keywords(details, limit=5)
    top_outline_lines = dedupe_preserve_order(
        [line for detail in details for line in detail.outline_sections[:2]]
    )
    if industries:
        structures.append(
            "当前样本覆盖的行业视角包括：" + "、".join(industries[:5]) + "。"
        )
    if keywords:
        structures.append(
            "从关键词聚合看，当前议题主要围绕：" + "、".join(keywords) + "。"
        )
    if top_outline_lines:
        structures.append(
            "公开目录与榜单显示，研究拆解重点包括："
            + "；".join(top_outline_lines[:4])
            + "。"
        )
    return structures


def build_competitive_landscape(details: list[ReportDetail]) -> list[str]:
    """Build competitive-landscape observations from report and index evidence."""
    observations: list[str] = []
    index_details = [
        detail for detail in details if detail.source == IRESEARCH_INDEX_SOURCE
    ]
    report_details = [detail for detail in details if detail.source == IRESEARCH_SOURCE]

    top_snapshot_items = dedupe_preserve_order(
        [item for detail in index_details for item in detail.outline_sections[:3]]
    )
    if top_snapshot_items:
        observations.append(
            "指数快照层面可见的头部竞争信号包括："
            + "；".join(top_snapshot_items[:4])
            + "。"
        )

    report_titles = dedupe_preserve_order([detail.title for detail in report_details])
    if report_titles:
        observations.append(
            "正式报告当前重点关注的竞争主题包括：" + "；".join(report_titles[:3]) + "。"
        )

    if not observations:
        observations.append(
            "当前公开样本更适合识别赛道热点与关注方向，尚不足以直接还原完整竞争格局。"
        )
    return observations


def resolve_primary_index_focus(query: str, details: list[ReportDetail]) -> str | None:
    """Resolve the main index focus for a query-aware insight."""
    _, matched_report_ids = classify_index_query(query)
    if matched_report_ids:
        for detail in details:
            if (
                detail.source == IRESEARCH_INDEX_SOURCE
                and detail.report_id in matched_report_ids
            ):
                return detail.report_id
        return next(iter(sorted(matched_report_ids)), None)

    for detail in details:
        if detail.source == IRESEARCH_INDEX_SOURCE:
            return detail.report_id
    return None


def resolve_signal_sources(
    query: str,
    details: list[ReportDetail],
) -> tuple[str | None, str | None]:
    """Return primary and secondary index signal source ids for the insight."""
    primary_signal = resolve_primary_index_focus(query, details)
    if not primary_signal:
        return None, None

    secondary_signal = None
    allowed_neighbors = set(INDEX_CROSS_SIGNAL_NEIGHBORS.get(primary_signal, ()))
    for detail in details:
        if detail.source != IRESEARCH_INDEX_SOURCE:
            continue
        if detail.report_id == primary_signal:
            continue
        if allowed_neighbors and detail.report_id not in allowed_neighbors:
            continue
        secondary_signal = detail.report_id
        break
    return primary_signal, secondary_signal


def build_growth_drivers(query: str, details: list[ReportDetail]) -> list[str]:
    """Build growth-driver observations grounded in public summaries and keywords."""
    primary_focus = resolve_primary_index_focus(query, details)
    if primary_focus == "irindex.device":
        return [
            "终端驱动上，品牌覆盖率与装机基础决定了设备厂商在分发入口和生态触达中的长期优势。",
            "换机与品牌迁移驱动上，头部厂商之间的份额变化会先反映在覆盖率榜单，再传导到应用分发与服务生态。",
        ]
    if primary_focus == "irindex.video":
        return [
            "内容供给驱动上，爆款内容的持续生产能力仍是拉动视频热度榜单变化的核心变量。",
            "分发驱动上，平台首页推荐、短视频切条传播和热点话题联动会直接影响内容 UV 的短期跃升。",
        ]
    if primary_focus == "irindex.ad":
        return [
            "预算驱动上，品牌投放强度和媒介排期变化仍是广告指数波动最直接的来源。",
            "渠道效率驱动上，广告主会持续把预算向更高转化效率和更强触达能力的媒介组合迁移。",
        ]
    if primary_focus == "irindex.app":
        return [
            "流量驱动上，头部应用的独立设备规模和使用次数仍是判断赛道扩张速度的直接信号。",
            "使用时长驱动上，用户注意力向高频高停留时长场景集中，会持续改变赛道排序和应用位次。",
        ]
    if primary_focus == "irindex.ai":
        return [
            "技术驱动上，生成式 AI 与模型能力提升仍是活跃指数和粘性指数变化的主要牵引因素。",
            "场景驱动上，AI 应用能否嵌入真实工作流和高频需求，会直接决定留存与头部集中度。",
        ]

    drivers: list[str] = []
    keyword_blob = " ".join(common_topic_keywords(details, limit=10))
    summaries = " ".join(detail.summary for detail in details)

    if any(
        token in keyword_blob or token in summaries for token in ("AI", "AIGC", "智能")
    ):
        drivers.append(
            "技术驱动上，生成式 AI 与智能化能力持续进入真实业务场景，是当前最明显的增长牵引因素之一。"
        )
    if any(
        token in keyword_blob or token in summaries
        for token in ("流量", "用户", "活跃", "渗透率")
    ):
        drivers.append(
            "需求驱动上，用户活跃度、流量迁移和渗透率变化仍是判断赛道扩张速度的重要先行信号。"
        )
    if any(
        token in keyword_blob or token in summaries
        for token in ("广告", "营销", "投放", "品牌")
    ):
        drivers.append(
            "商业化驱动上，品牌投放效率与营销转化质量的改善，正在成为推动预算继续向新渠道迁移的核心变量。"
        )
    if any(
        token in keyword_blob or token in summaries
        for token in ("数据", "交易", "平台", "生态")
    ):
        drivers.append(
            "基础设施驱动上，数据流通、平台化能力和生态协同成熟度，会直接影响行业从概念试点走向规模复制的速度。"
        )

    return dedupe_preserve_order(drivers)[:4]


def build_risk_watchpoints(details: list[ReportDetail]) -> list[str]:
    """Build key risk and watchpoint observations for the insight payload."""
    watchpoints: list[str] = []
    has_indexes = any(detail.source == IRESEARCH_INDEX_SOURCE for detail in details)
    has_reports = any(detail.source == IRESEARCH_SOURCE for detail in details)

    if has_indexes:
        watchpoints.append(
            "指数页反映的是公开可见快照，适合做热度和排名观察，但不等同于完整数据库口径。"
        )
    if has_reports:
        watchpoints.append(
            "正式报告多提供方向性和结构性解释，但并不总是覆盖最新周度或月度变化，因此需要与高频数据交叉验证。"
        )
    watchpoints.append(
        "若后续新增公开样本主要集中在单一机构或单一赛道，结论可能会对该视角产生偏置，需要持续补充交叉来源。"
    )
    return dedupe_preserve_order(watchpoints)[:3]


def build_future_trends(query: str, details: list[ReportDetail]) -> list[str]:
    """Build conservative future trend hypotheses from the evidence set."""
    primary_focus = resolve_primary_index_focus(query, details)
    if primary_focus == "irindex.device":
        return [
            "未来趋势上，更值得跟踪的是头部厂商品牌覆盖率是否继续集中，还是在新一轮换机周期中重新分化。",
            "设备市场后续的关键观察点是品牌份额变化是否同步带动生态应用和服务入口的再分配。",
            f"对“{query}”的未来判断应持续观察：覆盖率榜单是否出现头部更替，以及品牌集中度是否进一步抬升。",
        ]
    if primary_focus == "irindex.video":
        return [
            "未来趋势上，更值得跟踪的是内容热度是否继续由少数头部爆款集中，还是回到更多元的分散竞争。",
            "视频内容市场后续的关键变量是平台分发机制变化是否会缩短爆款生命周期并加快榜单轮换。",
            f"对“{query}”的未来判断应持续观察：电影、剧集、综艺和动漫四类榜单是否同步出现头部更替。",
        ]
    if primary_focus == "irindex.ad":
        return [
            "未来趋势上，更值得跟踪的是广告预算是否继续向头部广告主和高效率媒介进一步集中。",
            "广告投放市场后续的关键变量是全端、PC端和移动端的投入结构是否继续分化。",
            f"对“{query}”的未来判断应持续观察：头部广告主榜单是否换位，以及端别投入结构是否发生迁移。",
        ]
    if primary_focus == "irindex.app":
        return [
            "未来趋势上，更值得跟踪的是头部应用独立设备规模是否继续稳定，还是被新流量入口打破。",
            "APP 市场后续的关键变量是赛道级使用次数和有效使用时间占比是否持续向少数高频场景集中。",
            f"对“{query}”的未来判断应持续观察：APP 榜单头部是否更替，以及赛道排序是否出现明显迁移。",
        ]
    if primary_focus == "irindex.ai":
        return [
            "未来趋势上，更值得关注的是 AI 应用头部榜单是否继续向少数平台集中，还是出现新的场景化突破者。",
            "AI 应用市场后续的关键变量是活跃指数增长能否继续转化为粘性提升，而不只是短期热度波动。",
            f"对“{query}”的未来判断应持续观察：活跃指数与粘性指数是否同步改善，以及头部应用是否出现更替。",
        ]

    trends: list[str] = []
    keywords = common_topic_keywords(details, limit=8)
    keyword_blob = " ".join(keywords)
    if any(token in keyword_blob for token in ("AI", "人工智能", "AIGC", "智能")):
        trends.append(
            "未来趋势上，更值得关注的是 AI/智能能力是否继续从单点功能走向更完整的场景化落地。"
        )
    if any(token in keyword_blob for token in ("广告", "营销", "投放", "品牌")):
        trends.append(
            "在营销与广告场景中，后续更关键的不是单纯投入规模，而是投放效率、转化质量和渠道结构变化。"
        )
    if any(
        token in keyword_blob for token in ("APP", "设备", "视频", "活跃指数", "覆盖率")
    ):
        trends.append(
            "如果指数快照持续更新，后续可以重点跟踪头部榜单、活跃度和覆盖率的变化，以判断市场是否继续集中或发生分化。"
        )
    trends.append(
        f"对“{query}”的未来判断应持续观察：正式报告是否继续更新、指数榜单是否出现头部更替、以及公开研究是否从现象描述转向效率和结构分析。"
    )
    return dedupe_preserve_order(trends)[:4]


def build_insight_evidence(details: list[ReportDetail], limit: int = 6) -> list[str]:
    """Build concise evidence bullets for an insight payload."""
    evidence: list[str] = []
    for detail in details:
        intro = first_sentences(detail.summary, limit=1)
        if intro:
            evidence.append(f"{detail.title}：{intro}")
        elif detail.outline_sections:
            evidence.append(f"{detail.title}：{'；'.join(detail.outline_sections[:3])}")
        if len(evidence) >= limit:
            break
    return dedupe_preserve_order(evidence)


def build_insight_analysis(
    query: str,
    pages: int,
    page_size: int,
    industry: str | None,
    include_questmobile: bool,
    sort_by: str,
    sort_order: str,
    since: str | None,
) -> InsightAnalysis:
    """Build a market and industry insight analysis from search results and details."""
    search_results = collect_insight_candidate_results(
        query=query,
        pages=pages,
        page_size=page_size,
        industry=industry,
        include_questmobile=include_questmobile,
        sort_by=sort_by,
        sort_order=sort_order,
        since=since,
        limit=max(8, SEARCH_DEFAULT_LIMIT),
    )
    if not search_results:
        raise ValueError(
            "Could not build insight because no usable report or index source was found"
        )

    details = fetch_insight_details(
        search_results,
        query=query,
        pages=pages,
        page_size=page_size,
    )
    if not details:
        raise ValueError(
            "Could not build insight because no detail evidence could be fetched"
        )

    source_breakdown: dict[str, int] = {}
    for detail in details:
        source_breakdown[detail.source] = source_breakdown.get(detail.source, 0) + 1

    evidence_boundaries = dedupe_preserve_order(
        [detail.evidence_boundary for detail in details if detail.evidence_boundary]
    )
    analyzed_items = [
        {
            "source": detail.source,
            "report_id": detail.report_id,
            "title": detail.title,
            "published_at": detail.published_at or "",
            "report_link": detail.detail_url,
        }
        for detail in details
    ]
    primary_signal_source, secondary_signal_source = resolve_signal_sources(
        query,
        details,
    )

    return InsightAnalysis(
        query=query,
        primary_signal_source=primary_signal_source,
        secondary_signal_source=secondary_signal_source,
        executive_summary=build_insight_summary(query, details),
        market_judgement=build_market_judgement(query, details),
        market_signals=build_market_signals(details),
        industry_structure=build_industry_structure(details),
        competitive_landscape=build_competitive_landscape(details),
        growth_drivers=build_growth_drivers(query, details),
        risk_watchpoints=build_risk_watchpoints(details),
        future_trends=build_future_trends(query, details),
        evidence=build_insight_evidence(details),
        evidence_boundary=" ".join(evidence_boundaries),
        source_breakdown=source_breakdown,
        analyzed_items=analyzed_items,
    )


def build_evidence_boundary(source: str, has_viewer_images: bool) -> str:
    """Explain what the current interpretation is grounded on."""
    if source == IRESEARCH_SOURCE:
        if has_viewer_images:
            return (
                "当前解读主要基于公开的报告简介、meta description、目录、图表目录，以及在线浏览页暴露的页面图片链接。"
                "脚本当前不会对页面图片做 OCR，因此涉及具体页内数据或精确表述时，仍应回到 viewer_images 对应页面进行人工核验。"
            )
        return (
            "当前解读主要基于公开的报告简介、meta description、目录和图表目录。"
            "在没有进一步检查页面图片的情况下，结论应限制在这些公开可见部分能够支持的范围内。"
        )
    return (
        "当前解读主要基于公开的导语、元数据区块、标题结构以及页面中暴露的图片。"
        "它应被视为基于公开页面的解读，而不是对完整报告正文的逐页通读。"
    )


def decode_html(data: bytes) -> str:
    """Decode HTML pages for both supported sources."""
    for encoding in ("utf-8", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="ignore")


def fetch_bytes(
    url: str,
    headers: dict[str, str],
    method: str = "GET",
    data: bytes | None = None,
) -> bytes:
    """Fetch a URL and return raw bytes."""
    request = Request(url, headers=headers, data=data, method=method.upper())
    with urlopen(request, timeout=20) as response:
        return response.read()


def fetch_json(
    url: str,
    method: str = "GET",
    data: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
) -> Any:
    """Fetch JSON from a public API endpoint."""
    request_headers = dict(JSON_HEADERS)
    if headers:
        request_headers.update(headers)
    payload = json.dumps(data).encode("utf-8") if data is not None else None
    if payload is not None:
        request_headers.setdefault("Content-Type", "application/json;charset=UTF-8")
    return json.loads(
        fetch_bytes(
            url,
            request_headers,
            method=method,
            data=payload,
        ).decode("utf-8")
    )


def fetch_html(url: str) -> str:
    """Fetch and decode an HTML page."""
    return decode_html(fetch_bytes(url, HTML_HEADERS))


def build_iresearch_list_url(
    last_id: str,
    page_size: int,
    fee: int = 0,
    date: str = "",
) -> str:
    """Build the iResearch list API URL."""
    query = urlencode(
        {
            "fee": fee,
            "date": date,
            "lastId": last_id,
            "pageSize": page_size,
        }
    )
    return f"{IRESEARCH_API_URL}?{query}"


def build_iresearch_viewer_url(news_id: int) -> str:
    """Return the iResearch online reader URL for a report."""
    return f"https://report.iresearch.cn/report_pdf.aspx?id={news_id}"


def build_questmobile_detail_url(news_id: int) -> str:
    """Return the QuestMobile detail URL for a report."""
    return f"https://www.questmobile.com.cn/research/report/{news_id}"


def normalize_report_link(url: str | None) -> str:
    """Normalize and validate a public report link."""
    value = clean_text(url or "")
    if not value:
        return ""
    if value.startswith("//"):
        return f"https:{value}"
    if value.startswith("http://") or value.startswith("https://"):
        return value
    return ""


def require_report_link(url: str | None) -> str:
    """Require a valid public report link and raise when it is missing."""
    normalized = normalize_report_link(url)
    if not normalized:
        raise ValueError("Report link is required and cannot be empty")
    return normalized


def build_questmobile_list_url(
    page_no: int,
    page_size: int,
    industry_id: int = -1,
    label_id: int = -1,
    version: int = 0,
) -> str:
    """Return the QuestMobile paginated article-list endpoint URL."""
    query = urlencode(
        {
            "version": version,
            "pageSize": page_size,
            "pageNo": page_no,
            "industryId": industry_id,
            "labelId": label_id,
        }
    )
    return f"{QUESTMOBILE_ARTICLE_LIST_URL}?{query}"


def tokenize(query: str) -> list[str]:
    """Split a search query into ranking tokens."""
    base_tokens = [
        clean_text(value) for value in re.split(r"[\s,，、/]+", query) if value.strip()
    ]
    if not base_tokens:
        return [clean_text(query)]

    tokens: list[str] = []
    for token in base_tokens:
        if token and token not in tokens:
            tokens.append(token)
        for segment in re.findall(r"[A-Za-z0-9]+|[\u4e00-\u9fff]+", token):
            normalized_segment = clean_text(segment)
            if normalized_segment and normalized_segment not in tokens:
                tokens.append(normalized_segment)
    return tokens


def extract_years(text: str) -> list[int]:
    """Extract distinct 4-digit years from text in appearance order."""
    years: list[int] = []
    for match in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", clean_text(text)):
        year = int(match)
        if year not in years:
            years.append(year)
    return years


def non_year_query_tokens(query: str) -> list[str]:
    """Return non-year ranking tokens from a query."""
    query_year_tokens = {str(year) for year in extract_years(query)}
    return [
        token for token in tokenize(query) if token.lower() not in query_year_tokens
    ]


def has_strong_title_topic_match(results: list[dict[str, Any]], query: str) -> bool:
    """Return whether at least one result title strongly matches the non-year topic tokens."""
    topic_tokens = [clean_text(token).lower() for token in non_year_query_tokens(query)]
    if not topic_tokens:
        return True
    for item in results:
        title = clean_text(str(item.get("title") or "")).lower()
        if title and all(token in title for token in topic_tokens):
            return True
    return False


def find_index_snapshot_config(identifier: str) -> IndexSnapshotConfig | None:
    """Find an index snapshot config by synthetic id or URL."""
    normalized_identifier = clean_text(identifier)
    for config in IRESEARCH_INDEX_CONFIGS:
        if normalized_identifier == config.report_id:
            return config
        if normalized_identifier == config.detail_url:
            return config
    return None


def format_snapshot_date(raw_value: str, label: str = "") -> str:
    """Format a compact snapshot date from API values or page labels."""
    cleaned_label = clean_text(label)
    if cleaned_label:
        return cleaned_label

    cleaned_value = clean_text(raw_value)
    if re.fullmatch(r"\d{8}", cleaned_value):
        return f"{cleaned_value[:4]}-{cleaned_value[4:6]}-{cleaned_value[6:8]}"
    if re.fullmatch(r"\d{6}", cleaned_value):
        return f"{cleaned_value[:4]}-{cleaned_value[4:6]}"
    return cleaned_value


def format_metric_number(value: Any) -> str:
    """Format a numeric index value for readable output."""
    if value in (None, ""):
        return "-"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return clean_text(str(value)) or "-"
    if number.is_integer():
        return f"{int(number):,}"
    return f"{number:,.2f}"


def format_growth_rate(value: Any) -> str:
    """Format the growth-rate field used by index APIs."""
    if value in (None, ""):
        return "-"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return clean_text(str(value)) or "-"
    percentage = number * 100 if abs(number) <= 1 else number
    return f"{percentage:+.2f}%"


def format_rank_change(value: Any) -> str:
    """Format a rank-change indicator for readable output."""
    if value in (None, ""):
        return "-"
    try:
        number = int(float(value))
    except (TypeError, ValueError):
        return clean_text(str(value)) or "-"
    if number == 0:
        return "0"
    return f"{number:+d}"


def format_signed_percent(value: Any) -> str:
    """Format a percentage value that is already expressed in percent units."""
    if value in (None, ""):
        return "-"
    try:
        number = float(value)
    except (TypeError, ValueError):
        return clean_text(str(value)) or "-"
    return f"{number:+.2f}%"


def build_ai_index_metric_line(row: dict[str, Any], metric_label: str) -> str:
    """Build one readable leaderboard line from the AI index API."""
    app_name = clean_text(str(row.get("appName") or ""))
    category_name = clean_text(
        str(
            row.get("kclassName")
            or row.get("className")
            or row.get("trackName")
            or row.get("track")
            or ""
        )
    )
    display_name = app_name
    if category_name and category_name != "全部":
        display_name = f"{app_name}（{category_name}）"

    metrics = [f"{metric_label}{format_metric_number(row.get('indexValue'))}"]
    growth_rate = format_growth_rate(row.get("growthRate"))
    if growth_rate != "-":
        metrics.append(f"环比{growth_rate}")
    rank_change = format_rank_change(row.get("rankChange"))
    if rank_change != "-":
        metrics.append(f"排名变动{rank_change}")
    return f"{display_name} | " + " | ".join(metrics)


def build_request_token() -> str:
    """Build a lightweight request token for iResearch index endpoints."""
    return str(int(datetime.now().timestamp() * 1000))


def build_ad_index_metric_line(device_label: str, row: dict[str, Any]) -> str:
    """Build one readable leaderboard line from the ad index API."""
    advertiser_name = clean_text(str(row.get("AdverName") or ""))
    if not advertiser_name:
        return ""
    metric_value = format_metric_number(row.get("HistoryIBill"))
    return f"{device_label} | {advertiser_name} | 投入指数{metric_value}"


def build_app_index_metric_line(row: dict[str, Any]) -> str:
    """Build one readable leaderboard line from the app index API."""
    app_name = clean_text(str(row.get("AppName") or ""))
    primary_class = clean_text(str(row.get("FclassName") or ""))
    secondary_class = clean_text(str(row.get("KclassName") or ""))
    if not app_name:
        return ""
    display_name = app_name
    if primary_class and secondary_class:
        display_name = f"{app_name}（{primary_class}-{secondary_class}）"
    elif primary_class:
        display_name = f"{app_name}（{primary_class}）"

    metrics = [f"独立设备(万台){format_metric_number(row.get('UseNum'))}"]
    growth_rate = format_signed_percent(row.get("Growth"))
    if growth_rate != "-":
        metrics.append(f"环比{growth_rate}")
    return f"{display_name} | " + " | ".join(metrics)


def build_device_index_metric_line(row: dict[str, Any]) -> str:
    """Build one readable leaderboard line from the device index API."""
    brand_name = clean_text(str(row.get("BrandName") or ""))
    if not brand_name:
        return ""
    coverage = format_growth_rate(row.get("Percent"))
    if coverage == "-":
        coverage = "-"
    return f"{brand_name} | 覆盖率{coverage}"


def build_video_index_metric_line(class_label: str, row: dict[str, Any]) -> str:
    """Build one readable leaderboard line from the video index API."""
    media_name = clean_text(str(row.get("mName") or ""))
    if not media_name:
        return ""
    metrics = [f"UV {format_metric_number(row.get('UV'))}"]
    class_rank = row.get("ClassRank")
    if class_rank not in (None, ""):
        try:
            metrics.append(f"类目排名{int(float(str(class_rank)))}")
        except (TypeError, ValueError):
            pass
    return f"{class_label} | {media_name} | " + " | ".join(metrics)


def fetch_ai_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured leaderboard data from the public AI index API."""
    api_headers = {
        "Referer": config.detail_url,
        "Origin": "https://ircloud.iresearchdata.cn",
    }
    categories = fetch_json(
        f"{AI_INDEX_API_BASE_URL}/ai_index/_category",
        headers=api_headers,
    )
    date_ranges = fetch_json(
        f"{AI_INDEX_API_BASE_URL}/ai_index/_dateRange",
        headers=api_headers,
    )
    if isinstance(categories, dict):
        categories = categories.get("data") or []
    if isinstance(date_ranges, dict):
        date_ranges = date_ranges.get("data") or []
    if not isinstance(date_ranges, list) or not date_ranges:
        raise ValueError("AI index date range API returned no usable snapshot date")

    current_date_item = next(
        (
            item
            for item in date_ranges
            if isinstance(item, dict) and clean_text(str(item.get("value") or ""))
        ),
        None,
    )
    if current_date_item is None:
        raise ValueError("AI index date range API did not expose a usable value")

    time_name = clean_text(str(current_date_item.get("value") or ""))
    snapshot_date = format_snapshot_date(
        time_name,
        label=str(current_date_item.get("label") or ""),
    )

    visible_categories = []
    if isinstance(categories, list):
        visible_categories = [
            clean_text(str(item.get("label") or ""))
            for item in categories
            if isinstance(item, dict)
            and clean_text(str(item.get("label") or ""))
            and clean_text(str(item.get("label") or "")) != "全部"
        ]

    outline_sections: list[str] = []
    metric_labels = {
        "activity": "活跃指数",
        "stickiness": "粘性指数",
    }
    for index_type, metric_label in metric_labels.items():
        payload = {
            "page": 1,
            "orderType": "desc",
            "orderColumn": "",
            "pageSize": 5,
            "timeName": time_name,
            "kclassId": None,
            "indexType": index_type,
        }
        rank_data = fetch_json(
            f"{AI_INDEX_API_BASE_URL}/ai_index/_rank",
            method="POST",
            data=payload,
            headers=api_headers,
        )
        if not isinstance(rank_data, dict):
            continue
        rank_payload = rank_data.get("data") or {}
        if not isinstance(rank_payload, dict):
            continue
        rows = rank_payload.get("tableData") or []
        if not isinstance(rows, list):
            continue
        for row in rows[:5]:
            if not isinstance(row, dict):
                continue
            line = build_ai_index_metric_line(row, metric_label)
            if clean_text(line):
                outline_sections.append(line)

    outline_sections = dedupe_preserve_order(outline_sections)
    summary_parts = [config.summary_hint]
    if snapshot_date:
        summary_parts.append(f"当前可见快照时间：{snapshot_date}。")
    if visible_categories:
        summary_parts.append(
            "当前公开赛道筛选包括：" + "、".join(visible_categories[:6]) + "。"
        )
    if outline_sections:
        summary_parts.append(
            "通过页面公开请求 API 可见的头部应用及指标包括："
            + "；".join(outline_sections[:5])
            + "。"
        )

    keywords = dedupe_preserve_order(config.keywords + visible_categories[:4])
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=" ".join(summary_parts),
        outline_sections=outline_sections,
        chart_catalog="\n".join(outline_sections),
        keywords=keywords,
    )


def fetch_ad_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured leaderboard data from the public ad index APIs."""
    request_token = build_request_token()
    api_headers = {
        "Referer": "https://index.iresearch.com.cn/new/",
        "Token": request_token,
    }
    categories = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/home/AdIndustryClass?t={request_token}",
        headers=api_headers,
    )
    date_ranges = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/home/AdTimes?t={request_token}",
        headers=api_headers,
    )
    if not isinstance(categories, list) or not categories:
        raise ValueError("Ad index category API returned no usable categories")
    if not isinstance(date_ranges, list) or not date_ranges:
        raise ValueError("Ad index date API returned no usable snapshot date")

    current_date_item = next(
        (
            item
            for item in date_ranges
            if isinstance(item, dict) and clean_text(str(item.get("Id") or ""))
        ),
        None,
    )
    if current_date_item is None:
        raise ValueError("Ad index date API did not expose a usable value")

    time_name = clean_text(str(current_date_item.get("Id") or ""))
    snapshot_date = format_snapshot_date(
        time_name,
        label=str(current_date_item.get("Name") or ""),
    )
    visible_categories = [
        clean_text(str(item.get("Name") or ""))
        for item in categories
        if isinstance(item, dict) and clean_text(str(item.get("Name") or ""))
    ]

    outline_sections: list[str] = []
    endpoint_types = {
        "all": "全端",
        "pc": "PC端",
        "mobile": "移动端",
    }
    for endpoint_type, device_label in endpoint_types.items():
        rank_data = fetch_json(
            (
                f"{AD_INDEX_API_BASE_URL}/ad/GetAdData?type={endpoint_type}"
                f"&classId=0&time={time_name}"
            ),
            headers=api_headers,
        )
        if not isinstance(rank_data, dict):
            continue
        rows = rank_data.get("List") or []
        if not isinstance(rows, list):
            continue
        for row in rows[:5]:
            if not isinstance(row, dict):
                continue
            line = build_ad_index_metric_line(device_label, row)
            if clean_text(line):
                outline_sections.append(line)

    outline_sections = dedupe_preserve_order(outline_sections)
    summary_parts = [config.summary_hint]
    if snapshot_date:
        summary_parts.append(f"当前可见快照时间：{snapshot_date}。")
    if visible_categories:
        summary_parts.append(
            "当前公开行业筛选包括：" + "、".join(visible_categories[:8]) + "。"
        )
    if outline_sections:
        summary_parts.append(
            "通过页面公开请求 API 可见的头部广告主与品牌投入指数包括："
            + "；".join(outline_sections[:6])
            + "。"
        )

    keywords = dedupe_preserve_order(
        config.keywords + visible_categories[:4] + ["PC端", "移动端", "全端"]
    )
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=" ".join(summary_parts),
        outline_sections=outline_sections,
        chart_catalog="\n".join(outline_sections),
        keywords=keywords,
    )


def fetch_app_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured leaderboard data from the public app index APIs."""
    request_token = build_request_token()
    api_headers = {
        "Referer": "https://index.iresearch.com.cn/new/",
        "Token": request_token,
    }
    date_ranges = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/home/appMonthSpans?t={request_token}",
        headers=api_headers,
    )
    if not isinstance(date_ranges, list) or not date_ranges:
        raise ValueError("App index date API returned no usable snapshot date")

    current_date_item = next(
        (
            item
            for item in date_ranges
            if isinstance(item, dict) and clean_text(str(item.get("ID") or ""))
        ),
        None,
    )
    if current_date_item is None:
        raise ValueError("App index date API did not expose a usable value")

    time_name = clean_text(str(current_date_item.get("ID") or ""))
    snapshot_date = format_snapshot_date(
        time_name,
        label=str(current_date_item.get("TimeName") or ""),
    )

    overview_labels = {
        1: "APP热门赛道环比增幅排行",
        2: "行业独立设备数",
        3: "行业使用次数",
        4: "行业有效使用时间占比",
    }
    overview_sections: list[str] = []
    overview_keywords: list[str] = []
    for overview_type, overview_label in overview_labels.items():
        overview_data = fetch_json(
            f"{AD_INDEX_API_BASE_URL}/app/getClassIndex?timeid={time_name}&type={overview_type}",
            headers=api_headers,
        )
        if not isinstance(overview_data, dict):
            continue
        rows = overview_data.get("List") or []
        if not isinstance(rows, list):
            continue
        for row in rows[:3]:
            if not isinstance(row, dict):
                continue
            class_name = clean_text(str(row.get("KclassName") or ""))
            if not class_name:
                continue
            metric_value = format_metric_number(row.get("num"))
            if overview_type in (1, 4):
                metric_value = format_signed_percent(row.get("num"))
            elif overview_type == 2:
                metric_value = f"{metric_value}亿"
            elif overview_type == 3:
                metric_value = f"{metric_value}亿次"
            overview_sections.append(
                f"{overview_label} | {class_name} | {metric_value}"
            )
            overview_keywords.append(class_name)

    app_rank_data = fetch_json(
        (
            f"{AD_INDEX_API_BASE_URL}/app/GetDataList2?classId=0&classLevel=0"
            f"&timeid={time_name}&orderBy=2"
        ),
        headers=api_headers,
    )
    outline_sections: list[str] = []
    if isinstance(app_rank_data, dict):
        rows = app_rank_data.get("List") or []
        if isinstance(rows, list):
            for row in rows[:8]:
                if not isinstance(row, dict):
                    continue
                line = build_app_index_metric_line(row)
                if clean_text(line):
                    outline_sections.append(line)

    outline_sections = dedupe_preserve_order(overview_sections + outline_sections)
    summary_parts = [config.summary_hint]
    if snapshot_date:
        summary_parts.append(f"当前可见快照时间：{snapshot_date}。")
    if overview_sections:
        summary_parts.append(
            "页面公开类目指标包括：" + "；".join(overview_sections[:6]) + "。"
        )
    if outline_sections:
        summary_parts.append(
            "页面公开 APP 榜单包括："
            + "；".join(
                [line for line in outline_sections if "独立设备(万台)" in line][:5]
            )
            + "。"
        )

    keywords = dedupe_preserve_order(config.keywords + overview_keywords[:6])
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=" ".join(summary_parts),
        outline_sections=outline_sections,
        chart_catalog="\n".join(outline_sections),
        keywords=keywords,
    )


def fetch_device_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured leaderboard data from the public device index APIs."""
    request_token = build_request_token()
    api_headers = {
        "Referer": "https://index.iresearch.com.cn/new/",
        "Token": request_token,
    }
    date_ranges = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/home/deviceMonth",
        headers=api_headers,
    )
    if not isinstance(date_ranges, list) or not date_ranges:
        raise ValueError("Device index date API returned no usable snapshot date")

    current_date_item = next(
        (
            item
            for item in date_ranges
            if isinstance(item, dict) and clean_text(str(item.get("id") or ""))
        ),
        None,
    )
    if current_date_item is None:
        raise ValueError("Device index date API did not expose a usable value")

    time_name = clean_text(str(current_date_item.get("id") or ""))
    snapshot_date = format_snapshot_date(
        time_name,
        label=str(current_date_item.get("name") or ""),
    )

    rank_data = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/Device/GetTopBrandData?osType=0&topNum=20&week={time_name}",
        headers=api_headers,
    )
    outline_sections: list[str] = []
    device_keywords: list[str] = []
    if isinstance(rank_data, dict):
        rows = rank_data.get("List") or []
        if isinstance(rows, list):
            for row in rows[:8]:
                if not isinstance(row, dict):
                    continue
                line = build_device_index_metric_line(row)
                if clean_text(line):
                    outline_sections.append(line)
                brand_name = clean_text(str(row.get("BrandName") or ""))
                if brand_name:
                    device_keywords.append(brand_name)

    summary_parts = [config.summary_hint]
    if snapshot_date:
        summary_parts.append(f"当前可见快照时间：{snapshot_date}。")
    if outline_sections:
        summary_parts.append(
            "页面公开厂商品牌排名包括：" + "；".join(outline_sections[:6]) + "。"
        )

    keywords = dedupe_preserve_order(config.keywords + device_keywords[:6] + ["覆盖率"])
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=" ".join(summary_parts),
        outline_sections=outline_sections,
        chart_catalog="\n".join(outline_sections),
        keywords=keywords,
    )


def fetch_video_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured leaderboard data from the public video index APIs."""
    date_ranges = fetch_json(
        f"{AD_INDEX_API_BASE_URL}/Content/Json/videoMonthSpans.json?t={build_request_token()}"
    )
    if not isinstance(date_ranges, list) or not date_ranges:
        raise ValueError("Video index date API returned no usable snapshot date")

    current_date_item = next(
        (
            item
            for item in date_ranges
            if isinstance(item, dict) and clean_text(str(item.get("ID") or ""))
        ),
        None,
    )
    if current_date_item is None:
        raise ValueError("Video index date API did not expose a usable value")

    time_name = clean_text(str(current_date_item.get("ID") or ""))
    snapshot_date = format_snapshot_date(
        time_name,
        label=str(current_date_item.get("TimeName") or ""),
    )

    class_ids = (1, 2, 3, 4)
    outline_sections: list[str] = []
    video_keywords: list[str] = []
    for class_id in class_ids:
        rank_data = fetch_json(
            (
                f"{AD_INDEX_API_BASE_URL}/Video/GetDataList?classId={class_id}"
                f"&deviceTypeId=1&timeId={time_name}&pageSize=10"
            )
        )
        if not isinstance(rank_data, dict):
            continue
        rows = rank_data.get("List") or []
        if not isinstance(rows, list):
            continue
        for row in rows[:3]:
            if not isinstance(row, dict):
                continue
            class_label = (
                clean_text(str(row.get("ClassName") or "")) or f"类目{class_id}"
            )
            line = build_video_index_metric_line(class_label, row)
            if clean_text(line):
                outline_sections.append(line)
            if class_label:
                video_keywords.append(class_label)

    outline_sections = dedupe_preserve_order(outline_sections)
    summary_parts = [config.summary_hint]
    if snapshot_date:
        summary_parts.append(f"当前可见快照时间：{snapshot_date}。")
    if outline_sections:
        summary_parts.append(
            "页面公开内容热度榜单包括：" + "；".join(outline_sections[:8]) + "。"
        )

    keywords = dedupe_preserve_order(config.keywords + video_keywords[:6] + ["UV"])
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=" ".join(summary_parts),
        outline_sections=outline_sections,
        chart_catalog="\n".join(outline_sections),
        keywords=keywords,
    )


def fetch_index_snapshot_data(config: IndexSnapshotConfig) -> IndexSnapshotData:
    """Fetch structured data for a configured iResearch index snapshot."""
    if config.report_id == "irindex.ai":
        try:
            return fetch_ai_index_snapshot_data(config)
        except Exception:
            pass
    if config.report_id == "irindex.ad":
        try:
            return fetch_ad_index_snapshot_data(config)
        except Exception:
            pass
    if config.report_id == "irindex.app":
        try:
            return fetch_app_index_snapshot_data(config)
        except Exception:
            pass
    if config.report_id == "irindex.device":
        try:
            return fetch_device_index_snapshot_data(config)
        except Exception:
            pass
    if config.report_id == "irindex.video":
        try:
            return fetch_video_index_snapshot_data(config)
        except Exception:
            pass

    html = fetch_html(config.detail_url)
    text = html_to_text(html)
    snapshot_date = extract_index_snapshot_date(text) or ""
    top_items = extract_index_top_items(config, text)
    summary = build_index_snapshot_summary(config, snapshot_date, top_items)
    return IndexSnapshotData(
        snapshot_date=snapshot_date,
        summary=summary,
        outline_sections=top_items,
        chart_catalog="\n".join(top_items),
        keywords=config.keywords,
    )


def extract_index_snapshot_date(text: str) -> str | None:
    """Extract a visible snapshot date from an index page text blob."""
    patterns = (
        r"((?:19|20)\d{2}-\d{2}-\d{2})",
        r"((?:19|20)\d{2}-\d{2})",
        r"((?:19|20)\d{2}年\d{1,2}月\d{1,2}日)",
        r"((?:19|20)\d{2}年\d{1,2}月)",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return clean_text(match.group(1))
    return None


def extract_index_top_items(config: IndexSnapshotConfig, text: str) -> list[str]:
    """Extract a few readable top items from an index page text blob."""
    patterns_by_config: dict[str, list[str]] = {
        "irindex.ai": [
            r"([A-Za-z0-9一-龥（）()·\-]{2,30}\s+人工智能-[^\s]{2,20}\s+[\d,]+(?:\.\d+)?)"
        ],
        "irindex.app": [
            r"([A-Za-z0-9一-龥（）()·\-]{2,30}\s+(?:通讯聊天|短视频|电子商务|金融理财|旅游出行|聚合资讯|社交网络|实用工具)\s*-\s*[^\s]{2,20}\s+[\d,]+)"
        ],
        "irindex.ad": [
            r"([A-Za-z0-9一-龥（）()·\-]+>>[A-Za-z0-9一-龥（）()·\-]+\s*[\d,]+(?:\.\d+)?)"
        ],
        "irindex.device": [r"([A-Za-z0-9一-龥（）()·\-]{1,20}\s+\d+(?:\.\d+)?%)"],
        "irindex.video": [
            r"([A-Za-z0-9一-龥（）()·《》“”\-]{2,40}\s+(?:爱奇艺|腾讯视频|优酷|芒果TV|B站|哔哩哔哩)(?:\s+(?:爱奇艺|腾讯视频|优酷|芒果TV|B站|哔哩哔哩))?)"
        ],
    }
    items: list[str] = []
    for pattern in patterns_by_config.get(config.report_id, []):
        for match in re.findall(pattern, text):
            item = clean_text(match)
            if not item:
                continue
            if item not in items:
                items.append(item)
            if len(items) >= 8:
                return items
    return items


def build_index_snapshot_summary(
    config: IndexSnapshotConfig,
    snapshot_date: str | None,
    top_items: list[str],
) -> str:
    """Build a compact summary for an index snapshot page."""
    parts = [config.summary_hint]
    if snapshot_date:
        parts.append(f"当前可见快照时间：{snapshot_date}。")
    if top_items:
        parts.append("当前页面可见的头部数据包括：" + "；".join(top_items[:5]) + "。")
    return " ".join(parts)


def fetch_index_snapshot_summary(config: IndexSnapshotConfig) -> ReportSummary:
    """Fetch one configured iResearch index page as a search-ready snapshot."""
    snapshot_data = fetch_index_snapshot_data(config)
    return ReportSummary(
        source=IRESEARCH_INDEX_SOURCE,
        report_id=config.report_id,
        news_id=config.news_id,
        title=config.title,
        summary=snapshot_data.summary,
        industry=config.industry,
        author=config.author,
        published_at=snapshot_data.snapshot_date,
        views=0,
        keywords=snapshot_data.keywords,
        price=None,
        detail_url=require_report_link(config.detail_url),
        online_read_url=require_report_link(config.detail_url),
    )


def list_iresearch_index_snapshots() -> list[ReportSummary]:
    """Fetch all configured iResearch index snapshot pages."""
    snapshots: list[ReportSummary] = []
    for config in IRESEARCH_INDEX_CONFIGS:
        try:
            snapshots.append(fetch_index_snapshot_summary(config))
        except Exception:
            continue
    return snapshots


def score_report(query: str, report: ReportSummary) -> int:
    """Compute a simple lexical relevance score for a report."""
    query_text = clean_text(query).lower()
    query_years = {str(year) for year in extract_years(query)}
    title = report.title.lower()
    summary = report.summary.lower()
    industry = report.industry.lower()
    keyword_blob = " ".join(keyword.lower() for keyword in report.keywords)
    score = 0
    has_index_intent, matched_report_ids = classify_index_query(query)
    if query_text and query_text in title:
        score += 40
    if query_text and query_text in summary:
        score += 20
    if query_text and query_text in keyword_blob:
        score += 12
    for token in tokenize(query):
        token_lower = token.lower()
        is_year_token = token_lower in query_years
        title_weight = 4 if is_year_token else 12
        keyword_weight = 3 if is_year_token else 7
        industry_weight = 2 if is_year_token else 6
        summary_weight = 2 if is_year_token else 4
        if token_lower in title:
            score += title_weight
        if token_lower in keyword_blob:
            score += keyword_weight
        if token_lower in industry:
            score += industry_weight
        if token_lower in summary:
            score += summary_weight
    if report.source == IRESEARCH_INDEX_SOURCE and has_index_intent:
        score += 4
        if report.report_id in matched_report_ids:
            score += 28
        elif not matched_report_ids:
            score += 8
        if "指数" in title:
            score += 6
    if score > 0:
        score += min(report.views // 5000, 8)
    return score


def published_at_sort_key(value: str) -> tuple[int, int, int, int, int, int]:
    """Convert a published_at string into a descending-friendly datetime tuple."""
    normalized = clean_text(value)
    if not normalized:
        return (0, 0, 0, 0, 0, 0)

    for fmt in ("%Y/%m/%d %H:%M:%S", "%Y/%m/%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            parsed = datetime.strptime(normalized, fmt)
        except ValueError:
            continue
        return (
            parsed.year,
            parsed.month,
            parsed.day,
            parsed.hour,
            parsed.minute,
            parsed.second,
        )

    numbers = [int(part) for part in re.findall(r"\d+", normalized)]
    padded = (numbers + [0, 0, 0, 0, 0, 0])[:6]
    return tuple(padded)  # type: ignore[return-value]


def parse_cli_datetime(value: str) -> tuple[int, int, int, int, int, int]:
    """Parse a CLI date or datetime string into a sortable tuple."""
    normalized = clean_text(value)
    if not normalized:
        raise ValueError("Date value cannot be empty")

    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S"):
        try:
            parsed = datetime.strptime(normalized, fmt)
        except ValueError:
            continue
        return (
            parsed.year,
            parsed.month,
            parsed.day,
            parsed.hour,
            parsed.minute,
            parsed.second,
        )
    raise ValueError(
        "Unsupported date format. Use YYYY-MM-DD, YYYY/MM/DD, YYYY-MM-DD HH:MM:SS, or YYYY/MM/DD HH:MM:SS"
    )


def should_include_report(
    published_at: str,
    since: tuple[int, int, int, int, int, int] | None,
) -> bool:
    """Return whether a report passes the optional since-date filter."""
    if since is None:
        return True
    return published_at_sort_key(published_at) >= since


def extract_match(pattern: str, html: str) -> str | None:
    """Return the first cleaned regex capture from HTML."""
    match = re.search(pattern, html, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        return None
    return clean_text(match.group(1))


def extract_all_matches(pattern: str, html: str) -> list[str]:
    """Return all cleaned regex captures from HTML."""
    matches = re.findall(pattern, html, flags=re.DOTALL | re.IGNORECASE)
    cleaned: list[str] = []
    for match in matches:
        raw_value = match if isinstance(match, str) else match[0]
        value = clean_text(html_to_text(raw_value))
        if value and value not in cleaned:
            cleaned.append(value)
    return cleaned


def extract_iresearch_section(html: str, heading: str) -> str:
    """Extract a section block delimited by iResearch `<h3>` headings."""
    pattern = rf"<h3>\s*{re.escape(heading)}\s*</h3>\s*<p>(.*?)</p>"
    match = re.search(pattern, html, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        return ""
    return html_to_text(match.group(1))


def report_from_iresearch_item(item: dict[str, Any]) -> ReportSummary:
    """Map an iResearch list API item into a typed report summary."""
    news_id = int(item["NewsId"])
    return ReportSummary(
        source=IRESEARCH_SOURCE,
        report_id=item["Id"],
        news_id=news_id,
        title=clean_text(item.get("Title") or item.get("sTitle") or ""),
        summary=clean_text(item.get("Content") or ""),
        industry=clean_text(item.get("industry") or ""),
        author=clean_text(item.get("Author") or ""),
        published_at=clean_text(item.get("Uptime") or ""),
        views=int(item.get("views") or 0),
        keywords=[clean_text(value) for value in item.get("Keyword") or [] if value],
        price=int(item.get("Price") or 0),
        detail_url=normalize_report_link(item.get("VisitUrl")),
        online_read_url=build_iresearch_viewer_url(news_id),
    )


def list_iresearch_reports(
    pages: int,
    page_size: int,
    last_id: str = IRESEARCH_DEFAULT_LAST_ID,
    fee: int = 0,
    date: str = "",
) -> list[ReportSummary]:
    """Fetch multiple pages of the iResearch free report feed.

    The public API conceptually uses large page sizes, but the live endpoint
    currently fails at 100 items in a single request. To keep a logical
    page-size of 100 while remaining compatible, the script transparently
    splits large fetches into multiple 50-item backend requests.
    """
    reports: list[ReportSummary] = []
    seen_ids: set[str] = set()
    cursor = last_id
    remaining_items = max(0, pages * page_size)

    while remaining_items > 0:
        request_page_size = min(IRESEARCH_MAX_BATCH_SIZE, remaining_items)
        payload = fetch_json(
            build_iresearch_list_url(
                cursor,
                request_page_size,
                fee=fee,
                date=date,
            )
        )
        if payload.get("Status") != "success":
            raise RuntimeError(f"Unexpected API status: {payload.get('Status')!r}")
        batch = [report_from_iresearch_item(item) for item in payload.get("List") or []]
        if not batch:
            break
        for report in batch:
            if not report.detail_url:
                continue
            if report.report_id in seen_ids:
                continue
            reports.append(report)
            seen_ids.add(report.report_id)
        cursor = batch[-1].report_id
        remaining_items -= len(batch)
        if len(batch) < request_page_size:
            break
    return reports


def parse_questmobile_card_keywords(value: str) -> list[str]:
    """Normalize the QuestMobile card keyword blob into a list."""
    return [
        clean_text(keyword)
        for keyword in re.split(r"[、|]", value.replace(" ", ""))
        if clean_text(keyword)
    ]


def report_from_questmobile_item(item: dict[str, Any]) -> ReportSummary:
    """Map a QuestMobile article-list item into a typed report summary."""
    news_id = int(item["id"])
    industry_list = [
        clean_text(value) for value in item.get("industryList") or [] if value
    ]
    label_list = [clean_text(value) for value in item.get("labelList") or [] if value]
    return ReportSummary(
        source=QUESTMOBILE_SOURCE,
        report_id=f"qm.{news_id}",
        news_id=news_id,
        title=clean_text(item.get("title") or ""),
        summary=clean_text(item.get("introduction") or item.get("content") or ""),
        industry=" | ".join(industry_list),
        author="QuestMobile 研究院",
        published_at=clean_text(item.get("publishTime") or ""),
        views=0,
        keywords=label_list,
        price=None,
        detail_url=build_questmobile_detail_url(news_id),
        online_read_url=build_questmobile_detail_url(news_id),
    )


def list_questmobile_reports(
    pages: int,
    page_size: int,
    industry_id: int = -1,
    label_id: int = -1,
) -> list[ReportSummary]:
    """Fetch paginated public QuestMobile reports from the article-list API."""
    reports: list[ReportSummary] = []
    seen_ids: set[int] = set()
    total_pages: int | None = None
    for page_no in range(1, pages + 1):
        payload = fetch_json(
            build_questmobile_list_url(
                page_no=page_no,
                page_size=page_size,
                industry_id=industry_id,
                label_id=label_id,
            )
        )
        if int(payload.get("code") or 0) != 100200:
            raise RuntimeError(
                f"Unexpected QuestMobile API status: {payload.get('code')!r}"
            )
        batch = [
            report_from_questmobile_item(item) for item in payload.get("data") or []
        ]
        if not batch:
            break
        for report in batch:
            if not report.detail_url:
                continue
            if report.news_id in seen_ids:
                continue
            reports.append(report)
            seen_ids.add(report.news_id)
        total_pages = int(payload.get("totalPage") or 0) or total_pages
        if total_pages is not None and page_no >= total_pages:
            break
    return reports


def build_scored_results(
    query: str,
    reports: list[ReportSummary],
    normalized_industry: str,
    since_filter: tuple[int, int, int, int, int, int] | None,
) -> list[dict[str, Any]]:
    """Filter and score report summaries into serializable search results."""
    scored_results: list[dict[str, Any]] = []
    for report in reports:
        if normalized_industry and normalized_industry not in report.industry.lower():
            continue
        if not should_include_report(report.published_at, since_filter):
            continue
        score = score_report(query, report)
        if score <= 0:
            continue
        result = asdict(report)
        result["score"] = score
        result["source_priority"] = SOURCE_PRIORITY[report.source]
        scored_results.append(result)
    return scored_results


def report_summary_from_payload(payload: dict[str, Any]) -> ReportSummary:
    """Rebuild a typed report summary from a serialized payload."""
    return ReportSummary(
        source=str(payload.get("source") or ""),
        report_id=str(payload.get("report_id") or ""),
        news_id=int(payload.get("news_id") or 0),
        title=clean_text(str(payload.get("title") or "")),
        summary=clean_text(str(payload.get("summary") or "")),
        industry=clean_text(str(payload.get("industry") or "")),
        author=clean_text(str(payload.get("author") or "")),
        published_at=clean_text(str(payload.get("published_at") or "")),
        views=int(payload.get("views") or 0),
        keywords=[
            clean_text(item)
            for item in payload.get("keywords") or []
            if clean_text(str(item))
        ],
        price=(
            int(payload["price"]) if payload.get("price") not in (None, "") else None
        ),
        detail_url=normalize_report_link(str(payload.get("detail_url") or "")),
        online_read_url=normalize_report_link(str(payload.get("online_read_url") or ""))
        or None,
    )


def sort_scored_results(
    scored_results: list[dict[str, Any]],
    query: str,
    sort_by: str,
    sort_order: str,
) -> list[dict[str, Any]]:
    """Sort scored results within a source by the configured strategy."""

    def recency_key(item: dict[str, Any]) -> tuple[int, int, int, int, int, int]:
        return published_at_sort_key(item["published_at"])

    def relevance_key(item: dict[str, Any]) -> int:
        return int(item["score"])

    def views_key(item: dict[str, Any]) -> int:
        return int(item["views"])

    query_years = extract_years(query)

    def title_year_key(item: dict[str, Any]) -> tuple[int, int]:
        title_years = extract_years(str(item.get("title") or ""))
        matched_years = [year for year in title_years if year in query_years]
        return (
            max(matched_years, default=0),
            max(title_years, default=0),
        )

    reverse_sort = sort_order == "desc"
    sorted_results = list(scored_results)
    if query_years:
        sorted_results.sort(
            key=lambda item: (
                title_year_key(item),
                relevance_key(item),
                recency_key(item),
            ),
            reverse=True,
        )
        return sorted_results

    if sort_by == "recency":
        sorted_results.sort(
            key=lambda item: (
                recency_key(item),
                relevance_key(item),
                views_key(item),
            ),
            reverse=reverse_sort,
        )
    else:
        sorted_results.sort(
            key=lambda item: (
                relevance_key(item),
                recency_key(item),
                views_key(item),
            ),
            reverse=reverse_sort,
        )
    return sorted_results


def search_reports(
    query: str,
    pages: int,
    page_size: int,
    limit: int,
    industry: str | None = None,
    include_questmobile: bool = True,
    sort_by: str = "recency",
    sort_order: str = "desc",
    since: str | None = None,
) -> list[dict[str, Any]]:
    """Search reports, always ordering iResearch ahead of QuestMobile."""
    if limit <= 0:
        return []

    normalized_industry = clean_text(industry or "").lower()
    since_filter = parse_cli_datetime(since) if since else None

    iresearch_reports = list_iresearch_reports(pages=pages, page_size=page_size)
    iresearch_results = build_scored_results(
        query,
        iresearch_reports,
        normalized_industry,
        since_filter,
    )
    fetched_pages = pages
    last_cursor = iresearch_reports[-1].report_id if iresearch_reports else ""

    query_has_years = bool(extract_years(query))
    query_has_topic_tokens = bool(non_year_query_tokens(query))

    while iresearch_reports and fetched_pages < SEARCH_AUTO_MAX_PAGES:
        enough_results = len(iresearch_results) >= limit
        enough_topic_precision = not (
            query_has_years
            and query_has_topic_tokens
            and not has_strong_title_topic_match(iresearch_results, query)
        )
        if enough_results and enough_topic_precision:
            break

        extra_pages = min(SEARCH_AUTO_PAGE_STEP, SEARCH_AUTO_MAX_PAGES - fetched_pages)
        extra_reports = list_iresearch_reports(
            pages=extra_pages,
            page_size=page_size,
            last_id=last_cursor,
        )
        if not extra_reports:
            break
        iresearch_results.extend(
            build_scored_results(
                query,
                extra_reports,
                normalized_industry,
                since_filter,
            )
        )
        iresearch_reports = extra_reports
        last_cursor = extra_reports[-1].report_id
        fetched_pages += extra_pages
        if len(extra_reports) < extra_pages * page_size:
            break

    iresearch_results = sort_scored_results(
        iresearch_results,
        query,
        sort_by,
        sort_order,
    )

    index_snapshot_results = prioritize_index_results(
        query,
        build_ranked_results(
            query,
            list_iresearch_index_snapshots(),
            normalized_industry,
            since_filter,
            sort_by,
            sort_order,
        ),
    )
    preferred_index_results = select_preferred_index_results(
        query,
        index_snapshot_results,
        limit,
    )

    if not include_questmobile:
        if len(iresearch_results) >= limit and not preferred_index_results:
            return iresearch_results[:limit]
        formal_slots = max(0, limit - len(preferred_index_results))
        selected: list[dict[str, Any]] = []
        seen_ids: set[str] = set()
        extend_unique_results(
            selected, iresearch_results[:formal_slots], seen_ids, limit
        )
        extend_unique_results(selected, preferred_index_results, seen_ids, limit)
        if len(selected) < limit:
            extend_unique_results(selected, index_snapshot_results, seen_ids, limit)
        return selected[:limit]

    if len(iresearch_results) >= limit and not preferred_index_results:
        return iresearch_results[:limit]

    questmobile_results = build_ranked_results(
        query,
        list_questmobile_reports(pages=pages, page_size=page_size),
        normalized_industry,
        since_filter,
        sort_by,
        sort_order,
    )

    if not iresearch_results and not preferred_index_results:
        if index_snapshot_results:
            if len(index_snapshot_results) >= limit:
                return index_snapshot_results[:limit]
            remaining_slots = max(0, limit - len(index_snapshot_results))
            return index_snapshot_results + questmobile_results[:remaining_slots]
        return questmobile_results[:limit]

    formal_slots = max(0, limit - len(preferred_index_results))
    selected = []
    seen_ids = set()
    extend_unique_results(selected, iresearch_results[:formal_slots], seen_ids, limit)
    extend_unique_results(selected, preferred_index_results, seen_ids, limit)
    if len(selected) < limit:
        extend_unique_results(selected, index_snapshot_results, seen_ids, limit)
    if len(selected) < limit:
        extend_unique_results(selected, questmobile_results, seen_ids, limit)
    return selected[:limit]


def group_reports_by_source(
    reports: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    """Group search results by source using the configured source priority."""
    grouped: dict[str, list[dict[str, Any]]] = {
        IRESEARCH_SOURCE: [],
        QUESTMOBILE_SOURCE: [],
        IRESEARCH_INDEX_SOURCE: [],
    }
    for report in reports:
        grouped.setdefault(report["source"], []).append(report)
    return {
        source: grouped[source]
        for source in sorted(grouped, key=lambda source: SOURCE_PRIORITY[source])
    }


def extract_iresearch_viewer_images(news_id: int) -> list[str]:
    """Extract image URLs from the iResearch online reader page."""
    html = fetch_html(build_iresearch_viewer_url(news_id))
    matches = re.findall(
        rf"https://pic\.iresearch\.cn/rimgs/{news_id}/\d+\.jpg",
        html,
        flags=re.IGNORECASE,
    )
    images: list[str] = []
    for match in matches:
        if match not in images:
            images.append(match)
    return images


def resolve_iresearch_summary(
    identifier: str,
    pages: int,
    page_size: int,
    last_id: str,
) -> ReportSummary:
    """Resolve an iResearch identifier into a report summary."""
    if identifier.startswith("http://") or identifier.startswith("https://"):
        news_id_match = re.search(r"/(\d+)\.shtml", identifier)
        news_id = int(news_id_match.group(1)) if news_id_match else None
        if news_id is not None:
            for report in list_iresearch_reports(
                pages=pages,
                page_size=page_size,
                last_id=last_id,
            ):
                if report.news_id == news_id or report.detail_url == identifier:
                    return report
        raise ValueError(
            "Could not resolve the iResearch report URL from the current feed window"
        )

    reports = list_iresearch_reports(pages=pages, page_size=page_size, last_id=last_id)
    for report in reports:
        if report.report_id == identifier:
            return report
        if str(report.news_id) == identifier:
            return report
    raise ValueError(f"Could not find iResearch report identifier: {identifier}")


def fetch_iresearch_detail(
    identifier: str,
    pages: int,
    page_size: int,
    last_id: str,
    include_images: bool,
) -> ReportDetail:
    """Fetch detail information for an iResearch report."""
    summary = resolve_iresearch_summary(
        identifier,
        pages=pages,
        page_size=page_size,
        last_id=last_id,
    )
    return fetch_iresearch_detail_from_summary(summary, include_images=include_images)


def fetch_iresearch_detail_from_summary(
    summary: ReportSummary,
    include_images: bool,
) -> ReportDetail:
    """Fetch iResearch detail information using an already-resolved summary."""
    detail_url = require_report_link(summary.detail_url)
    html = fetch_html(detail_url)
    meta_summary = extract_match(r'<meta name="description" content="([^"]+)"', html)
    source_block = extract_match(r"来源：\s*([^<]+?)\s+\d{4}/\d{1,2}/\d{1,2}", html)
    published_at = extract_match(
        r"来源：\s*[^<]+?\s+(\d{4}/\d{1,2}/\d{1,2}\s+\d{1,2}:\d{2}:\d{2})",
        html,
    )
    industry = extract_match(r"所属行业：</span><em>(.*?)</em>", html)
    report_type = extract_match(r"报告类型：</span><em>(.*?)</em>", html)
    page_count_text = extract_match(r"页数：</span><em>(.*?)</em>", html)
    chart_count_text = extract_match(r"图表：</span><em>(.*?)</em>", html)
    price = extract_match(r'<li class="price">(.*?)</li>', html)
    online_read_path = extract_match(
        r'href="([^"]*report_pdf\.aspx\?id=\d+)"[^>]*>\s*在线浏览',
        html,
    )
    online_read_url = None
    if online_read_path:
        online_read_url = (
            online_read_path
            if online_read_path.startswith("http")
            else f"https://report.iresearch.cn{online_read_path}"
        )
    viewer_images = (
        extract_iresearch_viewer_images(summary.news_id) if include_images else []
    )
    public_summary = (
        extract_iresearch_section(html, "报告简介") or meta_summary or summary.summary
    )
    catalog = extract_iresearch_section(html, "目录")
    chart_catalog = extract_iresearch_section(html, "图表目录")
    outline_sections = extract_outline_sections(catalog)
    return ReportDetail(
        source=IRESEARCH_SOURCE,
        report_id=summary.report_id,
        news_id=summary.news_id,
        title=summary.title,
        author=source_block or summary.author,
        published_at=published_at or summary.published_at,
        industry=industry or summary.industry,
        report_type=report_type,
        page_count=int(page_count_text)
        if page_count_text and page_count_text.isdigit()
        else None,
        chart_count=int(chart_count_text)
        if chart_count_text and chart_count_text.isdigit()
        else None,
        price=price,
        detail_url=detail_url,
        online_read_url=online_read_url or summary.online_read_url,
        summary=public_summary,
        interpretation=build_interpretation(
            IRESEARCH_SOURCE,
            summary.title,
            public_summary,
            outline_sections,
            chart_catalog,
            summary.keywords,
        ),
        evidence_boundary=build_evidence_boundary(
            IRESEARCH_SOURCE,
            has_viewer_images=bool(viewer_images),
        ),
        outline_sections=outline_sections,
        catalog=catalog,
        chart_catalog=chart_catalog,
        viewer_images=viewer_images,
        keywords=summary.keywords,
    )


def resolve_questmobile_identifier(identifier: str) -> int:
    """Resolve a QuestMobile identifier into a numeric report id."""
    if identifier.startswith("qm."):
        return int(identifier.split(".", maxsplit=1)[1])
    if identifier.startswith("qm:"):
        return int(identifier.split(":", maxsplit=1)[1])
    if "questmobile.com.cn/research/report/" in identifier:
        match = re.search(r"/research/report/(\d+)", identifier)
        if match:
            return int(match.group(1))
    raise ValueError("Could not resolve the QuestMobile identifier")


def extract_questmobile_metadata(
    html: str,
) -> tuple[str | None, list[str], str | None, str | None]:
    """Extract industry, keywords, published date, and author from QuestMobile."""
    industry_fragment = extract_match(
        r"行业：(.+?)</div></div><div[^>]*class=\"other\"", html
    )
    keywords_fragment = extract_match(
        r"关键词：</strong>(.+?)</div></div><div[^>]*class=\"dataAndsource\"", html
    )
    published_at = extract_match(
        r"<span[^>]*>(\d{4}-\d{2}-\d{2})</span></div><div[^>]*class=\"source\"", html
    )
    author = extract_match(r"class=\"source\">来源：([^<]+)</div>", html)

    industry = None
    if industry_fragment:
        industry = clean_text(html_to_text(industry_fragment)).replace("|", " | ")

    keywords: list[str] = []
    if keywords_fragment:
        keywords = extract_all_matches(r"<span>(.*?)</span>", keywords_fragment)
        if not keywords:
            keywords = [clean_text(html_to_text(keywords_fragment))]

    return industry, keywords, published_at, author


def extract_questmobile_catalog(body_html: str) -> str:
    """Extract top-level section headings from QuestMobile detail content."""
    headings = [
        heading
        for heading in extract_all_matches(r"<h3[^>]*>(.*?)</h3>", body_html)
        if re.match(r"^[一二三四五六七八九十]+、", heading)
    ]
    return "\n".join(headings)


def extract_questmobile_chart_catalog(body_html: str) -> str:
    """Extract lower-level narrative headings from QuestMobile detail content."""
    headings = [
        heading
        for heading in extract_all_matches(r"<h4[^>]*>(.*?)</h4>", body_html)
        if heading and not heading.startswith("http") and len(heading) <= 120
    ]
    return "\n".join(headings)


def extract_questmobile_images(body_html: str) -> list[str]:
    """Extract QuestMobile report image URLs from the article body."""
    matches = re.findall(
        r"https://ws\.questmobile\.cn/report/article/images/[A-Za-z0-9]+\.png",
        body_html,
        flags=re.IGNORECASE,
    )
    images: list[str] = []
    for match in matches:
        if match not in images:
            images.append(match)
    return images


def fetch_questmobile_detail(identifier: str, include_images: bool) -> ReportDetail:
    """Fetch detail information for a QuestMobile report."""
    news_id = resolve_questmobile_identifier(identifier)
    detail_url = build_questmobile_detail_url(news_id)
    html = fetch_html(detail_url)
    title = (
        extract_match(r"<h1[^>]*>(.*?)</h1>", html) or f"QuestMobile Report {news_id}"
    )
    meta_summary = extract_match(r'<meta name="description" content="([^"]+)"', html)
    industry, keywords, published_at, author = extract_questmobile_metadata(html)
    intro = extract_match(r"class=\"daoyu\">(.*?)</div><div[^>]*innerhtml=", html)
    body_anchor = html.find("<h1")
    body_html = html[body_anchor:] if body_anchor != -1 else html
    body_html = re.sub(r'\sinnerhtml="[^"]*"', "", body_html)
    chart_catalog = extract_questmobile_chart_catalog(body_html)
    summary_text = intro or meta_summary or ""
    outline_sections = extract_questmobile_catalog(body_html).splitlines()
    return ReportDetail(
        source=QUESTMOBILE_SOURCE,
        report_id=f"qm.{news_id}",
        news_id=news_id,
        title=title,
        author=author or "QuestMobile 研究院",
        published_at=published_at,
        industry=industry,
        report_type="Public report page",
        page_count=None,
        chart_count=None,
        price=None,
        detail_url=detail_url,
        online_read_url=detail_url,
        summary=summary_text,
        interpretation=build_interpretation(
            QUESTMOBILE_SOURCE,
            title,
            summary_text,
            [clean_text(item) for item in outline_sections if clean_text(item)],
            chart_catalog,
            keywords,
        ),
        evidence_boundary=build_evidence_boundary(
            QUESTMOBILE_SOURCE,
            has_viewer_images=include_images,
        ),
        outline_sections=[
            clean_text(item) for item in outline_sections if clean_text(item)
        ],
        catalog=extract_questmobile_catalog(body_html),
        chart_catalog=chart_catalog,
        viewer_images=extract_questmobile_images(body_html) if include_images else [],
        keywords=keywords,
    )


def fetch_report_detail(
    identifier: str,
    pages: int,
    page_size: int,
    last_id: str,
    include_images: bool,
) -> ReportDetail:
    """Fetch detail information for a report from either source."""
    if identifier.startswith("qm.") or identifier.startswith("qm:"):
        return fetch_questmobile_detail(identifier, include_images=include_images)
    if "questmobile.com.cn/research/report/" in identifier:
        return fetch_questmobile_detail(identifier, include_images=include_images)
    index_config = find_index_snapshot_config(identifier)
    if index_config is not None:
        snapshot_data = fetch_index_snapshot_data(index_config)
        return ReportDetail(
            source=IRESEARCH_INDEX_SOURCE,
            report_id=index_config.report_id,
            news_id=index_config.news_id,
            title=index_config.title,
            author=index_config.author,
            published_at=snapshot_data.snapshot_date,
            industry=index_config.industry,
            report_type=index_config.report_type,
            page_count=None,
            chart_count=None,
            price=None,
            detail_url=require_report_link(index_config.detail_url),
            online_read_url=require_report_link(index_config.detail_url),
            summary=snapshot_data.summary,
            interpretation=build_interpretation(
                IRESEARCH_INDEX_SOURCE,
                index_config.title,
                snapshot_data.summary,
                snapshot_data.outline_sections,
                snapshot_data.chart_catalog,
                snapshot_data.keywords,
            ),
            evidence_boundary=(
                "当前解读优先基于指数页前端公开请求 API 返回的榜单、快照时间和指标值；"
                "若 API 不可用，则退回公开页面可见文本。它反映的是公开指数页的数据切片，而不是完整后台数据库导出。"
            ),
            outline_sections=snapshot_data.outline_sections,
            catalog="\n".join(snapshot_data.outline_sections),
            chart_catalog=snapshot_data.chart_catalog,
            viewer_images=[],
            keywords=snapshot_data.keywords,
        )
    return fetch_iresearch_detail(
        identifier,
        pages=pages,
        page_size=page_size,
        last_id=last_id,
        include_images=include_images,
    )


def with_report_link(payload: dict[str, Any]) -> dict[str, Any]:
    """Add a stable report_link field to a serialized report payload."""
    enriched = dict(payload)
    enriched["report_link"] = require_report_link(enriched.get("detail_url"))
    return enriched


def render_report_list_markdown(
    reports: list[dict[str, Any]],
    sort_by: str | None = None,
    sort_order: str | None = None,
    since: str | None = None,
) -> str:
    """Render report summaries as Markdown."""
    lines = ["# Report Search Results", ""]
    if sort_by and sort_order:
        lines.append(f"- Sort: {sort_by} ({sort_order})")
    if since:
        lines.append(f"- Since: {since}")
    if len(lines) > 2:
        lines.append("")
    for index, report in enumerate(reports, start=1):
        lines.extend(
            [
                f"## {index}. {report['title']}",
                f"- Source: {report['source']}",
                f"- Report ID: {report['report_id']}",
                f"- News ID: {report['news_id']}",
                f"- Industry: {report['industry'] or 'Unknown'}",
                f"- Published: {report['published_at'] or 'Unknown'}",
                f"- Views: {report['views']}",
                f"- Score: {report.get('score', 0)}",
                f"- Keywords: {', '.join(report['keywords']) if report['keywords'] else 'None'}",
                f"- Report Link: {report['report_link']}",
                f"- Detail URL: {report['detail_url']}",
                f"- Online Read: {report['online_read_url'] or 'N/A'}",
                f"- Summary: {report['summary']}",
                "",
            ]
        )
    return "\n".join(lines).strip()


def render_grouped_report_list_markdown(
    grouped_reports: dict[str, list[dict[str, Any]]],
    sort_by: str | None = None,
    sort_order: str | None = None,
    since: str | None = None,
) -> str:
    """Render search results grouped by source with iResearch first."""
    lines = ["# Report Search Results", ""]
    if sort_by and sort_order:
        lines.append(f"- Sort: {sort_by} ({sort_order})")
    if since:
        lines.append(f"- Since: {since}")
    if len(lines) > 2:
        lines.append("")
    section_titles = {
        IRESEARCH_SOURCE: "iResearch Reports",
        QUESTMOBILE_SOURCE: "QuestMobile Reports",
        IRESEARCH_INDEX_SOURCE: "iResearch Index Snapshots",
    }
    for source in sorted(grouped_reports, key=lambda source: SOURCE_PRIORITY[source]):
        reports = grouped_reports[source]
        if not reports:
            continue
        lines.extend([f"## {section_titles.get(source, source.title())}", ""])
        for index, report in enumerate(reports, start=1):
            lines.extend(
                [
                    f"### {index}. {report['title']}",
                    f"- Report ID: {report['report_id']}",
                    f"- News ID: {report['news_id']}",
                    f"- Industry: {report['industry'] or 'Unknown'}",
                    f"- Published: {report['published_at'] or 'Unknown'}",
                    f"- Views: {report['views']}",
                    f"- Score: {report.get('score', 0)}",
                    f"- Keywords: {', '.join(report['keywords']) if report['keywords'] else 'None'}",
                    f"- Report Link: {report['report_link']}",
                    f"- Detail URL: {report['detail_url']}",
                    f"- Online Read: {report['online_read_url'] or 'N/A'}",
                    f"- Summary: {report['summary']}",
                    "",
                ]
            )
    return "\n".join(lines).strip()


def render_report_detail_markdown(report: ReportDetail) -> str:
    """Render a report detail object as Markdown."""
    lines = [
        f"# {report.title}",
        "",
        f"- Source: {report.source}",
        f"- Report ID: {report.report_id}",
        f"- News ID: {report.news_id}",
        f"- Author: {report.author or 'Unknown'}",
        f"- Published: {report.published_at or 'Unknown'}",
        f"- Industry: {report.industry or 'Unknown'}",
        f"- Report Type: {report.report_type or 'Unknown'}",
        f"- Page Count: {report.page_count if report.page_count is not None else 'Unknown'}",
        f"- Chart Count: {report.chart_count if report.chart_count is not None else 'Unknown'}",
        f"- Price: {report.price or 'Unknown'}",
        f"- Report Link: {report.detail_url}",
        f"- Detail URL: {report.detail_url}",
        f"- Online Read: {report.online_read_url or 'N/A'}",
        f"- Keywords: {', '.join(report.keywords) if report.keywords else 'None'}",
        "",
        "## Summary",
        report.summary or "",
        "",
        "## Interpretation",
        report.interpretation or "",
        "",
        "## Evidence Boundary",
        report.evidence_boundary or "",
        "",
        "## Outline Sections",
        "\n".join(report.outline_sections) if report.outline_sections else "",
        "",
        "## Catalog",
        report.catalog or "",
        "",
        "## Chart Catalog",
        report.chart_catalog or "",
    ]
    if report.viewer_images:
        lines.extend(["", "## Viewer Images", *report.viewer_images])
    return "\n".join(lines).strip()


def render_report_answer_markdown(report_answer: ReportAnswer) -> str:
    """Render a grounded report answer as Markdown."""
    lines = [
        f"# {report_answer.title}",
        "",
        f"- Source: {report_answer.source}",
        f"- Report ID: {report_answer.report_id}",
        f"- Question: {report_answer.question}",
        f"- Report Link: {report_answer.report_link}",
        f"- Online Read: {report_answer.online_read_url or 'N/A'}",
        "",
        "## Answer",
        report_answer.answer,
        "",
        "## Evidence",
        *(f"- {item}" for item in report_answer.evidence),
        "",
        "## Evidence Boundary",
        report_answer.evidence_boundary,
    ]
    if report_answer.verification_links:
        lines.extend(["", "## Verification Links", *report_answer.verification_links])
    return "\n".join(lines).strip()


def render_insight_markdown(insight: InsightAnalysis) -> str:
    """Render a structured market insight payload as Markdown."""
    signal_lines: list[str] = []
    if insight.primary_signal_source:
        signal_lines.append(f"- primary: {insight.primary_signal_source}")
    if insight.secondary_signal_source:
        signal_lines.append(f"- secondary: {insight.secondary_signal_source}")
    if not signal_lines:
        signal_lines.append("- No dominant index signal source identified")

    lines = [
        f"# Market Insight: {insight.query}",
        "",
        "## Executive Summary",
        insight.executive_summary,
        "",
        "## Signal Sources",
        *signal_lines,
        "",
        "## Market Judgement",
        insight.market_judgement,
        "",
        "## Market Signals",
        *(f"- {item}" for item in insight.market_signals),
        "",
        "## Industry Structure",
        *(f"- {item}" for item in insight.industry_structure),
        "",
        "## Competitive Landscape",
        *(f"- {item}" for item in insight.competitive_landscape),
        "",
        "## Growth Drivers",
        *(f"- {item}" for item in insight.growth_drivers),
        "",
        "## Risk Watchpoints",
        *(f"- {item}" for item in insight.risk_watchpoints),
        "",
        "## Future Trends",
        *(f"- {item}" for item in insight.future_trends),
        "",
        "## Evidence",
        *(f"- {item}" for item in insight.evidence),
        "",
        "## Source Breakdown",
        *(f"- {source}: {count}" for source, count in insight.source_breakdown.items()),
        "",
        "## Analyzed Items",
        *(
            f"- {item['title']} | {item['source']} | {item['published_at'] or 'Unknown'} | {item['report_link']}"
            for item in insight.analyzed_items
        ),
        "",
        "## Evidence Boundary",
        insight.evidence_boundary,
    ]
    return "\n".join(lines).strip()


def output_payload(
    payload: Any,
    output_format: str,
    render_markdown: Callable[[Any], str] | None = None,
) -> None:
    """Print payload as JSON or Markdown."""
    if output_format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    if render_markdown is None:
        raise ValueError("Markdown output requires a renderer")
    print(render_markdown(payload))


def warn_if_debug_last_id(last_id: str) -> None:
    """Warn when the deprecated debug-only last_id cursor is used explicitly."""
    if clean_text(last_id):
        print(
            "Warning: --last-id is deprecated for normal usage and should only be used for debugging older iResearch cursor windows.",
            file=sys.stderr,
        )


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser(
        "list",
        help="List the latest iResearch free reports",
    )
    list_parser.add_argument("--pages", type=int, default=1)
    list_parser.add_argument(
        "--page-size", type=int, default=IRESEARCH_DEFAULT_PAGE_SIZE
    )
    list_parser.add_argument(
        "--last-id",
        default=IRESEARCH_DEFAULT_LAST_ID,
        help=argparse.SUPPRESS,
    )
    list_parser.add_argument("--format", choices=("json", "markdown"), default="json")

    search_parser = subparsers.add_parser(
        "search",
        help="Search iResearch first and QuestMobile second",
    )
    search_parser.add_argument("query")
    search_parser.add_argument("--pages", type=int, default=SEARCH_DEFAULT_PAGES)
    search_parser.add_argument(
        "--page-size", type=int, default=IRESEARCH_DEFAULT_PAGE_SIZE
    )
    search_parser.add_argument("--limit", type=int, default=SEARCH_DEFAULT_LIMIT)
    search_parser.add_argument("--industry")
    search_parser.add_argument(
        "--sort-by",
        choices=("recency", "relevance"),
        default="recency",
        help="Sort within each source by recency first or relevance first",
    )
    search_parser.add_argument(
        "--sort-order",
        choices=("desc", "asc"),
        default="desc",
        help="Sort direction within each source; default is descending",
    )
    search_parser.add_argument(
        "--since",
        help="Only include reports published on or after this date",
    )
    search_parser.add_argument(
        "--no-questmobile",
        action="store_true",
        help="Disable QuestMobile as the secondary source",
    )
    search_parser.add_argument(
        "--iresearch-only",
        action="store_true",
        help="Use only iResearch results and disable QuestMobile fallback",
    )
    search_parser.add_argument(
        "--grouped",
        action="store_true",
        help="Group results by source with iResearch first and QuestMobile second",
    )
    search_parser.add_argument("--format", choices=("json", "markdown"), default="json")

    detail_parser = subparsers.add_parser(
        "detail",
        help="Fetch a report detail page from iResearch or QuestMobile",
    )
    detail_parser.add_argument("identifier")
    detail_parser.add_argument("--pages", type=int, default=8)
    detail_parser.add_argument(
        "--page-size", type=int, default=IRESEARCH_DEFAULT_PAGE_SIZE
    )
    detail_parser.add_argument(
        "--last-id",
        default=IRESEARCH_DEFAULT_LAST_ID,
        help=argparse.SUPPRESS,
    )
    detail_parser.add_argument("--include-images", action="store_true")
    detail_parser.add_argument("--format", choices=("json", "markdown"), default="json")

    answer_parser = subparsers.add_parser(
        "answer",
        help="Answer a question using public evidence from one report detail page",
    )
    answer_parser.add_argument("identifier")
    answer_parser.add_argument("question")
    answer_parser.add_argument("--pages", type=int, default=8)
    answer_parser.add_argument(
        "--page-size", type=int, default=IRESEARCH_DEFAULT_PAGE_SIZE
    )
    answer_parser.add_argument(
        "--last-id",
        default=IRESEARCH_DEFAULT_LAST_ID,
        help=argparse.SUPPRESS,
    )
    answer_parser.add_argument("--include-images", action="store_true")
    answer_parser.add_argument("--format", choices=("json", "markdown"), default="json")

    insight_parser = subparsers.add_parser(
        "insight",
        help="Synthesize market and industry insight from reports and index snapshots",
    )
    insight_parser.add_argument("query")
    insight_parser.add_argument("--pages", type=int, default=SEARCH_DEFAULT_PAGES)
    insight_parser.add_argument(
        "--page-size", type=int, default=IRESEARCH_DEFAULT_PAGE_SIZE
    )
    insight_parser.add_argument("--industry")
    insight_parser.add_argument(
        "--sort-by",
        choices=("recency", "relevance"),
        default="recency",
    )
    insight_parser.add_argument(
        "--sort-order",
        choices=("desc", "asc"),
        default="desc",
    )
    insight_parser.add_argument("--since")
    insight_parser.add_argument(
        "--no-questmobile",
        action="store_true",
        help="Disable QuestMobile as the secondary source",
    )
    insight_parser.add_argument(
        "--iresearch-only",
        action="store_true",
        help="Use only iResearch reports and index snapshots",
    )
    insight_parser.add_argument(
        "--format", choices=("json", "markdown"), default="json"
    )
    return parser


def main() -> int:
    """CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "list":
            warn_if_debug_last_id(args.last_id)
            report_list = [
                with_report_link(asdict(report))
                for report in list_iresearch_reports(
                    pages=args.pages,
                    page_size=args.page_size,
                    last_id=args.last_id,
                )
            ]
            output_payload(
                report_list,
                args.format,
                render_markdown=render_report_list_markdown,
            )
            return 0
        if args.command == "search":
            search_results = [
                with_report_link(report)
                for report in search_reports(
                    query=args.query,
                    pages=args.pages,
                    page_size=args.page_size,
                    limit=args.limit,
                    industry=args.industry,
                    include_questmobile=not (
                        args.no_questmobile or args.iresearch_only
                    ),
                    sort_by=args.sort_by,
                    sort_order=args.sort_order,
                    since=args.since,
                )
            ]
            if args.grouped or args.format == "markdown":
                grouped_results = group_reports_by_source(search_results)
                if args.format == "json":
                    print(json.dumps(grouped_results, ensure_ascii=False, indent=2))
                else:
                    print(
                        render_grouped_report_list_markdown(
                            grouped_results,
                            sort_by=args.sort_by,
                            sort_order=args.sort_order,
                            since=args.since,
                        )
                    )
                return 0
            output_payload(
                search_results,
                args.format,
                render_markdown=lambda reports: render_report_list_markdown(
                    reports,
                    sort_by=args.sort_by,
                    sort_order=args.sort_order,
                    since=args.since,
                ),
            )
            return 0
        if args.command == "detail":
            warn_if_debug_last_id(args.last_id)
            report_detail = fetch_report_detail(
                identifier=args.identifier,
                pages=args.pages,
                page_size=args.page_size,
                last_id=args.last_id,
                include_images=args.include_images,
            )
            if args.format == "json":
                print(
                    json.dumps(
                        with_report_link(asdict(report_detail)),
                        ensure_ascii=False,
                        indent=2,
                    )
                )
            else:
                print(render_report_detail_markdown(report_detail))
            return 0
        if args.command == "answer":
            warn_if_debug_last_id(args.last_id)
            report_detail = fetch_report_detail(
                identifier=args.identifier,
                pages=args.pages,
                page_size=args.page_size,
                last_id=args.last_id,
                include_images=args.include_images,
            )
            report_answer = build_report_answer(report_detail, args.question)
            if args.format == "json":
                print(json.dumps(asdict(report_answer), ensure_ascii=False, indent=2))
            else:
                print(render_report_answer_markdown(report_answer))
            return 0
        if args.command == "insight":
            insight = build_insight_analysis(
                query=args.query,
                pages=args.pages,
                page_size=args.page_size,
                industry=args.industry,
                include_questmobile=not (args.no_questmobile or args.iresearch_only),
                sort_by=args.sort_by,
                sort_order=args.sort_order,
                since=args.since,
            )
            if args.format == "json":
                print(json.dumps(asdict(insight), ensure_ascii=False, indent=2))
            else:
                print(render_insight_markdown(insight))
            return 0
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

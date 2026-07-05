#!/usr/bin/env python3
"""
arXiv neuroscience paper search script.
Searches multiple queries, filters by date, deduplicates, and outputs structured results.

Usage:
  python3 arxiv-neuroscience-search.py [days] [max_per_query]
  python3 arxiv-neuroscience-search.py 7 15   # last 7 days, 15 per query
"""

import arxiv
import sys
import time
from datetime import datetime, timedelta


def search_neuroscience(days=7, max_per_query=15):
    """Search arXiv for recent neuroscience papers."""

    queries = [
        "cat:q-bio.NC AND (neural OR brain OR spiking)",
        "cat:cs.NE AND (spiking OR brain OR neural)",
        "cat:cs.AI AND (brain-inspired OR spiking OR neural network)",
        "all:spiking neural network AND cat:cs.AI",
        "all:brain dynamics AND (neural OR fMRI OR EEG)",
    ]

    all_papers = []
    cutoff = datetime.now() - timedelta(days=days)

    for q in queries:
        print(f"Searching: {q}", flush=True)
        search = arxiv.Search(
            query=q,
            max_results=max_per_query,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        client = arxiv.Client()
        count = 0
        for paper in client.results(search):
            count += 1
            if paper.published.replace(tzinfo=None) >= cutoff:
                all_papers.append(
                    {
                        "id": paper.entry_id.split("/")[-1],
                        "title": paper.title.replace("\n", " "),
                        "authors": [a.name for a in paper.authors[:5]],
                        "abstract": paper.summary.replace("\n", " "),
                        "published": paper.published.date().isoformat(),
                        "categories": list(paper.categories)[:3],
                        "pdf_url": paper.pdf_url,
                        "abs_url": paper.entry_id,
                    }
                )
        print(f"  Found {count} results", flush=True)
        time.sleep(3)

    # Deduplicate and sort
    seen = set()
    unique = []
    for p in all_papers:
        if p["id"] not in seen:
            seen.add(p["id"])
            unique.append(p)

    unique.sort(key=lambda x: x["published"], reverse=True)
    return unique


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    papers = search_neuroscience(days, max_results)
    print(f"\nFound {len(papers)} unique papers from last {days} days\n")

    for i, p in enumerate(papers):
        print(f"=== {i + 1}. {p['title']} ===")
        print(f"ID: {p['id']} | Date: {p['published']}")
        print(f"Authors: {', '.join(p['authors'])}")
        print(f"URL: {p['abs_url']}")
        print(f"Abstract: {p['abstract'][:250]}...\n")

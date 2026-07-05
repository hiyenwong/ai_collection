#!/usr/bin/env python3
"""arXiv search via urllib with proxy and retry — reliable fallback when httpx fails."""

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import os


def search_arxiv_fallback(query, max_results=5, proxy_url=None):
    """
    Search arXiv using urllib (stdlib) — avoids httpx proxy/timeout issues.

    Args:
        query: arXiv search_query string (e.g. 'all:"quantum neural"')
        max_results: number of papers to return
        proxy_url: HTTP proxy URL (e.g. 'http://127.0.0.1:7890')

    Returns:
        list of paper dicts, or empty list on total failure
    """
    if proxy_url is None:
        proxy_url = os.environ.get("HTTP_PROXY", "http://127.0.0.1:7890")

    proxy_handler = urllib.request.ProxyHandler({"http": proxy_url, "https": proxy_url})
    opener = urllib.request.build_opener(proxy_handler)

    base = "https://export.arxiv.org/api/query"
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": max_results,
        }
    )
    url = f"{base}?{params}"

    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }

    for attempt in range(4):
        try:
            time.sleep(max(3, attempt * 5))  # exponential backoff
            resp = opener.open(url, timeout=30)
            data = resp.read().decode("utf-8")

            root = ET.fromstring(data)
            papers = []
            for entry in root.findall("atom:entry", ns):
                aid = entry.find("atom:id", ns).text.split("/")[-1]
                title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
                abstract = (
                    entry.find("atom:summary", ns).text.strip().replace("\n", " ")
                )
                published = entry.find("atom:published", ns).text[:10]
                authors = [
                    a.find("atom:name", ns).text
                    for a in entry.findall("atom:author", ns)
                ]
                cat = entry.find("atom:category", ns)
                category = cat.get("term") if cat is not None else ""
                pdf_url = f"https://arxiv.org/pdf/{aid}"
                for link in entry.findall("atom:link", ns):
                    if link.get("title") == "pdf":
                        pdf_url = link.get("href")

                papers.append(
                    {
                        "id": aid,
                        "title": title,
                        "abstract": abstract,
                        "published": published,
                        "authors": authors,
                        "category": category,
                        "pdf_url": pdf_url,
                        "abs_url": f"https://arxiv.org/abs/{aid}",
                    }
                )
            return papers

        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 * (attempt + 1)
                print(f"  Rate limited (429), waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP error {e.code}: {e.reason}")
                if attempt == 3:
                    return []
        except Exception as e:
            print(f"  Error (attempt {attempt + 1}): {e}")
            if attempt == 3:
                return []

    return []


if __name__ == "__main__":
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else 'all:"quantum neural network"'
    papers = search_arxiv_fallback(q, max_results=3)
    for p in papers:
        print(f"[{p['id']}] {p['title'][:80]}")
        print(f"  {p['abstract'][:200]}...")
        print()

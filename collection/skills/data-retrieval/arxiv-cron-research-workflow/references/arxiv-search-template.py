"""
Template for fetching recent arXiv submissions via the Atom API.
Save this script to /tmp/ and run it with python3.

Behaviour:
- Queries each entry in QUERIES via the arXiv Atom API.
- Routes requests through a configurable HTTP/HTTPS proxy.
- Uses a short per-request timeout to avoid hanging.
- Sleeps between queries to respect arXiv rate limits.
- Deduplicates by arXiv ID and filters entries by PUBLISHED_SINCE_DAYS.
- Writes the result to OUTPUT_PATH as JSON.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import time

# --- Configuration ---
PROXY = "http://127.0.0.1:7890"  # change if your environment uses a different proxy
QUERIES = [
    "cat:q-bio.NC",
    "all:spiking neural network",
    "all:brain network",
]
PUBLISHED_SINCE_DAYS = 2
MAX_RESULTS_PER_QUERY = 10
REQUEST_TIMEOUT = 120
SLEEP_BETWEEN_QUERIES = 10
OUTPUT_PATH = "/tmp/arxiv_neuro_results.json"
USER_AGENT = "Mozilla/5.0"

# --- Setup ---
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({"http": PROXY, "https": PROXY})
)
urllib.request.install_opener(opener)

end_date = datetime.now(timezone.utc)
start_date = end_date - timedelta(days=PUBLISHED_SINCE_DAYS)

ns = {"atom": "http://www.w3.org/2005/Atom"}
all_papers = []
seen_ids = set()

for q in QUERIES:
    try:
        encoded_q = urllib.parse.quote(q)
        url = (
            f"http://export.arxiv.org/api/query?search_query={encoded_q}"
            f"&sortBy=submittedDate&sortOrder=descending"
            f"&start=0&max_results={MAX_RESULTS_PER_QUERY}"
        )
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method="GET")
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            data = resp.read().decode("utf-8")

        root = ET.fromstring(data)
        for entry in root.findall("atom:entry", ns):
            id_el = entry.find("atom:id", ns)
            if id_el is None:
                continue
            arxiv_id = id_el.text.split("/abs/")[-1]
            if arxiv_id in seen_ids:
                continue

            title = (entry.find("atom:title", ns).text or "").replace("\n", " ").strip()
            summary = (entry.find("atom:summary", ns).text or "").replace("\n", " ").strip()
            published = entry.find("atom:published", ns).text
            updated = entry.find("atom:updated", ns).text
            authors = [
                a.find("atom:name", ns).text
                for a in entry.findall("atom:author", ns)
                if a.find("atom:name", ns) is not None
            ]
            categories = [c.get("term") for c in entry.findall("atom:category", ns)]
            link = entry.find("atom:link[@title='pdf']", ns)
            pdf_url = link.get("href") if link is not None else f"https://arxiv.org/pdf/{arxiv_id}.pdf"

            pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
            if pub_dt < start_date:
                continue

            seen_ids.add(arxiv_id)
            all_papers.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "summary": summary,
                "published": published,
                "updated": updated,
                "authors": authors,
                "categories": categories,
                "pdf_url": pdf_url,
                "query": q,
            })

        time.sleep(SLEEP_BETWEEN_QUERIES)
    except Exception as e:
        print(f"Error for query {q}: {e}")

all_papers.sort(key=lambda x: x["published"], reverse=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(all_papers, f, ensure_ascii=False, indent=2)

print(f"Found {len(all_papers)} unique papers in last {PUBLISHED_SINCE_DAYS} days")
for p in all_papers:
    print(f"{p['published'][:10]} | {p['arxiv_id']} | {p['title'][:90]}")

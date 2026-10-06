#!/usr/bin/env python3
"""Fetch latest arXiv papers and output as JSON for processing."""
import json
import urllib.request
import xml.etree.ElementTree as ET

CATEGORIES = ['cs.AI', 'cs.NE', 'cs.LG', 'q-bio.NC', 'cs.MA']
cat_query = '+OR+'.join([f'cat:{c}' for c in CATEGORIES])
url = f'http://export.arxiv.org/api/query?search_query={cat_query}&sortBy=submittedDate&sortOrder=descending&max_results=100'

NS = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

req = urllib.request.Request(url, headers={'User-Agent': 'HermesAgent/1.0'})
with urllib.request.urlopen(req, timeout=60) as resp:
    data = resp.read().decode('utf-8')

root = ET.fromstring(data)
entries = root.findall('atom:entry', NS)

papers = []
for entry in entries:
    arxiv_id = entry.find('atom:id', NS).text.strip().split('/abs/')[-1]
    title = ' '.join(entry.find('atom:title', NS).text.strip().split())
    summary = ' '.join(entry.find('atom:summary', NS).text.strip().split())
    published = entry.find('atom:published', NS).text.strip()[:10]
    authors = [a.find('atom:name', NS).text for a in entry.findall('atom:author', NS)]
    cats = [c.get('term') for c in entry.findall('atom:category', NS)]
    
    papers.append({
        'id': arxiv_id,
        'title': title,
        'authors': ', '.join(authors[:5]) + ('...' if len(authors) > 5 else ''),
        'summary': summary[:2000],
        'published': published,
        'categories': cats,
        'url': f'https://arxiv.org/abs/{arxiv_id}'
    })

print(json.dumps(papers, indent=2))
print(f"\n--- Total papers fetched: {len(papers)} ---")

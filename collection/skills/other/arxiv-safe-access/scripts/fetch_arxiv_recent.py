#!/usr/bin/env python3
"""
Example script to fetch recent arXiv papers from an RSS feed and filter by keywords.
This demonstrates a reliable method for accessing arXiv data without common pitfalls.
"""
import xml.etree.ElementTree as ET
import urllib.request
import re
from datetime import datetime, timedelta

def fetch_arxiv_rss(category):
    """Fetch the RSS feed for a given arXiv category."""
    url = f"https://rss.arxiv.org/rss/{category}"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read()
    except Exception as e:
        print(f"Error fetching RSS feed for {category}: {e}")
        return None

def parse_rss_content(xml_data):
    """Parse RSS XML and return a list of papers."""
    if not xml_data:
        return []
    
    root = ET.fromstring(xml_data)
    # RSS 2.0 namespace
    ns = {'': 'http://purl.org/rss/1.0/'}
    
    papers = []
    for item in root.findall('.//item'):
        title_elem = item.find('title')
        link_elem = item.find('link')
        desc_elem = item.find('description')
        pubdate_elem = item.find('pubDate')
        
        if title_elem is not None and link_elem is not None:
            title = title_elem.text.strip()
            link = link_elem.text.strip()
            description = desc_elem.text.strip() if desc_elem is not None else ''
            pubdate = pubdate_elem.text.strip() if pubdate_elem is not None else ''
            
            # Extract arXiv ID
            match = re.search(r'abs/(\d+\.\d+)', link)
            arxiv_id = match.group(1) if match else link.split('/')[-1]
            
            papers.append({
                'id': arxiv_id,
                'title': title,
                'link': link,
                'description': description,
                'pubDate': pubdate
            })
    return papers

def filter_by_keywords(papers, keywords):
    """Filter papers by keywords in title or description."""
    if not keywords:
        return papers
    
    filtered = []
    for paper in papers:
        text = (paper['title'] + ' ' + paper['description']).lower()
        if any(keyword.lower() in text for keyword in keywords):
            filtered.append(paper)
    return filtered

def main():
    # Example: Get recent papers from cs.Neural and Evolutionary Computation (q-bio.NC)
    categories = ['cs.NE', 'q-bio.NC']
    keywords = ['neuroscience', 'brain network', 'neural dynamics', 'spiking neural network', 
                'computational neuroscience', 'cellular automata']
    
    all_papers = []
    for category in categories:
        print(f"Fetching {category}...")
        xml_data = fetch_arxiv_rss(category)
        papers = parse_rss_content(xml_data)
        print(f"  Found {len(papers)} papers")
        all_papers.extend(papers)
    
    # Filter by keywords
    filtered_papers = filter_by_keywords(all_papers, keywords)
    print(f"\nFound {len(filtered_papers)} papers matching keywords: {', '.join(keywords)}")
    
    # Sort by date (newest first) - simple string sort works for RFC 822 dates
    filtered_papers.sort(key=lambda x: x['pubDate'], reverse=True)
    
    # Print results
    for paper in filtered_papers[:10]:  # Show top 10
        print(f"\n{paper['id']}: {paper['title']}")
        print(f"  Published: {paper['pubDate']}")
        print(f"  Link: {paper['link']}")

if __name__ == "__main__":
    main()
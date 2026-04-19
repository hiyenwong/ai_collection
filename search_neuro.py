import urllib.request
import xml.etree.ElementTree as ET
import json

# More targeted neuroscience queries
queries = [
    "all:spiking+AND+all:neural+AND+all:network",
    "all:brain+AND+all:connectivity+AND+all:graph",
    "all:neural+dynamics+AND+all:attractor",
    "all:neuroscience+AND+all:deep+learning",
    "all:working+memory+AND+all:spiking",
    "all:fmri+AND+all:decoding",
    "all:eeg+AND+all:transformer",
]

all_papers = []

for query in queries:
    url = f'http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=10'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        xml_data = response.read().decode('utf-8')
    
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
    
    for entry in root.findall('atom:entry', ns):
        paper_id = entry.find('atom:id', ns).text
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        published = entry.find('atom:published', ns).text[:10]
        
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        categories = [c.get('term') for c in entry.findall('atom:category', ns)]
        
        # Filter for neuroscience relevance
        lower_title = title.lower()
        relevant_keywords = ['neural', 'brain', 'spiking', 'neuro', 'cognitive', 
                           'cortex', 'synapse', 'neuron', 'fmri', 'eeg', 'mec',
                           'hippocamp', 'memory', 'dynamics', 'connectivity',
                           'network', 'plasticity', 'receptive', 'computation']
        
        if any(kw in lower_title for kw in relevant_keywords):
            all_papers.append({
                'id': paper_id.split('/')[-1],
                'title': title,
                'summary': summary[:800],
                'published': published,
                'authors': authors[:4],
                'categories': categories,
                'score': sum(1 for kw in relevant_keywords if kw in lower_title)
            })

seen = set()
unique_papers = []
for p in all_papers:
    if p['id'] not in seen:
        seen.add(p['id'])
        unique_papers.append(p)

unique_papers.sort(key=lambda x: (x['published'], x['score']), reverse=True)

print(f"Found {len(unique_papers)} neuroscience-relevant papers")
for i, p in enumerate(unique_papers[:20]):
    print(f"\n{'='*80}")
    print(f"Paper {i+1} | ID: {p['id']} | Date: {p['published']} | Score: {p['score']}")
    print(f"Categories: {', '.join(p['categories'])}")
    print(f"Title: {p['title']}")
    print(f"Authors: {', '.join(p['authors'])}")
    print(f"\nSummary: {p['summary'][:500]}...")

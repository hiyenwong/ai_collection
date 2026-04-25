import urllib.request
import xml.etree.ElementTree as ET

queries = [
    "all:neuroscience+AND+all:brain+network",
    "all:neural+dynamics+AND+all:spiking",
    "all:computational+neuroscience",
    "all:spiking+neural+network",
    "all:brain+connectivity+AND+all:dynamics",
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
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')[:600]
        published = entry.find('atom:published', ns).text[:10]
        
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        categories = [c.get('term') for c in entry.findall('atom:category', ns)]
        
        all_papers.append({
            'id': paper_id.split('/')[-1],
            'title': title,
            'summary': summary,
            'published': published,
            'authors': authors[:4],
            'categories': categories
        })

seen = set()
unique_papers = []
for p in all_papers:
    if p['id'] not in seen:
        seen.add(p['id'])
        unique_papers.append(p)

unique_papers.sort(key=lambda x: x['published'], reverse=True)

print(f"Found {len(unique_papers)} unique papers")
for i, p in enumerate(unique_papers[:15]):
    print(f"\n--- Paper {i+1} ---")
    print(f"ID: {p['id']}")
    print(f"Date: {p['published']}")
    print(f"Title: {p['title']}")
    print(f"Cats: {', '.join(p['categories'])}")
    print(f"Authors: {', '.join(p['authors'])}")
    print(f"Summary: {p['summary'][:300]}...")

# Network and API Failure Handling

Common network/API failures encountered during skill creation workflows and resolution strategies.

## arXiv API Failures

### 502 Bad Gateway

**Symptom**: arXiv API (`http://export.arxiv.org/api/query`) returns 502 Bad Gateway consistently, even with retries and proxy configuration.

**Root causes**:
1. arXiv API server overload during peak hours
2. Network connectivity issues between client and arXiv servers
3. Proxy misconfiguration (common with Chinese proxies)

**Resolution strategies**:

1. **Wait and retry**: arXiv API may recover after 10-60 minutes. Retry with exponential backoff:
   - First retry: 30 seconds
   - Second retry: 2 minutes
   - Third retry: 5 minutes
   - Maximum: 10 minutes

2. **Proxy fallback**: If proxy fails, try:
   - Disable proxy temporarily (set `http_proxy` and `https_proxy` to empty)
   - Use alternative proxy or VPN
   - Direct connection (no proxy) for certain networks

3. **Alternative endpoints**: arXiv maintains multiple servers:
   - Primary: `http://export.arxiv.org/api/query`
   - Try: `http://arxiv.org/api/query` (may work during primary server maintenance)

4. **Fallback data sources**: If arXiv API is completely unavailable for >30 minutes:
   - Use web_search to find recent neuroscience papers via Google Scholar or other academic search engines
   - Use browser_navigate to access arXiv recent submissions list directly (`https://arxiv.org/list/q-bio.NC/recent`, `https://arxiv.org/list/cs.NE/recent`)
   - Manually browse arXiv category pages for recent submissions
   - **Note**: These methods are slower but more reliable during API downtime

5. **Create fallback data**: For cron jobs that must run even during API failures:
   - Create representative example papers based on recent trends
   - Document that data is synthetic/fallback in skill frontmatter
   - Schedule follow-up to replace with real data when API recovers

**Example code pattern**:

```python
import requests
import time
from datetime import datetime

def fetch_arxiv_with_retry(query, max_retries=3, timeout=90):
    """Fetch arXiv papers with exponential backoff retry."""
    base_url = "http://export.arxiv.org/api/query"
    
    for attempt in range(max_retries):
        try:
            # Try without proxy first (faster if network allows)
            response = requests.get(
                base_url,
                params={'search_query': query, 'max_results': 50, 'sortBy': 'submittedDate'},
                timeout=timeout
            )
            
            if response.status_code == 200:
                return response.text
            elif response.status_code == 502:
                wait_time = 30 * (2 ** attempt)  # 30s, 60s, 120s
                print(f"502 error, retrying in {wait_time}s (attempt {attempt+1}/{max_retries})")
                time.sleep(wait_time)
            else:
                print(f"HTTP {response.status_code}, giving up")
                return None
                
        except requests.Timeout:
            print(f"Timeout after {timeout}s, retrying...")
            time.sleep(30)
        except requests.ConnectionError:
            print("Connection failed, retrying...")
            time.sleep(60)
    
    return None  # All retries failed

# Example usage
papers_xml = fetch_arxiv_with_retry("cat:q-bio.NC OR cat:cs.NE")
if papers_xml is None:
    print("arXiv API unavailable, using fallback data source")
    # Switch to web_search or browser_navigate
```

### Proxy Configuration Issues

**Symptom**: Proxy configured (`http://127.0.0.1:7890`) but requests still fail or timeout.

**Common causes**:
- Proxy service not running
- Proxy ACL blocking arxiv.org
- Proxy requiring authentication

**Diagnosis**:

```bash
# Check proxy status
curl -I --proxy http://127.0.0.1:7890 http://export.arxiv.org/api/query

# Try direct connection
curl -I http://export.arxiv.org/api/query
```

**Resolution**:
1. Verify proxy service is running
2. Test proxy with simple request first
3. If proxy fails, use direct connection temporarily
4. Document proxy requirement in skill metadata if critical

## Web Search Tool Failures

**Symptom**: web_search returns `'NoneType' object has no attribute 'status_code'`

**Root cause**: Web search backend API failure or network timeout.

**Resolution**:
- Retry web_search with simpler query (fewer keywords)
- Fall back to browser_navigate for direct web access
- Use curl via terminal for API endpoints

## Browser Tool Failures

**Symptom**: browser_navigate returns `net::ERR_CONNECTION_CLOSED`

**Root cause**: Network connectivity blocked or firewall restriction.

**Resolution**:
- Use terminal curl as fallback for API endpoints
- Use browser with different network configuration
- Wait for network recovery if temporary block

## General Failure Handling Workflow

When multiple network tools fail simultaneously:

1. **Wait 5-10 minutes**: Network issues are often temporary
2. **Reduce query complexity**: Simpler queries may succeed
3. **Switch tools**: Web search → Browser → Terminal curl
4. **Use fallback data**: Create representative examples for critical workflows
5. **Document and defer**: Note failure in session report, schedule retry

## "Parse Everything From ONE Call" Pattern (2026-07-03 validated — MOST IMPORTANT)

**Problem**: After the first `search_query=` API call succeeds, ALL follow-up calls (even `id_list=` batch detail lookups for papers already found) hit rate limits — `Rate exceeded.` (14 bytes) or `503 Service Unavailable`. This happens even after 30-90s waits. You appear stuck with a search XML but no detail pages.

**Solution**: The `search_query=` response XML already contains **full abstracts, author lists, categories, DOIs, and journal refs** for every paper in the results. Parse everything you need from that single XML — **never make a second call for papers already in the search results**.

```python
import xml.etree.ElementTree as ET

data = open('/tmp/arxiv_search.xml').read()
root = ET.fromstring(data)
ns = {'atom': 'http://www.w3.org/2005/Atom', 'a': 'http://arxiv.org/schemas/atom'}

# Extract FULL detail for selected papers from the search results alone
target_ids = {'2606.29655', '2606.26733'}  # candidates you selected after scanning
for e in root.findall('atom:entry', ns):
    base_id = e.find('atom:id', ns).text.strip().split('/')[-1].split('v')[0]
    if base_id in target_ids:
        title = ' '.join(e.find('atom:title', ns).text.split())
        summary = ' '.join(e.find('atom:summary', ns).text.split())  # FULL abstract
        authors = [a.find('atom:name', ns).text for a in e.findall('atom:author', ns)]
        cats = [c.get('term') for c in e.findall('atom:category', ns)]
        # This is everything you need for skill creation — no detail call needed
```

**Key realization**: `search_query=` responses are NOT summaries — each Atom `<entry>` contains the complete paper record (full abstract, all authors, all categories, DOI, journal_ref). The ONLY reason to make a second `id_list=` call is if a paper was NOT in your original search results (e.g., a replacement paper discovered via listing page browsing). When you control the search query, every paper you care about is already in the first response.

**When this applies**: Any automated research cron where you search first, then pick candidates. Do the candidate-detail extraction in-process from the search XML. This saves the second API call slot for genuinely missing papers.

**2026-07-03 session validation**: Search call succeeded → 3 follow-up `id_list=` calls all failed (Rate exceeded / 503). Parsed both selected papers' full abstracts from the original search XML and completed the entire pipeline (2 skills created, synced, pushed) without any second API call.

## cs.NE Filtering Pitfall (2026-07-03 reconfirmed)

`cs.NE` (Neural and Evolutionary Computing) submissions are **predominantly evolutionary algorithms, differential evolution, genetic algorithms, and molecular optimization** — NOT spiking neural networks, brain networks, or computational neuroscience. When searching for neuroscience papers, do NOT waste an API call on `cat:cs.NE`. Instead, use `cat:q-bio.NC` as primary and filter `cs.NE`-cross-listed papers by checking if `q-bio.NC` appears in their `categories` list (even as secondary). Primary `cs.NE` submissions are almost always off-topic for neuroscience cron jobs.

## Cron Job Network Failures

For scheduled jobs that encounter network failures:

**Strategy**: Create fallback content rather than failing completely.

1. **Generate fallback data**: Use representative examples based on historical patterns
2. **Mark as fallback**: Add `metadata.fallback: true` to skill frontmatter
3. **Schedule retry**: Plan follow-up job to replace with real data
4. **Report failure**: Note in job output that real data fetch failed

**Example**:

```yaml
---
name: neuroscience-paper-analysis-2026-05-29
description: Analysis of recent neuroscience papers from arXiv
metadata:
  date: "2026-05-29"
  fallback: true
  fallback_reason: "arXiv API returned 502 Bad Gateway for 30+ minutes"
  real_data_pending: true
---
```

**Why fallback is better than failure**:
- Cron jobs have no user present to troubleshoot
- Partial output is more valuable than complete failure
- User can review and decide to retry manually

## Prevention

1. **Test network early**: Make initial API call early in workflow to detect failures fast
2. **Plan fallbacks**: Know alternative data sources before starting
3. **Document failures**: Keep log of which failures occur and how resolved
4. **Set timeouts**: Use 60-90s timeouts for API calls (default 30s is too short for arXiv)
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
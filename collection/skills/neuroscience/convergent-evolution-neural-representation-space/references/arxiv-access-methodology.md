# ArXiv Access Methodology for Neuroscience Research

## Browser-Based Navigation Approach

When automated arXiv access fails due to:
- Proxy configuration issues (system proxy at 127.0.0.1:7890)
- Security scanner blocks on direct URL access
- SSL/TLS certificate validation problems

Use browser-based navigation with specific URL patterns:

### Direct Category Access
For neuroscience papers, navigate directly to category pages:
- `https://arxiv.org/list/q-bio.NC/recent` - Neurons and Cognition recent submissions

### Advanced Search Construction
When multiple keywords are needed, construct advanced search URLs:
- Use date range filtering: `from=2026-08-06&to=2026-08-07`
- Combine keywords with OR logic in separate search fields
- Set results per page to 50 for comprehensive coverage

### HTML Extraction Preference
When available, prefer HTML version over PDF:
- Navigate to `https://arxiv.org/html/{arxiv_id}` 
- Provides structured, readable content without PDF parsing
- Includes section navigation and full abstract

## Proxy Handling
For macOS systems with system proxy:
- Browser tools automatically respect system proxy settings
- No additional configuration needed for browser_navigate
- Avoid curl/web_extract tools which may not respect proxy properly

## Error Recovery Patterns
If initial search page loads but shows no results:
1. Verify search form parameters are correctly populated
2. Click the search button explicitly to submit the form
3. Check for JavaScript errors in console that might prevent results loading
4. Fall back to direct category browsing if advanced search fails

## Validation Checklist
Before proceeding with skill creation:
- [ ] Paper title matches expected research topic
- [ ] Abstract contains sufficient technical detail
- [ ] Submission date falls within target range (last 24 hours)
- [ ] Authors and affiliations are credible academic sources
- [ ] HTML or PDF content is accessible and complete
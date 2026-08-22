# ArXiv Research Automation Lessons - July 2026

## Key Workflow Insights

### Browser vs API Access in Cron Jobs
- **Primary Method**: Use `browser_navigate` for arXiv paper discovery in automated/cron contexts
- **API Limitation**: arXiv API rate-limits immediately when called from automated scripts, even with proper proxy settings and delays
- **Reliability**: Browser scraping proved more reliable than direct API calls for recent paper discovery

### Skill Name Ambiguity Problem  
- **Issue**: Common skill names like "arxiv-search" can have multiple local matches across different directories:
  - `~/.hermes/skills/arxiv-search/`
  - `~/.hermes/skills/ai_collection/arxiv-search/`  
  - `~/.hermes/skills/openclaw-imports/arxiv-search/`
- **Impact**: Causes `skill_view()` failures with "ambiguous skill name" errors in automated workflows
- **Solution**: In automated contexts, prefer direct tool usage (browser/API) over ambiguous skill invocations

### Proxy Configuration for External Requests
- **Required**: Set both `HTTP_PROXY` and `HTTPS_PROXY` environment variables for outbound requests
- **Format**: `export HTTP_PROXY=http://127.0.0.1:7890 && export HTTPS_PROXY=http://127.0.0.1:7890`
- **Context**: Essential for environments requiring proxy access to external resources

### Execute Code Restrictions in Cron
- **Limitation**: `execute_code` tool is blocked in unattended cron jobs due to security policy
- **Workaround**: Use standard tools (`web_search`, `browser_navigate`, `terminal`) instead of custom Python scripts
- **Implication**: Requires more verbose multi-step approaches but ensures cron job reliability

## Verification Steps for Automated Research

1. **Test arXiv access method** - verify browser_navigate works before relying on API
2. **Check skill name uniqueness** - use `skills_list` to verify no ambiguous matches exist  
3. **Validate proxy configuration** - ensure external requests can reach target servers
4. **Confirm cron permissions** - avoid execute_code and other restricted operations
5. **Verify kg.db schema** - check table structure before attempting insertions

## Error Recovery Patterns

- **API Rate Limiting**: Immediately fall back to browser-based scraping
- **Skill Ambiguity**: Use fully qualified paths or direct tool methods instead of skill_view
- **Proxy Failures**: Verify both HTTP_PROXY and HTTPS_PROXY are set correctly
- **Cron Restrictions**: Replace execute_code with standard tool sequences

This reference captures hard-won lessons from automated neuroscience research pipeline development in July 2026.
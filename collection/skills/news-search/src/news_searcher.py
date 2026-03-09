#!/usr/bin/env python3
"""
News Search - Multi-source news search and retrieval.

Usage:
    from news_searcher import NewsSearcher
    
    searcher = NewsSearcher()
    results = searcher.search("人工智能", lang="zh", days=7)
"""

import json
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Any
from urllib.parse import quote_plus

try:
    import feedparser
except ImportError:
    print("Please install feedparser: pip install feedparser")
    raise

try:
    import requests
except ImportError:
    print("Please install requests: pip install requests")
    raise


# ============================================================================
# Data Models
# ============================================================================

@dataclass
class NewsArticle:
    """Represents a news article."""
    title: str
    link: str
    summary: str = ""
    source: str = ""
    published: Optional[datetime] = None
    author: str = ""
    image_url: str = ""
    category: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "link": self.link,
            "summary": self.summary,
            "source": self.source,
            "published": self.published.isoformat() if self.published else None,
            "author": self.author,
            "image_url": self.image_url,
            "category": self.category,
        }


@dataclass
class SearchResult:
    """Search result container."""
    query: str
    articles: List[NewsArticle]
    total: int
    source: str
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "total": self.total,
            "source": self.source,
            "timestamp": self.timestamp.isoformat(),
            "articles": [a.to_dict() for a in self.articles],
        }


# ============================================================================
# Cache
# ============================================================================

class NewsCache:
    """Simple file-based cache for news results."""
    
    def __init__(self, cache_dir: Optional[Path] = None, ttl_seconds: int = 3600):
        self.cache_dir = cache_dir or Path.home() / ".openclaw" / "cache" / "news"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_seconds
    
    def _get_cache_key(self, query: str, **kwargs) -> str:
        key_data = f"{query}:{json.dumps(kwargs, sort_keys=True)}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def get(self, query: str, **kwargs) -> Optional[SearchResult]:
        key = self._get_cache_key(query, **kwargs)
        cache_file = self.cache_dir / f"{key}.json"
        
        if not cache_file.exists():
            return None
            
        try:
            data = json.loads(cache_file.read_text())
            timestamp = datetime.fromisoformat(data["timestamp"])
            
            if datetime.now() - timestamp > timedelta(seconds=self.ttl_seconds):
                cache_file.unlink()
                return None
                
            articles = [NewsArticle(**a) for a in data["articles"]]
            return SearchResult(
                query=data["query"],
                articles=articles,
                total=data["total"],
                source=data["source"],
                timestamp=timestamp,
            )
        except (json.JSONDecodeError, KeyError):
            return None
    
    def set(self, result: SearchResult, **kwargs):
        key = self._get_cache_key(result.query, **kwargs)
        cache_file = self.cache_dir / f"{key}.json"
        cache_file.write_text(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))


# ============================================================================
# News Sources
# ============================================================================

class NewsSource:
    """Base class for news sources."""
    name: str = "base"
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20) -> SearchResult:
        raise NotImplementedError
    
    def get_headlines(self, category: str = "general", country: str = "cn") -> SearchResult:
        raise NotImplementedError


class GoogleNewsRSS(NewsSource):
    """Google News RSS feed source (free, no API key required)."""
    
    name = "google_news_rss"
    BASE_URL = "https://news.google.com/rss"
    
    CATEGORIES = {
        "general": "",
        "world": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YzY5U0FtVnliZ0pWVXlnQVAB",
        "tech": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnliZ0pWVXlnQVAB",
        "business": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGxqTjBjd0FtVnliZ0pWVXlnQVAB",
        "science": "CAAqJggKIiBDQkFTRWdvSUwyMHZNWFp0WldWU0FtVnliZ0pWVXlnQVAB",
        "health": "CAAqJggKIiBDQkFTRWdvSUwyMHZNR3hvYjNjd0FtVnliZ0pWVXlnQVAB",
        "sports": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnliZ0pWVXlnQVAB",
        "entertainment": "CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnliZ0pWVXlnQVAB",
    }
    
    def _parse_entry(self, entry) -> NewsArticle:
        """Parse a feed entry into NewsArticle."""
        published = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published = datetime(*entry.published_parsed[:6])
        
        title = entry.get("title", "")
        if " - " in title:
            title = title.rsplit(" - ", 1)[0]
        
        source = ""
        if hasattr(entry, "source") and hasattr(entry.source, "title"):
            source = entry.source.title
        elif " - " in entry.get("title", ""):
            source = entry.title.rsplit(" - ", 1)[-1]
        
        return NewsArticle(
            title=title,
            link=entry.get("link", ""),
            summary=entry.get("summary", ""),
            source=source,
            published=published,
        )
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20) -> SearchResult:
        """Search news by keyword."""
        hl = "zh-CN" if lang == "zh" else "en-US"
        gl = "CN" if lang == "zh" else "US"
        url = f"{self.BASE_URL}/search?q={quote_plus(query)}&hl={hl}&gl={gl}&ceid={gl}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            articles = []
            cutoff_date = datetime.now() - timedelta(days=days)
            
            for entry in feed.entries[:limit * 2]:
                article = self._parse_entry(entry)
                if article.published and article.published < cutoff_date:
                    continue
                articles.append(article)
                if len(articles) >= limit:
                    break
            
            return SearchResult(query=query, articles=articles, total=len(articles), source=self.name)
        except Exception as e:
            print(f"Error searching Google News: {e}")
            return SearchResult(query=query, articles=[], total=0, source=self.name)
    
    def get_headlines(self, category: str = "general", country: str = "cn") -> SearchResult:
        """Get headlines by category."""
        hl = "zh-CN" if country == "cn" else "en-US"
        gl = country.upper()
        topic_id = self.CATEGORIES.get(category, "")
        
        if topic_id:
            url = f"{self.BASE_URL}/topics/{topic_id}?hl={hl}&gl={gl}&ceid={gl}"
        else:
            url = f"{self.BASE_URL}?hl={hl}&gl={gl}&ceid={gl}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            articles = [self._parse_entry(entry) for entry in feed.entries[:20]]
            return SearchResult(query=category, articles=articles, total=len(articles), source=self.name)
        except Exception as e:
            print(f"Error getting headlines: {e}")
            return SearchResult(query=category, articles=[], total=0, source=self.name)


class SinaNewsRSS(NewsSource):
    """Sina News RSS feed (Chinese news)."""
    
    name = "sina_news"
    FEEDS = {
        "general": "https://news.sina.com.cn/724-1-1.xml",
        "tech": "https://tech.sina.com.cn/724-1-1.xml",
        "finance": "https://finance.sina.com.cn/724-1-1.xml",
        "sports": "https://sports.sina.com.cn/724-1-1.xml",
        "entertainment": "https://ent.sina.com.cn/724-1-1.xml",
    }
    
    def _parse_entry(self, entry) -> NewsArticle:
        published = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published = datetime(*entry.published_parsed[:6])
        
        return NewsArticle(
            title=entry.get("title", ""),
            link=entry.get("link", ""),
            summary=entry.get("summary", ""),
            source="新浪新闻",
            published=published,
            category=entry.get("tags", [{}])[0].get("term", "") if entry.get("tags") else "",
        )
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20) -> SearchResult:
        result = self.get_headlines(category="general")
        result.query = query
        filtered = [a for a in result.articles if query.lower() in a.title.lower()]
        result.articles = filtered[:limit]
        result.total = len(result.articles)
        return result
    
    def get_headlines(self, category: str = "general", country: str = "cn") -> SearchResult:
        url = self.FEEDS.get(category, self.FEEDS["general"])
        
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            articles = [self._parse_entry(entry) for entry in feed.entries[:20]]
            return SearchResult(query=category, articles=articles, total=len(articles), source=self.name)
        except Exception as e:
            print(f"Error getting Sina news: {e}")
            return SearchResult(query=category, articles=[], total=0, source=self.name)


class NewsAPISource(NewsSource):
    """NewsAPI source (requires API key)."""
    
    name = "newsapi"
    BASE_URL = "https://newsapi.org/v2"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        if not self.api_key:
            config_path = Path.home() / ".openclaw" / "keys" / "news-search.json"
            if config_path.exists():
                try:
                    config = json.loads(config_path.read_text())
                    self.api_key = config.get("newsapi")
                except:
                    pass
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20) -> SearchResult:
        if not self.api_key:
            return SearchResult(query=query, articles=[], total=0, source=self.name)
        
        from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        params = {
            "q": query,
            "from": from_date,
            "language": "zh" if lang == "zh" else "en",
            "pageSize": limit,
            "apiKey": self.api_key,
        }
        
        try:
            response = requests.get(f"{self.BASE_URL}/everything", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = []
            
            for item in data.get("articles", []):
                published = None
                if item.get("publishedAt"):
                    published = datetime.fromisoformat(item["publishedAt"].replace("Z", "+00:00"))
                
                articles.append(NewsArticle(
                    title=item.get("title", ""),
                    link=item.get("url", ""),
                    summary=item.get("description", "") or "",
                    source=item.get("source", {}).get("name", ""),
                    published=published,
                    author=item.get("author", "") or "",
                    image_url=item.get("urlToImage", "") or "",
                ))
            
            return SearchResult(query=query, articles=articles, total=data.get("totalResults", 0), source=self.name)
        except Exception as e:
            print(f"Error searching NewsAPI: {e}")
            return SearchResult(query=query, articles=[], total=0, source=self.name)
    
    def get_headlines(self, category: str = "general", country: str = "cn") -> SearchResult:
        if not self.api_key:
            return SearchResult(query=category, articles=[], total=0, source=self.name)
        
        params = {"category": category, "country": country, "pageSize": 20, "apiKey": self.api_key}
        
        try:
            response = requests.get(f"{self.BASE_URL}/top-headlines", params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = []
            
            for item in data.get("articles", []):
                published = None
                if item.get("publishedAt"):
                    published = datetime.fromisoformat(item["publishedAt"].replace("Z", "+00:00"))
                
                articles.append(NewsArticle(
                    title=item.get("title", ""),
                    link=item.get("url", ""),
                    summary=item.get("description", "") or "",
                    source=item.get("source", {}).get("name", ""),
                    published=published,
                    author=item.get("author", "") or "",
                    image_url=item.get("urlToImage", "") or "",
                    category=category,
                ))
            
            return SearchResult(query=category, articles=articles, total=data.get("totalResults", 0), source=self.name)
        except Exception as e:
            print(f"Error getting NewsAPI headlines: {e}")
            return SearchResult(query=category, articles=[], total=0, source=self.name)


# ============================================================================
# Main Searcher
# ============================================================================

class NewsSearcher:
    """
    Multi-source news searcher.
    
    Usage:
        searcher = NewsSearcher()
        results = searcher.search("人工智能", lang="zh", days=7)
        for article in results.articles:
            print(f"[{article.source}] {article.title}")
    """
    
    def __init__(self, use_cache: bool = True, cache_ttl: int = 3600, sources: Optional[List[str]] = None):
        self.cache = NewsCache(ttl_seconds=cache_ttl) if use_cache else None
        self.sources: Dict[str, NewsSource] = {}
        
        default_sources = sources or ["google_news_rss", "sina_news"]
        
        if "google_news_rss" in default_sources:
            self.sources["google_news_rss"] = GoogleNewsRSS()
        if "sina_news" in default_sources:
            self.sources["sina_news"] = SinaNewsRSS()
        if "newsapi" in default_sources:
            newsapi = NewsAPISource()
            if newsapi.api_key:
                self.sources["newsapi"] = newsapi
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20, source: Optional[str] = None) -> SearchResult:
        """Search news across all sources."""
        if self.cache:
            cached = self.cache.get(query, lang=lang, days=days, limit=limit, source=source)
            if cached:
                return cached
        
        sources_to_use = {source: self.sources.get(source)} if source and source in self.sources else self.sources
        all_articles = []
        
        for src_name, src in sources_to_use.items():
            try:
                result = src.search(query, lang=lang, days=days, limit=limit)
                all_articles.extend(result.articles)
            except Exception as e:
                print(f"Error from {src_name}: {e}")
        
        seen_urls = set()
        unique_articles = []
        for article in all_articles:
            if article.link not in seen_urls:
                seen_urls.add(article.link)
                unique_articles.append(article)
        
        unique_articles.sort(key=lambda a: a.published or datetime.min, reverse=True)
        result = SearchResult(query=query, articles=unique_articles[:limit], total=len(unique_articles), source="aggregated")
        
        if self.cache:
            self.cache.set(result, lang=lang, days=days, limit=limit, source=source)
        
        return result
    
    def get_headlines(self, category: str = "general", country: str = "cn", source: Optional[str] = None) -> SearchResult:
        """Get top headlines."""
        sources_to_use = {source: self.sources.get(source)} if source and source in self.sources else self.sources
        all_articles = []
        
        for src_name, src in sources_to_use.items():
            try:
                result = src.get_headlines(category=category, country=country)
                all_articles.extend(result.articles)
            except Exception as e:
                print(f"Error from {src_name}: {e}")
        
        seen_urls = set()
        unique_articles = []
        for article in all_articles:
            if article.link not in seen_urls:
                seen_urls.add(article.link)
                unique_articles.append(article)
        
        return SearchResult(query=category, articles=unique_articles[:20], total=len(unique_articles), source="aggregated")
    
    def list_sources(self) -> List[str]:
        """List available news sources."""
        return list(self.sources.keys())


# ============================================================================
# CLI
# ============================================================================

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="News Search Tool")
    parser.add_argument("command", choices=["search", "headlines", "sources"], help="Command")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--category", "-c", default="general", help="Category")
    parser.add_argument("--lang", "-l", default="zh", help="Language (zh/en)")
    parser.add_argument("--days", "-d", type=int, default=7, help="Days to search")
    parser.add_argument("--limit", "-n", type=int, default=10, help="Result limit")
    parser.add_argument("--source", "-s", help="Specific source")
    parser.add_argument("--json", "-j", action="store_true", help="JSON output")
    
    args = parser.parse_args()
    searcher = NewsSearcher()
    
    if args.command == "sources":
        print("Available sources:")
        for src in searcher.list_sources():
            print(f"  - {src}")
        return
    
    if args.command == "search":
        if not args.query:
            print("Error: --query required for search")
            return
        result = searcher.search(args.query, lang=args.lang, days=args.days, limit=args.limit, source=args.source)
    elif args.command == "headlines":
        result = searcher.get_headlines(category=args.category, country="cn" if args.lang == "zh" else "us", source=args.source)
    
    if args.json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(f"\n查询: {result.query}")
        print(f"来源: {result.source}")
        print(f"结果数: {result.total}\n")
        
        for i, article in enumerate(result.articles, 1):
            print(f"{i}. [{article.source}] {article.title}")
            print(f"   {article.link}")
            if article.published:
                print(f"   {article.published.strftime('%Y-%m-%d %H:%M')}")
            print()


if __name__ == "__main__":
    main()

class TencentNewsRSS(NewsSource):
    """Tencent News RSS feed (腾讯新闻)."""
    
    name = "tencent_news"
    FEEDS = {
        "general": "https://news.qq.com/a/index_rss.xml",
        "world": "https://news.qq.com/a/index_rss.xml",  # 国际新闻混在主页
        "military": "https://news.qq.com/a/index_rss.xml",  # 军事新闻
    }
    
    def _parse_entry(self, entry) -> NewsArticle:
        published = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            published = datetime(*entry.published_parsed[:6])
        
        return NewsArticle(
            title=entry.get("title", ""),
            link=entry.get("link", ""),
            summary=entry.get("summary", ""),
            source="腾讯新闻",
            published=published,
        )
    
    def search(self, query: str, lang: str = "zh", days: int = 7, limit: int = 20) -> SearchResult:
        # 腾讯新闻不支持搜索，获取主页并过滤
        result = self.get_headlines(category="general")
        result.query = query
        
        # 关键词过滤
        filtered = [a for a in result.articles if query.lower() in a.title.lower()]
        result.articles = filtered[:limit]
        result.total = len(result.articles)
        
        return result
    
    def get_headlines(self, category: str = "general", country: str = "cn") -> SearchResult:
        url = self.FEEDS.get(category, self.FEEDS["general"])
        
        try:
            response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            articles = [self._parse_entry(entry) for entry in feed.entries[:30]]
            return SearchResult(query=category, articles=articles, total=len(articles), source=self.name)
        except Exception as e:
            print(f"Error getting Tencent news: {e}")
            return SearchResult(query=category, articles=[], total=0, source=self.name)

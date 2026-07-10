# News Search Skill

新闻搜索与获取技能，支持多个免费数据源。

## 快速开始

### 安装依赖

```bash
pip install feedparser httpx beautifulsoup4
```

### 命令行使用

```bash
# 搜索新闻
python news-search search -q "人工智能" -l zh -d 7

# 获取头条
python news-search headlines -c tech -l zh

# 列出数据源
python news-search sources

# JSON 输出
python news-search search -q "苹果公司" --json
```

### Python API

```python
from news_searcher import NewsSearcher

searcher = NewsSearcher()

# 搜索新闻
results = searcher.search("人工智能", lang="zh", days=7, limit=10)

for article in results.articles:
    print(f"[{article.source}] {article.title}")
    print(f"  {article.link}")
    print(f"  {article.published}")
```

## 支持的数据源

| 数据源 | 类型 | 需要配置 | 说明 |
|--------|------|----------|------|
| Google News RSS | 免费 | 否 | 默认启用，支持搜索和分类 |
| 新浪新闻 RSS | 免费 | 否 | 中文新闻，支持分类 |
| NewsAPI | 免费/付费 | 需要 API Key | 免费 100 请求/天 |

## 配置 NewsAPI（可选）

如需使用 NewsAPI，创建配置文件：

```bash
mkdir -p ~/.openclaw/keys
echo '{"newsapi": "YOUR_API_KEY"}' > ~/.openclaw/keys/news-search.json
```

获取 API Key: https://newsapi.org/register

## API 参数

### search(query, ...)

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| query | str | 必填 | 搜索关键词 |
| lang | str | "zh" | 语言 (zh/en) |
| days | int | 7 | 搜索天数范围 |
| limit | int | 20 | 最大结果数 |
| source | str | None | 指定数据源 |

### get_headlines(category, ...)

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| category | str | "general" | 分类 |
| country | str | "cn" | 国家 |
| source | str | None | 指定数据源 |

## 分类列表

- general - 综合
- tech - 科技
- business/finance - 财经
- sports - 体育
- entertainment - 娱乐
- science - 科学
- health - 健康

## 与其他 Skill 集成

### stock-analysis

```python
# 搜索股票相关新闻
news = searcher.search("贵州茅台", lang="zh", days=7)

# 分析新闻影响
# ...
```

### teach-cofounder

```python
# 获取技术新闻作为教学材料
news = searcher.get_headlines(category="tech", country="us")

# 用于技术讲解
# ...
```
# Embedding Providers Reference

## Zhipu AI (智谱AI) - Recommended

**Model:** `embeddings-2` (1024 dimensions)

**API Endpoint:** `https://open.bigmodel.cn/api/paas/v4/embeddings`

**Get API Key:** https://open.bigmodel.cn/

**Configuration in .env:**

```bash
CHAT_HISTORY_EMBEDDING_PROVIDER=zhipu
ZHIPU_API_KEY=your_api_key_here
ZHIPU_EMBEDDING_MODEL=embeddings-2
CHAT_HISTORY_VECTOR_DIMENSION=1024
```

**API Request Format:**

```json
{
  "model": "embeddings-2",
  "input": "text to embed"
}
```

**Response Format:**

```json
{
  "data": [
    {
      "embedding": [0.1, 0.2, ...],  // 1024 floats
      "index": 0,
      "object": "embedding"
    }
  ],
  "model": "embeddings-2",
  "object": "list"
}
```

## Volcano Engine (火山引擎)

**Models:** Various (check documentation)

**Get API Key:** https://www.volcengine.com/

**Configuration in .env:**

```bash
CHAT_HISTORY_EMBEDDING_PROVIDER=volcengine
VOLCENGINE_API_KEY=your_api_key_here
VOLCENGINE_API_SECRET=your_api_secret_here
VOLCENGINE_EMBEDDING_MODEL=your_endpoint_id
CHAT_HISTORY_VECTOR_DIMENSION=1024
```

## Cost Considerations

- Embedding API calls have associated costs
- Consider caching embeddings (already implemented via content_hash)
- Use `--no-embedding` flag for non-critical messages
- Batch messages when possible

## Testing

```bash
# Test embedding generation
# (Use the semantic search feature to verify)
```

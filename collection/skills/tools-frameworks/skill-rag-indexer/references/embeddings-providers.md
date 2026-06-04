# Embeddings Providers

## 支持的提供商

### OpenAI (推荐)

**模型**:
- `text-embedding-3-small` (默认) - 1536 维，性价比高
- `text-embedding-3-large` - 3072 维，更高精度
- `text-embedding-ada-002` - 1536 维，旧版模型

**配置**:
```bash
# .env
EMBEDDING_PROVIDER=openai
OPENAI_API_KEY=sk-your-api-key-here
EMBEDDING_MODEL=text-embedding-3-small
```

**费用**:
- text-embedding-3-small: $0.00002 / 1K tokens
- text-embedding-3-large: $0.00013 / 1K tokens

**获取 API Key**: https://platform.openai.com/api-keys

---

### Cohere

**模型**:
- `embed-v3.0` (默认) - 1024 维
- `embed-english-v3.0` - 1024 维
- `embed-multilingual-v3.0` - 1024 维

**配置**:
```bash
# .env
EMBEDDING_PROVIDER=cohere
COHERE_API_KEY=your-api-key-here
EMBEDDING_MODEL=embed-v3.0
```

**费用**:
- embed-v3.0: $0.0001 / 1K tokens

**获取 API Key**: https://dashboard.cohere.com/api-keys

---

## Provider 接口

所有 provider 都实现 `EmbeddingProvider` 接口:

```typescript
interface EmbeddingProvider {
  name: string;
  generate(text: string): Promise<number[]>;
  generateBatch(texts: string[]): Promise<number[][]>;
  getDimension(): number;
}
```

## 自定义 Provider

可以通过实现 `EmbeddingProvider` 接口来添加自定义 provider:

```typescript
class MyEmbeddingProvider implements EmbeddingProvider {
  get name(): string {
    return 'my-provider';
  }

  getDimension(): number {
    return 768;
  }

  async generate(text: string): Promise<number[]> {
    // 实现你的嵌入生成逻辑
  }

  async generateBatch(texts: string[]): Promise<number[][]> {
    // 批量生成
  }
}
```

然后在 `createEmbeddingProvider()` 中注册:

```typescript
if (provider === 'my-provider') {
  return new MyEmbeddingProvider();
}
```

## 选择建议

| 场景 | 推荐 Provider | 推荐模型 |
|------|---------------|----------|
| 预算敏感 | OpenAI | text-embedding-3-small |
| 需要最高精度 | OpenAI | text-embedding-3-large |
| 多语言内容 | Cohere | embed-multilingual-v3.0 |
| 已有 Cohere 账号 | Cohere | embed-v3.0 |

## 测试

测试你的配置:

```bash
# 构建索引会自动使用配置的 provider
npm run index:build
```

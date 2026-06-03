/**
 * Embedding Providers - Zhipu AI and Volcano Engine
 */

export interface EmbeddingProvider {
  name: string;
  generateEmbedding(text: string): Promise<number[]>;
  getDimension(): number;
}

export interface EmbeddingConfig {
  provider: 'zhipu' | 'volcengine';
  zhipu?: {
    api_key: string;
    model: string;
  };
  volcengine?: {
    api_key: string;
    api_secret: string;
    model: string;
  };
  vector_dimension: number;
}

/**
 * Zhipu AI (智谱AI) Embedding Provider
 */
export class ZhipuEmbeddingProvider implements EmbeddingProvider {
  private apiKey: string;
  private model: string;
  private dimension: number;

  constructor(apiKey: string, model: string = 'embeddings-2') {
    this.apiKey = apiKey;
    this.model = model;
    this.dimension = model === 'embeddings-3' ? 2560 : 1024;
  }

  get name(): string {
    return 'zhipu';
  }

  getDimension(): number {
    return this.dimension;
  }

  async generateEmbedding(text: string): Promise<number[]> {
    if (!this.apiKey) {
      throw new Error('ZHIPU_API_KEY is not configured');
    }

    // Truncate text if too long (Zhipu has token limits)
    const truncatedText = this.truncateText(text);

    const response = await fetch('https://open.bigmodel.cn/api/paas/v4/embeddings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify({
        model: this.model,
        input: truncatedText,
      }),
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`Zhipu API error: ${response.status} - ${error}`);
    }

    const data = await response.json();
    return data.data[0].embedding;
  }

  private truncateText(text: string, maxChars: number = 8000): string {
    if (text.length <= maxChars) {
      return text;
    }
    // Keep the beginning and end, truncate middle
    const half = Math.floor(maxChars / 2);
    return text.slice(0, half) + '\n...[truncated]...\n' + text.slice(-half);
  }
}

/**
 * Volcano Engine (火山引擎) Embedding Provider
 */
export class VolcengineEmbeddingProvider implements EmbeddingProvider {
  private apiKey: string;
  private apiSecret: string;
  private model: string;
  private dimension: number;

  constructor(apiKey: string, apiSecret: string, model: string, dimension: number = 1024) {
    this.apiKey = apiKey;
    this.apiSecret = apiSecret;
    this.model = model;
    this.dimension = dimension;
  }

  get name(): string {
    return 'volcengine';
  }

  getDimension(): number {
    return this.dimension;
  }

  async generateEmbedding(text: string): Promise<number[]> {
    if (!this.apiKey || !this.apiSecret) {
      throw new Error('VOLCENGINE_API_KEY and VOLCENGINE_API_SECRET are not configured');
    }

    // Volcano Engine API implementation
    // This is a placeholder - actual implementation would use their SDK
    // For now, we'll throw an error indicating it needs implementation
    throw new Error('Volcano Engine embedding provider not yet implemented. Please use Zhipu AI for now.');
  }
}

/**
 * Factory function to create embedding provider
 */
export function createEmbeddingProvider(config: EmbeddingConfig): EmbeddingProvider {
  switch (config.provider) {
    case 'zhipu':
      if (!config.zhipu?.api_key) {
        throw new Error('ZHIPU_API_KEY is required for Zhipu provider');
      }
      return new ZhipuEmbeddingProvider(config.zhipu.api_key, config.zhipu.model);

    case 'volcengine':
      if (!config.volcengine?.api_key || !config.volcengine?.api_secret) {
        throw new Error('VOLCENGINE_API_KEY and VOLCENGINE_API_SECRET are required for Volcano Engine provider');
      }
      return new VolcengineEmbeddingProvider(
        config.volcengine.api_key,
        config.volcengine.api_secret,
        config.volcengine.model,
        config.vector_dimension
      );

    default:
      throw new Error(`Unknown embedding provider: ${config.provider}`);
  }
}

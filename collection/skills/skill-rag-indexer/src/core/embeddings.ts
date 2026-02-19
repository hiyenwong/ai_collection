import OpenAI from 'openai';
import { CohereClient } from 'cohere-ai';
import { Skill } from '../types/index.js';

export interface EmbeddingProvider {
  name: string;
  generate(text: string): Promise<number[]>;
  generateBatch(texts: string[]): Promise<number[][]>;
  getDimension(): number;
}

export class OpenAIEmbeddingProvider implements EmbeddingProvider {
  private client: OpenAI;
  private model: string;

  constructor(apiKey: string, model: string = 'text-embedding-3-small') {
    this.client = new OpenAI({ apiKey });
    this.model = model;
  }

  get name(): string {
    return 'openai';
  }

  getDimension(): number {
    return this.model.includes('large') ? 3072 : 1536;
  }

  async generate(text: string): Promise<number[]> {
    const response = await this.client.embeddings.create({
      model: this.model,
      input: text,
    });
    return response.data[0].embedding;
  }

  async generateBatch(texts: string[]): Promise<number[][]> {
    const response = await this.client.embeddings.create({
      model: this.model,
      input: texts,
    });
    return response.data.map((d) => d.embedding);
  }
}

export class CohereEmbeddingProvider implements EmbeddingProvider {
  private client: CohereClient;
  private model: string;

  constructor(apiKey: string, model: string = 'embed-v3.0') {
    this.client = new CohereClient({ token: apiKey });
    this.model = model;
  }

  get name(): string {
    return 'cohere';
  }

  getDimension(): number {
    return 1024;
  }

  async generate(text: string): Promise<number[]> {
    const response = await this.client.embed({
      model: this.model,
      texts: [text],
      inputType: 'search_document',
    });
    return response.embeddings[0] as number[];
  }

  async generateBatch(texts: string[]): Promise<number[][]> {
    const response = await this.client.embed({
      model: this.model,
      texts,
      inputType: 'search_document',
    });
    return response.embeddings as number[][];
  }
}

export class EmbeddingGenerator {
  private provider: EmbeddingProvider;
  private cache: Map<string, number[]>;

  constructor(provider: EmbeddingProvider) {
    this.provider = provider;
    this.cache = new Map();
  }

  async generateForSkill(skill: Skill): Promise<number[]> {
    const text = this.generateSkillText(skill);
    const cacheKey = `${skill.id}-${skill.contentHash}`;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey)!;
    }

    const embedding = await this.provider.generate(text);
    this.cache.set(cacheKey, embedding);
    return embedding;
  }

  async generateForChunk(content: string): Promise<number[]> {
    return this.provider.generate(content);
  }

  generateSkillText(skill: Skill): string {
    const parts: string[] = [];
    parts.push(`# ${skill.name}`);
    parts.push(skill.description);

    if (skill.activationKeywords.length > 0) {
      parts.push(`Keywords: ${skill.activationKeywords.join(', ')}`);
    }

    if (skill.toolsUsed.length > 0) {
      const toolStr = skill.toolsUsed.map((t) => `${t.tool}: ${t.description}`).join('; ');
      parts.push(`Tools: ${toolStr}`);
    }

    if (skill.instructions) {
      parts.push('Instructions:');
      parts.push(skill.instructions);
    }

    return parts.join('\n\n');
  }

  getDimension(): number {
    return this.provider.getDimension();
  }
}

export function createEmbeddingProvider(): EmbeddingProvider {
  const provider = process.env.EMBEDDING_PROVIDER || 'openai';

  if (provider === 'openai') {
    const apiKey = process.env.OPENAI_API_KEY;
    if (!apiKey) {
      throw new Error('OPENAI_API_KEY is required for OpenAI embeddings');
    }
    const model = process.env.EMBEDDING_MODEL || 'text-embedding-3-small';
    return new OpenAIEmbeddingProvider(apiKey, model);
  }

  if (provider === 'cohere') {
    const apiKey = process.env.COHERE_API_KEY;
    if (!apiKey) {
      throw new Error('COHERE_API_KEY is required for Cohere embeddings');
    }
    const model = process.env.EMBEDDING_MODEL || 'embed-v3.0';
    return new CohereEmbeddingProvider(apiKey, model);
  }

  throw new Error(`Unsupported embedding provider: ${provider}`);
}

/**
 * Search and RAG functionality
 */

import type { ChatHistoryDatabase } from './database.js';
import type { EmbeddingProvider } from './embeddings.js';

// Type aliases for compatibility
type AnyRecord = Record<string, any>;

export interface SearchOptions {
  mode?: 'semantic' | 'keyword' | 'hybrid';
  session_id?: string;
  limit?: number;
  offset?: number;
  min_score?: number;
}

export interface RagOptions {
  limit?: number;
  session_id?: string;
  min_score?: number;
  include_session_context?: boolean;
  max_tokens?: number;
}

export interface ContextPromptOptions extends RagOptions {
  format?: 'text' | 'json';
  include_timestamps?: boolean;
}

export class ChatSearcher {
  private db: ChatHistoryDatabase;
  private embeddingProvider: EmbeddingProvider;

  constructor(db: ChatHistoryDatabase, embeddingProvider: EmbeddingProvider) {
    this.db = db;
    this.embeddingProvider = embeddingProvider;
  }

  async semanticSearch(query: string, options: SearchOptions = {}): Promise<any[]> {
    const embedding = await this.embeddingProvider.generateEmbedding(query);
    const results = await this.db.searchByVector(embedding, options);
    return results;
  }

  async keywordSearch(query: string, options: SearchOptions = {}): Promise<any[]> {
    return this.db.searchByKeyword(query, options);
  }

  async hybridSearch(query: string, options: SearchOptions = {}): Promise<any[]> {
    const embedding = await this.embeddingProvider.generateEmbedding(query);
    return this.db.hybridSearch(query, embedding, options);
  }

  async search(query: string, options: SearchOptions = {}): Promise<any[]> {
    const mode = options.mode || 'hybrid';
    switch (mode) {
      case 'semantic':
        return this.semanticSearch(query, options);
      case 'keyword':
        return this.keywordSearch(query, options);
      case 'hybrid':
      default:
        return this.hybridSearch(query, options);
    }
  }

  async retrieveForRag(query: string, options: RagOptions = {}): Promise<any> {
    const limit = options.limit || 10;
    const minScore = options.min_score || 0.5;

    const results = await this.semanticSearch(query, {
      limit: limit * 2,
      min_score: minScore,
      session_id: options.session_id,
    });

    // Group by session and get context
    const messages = results.slice(0, limit).map((r: any) => r.message);
    const sessionId = messages[0]?.session_id;
    const session = sessionId ? await this.db.getSession(sessionId) : null;

    return {
      messages,
      session: session || {
        session_id: 'unknown',
        title: 'Unknown Session',
        created_at: Date.now(),
        updated_at: Date.now(),
      },
      relevance_score: results[0]?.score || 0,
      context_summary: `Retrieved ${messages.length} relevant messages`,
    };
  }

  async buildContextPrompt(query: string, options: ContextPromptOptions = {}): Promise<string> {
    const ragContext = await this.retrieveForRag(query, options);

    if (ragContext.messages.length === 0) {
      return 'No relevant context found.';
    }

    if (options.format === 'json') {
      return JSON.stringify(ragContext, null, 2);
    }

    // Build text format
    let prompt = `## Context from "${ragContext.session.title}"\n\n`;
    prompt += `Relevance: ${Math.round(ragContext.relevance_score * 100)}%\n\n`;
    prompt += `---\n\n`;

    for (const msg of ragContext.messages) {
      prompt += `### ${msg.role.charAt(0).toUpperCase() + msg.role.slice(1)}`;
      if (options.include_timestamps) {
        prompt += ` (${new Date(msg.timestamp).toISOString()})`;
      }
      prompt += `\n\n${msg.content}\n\n`;
    }

    prompt += `---\n\n`;
    prompt += `## Current Query\n\n${query}\n`;

    return prompt;
  }
}

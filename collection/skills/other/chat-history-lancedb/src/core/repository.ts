/**
 * Chat Repository - High-level business logic
 */

import type { ChatHistoryDatabase } from './database.js';
import type { EmbeddingProvider } from './embeddings.js';
import {
  generateId,
  sanitizeMessageInput,
  sanitizeSessionInput,
  nowTimestamp,
} from '../utils/validation.js';

// Type aliases for compatibility
type AnyRecord = Record<string, any>;

export interface ContextOptions {
  limit?: number;
  before_timestamp?: number;
  after_timestamp?: number;
  include_system?: boolean;
}

export interface RetrieveOptions {
  limit?: number;
  session_id?: string;
  min_score?: number;
}

export class ChatRepository {
  private db: ChatHistoryDatabase;
  private embeddingProvider: EmbeddingProvider | null;

  constructor(db: ChatHistoryDatabase, embeddingProvider: EmbeddingProvider | null = null) {
    this.db = db;
    this.embeddingProvider = embeddingProvider;
  }

  // ============ Message Operations ============

  async saveMessage(
    input: AnyRecord,
    generateEmbedding: boolean = true
  ): Promise<string> {
    const sanitized = sanitizeMessageInput(input as any);

    const message: AnyRecord = {
      message_id: sanitized.message_id || generateId(),
      session_id: sanitized.session_id,
      role: sanitized.role,
      content: sanitized.content,
      timestamp: sanitized.timestamp || nowTimestamp(),
      parent_message_id: sanitized.parent_message_id,
      metadata: sanitized.metadata,
      tags: sanitized.tags,
      attachments: sanitized.attachments,
    };

    // Generate embedding if requested and provider is available
    if (generateEmbedding && this.embeddingProvider) {
      try {
        message.embedding = await this.embeddingProvider.generateEmbedding(message.content);
      } catch (err) {
        console.warn('Failed to generate embedding:', err);
      }
    }

    await this.db.insertMessage(message);
    return message.message_id;
  }

  async getMessage(messageId: string): Promise<AnyRecord | null> {
    return this.db.getMessage(messageId);
  }

  async updateMessage(messageId: string, updates: Partial<AnyRecord>): Promise<void> {
    await this.db.updateMessage(messageId, updates);
  }

  async deleteMessage(messageId: string): Promise<void> {
    await this.db.deleteMessage(messageId);
  }

  // ============ Session Operations ============

  async createSession(input?: AnyRecord): Promise<string> {
    const sanitized = sanitizeSessionInput(input || {});

    const session: AnyRecord = {
      session_id: sanitized.session_id,
      title: sanitized.title,
      created_at: sanitized.created_at,
      updated_at: sanitized.updated_at,
      metadata: sanitized.metadata,
      tags: sanitized.tags,
      message_count: 0,
    };

    await this.db.insertSession(session);
    return session.session_id;
  }

  async getSession(sessionId: string): Promise<AnyRecord | null> {
    return this.db.getSession(sessionId);
  }

  async updateSession(sessionId: string, updates: Partial<AnyRecord>): Promise<void> {
    await this.db.updateSession(sessionId, updates);
  }

  async deleteSession(sessionId: string, deleteMessages: boolean = false): Promise<void> {
    await this.db.deleteSession(sessionId, deleteMessages);
  }

  async getSessionMessages(
    sessionId: string,
    options: ContextOptions = {}
  ): Promise<AnyRecord[]> {
    const messages = await this.db.getSessionMessages(
      sessionId,
      options.limit || 100,
      0
    );

    // Apply filters
    return messages.filter((msg) => {
      if (options.before_timestamp && msg.timestamp > options.before_timestamp) {
        return false;
      }
      if (options.after_timestamp && msg.timestamp < options.after_timestamp) {
        return false;
      }
      if (!options.include_system && msg.role === 'system') {
        return false;
      }
      return true;
    });
  }

  async listSessions(limit: number = 50, offset: number = 0): Promise<AnyRecord[]> {
    return this.db.listSessions(limit, offset);
  }

  // ============ RAG Operations ============

  async retrieveRelevantHistory(
    query: string,
    options: RetrieveOptions = {}
  ): Promise<any[]> {
    if (!this.embeddingProvider) {
      throw new Error('Embedding provider is required for RAG retrieval');
    }

    const embedding = await this.embeddingProvider.generateEmbedding(query);
    const searchResults = await this.db.searchByVector(embedding, {
      limit: options.limit || 10,
      min_score: options.min_score || 0.5,
      session_id: options.session_id,
    });

    // Group by session
    const sessionMap = new Map<string, { messages: AnyRecord[]; score: number }>();

    for (const result of searchResults) {
      const sessionId = result.message.session_id;
      const existing = sessionMap.get(sessionId);
      if (existing) {
        existing.messages.push(result.message);
        existing.score = Math.max(existing.score, result.score);
      } else {
        sessionMap.set(sessionId, {
          messages: [result.message],
          score: result.score,
        });
      }
    }

    // Build contexts
    const contexts: any[] = [];
    for (const [sessionId, data] of sessionMap) {
      const session = await this.db.getSession(sessionId);
      if (session) {
        contexts.push({
          messages: data.messages,
          session,
          relevance_score: data.score,
          context_summary: `Relevant messages from "${session.title}"`,
        });
      }
    }

    return contexts.sort((a, b) => b.relevance_score - a.relevance_score);
  }
}

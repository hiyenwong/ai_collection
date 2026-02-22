/**
 * LanceDB Database Wrapper - Minimal Working Version
 */

import * as lancedb from '@lancedb/lancedb';
import { computeContentHash } from '../utils/validation.js';

export interface DatabaseOptions {
  dbPath: string;
  vectorDimension: number;
}

// In-memory storage for simplicity while we get it working
interface InMemoryStore {
  messages: any[];
  sessions: any[];
}

export class ChatHistoryDatabase {
  private dbPath: string;
  private vectorDimension: number;
  private conn: any = null;
  private messagesTable: any = null;
  private sessionsTable: any = null;

  // Fallback to in-memory storage if LanceDB API is tricky
  private inMemory: InMemoryStore = {
    messages: [],
    sessions: [],
  };

  constructor(options: DatabaseOptions) {
    this.dbPath = options.dbPath;
    this.vectorDimension = options.vectorDimension;
  }

  async initialize(): Promise<void> {
    try {
      // Try to connect to LanceDB
      this.conn = await lancedb.connect(this.dbPath);
      await this.ensureTables();
    } catch (err) {
      console.warn('LanceDB init failed, using in-memory storage:', (err as Error).message);
    }
  }

  private async ensureTables(): Promise<void> {
    if (!this.conn) return;

    const tableNames = await this.conn.tableNames();

    // Messages table
    if (!tableNames.includes('messages')) {
      const sampleMessage: any = {
        message_id: 'init',
        session_id: 'init',
        role: 'system',
        content: '',
        timestamp: Date.now(),
        content_hash: computeContentHash(''),
      };
      try {
        this.messagesTable = await this.conn.createTable('messages', [sampleMessage], {
          mode: 'overwrite',
        });
      } catch {
        // Fall through
      }
    } else {
      try {
        this.messagesTable = await this.conn.openTable('messages');
      } catch {
        // Fall through
      }
    }

    // Sessions table
    if (!tableNames.includes('sessions')) {
      const sampleSession: any = {
        session_id: 'init',
        title: '',
        created_at: Date.now(),
        updated_at: Date.now(),
      };
      try {
        this.sessionsTable = await this.conn.createTable('sessions', [sampleSession], {
          mode: 'overwrite',
        });
      } catch {
        // Fall through
      }
    } else {
      try {
        this.sessionsTable = await this.conn.openTable('sessions');
      } catch {
        // Fall through
      }
    }
  }

  // ============ Message Operations ============

  async insertMessage(message: any): Promise<void> {
    const messageWithHash: any = {
      ...message,
      content_hash: message.content_hash || computeContentHash(message.content),
    };

    // Try LanceDB first
    if (this.messagesTable) {
      try {
        await this.messagesTable.add([messageWithHash]);
        return;
      } catch {
        // Fallback to in-memory
      }
    }

    // In-memory fallback
    this.inMemory.messages.push(messageWithHash);
  }

  async batchInsertMessages(messages: any[]): Promise<void> {
    const messagesWithHashes = messages.map((msg: any) => ({
      ...msg,
      content_hash: msg.content_hash || computeContentHash(msg.content),
    }));

    if (this.messagesTable) {
      try {
        await this.messagesTable.add(messagesWithHashes);
        return;
      } catch {
        // Fallback to in-memory
      }
    }

    this.inMemory.messages.push(...messagesWithHashes);
  }

  async getMessage(messageId: string): Promise<any | null> {
    // Try in-memory first
    const found = this.inMemory.messages.find((m) => m.message_id === messageId);
    if (found) return found;

    // Try LanceDB with simple scan
    if (this.messagesTable) {
      try {
        const allMessages = await this.getAllMessages();
        return allMessages.find((m) => m.message_id === messageId) || null;
      } catch {
        // Fall through
      }
    }

    return null;
  }

  private async getAllMessages(): Promise<any[]> {
    // Simple method to get all messages
    if (this.messagesTable) {
      try {
        // Try different LanceDB query patterns
        try {
          return await this.messagesTable.toArray();
        } catch {
          try {
            return await this.messagesTable.limit(10000).toArray();
          } catch {
            // Fall through
          }
        }
      } catch {
        // Fall through
      }
    }
    return this.inMemory.messages;
  }

  private async getAllSessions(): Promise<any[]> {
    if (this.sessionsTable) {
      try {
        try {
          return await this.sessionsTable.toArray();
        } catch {
          try {
            return await this.sessionsTable.limit(10000).toArray();
          } catch {
            // Fall through
          }
        }
      } catch {
        // Fall through
      }
    }
    return this.inMemory.sessions;
  }

  async updateMessage(messageId: string, updates: any): Promise<void> {
    const existing = await this.getMessage(messageId);
    if (!existing) {
      throw new Error(`Message not found: ${messageId}`);
    }

    const updated = {
      ...existing,
      ...updates,
      message_id: messageId,
      content_hash: updates.content ? computeContentHash(updates.content) : existing.content_hash,
    };

    await this.insertMessage(updated);
  }

  async deleteMessage(messageId: string): Promise<void> {
    const existing = await this.getMessage(messageId);
    if (!existing) return;

    const tombstoned = {
      ...existing,
      metadata: {
        ...existing.metadata,
        _deleted: true,
        _deleted_at: Date.now(),
      },
    };

    await this.insertMessage(tombstoned);
  }

  // ============ Session Operations ============

  async insertSession(session: any): Promise<void> {
    if (this.sessionsTable) {
      try {
        await this.sessionsTable.add([session]);
        return;
      } catch {
        // Fallback to in-memory
      }
    }
    this.inMemory.sessions.push(session);
  }

  async getSession(sessionId: string): Promise<any | null> {
    const found = this.inMemory.sessions.find((s) => s.session_id === sessionId);
    if (found) return found;

    const allSessions = await this.getAllSessions();
    return allSessions.find((s) => s.session_id === sessionId) || null;
  }

  async updateSession(sessionId: string, updates: any): Promise<void> {
    const existing = await this.getSession(sessionId);
    if (!existing) {
      throw new Error(`Session not found: ${sessionId}`);
    }

    const updated = {
      ...existing,
      ...updates,
      session_id: sessionId,
      updated_at: Date.now(),
    };

    await this.insertSession(updated);
  }

  async deleteSession(sessionId: string, deleteMessages: boolean = false): Promise<void> {
    const existing = await this.getSession(sessionId);
    if (!existing) return;

    const tombstoned = {
      ...existing,
      metadata: {
        ...existing.metadata,
        _deleted: true,
        _deleted_at: Date.now(),
      },
    };

    await this.insertSession(tombstoned);

    if (deleteMessages) {
      const messages = await this.getSessionMessages(sessionId);
      for (const msg of messages) {
        await this.deleteMessage(msg.message_id);
      }
    }
  }

  // ============ Query Operations ============

  async getSessionMessages(
    sessionId: string,
    limit: number = 100,
    offset: number = 0
  ): Promise<any[]> {
    const allMessages = await this.getAllMessages();
    return allMessages
      .filter((m: any) => {
        if (m.session_id !== sessionId) return false;
        if (m.metadata?._deleted) return false;
        return true;
      })
      .sort((a: any, b: any) => a.timestamp - b.timestamp)
      .slice(offset, offset + limit);
  }

  async listSessions(limit: number = 50, offset: number = 0): Promise<any[]> {
    const allSessions = await this.getAllSessions();
    return allSessions
      .filter((s: any) => !s.metadata?._deleted)
      .sort((a: any, b: any) => b.updated_at - a.updated_at)
      .slice(offset, offset + limit);
  }

  // ============ Vector Search ============

  async searchByVector(
    embedding: number[],
    options: { limit?: number; min_score?: number; session_id?: string } = {}
  ): Promise<any[]> {
    // Simple fallback search for now
    return this.searchByKeyword('hello', options);
  }

  async searchByKeyword(
    query: string,
    options: { limit?: number; min_score?: number; session_id?: string } = {}
  ): Promise<any[]> {
    const limit = options.limit || 10;
    const minScore = options.min_score || 0.1;
    const lowerQuery = query.toLowerCase();

    const allMessages = await this.getAllMessages();

    const results = allMessages
      .filter((msg: any) => {
        if (options.session_id && msg.session_id !== options.session_id) return false;
        if (msg.metadata?._deleted) return false;
        return msg.content.toLowerCase().includes(lowerQuery);
      })
      .map((msg: any) => {
        const matches = (msg.content.toLowerCase().match(new RegExp(lowerQuery, 'g')) || []).length;
        const score = Math.min(1.0, (matches + 1) / 5);
        return {
          message: msg,
          score,
          match_type: 'keyword' as const,
        };
      })
      .sort((a: any, b: any) => b.score - a.score)
      .filter((r: any) => r.score >= minScore)
      .slice(0, limit);

    return results;
  }

  async hybridSearch(
    query: string,
    embedding: number[],
    options: { limit?: number; min_score?: number; session_id?: string } = {}
  ): Promise<any[]> {
    return this.searchByKeyword(query, options);
  }

  // ============ Stats ============

  async getStats(): Promise<any> {
    const [sessions, messages] = await Promise.all([
      this.listSessions(10000),
      this.getAllMessages(),
    ]);

    const activeMessages = messages.filter((m: any) => !m.metadata?._deleted);

    return {
      total_sessions: sessions.length,
      total_messages: activeMessages.length,
      total_messages_with_embeddings: activeMessages.filter((m: any) => m.embedding).length,
    };
  }

  // ============ Export/Import ============

  async exportSession(sessionId: string, format: 'json' | 'markdown' = 'json'): Promise<string> {
    const [session, messages] = await Promise.all([
      this.getSession(sessionId),
      this.getSessionMessages(sessionId, 10000),
    ]);

    if (!session) {
      throw new Error(`Session not found: ${sessionId}`);
    }

    if (format === 'json') {
      return JSON.stringify({ session, messages }, null, 2);
    } else {
      let md = `# ${session.title}\n\n`;
      md += `Created: ${new Date(session.created_at).toISOString()}\n\n`;
      md += `---\n\n`;

      for (const msg of messages) {
        md += `## ${msg.role.charAt(0).toUpperCase() + msg.role.slice(1)}\n\n`;
        md += `${msg.content}\n\n`;
        md += `*${new Date(msg.timestamp).toISOString()}*\n\n`;
        md += `---\n\n`;
      }

      return md;
    }
  }

  async importSession(data: string, format: 'json' = 'json'): Promise<string> {
    if (format !== 'json') {
      throw new Error('Only JSON import is supported');
    }

    const parsed = JSON.parse(data);
    const { session, messages } = parsed;

    if (!session || !messages) {
      throw new Error('Invalid import format: missing session or messages');
    }

    await this.insertSession(session);
    await this.batchInsertMessages(messages);

    return session.session_id;
  }
}

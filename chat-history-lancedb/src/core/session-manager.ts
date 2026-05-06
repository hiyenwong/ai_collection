/**
 * Session Management
 */

import type { ChatHistoryDatabase } from './database.js';

// Type aliases for compatibility
type AnyRecord = Record<string, any>;

export class SessionManager {
  private db: ChatHistoryDatabase;

  constructor(db: ChatHistoryDatabase) {
    this.db = db;
  }

  async createSession(title?: string): Promise<string> {
    const { ChatRepository } = await import('./repository.js');
    const repo = new ChatRepository(this.db);
    return repo.createSession({ title });
  }

  async renameSession(sessionId: string, title: string): Promise<void> {
    await this.db.updateSession(sessionId, { title });
  }

  async archiveSession(sessionId: string): Promise<void> {
    const session = await this.db.getSession(sessionId);
    if (!session) {
      throw new Error(`Session not found: ${sessionId}`);
    }

    const tags = [...((session.tags as string[]) || [])];
    if (!tags.includes('archived')) {
      tags.push('archived');
    }

    await this.db.updateSession(sessionId, { tags });
  }

  async getSessionStats(sessionId: string): Promise<any> {
    const [session, messages] = await Promise.all([
      this.db.getSession(sessionId),
      this.db.getSessionMessages(sessionId, 10000),
    ]);

    if (!session) {
      throw new Error(`Session not found: ${sessionId}`);
    }

    const userMessages = messages.filter((m) => m.role === 'user');
    const assistantMessages = messages.filter((m) => m.role === 'assistant');

    return {
      session_id: session.session_id,
      title: session.title,
      message_count: messages.length,
      created_at: session.created_at,
      updated_at: session.updated_at,
      user_message_count: userMessages.length,
      assistant_message_count: assistantMessages.length,
      first_message_at: messages[0]?.timestamp,
      last_message_at: messages[messages.length - 1]?.timestamp,
    };
  }

  async getOverallStats(): Promise<any> {
    const [sessions, dbStats] = await Promise.all([
      this.db.listSessions(10000),
      this.db.getStats(),
    ]);

    let totalUserMessages = 0;
    let totalAssistantMessages = 0;
    let oldestSessionAt: number | undefined;
    let newestSessionAt: number | undefined;

    for (const session of sessions) {
      const stats = await this.getSessionStats(session.session_id);
      totalUserMessages += stats.user_message_count;
      totalAssistantMessages += stats.assistant_message_count;

      if (!oldestSessionAt || session.created_at < oldestSessionAt) {
        oldestSessionAt = session.created_at;
      }
      if (!newestSessionAt || session.created_at > newestSessionAt) {
        newestSessionAt = session.created_at;
      }
    }

    return {
      total_sessions: sessions.length,
      total_messages: dbStats.total_messages,
      total_user_messages: totalUserMessages,
      total_assistant_messages: totalAssistantMessages,
      oldest_session_at: oldestSessionAt,
      newest_session_at: newestSessionAt,
      avg_messages_per_session: sessions.length > 0 ? dbStats.total_messages / sessions.length : 0,
    };
  }
}

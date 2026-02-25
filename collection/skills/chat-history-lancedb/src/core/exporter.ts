/**
 * Export/Import functionality - Simplified Version
 */

import type { ChatHistoryDatabase } from './database.js';

export class ChatExporter {
  private db: ChatHistoryDatabase;

  constructor(db: ChatHistoryDatabase) {
    this.db = db;
  }

  async exportSession(
    sessionId: string,
    format: 'json' | 'markdown' | 'html' = 'json'
  ): Promise<string> {
    return this.db.exportSession(sessionId, format as any);
  }

  async exportAllSessions(format: 'json' | 'markdown' = 'json'): Promise<Map<string, string>> {
    const sessions = await this.db.listSessions(10000);
    const results = new Map<string, string>();

    for (const session of sessions) {
      const content = await this.exportSession(session.session_id, format);
      results.set(session.session_id, content);
    }

    return results;
  }

  async importSession(jsonData: string): Promise<string> {
    return this.db.importSession(jsonData, 'json');
  }

  async importSessions(jsonDataArray: string[]): Promise<string[]> {
    const results: string[] = [];
    for (const data of jsonDataArray) {
      const sessionId = await this.importSession(data);
      results.push(sessionId);
    }
    return results;
  }

  async mergeSessions(
    sourceSessionIds: string[],
    targetTitle: string
  ): Promise<string> {
    const { ChatRepository } = await import('./repository.js');
    const repo = new ChatRepository(this.db);

    const targetSessionId = await repo.createSession({ title: targetTitle });

    const allMessages: any[] = [];

    for (const sessionId of sourceSessionIds) {
      const session = await this.db.getSession(sessionId);
      const messages = await this.db.getSessionMessages(sessionId, 10000);
      if (session) {
        for (const msg of messages) {
          allMessages.push({ ...msg, original_session_id: session.session_id });
        }
      }
    }

    allMessages.sort((a, b) => a.timestamp - b.timestamp);

    for (const msg of allMessages) {
      await repo.saveMessage(
        {
          session_id: targetSessionId,
          role: msg.role,
          content: msg.content,
          parent_message_id: msg.parent_message_id,
          metadata: {
            ...msg.metadata,
            _original_session_id: msg.original_session_id,
          },
          tags: msg.tags,
          attachments: msg.attachments,
        },
        false
      );
    }

    return targetSessionId;
  }
}

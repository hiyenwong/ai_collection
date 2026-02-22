/**
 * Search and RAG Types
 */

import { ChatMessage, ChatSession } from './index.js';

export type SearchMode = 'semantic' | 'keyword' | 'hybrid';

export interface SearchOptions {
  mode?: SearchMode;
  session_id?: string;
  limit?: number;
  offset?: number;
  min_score?: number;
  role?: string;
  start_time?: number;
  end_time?: number;
}

export interface MessageSearchResult {
  message: ChatMessage;
  session?: ChatSession;
  score: number;
  match_type: SearchMode;
  highlight?: string;
}

export interface RagContext {
  messages: ChatMessage[];
  session: ChatSession;
  relevance_score: number;
  context_summary: string;
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

export interface DatabaseStats {
  total_sessions: number;
  total_messages: number;
  total_messages_with_embeddings: number;
  database_size_bytes?: number;
  oldest_message_at?: number;
  newest_message_at?: number;
}

/**
 * Chat Session Types
 */

export interface ChatSession {
  session_id: string;
  title: string;
  created_at: number;
  updated_at: number;

  // Metadata
  metadata?: Record<string, any>;
  tags?: string[];

  // Cached stats
  message_count?: number;
  last_message_at?: number;
}

export interface CreateSessionInput {
  session_id?: string;
  title?: string;
  metadata?: Record<string, any>;
  tags?: string[];
}

export interface UpdateSessionInput extends Partial<Omit<ChatSession, 'session_id' | 'created_at'>> {}

export interface SessionStats {
  session_id: string;
  title: string;
  message_count: number;
  created_at: number;
  updated_at: number;
  user_message_count: number;
  assistant_message_count: number;
  first_message_at?: number;
  last_message_at?: number;
}

export interface OverallStats {
  total_sessions: number;
  total_messages: number;
  total_user_messages: number;
  total_assistant_messages: number;
  oldest_session_at?: number;
  newest_session_at?: number;
  avg_messages_per_session: number;
}

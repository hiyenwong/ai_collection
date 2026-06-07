/**
 * Chat Message Types
 */

export type MessageRole = 'user' | 'assistant' | 'system' | 'tool';

export interface Attachment {
  id: string;
  type: 'image' | 'file' | 'link';
  url: string;
  name?: string;
  mime_type?: string;
}

export interface ChatMessage {
  message_id: string;
  session_id: string;
  role: MessageRole;
  content: string;
  timestamp: number;

  // Extended fields
  parent_message_id?: string;
  metadata?: Record<string, any>;
  tags?: string[];
  attachments?: Attachment[];

  // Vector search fields
  embedding?: number[];
  content_hash?: string;
}

export interface CreateMessageInput
  extends Omit<ChatMessage, 'message_id' | 'timestamp' | 'content_hash' | 'embedding'> {
  message_id?: string;
  timestamp?: number;
}

export interface UpdateMessageInput extends Partial<Omit<ChatMessage, 'message_id' | 'session_id' | 'timestamp' | 'content_hash' | 'embedding'>> {}

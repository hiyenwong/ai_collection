/**
 * Validation Utilities
 */

import { v4 as uuidv4 } from 'uuid';
import CryptoJS from 'crypto-js';

type MessageRole = 'user' | 'assistant' | 'system' | 'tool';

export function generateId(): string {
  return uuidv4();
}

export function validateMessageRole(role: string): role is MessageRole {
  return ['user', 'assistant', 'system', 'tool'].includes(role);
}

export function computeContentHash(content: string): string {
  return CryptoJS.SHA256(content).toString();
}

export function nowTimestamp(): number {
  return Date.now();
}

export function sanitizeMessageInput(input: any): any {
  const sanitized: any = {
    ...input,
    message_id: input.message_id || generateId(),
    timestamp: input.timestamp || nowTimestamp(),
  };

  // Validate role
  if (!validateMessageRole(sanitized.role)) {
    throw new Error(`Invalid message role: ${sanitized.role}`);
  }

  // Ensure content is not empty
  if (!sanitized.content || sanitized.content.trim().length === 0) {
    throw new Error('Message content cannot be empty');
  }

  return sanitized;
}

export function sanitizeSessionInput(input: any): any {
  const now = nowTimestamp();
  return {
    ...input,
    session_id: input.session_id || generateId(),
    title: input.title || `Session ${new Date().toISOString().slice(0, 10)}`,
    created_at: now,
    updated_at: now,
  };
}

export function formatTimestamp(timestamp: number): string {
  return new Date(timestamp).toISOString();
}

export function formatDuration(start: number, end: number): string {
  const ms = end - start;
  const seconds = Math.floor(ms / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);

  if (hours > 0) {
    return `${hours}h ${minutes % 60}m`;
  } else if (minutes > 0) {
    return `${minutes}m ${seconds % 60}s`;
  } else {
    return `${seconds}s`;
  }
}

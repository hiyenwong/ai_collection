/**
 * Configuration Management
 */

import dotenv from 'dotenv';
import path from 'path';
import os from 'os';

export interface EmbeddingConfig {
  provider: 'zhipu' | 'volcengine';
  zhipu?: {
    api_key: string;
    model: string;
  };
  volcengine?: {
    api_key: string;
    api_secret: string;
    model: string;
  };
  vector_dimension: number;
}

export interface DatabaseConfig {
  db_path: string;
}

export interface SearchConfig {
  default_limit: number;
  min_score: number;
  hybrid_weight: number;
}

export interface ChatHistoryConfig {
  database: DatabaseConfig;
  embedding: EmbeddingConfig;
  search: SearchConfig;
}

const DEFAULT_CONFIG: ChatHistoryConfig = {
  database: {
    db_path: path.join(os.homedir(), '.chat-history-lancedb'),
  },
  embedding: {
    provider: 'zhipu',
    vector_dimension: 1024,
    zhipu: {
      api_key: '',
      model: 'embeddings-2',
    },
    volcengine: {
      api_key: '',
      api_secret: '',
      model: '',
    },
  },
  search: {
    default_limit: 10,
    min_score: 0.5,
    hybrid_weight: 0.7,
  },
};

let loadedConfig: ChatHistoryConfig | null = null;

export function loadConfig(envPath?: string): ChatHistoryConfig {
  if (loadedConfig) {
    return loadedConfig;
  }

  // Load environment variables
  if (envPath) {
    dotenv.config({ path: envPath });
  } else {
    dotenv.config();
  }

  const config: ChatHistoryConfig = { ...DEFAULT_CONFIG };

  // Database config
  if (process.env.CHAT_HISTORY_DB_PATH) {
    config.database.db_path = process.env.CHAT_HISTORY_DB_PATH.replace('~', os.homedir());
  }

  // Embedding config
  if (process.env.CHAT_HISTORY_EMBEDDING_PROVIDER) {
    config.embedding.provider = process.env.CHAT_HISTORY_EMBEDDING_PROVIDER as 'zhipu' | 'volcengine';
  }

  if (process.env.ZHIPU_API_KEY) {
    config.embedding.zhipu!.api_key = process.env.ZHIPU_API_KEY;
  }
  if (process.env.ZHIPU_EMBEDDING_MODEL) {
    config.embedding.zhipu!.model = process.env.ZHIPU_EMBEDDING_MODEL;
  }

  if (process.env.VOLCENGINE_API_KEY) {
    config.embedding.volcengine!.api_key = process.env.VOLCENGINE_API_KEY;
  }
  if (process.env.VOLCENGINE_API_SECRET) {
    config.embedding.volcengine!.api_secret = process.env.VOLCENGINE_API_SECRET;
  }
  if (process.env.VOLCENGINE_EMBEDDING_MODEL) {
    config.embedding.volcengine!.model = process.env.VOLCENGINE_EMBEDDING_MODEL;
  }

  if (process.env.CHAT_HISTORY_VECTOR_DIMENSION) {
    config.embedding.vector_dimension = parseInt(process.env.CHAT_HISTORY_VECTOR_DIMENSION, 10);
  }

  // Search config
  if (process.env.CHAT_HISTORY_SEARCH_LIMIT) {
    config.search.default_limit = parseInt(process.env.CHAT_HISTORY_SEARCH_LIMIT, 10);
  }
  if (process.env.CHAT_HISTORY_SEARCH_MIN_SCORE) {
    config.search.min_score = parseFloat(process.env.CHAT_HISTORY_SEARCH_MIN_SCORE);
  }

  loadedConfig = config;
  return config;
}

export function getConfig(): ChatHistoryConfig {
  if (!loadedConfig) {
    return loadConfig();
  }
  return loadedConfig;
}

export function setConfig(config: Partial<ChatHistoryConfig>): void {
  loadedConfig = {
    ...(loadedConfig || DEFAULT_CONFIG),
    ...config,
  };
}

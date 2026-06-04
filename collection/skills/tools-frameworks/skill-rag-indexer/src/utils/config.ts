import * as path from 'path';
import * as fs from 'fs';

export interface Config {
  databasePath: string;
  embeddingsProvider: string;
  embeddingsModel: string;
  skillsRoot: string;
  search: {
    defaultLimit: number;
    minScore: number;
    hybridWeight: number;
  };
}

const DEFAULT_CONFIG: Config = {
  databasePath: process.env.SKILL_RAG_DB_PATH || './skills-index.db',
  embeddingsProvider: process.env.EMBEDDING_PROVIDER || 'openai',
  embeddingsModel: process.env.EMBEDDING_MODEL || 'text-embedding-3-small',
  skillsRoot: '../../collection/skills',
  search: {
    defaultLimit: parseInt(process.env.SKILL_RAG_DEFAULT_LIMIT || '10', 10),
    minScore: parseFloat(process.env.SKILL_RAG_MIN_SCORE || '0.5'),
    hybridWeight: parseFloat(process.env.SKILL_RAG_HYBRID_WEIGHT || '0.7'),
  },
};

let cachedConfig: Config | null = null;

export function loadConfig(configPath?: string): Config {
  if (cachedConfig) {
    return cachedConfig;
  }

  let config = { ...DEFAULT_CONFIG };

  if (configPath && fs.existsSync(configPath)) {
    const fileConfig = JSON.parse(fs.readFileSync(configPath, 'utf-8'));
    config = { ...config, ...fileConfig };
  }

  const localConfigPath = path.resolve('.skill-rag-indexer.json');
  if (fs.existsSync(localConfigPath)) {
    const localConfig = JSON.parse(fs.readFileSync(localConfigPath, 'utf-8'));
    config = { ...config, ...localConfig };
  }

  if (!path.isAbsolute(config.databasePath)) {
    config.databasePath = path.resolve(config.databasePath);
  }

  cachedConfig = config;
  return config;
}

export function getConfig(): Config {
  return loadConfig();
}

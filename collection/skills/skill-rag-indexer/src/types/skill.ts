export interface ToolUsage {
  tool: string;
  description: string;
}

export interface SkillMetadata {
  createdAt: Date;
  updatedAt: Date;
  sections: string[];
}

export interface Skill {
  id: string;
  name: string;
  description: string;
  activationKeywords: string[];
  toolsUsed: ToolUsage[];
  instructions: string;
  contentHash: string;
  path: string;
  metadata: SkillMetadata;
}

export interface IndexedSkill extends Skill {
  embedding: number[];
}

export interface SearchResult {
  skill: Skill;
  score: number;
  distance: number;
  matchType: 'semantic' | 'keyword' | 'hybrid';
}

export interface Recommendation {
  skill: Skill;
  score: number;
  reason: string;
}

export interface SearchOptions {
  limit?: number;
  minScore?: number;
  includeChunks?: boolean;
}

export interface RecommendOptions {
  limit?: number;
  includeSkills?: string[];
  excludeSkills?: string[];
}

export interface IndexResult {
  totalSkills: number;
  indexed: number;
  updated: number;
  skipped: number;
  errors: string[];
  duration: number;
}

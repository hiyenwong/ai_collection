import { SearchResult, Recommendation, SearchOptions, RecommendOptions } from '../types/index.js';
import { SkillDatabase } from './database.js';
import { EmbeddingGenerator } from './embeddings.js';
import { getConfig } from '../utils/config.js';

export class SkillSearcher {
  private db: SkillDatabase;
  private embeddings: EmbeddingGenerator;
  private config = getConfig();

  constructor(db: SkillDatabase, embeddings: EmbeddingGenerator) {
    this.db = db;
    this.embeddings = embeddings;
  }

  async semanticSearch(query: string, options: SearchOptions = {}): Promise<SearchResult[]> {
    const limit = options.limit || this.config.search.defaultLimit;
    const minScore = options.minScore ?? this.config.search.minScore;

    const queryEmbedding = await this.embeddings.generateForChunk(query);
    const results = this.db.searchByVector(queryEmbedding, limit * 2);

    return results
      .filter((r) => r.score >= minScore)
      .slice(0, limit)
      .map((r) => ({ ...r, matchType: 'semantic' }));
  }

  async keywordSearch(query: string, options: SearchOptions = {}): Promise<SearchResult[]> {
    const limit = options.limit || this.config.search.defaultLimit;
    const results = this.db.searchByKeyword(query, limit);
    return results.map((r) => ({ ...r, matchType: 'keyword' }));
  }

  async hybridSearch(query: string, options: SearchOptions = {}): Promise<SearchResult[]> {
    const limit = options.limit || this.config.search.defaultLimit;
    const hybridWeight = this.config.search.hybridWeight;

    const [semanticResults, keywordResults] = await Promise.all([
      this.semanticSearch(query, { ...options, limit: limit * 2 }),
      this.keywordSearch(query, { ...options, limit: limit * 2 }),
    ]);

    const scoreMap = new Map<string, { score: number; result: SearchResult }>();

    semanticResults.forEach((result, idx) => {
      const rrfScore = 1.0 / (idx + 60);
      const current = scoreMap.get(result.skill.id);
      const combinedScore = current ? current.score : 0;
      scoreMap.set(result.skill.id, {
        score: combinedScore + rrfScore * hybridWeight,
        result,
      });
    });

    keywordResults.forEach((result, idx) => {
      const rrfScore = 1.0 / (idx + 60);
      const current = scoreMap.get(result.skill.id);
      const combinedScore = current ? current.score : 0;
      scoreMap.set(result.skill.id, {
        score: combinedScore + rrfScore * (1 - hybridWeight),
        result,
      });
    });

    const mergedResults = Array.from(scoreMap.entries())
      .sort((a, b) => b[1].score - a[1].score)
      .slice(0, limit)
      .map(([_, { result, score }]) => ({
        ...result,
        score,
        matchType: 'hybrid' as const,
      }));

    return mergedResults;
  }

  async recommendForTask(
    taskDescription: string,
    options: RecommendOptions = {}
  ): Promise<Recommendation[]> {
    const limit = options.limit || 5;
    const includeSet = options.includeSkills ? new Set(options.includeSkills) : null;
    const excludeSet = options.excludeSkills ? new Set(options.excludeSkills) : null;

    const searchResults = await this.hybridSearch(taskDescription, { limit: limit * 2 });

    const filteredResults = searchResults.filter((r) => {
      if (includeSet && !includeSet.has(r.skill.id)) return false;
      if (excludeSet && excludeSet.has(r.skill.id)) return false;
      return true;
    });

    return filteredResults.slice(0, limit).map((result) => ({
      skill: result.skill,
      score: result.score,
      reason: this.generateRecommendationReason(result, taskDescription),
    }));
  }

  async findSimilar(skillId: string, limit: number = 5): Promise<SearchResult[]> {
    const skill = this.db.getSkill(skillId);
    if (!skill) {
      return [];
    }

    const results = await this.semanticSearch(skill.name + ' ' + skill.description, { limit: limit + 1 });
    return results.filter((r) => r.skill.id !== skillId).slice(0, limit);
  }

  private generateRecommendationReason(result: SearchResult, taskDescription: string): string {
    const reasons: string[] = [];

    if (result.matchType === 'semantic' || result.matchType === 'hybrid') {
      if (result.score > 0.8) {
        reasons.push('高度语义匹配');
      } else if (result.score > 0.6) {
        reasons.push('良好语义匹配');
      }
    }

    if (result.matchType === 'keyword') {
      reasons.push('关键词匹配');
    }

    if (!reasons.length) {
      reasons.push('基于任务内容推荐');
    }

    return reasons.join('，');
  }
}

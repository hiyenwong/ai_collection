import Database from 'better-sqlite3';
import * as sqlite_vss from 'sqlite-vss';
import * as path from 'path';
import { Skill, SearchResult } from '../types/index.js';

export class SkillDatabase {
  private db: Database.Database;
  private dbPath: string;

  constructor(dbPath: string = './skills-index.db') {
    this.dbPath = dbPath;
    this.db = new Database(dbPath);
    sqlite_vss.load(this.db);
    this.db.pragma('journal_mode = WAL');
  }

  initialize(): void {
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS skills (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        path TEXT NOT NULL,
        content_hash TEXT NOT NULL,
        created_at INTEGER NOT NULL,
        updated_at INTEGER NOT NULL,
        metadata TEXT NOT NULL
      );

      CREATE TABLE IF NOT EXISTS skill_chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skill_id TEXT NOT NULL,
        chunk_type TEXT NOT NULL,
        content TEXT NOT NULL,
        chunk_index INTEGER NOT NULL,
        FOREIGN KEY (skill_id) REFERENCES skills(id)
      );

      CREATE INDEX IF NOT EXISTS idx_chunks_skill_id ON skill_chunks(skill_id);
    `);

    const dimension = this.getVectorDimension();
    this.db.exec(`
      CREATE VIRTUAL TABLE IF NOT EXISTS vss_skills
      USING vss0(embedding(${dimension}));

      CREATE VIRTUAL TABLE IF NOT EXISTS vss_chunks
      USING vss0(embedding(${dimension}));

      CREATE VIRTUAL TABLE IF NOT EXISTS fts_skills
      USING fts5(
        name,
        description,
        instructions,
        activation_keywords,
        content = skills,
        content_rowid = rowid
      );
    `);
  }

  private getVectorDimension(): number {
    const provider = process.env.EMBEDDING_PROVIDER || 'openai';
    if (provider === 'cohere') return 1024;
    const model = process.env.EMBEDDING_MODEL || 'text-embedding-3-small';
    return model.includes('large') ? 3072 : 1536;
  }

  insertSkill(skill: Skill, embedding: number[]): void {
    const insertSkill = this.db.prepare(`
      INSERT INTO skills (
        id, name, description, path, content_hash, created_at, updated_at, metadata
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      ON CONFLICT(id) DO UPDATE SET
        name = excluded.name,
        description = excluded.description,
        path = excluded.path,
        content_hash = excluded.content_hash,
        updated_at = excluded.updated_at,
        metadata = excluded.metadata
    `);

    const result = insertSkill.run(
      skill.id,
      skill.name,
      skill.description,
      skill.path,
      skill.contentHash,
      skill.metadata.createdAt.getTime(),
      skill.metadata.updatedAt.getTime(),
      JSON.stringify(skill.metadata)
    );

    const rowid = result.lastInsertRowid;

    this.insertSkillVector(Number(rowid), embedding);
    this.updateFts(Number(rowid), skill);
  }

  private insertSkillVector(rowid: number, embedding: number[]): void {
    const deleteOld = this.db.prepare(`
      DELETE FROM vss_skills WHERE rowid = (
        SELECT rowid FROM skills WHERE id = (SELECT id FROM skills WHERE rowid = ?)
      )
    `);
    deleteOld.run(rowid);

    const insertVss = this.db.prepare(`
      INSERT INTO vss_skills (rowid, embedding) VALUES (?, ?)
    `);
    insertVss.run(rowid, JSON.stringify(embedding));
  }

  private updateFts(rowid: number, skill: Skill): void {
    const deleteFts = this.db.prepare(`
      DELETE FROM fts_skills WHERE rowid = ?
    `);
    deleteFts.run(rowid);

    const insertFts = this.db.prepare(`
      INSERT INTO fts_skills (rowid, name, description, instructions, activation_keywords)
      VALUES (?, ?, ?, ?, ?)
    `);
    insertFts.run(
      rowid,
      skill.name,
      skill.description,
      skill.instructions,
      skill.activationKeywords.join(', ')
    );
  }

  getSkill(id: string): Skill | null {
    const stmt = this.db.prepare('SELECT * FROM skills WHERE id = ?');
    const row = stmt.get(id) as any;

    if (!row) return null;

    return {
      id: row.id,
      name: row.name,
      description: row.description,
      activationKeywords: [],
      toolsUsed: [],
      instructions: '',
      contentHash: row.content_hash,
      path: row.path,
      metadata: JSON.parse(row.metadata),
    };
  }

  getAllSkills(): Skill[] {
    const stmt = this.db.prepare('SELECT * FROM skills ORDER BY name');
    const rows = stmt.all() as any[];

    return rows.map((row) => ({
      id: row.id,
      name: row.name,
      description: row.description,
      activationKeywords: [],
      toolsUsed: [],
      instructions: '',
      contentHash: row.content_hash,
      path: row.path,
      metadata: JSON.parse(row.metadata),
    }));
  }

  deleteSkill(id: string): void {
    const getRowid = this.db.prepare('SELECT rowid FROM skills WHERE id = ?');
    const row = getRowid.get(id) as any;

    if (row) {
      const deleteVss = this.db.prepare('DELETE FROM vss_skills WHERE rowid = ?');
      deleteVss.run(row.rowid);

      const deleteFts = this.db.prepare('DELETE FROM fts_skills WHERE rowid = ?');
      deleteFts.run(row.rowid);

      const deleteChunks = this.db.prepare('DELETE FROM skill_chunks WHERE skill_id = ?');
      deleteChunks.run(id);

      const deleteSkill = this.db.prepare('DELETE FROM skills WHERE id = ?');
      deleteSkill.run(id);
    }
  }

  searchByVector(embedding: number[], limit: number = 10): SearchResult[] {
    const search = this.db.prepare(`
      SELECT
        skills.*,
        vss_skills.distance
      FROM vss_skills
      JOIN skills ON vss_skills.rowid = skills.rowid
      WHERE vss_search(vss_skills.embedding, vss_query_embedding(?))
      ORDER BY distance ASC
      LIMIT ?
    `);

    const rows = search.all(JSON.stringify(embedding), limit) as any[];

    return rows.map((row) => ({
      skill: {
        id: row.id,
        name: row.name,
        description: row.description,
        activationKeywords: [],
        toolsUsed: [],
        instructions: '',
        contentHash: row.content_hash,
        path: row.path,
        metadata: JSON.parse(row.metadata),
      },
      score: Math.max(0, 1 - row.distance),
      distance: row.distance,
      matchType: 'semantic',
    }));
  }

  searchByKeyword(query: string, limit: number = 10): SearchResult[] {
    const search = this.db.prepare(`
      SELECT
        skills.*,
        rank
      FROM fts_skills
      JOIN skills ON fts_skills.rowid = skills.rowid
      WHERE fts_skills MATCH ?
      ORDER BY rank ASC
      LIMIT ?
    `);

    const rows = search.all(query, limit) as any[];

    return rows.map((row, idx) => ({
      skill: {
        id: row.id,
        name: row.name,
        description: row.description,
        activationKeywords: [],
        toolsUsed: [],
        instructions: '',
        contentHash: row.content_hash,
        path: row.path,
        metadata: JSON.parse(row.metadata),
      },
      score: 1 - idx / rows.length,
      distance: idx / rows.length,
      matchType: 'keyword',
    }));
  }

  getSkillContentHash(id: string): string | null {
    const stmt = this.db.prepare('SELECT content_hash FROM skills WHERE id = ?');
    const row = stmt.get(id) as any;
    return row?.content_hash || null;
  }

  getIndexStats(): { totalSkills: number; lastUpdated: Date | null } {
    const countStmt = this.db.prepare('SELECT COUNT(*) as count FROM skills');
    const countRow = countStmt.get() as any;

    const updatedStmt = this.db.prepare('SELECT MAX(updated_at) as max_updated FROM skills');
    const updatedRow = updatedStmt.get() as any;

    return {
      totalSkills: countRow.count,
      lastUpdated: updatedRow.max_updated ? new Date(updatedRow.max_updated) : null,
    };
  }

  close(): void {
    this.db.close();
  }
}

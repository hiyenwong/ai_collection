import * as fs from 'fs';
import * as path from 'path';
import { Skill, IndexResult } from '../types/index.js';
import { SkillDatabase } from './database.js';
import { SkillParser } from './parser.js';
import { EmbeddingGenerator } from './embeddings.js';

export class SkillIndexer {
  private db: SkillDatabase;
  private parser: SkillParser;
  private embeddings: EmbeddingGenerator;
  private skillsRoot: string;

  constructor(
    db: SkillDatabase,
    parser: SkillParser,
    embeddings: EmbeddingGenerator,
    skillsRoot: string = '../../collection/skills'
  ) {
    this.db = db;
    this.parser = parser;
    this.embeddings = embeddings;
    this.skillsRoot = path.resolve(skillsRoot);
  }

  async buildFullIndex(force: boolean = false, verbose: boolean = false): Promise<IndexResult> {
    const startTime = Date.now();
    const errors: string[] = [];
    let indexed = 0;
    let skipped = 0;

    if (force) {
      const allSkills = this.db.getAllSkills();
      for (const skill of allSkills) {
        this.db.deleteSkill(skill.id);
      }
    }

    const skillIds = this.discoverSkills();
    const totalSkills = skillIds.length;

    if (verbose) {
      console.log(`Found ${totalSkills} skills in ${this.skillsRoot}`);
    }

    for (const skillId of skillIds) {
      try {
        const skillPath = path.join(this.skillsRoot, skillId);
        const skill = await this.parser.parse(skillPath);

        const existingHash = this.db.getSkillContentHash(skill.id);
        if (!force && existingHash === skill.contentHash) {
          skipped++;
          if (verbose) console.log(`Skipping ${skillId} (unchanged)`);
          continue;
        }

        const embedding = await this.embeddings.generateForSkill(skill);
        this.db.insertSkill(skill, embedding);
        indexed++;

        if (verbose) console.log(`Indexed ${skillId}`);
      } catch (error) {
        const msg = `Failed to index ${skillId}: ${(error as Error).message}`;
        errors.push(msg);
        if (verbose) console.error(msg);
      }
    }

    return {
      totalSkills,
      indexed,
      updated: 0,
      skipped,
      errors,
      duration: Date.now() - startTime,
    };
  }

  async updateIndex(verbose: boolean = false): Promise<IndexResult> {
    const startTime = Date.now();
    const errors: string[] = [];
    let indexed = 0;
    let updated = 0;
    let skipped = 0;

    const skillIds = this.discoverSkills();
    const totalSkills = skillIds.length;

    const existingSkills = new Set(this.db.getAllSkills().map((s) => s.id));

    if (verbose) {
      console.log(`Found ${totalSkills} skills, ${existingSkills.size} existing`);
    }

    for (const skillId of skillIds) {
      try {
        const skillPath = path.join(this.skillsRoot, skillId);
        const skill = await this.parser.parse(skillPath);

        const existingHash = this.db.getSkillContentHash(skill.id);

        if (!existingHash) {
          const embedding = await this.embeddings.generateForSkill(skill);
          this.db.insertSkill(skill, embedding);
          indexed++;
          if (verbose) console.log(`Indexed new skill: ${skillId}`);
        } else if (existingHash !== skill.contentHash) {
          const embedding = await this.embeddings.generateForSkill(skill);
          this.db.insertSkill(skill, embedding);
          updated++;
          if (verbose) console.log(`Updated skill: ${skillId}`);
        } else {
          skipped++;
        }

        existingSkills.delete(skillId);
      } catch (error) {
        const msg = `Failed to process ${skillId}: ${(error as Error).message}`;
        errors.push(msg);
        if (verbose) console.error(msg);
      }
    }

    for (const deletedId of existingSkills) {
      this.db.deleteSkill(deletedId);
      if (verbose) console.log(`Removed deleted skill: ${deletedId}`);
    }

    return {
      totalSkills,
      indexed,
      updated,
      skipped,
      errors,
      duration: Date.now() - startTime,
    };
  }

  async indexSkill(skillId: string): Promise<void> {
    const skillPath = path.join(this.skillsRoot, skillId);
    if (!fs.existsSync(skillPath)) {
      throw new Error(`Skill not found: ${skillId}`);
    }

    const skill = await this.parser.parse(skillPath);
    const embedding = await this.embeddings.generateForSkill(skill);
    this.db.insertSkill(skill, embedding);
  }

  private discoverSkills(): string[] {
    if (!fs.existsSync(this.skillsRoot)) {
      return [];
    }

    return fs
      .readdirSync(this.skillsRoot, { withFileTypes: true })
      .filter((dirent) => dirent.isDirectory())
      .filter((dirent) => {
        const skillMdPath = path.join(this.skillsRoot, dirent.name, 'SKILL.md');
        return fs.existsSync(skillMdPath);
      })
      .map((dirent) => dirent.name);
  }
}

import * as fs from 'fs';
import * as path from 'path';
import { Skill, SkillMetadata, ToolUsage } from '../types/index.js';
import { parseMarkdownSections, computeContentHash } from '../utils/markdown.js';

export class SkillParser {
  async parse(skillPath: string): Promise<Skill> {
    const skillMdPath = path.join(skillPath, 'SKILL.md');
    if (!fs.existsSync(skillMdPath)) {
      throw new Error(`SKILL.md not found at ${skillMdPath}`);
    }

    const content = fs.readFileSync(skillMdPath, 'utf-8');
    return this.parseMarkdown(content, skillPath);
  }

  parseMarkdown(content: string, skillPath: string): Skill {
    const sections = parseMarkdownSections(content);
    const sectionNames = sections.map((s) => s.heading);

    const id = path.basename(skillPath);
    const now = new Date();

    const skill: Skill = {
      id,
      name: this.parseName(sections) || id,
      description: this.parseDescription(sections) || '',
      activationKeywords: this.parseActivationKeywords(sections),
      toolsUsed: this.parseToolsUsed(sections),
      instructions: this.parseInstructions(sections),
      contentHash: computeContentHash(content),
      path: skillPath,
      metadata: {
        createdAt: now,
        updatedAt: now,
        sections: sectionNames,
      },
    };

    return skill;
  }

  private parseName(sections: ReturnType<typeof parseMarkdownSections>): string | null {
    const titleSection = sections.find((s) => s.level === 1);
    return titleSection?.heading || null;
  }

  private parseDescription(sections: ReturnType<typeof parseMarkdownSections>): string | null {
    const descSection = sections.find(
      (s) => s.level === 2 && s.heading.toLowerCase() === 'description'
    );
    return descSection?.content.trim() || null;
  }

  private parseActivationKeywords(sections: ReturnType<typeof parseMarkdownSections>): string[] {
    const keywordsSection = sections.find(
      (s) => s.level === 2 && s.heading.toLowerCase().includes('activation keyword')
    );

    if (!keywordsSection) {
      return [];
    }

    const keywords: string[] = [];
    const lines = keywordsSection.content.split('\n');

    for (const line of lines) {
      const match = line.match(/^[-*]\s*(.+)$/);
      if (match) {
        keywords.push(match[1].trim());
      }
    }

    return keywords;
  }

  private parseToolsUsed(sections: ReturnType<typeof parseMarkdownSections>): ToolUsage[] {
    const toolsSection = sections.find(
      (s) => s.level === 2 && s.heading.toLowerCase() === 'tools used'
    );

    if (!toolsSection) {
      return [];
    }

    const tools: ToolUsage[] = [];
    const lines = toolsSection.content.split('\n');

    for (const line of lines) {
      const match = line.match(/^[-*]\s*([^:]+):\s*(.+)$/);
      if (match) {
        tools.push({
          tool: match[1].trim(),
          description: match[2].trim(),
        });
      }
    }

    return tools;
  }

  private parseInstructions(sections: ReturnType<typeof parseMarkdownSections>): string {
    const instrSection = sections.find(
      (s) => s.level === 2 && s.heading.toLowerCase().includes('instruction')
    );

    return instrSection?.content.trim() || '';
  }
}

import { marked } from 'marked';
import * as crypto from 'crypto';

export interface MarkdownSection {
  level: number;
  heading: string;
  content: string;
}

export function parseMarkdownSections(content: string): MarkdownSection[] {
  const sections: MarkdownSection[] = [];
  const lines = content.split('\n');
  let currentSection: MarkdownSection | null = null;

  for (const line of lines) {
    const headingMatch = line.match(/^(#{1,6})\s+(.+)$/);
    if (headingMatch) {
      if (currentSection) {
        sections.push(currentSection);
      }
      currentSection = {
        level: headingMatch[1].length,
        heading: headingMatch[2].trim(),
        content: '',
      };
    } else if (currentSection) {
      currentSection.content += (currentSection.content ? '\n' : '') + line;
    }
  }

  if (currentSection) {
    sections.push(currentSection);
  }

  return sections;
}

export function extractTextFromMarkdown(content: string): string {
  const renderer = new marked.Renderer();
  renderer.text = (text) => text;
  renderer.link = (_href, _title, text) => text;
  renderer.image = (_href, _title, text) => text || '';
  renderer.listitem = (text) => `${text}\n`;
  renderer.paragraph = (text) => `${text}\n`;
  renderer.codespan = (code) => code;
  renderer.code = (code, _lang) => code;

  return marked.parse(content, { renderer }).toString().trim();
}

export function computeContentHash(content: string): string {
  return crypto.createHash('sha256').update(content).digest('hex');
}

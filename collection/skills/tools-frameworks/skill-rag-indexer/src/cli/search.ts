import { SkillDatabase } from '../core/database.js';
import { EmbeddingGenerator, createEmbeddingProvider } from '../core/embeddings.js';
import { SkillSearcher } from '../core/searcher.js';
import { getConfig } from '../utils/config.js';

interface SearchOptions {
  keyword?: boolean;
  semantic?: boolean;
  hybrid?: boolean;
  limit?: string;
  minScore?: string;
}

export async function searchCommand(query: string, options: SearchOptions): Promise<void> {
  const config = getConfig();

  const db = new SkillDatabase(config.databasePath);
  db.initialize();

  try {
    const provider = createEmbeddingProvider();
    const embeddings = new EmbeddingGenerator(provider);
    const searcher = new SkillSearcher(db, embeddings);

    const searchOptions = {
      limit: options.limit ? parseInt(options.limit, 10) : undefined,
      minScore: options.minScore ? parseFloat(options.minScore) : undefined,
    };

    let results;

    if (options.keyword) {
      results = await searcher.keywordSearch(query, searchOptions);
    } else if (options.hybrid) {
      results = await searcher.hybridSearch(query, searchOptions);
    } else {
      results = await searcher.semanticSearch(query, searchOptions);
    }

    console.log(`\n=== Search Results for "${query}" ===\n`);

    if (results.length === 0) {
      console.log('No results found.');
      return;
    }

    results.forEach((result, idx) => {
      const scorePct = (result.score * 100).toFixed(1);
      const icon = result.score > 0.8 ? '🟢' : result.score > 0.6 ? '🟡' : '⚪';

      console.log(`${idx + 1}. ${icon} ${result.skill.name} [${scorePct}%]`);
      console.log(`   ID: ${result.skill.id}`);
      console.log(`   Path: ${result.skill.path}`);
      if (result.skill.description) {
        const desc = result.skill.description.slice(0, 150);
        console.log(`   ${desc}${result.skill.description.length > 150 ? '...' : ''}`);
      }
      console.log();
    });
  } finally {
    db.close();
  }
}

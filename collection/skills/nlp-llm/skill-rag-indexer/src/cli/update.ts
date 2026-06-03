import { SkillDatabase } from '../core/database.js';
import { SkillParser } from '../core/parser.js';
import { EmbeddingGenerator, createEmbeddingProvider } from '../core/embeddings.js';
import { SkillIndexer } from '../core/indexer.js';
import { getConfig } from '../utils/config.js';

interface UpdateOptions {
  verbose?: boolean;
}

export async function updateCommand(options: UpdateOptions): Promise<void> {
  const config = getConfig();
  const verbose = options.verbose ?? false;

  if (verbose) {
    console.log('Initializing database...');
  }
  const db = new SkillDatabase(config.databasePath);
  db.initialize();

  try {
    const provider = createEmbeddingProvider();
    const embeddings = new EmbeddingGenerator(provider);
    const parser = new SkillParser();
    const indexer = new SkillIndexer(db, parser, embeddings, config.skillsRoot);

    if (verbose) {
      console.log('Updating index...');
    }

    const result = await indexer.updateIndex(verbose);

    console.log('\n=== Index Update Complete ===');
    console.log(`Total skills found: ${result.totalSkills}`);
    console.log(`Newly indexed: ${result.indexed}`);
    console.log(`Updated: ${result.updated}`);
    console.log(`Skipped (unchanged): ${result.skipped}`);
    console.log(`Duration: ${(result.duration / 1000).toFixed(2)}s`);

    if (result.errors.length > 0) {
      console.log(`\nErrors (${result.errors.length}):`);
      result.errors.forEach((err) => console.log(`  - ${err}`));
    }
  } finally {
    db.close();
  }
}

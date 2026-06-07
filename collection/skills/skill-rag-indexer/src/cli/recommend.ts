import { SkillDatabase } from '../core/database.js';
import { EmbeddingGenerator, createEmbeddingProvider } from '../core/embeddings.js';
import { SkillSearcher } from '../core/searcher.js';
import { getConfig } from '../utils/config.js';

interface RecommendOptions {
  limit?: string;
  include?: string;
  exclude?: string;
}

export async function recommendCommand(task: string, options: RecommendOptions): Promise<void> {
  const config = getConfig();

  const db = new SkillDatabase(config.databasePath);
  db.initialize();

  try {
    const provider = createEmbeddingProvider();
    const embeddings = new EmbeddingGenerator(provider);
    const searcher = new SkillSearcher(db, embeddings);

    const recommendOptions = {
      limit: options.limit ? parseInt(options.limit, 10) : undefined,
      includeSkills: options.include ? options.include.split(',') : undefined,
      excludeSkills: options.exclude ? options.exclude.split(',') : undefined,
    };

    const recommendations = await searcher.recommendForTask(task, recommendOptions);

    console.log(`\n=== Skill Recommendations for Task ===`);
    console.log(`Task: "${task}"\n`);

    if (recommendations.length === 0) {
      console.log('No recommendations found.');
      return;
    }

    recommendations.forEach((rec, idx) => {
      const scorePct = (rec.score * 100).toFixed(1);
      const icon = rec.score > 0.8 ? '⭐' : rec.score > 0.6 ? '👍' : '•';

      console.log(`${idx + 1}. ${icon} ${rec.skill.name} [${scorePct}%]`);
      console.log(`   ID: ${rec.skill.id}`);
      console.log(`   Reason: ${rec.reason}`);
      if (rec.skill.description) {
        const desc = rec.skill.description.slice(0, 200);
        console.log(`   ${desc}${rec.skill.description.length > 200 ? '...' : ''}`);
      }
      console.log();
    });
  } finally {
    db.close();
  }
}

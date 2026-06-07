import { SkillDatabase } from '../core/database.js';
import { getConfig } from '../utils/config.js';

export async function statusCommand(): Promise<void> {
  const config = getConfig();

  const db = new SkillDatabase(config.databasePath);

  try {
    const stats = db.getIndexStats();
    const skills = db.getAllSkills();

    console.log('\n=== Skill RAG Index Status ===\n');
    console.log(`Database: ${config.databasePath}`);
    console.log(`Total skills: ${stats.totalSkills}`);
    console.log(`Embedding provider: ${config.embeddingsProvider}`);
    console.log(`Embedding model: ${config.embeddingsModel}`);
    console.log(`Skills root: ${config.skillsRoot}`);

    if (stats.lastUpdated) {
      console.log(`Last updated: ${stats.lastUpdated.toLocaleString()}`);
    }

    if (skills.length > 0) {
      console.log('\nIndexed skills:');
      skills.forEach((skill, idx) => {
        console.log(`  ${idx + 1}. ${skill.name} (${skill.id})`);
      });
    }

    console.log();
  } finally {
    db.close();
  }
}

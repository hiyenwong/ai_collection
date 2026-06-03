#!/usr/bin/env node
/**
 * Chat History LanceDB - CLI Entry Point
 */

import { Command } from 'commander';
import { loadConfig } from './utils/config.js';
import { ChatHistoryDatabase } from './core/database.js';
import { createEmbeddingProvider } from './core/embeddings.js';

const program = new Command();

program
  .name('chat-history')
  .description('Chat history database using LanceDB')
  .version('1.0.0');

// Global options
program.option('--db-path <path>', 'Path to LanceDB database');
program.option('--env-file <path>', 'Path to .env file');

// Initialize database
async function init() {
  const config = loadConfig();
  const dbPath = program.opts().dbPath || config.database.db_path;

  const db = new ChatHistoryDatabase({
    dbPath,
    vectorDimension: config.embedding.vector_dimension,
  });

  await db.initialize();

  let embeddingProvider = null;
  try {
    embeddingProvider = createEmbeddingProvider(config.embedding);
  } catch (err) {
    console.warn('Embedding provider not configured:', (err as Error).message);
  }

  return { db, embeddingProvider, config };
}

// ============ Commands ============

// Save command
program
  .command('save')
  .description('Save a message')
  .requiredOption('--session <id>', 'Session ID')
  .requiredOption('--role <role>', 'Role (user/assistant/system/tool)')
  .requiredOption('--content <text>', 'Message content')
  .option('--no-embedding', 'Skip embedding generation')
  .action(async (options) => {
    const { db, embeddingProvider } = await init();
    const { ChatRepository } = await import('./core/repository.js');
    const repo = new ChatRepository(db, embeddingProvider);

    const messageId = await repo.saveMessage(
      {
        session_id: options.session,
        role: options.role,
        content: options.content,
      },
      options.embedding !== false
    );

    console.log(`Message saved: ${messageId}`);
  });

// Search command
program
  .command('search <query>')
  .description('Search chat history')
  .option('--semantic', 'Use semantic search')
  .option('--keyword', 'Use keyword search')
  .option('--session <id>', 'Filter by session')
  .option('--limit <n>', 'Limit results', '10')
  .option('--min-score <score>', 'Minimum score', '0.5')
  .action(async (query, options) => {
    const { db, embeddingProvider } = await init();

    let mode: any = 'hybrid';
    if (options.semantic) mode = 'semantic';
    if (options.keyword) mode = 'keyword';

    if (embeddingProvider && mode !== 'keyword') {
      const { ChatSearcher } = await import('./core/searcher.js');
      const searcher = new ChatSearcher(db, embeddingProvider as any);

      const results = await searcher.search(query, {
        mode,
        session_id: options.session,
        limit: parseInt(options.limit, 10),
        min_score: parseFloat(options.minScore),
      });

      console.log(`Found ${results.length} results:`);
      for (const result of results as any[]) {
        console.log(`\n[${(result.score * 100).toFixed(0)}%] ${result.message.role}: ${result.message.content.slice(0, 100)}...`);
      }
    } else {
      const results = await db.searchByKeyword(query, {
        session_id: options.session,
        limit: parseInt(options.limit, 10),
        min_score: parseFloat(options.minScore),
      });

      console.log(`Found ${results.length} results:`);
      for (const result of results) {
        console.log(`\n[${(result.score * 100).toFixed(0)}%] ${result.message.role}: ${result.message.content.slice(0, 100)}...`);
      }
    }
  });

// List commands
const listCommand = program.command('list').description('List resources');

listCommand
  .command('sessions')
  .description('List sessions')
  .option('--limit <n>', 'Limit results', '50')
  .option('--offset <n>', 'Offset', '0')
  .action(async (options) => {
    const { db } = await init();
    const sessions = await db.listSessions(
      parseInt(options.limit, 10),
      parseInt(options.offset, 10)
    );

    console.log(`Sessions (${sessions.length}):`);
    for (const session of sessions) {
      console.log(`- ${session.session_id} - ${session.title}`);
    }
  });

listCommand
  .command('messages')
  .description('List messages in a session')
  .requiredOption('--session <id>', 'Session ID')
  .option('--limit <n>', 'Limit results', '100')
  .option('--offset <n>', 'Offset', '0')
  .action(async (options) => {
    const { db } = await init();
    const messages = await db.getSessionMessages(
      options.session,
      parseInt(options.limit, 10),
      parseInt(options.offset, 10)
    );

    console.log(`Messages (${messages.length}):`);
    for (const msg of messages) {
      const time = new Date(msg.timestamp).toISOString();
      console.log(`[${time}] ${msg.role}: ${msg.content.slice(0, 80)}...`);
    }
  });

// Session commands
const sessionCommand = program.command('session').description('Session management');

sessionCommand
  .command('create [title]')
  .description('Create a new session')
  .action(async (title) => {
    const { db } = await init();
    const { SessionManager } = await import('./core/session-manager.js');
    const manager = new SessionManager(db);
    const sessionId = await manager.createSession(title);
    console.log(`Session created: ${sessionId}`);
  });

sessionCommand
  .command('rename <id> <title>')
  .description('Rename a session')
  .action(async (id, title) => {
    const { db } = await init();
    const { SessionManager } = await import('./core/session-manager.js');
    const manager = new SessionManager(db);
    await manager.renameSession(id, title);
    console.log(`Session renamed`);
  });

// Export command
program
  .command('export')
  .description('Export a session')
  .argument('<id>', 'Session ID')
  .option('--format <format>', 'Output format (json/markdown)', 'json')
  .option('--output <path>', 'Output file path')
  .action(async (id, options) => {
    const { db } = await init();
    const { ChatExporter } = await import('./core/exporter.js');
    const exporter = new ChatExporter(db);
    const content = await exporter.exportSession(id, options.format as any);
    console.log(content);
  });

// Stats command
program
  .command('stats')
  .description('Get statistics')
  .option('--session <id>', 'Session ID (optional)')
  .option('--detailed', 'Detailed stats')
  .action(async (options) => {
    const { db } = await init();
    if (options.session) {
      const { SessionManager } = await import('./core/session-manager.js');
      const manager = new SessionManager(db);
      const stats = await manager.getSessionStats(options.session);
      console.log('Session Stats:', JSON.stringify(stats, null, 2));
    } else {
      const stats = await db.getStats();
      console.log('Database Stats:', JSON.stringify(stats, null, 2));
    }
  });

// RAG command
program
  .command('rag <query>')
  .description('RAG context retrieval')
  .option('--session <id>', 'Session ID (optional)')
  .option('--limit <n>', 'Limit results', '10')
  .option('--format <format>', 'Output format (text/json)', 'text')
  .action(async (query, options) => {
    const { db, embeddingProvider } = await init();
    if (!embeddingProvider) {
      console.error('Embedding provider required for RAG');
      process.exit(1);
    }

    const { ChatSearcher } = await import('./core/searcher.js');
    const searcher = new ChatSearcher(db, embeddingProvider);

    const prompt = await searcher.buildContextPrompt(query, {
      limit: parseInt(options.limit, 10),
      session_id: options.session,
      format: options.format as any,
      include_timestamps: true,
    });

    console.log(prompt);
  });

// Parse and run
program.parseAsync().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});

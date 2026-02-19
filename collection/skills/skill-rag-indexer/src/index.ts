#!/usr/bin/env node

import 'dotenv/config';
import { Command } from 'commander';
import { buildCommand } from './cli/build.js';
import { searchCommand } from './cli/search.js';
import { recommendCommand } from './cli/recommend.js';
import { updateCommand } from './cli/update.js';
import { statusCommand } from './cli/status.js';

const program = new Command();

program
  .name('skill-rag')
  .description('Skill RAG Indexer - Semantic search and recommendation for OpenClaw skills')
  .version('1.0.0');

const indexCmd = program.command('index').description('Index management commands');

indexCmd
  .command('build')
  .description('Build full skill index')
  .option('-f, --force', 'Force rebuild even if index exists')
  .option('-v, --verbose', 'Verbose output')
  .action(buildCommand);

indexCmd
  .command('update')
  .description('Update index with changed skills')
  .option('-v, --verbose', 'Verbose output')
  .action(updateCommand);

indexCmd.command('status').description('Show index status').action(statusCommand);

program
  .command('search <query>')
  .description('Search skills')
  .option('-k, --keyword', 'Keyword search only')
  .option('-s, --semantic', 'Semantic search only (default)')
  .option('-y, --hybrid', 'Hybrid search')
  .option('-l, --limit <number>', 'Number of results', '10')
  .option('--min-score <number>', 'Minimum score threshold')
  .action(searchCommand);

program
  .command('recommend <task>')
  .description('Recommend skills for a task')
  .option('-l, --limit <number>', 'Number of recommendations', '5')
  .option('--include <skills>', 'Include only these skills (comma-separated)')
  .option('--exclude <skills>', 'Exclude these skills (comma-separated)')
  .action(recommendCommand);

program.parse();

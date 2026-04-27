#!/usr/bin/env node
import { readFileSync, copyFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const pkgRoot = join(__dirname, '..');

const index = JSON.parse(readFileSync(join(pkgRoot, 'skills.json'), 'utf8'));

function allSkills() {
  const skills = [];
  for (const group of ['primary_sections', 'companion_skills', 'framework_subskills']) {
    for (const s of index[group] ?? []) skills.push(s);
  }
  return skills;
}

function findSkill(id) {
  return allSkills().find(s => s.id === id);
}

const [,, cmd, ...args] = process.argv;

if (!cmd || cmd === 'help' || cmd === '--help' || cmd === '-h') {
  console.log(`miii-security — AI security skill packs for Claude Code

Usage:
  npx miii-security list              list all available skills
  npx miii-security add <skill-id>    copy skill into .claude/skills/<skill-id>/SKILL.md
  npx miii-security show <skill-id>   print skill content to stdout
`);
  process.exit(0);
}

if (cmd === 'list') {
  const groups = [
    ['primary_sections', 'Core'],
    ['companion_skills', 'Companion'],
    ['framework_subskills', 'Framework'],
  ];
  for (const [key, label] of groups) {
    const entries = index[key] ?? [];
    if (entries.length) {
      console.log(`\n${label}:`);
      for (const s of entries) console.log(`  ${s.id}`);
    }
  }
  console.log('');
  process.exit(0);
}

if (cmd === 'show') {
  const id = args[0];
  if (!id) { console.error('Error: skill-id required'); process.exit(1); }
  const skill = findSkill(id);
  if (!skill) {
    console.error(`Error: unknown skill "${id}"\nRun "npx miii-security list" to see available skills`);
    process.exit(1);
  }
  process.stdout.write(readFileSync(join(pkgRoot, skill.path), 'utf8'));
  process.exit(0);
}

if (cmd === 'add') {
  const id = args[0];
  if (!id) { console.error('Error: skill-id required'); process.exit(1); }
  const skill = findSkill(id);
  if (!skill) {
    console.error(`Error: unknown skill "${id}"\nRun "npx miii-security list" to see available skills`);
    process.exit(1);
  }
  const destDir = join(process.cwd(), '.claude', 'skills', id);
  mkdirSync(destDir, { recursive: true });
  copyFileSync(join(pkgRoot, skill.path), join(destDir, 'SKILL.md'));
  console.log(`Added: .claude/skills/${id}/SKILL.md`);
  process.exit(0);
}

console.error(`Unknown command: ${cmd}\nRun "npx miii-security help" for usage`);
process.exit(1);

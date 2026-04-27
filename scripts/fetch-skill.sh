#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <skill-id>" >&2
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
skill_path="$repo_root/skills/$1/SKILL.md"

if [[ ! -f "$skill_path" ]]; then
  echo "skill not found: $1" >&2
  exit 1
fi

cat "$skill_path"

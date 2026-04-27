#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"

python3 - <<'PY' "$repo_root/skills.json"
import json
import sys
from pathlib import Path

data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

for group in ("primary_sections", "companion_skills", "framework_subskills"):
    for entry in data.get(group, []):
        print(entry["id"])
PY

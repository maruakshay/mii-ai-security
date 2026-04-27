#!/usr/bin/env python3
import json
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_JSON = REPO_ROOT / "skills.json"


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def skill_entries(data: dict):
    for group in ("primary_sections", "companion_skills", "framework_subskills"):
        for entry in data.get(group, []):
            yield group, entry


def validate_skill_file(path: Path) -> list[str]:
    errors = []
    if not path.is_file():
        return [f"missing skill file: {path.relative_to(REPO_ROOT)}"]

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"missing YAML frontmatter: {path.relative_to(REPO_ROOT)}")
    if "description:" not in text.split("---", 2)[1]:
        errors.append(f"missing skill description: {path.relative_to(REPO_ROOT)}")
    if re.search(r"^#\s+", text, flags=re.MULTILINE) is None:
        errors.append(f"missing top-level heading: {path.relative_to(REPO_ROOT)}")
    return errors


def main() -> int:
    data = load_json(SKILLS_JSON)
    errors = []
    seen_ids = set()

    for group, entry in skill_entries(data):
        skill_id = entry.get("id")
        skill_path = entry.get("path")
        if not skill_id:
            errors.append(f"{group}: entry missing id")
            continue
        if skill_id in seen_ids:
            errors.append(f"duplicate skill id: {skill_id}")
        seen_ids.add(skill_id)
        if not skill_path:
            errors.append(f"{group}/{skill_id}: entry missing path")
            continue
        path = REPO_ROOT / skill_path
        errors.extend(validate_skill_file(path))

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print(f"validated {len(seen_ids)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

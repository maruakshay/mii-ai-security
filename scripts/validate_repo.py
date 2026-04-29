#!/usr/bin/env python3
from datetime import date
import json
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_JSON = REPO_ROOT / "skills.json"
FIXTURES_DIR = REPO_ROOT / "tests" / "adversarial-fixtures"
ALLOWED_SEVERITIES = {"critical", "high", "medium", "low"}
REQUIRED_FIXTURE_FIELDS = {
    "id",
    "title",
    "category",
    "attack_surface",
    "prompt",
    "expected_behavior",
    "tags",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from exc


def skill_entries(data: dict):
    for group in (
        "primary_sections",
        "companion_skills",
        "framework_subskills",
        "attack_surface_skills",
        "infra_ops_skills",
        "compliance_governance_skills",
    ):
        for entry in data.get(group, []):
            yield group, entry


def parse_frontmatter(text: str) -> dict[str, str]:
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    frontmatter = {}
    for line in parts[1].splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def is_iso_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_controls(group: str, skill_id: str, controls: object) -> list[str]:
    errors = []
    if not isinstance(controls, list) or not controls:
        return [f"{group}/{skill_id}: entry missing controls"]

    seen_control_ids = set()
    for idx, control in enumerate(controls):
        if not isinstance(control, dict):
            errors.append(f"{group}/{skill_id}: control #{idx + 1} must be an object")
            continue

        control_id = control.get("id")
        title = control.get("title")
        severity = control.get("severity")

        if not control_id:
            errors.append(f"{group}/{skill_id}: control #{idx + 1} missing id")
        elif control_id in seen_control_ids:
            errors.append(f"{group}/{skill_id}: duplicate control id {control_id}")
        else:
            seen_control_ids.add(control_id)

        if not title:
            errors.append(f"{group}/{skill_id}: control {control_id or idx + 1} missing title")

        if severity not in ALLOWED_SEVERITIES:
            errors.append(
                f"{group}/{skill_id}: control {control_id or idx + 1} has invalid severity {severity!r}"
            )

    return errors


def validate_skill_file(path: Path, skill_id: str, expected_last_reviewed: str) -> list[str]:
    errors = []
    if not path.is_file():
        return [f"missing skill file: {path.relative_to(REPO_ROOT)}"]

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"missing YAML frontmatter: {path.relative_to(REPO_ROOT)}")

    frontmatter = parse_frontmatter(text)
    if frontmatter.get("name") != skill_id:
        errors.append(f"frontmatter name mismatch: {path.relative_to(REPO_ROOT)}")
    if "description" not in frontmatter:
        errors.append(f"missing skill description: {path.relative_to(REPO_ROOT)}")
    if not frontmatter.get("last_reviewed"):
        errors.append(f"missing skill last_reviewed: {path.relative_to(REPO_ROOT)}")
    elif not is_iso_date(frontmatter["last_reviewed"]):
        errors.append(f"invalid skill last_reviewed: {path.relative_to(REPO_ROOT)}")
    elif frontmatter["last_reviewed"] != expected_last_reviewed:
        errors.append(f"skill last_reviewed mismatch: {path.relative_to(REPO_ROOT)}")

    if re.search(r"^#\s+", text, flags=re.MULTILINE) is None:
        errors.append(f"missing top-level heading: {path.relative_to(REPO_ROOT)}")
    return errors


def validate_fixtures() -> list[str]:
    errors = []
    if not FIXTURES_DIR.is_dir():
        return [f"missing fixtures directory: {FIXTURES_DIR.relative_to(REPO_ROOT)}"]

    fixture_paths = sorted(FIXTURES_DIR.glob("*.json"))
    if len(fixture_paths) < 10:
        errors.append(
            f"expected at least 10 adversarial fixtures in {FIXTURES_DIR.relative_to(REPO_ROOT)}"
        )

    seen_ids = set()
    for path in fixture_paths:
        try:
            fixture = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}")
            continue

        missing_fields = sorted(REQUIRED_FIXTURE_FIELDS - set(fixture))
        if missing_fields:
            errors.append(
                f"{path.relative_to(REPO_ROOT)} missing fields: {', '.join(missing_fields)}"
            )
            continue

        fixture_id = fixture["id"]
        if fixture_id in seen_ids:
            errors.append(f"duplicate fixture id: {fixture_id}")
        seen_ids.add(fixture_id)

        tags = fixture.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(tag, str) for tag in tags):
            errors.append(f"{path.relative_to(REPO_ROOT)} has invalid tags")

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
        last_reviewed = entry.get("last_reviewed")
        if not last_reviewed:
            errors.append(f"{group}/{skill_id}: entry missing last_reviewed")
            continue
        if not is_iso_date(last_reviewed):
            errors.append(f"{group}/{skill_id}: invalid last_reviewed {last_reviewed!r}")

        errors.extend(validate_controls(group, skill_id, entry.get("controls")))
        path = REPO_ROOT / skill_path
        errors.extend(validate_skill_file(path, skill_id, last_reviewed))

    errors.extend(validate_fixtures())

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    print(f"validated {len(seen_ids)} skills and {len(list(FIXTURES_DIR.glob('*.json')))} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

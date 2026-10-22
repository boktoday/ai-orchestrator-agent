"""Create the student's work folder and progress file."""
import datetime as dt
import json
import pathlib
import shutil
import sys

TEMPLATES = pathlib.Path(__file__).resolve().parents[3] / "shared"
DEST = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path.home() / "ai-orchestrator")

FOLDERS = ["position", "language", "skills", "build", "connect", "automate", "guardrails"]


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for folder in FOLDERS:
        (DEST / folder).mkdir(parents=True, exist_ok=True)
    progress = DEST / "progress.json"
    if not progress.exists():
        data = {
            "student": "",
            "started": dt.date.today().isoformat(),
            "module": 1,
            "lesson": 1,
            "sealed": [],
            "artefacts": {},
            "notes": "",
        }
        progress.write_text(json.dumps(data, indent=2), encoding="utf-8")
    for name in ("rules-card.template.md", "skill-template.md"):
        src = TEMPLATES / name
        dst = DEST / name.replace(".template", "")
        if src.exists() and not dst.exists():
            shutil.copyfile(src, dst)
    print("work folder ready at", DEST)
    print("progress file:", progress)


if __name__ == "__main__":
    main()

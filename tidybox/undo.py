import json
import os
import shutil
from pathlib import Path
from pathlib import Path

TIDYBOX_DIR = Path.home() / ".tidybox"
UNDO_FILE = TIDYBOX_DIR / "undo.json"

def save_undo(moves: list):
    TIDYBOX_DIR.mkdir(parents=True, exist_ok=True)
    with open(UNDO_FILE, "w") as f:
        json.dump(moves, f, indent=2)

def undo_last():
    if not os.path.exists(UNDO_FILE):
        print("Nothing to undo.")
        return

    with open(UNDO_FILE) as f:
        moves = json.load(f)

    for move in moves:
        src = Path(move["from"])
        dest = Path(move["to"])
        if src.exists():
            shutil.move(str(src), str(dest))
            print(f"↩️  Restored: {src.name}")
        else:
            print(f"⚠️  File not found: {src.name}")

    os.remove(UNDO_FILE)
    print("Undo complete.")
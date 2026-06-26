import os
import shutil
from pathlib import Path
from tidybox.rules import get_folder_for
from tidybox.logger import log
from tidybox.undo import save_undo

def scan(directory: str):
    path = Path(directory)
    files = [f for f in path.iterdir() if f.is_file()]
    
    if not files:
        print("No files found.")
        return

    groups = {}
    for f in files:
        folder = get_folder_for(f.suffix)
        groups.setdefault(folder, []).append(f.name)

    for folder, names in groups.items():
        print(f"\n📁 {folder}/")
        for name in names:
            print(f"   {name}")

def clean(directory: str, dry_run: bool = False, recursive: bool = False):
    path = Path(directory)
    pattern = "**/*" if recursive else "*"
    files = [f for f in path.glob(pattern) if f.is_file()]

    if not files:
        print("No files to organize.")
        return

    moves = []  # for undo log

    for f in files:
        folder_name = get_folder_for(f.suffix)
        dest_dir = path / folder_name
        dest_file = dest_dir / f.name

        if dry_run:
            print(f"[DRY RUN] {f.name} → {folder_name}/")
        else:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(f), str(dest_file))
            moves.append({"from": str(dest_file), "to": str(f)})
            log(f"Moved: {f.name} → {folder_name}/")
            print(f"✅ {f.name} → {folder_name}/")

    if not dry_run and moves:
        save_undo(moves)
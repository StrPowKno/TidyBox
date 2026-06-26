import os
from datetime import datetime
from pathlib import Path

TIDYBOX_DIR = Path.home() / ".tidybox" / "logs"

def log(message: str):
    TIDYBOX_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = TIDYBOX_DIR / f"{today}.log"
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
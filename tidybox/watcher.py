import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tidybox.organizer import clean

class Handler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_created(self, event):
        if not event.is_directory:
            print(f"🔍 New file detected: {Path(event.src_path).name}")
            clean(self.directory)

def watch(directory: str):
    print(f"👀 Watching {directory} for new files... (Ctrl+C to stop)")
    handler = Handler(directory)
    observer = Observer()
    observer.schedule(handler, directory, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
import click
import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReloadHandler(FileSystemEventHandler):

    def __init__(self, restart):
        super().__init__()
        self.restart = restart
        self.last = 0

    def on_any_event(self, event):

        if not event.src_path.endswith(".py"):
            return

        now = time.time()
        if now - self.last < 0.5:
            return

        self.last = now
        print(f"Alteração detectada: {event.src_path}")
        self.restart()


@click.command()
@click.argument("app", default="main.py")
def dev(app):

    if os.environ.get("TERMINUI_WORKER") == "true":
        return

    worker = None

    def start_worker():
        nonlocal worker

        if worker:
            worker.terminate()
            worker.wait()
        
        print("Iniciando worker...")
        worker = subprocess.Popen(
            [sys.executable, app],
            env={**os.environ, "TERMINUI_WORKER": "true"}
        )

        start_worker()

        observer = Observer()
        handler = ReloadHandler(start_worker)

        observer.schedule(handler, os.getcwd(), recursive=True)
        observer.start()

        print("Modo dev ativo (hot reload)")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        if worker:
            worker.terminate()

        observer.join()

#AI made

import click
import os
import sys
import time
import subprocess
import threading
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
        if now - self.last < 1:
            return

        self.last = now
        print(f"\nAlteração detectada: {event.src_path}")
        self.restart()


@click.command()
@click.argument("app", default="main.py")
def dev(app):

    worker = None

    def stream_output(proc):
        for line in proc.stdout:
            print(line, end="")

    def start_worker():
        nonlocal worker

        if worker and worker.poll() is None:
            print("Parando worker...")
            worker.terminate()
            worker.wait()

        print("Iniciando worker...")

        worker = subprocess.Popen(
            [sys.executable, app],
            text=True,
            bufsize=1,
        )

        threading.Thread(
            target=stream_output,
            args=(worker,),
            daemon=True
        ).start()

    start_worker()

    observer = Observer()
    handler = ReloadHandler(start_worker)

    observer.schedule(handler, os.getcwd(), recursive=True)
    observer.start()

    print("Modo dev ativo (hot reload)")
    print("Observando alterações...\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando dev server...")
        observer.stop()

    if worker:
        worker.terminate()

    observer.join()

import click
import sys
import time
import importlib
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Lista de módulos que queremos monitorar
# Pode incluir todos os módulos do projeto
from .termenul import Termenul

MODULES_TO_WATCH = [Termenul]


class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_reload = 0

    def on_modified(self, event):
        if not event.src_path.endswith(".py"):
            return

        now = time.time()
        if now - self.last_reload < 0.5:
            return  # evita múltiplos reloads em sequência

        self.last_reload = now
        file_name = os.path.basename(event.src_path)
        module_name = file_name.replace(".py", "")
        print(f"Arquivo alterado: {file_name}")

        # Recarrega apenas os módulos carregados
        for module in MODULES_TO_WATCH:
            if module.__name__ == module_name:
                print(f"Recarregando módulo {module_name}...")
                importlib.reload(module)
                print(f"Módulo {module_name} recarregado!")


@click.command()
def dev():
    observer = Observer()
    observer.schedule(ReloadHandler(), ".", recursive=True)
    observer.start()
    print("Rodando em modo dev (hot reload)...")

    try:
        while True:
            # Exemplo de execução usando módulos atualizados
            # Você pode chamar funções aqui repetidamente para teste
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    dev()
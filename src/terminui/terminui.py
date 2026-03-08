import asyncio
import shutil
import sys
import os

from terminui.core.content import Content
from terminui.core.ANSI import ANSI
from terminui.mainInstance import MainInstance

if sys.platform == "win32":
    import msvcrt
    def clearTerminal():
        os.system('cls')
else:
    import termios
    import tty
    import select
    def clearTerminal():
        os.system('clear')


class Terminui(Content):

    def __init__(self):
        MainInstance.setInstance(self)
        super().__init__()
        self.reset = False
        self.terminal_size_before = None
        self.resize()

    def resize(self):
        terminal_size = shutil.get_terminal_size()
        if terminal_size != self.terminal_size_before:
            self.width = terminal_size.columns
            self.height = terminal_size.lines
            self.terminal_size_before = terminal_size
            return True
        return False

    async def keyboardEntry(self):
        if sys.platform == "win32":
            while self.running:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode("utf-8", errors="ignore")
                    if key == "r":
                        self.reset = True
                    if key == "q":
                        self.running = False
                await asyncio.sleep(0.05)
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                while self.running:
                    r, _, _ = select.select([sys.stdin], [], [], 0)
                    if r:
                        key = sys.stdin.read(1)
                        if key == "r":
                            self.reset = True
                        if key == "q":
                            self.running = False
                    await asyncio.sleep(0.05)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    async def _run(self):
        try:
            while self.running:
                if self.resize() or self.reset:
                    self.reset = False
                clearTerminal()
                self.render()
                await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            print("\nClosing Contents...")
            raise
    
    async def _tasks(self):
        task1 = asyncio.create_task(self._run())
        task2 = asyncio.create_task(self.keyboardEntry())

        await asyncio.gather(task1, task2)
        

    def start(self):
        ANSI.hide_cursor()
        self.running = True
        try:
            asyncio.run(self._tasks())
        except KeyboardInterrupt:
            pass

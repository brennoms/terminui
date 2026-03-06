import asyncio
import shutil
import curses

from terminui.core.content import Content
from terminui.core.util.ANSI import ANSI


class Terminui(Content):

    def __init__(self):
        super().__init__()
        self.reset = False
        self.terminal_size_before = None
        self.setMainContent(Content())
        self.resize()

    def setMainContent(self, content):
        self.mainContent = content

    def resizeMainContent(self):
        self.mainContent.width = self.width
        self.mainContent.height = self.height
        self.mainContent.pos_x = self.pos_x
        self.mainContent.pos_y = self.pos_y

    def render(self):
        self.mainContent.render()

    def resize(self):
        terminal_size = shutil.get_terminal_size()
        if terminal_size != self.terminal_size_before:
            self.width = terminal_size.columns
            self.height = terminal_size.lines
            self.terminal_size_before = terminal_size
            self.resizeMainContent()
            return True
        return False

    async def keyboardEntry(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.nodelay(True)
        stdscr.keypad(True)
        try:
            while self.running:
                key = stdscr.getch()

                if key != -1:
                    if key == ord('r'):
                        self.reset = True

                    if key == ord('q'):
                        self.running = False

                await asyncio.sleep(0.05)
        except asyncio.CancelledError:
            print("\nClosing KeyboardEntry...")
            raise
        finally:
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()

    async def _run(self):
        try:
            while self.running:
                self.render()
                await asyncio.sleep(0.1)
                if self.resize() or self.reset:
                    self.resize()
                    self.reset = False
                await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            print("\nClosing mainContent...")
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


if __name__ == '__main__':
    termenul = Terminui()
    termenul.start()

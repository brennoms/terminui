import asyncio
import shutil

from terminui.core.content import Content


class Terminui(Content):

    def __init__(self):
        super().__init__()
        self.position = [0,0]
        self.terminal_size_before = None
        self.resize()
        self.menus = {}

    def resize(self):
        terminal_size = shutil.get_terminal_size()
        if terminal_size != self.terminal_size_before:
            self.width = terminal_size.columns
            self.height = terminal_size.lines
            self.terminal_size_before = terminal_size
            return True
        return False

    async def _run(self):
        try:
            while True:
                if self.resize():
                    print(self.height, self.width)
                await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            print("Closing Screen...")
            raise

    def start(self):
        try:
            asyncio.run(self._run())
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    termenul = Terminui()
    termenul.start()

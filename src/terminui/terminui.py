import asyncio

from terminui.core.screen import Screen
from terminui.core.content import Content


class Terminui(Content):

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.menus = {}

    async def _run(self):
        try:
            while True:
                if self.screen.resize():
                    print(self.screen.height, self.screen.width)
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

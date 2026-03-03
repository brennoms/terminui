import asyncio

from termenul.core.screen import Screen


class Termenul:

    def __init__(self):
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
    
    def addMenu(self, menu):
        self.menus[menu.__class__.__name__] = menu
        menu.termenul = self


if __name__ == '__main__':
    termenul = Termenul()
    termenul.start()

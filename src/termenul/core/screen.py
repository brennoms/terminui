import shutil

class Screen:

    def __init__(self):
        self.width = None
        self.height = None
        self.terminal_size_before = None

    def resize(self):
        terminal_size = shutil.get_terminal_size()
        if terminal_size != self.terminal_size_before:
            self.width = terminal_size.columns
            self.height = terminal_size.lines
            self.terminal_size_before = terminal_size
            return True
        return False

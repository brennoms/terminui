import sys

from terminui.core.data_content.position import Position
from terminui.core.data_content.size import Size
from terminui.core.data_content.padding import Padding
from terminui.core.data_content.style import Style
from terminui.core.ANSI import ANSI
from terminui.core.text_block import TextBlock

class Content:

    def __init__(self, x=0, y=0, width=0, height=0, pad_x=0, pad_y=0, bg = None, fg = None, text=' ', alignment='center'):
        self.pos = Position(self, x, y)
        self.size = Size(self, width, height)
        self.pad = Padding(self, pad_x, pad_y)
        self.style = Style(self, bg, fg)
        self.txtblock = TextBlock(text, alignment, width, height)
        
        self._contents = []
        self._reframe()

    def addContent(self, content):
        if isinstance(content, Content):
            self._contents.append(content)
    
    def changed(self):
        pass
    
    def _when_position_changed(self):
        self.changed()
        self.whenPosChanged()
    def whenPosChanged(self):
        pass

    def _when_size_changed(self):
        self.changed()
        self.txtblock.setSize(self.size.width, self.size.height)
        self.whenSizeChanged()
    def whenSizeChanged(self):
        pass

    def _when_padding_changed(self):
        self.changed()
        self.whenPadChanged()
    def whenPadChanged(self):
        pass

    def _when_style_changed(self):
        self.changed()
        self.whenStyleChanged()
    def whenStyleChanged(self):
        pass

    def _reframe(self):
        self._frame = []
        lines = self.txtblock.lines
        pos_y = self.pos.y
        pos_x = self.pos.x

        for i, line in enumerate(lines):
            l = []
            for j, collumn in enumerate(line):
                y = pos_y + i
                x = pos_x + j

                if y >= self.size.height+pos_y and x >= self.size.width+pos_x:
                    continue

                if i < self.pad.y or j < self.pad.x:
                    string = ANSI.text_pos(collumn, pos_x+j, pos_y+i)
                    l.append(string) #WIP
                    continue

                string = ANSI.bg(collumn, self.style.bg.color) #WIP
                string = ANSI.color(string, self.style.fg.color) #WiP
                if self.style.bold:
                    string = ANSI.bold(string)
                if self.style.italic:
                    string = ANSI.itallic(string)
                if self.style.underline:
                    string = ANSI.underline(string)
                string = ANSI.text_pos(string, y, x)

                sys.stdout.write(string)
                l.append(string)
            self._frame.append(l)

        sys.stdout.flush()

    def render(self):
        self._reframe()
        for content in self._contents:
            if isinstance(content, Content):
                content.render()

if __name__ == "__main__":
    content = Content()
    content.size.width = 10
    content.size.height = 5
    content.pos.x = 10
    content.pos.y = 10
    content.style.bg.color = "red"
    content.render()

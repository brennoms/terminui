from enum import verify
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
            content.pos.x += self.pos.x
            content.pos.y += self.pos.y
            self._contents.append(content)
    
    def changed(self):
        self._reframe()
    
    def _when_position_changed(self):
        self.changed()
        self.whenPosChanged()
    def whenPosChanged(self):
        pass

    def _when_size_changed(self):
        self.txtblock.setSize(self.size.width, self.size.height)
        self.changed()
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

        x = self.pos.x
        y = self.pos.y
        width = self.size.width
        height = self.size.height

        for line in range(height):
            l = []

            for collumn in range(width):
                pos_x = x + collumn
                pos_y = y + line
                ansi = self.txtblock.getPos(line, collumn)
                ansi = ANSI.super_formated_text(
                    ansi, pos_y, pos_x, self.style.bg.color, 
                    self.style.fg.color, self.style.bold,
                    self.style.italic, self.style.underline
                    )
                l.append(ansi)

            self._frame.append(l)

    def render(self, restriction=None):

        def verify_in(line, collumn, restriction):
            if line >= restriction.pos.y and collumn >= restriction.pos.x:
                if line < restriction.pos.y + restriction.size.height and collumn < restriction.pos.x + restriction.size.width:
                    return True

        buffer = []
        for l, line in enumerate(self._frame):
            for c, collumn in enumerate(line):
                if restriction == None:
                    buffer.append(collumn)
                elif verify_in(self.pos.y+l, self.pos.x+c, restriction):
                        buffer.append(collumn)

        sys.stdout.write("".join(buffer))

        for content in self._contents:
            content.render(self)
        
        sys.stdout.flush()


if __name__ == "__main__":
    content = Content()
    content.size.width = 10
    content.size.height = 5
    content.pos.x = 10
    content.pos.y = 10
    content.style.bg.color = "red"
    content.render()

import sys

from terminui.mainInstance import MainInstance
from terminui.core.data_content.position import Position
from terminui.core.data_content.size import Size
from terminui.core.data_content.padding import Padding
from terminui.core.data_content.style import Style
from terminui.core.ANSI import ANSI

class Content:

    def __init__(self, x=0, y=0, width=0, height=0, pad_x=0, pad_y=0, bg = None, fg = None):
        self.pos = Position(self, x, y)
        self.size = Size(self, width, height)
        self.pad = Padding(self, pad_x, pad_y)
        self.style = Style(self, bg, fg)
        
        self._contents = []
        self._frame = []
        self._changed()

    def addContent(self, content):
        if isinstance(content, Content):
            self._contents.append(content)
    
    def _changed(self):
        self._reframe()
    
    def _reframe(self):
        self._frame = []
        for line in range(self.size.height):
            l = []
            for collumn in range(self.size.width):
                if line < self.pad.y:
                    string = ANSI.text_pos(' ', self.pos.x+collumn, self.pos.y+line)
                    l.append(string) #WIP
                    continue
                if collumn < self.pad.x:
                    string = ANSI.text_pos(' ', self.pos.x+collumn, self.pos.y+line)
                    l.append(string) #WIP
                    continue
                string = ANSI.bg(' ', self.style.bg.color) #WIP
                string = ANSI.color(string, self.style.fg.color) #Wip
                if self.style.bold:
                    string = ANSI.bold(string)
                if self.style.italic:
                    string = ANSI.itallic(string)
                if self.style.underline:
                    string = ANSI.underline(string)
                string = ANSI.text_pos(string, self.pos.x+collumn, self.pos.y+line)
                l.append(string)
            self._frame.append(l)
        
    def _when_position_changed(self):
        self._changed()
        self.whenPosChanged()
    def _when_size_changed(self):
        self._changed()
        self.whenSizeChanged()
    def _when_padding_changed(self):
        self._changed()
        self.whenPadChanged()
    def _when_style_changed(self):
        self._changed()
        self.whenStyleChanged()
    def whenPosChanged(self):
        pass
    def whenSizeChanged(self):
        pass
    def whenPadChanged(self):
        pass
    def whenStyleChanged(self):
        pass

    def render(self):
        for line in self._frame:
            for collumn in line:
                sys.stdout.write(collumn)
        sys.stdout.flush()
        for content in self._contents:
            if isinstance(content, Content):
                content.render()

if __name__ == "__main__":
    content = Content()
    content.size.width = 5
    content.size.height = 5
    content.pos.x = 10
    content.pos.y = 10
    content.style.bg.color = "red"
    content.style.fg.color = "blue"
    content.render()

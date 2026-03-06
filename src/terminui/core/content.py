from terminui.core.textBlock import textBlock
from terminui.core.ANSI import ANSI
from terminui.core.exceptions import ExceptionBgColor


class Content:
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._update_content()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update_content()
    
    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        if color not in ANSI.bg_colors:
            raise ExceptionBgColor(self)
        self._background_color = color


    def __init__(self, pos_x=0, pos_y=0, width=0, height=0, padding_x=0, padding_y=0, background_color='black'):
        self.father = None

        self.pos_x = pos_x
        self.pos_y = pos_y

        self._width = width
        self._height = height
        self.padding_x = padding_x
        self.padding_y = padding_y

        self._background_color = background_color

        self.contents = []
        self._update_content()

    
    def _update_content(self):
        self.mainContent = textBlock('', width=self._width, height=self._height)

    def render(self):
        for i in range(len(self.mainContent.lines)):
            line = ANSI.bg(self.mainContent.lines[i], self.background_color)
            ANSI.writePos(line, self.pos_y+i, self.pos_x)
        for content in self.contents:
            if isinstance(content, Content):
                content.render()
    
    def addContent(self, content):
        self.contents.append(content)

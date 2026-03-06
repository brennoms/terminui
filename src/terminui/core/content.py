from terminui.core.util.textBlock import textBlock
from terminui.core.util.ANSI import ANSI


class Content:
    
    def __init__(self, width=0, height=0, padding_x=0, padding_y=0, background_color='black'):
        self.father = None

        self.pos_x = 0
        self.pos_y = 0

        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y
    
        self.background_color = background_color

    def render(self):
        box = textBlock('', width=self.width, height=self.height)
        for i in range(len(box.lines)):
            line = ANSI.bg(box.lines[i], 'blue')
            ANSI.writePos(line, self.pos_y+i, self.pos_x)

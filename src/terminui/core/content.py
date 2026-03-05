from terminui.core.util.textBlock import textBlock
import terminui.core.util.ANSI as ANSI


class Content:
    
    def __init__(self, orientation='tb', alignment='center', width='auto', height='auto', padding_x=0, padding_y=0, background_color='black', text_color='black', text=None):
        self.father = None

        self.pos_x = 0
        self.pos_y = 0

        self.used_x = 0
        self.used_y = 0
        
        self.orientation = orientation
        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y

        self.setText(text)
        self.alignment = alignment
        self.background_color = background_color
        self.text_color = text_color
        
        self._contents = []

        self.autoSize()
    

    def setText(self, text):
        if type(text) == str:
            self.text = text
            self.text_block = textBlock(text)
        else:
            self.text = None
            self.text_block = None
    

    def autoSize(self):
        if self.width == 'auto':
            self._autoWidth()
        if self.height == 'auto':
            self._autoHeight()

    def _autoWidth(self):
        if self.text_block != None:
            self.width = self.text_block.columns + 2*self.padding_x
        else:
            self.width = 0

    def _autoHeight(self):
        if self.text_block != None:
            self.width = self.text_block.lines + 2*self.padding_y
        else:
            self.width = 0
    

    def addContent(self, content):
        if isinstance(content, Content):
            content.father = self
            self.used_x += content.width
            self.used_y += content.height
            content.autoPosition()
            self._contents.append(content)
        else:
            raise Exception('Content.addContent(), only accepts an instance of the Content class as a parameter')
    
    def removeContent(self, content):
        self._contents.remove(content)
    

    def autoPosition(self):
        if self.father.orientation == 'tb':
            self.pos_x = self.father.pos_x
            self.pos_y = self.father.pos_y + self.father.used_y
        elif self.father.orientation == 'lr':
            self.pos_x = self.father.pos_x + self.father.used_x
            self.pos_y = self.father.pos_y

    def render(self):
        if len(self._contents) > 0:
            self.renderContents()
        else:
            #pintar background
            pos = [self.pos_x+self.padding_x, self.pos_y+self.padding_y]
            self.text_block.posText(pos)

    def renderContents(self):
        for content in self._contents:
            content.render()

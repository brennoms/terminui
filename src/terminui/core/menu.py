class Menu:
    
    def __init__(self, orientation='tb', alignment='center', padding_x=0, padding_y=0, background_color='black'):
        self.termenul = None
        self.orientation = orientation
        self.alignment = alignment
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.background_color = background_color
        self.contents = []
    
    def addContent(self, content):
        self.content.append(content)
    
    def render(self):
        contents_str = ''
        for content in self.contents:
            contents_str += f'\n{content.render()}'

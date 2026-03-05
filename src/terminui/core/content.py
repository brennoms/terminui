class Content:
    
    def __init__(self, orientation='tb', alignment='center', padding_x=0, padding_y=0, background_color='black', text_color='black', text=None):
        self.super = None
        self.orientation = orientation
        self.alignment = alignment
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.background_color = background_color
        self.text_color = text_color
        self.text = text
        self._contents = []
    
    def addContent(self, content):
        if isinstance(content, Content):
            self._contents.append(content)
        else:
            raise Exception('Content.addContent(), only accepts an instance of the Content class as a parameter')
    
    def removeContent(self, content):
        try:
            self._contents.remove(content)
        except:
            return False

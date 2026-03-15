class TextBlock:

    def __init__(self, text, alignment='center', width='auto', height='auto'):

        self.text = text
        self.alignment = alignment
        self.width = width if type(width) == int else 'auto'
        self.height = height if type(height) == int else 'auto'
        self.lines = []

        if self.width == 'auto' or self.height == 'auto':
            ltext = text.split('\n')
            columns = 0
            lines = 0
            for line in ltext:
                if columns < len(line):
                    columns = len(line)
                lines += 1
            self.width = columns
            self.height = lines

        self.align()

    def getPos(self, line, collum):
        return self.lines[line][collum]

        
    def setSize(self, width, height):
        self.width = width
        self.height = height
        self.align()
    
    def setAlignment(self, alignment):
        self.alignment = alignment
    
    def align(self):
        ltext = self.text.split('\n')
        for i in range(self.height):
            if i < len(ltext):
                columns = len(ltext[i])
                if self.width > columns:
                    match self.alignment:
                        case 'left':
                            line = ltext[i] + ' '*(self.width-columns)
                        case 'center':
                            line = ' '*((self.width-columns)//2) + ltext[i] + ' '*((self.width-columns+1)//2)
                        case 'right':
                            line = ' '*(self.width-columns) + ltext[i]
                elif self.width < columns:
                    match self.alignment:
                        case 'left':
                            line = ltext[i][:self.width]
                        case 'center':
                            line = ltext[i][(columns-self.width)//2:(columns+self.width+1)//2]
                        case 'right':
                            line = ltext[i][columns-self.width:]
                else:
                    line = ltext[i]
            else:
                line = ' '*self.width
            self.lines.append(line)
    

if __name__ == "__main__":
    text = 'aaaaa\naa\naaa'
    text_plus = TextBlock(text, alignment='right')
    #text_plus = textBlock(text, width=3, height=10)
    text_plus = TextBlock('', width=5, height=5)
    print(text_plus.text, '\n')
    print(f'width: {text_plus.width}')
    print(f'height: {text_plus.height}')
    print(f'lines: {text_plus.lines}')


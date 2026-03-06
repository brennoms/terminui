class textBlock:

    def __init__(self, string, alignment='center', width='auto', height='auto'):

        self.string = string
        self.alignment = alignment
        self.width = width if type(width) == int else 'auto'
        self.height = height if type(height) == int else 'auto'
        self.lines = []

        if self.width == 'auto' or self.height == 'auto':
            lstring = string.split('\n')
            columns = 0
            lines = 0
            for line in lstring:
                if columns < len(line):
                    columns = len(line)
                lines += 1
            self.width = columns
            self.height = lines

        self.align()

        
    def setSize(self, width, height):
        self.width = width
        self.height = height
        self.align(self.alignment)
    
    def setAlignment(self, alignment):
        self.alignment = alignment
    
    def align(self):
        lstring = self.string.split('\n')
        for i in range(self.height):
            if i < len(lstring):
                columns = len(lstring[i])
                if self.width > columns:
                    match self.alignment:
                        case 'left':
                            line = lstring[i] + ' '*(self.width-columns)
                        case 'center':
                            line = ' '*((self.width-columns)//2) + lstring[i] + ' '*((self.width-columns+1)//2)
                        case 'right':
                            line = ' '*(self.width-columns) + lstring[i]
                elif self.width < columns:
                    match self.alignment:
                        case 'left':
                            line = lstring[i][:self.width]
                        case 'center':
                            line = lstring[i][(columns-self.width)//2:(columns+self.width+1)//2]
                        case 'right':
                            line = lstring[i][columns-self.width:]
                else:
                    line = lstring[i]
            else:
                line = ' '*self.width
            self.lines.append(line)
    

if __name__ == "__main__":
    string = 'aaaaa\naa\naaa'
    string_plus = textBlock(string, alignment='right')
    #string_plus = textBlock(string, width=3, height=10)
    string_plus = textBlock('', width=5, height=5)
    print(string_plus.string, '\n')
    print(f'width: {string_plus.width}')
    print(f'height: {string_plus.height}')
    print(f'lines: {string_plus.lines}')


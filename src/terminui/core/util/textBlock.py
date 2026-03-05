class textBlock:
    def __init__(self, string):
        self.string = string
        self.columns = 0
        self.lines = 0
        for line in string.split('\n'):
            if len(line) > self.columns:
                self.columns = len(line)
            self.lines += 1
    
    def posText(pos, size='full'):
        pass

if __name__ == "__main__":
    string = 'aaaaa\naa\naaa'
    string_plus = textBlock(string)
    print(string_plus.string, '\n')
    print(f'columns: {string_plus.columns}')
    print(f'lines: {string_plus.lines}')

from terminui.core.color import Color

class Style:

    def __init__(self, parent=None, bg=None, fg=None, bold=False, italic=False, underline=False):
        self.parent = parent
        self._fg = Color(fg) if fg is not None else Color()
        self._bg = Color(bg) if bg is not None else Color()
        if self.parent != None:
            self._fg.parent = self.parent
            self._fg.parent = self.parent
        self._bold = bold if bold == True else False
        self._italic = italic if italic == True else False
        self._underline = underline if underline == True else False

    def _changed(self):
        if self.parent is not None:
            self.parent._when_style_changed()

    @property
    def fg(self):
        return self._fg
    @fg.setter
    def fg(self, value):
        if isinstance(value, Color):
            value._parent = self
            self._fg = value
            self._changed()
        else:
            raise Exception('foreground only accepts an instance of Color class \n if you want change the color try fg.color = color')

    @property
    def bg(self):
        return self._bg
    @bg.setter
    def bg(self, value):
        if isinstance(value, Color):
            value._parent = self
            self._bg = value
            self._changed()
        else:
            raise Exception('background only accepts an instance of Color class \n if you want change the color try bg.color = color')


    @property
    def bold(self):
        return self._bold
    @bold.setter
    def bold(self, value):
        self._bold = value
        self._changed()

    @property
    def italic(self):
        return self._italic
    @italic.setter
    def italic(self, value):
        self._italic = value
        self._changed()

    @property
    def underline(self):
        return self._underline
    @underline.setter
    def underline(self, value):
        self._underline = value
        self._changed()

    def __str__(self):
        return f"Style(fg={self._fg.color}, bg={self._bg.color}, bold={self._bold}, italic={self._italic}, underline={self._underline})"


if __name__ == "__main__":
    style = Style()
    print(style)
    style.fg = Color('red')
    style.bg = Color(0, 255, 0)
    print(style)
    style.fg.color = "green"
    style.bg.color = 1, 2, 3
    print(style)
    style.bold = True
    print(style)
    style.italic = True
    print(style)
    style.underline = True
    print(style)
    

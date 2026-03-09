from terminui.core.colorClasses import Color

class Style:

    def __init__(self, parent=None, fg=None, bg=None, bold=False, italic=False, underline=False):
        self.parent = parent
        self._fg = self._validate_color(fg) if fg is not None else Color("white")
        self._bg = self._validate_color(bg) if bg is not None else Color("white")
        self._bold = bold if bold == True else False
        self._italic = italic if italic == True else False
        self._underline = underline if underline == True else False

    def _changed(self):
        if self.parent is not None:
            self.parent._whenStyleChanged()

    @property
    def fg(self):
        return self._fg
    @fg.setter
    def fg(self, value):
        self._fg = Color(value)
        self._changed()

    @property
    def bg(self):
        return self._bg
    @bg.setter
    def bg(self, value):
        self._bg = Color(value)
        self._changed()

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
    style.fg = "red"
    print(style)
    style.bg = (0, 255, 0)
    print(style)
    style.bold = True
    print(style)
    style.italic = True
    print(style)
    style.underline = True
    print(style)
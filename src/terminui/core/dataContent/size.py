class Size:

    def __init__(self, parent=None):
        self._size = [0, 0]
        self.parent = parent

    def _validate(self, value, name):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} can't be negative")

    def _changed(self):
        if self.parent is not None:
            self.parent.whenSizeChanged()

    @property
    def width(self):
        return self._size[0]

    @width.setter
    def width(self, value):
        self._validate(value, "Width")
        self._size[0] = value
        self._changed()

    @property
    def height(self):
        return self._size[1]

    @height.setter
    def height(self, value):
        self._validate(value, "Height")
        self._size[1] = value
        self._changed()

    def __iter__(self):
        return iter(self._size)

    def __getitem__(self, i):
        if 0 <= i <= 1:
            return self._size[i]
        raise IndexError("Size just have 2 values")

    def __setitem__(self, i, v):
        if i == 0:
            self.width = v
        elif i == 1:
            self.height = v
        else:
            raise IndexError("Size just have 2 values")

    def __repr__(self):
        return f"Size{self._size}"
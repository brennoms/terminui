class Padding:

    def __init__(self, parent=None):
        self._padding = [0, 0]
        self.parent = parent

    def _validate(self, value, name):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} can't be negative")

    def _changed(self):
        if self.parent is not None:
            self.parent.whenPaddingChanged()

    @property
    def x(self):
        return self._padding[0]

    @x.setter
    def x(self, value):
        self._validate(value, "padding.x")
        self._padding[0] = value
        self._changed()

    @property
    def y(self):
        return self._padding[1]

    @y.setter
    def y(self, value):
        self._validate(value, "padding.y")
        self._padding[1] = value
        self._changed()

    def __iter__(self):
        return iter(self._padding)

    def __getitem__(self, i):
        if 0 <= i <= 1:
            return self._padding[i]
        raise IndexError("Padding just have 2 values")

    def __setitem__(self, i, v):
        if i == 0:
            self.x = v
        elif i == 1:
            self.y = v
        else:
            raise IndexError("Padding just have 2 values")

    def __repr__(self):
        return f"Padding{self._padding}"
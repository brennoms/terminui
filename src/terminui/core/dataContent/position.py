class Pos:
    
    def __init__(self, parent=None, x=0, y=0):
        self._pos = [x, y]
        self.parent = parent

    def _validate(self, value, name):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} can't be negative")

    def _changed(self):
        if self.parent is not None:
            self.parent._whenPosChanged()

    @property
    def x(self):
        return self._pos[0]

    @x.setter
    def x(self, value):
        self._validate(value, "pos.x")
        self._pos[0] = value
        self._changed()

    @property
    def y(self):
        return self._pos[1]

    @y.setter
    def y(self, value):
        self._validate(value, "pos.y")
        self._pos[1] = value
        self._changed()

    def __iter__(self):
        return iter(self._pos)

    def __getitem__(self, i):
        if 0 <= i <= 1:
            return self._pos[i]
        raise IndexError("Pos just have 2 values")

    def __setitem__(self, i, v):
        if i == 0:
            self.x = v
        elif i == 1:
            self.y = v
        else:
            raise IndexError("Pos just have 2 values")

    def __add__(self, other):
        return Pos(self._pos[0] + other.x, self._pos[1] + other.y)

    def __mul__(self, value):
        return Pos(self._pos[0] * value, self._pos[1] * value)

    def __repr__(self):
        return f"Pos{self._pos}"

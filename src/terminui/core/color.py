from terminui.core.ANSI import ANSI

class Color:
    def __init__(self, *args, **kargs):
        if "parent" in kargs:
            self.parent = kargs["parent"]
        else:
            self.parent = None
        if len(args) == 1:
            args = args[0]
        elif len(args) == 0:
            args = 'white'
        self.color = args

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str):
            if value not in ANSI.colors:
                raise ValueError(f'Color "{value}" is not a valid ANSI color')
            self._color = value
            self._schema = ['ANSI', 'ansi']
            if self.parent != None:
                self.parent._changed()
            return
        if isinstance(value, (list, tuple)):
            if len(value) != 3 or not all(isinstance(c, int) for c in value):
                raise ValueError("RGB color must contain three integers")
            if not all(0 <= c <= 255 for c in value):
                raise ValueError("RGB values must be in the range 0-255")
            self._color = tuple(value)
            self._schema = ['rgb', 'RGB']
            if self.parent != None:
                self.parent._changed()
            return
        raise ValueError("Invalid color format")

    @property
    def schema(self):
        return self._schema
    @schema.setter
    def schema(self, *args):
        pass

 
if __name__ == "__main__":
    color_rgb = Color()
    color_rgb.color = 255, 0, 0
    print(color_rgb.color)  # Output: (255, 0, 0)
    color_rgb.color = [0, 255, 0]
    print(color_rgb.color)  # Output: (0, 255, 0)
    color_rgb.color = (0, 0, 255)
    print(color_rgb.color)  # Output: (0, 0, 255)
    try:
        color_rgb.color = (256, 0, 0)
    except ValueError as e:
        print(e)  # Output: "RGB value must be in the range 0-255"
    try:
        color_rgb.color = "not_a_color"
    except ValueError as e:
        print(e)  # Output: "RGB color must be a list or tuple of three integers"

    print()

    color_ansi = Color("red")
    print(color_ansi.color)  # Output: "red"
    color_ansi.color = "green"
    print(color_ansi.color)  # Output: "green"
    try:
        color_ansi.color = "invalid_color"
    except ValueError as e:
        print(e)  # Output: "Color 'invalid_color' is not a valid ANSI color"

from terminui.core.ANSI import ANSI

class Color:
    def __init__(self, color):
        self.color = color
    
    @property
    def color(self):
        return self._color.color
    @color.setter
    def color(self, value):
        if isinstance(value, str):
            self._color = ColorANSI(value)
        else:
            self._color = ColorRgb(*value)
 

class ColorRgb:

    def __init__(self, r=0, g=0, b=0):
        self.color = (r, g, b)

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, values):
        if not isinstance(values, (list, tuple)) or len(values) != 3 or not all(isinstance(c, int) for c in values):
            raise ValueError("RGB color must be a list or tuple of three integers")
        if not all(0 <= c <= 255 for c in values):
            raise ValueError("RGB values must be in the range 0-255")
        self._color = tuple(values)


class ColorANSI:
    # for compatibility with ANSI color names
    def __init__(self, color):
        self.color = color
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        if value not in ANSI.colors:
            raise ValueError(f"Color '{value}' is not a valid ANSI color")
        self._color = value


if __name__ == "__main__":
    color_rgb = ColorRgb()
    color_rgb.color = 255, 0, 0
    print(color_rgb.color)  # Output: (255, 0, 0)
    color_rgb.color = [0, 255, 0]
    print(color_rgb.color)  # Output: (0, 255, 0)
    color_rgb.color = (0, 0, 255)
    print(color_rgb.color)  # Output: (0, 0, 255)
    try:
        color_rgb.color = (256, 0, 0)
    except ValueError as e:
        print(e)  # Output: "RGB values must be in the range 0-255"
    try:
        color_rgb.color = "not_a_color"
    except ValueError as e:
        print(e)  # Output: "RGB color must be a list or tuple of three integers"

    print()

    color_ansi = ColorANSI("red")
    print(color_ansi.color)  # Output: "red"
    color_ansi.color = "green"
    print(color_ansi.color)  # Output: "green"
    try:
        color_ansi.color = "invalid_color"
    except ValueError as e:
        print(e)  # Output: "Color 'invalid_color' is not a valid ANSI color"

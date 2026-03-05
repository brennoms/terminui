#AI made
import sys


class ANSIText:

    ESC = "\033["

    # =========================
    # STANDARD COLORS
    # =========================
    colors = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,

        "bright_black": 90,
        "bright_red": 91,
        "bright_green": 92,
        "bright_yellow": 93,
        "bright_blue": 94,
        "bright_magenta": 95,
        "bright_cyan": 96,
        "bright_white": 97
    }

    bg_colors = {
        "black": 40,
        "red": 41,
        "green": 42,
        "yellow": 43,
        "blue": 44,
        "magenta": 45,
        "cyan": 46,
        "white": 47,

        "bright_black": 100,
        "bright_red": 101,
        "bright_green": 102,
        "bright_yellow": 103,
        "bright_blue": 104,
        "bright_magenta": 105,
        "bright_cyan": 106,
        "bright_white": 107
    }

    # =========================
    # INTERNAL
    # =========================
    @staticmethod
    def _get_color_code(color, bg=False):
        if isinstance(color, int):
            return color

        if bg:
            return ANSIText.bg_colors.get(color, 49)
        else:
            return ANSIText.colors.get(color, 39)

    # =========================
    # RESET
    # =========================
    @staticmethod
    def reset():
        return f"{ANSIText.ESC}0m"

    # =========================
    # TEXT COLORS
    # =========================
    @staticmethod
    def color(text, color):
        code = ANSIText._get_color_code(color)
        return f"{ANSIText.ESC}{code}m{text}{ANSIText.reset()}"

    # =========================
    # BACKGROUND COLORS
    # =========================
    @staticmethod
    def bg(text, color):
        code = ANSIText._get_color_code(color, bg=True)
        return f"{ANSIText.ESC}{code}m{text}{ANSIText.reset()}"

    # =========================
    # STYLES
    # =========================
    @staticmethod
    def bold(text):
        return f"{ANSIText.ESC}1m{text}{ANSIText.reset()}"

    @staticmethod
    def italic(text):
        return f"{ANSIText.ESC}3m{text}{ANSIText.reset()}"

    @staticmethod
    def underline(text):
        return f"{ANSIText.ESC}4m{text}{ANSIText.reset()}"

    @staticmethod
    def blink(text):
        return f"{ANSIText.ESC}5m{text}{ANSIText.reset()}"

    @staticmethod
    def inverse(text):
        return f"{ANSIText.ESC}7m{text}{ANSIText.reset()}"

    @staticmethod
    def strike(text):
        return f"{ANSIText.ESC}9m{text}{ANSIText.reset()}"

    # =========================
    # 256 COLORS
    # =========================
    @staticmethod
    def color256(text, color):
        return f"{ANSIText.ESC}38;5;{color}m{text}{ANSIText.reset()}"

    @staticmethod
    def bg256(text, color):
        return f"{ANSIText.ESC}48;5;{color}m{text}{ANSIText.reset()}"

    # =========================
    # TRUE COLOR (RGB)
    # =========================
    @staticmethod
    def rgb(text, r, g, b):
        return f"{ANSIText.ESC}38;2;{r};{g};{b}m{text}{ANSIText.reset()}"

    @staticmethod
    def bg_rgb(text, r, g, b):
        return f"{ANSIText.ESC}48;2;{r};{g};{b}m{text}{ANSIText.reset()}"

    # =========================
    # CURSOR POSITION
    # =========================
    @staticmethod
    def move_to(row, col):
        sys.stdout.write(f"{ANSIText.ESC}{row};{col}H")

    @staticmethod
    def up(n=1):
        sys.stdout.write(f"{ANSIText.ESC}{n}A")

    @staticmethod
    def down(n=1):
        sys.stdout.write(f"{ANSIText.ESC}{n}B")

    @staticmethod
    def right(n=1):
        sys.stdout.write(f"{ANSIText.ESC}{n}C")

    @staticmethod
    def left(n=1):
        sys.stdout.write(f"{ANSIText.ESC}{n}D")

    # =========================
    # SAVE / RESTORE CURSOR
    # =========================
    @staticmethod
    def save_cursor():
        sys.stdout.write("\033[s")

    @staticmethod
    def restore_cursor():
        sys.stdout.write("\033[u")

    # =========================
    # CLEAR SCREEN
    # =========================
    @staticmethod
    def clear():
        sys.stdout.write(f"{ANSIText.ESC}2J")

    @staticmethod
    def clear_line():
        sys.stdout.write(f"{ANSIText.ESC}2K")

    @staticmethod
    def clear_to_end():
        sys.stdout.write(f"{ANSIText.ESC}K")

    # =========================
    # CURSOR VISIBILITY
    # =========================
    @staticmethod
    def hide_cursor():
        sys.stdout.write("\033[?25l")

    @staticmethod
    def show_cursor():
        sys.stdout.write("\033[?25h")

    # =========================
    # BEEP
    # =========================
    @staticmethod
    def beep():
        sys.stdout.write("\a")
    
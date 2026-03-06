#AI made
import sys


class ANSI:

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
            return ANSI.bg_colors.get(color, 49)
        else:
            return ANSI.colors.get(color, 39)

    # =========================
    # RESET
    # =========================
    @staticmethod
    def reset():
        return f"{ANSI.ESC}0m"
    
    @staticmethod
    def flush():
        sys.stdout.flush()

    # =========================
    # TEXT COLORS
    # =========================
    @staticmethod
    def color(text, color):
        code = ANSI._get_color_code(color)
        return f"{ANSI.ESC}{code}m{text}{ANSI.reset()}"

    # =========================
    # BACKGROUND COLORS
    # =========================
    @staticmethod
    def bg(text, color):
        code = ANSI._get_color_code(color, bg=True)
        return f"{ANSI.ESC}{code}m{text}{ANSI.reset()}"

    # =========================
    # STYLES
    # =========================
    @staticmethod
    def bold(text):
        return f"{ANSI.ESC}1m{text}{ANSI.reset()}"

    @staticmethod
    def italic(text):
        return f"{ANSI.ESC}3m{text}{ANSI.reset()}"

    @staticmethod
    def underline(text):
        return f"{ANSI.ESC}4m{text}{ANSI.reset()}"

    @staticmethod
    def blink(text):
        return f"{ANSI.ESC}5m{text}{ANSI.reset()}"

    @staticmethod
    def inverse(text):
        return f"{ANSI.ESC}7m{text}{ANSI.reset()}"

    @staticmethod
    def strike(text):
        return f"{ANSI.ESC}9m{text}{ANSI.reset()}"

    # =========================
    # 256 COLORS
    # =========================
    @staticmethod
    def color256(text, color):
        return f"{ANSI.ESC}38;5;{color}m{text}{ANSI.reset()}"

    @staticmethod
    def bg256(text, color):
        return f"{ANSI.ESC}48;5;{color}m{text}{ANSI.reset()}"

    # =========================
    # TRUE COLOR (RGB)
    # =========================
    @staticmethod
    def rgb(text, r, g, b):
        return f"{ANSI.ESC}38;2;{r};{g};{b}m{text}{ANSI.reset()}"

    @staticmethod
    def bg_rgb(text, r, g, b):
        return f"{ANSI.ESC}48;2;{r};{g};{b}m{text}{ANSI.reset()}"

    # =========================
    # CURSOR POSITION
    # =========================
    @staticmethod
    def move_to(row, col):
        sys.stdout.write(f"{ANSI.ESC}{row};{col}H")
        ANSI.flush()
    
    def writePos(text, row, col):
        sys.stdout.write(f'{ANSI.ESC}{row};{col}H{text}{ANSI.reset()}')
        ANSI.flush()

    @staticmethod
    def up(n=1):
        sys.stdout.write(f"{ANSI.ESC}{n}A")

    @staticmethod
    def down(n=1):
        sys.stdout.write(f"{ANSI.ESC}{n}B")

    @staticmethod
    def right(n=1):
        sys.stdout.write(f"{ANSI.ESC}{n}C")

    @staticmethod
    def left(n=1):
        sys.stdout.write(f"{ANSI.ESC}{n}D")


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
        sys.stdout.write(f"{ANSI.ESC}2J")
        ANSI.flush()
        
    @staticmethod
    def clear_to_line(line):
        ANSI.move_to(0,0)
        for i in range(line):
            ANSI.clear_line()
            ANSI.down(0)
        ANSI.flush()

    @staticmethod
    def clear_line():
        sys.stdout.write(f"{ANSI.ESC}2K")

    @staticmethod
    def clear_to_end():
        sys.stdout.write(f"{ANSI.ESC}K")

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
        sys.stdout.write(f"\a{ANSI.reset()}")
        ANSI.flush()
    
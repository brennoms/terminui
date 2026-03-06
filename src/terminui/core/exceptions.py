class ExceptionBgColor(Exception):
    def __init__(self, content):
        from terminui.core.ANSI import ANSI
        msg = "\nbackgound_color only accept the following terms:\n["
        for key in ANSI.bg_colors:
            msg += f'{key}, '
        msg += ']'
        super().__init__(msg)

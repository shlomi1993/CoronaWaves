# Shlomi Ben-Shushan 311408264
# Itamar Laredo _________


class Palette:
    """
    This class represents a color palette for easy access to pre-defined colors.
    """
    def __init__(self):
        self.bg = '#2c313a'
        self.fg = '#1f7db7'
        self.canvas_bg = '#404040'
        self.canvas_outline = 'gray'
        self.btn_bg = '#181818'
        self.btn_fg = '#f0f0f0'
        self.red = '#ff0000'
        self.orange = '#ffa500'
        self.cyan = '#00ffff'
        self.white = '#ffffff'


class Fonts:
    """
    This class represents a font menu for easy access to pre-defined fonts.
    """
    def __init__(self):
        self.regular = ('Consoles', 11)
        self.bold = ("Consoles", 11, 'bold')
        self.credit = ('Consoles', 8, 'italic')


# Making a single instance from each class to expose it to other classes.
palette = Palette()
fonts = Fonts()

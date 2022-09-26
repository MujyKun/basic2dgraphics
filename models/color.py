class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def set_rgb(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    @property
    def rgb(self):
        return self.r, self.g, self.b

    @classmethod
    def black(cls):
        return Color(0, 0, 0).rgb

    @classmethod
    def white(cls):
        return Color(255, 255, 255).rgb

    @classmethod
    def red(cls):
        return Color(255, 0, 0).rgb

    @classmethod
    def lime(cls):
        return Color(0, 255, 0).rgb

    @classmethod
    def blue(cls):
        return Color(0, 0, 255).rgb

    @classmethod
    def yellow(cls):
        return Color(255, 255, 0).rgb

    @classmethod
    def cyan(cls):
        return Color(0, 255, 255).rgb

    @classmethod
    def magenta(cls):
        return Color(255, 0, 255).rgb

    @classmethod
    def silver(cls):
        return Color(192, 192, 192).rgb

    @classmethod
    def gray(cls):
        return Color(128, 128, 128).rgb

    @classmethod
    def maroon(cls):
        return Color(128, 0, 0).rgb

    @classmethod
    def olive(cls):
        return Color(128, 128, 0).rgb

    @classmethod
    def green(cls):
        return Color(0, 128, 0).rgb

    @classmethod
    def purple(cls):
        return Color(128, 0, 128).rgb

    @classmethod
    def teal(cls):
        return Color(0, 128, 128).rgb

    @classmethod
    def navy(cls):
        return Color(0, 0, 128).rgb

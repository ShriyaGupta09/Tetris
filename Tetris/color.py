class Colors:
    dark_grey = (26, 31, 40)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    purple = (128, 0, 128)
    magenta = (255, 0, 255)
    blue = (0, 0, 255)
    cyan = (0, 255, 255)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    saffron = (248, 248, 255)
    black = (0, 0, 0)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.red, cls.orange, cls.green, cls.green, cls.yellow,
                cls.purple, cls.magenta, cls.blue, cls.cyan]

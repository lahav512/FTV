class Log:
    """This class is temporary!"""
    ENABLED = True
    __BLANK_SPACE = 0

    @staticmethod
    def p(message, color=""):
        Log.__print("", message, color)

    @staticmethod
    def i(message, color=""):
        Log.__print("info", message, color)

    @staticmethod
    def d(message, color=""):
        Log.__print("debug", message, color)

    @staticmethod
    def e(message, color=""):
        Log.__print("error", message, color)

    @staticmethod
    def __print(mode, message, color):
        if Log.ENABLED:
            mode_str = "".join((mode, ": "*int(bool(mode))))
            print("".join((mode_str, "   "*Log.__BLANK_SPACE, color, message, "\033[0m")))

    @classmethod
    def step(cls, step):
        cls.__BLANK_SPACE += step

    class color(object):
        LIGHT_BLUE = "\033[0;96m"
        BLUE = "\033[0;34m"
        ORANGE = "\033[0;33m"
        PURPLE = "\033[0;35m"
        PINK = "\033[0;95m"
        RED = "\033[0;31m"


if __name__ == '__main__':
    for i in list(range(30, 38)) + list(range(90, 98)):
        color_code = "\033[0;{}m".format(i)
        print("{}color {}{}".format(color_code, i, "\033[0m"))

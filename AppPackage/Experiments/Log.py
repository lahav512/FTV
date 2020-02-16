
class Log:
    """This class is temporary!"""

    @staticmethod
    def i(message):
        Log.__print("info", message)

    @staticmethod
    def d(message):
        Log.__print("debug", message)

    @staticmethod
    def e(message):
        Log.__print("error", message)

    @staticmethod
    def __print(mode, message):
        print("{}: {}".format(mode, message))

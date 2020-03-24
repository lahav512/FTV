
class Log:
    """This class is temporary!"""
    ENABLED = True

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
        if Log.ENABLED:
            print("{}: {}".format(mode, message))

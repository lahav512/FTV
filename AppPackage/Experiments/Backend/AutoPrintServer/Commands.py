class CommandMeta(type):
    cmd_name = None

    def __getattribute__(cls, item):
        cmd_name = super(CommandMeta, cls).__getattribute__("cmd_name")
        if cmd_name is not None:
            item = f"{cmd_name}/{item}"
            return item

        return super(CommandMeta, cls).__getattribute__(item)

    def getClassName(cls):
        return super(CommandMeta, cls).__getattribute__("__name__")


class Command(metaclass=CommandMeta):
    def __init_subclass__(cls, **kwargs):
        cls.cmd_name = cls.getClassName()


class AutoPrintServerCommands:
    class Server(Command):
        login = "login"
        logout = "logout"
        register = "register"

    class LocalServer(Command):
        info = "info"
        select = "select"
        get = "get"
        add = "add"
        remove = "remove"

    class Printer(Command):
        getTemperature = "getTemperature"
        setTemperature = "setTemperature"
        home = "home"
        move = "move"

    class Bed(Command):
        move = "move"
        moveUntilBreak = "moveUntilBreak"
        release = "release"
        home = "home"

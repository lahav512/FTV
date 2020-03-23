from functools import wraps, partial


class FTVMethodVariables:
    def __init__(self, func):
        self.func = func
        self.name = self.func.__name__
        self.__triggers__ = []

    def __call__(self, *args, **kwargs):
        self.func(self, *args, **kwargs)

    def addTrigger(self, trigger):
        self.__triggers__.append(trigger)


def FTVMethod(func=None):
    if not func:
        return partial(FTVMethod)

    @FTVMethodVariables
    def run_func():
        return func()

    @wraps(run_func)
    def wrapper(*args, **kwargs):
        print("-> " + func.__name__)
        ans = func(*args, **kwargs)
        print("<- " + func.__name__)
        return ans
    return wrapper


class Feature1:

    def __setattr__(self, key, value):
        if key in dir(self):
            if callable(getattr(self, key)):
                raise Exception(
                    "Can't add the attribute \"{}\" to the object \"{}\", since it is already exists as a method.".format(
                        key, self.__class__.__name__))
        else:
            super().__setattr__(key, value)

    def __getattribute__(self, item):
        ans = object.__getattribute__(self, item)
        if callable(ans):
            print(item)
            return ans
        else:
            return ans

    def __init__(self):
        self.__setMethodTriggers([])

        # self.action = "lahav"

    def action(self):
        self.do()

    def addTrigger(self, trigger):
        self.__getMethodTriggers().append(trigger)

    def __setMethodTriggers(self, triggers):
        setattr(object.__getattribute__(self.__class__, "action"), "__triggers__", triggers)

    def __getMethodTriggers(self) -> list:
        return getattr(object.__getattribute__(self.__class__, "action"), "__triggers__")

    def do(self):
        print("do")


class Feature2:

    def __init__(self):
        self.a = 2

    def __setattr__(self, key, value):
        if key in dir(self):
            if callable(getattr(self, key)):
                raise Exception(
                    "Can't add the attribute \"{}\" to the object \"{}\", since it is already exists as a method.".format(
                        key, self.__class__.__name__))
        else:
            super().__setattr__(key, value)

    @FTVMethodVariables
    def action(self):
        self.do()

    def addTrigger(self, trigger):
        self.action.__triggers__.append(trigger)

    def do(self):
        print("do")


feature = Feature1()
feature.addTrigger("a")
feature.addTrigger("b")
feature.addTrigger("c")
print(feature.action.__triggers__)
feature.action()

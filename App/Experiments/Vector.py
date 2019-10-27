from math import atan, pi, sqrt, pow, sin, cos
from time import time


class Link:
    def __init__(self, feature, trigger, method):
        self.feature = feature
        self.trigger = trigger()
        self.method = method

    @staticmethod
    def getVarByID(id):
        return [x for x in globals().values() if id(x) == id]


class TM:
    links = {}
    preventLoop = False

    def __init__(self):
        pass

    def addTrigger(self, variable, trigger, method):
        TM.links[id(variable)] = Link(self, trigger, method)

    @classmethod
    def renameKey(self, old_id, new_id):
        if old_id == new_id:
            return
        link = self.links[old_id]
        del self.links[old_id]
        self.links[new_id] = link


class VP:
    _forbidden = ("_hold", "_current_key", "_current_value")

    def __init__(self):
        self._hold = False
        self._current_key = None
        self._current_value = None

    def __setattr__(self, key, value):
        if key in self._forbidden:
            super().__setattr__(key, value)
            return
        if self._hold:
            self._current_key = key
            self._current_value = value
            super().__setattr__(key, value)
            return
        if key in dir(self):
            old_var = getattr(self, key)
            old_var_id = id(old_var)
            super().__setattr__(key, value)
            new_var = getattr(self, key)
            new_var_id = id(new_var)
            if old_var_id in TM.links:
                TM.renameKey(old_var_id, new_var_id)
                link = TM.links[new_var_id]
                link.trigger.setArgs(old_var, new_var)
                if link.trigger.condition():
                    print("Change: " + str(key) + " = " + str(value))
                    link.method()

        super().__setattr__(key, value)

    def addTrigger(self, variable, trigger, method):
        TM.addTrigger(self, variable, trigger, method)

    def setTriggers(self):
        pass

    def hold(self):
        self._hold = True

    def release(self):
        self._hold = False
        self.__setattr__(self._current_key, self._current_value)


class Trigger:
    def setArgs(self, old_var, new_var):
        self.old_var = old_var
        self.new_var = new_var

    def condition(self):
        return False


class FloatChanged(Trigger):
    def condition(self):
        return self.new_var != self.old_var


class MultipleFloatsChanged(FloatChanged):
    def condition(self):
        return self.new_var != self.old_var


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.update_r()
        self.update_theta()

    def move_x_steps(self, x):
        self.x += x

    def move_y_steps(self, y):
        self.y += y

    def update_theta(self):
        self.theta = atan(self.y / self.x) * 180 / pi

    def update_r(self):
        self.r = sqrt(pow(self.x, 2) + pow(self.y, 2))

    def update_r_and_theta(self):
        self.update_theta()
        self.update_r()
        print("\ttheta = " + str(self.theta))
        print("\tr = " + str(self.r))

    def update_x(self):
        self.x = self.r*cos(self.theta * pi / 180)

    def update_y(self):
        self.y = self.r*sin(self.theta * pi / 180)

    def update_x_and_y(self):
        self.update_x()
        self.update_y()
        print("\tx = " + str(self.x))
        print("\ty = " + str(self.y))


class CustomVector(Vector, VP):
    def __init__(self, x, y):
        VP.__init__(self)
        Vector.__init__(self, x, y)

    def update_r_and_theta(self):
        self.hold()
        super(CustomVector, self).update_r_and_theta()
        self.release()

    def update_x_and_y(self):
        self.hold()
        super(CustomVector, self).update_x_and_y()
        self.release()


class VM(VP):
    vector = CustomVector(3, 4)

    def setTriggers(self):
        pass
        self.addTrigger(self.vector.x, FloatChanged, self.vector.update_r_and_theta)
        self.addTrigger(self.vector.y, FloatChanged, self.vector.update_r_and_theta)
        # self.addTrigger(self.vector.r, FloatChanged, self.vector.update_x_and_y)
        # self.addTrigger(self.vector.theta, FloatChanged, self.vector.update_x_and_y)


class FW:
    tm = None
    vm = None

    def __init__(self):
        self.setTriggerManager(TM)
        self.setVariableManager(VM)
        self.vm.setTriggers()

        start = time()
        self.myActions()
        end = time()

        total_time = (end - start)
        time_per_action = total_time / 1000
        print("Total time: " + str(total_time))
        print("Time per action: " + str(time_per_action))

    def myActions(self):
        for k in range(1, 1000):
            self.vm.vector.x = k

    def setTriggerManager(self, tm):
        self.tm = tm()

    def setVariableManager(self, vm):
        self.vm = vm()


FW()


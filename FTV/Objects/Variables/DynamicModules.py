from queue import Queue

from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicModule import DynamicModuleParent
from FTV.Objects.Variables.DynamicMethods import DyBuiltinMethod
from FTV.Objects.Variables.DynamicObjects import DySwitch, DyObject


class DyModule(DynamicModuleParent, DyObject):
    type = "DynamicModule"
    
    def __init__(self, value=None):
        DyObject.__init__(self, value)
        super(DyModule, self).__init__(value)

    @DyBuiltinMethod()
    def _setupEnvironment(self):
        self._loadBuiltinSelf()

    @DyBuiltinMethod()
    def _loadBuiltinSelf(self):
        self._setupBuiltinVariables()
        self._setupBuiltinMethods()
        self._setupBuiltinTriggers()

    @DyBuiltinMethod()
    def _loadSelf(self):
        self.setupVariables()
        self._setupMethods()
        self.setupTriggers()

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf)\
            .setAction(self.POST_BUILTIN_INIT)\
            # .setThread("thread.main")  # TODO lahav use this line: , "thread.main")
        self.addTrigger(self.POST_BUILTIN_INIT)\
            .setAction(self.PRE_INIT)
        self.addTrigger(self.PRE_INIT)\
            .setAction(self._loadSelf)
        self.addTrigger(self._setupEnvironment)\
            .setAction(self.POST_INIT)

    def _setupBuiltinVariables(self):
        self.POST_BUILTIN_INIT = DySwitch(builtin=True)
        self.PRE_INIT = DySwitch(builtin=True)
        self.POST_INIT = DySwitch()

    def setupVariables(self):
        pass

    def setupTriggers(self):
        pass

    # @staticmethod
    # def _distributeTriggers(dy_object: DynamicObject):
    #     for trigger in dy_object.__triggers__:
    #         if trigger.thread is None:
    #             dy_object.__active_triggers__.put_nowait(trigger)
    #         else:
    #             # TODO lahav Add trigger to its designated thread
    #             pass
    #
    # @staticmethod
    # def _runActiveTriggers(dy_object: DynamicObject):
    #     while not dy_object.__active_triggers__.empty():
    #         dy_object.__active_triggers__.get_nowait().action()

    def __setattr__(self, key, value):
        # try:
        #     getattr(self, key)
        #     is_new_var = False
        # except:
        #     is_new_var = True

        is_new_var = key not in locals()
        # is_new_var = True

        super(DyModule, self).__setattr__(key, value)
        _object = getattr(self, key)
        try:
            if isinstance(_object, DyObject):
                if not is_new_var:
                    Log.p(key, Log.color.BLUE)
                    _object._prepareAndRunTriggers(_object)
                else:
                    _object.__name__ = key
        except:
            pass


    # def __getattribute__(self, item):
    #     return super(DynamicModule, self).__getattribute__(item)


# class DyModuleSwitch(DynamicModule):
#     def __init__(self):
#         super().__init__(False)
#         self.value: bool
#
#     def set(self, value):
#         if value:
#             super(DyModuleSwitch, self).set(True)
#
#         super(DyModuleSwitch, self)._set(False)
#
#     def activate(self):
#         self.set(True)
#
#
# if __name__ == '__main__':
#     bool = DyModuleSwitch()
#     bool.activate()

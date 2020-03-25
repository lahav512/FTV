from AppPackage.Experiments.Log import Log
from FTV.Objects.Variables.AbstractDynamicObject import DynamicModuleParent, DynamicObject, DynamicMethod
from FTV.Objects.Variables.DynamicObject import DySwitch


class DynamicModule(DynamicModuleParent, DynamicObject):
    type = "DynamicModule"

    @DynamicMethod()
    def _setupEnvironment(self):
        self._loadBuiltinSelf()

    @DynamicMethod()
    def _loadBuiltinSelf(self):
        self._setupBuiltinVariables()
        self._setupBuiltinMethods()
        self._setupBuiltinTriggers()

    @DynamicMethod()
    def _loadSelf(self):
        self.setupVariables()
        self._setupMethods()
        self.setupTriggers()

    def _setupBuiltinTriggers(self):
        self.addTrigger(self._loadBuiltinSelf, True, self.POST_BUILTIN_INIT)  # TODO lahav use this line: , "thread.main")
        self.addTrigger(self.POST_BUILTIN_INIT, True, self.PRE_INIT)
        self.addTrigger(self.PRE_INIT, True, self._loadSelf)
        self.addTrigger(self._setupEnvironment, True, self.POST_INIT)

    def _setupBuiltinVariables(self):

        self.POST_BUILTIN_INIT = DySwitch()
        self.PRE_INIT = DySwitch()
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

        super(DynamicModule, self).__setattr__(key, value)
        _object = getattr(self, key)
        try:
            if _object.type == DynamicObject.type:
                if not is_new_var:
                    Log.i("Activated: " + key)
                    _object._distributeTriggers()
                    _object._runActiveTriggers()
                else:
                    _object.__name__ = key
        except:
            pass


    # def __getattribute__(self, item):
    #     return super(DynamicModule, self).__getattribute__(item)

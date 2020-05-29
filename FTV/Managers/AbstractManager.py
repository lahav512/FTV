from FTV.Objects.Variables.DynamicModules import DyBuiltinModule


class AbstractManager(DyBuiltinModule):
    def __init__(self, _is_parent_app=None):
        # Log.p(f"init{self.__class__.__short_name__}: {self.__class__.__name__}")
        self._is_parent_app = _is_parent_app
        super(AbstractManager, self).__init__()

    def init(self):
        pass

    def setupSettings(self):
        pass

    def _setupBuiltinTriggers(self):
        super(AbstractManager, self)._setupBuiltinTriggers()
        self.removeTrigger(self.POST_BUILTIN_INIT)

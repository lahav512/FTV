class SetterTrigger:
    _type = 0

    def __call__(self, *args, **kwargs):
        cond = self.condition()
        if cond is None:
            cond = False
        return cond

    def set_args(self, old_var, new_var):
        self.old_var = old_var
        self.new_var = new_var

    def condition(self):
        return False


class GetterTrigger(SetterTrigger):
    _type = 1


class Used(SetterTrigger):
    def condition(self):
        return self.new_var != self.old_var


class Updated(SetterTrigger):
    def condition(self):
        return True


class Changed(SetterTrigger):
    def condition(self):
        return self.new_var != self.old_var
from FTV.Objects.Conditions import Trigger


class Updated(Trigger.Updated):
    pass


class Changed(Trigger.Changed):
    pass


class ChangedToTrue(Trigger.Changed):
    def condition(self):
        if not self.old_var:
            return self.new_var


class ChangedToFalse(Trigger.Changed):
    def condition(self):
        if self.old_var:
            return not self.new_var

from FTV.Triggers import Any


class Updated(Any.Updated):
    pass


class Changed(Any.Changed):
    pass


class ChangedLessThan(Any.Changed):
    def __init__(self, value):
        self.value = value

    def condition(self):
        is_changed = super().condition()
        if is_changed:
            if self.new_var < self.value:
                return True
        return False


class ChangedGraterThan(Any.Changed):
    def __init__(self, value):
        self.value = value

    def condition(self):
        is_changed = super().condition()
        if is_changed:
            if self.new_var > self.value:
                return True
        return False

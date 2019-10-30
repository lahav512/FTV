from FTV.Objects.VariableParent import VariableParent as VP


class List(list, VP):
    def __init__(self):
        VP.__init__(self)
        list.__init__(self)

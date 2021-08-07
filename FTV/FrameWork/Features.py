from FTV.Objects.Variables.AbstractDynamicModule import DynamicModuleParent


class Feature(DynamicModuleParent):
    pass


# TODO lahav Add a proper mechanism for the loaded features tree.
class NIFeature(Feature):
    pass


class UIFeature(NIFeature):
    pass


from AppPackage.Experiments.GeneralObjects.Dialog import Dialog, Dialog2


class FeatureDemo:
    def __init__(self):
        txt_question = "Would you like to answer the question?"
        btn_yes = "Yes"
        btn_no = "No"
        Dialog.set_item(txt_question, btn_yes, btn_no)

        # txt_question = "One more?"
        # btn_yes = "Fine"
        # btn_no = "Definitely no"
        # Dialog2.set_item(txt_question, btn_yes, btn_no)

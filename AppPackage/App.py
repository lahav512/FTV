from FTV.Managers.ApplicationManager import ApplicationManager

from time import time
from AppPackage.Managers.FeatureManager import FM
from AppPackage.Managers.TriggerManager import TM
from AppPackage.Managers.VariableManager import VM
from AppPackage.Managers.LogManager import LM


class App(ApplicationManager):
    def __init__(self):
        start = time()
        super().__init__()
        end = time()

        # start = time()
        # self.set_managers()
        #
        # for k in range(100):
        #     self.fm.features[0].load_gcode_file()
        #     self.fm.features[0].clean_file()
        #
        # end = time()

        total_time = (end - start)
        time_per_action = total_time
        print("Total time: " + str(total_time))
        print("Time per action: " + str(time_per_action))

    def set_managers(self):
        self.set_variable_manager(VM)
        self.set_feature_manager(FM)
        self.set_trigger_manager(TM)
        self.set_log_manager(LM)


if __name__ == '__main__':
    app = App()

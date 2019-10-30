from FTV.FrameWork import FrameWork

from time import time
from App.Managers.FeatureManager import FM
from App.Managers.TriggerManager import TM
from App.Managers.VariableManager import VM
from App.Managers.LogManager import LM


class Main(FrameWork):
    def __init__(self):
        super().__init__()

        start = time()
        self.my_actions()
        end = time()

        total_time = (end - start)
        time_per_action = total_time
        print("Total time: " + str(total_time))
        print("Time per action: " + str(time_per_action))

    def set_managers(self):
        self.set_feature_manager(FM)
        self.set_trigger_manager(TM)
        self.set_variable_manager(VM)
        self.set_log_manager(LM)

    def my_actions(self):
        pass

        # for k in range(1):
        #
        #     self.features_manager.get(0)\
        #         .load_gcode_file("C:/Users/user/PycharmProjects/ftv/App/ExampleGcodes/AI3M_Beak_B_R_3.gcode")
        #
        #     self.features_manager.get(0)\
        #         .clean_file(k)


if __name__ == '__main__':
    main = Main()

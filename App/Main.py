from FTV.FrameWork import FrameWork

from App.Features.AddPrintToEnvironment import AddPrintToEnvironment
from App.Managers.VM import VM
from App.Managers.TM import TM


class Main(FrameWork):
    def __init__(self):
        super().__init__()

        self.set_variables_manager(VM)
        # self.frame_work.set_triggers_manager(TM)

        self.features_manager.add_multiple(
            AddPrintToEnvironment()
        )

        for k in range(1):

            self.features_manager.get(0)\
                .load_gcode_file("C:/Users/user/PycharmProjects/ftv/App/ExampleGcodes/AI3M_Beak_B_R_3.gcode")

            self.features_manager.get(0)\
                .clean_file(k)


if __name__ == '__main__':
    main = Main()
    print()


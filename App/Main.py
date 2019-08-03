from FTV.FrameWork import FrameWork

from App.Features.AddPrintToEnvironment import AddPrintToEnvironment
from App.Managers.VM import VM
from App.Managers.TM import TM


class Main:
    def __init__(self):
        self.frame_work = FrameWork()

        self.frame_work.set_variables_manager(VM)
        self.frame_work.set_triggers_manager(TM)

        self.frame_work.features_manager.add_multiple(
            AddPrintToEnvironment()
        )

        self.frame_work.features_manager.get(0)\
            .load_gcode_file("C:/Users/user/PycharmProjects/ftv/App/ExampleGcodes/AI3M_Beak_B_R_3.gcode")

        VM.prints_manager.prints[1] = "B"
        #
        # self.frame_work.features_manager.get(0)\
        #     .clean_file(0)


if __name__ == '__main__':
    main = Main()
    print()


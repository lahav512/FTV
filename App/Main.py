from FTV.FrameWork import FrameWork

from App.Features.AddPrintToEnvironment import AddPrintToEnvironment


class Main:
    def __init__(self):
        self.fw = FrameWork()

        self.fw.fm.add_multiple(
            AddPrintToEnvironment()
        )


if __name__ == '__main__':
    Main()

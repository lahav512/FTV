import sys
from pathlib import Path

ROOT_DIR = str(Path(sys.argv[0]).parent.parent.parent.parent).replace("\\", "/") + "/"
sys.path.append(rf"{ROOT_DIR}")
# print(ROOT_DIR)
# exit()

from Experiments.Examples.BIUAutomation.BIUApp import BIUApp

BIUApp()

from Experiments.Examples.Algorithms.CalculationApp import CalculationApp
from FTV.Managers.Log import Log

# Log.setup()
CalculationApp()

# progress = 0
# maximum = 1600
# del_progress = 1 / maximum
# del_x = 0.001
#
# counter = 1
#
# for i in range(maximum):
#     old_val = progress
#     progress += del_progress
#     new_val = progress
#
#     if old_val < del_x*(new_val // del_x):
#         print(round(progress*100, 1))
#         counter += 1
#
# print(round(progress * 100, 1))
# print()
# print(counter)

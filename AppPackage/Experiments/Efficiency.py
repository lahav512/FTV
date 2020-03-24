import time


def check(module, repetitions, tag):
    start = time.time()
    for k in range(repetitions):
        temp_module = module()
    end = time.time()
    total_time = end - start
    # printResult(total_time, tag)
    return total_time

def printResult(_time, tag):
    print(tag + ": " + str(_time))


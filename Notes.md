# Notes

## Architecture

### Threads and Processes
UI thread overloading problem is divided into two issues:
1. The cmd print queue is overloaded. It leads to a delayed print lines even though the program is already done.
2. The DyUIThread is overloaded too. It leads to a massive amount of prints after the program is completed with the wrong variables.
   For example, an algorithm is calling a print status function, but the algorithm is too fast. Therefore, the printed status from some point is always 100%.

__Solutions__
1. Create a port for each thread and send the print commands to the right port. Take a look if there is a builtin solution with the command line for that.
2. Consider adding an option to make a trigger unique, which will make sure that there is only one trigger in a thread with the same address.

* There is still a strange behavior with the unique option.
* Make sure that the unique option works also when a thread is not defined for the trigger.
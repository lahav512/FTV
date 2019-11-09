import tkinter as tk


class A(tk.DoubleVar):
    def doubleVar(self, val):
        """ convenience function to create a tk.DoubleVar and bind it to the collector callback """
        var = tk.DoubleVar()
        var.set(val)
        var.trace('w', self.collectParameters)
        return var


a = A()
a.doubleVar(1)

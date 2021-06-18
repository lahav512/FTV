class Parent:
    def __init__(self):
        self.a = 0


def change(p):
    p.a = 2

p = Parent()
change(p)
print(p.a)
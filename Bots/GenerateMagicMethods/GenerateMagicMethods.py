import os

from Bots.GenerateMagicMethods.FileReader import FileString, FileReader


builtins_file_name = "source/Builtins_3_7.py"
new_file_name = "result/MagicMethodsInterfaces.py"
demo_file_name = "source/MagicMethodsInterfacesDemo.py"

current_dir = os.getcwd().replace("\\", "/") + "/"

builtins_file_path = current_dir + builtins_file_name
new_file_path = current_dir + new_file_name
demo_file_path = current_dir + demo_file_name

# Create the file reader
fileReader = FileReader(builtins_file_path, new_file_name, demo_file_name)

# Create variables
builtin_objects = {
    "object":"DyObject",
    "int":"DyInt",
    "float":"DyFloat",
    "bool":"DyBool",
    "str":"DyStr",
    "list":"DyList",
    "set":"DySet",
    "dict":"DyDict",
    "tuple":"DyTuple",
    "complex":"DyComplex",
    "bytes":"DyBytes",
    "bytearray":"DyByteArray"
}

for key in builtin_objects.keys():
    builtin_objects[key] += "MagicMethods"

compare_methods = [
    "__eq__",
    "__ne__",
    "__ge__",
    "__le__",
    "__gt__",
    "__lt__"
]

single_math_methods = [
    "__neg__",  # ???
    "__pos__",  # ???
    "__trunc__",  # ???
    "__round__",  # ???
    "__ceil__",
    "__floor__",
    "__abs__"
]

dual_math_methods = [
    "__add__",
    "__sub__",
    "__mul__",
    "__floordiv__",  # ???
    "__truediv__",  # ???
    "__divmod__",  # ???
    "__pow__",  # ???
    "__mod__",  # ???
    "__lshift__",  # ???
    "__rshift__",  # ???
    "__and__",  # ???
    "__or__",  # ???
    "__xor__"  # ???
]

i_dual_math_methods = [
    "__add__",
    "__sub__",
    "__mul__",
    "__and__",  # ???
    "__or__",  # ???
    "__xor__"  # ???
]

r_methods = [method.replace("__", "__r", 1) for method in dual_math_methods]

# i_methods = [method.replace("__", "__i", 1) for method in dual_math_methods]

string_methods = [
    "__repr__",
    "__format__",
    "__hash__",
]

iterator_methods = [
    "__index__",
    "__invert__",
    "__contains__",
    "__reversed__",
    "__iter__",
    "__len__"
]

type_methods = [
    "__bool__",
    "__str__",
    "__int__"
]

other_methods = [
    "__index__",
    "__invert__",
    "__contains__",
    "__reversed__",
    "__iter__",
    "__len__"
]

# Create the file reader (include filtering)
fileString = FileString(fileReader.fileData, list(builtin_objects), only_magic_methods=True)

# Replace objects' names
fileString.replaceClassesNames(builtin_objects)
fileString.replaceClassParentsNames(builtin_objects)

fileString.addNewIMethods(
    "self.set({cls}.{method}(self.get(), args[0] + 0, **kwargs))\n"
    "return self",
    i_dual_math_methods
)

fileString.addMethodsContent(
    "return {cls}.{method}(self.get(), *args, **kwargs)",
    compare_methods + single_math_methods + dual_math_methods + r_methods + string_methods + type_methods + iterator_methods
)

fileData = fileString.newFileString.joinFile()
fileReader.saveFile(new_file_name, fileData, demo_file_path, "### CONTENT")
print(fileData)

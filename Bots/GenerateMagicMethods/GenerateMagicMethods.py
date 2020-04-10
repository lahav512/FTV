import os


def openFile(fullpath, lines=True):
    with open(fullpath, 'r') as file:
        if lines:
            file_lines = file.readlines()
        else:
            file_lines = file.read()

    return file_lines

def saveFile(fullpath, data: str):
    with open(fullpath, 'w+') as file:
        file.write(data)

def getType(file_classes, obj_name, method_name):
    methods_list = list(filter(lambda cls: cls.startswith(obj_name), file_classes))[0].split("\n")
    method_lines = list(filter(lambda method_line: method_line.strip().startswith("def {}".format(method_name)), methods_list))
    if method_lines:
        method_line = method_lines[0]
        if "->" in method_line:
            type_name = method_line.rsplit("->", 1)[-1].rsplit(":", 1)[0].strip()
            if type_name == "None":
                return type_name

            if type_name.startswith("_") or type_name[0].upper() == type_name[0]:
                type_name = ""
        else:
            type_name = ""
    else:
        type_name = ""

    return type_name

def isClassOrStaticMethod(line: str):
    # if "@staticmethod" in line:
    #     print()
    line = line.strip()
    return line.startswith("@classmethod") or line.startswith("@staticmethod")

class_name = "{}MagicMethods"

builtin_objects = {
    "object": "DyObject",
    "int": "DyInt",
    "float": "DyFloat",
    "bool": "DyBool",
    "str": "DyStr",
    "list": "DyList",
    "set": "DySet",
    "dict": "DyDict",
    "tuple": "DyTuple"
}

compare_methods = {
    "__eq__",
    "__ne__",
    "__ge__",
    "__le__",
    "__gt__",
    "__lt__"
}

required_methods = {

}

ignored_methods = {
    "__init__"
}

builtins_hint_fullpath = "D:/Program Files/JetBrains/PyCharm Community Edition 2018.3/" \
                         "helpers/typeshed/stdlib/3/builtins.pyi"
builtins_fullpath = "C:/Users/user/.PyCharmCE2018.3/system/python_stubs/599981594/builtins.py"


file_hint_lines = openFile(builtins_hint_fullpath, lines=False).split("class ")

file_lines = openFile(builtins_fullpath)
new_file_lines = []

k = 0

while k < len(file_lines):
    line = file_lines[k]
    k += 1

    # Detect class
    if line.startswith("class "):
        obj_names = list(filter(lambda obj: line.startswith("class " + obj), builtin_objects.keys()))
        if obj_names:
            obj_name = obj_names[0]
            # print(obj_name)
            full_class_name = class_name.format(builtin_objects[obj_name])
            class_header_line = line.replace(obj_name, full_class_name)

            parent_names = list(filter(lambda obj: "({})".format(obj) in class_header_line, builtin_objects.keys()))
            if parent_names:
                parent_name = parent_names[0]
                full_parent_class_name = class_name.format(builtin_objects[parent_name])
                class_header_line = class_header_line.replace(parent_name, full_parent_class_name)

            # Add class header line
            new_file_lines.append("\n\n{}".format(class_header_line))

            k += 1
            method_header_line = ""

            while k < len(file_lines):
                last_method_header_line = method_header_line
                method_header_line = file_lines[k]
                k += 1

                if method_header_line.startswith("    def "):

                    # Get arguments string
                    args_str = method_header_line.split("(", 1)[-1].rsplit(")", 1)[0]
                    method_name = method_header_line.split("def ", 1)[-1].split("(", 1)[0]

                    type_name = getType(file_hint_lines, obj_name, method_name)

                    temp_char = "\n"
                    if isClassOrStaticMethod(last_method_header_line):
                        temp_char = ""

                    if type_name is not "":
                        type_str = ") -> {}: ".format(type_name)
                        method_header_line = type_str.join(method_header_line.split("):", 1))
                    else:
                        method_header_line = method_header_line.replace(": #", ":  #")

                    # Add method header line
                    new_file_lines.append("{}{}".format(temp_char, method_header_line))

                    method_content = "        return {}.{}(self, *args, **kwargs) # TODO Not Implemented\n".format(obj_name, method_name)

                    if args_str == "self, *args, **kwargs" or (method_name in required_methods and method_name not in ignored_methods):
                        if method_name in compare_methods:
                            method_content = "        return {}.{}(self.get(), args[0] + 0, **kwargs)\n".format(obj_name, method_name)
                        else:
                            method_content = "        return {}.{}(self.get(), *args, **kwargs)\n".format(obj_name, method_name)

                    elif args_str in ("*args, **kwargs", "self") or (method_name not in required_methods and method_name in ignored_methods):
                        if isClassOrStaticMethod(new_file_lines[-2]):
                            new_file_lines[-2] = "\n    # " + new_file_lines[-2].strip()

                        new_file_lines[-1] = "\n    # " + new_file_lines[-1].lstrip()
                        method_content = "    #     " + method_content.lstrip()

                    else:
                        method_content = "        pass  # Lahav\n"

                    new_file_lines.append(method_content)

                if isClassOrStaticMethod(method_header_line):
                    new_file_lines.append("\n{}".format(method_header_line))

                elif last_method_header_line == "\n" and method_header_line == "\n":
                    break


methods_file_str = "".join(new_file_lines)
print(methods_file_str)

directory = os.getcwd().replace("\\", "/") + "/result/"
file_name = "MagicMethodsInterfaces.py"

saveFile(directory + file_name, methods_file_str)

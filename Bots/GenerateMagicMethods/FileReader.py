import copy
import os

class FileString(dict):

    SEPARATOR = "%LAHAV%"

    def __init__(self, file_data: str, relevant_classes=None, file_hints_data: str=None):
        super(FileString, self).__init__()
        if relevant_classes is None:
            relevant_classes = []
        self.fileData = file_data
        self.newFileData = ""
        self.newFileString = None
        self.fileHintsData = file_hints_data

        self.classes = []
        self.classesNames = []

        if relevant_classes is None:
            relevant_classes = []
        self.relevantClasses = relevant_classes

        self.sliceFile()

    def sliceFile(self):
        self.__updateClasses()
        self.__updateClassesNames()

        for class_name in self.classesNames:
            self[class_name] = ClassString(self.getClass(class_name))

        self.newFileString = copy.copy(self)

    def joinFile(self):
        file_data = ""
        for cls in self:
            file_data += cls.joinClass() + "\n\n\n"

        return file_data.strip()

    def getFileLines(self) -> [str]:
        return self.fileData.split("\n")

    def __updateClasses(self) -> [str]:
        classes: list = (self.SEPARATOR + "\nclass ").join(self.fileData.split("\nclass ")).split(self.SEPARATOR)[1::]
        classes[-1] = "\n".join(list(filter(lambda cls: cls.startswith("class ") or cls.startswith("    "), classes[-1].split("\n"))))
        classes = list(map(lambda cls: cls.strip(), classes))
        classes = list(filter(lambda cls: cls.replace("class ", "", 1).split("(", 1)[0].split(":", 1)[0] in self.relevantClasses, classes))
        self.classes = classes

    def __updateClassesNames(self) -> [str]:
        self.classesNames = list(map(lambda cls: cls.split("(", 1)[0].split("class ", 1)[-1].split(":", 1)[0], self.getClasses()))

    def getClassesNames(self):
        return self.classesNames

    def getClasses(self):
        return self.classes

    def getClass(self, class_name) -> str:
        return self.getClasses()[self.getClassesNames().index(class_name)]

    def replaceClassesNames(self, rep_dict):
        for old_class, new_class in rep_dict.items():
            self.newFileString[old_class].replaceName(new_class)

    def replaceClassParentsNames(self, rep_dict):
        for cls in self.newFileString:
            for old_parent, new_parent in rep_dict.items():
                cls.replaceParent(old_parent, new_parent)

    def __iter__(self):
        return iter(map(lambda item: item[-1], self.items()))


class ClassString(dict):

    SEPARATOR = "%LAHAV%"

    def __init__(self, class_data: str, relevant_methods: list = None):
        super(ClassString, self).__init__()
        self.classData = class_data

        self.name = None
        self.parents = []
        self.methods = []
        self.methodsNames = []

        if relevant_methods is None:
            relevant_methods = []
        self.relevant_methods = relevant_methods

        self.headerPattern_1 = "class {name}:"
        self.headerPattern_2 = "class {name}({parents}):"
        self.headerPattern = self.headerPattern_2

        self.sliceClass()

    def sliceClass(self):
        self.__updateName()
        self.__updateParents()
        self.__updateMethods()
        self.__updateMethodsNames()

        for method_name in self.getMethodsNames():
            self[method_name] = MethodString(self.getMethod(method_name))
            # self[method_name].setClassName(self.getName())

    def joinClass(self):
        class_data = ""
        for method in self:
            class_data += method.joinMethod() + "\n\n"

        class_data = self.getHeader() + "\n\n" + class_data

        return class_data.strip()

    def __updateMethods(self) -> [str]:
        methods: list = (self.SEPARATOR + "\n    def ").join(self.classData.split("\n    def ")).split(self.SEPARATOR)[1::]
        methods[-1] = "\n".join(list(filter(lambda method: method.startswith("    def ") or method.startswith("        "), methods[-1].split("\n"))))
        methods = list(map(lambda method: "    " + method.strip(), methods))
        self.methods = methods

    def __updateMethodsNames(self) -> [str]:
        self.methodsNames = list(map(lambda method: method.split("(", 1)[0].split("def ", 1)[-1], self.getMethods()))

    def getMethods(self):
        return self.methods

    def getMethodsNames(self):
        return self.methodsNames

    def getMethod(self, method_name) -> str:
        return self.getMethods()[self.getMethodsNames().index(method_name)]

    def __updateName(self):
        self.name = self.classData.split("(", 1)[0].split("class ", 1)[-1]

    def __updateParents(self):
        if "):" not in self.classData.split("\n", 1)[0]:
            self.headerPattern = self.headerPattern_1
            return []

        self.parents = list(map(lambda arg: arg.strip(), self.classData.split("\n", 1)[0].split("#", 1)[0].split("(", 1)[-1].split(")", 1)[0].split(",")))

    def getName(self):
        return self.name

    def getParents(self):
        return self.parents

    def getHeader(self):
        if self.parents:
            header = self.headerPattern.format(name=self.name, parents=str((self.parents)).replace("\'", "")[1:-1:])
        else:
            header = self.headerPattern.format(name=self.name)

        return header

    def replaceName(self, name):
        self.name = name

    def replaceParent(self, old_parent, new_parent):
        if old_parent in self.parents:
            self.parents[self.parents.index(old_parent)] = new_parent

    def __iter__(self):
        return iter(map(lambda item: item[-1], self.items()))

    # def __repr__(self):
    #     return self.classData


class MethodString(str):
    def __init__(self, method_data: str):
        super(MethodString, self).__init__()
        self.methodData = method_data
        self.className = None

        self.name = None
        self.arguments = []

        self.headerPattern_1 = "def {name}({arguments}):"
        self.headerPattern = self.headerPattern_1
        self.content = None

        self.setupMethod()

    def setupMethod(self):
        self.__updateName()
        self.__updateArguments()
        self.__updateContent()

    def joinMethod(self):
        method_data = self.getHeader() + "\n" + self.content

        return "    " + method_data.strip()

    def __updateName(self):
        self.name = self.split("(", 1)[0].split("def ", 1)[-1]

    def __updateArguments(self):
        self.arguments = list(map(lambda arg: arg.strip(), self.split("\n", 1)[0].split("#", 1)[0].split("(", 1)[-1].rsplit(")", 1)[0].replace("\'", "\"").split(",")))

    def __updateContent(self):
        self.content = self.methodData.split("\n", 1)[-1]

    def getName(self):
        return self.name

    def getArguments(self):
        return self.arguments

    def getContent(self):
        return self.content

    def isArgumentExist(self, arg_name):
        return arg_name in self.getArguments()

    def areArgumentsExist(self, *arg_names):
        return bool(set(self.getArguments()) & set(arg_names))

    def areAllArgumentsExist(self, *arg_names):
        return not bool(set(self.getArguments()) - set(arg_names))

    def getHeader(self):
        return self.headerPattern.format(name=self.name, arguments=str(self.arguments).replace("\'", "")[1:-1:])

    def setClassName(self, class_name):
        self.className = class_name

    def getClassName(self):
        return self.className

    # def __repr__(self):
    #     return self.methodData


class FileReader(object):
    def __init__(self, file_path: str, new_file_path: str, demo_file_path: str):
        self.filePath = file_path
        self.newFilePath = new_file_path
        self.demoFilePath = demo_file_path

        self.fileData = self.readFile(self.filePath)
        self.fileDataLines = self.readFileLines(self.filePath)
        self.newFile = ""
        self.newFileLines = []

    @staticmethod
    def readFile(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def readFileLines(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()

    @staticmethod
    def saveFile(file_path, data: str, demo_file_path: str = None, demo_tag: str = None):
        if demo_file_path and demo_tag:
            demo_file_data = FileReader.readFile(demo_file_path)
        else:
            demo_file_data = "."
            demo_tag = "."

        with open(file_path, 'w+') as file:
            file.write(demo_file_data.replace(demo_tag, data))


# class FTVConverter(object):
#     def __init__(self):
#         pass
#
#     def replaceClassNames(self, old_name, new_name):
#         self.fileString[old_name]



if __name__ == '__main__':

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

    for key in builtin_objects.keys():
        builtin_objects[key] += "MagicMethods"

    # Create the file reader (include filtering classes)
    fileString = FileString(fileReader.fileData, list(builtin_objects))

    # Replace objects' names
    fileString.replaceClassesNames(builtin_objects)
    fileString.replaceClassParentsNames(builtin_objects)

    fileData = fileString.newFileString.joinFile()
    fileReader.saveFile(new_file_name, fileData, demo_file_path, "### CONTENT")
    # print(fileData)

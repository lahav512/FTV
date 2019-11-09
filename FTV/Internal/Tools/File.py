

class Any:

    @staticmethod
    def read(fullpath):
        with open(fullpath, 'r') as file:
            return file.read()

    @staticmethod
    def write(fullpath, data):
        with open(fullpath, 'w') as file:
            file.write(data)


class TXT(Any):
    pass

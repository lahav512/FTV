class DatabaseError(Exception):
    pass

class UsernameExist(DatabaseError):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username, \"{self.username}\", is already exist."

class UsernameNotExist(DatabaseError):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The username, \"{self.username}\", is not exist."

class WrongPassword(DatabaseError):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"The password for the username, \"{self.username}\", is wrong."

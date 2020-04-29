class DatabaseError(Exception):
    pass

# UserError

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

# WorkshopError

class WorkshopExist(DatabaseError):

    def __init__(self, username, workshop_name):
        self.username = username
        self.workshop_name = workshop_name

    def __str__(self):
        return f"The workshop, \"{self.workshop_name}\", is already exist in the username, \"{self.username}\"."

class WorkshopNotExist(DatabaseError):

    def __init__(self, username, workshop_name):
        self.username = username
        self.workshop_name = workshop_name

    def __str__(self):
        return f"The workshop, \"{self.workshop_name}\", is not exist in the username, \"{self.username}\"."

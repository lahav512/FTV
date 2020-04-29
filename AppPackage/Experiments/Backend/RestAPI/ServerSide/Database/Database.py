import copy
import json
import os

from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DataStructures import DataStructures as DS
from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DatabaseExceptions import (UsernameExist, WrongPassword,
                                                                                           UsernameNotExist,
                                                                                           DatabaseError)


DS = copy.copy(DS)
current_dir = os.getcwd().replace("\\", "/")
database_path = current_dir + "/database.json"

class Database:
    def __init__(self):
        self.file_path = database_path
        self.users = self.loadFromFile()

    def saveToFile(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file)

    def loadFromFile(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def isUserExist(self, username):
        return username in self.users.keys()

    def checkUser(self, username, password=None):
        if not self.isUserExist(username):
            raise UsernameNotExist(username)

        if password is not None:
            if self.users[username]["account"]["password"] == password:
                return "User has been approved."
            else:
                raise WrongPassword(username)

    def addUser(self, username, password, first_name="", last_name=""):
        if self.isUserExist(username):
            raise UsernameExist(username)

        self.users[username] = DS.user
        account = self.users[username]["account"]
        account["first_name"] = first_name
        account["last_name"] = last_name
        account["password"] = password

    def removeUser(self, username, password):
        if not self.isUserExist(username):
            raise UsernameNotExist(username)

        self.checkUser(username, password)
        del self.users[username]

    def addWorkshop(self, username, password, workshop):
        self.checkUser(username, password)
        self.users[username]["workshops"][workshop] = DS.workshop

    def removeWorkshop(self, username, password, workshop):
        self.checkUser(username, password)
        del self.users[username]["workshops"][workshop]

class DatabaseServer(Database):
    pass


if __name__ == '__main__':
    dbs = DatabaseServer()
    try:
        username = "daniel360"
        password = "1234"

        dbs.addUser(username, password, "Daniel", "Shtibel")
        dbs.addWorkshop(username, password, "apartment")
        # dbs.removeWorkshop(username, password, "apartment")
        # dbs.removeUser(username, password)

    except DatabaseError as e:
        print(e)

    dbs.saveToFile()

    # client = MongoClient('', 27017)
    # db = client.auto_print
    # users = db.users
    #
    # user_1 = {
    #     "username": "lahav512",
    #     "password": "1234",
    #     "first_name": "Lahav",
    #     "last_name": "Svorai"
    # }
    # users.insert_one(user_1)
    #
    # ans = users.find_one(user_1)
    # print(ans)

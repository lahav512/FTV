import copy
import json
import os

from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DataStructures import DataStructures as DS
from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DatabaseExceptions import UsernameExists


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

    def addUser(self, username, password, first_name="", last_name=""):
        if self.isUserExist(username):
            raise UsernameExists(username)

        self.users[username] = DS.user

        account = self.users[username]["account"]
        account["first_name"] = first_name
        account["last_name"] = last_name
        account["password"] = password


class DatabaseServer(Database):
    pass


if __name__ == '__main__':
    dbs = DatabaseServer()
    try:
        dbs.addUser("daniel360", "1234", "Daniel", "Shtibel")
    except UsernameExists as e:
        print(e)

    dbs.saveToFile()

import copy
import os

from pymongo import MongoClient
from pymongo.collection import Collection

from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DataStructures import DataStructures as DS
from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DatabaseExceptions import (UsernameExist, WrongPassword,
                                                                                           UsernameNotExist,
                                                                                           DatabaseError,
                                                                                           WorkshopNotExist,
                                                                                           WorkshopExist)


DS = copy.copy(DS)
current_dir = os.getcwd().replace("\\", "/")
database_path = current_dir + "/database.json"

class Database:
    def __init__(self):
        self.setupMongoDB()

    def setupMongoDB(self):
        self.mongo_db = MongoClient("mongodb+srv://lahavs512:lsd360@autoprint-2kiyr.azure.mongodb.net/test?retryWrites=true&w=majority")

        self.accounts: Collection = self.mongo_db.User.accounts
        self.workshops: Collection = self.mongo_db.User.workshops

    def getAccount(self, username):
        return self.accounts.find_one({"username": username})

    def getWorkshops(self, username):
        return self.workshops.find_one({"username": username})

    def isUserExist(self, username):
        return self.accounts.find_one({"username": username}) is not None

    def isWorkshopExist(self, username, workshop_name):
        return self.workshops.find_one({"username": username, "workshop_name": workshop_name}) is not None

    def checkUser(self, username, password=None):
        if not self.isUserExist(username):
            raise UsernameNotExist(username)

        if password is not None:
            if self.getAccount(username)["password"] == password:
                return "User has been approved."
            else:
                raise WrongPassword(username)

    def addUser(self, username, password, first_name="", last_name=""):
        if self.isUserExist(username):
            raise UsernameExist(username)

        account = DS.Users.account
        account["username"] = username
        account["password"] = password
        account["first_name"] = first_name
        account["last_name"] = last_name

        self.accounts.insert_one(account)

    def removeUser(self, username, password):
        if not self.isUserExist(username):
            raise UsernameNotExist(username)

        self.checkUser(username, password)
        self.accounts.delete_one({"username": username})
        self.workshops.delete_many({"username": username})

    def addWorkshop(self, username, password, workshop_name):
        self.checkUser(username, password)

        if self.isWorkshopExist(username, workshop_name):
            raise WorkshopExist(username, workshop_name)

        workshop = DS.Users.workshop
        workshop["username"] = username
        workshop["workshop_name"] = workshop_name

        self.workshops.insert_one(workshop)

    def removeWorkshop(self, username, password, workshop_name):
        self.checkUser(username, password)
        filter = {"username": username, "workshop_name": workshop_name}

        if not self.workshops.delete_one(filter).deleted_count:
            raise WorkshopNotExist(username, workshop_name)

    def renameWorkshop(self, username, password, old_workshop_name, new_workshop_name):
        self.checkUser(username, password)
        filter = {"username": username, "workshop_name": old_workshop_name}

        if self.isWorkshopExist(username, new_workshop_name):
            raise WorkshopExist(username, new_workshop_name)

        if not self.workshops.update_one(filter, {"$set": {"workshop_name": new_workshop_name}}).modified_count:
            raise WorkshopNotExist(username, old_workshop_name)



class DatabaseServer(Database):
    pass


if __name__ == '__main__':
    dbs = DatabaseServer()
    try:
        # dbs.addUser("daniel360", "1234", "Daniel", "Shtibel")
        # dbs.addUser("lahav512", "1234", "Lahav", "Svorai")
        # dbs.removeUser("daniel360", "1234")

        # dbs.addWorkshop("daniel360", "1234", "Hamama")
        # dbs.addWorkshop("daniel360", "1234", "Apartment")
        # dbs.addWorkshop("lahav512", "1234", "Hamama")

        # dbs.renameWorkshop("daniel360", "1234", "apartment", "Apartment")
        # dbs.renameWorkshop("lahav512", "1234", "apartment", "Apartment")
        pass

    except DatabaseError as e:
        print(e)

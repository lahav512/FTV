import copy
import os

import wrapt
from pymongo import MongoClient
from pymongo.collection import Collection

from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DataStructures import DataStructures as DS
from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DatabaseExceptions import (UsernameExist, WrongPassword,
                                                                                           UsernameNotExist,
                                                                                           DatabaseError,
                                                                                           WorkshopNotExist,
                                                                                           WorkshopExist, StationExist,
                                                                                           StationNotExist)


DS = copy.copy(DS)
current_dir = os.getcwd().replace("\\", "/")
database_path = current_dir + "/database.json"

class WorkshopAddChild(object):
    def __init__(self, child_type):
        super(WorkshopAddChild, self).__init__()
        self.child_type = child_type

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        _args = tuple(list(args) + [self.child_type])
        instance._addWorkshopChild(*_args, **kwargs)
        ans = wrapped(*args, **kwargs)
        return ans

class WorkshopRemoveChild(object):
    def __init__(self, child_type):
        super(WorkshopRemoveChild, self).__init__()
        self.child_type = child_type

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        _args = tuple(list(args) + [self.child_type])
        instance._removeWorkshopChild(*_args, **kwargs)
        ans = wrapped(*args, **kwargs)
        return ans

class WorkshopChildType:
    station = {"type":"Station", "tag":"station"}
    controller = {"type":"Controller", "tag":"controller"}
    printer = {"type":"Printer", "tag":"printer"}
    filament_changer = {"type":"FilamentChanger", "tag":"filament_changer"}
    filament = {"type":"Filament", "tag":"filament"}


class Database:
    def __init__(self):
        self.setupMongoDB()

    def setupMongoDB(self):
        self.mongo_db = MongoClient("mongodb+srv://lahavs512:lsd360@autoprint-2kiyr.azure.mongodb.net/test?retryWrites=true&w=majority")

        self.accounts: Collection = self.mongo_db.User.accounts
        self.workshops: Collection = self.mongo_db.User.workshops

        self.stations: Collection = self.mongo_db.Workshop.stations

    def getAccount(self, username):
        return self.accounts.find_one({"username": username})

    def getWorkshops(self, username):
        return self.workshops.find_one({"username": username})

    def isUserExist(self, username):
        return self.accounts.find_one({"username": username}) is not None

    def isWorkshopExist(self, username, workshop_name):
        return self.workshops.find_one({"username": username, "workshop_name": workshop_name}) is not None

    def isStationExist(self, username, workshop_name, station_name):
        return self.stations.find_one({"username": username, "workshop_name": workshop_name, "station_name": station_name}) is not None

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

    def _addWorkshopChild(self, username, password, workshop_name, child_type, child_name=None, **kwargs):
        self.checkUser(username, password)

        if not self.isWorkshopExist(username, workshop_name):
            raise WorkshopNotExist(username, workshop_name)

        is_child_exist_func = getattr(self, f"is{child_type['type']}Exist")
        child_exception = eval(f"{child_type['type']}Exist")

        if is_child_exist_func(username, workshop_name, child_name):
            raise child_exception(username, workshop_name, child_name)

        child = getattr(DS.Workshops, child_type["tag"])
        child["username"] = username
        child["workshop_name"] = workshop_name
        child[f"{child_type['tag']}_name"] = child_name
        child.update(kwargs)

        self.stations.insert_one(child)

    def _removeWorkshopChild(self, username, password, workshop_name, child_type, child_name=None):
        self.checkUser(username, password)
        filter = {"username": username, "workshop_name": workshop_name, f"{child_type['tag']}_name": child_name}

        child_obj = getattr(self, f"{child_type['tag']}s")
        child_exception = eval(f"{child_type['type']}NotExist")

        if not child_obj.delete_one(filter).deleted_count:
            raise child_exception(username, workshop_name, child_name)

    @WorkshopAddChild(WorkshopChildType.station)
    def addStation(self, username, password, workshop_name, station_name, **kwargs):
        pass

    @WorkshopRemoveChild(WorkshopChildType.station)
    def removeStation(self, username, password, workshop_name, station_name):
        pass

    def renameStation(self, username, password, workshop_name, old_station_name, new_station_name):
        self.checkUser(username, password)
        filter = {"username": username, "workshop_name": workshop_name, "station_name": old_station_name}

        if self.isStationExist(username, workshop_name, new_station_name):
            raise StationExist(username, workshop_name, new_station_name)

        if not self.stations.update_one(filter, {"$set": {"station_name": new_station_name}}).modified_count:
            raise StationNotExist(username, workshop_name, old_station_name)

    @WorkshopAddChild(WorkshopChildType.controller)
    def addController(self, username, password, workshop_name, station_name, **kwargs):
        pass

    @WorkshopRemoveChild(WorkshopChildType.controller)
    def removeController(self, username, password, workshop_name, station_name):
        pass

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

        # station = {"machine_version": "0.1", "firmware_version": "0.1"}
        # dbs.addStation("lahav512", "1234", "Apartment", "Secondary", **station)
        # dbs.addStation("lahav512", "1234", "Hamama", "Hexagon Room", **station)
        # dbs.removeStation("lahav512", "1234", "Apartment", "Secondary")
        # dbs.renameStation("lahav512", "1234", "Apartment", "main", "Main")

        controller = {"machine_version": "0.1", "firmware_version": "0.1"}
        dbs.addStation("lahav512", "1234", "Apartment", **controller)

        pass

    except DatabaseError as e:
        print(e)

import copy
import os

import wrapt
from pymongo import MongoClient
from pymongo.collection import Collection

from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DataStructures import DataStructures as DS
from AppPackage.Experiments.Backend.RestAPI.ServerSide.Database.DatabaseExceptions import *


DS = copy.copy(DS)
current_dir = os.getcwd().replace("\\", "/")
database_path = current_dir + "/database.json"

class WorkshopAddDevice(object):
    def __init__(self, child_type, allow_name=False):
        super(WorkshopAddDevice, self).__init__()
        self.child_type = child_type
        self.allow_name = allow_name

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs: dict):
        args = tuple(str(arg) for arg in args)
        _args = tuple(list(args) + [self.child_type])
        _kwargs = kwargs
        _kwargs["allow_name"] = self.allow_name
        return instance._addWorkshopChild(*_args, **_kwargs)
        # ans = wrapped(*args, **kwargs)
        # return ans


class WorkshopRemoveDevice(object):
    def __init__(self, child_type):
        super(WorkshopRemoveDevice, self).__init__()
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
        self.controllers: Collection = self.mongo_db.Workshop.controllers
        self.filament_changers: Collection = self.mongo_db.Workshop.filament_changers

    def getAccount(self, username):
        return self.accounts.find_one({"username": username})

    def getWorkshops(self, username):
        return self.workshops.find_many({"username": username})

    def getStations(self, username):
        return self.stations.find_many({"username": username})

    def getStation(self, username, workshop_name, station_name, station_id=None):
        _filter = {"username": username, "workshop_name": workshop_name, "station_name": station_name}
        if station_id is not None:
            _filter["device_id"] = station_id

        return self.stations.find_one(_filter)

    def isUserExist(self, username):
        return self.accounts.find_one({"username": username}) is not None

    def isWorkshopExist(self, username, workshop_name):
        return self.workshops.find_one({"username": username, "workshop_name": workshop_name}) is not None

    def isStationExist(self, username, workshop_name, station_name):
        return self.stations.find_one({"username": username, "workshop_name": workshop_name, "station_name": station_name}) is not None

    def isStationRegistered(self, station_id):
        return self.stations.find_one({"device_id": str(station_id)}) is not None

    def isControllerRegistered(self, controller_id):
        return self.controllers.find_one({"device_id": str(controller_id)}) is not None

    def isFilamentChangerRegistered(self, filament_changer_id):
        return self.filament_changers.find_one({"device_id": str(filament_changer_id)}) is not None

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
        _filter = {"username": username, "workshop_name": workshop_name}

        if not self.workshops.delete_one(_filter).deleted_count:
            raise WorkshopNotExist(username, workshop_name)

    def renameWorkshop(self, username, password, old_workshop_name, new_workshop_name):
        self.checkUser(username, password)
        _filter = {"username": username, "workshop_name": old_workshop_name}

        if self.isWorkshopExist(username, new_workshop_name):
            raise WorkshopExist(username, new_workshop_name)

        if not self.workshops.update_one(_filter, {"$set": {"workshop_name": new_workshop_name}}).modified_count:
            raise WorkshopNotExist(username, old_workshop_name)

    def _addWorkshopChild(self, username, password, workshop_name, child_id, child_type, child_name=None, allow_name=False, **kwargs):
        self.checkUser(username, password)
        name_key = f"{child_type['tag']}_name"
        if name_key in kwargs.keys():
            child_name = kwargs[name_key]

        if not self.isWorkshopExist(username, workshop_name):
            raise WorkshopNotExist(username, workshop_name)

        is_child_registered_func = getattr(self, f"is{child_type['type']}Registered")
        child_registered_exception = eval(f"{child_type['type']}Registered")

        if is_child_registered_func(child_id):
            raise child_registered_exception(child_id)

        if allow_name:
            is_child_exist_func = getattr(self, f"is{child_type['type']}Exist")
            child_exist_exception = eval(f"{child_type['type']}Exist")

            if is_child_exist_func(username, workshop_name, child_name):
                raise child_exist_exception(username, workshop_name, child_name)

        child = getattr(DS.Workshops, child_type["tag"]).copy()
        child["username"] = username
        child["workshop_name"] = workshop_name
        if child_name is not None:
            child[f"{child_type['tag']}_name"] = child_name
        child["device_id"] = child_id
        child.update(kwargs)

        child_obj = getattr(self, f"{child_type['tag']}s")
        return child_obj.insert_one(child)

    def _removeWorkshopChild(self, username, password, workshop_name, child_id, child_type):
        self.checkUser(username, password)
        _filter = {"username": username, "device_id": str(child_id), "workshop_name": workshop_name}
        # if workshop_name is not None:
        #     _filter["workshop_name"] = workshop_name
        # if child_name is not None:
        #     _filter[f"{child_type['tag']}_name"] = child_name

        if not self.isWorkshopExist(username, workshop_name):
            raise WorkshopNotExist(username, workshop_name)

        child_obj = getattr(self, f"{child_type['tag']}s")
        child_exception = eval(f"{child_type['type']}NotRegistered")

        result = child_obj.delete_one(_filter)

        if not result.deleted_count:
            raise child_exception(child_id)

        return result

    @WorkshopAddDevice(WorkshopChildType.station, allow_name=True)
    def addStation(self, username, password, workshop_name, station_id, station_name=None, **kwargs):
        pass

    @WorkshopRemoveDevice(WorkshopChildType.station)
    def removeStation(self, username, password, workshop_name, station_id):
        pass

    def renameStation(self, username, password, workshop_name, station_id, new_station_name):
        self.checkUser(username, password)

        if not self.isStationRegistered(station_id):
            raise StationNotRegistered(station_id)

        if self.isStationExist(username, workshop_name, new_station_name):
            raise StationExist(username, workshop_name, new_station_name)

        _filter = {"username": username, "workshop_name": workshop_name, "device_id": str(station_id)}
        self.stations.update_one(_filter, {"$set": {"station_name": new_station_name}})

    @WorkshopAddDevice(WorkshopChildType.controller)
    def addController(self, username, password, workshop_name, controller_id, controller_name=None, **kwargs):
        pass

    @WorkshopRemoveDevice(WorkshopChildType.controller)
    def removeController(self, username, password, workshop_name, controller_id):
        pass

    @WorkshopAddDevice(WorkshopChildType.filament_changer)
    def addFilamentChanger(self, username, password, workshop_name, filament_changer_id, filament_changer_name=None, **kwargs):
        pass

    @WorkshopRemoveDevice(WorkshopChildType.filament_changer)
    def removeFilamentChanger(self, username, password, workshop_name, filament_changer_id):
        pass


class DatabaseServer(Database):
    pass


if __name__ == '__main__':
    dbs = DatabaseServer()
    try:
        # dbs.addUser("doron", "1234", "Doron", "Mashiach")
        # dbs.addUser("lahav512", "1234", "Lahav", "Svorai")
        # dbs.removeUser("daniel360", "1234")

        # dbs.addWorkshop("daniel360", "1234", "Hamama")
        # dbs.addWorkshop("daniel360", "1234", "Apartment")
        # dbs.addWorkshop("lahav512", "1234", "Hamama")

        # dbs.renameWorkshop("daniel360", "1234", "apartment", "Apartment")
        # dbs.renameWorkshop("lahav512", "1234", "apartment", "Apartment")

        # station = {"machine_version": "0.1", "firmware_version": "0.1"}
        # dbs.addStation("lahav512", "1234", "Apartment", 1, station_name="Second Floor", **station)
        # dbs.addStation("daniel360", "1234", "Apartment", 2, station_name="Room", **station)
        # dbs.addStation("lahav512", "1234", "Hamama", 3, station_name="Hexagon Room", **station)
        # dbs.removeStation("daniel360", "1234", "Apartment", 2)
        # dbs.removeStation("lahav512", "1234", "Hamama", 3)
        # dbs.renameStation("lahav512", "1234", "Apartment", 0, "Frist Floor")

        # controller = {"machine_version": "0.1", "firmware_version": "0.1"}
        # dbs.addController("lahav512", "1234", "Apartment", 1, **controller)
        # dbs.addController("lahav512", "1234", "Apartment", 2, **controller)
        # dbs.addController("lahav512", "1234", "Hamama", 3, **controller)
        # dbs.removeController("lahav512", "1234", "Apartment", 1)

        filament_changer = {"min_temp": "205", "max_temp": "240"}
        # dbs.addFilamentChanger("lahav512", "1234", "Apartment", 0, **filament_changer)
        # dbs.addFilamentChanger("lahav512", "1234", "Apartment", 1, **filament_changer)
        dbs.addFilamentChanger("lahav512", "1234", "Apartment", 3, **filament_changer)
        # dbs.removeFilamentChanger("lahav512", "1234", "Apartment", 2)

        print("Action completed successfully.")

    except DatabaseError as e:
        print(e)

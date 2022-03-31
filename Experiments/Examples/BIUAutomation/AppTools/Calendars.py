import abc
from datetime import datetime, timedelta

from ticktick.oauth2 import OAuth2        # OAuth2 Manager
from ticktick.api import TickTickClient   # Main Interface


class Calendar(object):
    @abc.abstractmethod
    def login(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def create(self, event: dict, folder: str=None):
        pass

    @abc.abstractmethod
    def update(self, event: dict, folder: str=None):
        pass

    @abc.abstractmethod
    def isExist(self, event: dict):
        pass

    @abc.abstractmethod
    def delete(self, event: dict = None, event_id=None):
        pass


class TickTick(Calendar):

    class __CustomTickTickClient(TickTickClient):
        def get_by_path(self, path, **kwargs):
            location_list = [item.strip() for item in path.split("/") if item.strip()]
            parent = None

            for directory in location_list:
                item_data = self.get_by_fields(name=directory, **kwargs)
                if not isinstance(item_data, list):
                    item_data = [item_data]

                # lahav This mechanism should be improved.
                for item in item_data:
                    if "groupId" in item.keys() and self.get_by_id(item["groupId"]) is not None:
                        if self.get_by_id(item["groupId"])["name"] == parent["name"]:
                            parent = item
                            break
                    elif parent is None:
                        parent = item

            return parent

    def __init__(self, username, password):
        self.client: TickTick.__CustomTickTickClient
        self.username = username
        self.password = password

    def login(self):
        auth_client = OAuth2(client_id="tHl4Jde4tu9LW062rJ",
                             client_secret="Vt(3#N!(B7ZxL&iUwZLU9)8BeuT9*1!7",
                             redirect_uri="http://127.0.0.1:8080")

        self.client = TickTick.__CustomTickTickClient(self.username, self.password, auth_client)

    def create(self, event: dict, folder: str=None):
        return self.client.task.create(self._generateTask(event, folder))

    def update(self, event: dict, folder: str=None):
        new_task = self._getTask(event, folder).copy()
        new_task.update(self._generateTask(event, folder))
        return self.client.task.update(new_task)

    def isExist(self, task: dict, folder: str=None):
        return bool(self._getTask(task, folder))

    def _getTask(self, task: dict, folder: str=None) -> dict:
        if folder is not None:
            project = self.getProject(folder)

            non_completed_res = self.client.get_by_fields(projectId=project["id"])
            if isinstance(non_completed_res, dict):
                non_completed_res = [non_completed_res]

            res = self.client.task.get_completed(
                datetime.now() - timedelta(days=30),
                datetime.now() + timedelta(days=30)
            )
            if isinstance(res, dict):
                res = [res]

            res += non_completed_res
            res = [item for item in res if item["content"] == task["url"]]
            return next((item for item in res if item["projectId"] == project["id"]), {})

        return self.client.get_by_fields(content=task["url"])

    def _getTaskId(self, task: dict, folder: str=None):
        return self._getTask(task, folder)["id"]

    def getProject(self, path):
        return self.client.get_by_path(path)

    @staticmethod
    def formatDateTime(date, time, addition=0):
        date_list = [int(item) for item in date.split("/")]
        date_list.reverse()
        date_list += [int(item) for item in time.split(":")]
        date_list[-1] += addition
        if all(item == 0 for item in date_list[:-3:-1]):
            date_list[-2] = 23
            date_list[-1] = 59

        full_date = datetime(*date_list)
        return full_date

    def _generateTask(self, event: dict, folder: str, timezone="Asia/Jerusalem"):
        title = event["title"]
        description = event["description"]
        date = event["date"]
        time = event["time"]
        duration = event["duration"]
        due_date = event["end_time"]

        all_day = False
        if "all_day" in event.keys():
            all_day = event["all_day"]

        priority = 1
        if "all_day" in event.keys():
            priority = event["priority"]

        start_date = TickTick.formatDateTime(date, time)

        if due_date is None:
            due_date = TickTick.formatDateTime(date, time, duration)
        else:
            due_date = TickTick.formatDateTime(date, due_date)

        task = self.client.task.builder(
            title=title,
            content=description,
            priority=priority,
            allDay=all_day,
            startDate=start_date,
            dueDate=due_date,
            sortOrder=12345,
            projectId=self.getProject(folder)["id"],
            timeZone=timezone
        )
        return task

    @staticmethod
    def formatDateTime(date, time, addition=0):
        date_list = [int(item) for item in date.split("/")]
        date_list.reverse()
        date_list += [int(item) for item in time.split(":")]
        date_list[-1] += addition
        if all(item == 0 for item in date_list[:-3:-1]):
            date_list[-2] = 23
            date_list[-1] = 59

        full_date = datetime(*date_list)
        return full_date

    def filterTasks(self, local_data, task, local_key="url", task_key="url"):
        return [local_task for local_task in local_data if local_task[local_key].strip().strip("/") == task[task_key].strip().strip("/")]

    def isTaskChanged(self, local_task, task):
        comparison_keys = ("title", "startDate", "endDate")
        for comparison_key in comparison_keys:
            if local_task[comparison_key].strip() != task[comparison_key].strip():
                return True
        return False


class GoogleCalendar(Calendar):
    pass

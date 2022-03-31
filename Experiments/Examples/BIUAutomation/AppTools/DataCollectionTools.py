import abc
import json
import math
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


class Collector(object):
    def __init__(self, username, password, website_url):
        self.username = username
        self.password = password
        self.website_url = website_url
        self.token = None

    @abc.abstractmethod
    def login(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def getEvents(self, *args, **kwargs):
        pass


class Moodle(Collector):
    def login(self, url_ext, with_index=True):
        index_suffix = ""
        if with_index:
            index_suffix = "index.php"

        url_req = f"{self.website_url}{url_ext}{index_suffix}"
        res = requests.get(url_req)
        login_page = res.content

        soup = BeautifulSoup(login_page, "html.parser")
        login_form = soup.find(class_="loginform", id="login")
        self.token = next(item.attrs["value"] for item in login_form.find_all("input") if "name" in item.attrs.keys() and item.attrs["name"] == "logintoken")

        req_action = login_form.attrs["action"]
        req_method = login_form.attrs["method"]

        self.curSession = requests.Session()

        if req_method == "post":
            req_body = {
                "username": self.username,
                "password": self.password,
                "logintoken": self.token
            }
            res_item = self.curSession.post(req_action, data=req_body)
        elif req_method == "get":
            res_item = self.get(req_action)
        else:
            raise Exception(f"Could not start a request method '{req_method}'")

        self.currentHTML = res_item.text
        self.cookies = res_item.cookies

        if res_item.status_code != 200:
            raise Exception(f"Could not log into the website. ErrorCode: {res_item.status_code}")

    def getAllCourses(self):
        soup = BeautifulSoup(self.currentHTML, "html.parser")
        # li_elements = self.driver.find_element_by_id("main-navbar").find_element_by_class_name("navbar-collapse").find_elements_by_tag_name("li")
        li_elements = soup.find(id="main-navbar").find(class_="navbar-collapse").find_all(name="li")
        a_course_elements = next(item.find("ul").find_all("a") for item in li_elements if
             item.find(name="a") and "הקורסים שלי" in item.find(name="a").text)

        courses_data = [{"name": item.attrs["title"], "id": item.text, "link": item.attrs["href"]} for item in a_course_elements if item]
        return courses_data

    def getAllCoursesSchedule(self, coursesData, duration=30):
        for i in range(len(coursesData)):
            course = coursesData[i]
            link = course["link"]
            self.get(link)
            coursesData[i] = self.getCourseHomeworks(course, duration=duration)
        return coursesData

    def getCourseHomeworks(self, course, months=12, duration=30):
        [course.update({f"{item.split('-')[0]}id": item.split("-")[-1]}) for item in self.soup.find("body").attrs["class"] if
         item.startswith("course-") or item.startswith("category-")]
        link = course["link"].split("/course/")[0] + "/lib/ajax/service.php"
        # cookies = self.driver.get_cookies()
        current_datetime = datetime.now()
        year = current_datetime.year
        month = current_datetime.month
        day = current_datetime.day

        sesskey = self.currentHTML.split('"sesskey":')[-1].split(",")[0].strip().replace('"', "")


        req_body = []
        months = 12

        for i in range(months):
            updated_month = (month + i) % 12
            if updated_month == 0:
                updated_month = 12
            req_body.append({
                "methodname": "core_calendar_get_calendar_monthly_view",
                "index": i,
                "args": {
                    "year": int(math.floor(year + (month + i - 1)/12)),
                    "month": int(updated_month),
                    "courseid": int(course["courseid"]),
                    "categoryid": int(course["categoryid"]),
                    "includenavigation": True,
                    "mini": True,
                    "day": 1
                }
            })
            # 66077
            # 2976

        params = {
            "info": "core_calendar_get_calendar_monthly_view",
            "sesskey": sesskey,
        }

        link2 = f"{link}?sesskey={sesskey}&info={'core_calendar_get_calendar_monthly_view'}"
        # requests.post(link, data=req_body, params=params, cookies=cookies)


        # self.curSession.post(link, json=req_body, params=params).json()[0]

        # params = {
        #     "view": "month",
        #     "course": course["courseid"]
        # }

        # link = course["link"].replace("/course/", "/calendar/").split("?")[0]
        res_item = self.post(link, json=req_body, params=params)
        data_list = [item["data"] for item in res_item.json()]
        #
        # td_object_list = [item.find("tbody").find_all("td") for item in
        #               self.soup.find(id="block-region-side-post").find_all(attrs={"data-period": "month"})]
        # td_objects = []
        # [td_objects.__iadd__(item) for item in td_object_list]
        # a_objects = [item.find("a") for item in td_objects if item.find("a")]
        # dates = [item.parent.find("span").text for item in a_objects]

        days_list = [[day for day in item["days"] if day["events"]] for item in data_list[0]["weeks"]]
        days = []
        [days.__iadd__(item) for item in days_list]

        temp_list = [item["weeks"] for item in data_list]
        temps = []
        [temps.__iadd__(item) for item in temp_list]

        temp_list = [item["days"] for item in temps]
        temps = []
        [temps.__iadd__(item) for item in temp_list]

        days = [item for item in temps if item["events"]]

        course["events"] = []
        for day_item in days:
            date = day_item["daytitle"].split(",")[-1].strip()

            temp_day, temp_month, temp_year = [int(item) for item in date.split("/")]
            d = datetime(int(year), int(month), int(day))
            temp_d = datetime(temp_year, temp_month, temp_day)

            if temp_d < d:
                continue

            event_item = {
                "date": date
            }
            for event in day_item["events"]:
                end_time = None
                # print(f'formattedtime: {event["formattedtime"]}')
                formatted_time = event["formattedtime"].strip()

                if "span" in formatted_time:
                    formatted_time = formatted_time.split(">", 1)[-1].rsplit("<", 1)[0].strip()

                if len(formatted_time.split(":")) == 3:
                    time = formatted_time.split("<", 1)[0].strip()
                    end_time = formatted_time.rsplit(">", 1)[-1].strip()

                elif len(formatted_time) == 5 and formatted_time[2] == ":":
                    end_time = formatted_time
                    end_time_digits = end_time.split(":")
                    end_time_minutes = 60*int(end_time_digits[0]) + int(end_time_digits[1])

                    if end_time_minutes == 0:
                        event_item["date"] = self.addDaysToDate(date, -1)

                    end_time_minutes = round(end_time_minutes/15)*15
                    time_minutes = end_time_minutes - duration

                    time_digits = [(time_minutes // 60) % 24, time_minutes % 60]
                    time_digits = [str(item).rjust(2, '0') for item in time_digits]
                    time = ":".join(time_digits)

                    end_time_digits = [(end_time_minutes // 60) % 24, end_time_minutes % 60]
                    end_time_digits = [str(item).rjust(2, '0') for item in end_time_digits]
                    end_time = ":".join(end_time_digits)

                else:
                    raise Exception(f"Could not get the time and end_time of the event: {event['formattedtime']}")

                # print(time, end_time)
                event_item.update({
                    "name": event["name"],
                    "time": time,
                    "end_time": end_time,
                    "url": event["url"],
                    "duration": duration
                })

                course["events"].append(event_item)
        return course

    @staticmethod
    def addDaysToDate(date, addition, _format="%d/%m/%Y"):
        return (datetime(*[int(item) for item in date.split("/")[::-1]]) + timedelta(days=addition)).strftime(_format)

    def get(self, link, params=None):
        res_item = self.curSession.get(link, params=params)
        self.currentHTML = res_item.text
        self.soup = BeautifulSoup(self.currentHTML, "html.parser")
        return res_item

    def post(self, link, json=None, params=None):
        res_item = self.curSession.post(link, json=json, params=params)
        self.currentHTML = res_item.text
        self.soup = BeautifulSoup(self.currentHTML, "html.parser")
        return res_item

    def getEvents(self):
        all_events = []
        urls = []

        # Collect the homework data
        courses = self.getAllCoursesSchedule(self.getAllCourses(), duration=30)

        for course in reversed(courses):
            events = reversed(course["events"])
            for event in events:
                title_parts = event["name"].replace('"', "'").strip("'").split("'")
                title = f'{course["name"]} - {[item.replace("-", " ").strip() for item in title_parts][-1]}'
                url = event["url"]
                event["title"] = title
                event["description"] = url

                if not url or url in urls:
                    continue

                all_events.insert(0, event)
                urls.append(url)

        return all_events

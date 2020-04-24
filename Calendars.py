# This file models the data of a single line of a calendar_dates.txt gtfs file
from Reader import Reader
from pathlib import Path
from collections import defaultdict

class Calendar:

    def __init__(self, line):
        self.start_date = line["start_date"]
        self.service_id = line["service_id"]
        self.end_date = line["end_date"]
        self.mon = line["monday"]
        self.tues = line["tuesday"]
        self.wed = line["wednesday"]
        self.thurs = line["thursday"]
        self.fri = line["friday"]
        self.sat = line["saturday"]
        self.sun = line["sunday"]

class Calendars:

    def __init__(self, path):
        read_calendars = Reader(path / "calendar.txt")
        self.calendars_list = defaultdict(list)
        line = read_calendars.get_line()
        while line:
            service = Calendar(line)
            service_info = {"start" : service.start_date, "end" : service.end_date, "id" : service.service_id}
            if service.mon == "1":
                self.calendars_list["monday"].append(service_info)
            if service.tues == "1":
                self.calendars_list["tuesday"].append(service_info)
            if service.wed == "1":
                self.calendars_list["wednesday"].append(service_info)
            if service.thurs == "1":
                self.calendars_list["thursday"].append(service_info)
            if service.fri == "1":
                self.calendars_list["friday"].append(service_info)
            if service.sat == "1":
                self.calendars_list["saturday"].append(service_info)
            if service.sun == "1":
                self.calendars_list["sunday"].append(service_info)
            line = read_calendars.get_line()
        read_calendars.end()
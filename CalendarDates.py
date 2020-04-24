# This file models the data of a single line of a calendar_dates.txt gtfs file
from Reader import Reader
from pathlib import Path
from collections import defaultdict

class CalendarDate:

    def __init__(self, line):
        self.date = line["date"]
        self.service_id = line["service_id"]
        self.exception_type = line["exception_type"] 
        
class CalendarDates:

    def __init__(self, path):
        read_calendar_dates = Reader(path / "calendar_dates.txt")
        self.calendar_dates_list = []
        line = read_calendar_dates.get_line()
        while line:
            date_info = CalendarDate(line)
            date_dict = {
                "date" : line["date"],
                "service_id" : line["service_id"],
                "exception_type" : line["exception_type"]
            }
            self.calendar_dates_list.append(date_dict)
            line = read_calendar_dates.get_line()
        read_calendar_dates.end()
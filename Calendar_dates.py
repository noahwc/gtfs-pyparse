# This file models the data of a single line of a calendar_dates.txt gtfs file
from Reader import Reader
from Calendar_date import Calendar_date
from pathlib import Path
from collections import defaultdict

class Calendar_dates:

    def __init__(self, path):
        read_calendar_dates = Reader(path / "calendar_dates.txt")
        self.calendar_dates_list = []
        line = read_calendar_dates.get_line()
        while line:
            date_info = Calendar_date(line)
            date_dict = {
                "date" : date_info.date,
                "service_id" : date_info.service_id,
                "exception_type" : date_info.exception_type
            }
            self.calendar_dates_list.append(date_dict)
            line = read_calendar_dates.get_line()
        read_calendar_dates.end()
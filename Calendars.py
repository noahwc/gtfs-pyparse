# This file models the data of a single line of a calendar_dates.txt gtfs file
from Reader import Reader
from Calendar import Calendar
from pathlib import Path

class Calendars:

    def __init__(self, path):
        read_calendars = Reader(path / "calendar.txt")
        self.calendars_list = []
        line = read_calendars.get_line()
        while line:
            self.calendars_list.append(Calendar(line))
            line = read_calendars.get_line()
        read_calendars.end()
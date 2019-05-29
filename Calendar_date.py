# This file models the data of a single line of a calendar_date.txt gtfs file

class Calendar_date:

    def __init__(self, line):
        self.date = line["date"]
        self.service_id = line["service_id"]
        self.exception_type = line["exception_type"]
# This file models the data of a single line of a calendar.txt gtfs file

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
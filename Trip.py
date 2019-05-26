# This file models the data of a single line of a trips.txt gtfs file

class Trip:

    def __init__(self, line):
        self.route_id = line["route_id"]
        self.service_id = line["service_id"]
        self.trip_id = line["trip_id"]
# This file models the data of a single line of a trips.txt gtfs file

class Trip:

    def __init__(self, line):
        self.route_id = line["route_id"]
        self.service_id = line["service_id"]
        self.block_id = line["block_id"]
        self.trip_id = line["trip_id"]
        self.trip_headsign = line["trip_headsign"]
        self.direction_id = line["direction_id"]
        self.shape_id = line["shape_id"]
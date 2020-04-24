from Reader import Reader
from pathlib import Path
from collections import defaultdict

class StopTime:

    def __init__(self, line, trips):
        self.trip_id = line["trip_id"]
        self.departure_time = line["departure_time"]
        self.stop_id = line["stop_id"]
        self.associate_trip(trips)

    def associate_trip(self, trips):
        for trip in trips:
            if self.trip_id == trip.trip_id:
                self.trip = trip
                break

class StopCode:

    def __init__(self, line, trips):
        self.stop_id = line["stop_id"]
        self.stop_code = line["stop_code"]
        self.stop_times = defaultdict(list)


class StopCodes:

    def __init__(self, path, trips):
        read_stop_codes = Reader(path / "stops.txt")
        line = read_stop_codes.get_line()
        self.stop_codes = {}
        while line:
            stop = StopCode(line, trips)
            self.stop_codes[stop.stop_id] = stop
            line = read_stop_codes.get_line()
        read_stop_codes.end()

    def add_stop_time(self, stop_time):
        self.stop_codes[stop_time.stop_id].stop_times[stop_time.trip.service_id].append({"departure_time" : stop_time.departure_time, "route_id" : stop_time.trip.route_id })
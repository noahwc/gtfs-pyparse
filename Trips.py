# This file models the data of a single line of a trips.txt gtfs file
from Reader import Reader
from Trip import Trip
from pathlib import Path

class Trips:

    def __init__(self, path):
        read_trips = Reader(path / "trips.txt")
        self.trip_list = []
        line = read_trips.get_line()
        while line:
            self.trip_list.append(Trip(line))
            line = read_trips.get_line()
        read_trips.end()
# Models a line of a stoptimes.txt gtfs file
from Trips import Trips
from Reader import Reader
from StopTime import StopTime
import os.path
from pathlib import Path
from collections import defaultdict

class StopTimes:

    def __init__(self, path):
        trips = Trips(path)
        print("Trip list created...")
        read_stoptimes = Reader( path / "stop_times.txt")
        line = read_stoptimes.get_line()
        counter = 0
        self.stops = defaultdict(lambda: defaultdict(list))
        while line:
            stop = (StopTime(line, trips.trip_list))
            self.stops[str(stop.stop_id)][str(stop.trip.service_id)].append({"departure_time" : stop.departure_time, "route_id" : stop.trip.route_id })
            line = read_stoptimes.get_line()
            counter = counter + 1
            print(str(counter) + "/~800000 stops parsed.")
        print("Finished parsing stop times...")
        read_stoptimes.end()
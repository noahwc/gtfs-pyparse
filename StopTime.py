# Models a line of a stoptimes.txt gtfs file

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
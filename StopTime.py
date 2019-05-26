# Models a line of a stoptimes.txt gtfs file

class StopTime:

    def __init__(self, line, trips):
        self.trip_id = line["trip_id"]
        self.arrival_time = line["arrival_time"]
        self.departure_time = line["departure_time"]
        self.stop_id = line["stop_id"]
        self.stop_sequence = line["stop_sequence"]
        self.pickup_type = line["pickup_type"]
        self.drop_off_type = line["drop_off_type"]
        self.timepoint = line["timepoint"]
        self.associate_trip(trips)

    def associate_trip(self, trips):
        for trip in trips:
            if self.trip_id == trip.trip_id:
                self.trip = trip
                break
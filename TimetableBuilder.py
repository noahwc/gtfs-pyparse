# Builds a timetable for each stop id
from argparse import ArgumentParser
from StopTimes import StopTimes
from pathlib import Path
from CalendarDates import CalendarDates
from Calendars import Calendars
from StopCodes import StopCodes, StopTime
from Trips import Trips
from Reader import Reader
import os.path
import json
from collections import defaultdict

class TimetableBuilder:

    def __init__(self):
        cli_parser = ArgumentParser()
        cli_parser.add_argument("--gtfs", default="")
        cli_parser.add_argument("--out", default="stops")
        dirs = cli_parser.parse_args()
        gtfs_folder = Path(dirs.gtfs)
        out_folder = Path(dirs.out)
        self.setup_out_dir(dirs.out)
        self.link_stoptimes(gtfs_folder)
        self.write_stops(out_folder)
        exception_dates = CalendarDates(gtfs_folder)
        self.write_dict(exception_dates.calendar_dates_list, out_folder, "exceptions")
        services = Calendars(gtfs_folder)
        self.write_dict(services.calendars_list, out_folder, "services")
        print("Timetables output successfully.")


    def setup_out_dir(self, path):
        if(os.path.isdir(path)):
            print("The secified output directory already exists. Please choose another output directory.")
            quit()
        elif path is not "":
            os.mkdir(path)

    def link_stoptimes(self, path):
        trips = Trips(path)
        stops = StopCodes(path)
        read_stoptimes = Reader( path / "stop_times.txt")
        line = read_stoptimes.get_line()
        counter = 0
        self.stops = StopCodes(path)
        while line:
            stop_time = (StopTime(line, trips.trip_list))
            stops.add_stop_time(stop_time)
            line = read_stoptimes.get_line()
            counter = counter + 1
            print(str(counter) + " stops parsed.")
        print("Finished parsing stop times...")
        read_stoptimes.end()

    def write_stops(self, out_folder):
        print("Writing timetables to file...")
        for stop in self.stops:
            file = open(out_folder / (stop.stop_code + ".json"), 'a')
            json.dump(stop, file, indent = 4)
            file.close()

    def write_dict(self, dictionary, out_folder, filename):
        print("Writing dates to file...")
        file = open(out_folder / (filename +".json"), 'a')
        json.dump(dictionary, file, indent = 4)
        file.close()

gen_tables = TimetableBuilder()
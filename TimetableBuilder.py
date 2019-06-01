# Builds a timetable for each stop id
from argparse import ArgumentParser
from StopTimes import StopTimes
from pathlib import Path
from Calendar_dates import Calendar_dates
from Calendars import Calendars
import os.path
import json

class TimetableBuilder:

    def __init__(self):
        cli_parser = ArgumentParser()
        cli_parser.add_argument("--gtfs", default="")
        cli_parser.add_argument("--out", default="stops")
        dirs = cli_parser.parse_args()
        gtfs_folder = Path(dirs.gtfs)
        out_folder = Path(dirs.out)
        self.setup_out_dir(dirs.out)
        gtfs_processor = StopTimes(gtfs_folder)
        self.write_stops(gtfs_processor.stops, out_folder)
        exception_dates = Calendar_dates(gtfs_folder)
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

    def write_stops(self, dataset, out_folder):
        print("Writing timetables to file...")
        for data in dataset:
            file = open(out_folder / (data + ".json"), 'a')
            json.dump(dataset[data], file, indent = 4)
            file.close()

    def write_dict(self, dictionary, out_folder, filename):
        print("Writing dates to file...")
        file = open(out_folder / (filename +".json"), 'a')
        json.dump(dictionary, file, indent = 4)
        file.close()

gen_tables = TimetableBuilder()
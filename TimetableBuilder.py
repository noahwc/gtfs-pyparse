# Builds a timetable for each stop id
from argparse import ArgumentParser
from StopTimes import StopTimes
from pathlib import Path
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
        self.write_json(gtfs_processor.stops, out_folder)
        print("Timetables output successfully.")


    def setup_out_dir(self, path):
        if(os.path.isdir(path)):
            print("The secified output directory already exists. Please choose another output directory.")
            quit()
        elif path is not "":
            os.mkdir(path)

    def write_json(self, stops, out_folder):
        print("Writing timetables to file...")
        for stop in stops:
            file = open(out_folder / (stop + ".json"), 'a')
            json.dump(stops[stop], file, indent = 4)
            file.close()

gen_tables = TimetableBuilder()
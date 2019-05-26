# Builds a timetable for each stop id
from argparse import ArgumentParser
from StopTimes import StopTimes

cli_parser = ArgumentParser()
cli_parser.add_argument("--gtfs", default="")
cli_parser.add_argument("--out", default="stops")
dirs = cli_parser.parse_args()
gtfs_processor = StopTimes(dirs)
print("Timetables built successfully.")
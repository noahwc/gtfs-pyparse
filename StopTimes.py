# Models a line of a stoptimes.txt gtfs file
from Trips import Trips
from Reader import Reader
from StopTime import StopTime
import os.path
from pathlib import Path

class StopTimes:

    def __init__(self, dirs):
        gtfs_folder = Path(dirs.gtfs)
        out_folder = Path(dirs.out)
        trips = Trips(gtfs_folder)
        print("Trip list created...")
        read_stoptimes = Reader( gtfs_folder / "stop_times.txt")
        line = read_stoptimes.get_line()
        counter = 0
        if(os.path.isdir(dirs.out)):
            print("The secified output directory already exists. Please choose another output directory.")
            quit()
        elif dirs.out is not "":
            os.mkdir(dirs.out)
        while line:
            stop = (StopTime(line, trips.trip_list))
            file = open(out_folder / (stop.stop_id + ".txt"), 'a')
            file.write(stop.departure_time + "," + stop.trip.route_id + "," + stop.trip.service_id + "\n")
            counter = counter + 1
            file.close()
            line = read_stoptimes.get_line()
            print(str(counter) + "/~800000 stops processed.")
        print("Finished parsing stop times...")
        read_stoptimes.end()
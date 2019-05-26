# This class parses a gtfs text file

class Reader:

    def __init__(self, file):
        self.fields = []
        self.fp = open(file, "r")
        self.fields.extend(self.fp.readline().rstrip().split(","))

    def get_line(self):
        data = {}
        line  = self.fp.readline().rstrip().split(",")
        for el, field in zip (line, self.fields):
            data[field] = el
        if len(data) == 1:
            return None
        else:
            return data

    def end(self):
        self.fp.close()
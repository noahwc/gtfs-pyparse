# This class parses a gtfs text file

class Reader:

    def __init__(self, file):
        self.fields = []
        self.fp = open(file, "r")
        fields.extend(fp.readline().split(","))

    
    def get_line(self):
        self.lines = []
        for line in fp:
            lines.extend(line.split(","))
        return lines

    def end(self):
        self.fp.close()

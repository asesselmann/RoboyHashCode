
class Ride:
    def __init__(self, number,params):
        self.number = number
        self.start_row = params[0]
        self.start_col = params[1]
        self.end_row = params[2]
        self.end_col = params[3]
        self.start = params[4]
        self.finish = params[5]

    def distance(self):
        return abs(self.end_row - self.start_row) + abs(self.end_col - self.start_col)

    def time_distance(self):
        return self.finish - self.start



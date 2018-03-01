
class Ride:
    def __init__(self, start_row, start_col, end_row, end_col, start, finish):
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.start = start
        self.finish = finish

    def distance(self):
        return abs(self.end_row - self.start_row) + abs(self.end_col - self.start_col)

    def time_distance(self):
        return self.finish - self.start



import ride


class Vehicle:
    def __init__(self, rides=None):
        self.rides = rides

    def end_time(self):
        distance = 0
        distance += ride.l1_norm(0, 0, self.rides[0].start_row, self.rides[0].start_col)
        distance += self.rides[0].distance
        for i in range(1, len(self.rides)):
            distance += ride.l1_norm(self.rides[i-1].end_row, self.rides[i-1].end_col, self.rides[i].start_row, self.rides[i].start_col)
            distance += self.rides[i].distance

        return distance

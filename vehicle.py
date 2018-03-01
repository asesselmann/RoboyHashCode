class Vehicle:
    def __init__(self, rides=None):
        self.rides = rides

    def output(self):
    	string =  str(len(rides)) + ' '
    	string += ' '.join([rides.number for r in rides])
    	return string

	def rechable(self,ride):
		distance =  abs(self.rides[-1].end_row - ride.start_row) + abs(self.rides.end_col - ride.start_col)
		time =  ride.finish - ride.time_distance - self.end_time
		return time >= distance
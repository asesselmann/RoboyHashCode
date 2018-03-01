import ride
import sys
import random

# read input file
input_file = open(sys.argv[1], 'r')
line = input_file.readline()

R,C,F,N,B,T = line.split()
rides = []
for line in input_file:
    ride_params = [int(r) for r in line.split()]
    rides.append(ride.Ride(ride_params[0], ride_params[1], ride_params[2], ride_params[3], ride_params[4], ride_params[5]))

print rides

random.seed()
assigned_routes = [[x] for x in xrange(F)]
print(assigned_routes)
for i in range(N):
    index = random.randint(F)
    assigned_routes.append(i)

print(assigned_routes)


# calculate solution
vehiclerides = ''
for route in assigned_routes:
    for item in route:
        vehiclerides += item + ' '
    vehiclerides += '\n'

# write output file
out = sys.argv[1][0:-3]+'.out'
fh = open(out, 'w')
fh.writelines(vehiclerides)
fh.close() 
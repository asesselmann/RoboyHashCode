import ride
import sys
import random

# read input file
input_file = open(sys.argv[1], 'r')
line = input_file.readline()

R,C,F,N,B,T = [int(s) for s in line.split()]
rides = []
number = 0
for line in input_file:
	params = [int(r) for r in line.split()]
	rides.append(ride.Ride(number,params))
	number += 1

random.seed()
assigned_routes = [[x] for x in xrange(1,F+1)]
print(assigned_routes)
for i in range(N):
    index = random.randint(0,F-1)
    assigned_routes[index].append(i)

print(assigned_routes)


# calculate solution
vehiclerides = ''
for route in assigned_routes:
    for item in route:
        vehiclerides += str(item) + ' '
    vehiclerides += '\n'

# write output file
out = './solutions/'+sys.argv[1].split('/')[2].split('.')[0]+'.out'
fh = open(out, 'w')
fh.writelines(vehiclerides)
fh.close() 
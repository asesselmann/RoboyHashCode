import ride
import vehicle
import sys

# read input file
file = open(sys.argv[1], 'r')
line =  file.readline()

R,C,F,N,B,T = line.split()
rides = []
for line in file:
	params = [int(r) for r in line.split()]
	rides.append(Ride(params))


# calculate solution


vehiclerides = ''

# write output file
out = './solutions/'+sys.argv[1].split('/')[2].split('.')[0]+'.out'
fh = open(out, 'w')
fh.writelines(vehiclerides)
fh.close() 
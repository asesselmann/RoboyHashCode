import ride
import sys

# read input file
file = open(sys.argv[1], 'r')
line =  file.readline()

R,C,F,N,B,T = line.split()
rides = []
for line in file:
	ride = [int(r) for r in line.split()]
	rides.append(ride)

print rides

# calculate solution


vehiclerides = ''

# write output file
out = sys.argv[1][0:-3]+'.out'
fh = open(out, 'w')
fh.writelines(vehiclerides)
fh.close() 
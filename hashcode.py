# read input file
file = open('./samples/a_example.in', 'r')
line =  file.readline()
R,C,F,N,B,T = line.split()

rides = []
for line in file:
	ride = [int(r) for r in line.split()]
	rides.append(ride)

print rides

# calculate solution

# write output file
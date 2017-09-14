#This program checks qchem output files for the "TIME STEP" number and prints the Time Step
from sys import argv

filename = argv[1]
Object = open(filename, 'r')
TimeStep = 0
for line in Object:
    if "TIME STEP" in line:
	TimeStep += 1 
    else:
	pass

print TimeStep




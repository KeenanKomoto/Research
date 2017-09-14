#This program searches for "Total energy for state" in an ROKS output file and returns the 1st excitation energy (TDDFT) not (TDDFT/TDA)
from sys import argv

filename = argv[1]
Object = open(filename, 'r')
Completion = 0
complete = 0
for line in Object:
    if "Total energy for state" in line:
	Completion = Completion +1
        if Completion == 5:
            Energy=line.split()[5]
    if "Nuclear Repulsion Energy" in line:
        complete = complete +1
        if complete == 2:
	    NucRep=line.split()[4]
  
print filename, Energy, NucRep



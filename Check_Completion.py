#This program checks qchem output files for the term "Thank you very much for using Q-Chem."
from sys import argv

filename = argv[1]
Object = open(filename, 'r')
Completion = False
for line in Object:
    if "Thank you very much" in line:
	Completion = True
	break
    else:
	Completion = False 
if Completion == True:
    print "Completed"
else: 
    print "Gosh Darnit"



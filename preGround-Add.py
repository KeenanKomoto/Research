#!/usr/bin/python
#Run this file on qchem calculations you want to preconverge with a ground state calculation

#This script adds a ground state calculation before the qchem calculation

#Dependencies
from sys import argv
import subprocess
import os

#Variables and arrays
filename = argv[1]
xyz = []

#Job parameters (EDIT TO FIT YOUR NEEDS)
xyz.append("$rem\n")
xyz.append("  exchange  omegaB97X-D\n")
xyz.append("  basis  6-31G(d)\n")
xyz.append("  unrestricted  true\n")
#xyz.append("")
#xyz.append("")
#xyz.append("")

#Don't touch these ones
xyz.append("$end\n\n\n")
xyz.append("$molecule\n")

#Extract the xyz coordinates and charge/multiplicity from the original QChem input file and store in file named "temp"
#Could clean this up to store in array as above but am too lazy at the moment
with open(filename) as F, open('temp', 'w') as tmp:
    copy = False
    stopper = 0
    for line in F:
            if line.strip() == "$molecule":
                copy = True
            elif line.strip() == "$end":
                stopper += 1
                copy = False
            elif copy and stopper != 2:
                    xyz.append(line)
xyz.append("$end\n\n\n")
xyz.append("@@@\n\n\n")

#Read the original file and store in "a"
f1 = open(filename, 'r')
a = f1.readlines()

#Put the new ground state calculation and original file 'together'
together = xyz + a

#Overwrite the original file with the new calculation (ground state followed by original calculation)
F = open(filename, 'w')
for i in range(len(together)):
    F.write(together[i])
F.close()

#Remove the "temp" file that was storing the xyz/ground state calculation information
os.remove("temp")



















####################################################################################
####################################################################################
#####OLD STUFF, using Bash to do all the heavy work#################################
#with open("temp", 'a') as t:
#    t.write("$end\n")
#subprocess.Popen("sed -i '1i\$rem' temp; sed -i '2i\ \ exchange\ \ omegaB97X-D' temp; sed -i '3i\ \ basis\ \ 6-31G\(d\)' temp; sed -i '4i\ \ unrestricted\ \ true' temp; sed -i '5i\$end' temp; sed -i '6i\$molecule' temp; cat AT >> temp", shell=True, executable='/bin/bash')
#
#tmp.close()
#
#subprocess.Popen("./prepend.sh temp %s" %filename, shell=True, executable='/bin/bash')
####################################################################################
####################################################################################

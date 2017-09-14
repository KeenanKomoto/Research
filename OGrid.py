#This code generates a grid of oxygen molecules
#from sys import argv
from numpy import sqrt 
from os import system
 

# Working with file I/O
#filename = "O2file.xyz"
#file = open(filename,'w')
#
#var = 2
#file.write("%d" % var)
#file.close()

#Defining a function for using decimals in range
def frange(x, y, step):
  while x < y:
    yield x
    x += step

#Defining a function to compare distances between bodipy molecule
def dist_check(x,y,z):
    file=open("Bodipy_Coordinates")
    for line in file:
        xB,yB,zB=float(line.split()[1]),float(line.split()[2]),float(line.split()[3])
        distance=sqrt((x-xB)**2+(y-yB)**2+(z-zB)**2)
        if distance < 1.5:
	   # print "SHUCKS"
	    file.close() 
            return False
    file.close()
    return True
#Define same function for second Oxygen molecule with x2
#def dist_check2(x,y,z):
#  file=open("Bodipy_Coordinates")
#  for line in file:
#      xB,yB,zB=line.split()[1],line.split()[2],line.split()[3]
#      distance=sqrt((x2-xB)**2+(y-yB)**2+(z-zB)**2)
#      if distance < 0.5:
#          return False
#  return True
#

#Generate range of Oxygen molecules
#for loop: range starting at -15, go to 15 in 2.5 increments
#print: %s is variable "O", % variable, 6.2f space 6 spaces and print to 2 decimal places (float numbers)
counter=0
for x in frange(-6., 6., 1.):
    for y in frange(-6., 6., 1.):
	for z in frange(-4., 4., 1.):
	    x2 = x + 1.
	    if dist_check(x,y,z)==True and dist_check(x2,y,z)==True:
	        counter= 1+counter
		filename="OBodipy%d.in" %counter
		system("cat IncompleteBodipy.in > %s"%filename)
		file=open(filename, "a")
	        file.write("%s%-3.5f%12.6f%12.7f \n" % ("O    	   ",x,y,z))
	        file.write("%s%-4.5f%12.6f%12.7f \n" % ("O          ",x2,y,z))
	        file.write("$end")
		file.close()
            #else:
	     #   print '?'
	    

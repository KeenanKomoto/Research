#This script increments the xyz coordinates of a molecular system to separate an ethylene from an tetrafluoroethylene
from sys import argv

#initiate array
samelines=[]
newlines=[]

#open file (user input file) and read through the lines after the first two comments of an xyz file
#store the xyz coordinates in "newlines"
f = open(argv[1])

num = f.next()
comment = f.next()
linecount = 0

while True:
	try:
		if linecount <= 5:
			y = f.next()
			samelines.append(y)
			linecount += 1
		else:
			z = f.next().split()
			newlines.append(z)
	except StopIteration:
		break

#add 0.5Angstroms to the z-coordinates of a molecule and write the full coordinates to a new file titled "(filename)_i.xyz"
#then close the file
for i in range(1, 50):
	file=open(argv[1][:8]+"_"+str(0.5*i)+".xyz", 'w')
	for h in range(len(samelines)):
		file.write(str(samelines[h]))
	for j in range(len(newlines)):
		file.write(newlines[j][0]+'         '+newlines[j][1]+'        '+str(float(newlines[j][2])+(0.5*i))+'        '+newlines[j][3]+'\n')
	file.close()


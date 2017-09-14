import matplotlib.pyplot as plt
import numpy as np
from sys import argv


def g(f, i, x, vib):
    sigma = 10.
    x0 = np.ones(len(x))
    x0 *= f[vib]
    return i[vib]*np.exp(-(x-x0)**2/(sigma**2))

def L(f, i, x, vib):
    gamma = 0.4
    x0 = np.ones(len(x))
    x0 *= f[vib]
    return i[vib]*(1/np.pi)*((0.5*gamma)/(((x-x0)**2)+((0.5*gamma)**2)))


filename = argv[1]
file=open(filename,'r')
listx = []
listy = [] 

for line in file:
    if "Frequency:" in line:
	x1 = float(line.split()[1])
	x2 = float(line.split()[2])
	x3 = float(line.split()[3])
        listx.append(x1) 
        listx.append(x2) 
        listx.append(x3) 
    elif "Raman Intens:" in line:
	y1 = float(line.split()[2])
	y2 = float(line.split()[3])
	y3 = float(line.split()[4])
        listy.append(y1) 
        listy.append(y2) 
        listy.append(y3) 

nvib = len(listy)
arrayx = np.array(listx)
arrayy = np.array(listy)

resolution = 0.01
rangemin = 1500 
rangemax = 2000
grid = np.array(np.arange(rangemin, rangemax, resolution))
lineshape = np.zeros((rangemax-rangemin)/resolution)
for vib in range(nvib):
    lineshape = lineshape + L(arrayx, arrayy, grid, vib)

plt.plot(grid, lineshape)
#fig, ax = plt.subplots()
#ax.stem(arrayx, arrayy, markerfmt=' ')
plt.show()

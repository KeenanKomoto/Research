#!/usr/bin/python

#Note that this program uses the "Standard Nuclear Orientation" xyz coordinates in Q-Chem instead of the user input.
##Difference is that the Standard Nuclear Oriengation is a translation and rotation of the molecule(s). Distances/bond lengths are the same but coordinates are different than the original input


from sys import argv
from tkowalcz import molstruct as mol
import numpy as np

#Grab xyz
QCout = argv[1]
xyz = mol.Molecule(QCout)

#Get 3 Points on BODIPY molecule
A = np.array(xyz.coordinates.cartesians[9])
B = np.array(xyz.coordinates.cartesians[4])
C = np.array(xyz.coordinates.cartesians[18])

#Get O2 Coordinates
O1 = np.array(xyz.coordinates.cartesians[48])
O2 = np.array(xyz.coordinates.cartesians[49])

#Define 2 Vectors BODIPY
AB = A-B
CB = C-B

#Define O2 Vector
O = O1-O2

#Take cross product, X is the normal vector
X = np.cross(AB, CB)

#Solve for angle between Oxygen and BODIPY
numer = abs(np.dot(X, O))
#denom = np.dot(abs(X), abs(O))
denom = np.dot(np.linalg.norm(X), np.linalg.norm(O))
division = numer/denom
angle = np.arcsin(division)
degree = np.degrees(angle)

print degree








#########Unnecessary equation for plane################
##One point
#a1 = A[0]
#a2 = A[1]
#a3 = A[2]
#
##Define equation for plane
#x1 = X[0]
#x2 = X[1]
#x3 = X[2]
#d = a1*x1 + a2*x2 + a3*x3
#print xyz.coordinates.atomic_symbols
#print xyz.coordinates.cartesians
#print xyz.coordinates.atomic_symbols[49]
#print xyz.coordinates.cartesians[49]

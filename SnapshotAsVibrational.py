#!/usr/bin/python
#This script computes a value (weight) of how much a specific molecule's vibrational
#mode contributes to distorting an optimized geometry to a "snapshot" geometry

#***Note*** This script was made in collaboration with my research advisor:
#           Dr. Tim Kowalczyk

from sys import argv
from numpy import argsort, array, cos, dot, pi, reshape, sort
from scipy.linalg import inv, norm
from os import mkdir
from tkowalcz import molstruct as mol, qchem as q


class vibration:
    ''' Contains frequency and displacement for a vibration '''

    def __init__(self, filename=None, vib=1):
        file=open(filename,'r')
        in_displacement_section = False
        frequency_found = False
        self.disp = mol.Molecule()
        deadspace_counter = 7
        freq_counter = 0
        for line in file:
            if in_displacement_section:
                if "TransDip" in line:
                    in_displacement_section = False
                    break
                if (vib%3==0):
                    symbol = line.split()[0]
                    x      = float(line.split()[1])
                    y      = float(line.split()[2])
                    z      = float(line.split()[3])
                elif (vib%3==1):
                    symbol = line.split()[0]
                    x      = float(line.split()[4])
                    y      = float(line.split()[5])
                    z      = float(line.split()[6])
                elif (vib%3==2):
                    symbol = line.split()[0]
                    x      = float(line.split()[7])
                    y      = float(line.split()[8])
                    z      = float(line.split()[9])
                self.disp.append_atom(symbol,x,y,z)
            if frequency_found and deadspace_counter == 6:
                #Read displacements
                in_displacement_section = True
            if 'Frequency:' in line:
                if freq_counter > vib/3-1:
                    frequency_found = True
                    self.frequency = line.split()[1]
                    deadspace_counter = 0
                freq_counter = freq_counter + 1
            deadspace_counter += 1


def main(argv):
    ''' Express snapshot coordinates S as linear combinations
        of normal vibrational modes Q: S = S0 + QC           
        Only grab coordinates, displacements for atoms 3
        through N in order to ensure invertibility of Q      '''
    # Read in the optimized geometry
    geom_opt = mol.Molecule(argv[1])

    # Get number of atoms and number of vib modes
    x= geom_opt.num_atoms()
    nvib = 3*x-6
 
    # Store optimized coordinates as a column vector in S0
    S0 = reshape(geom_opt.coordinates.cartesians,3*x)
    S0 = S0[6:]

    # Get snapshot geometry, store as a column vector in S
    snapshot = mol.Molecule(argv[2])
    S = reshape(snapshot.coordinates.cartesians,3*x)
    S = S[6:]
 
    # Get all normal vibrational modes (Q Matrix)
    all_vibrations=[]
    for v in range(3*x-6):
	this_vib=vibration(argv[3],v)
	#all_vibrations.append(this_vib)
	all_vibrations.append(this_vib.disp.coordinates.cartesians[2:])
    all_vibrations=array(all_vibrations)
    Q = reshape(all_vibrations,(3*x-6,-1))

    # Solve S = S0 + QC for C
    # C = Q^(-1)*(S-S0)
    C = dot(inv(Q),(S-S0))
    C /= norm(C)

    # Display results
    print "%10s%10s" % ('Mode','|Weight|')
    print "--------------------"

    # Sorted by absolute value:
    #C_weights = -sort(-abs(C))
    #C_modes = argsort(-abs(C))

    # Sorted by weight:
    #C_weights = sort(C)
    #C_modes = argsort(C)

    # Sorted by mode number (i.e. by frequency):
    C_weights = C
    C_modes = range(3*x-6)

    for i in range(3*x-6):
        print "%10d%10.4f" % (C_modes[i],C_weights[i])

    ''' 
    # Sanity check: Reconstruct snapshot from decomposition
    # First insert the two fixed atoms
    print snapshot.coordinates.cartesians[0]
    print snapshot.coordinates.cartesians[1]
    # Then calculate the rest by reconstruction from C
    T = S0 + dot(Q,C)
    print reshape(T,(x-2,3))
    '''
    return



def vibview(r0,dr):
    ''' Create a set of xyz files from reference geometry r0 and displacements dr to visualize a vibrational mode '''


    # Different names for different vibs?
    mkdir('vibview')
    listfile = open('vibview/vib.list','w')

    resolution = 48
    for itheta in range(resolution):
        outfilename = 'vibview/vib.' + str(itheta) + '.xyz'
        outfile = open(outfilename,'w')
        theta = itheta*(2.*pi)/resolution
        r = r0
        r.coordinates.cartesians = array(r0.coordinates.cartesians)\
                      +cos(theta)*array(dr.coordinates.cartesians)
#        print r.coordinates.cartesians
#	print dr.coordinates.cartesians
        r.coordinates.write_cartesians(outfile)
        outfile.close()
        listfile.write('vib.' + str(itheta) + '.xyz\n')
    listfile.close()
    return


#main(argv)
if __name__=='__main__':
    if len(argv) == 4:
        main(argv)
    else:
        print "usage: %s [Optimized Reference Geometry] [Snapshot Geometry] [Vibrational Q-Chem outputfile]" % argv[0]


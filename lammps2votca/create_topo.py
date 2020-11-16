import pandas as pd
import numpy as np
import csv

from chemfiles import Trajectory

class Topo(object):

    def __init__(self,system):
        self.system=system

    def chemfile_read(self,filename,format_='LAMMPS Data'):
        data = Trajectory(filename,format=format_)
        frame=data.read()
        topology=frame.topology
        self.numberatom_permole=int(len(frame.atoms)/self.system.Number_Moles)
        self.atoms=frame.atoms
        self.bonds=topology.bonds[0:int(topology.bonds.shape[0]/self.system.Number_Moles)]+1
        self.angles=topology.angles[0:int(topology.angles.shape[0]/self.system.Number_Moles)]+1
        self.dihedrals=topology.dihedrals[0:int(topology.dihedrals.shape[0]/self.system.Number_Moles)]+1

    def output(self,file_=None):
        votca_file=open(file_,"w")
        with votca_file:
            writer=csv.writer(votca_file,delimiter='\t',
                            quotechar='\t', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['<topology name=\''+self.system.name+'\'>'])
            writer.writerow(['<molecules>'])
            writer.writerow(['<clear  />'])
            writer.writerow(['<molecule name=\''+self.system.name+'\' nmols=\''+str(self.system.Number_Moles) +'\' nbeads=\''+str(self.numberatom_permole)+'\'>'])
            for beadii in range(int(self.numberatom_permole)):
                writer.writerow(['<bead name =\''  + str(beadii+1)+ '\' type=\''+ str(self.atoms[beadii].type)+'\' mass=\''+str(self.atoms[beadii].mass)+ '\' q=\''+str(self.atoms[beadii].charge)+'\' />'])   
            writer.writerow(['</molecule>'])
            writer.writerow(['</molecules>'])
            writer.writerow(['<bonded>'])
            writer.writerow(['<bond>'])
            writer.writerow(['<name>bond</name>'])
            writer.writerow(['<beads>'])
            for bondii in range(int(self.bonds.shape[0])):
                writer.writerow([self.system.name+":"+str(self.bonds[bondii][0])+"   "+self.system.name+":"+str(self.bonds[bondii][1])])
            writer.writerow(['</beads>'])
            writer.writerow(['</bond>'])
            writer.writerow(['<angle>'])
            writer.writerow(['<name>angle</name>'])
            writer.writerow(['<beads>'])
            for angleii in range(int(self.angles.shape[0])):
                writer.writerow([self.system.name+":"+str(self.angles[angleii][0])+"   "+self.system.name+":"+str(self.angles[angleii][1])+"   "+self.system.name+":"+str(self.angles[angleii][2])])
            writer.writerow(['</beads>'])
            writer.writerow(['</angle>'])
            writer.writerow(['<dihedral>'])
            writer.writerow(['<name>dihedral</name>'])
            writer.writerow(['<beads>'])
            for dihedralii in range(int(self.dihedrals.shape[0])):
                writer.writerow([self.system.name+":"+str(self.dihedrals[dihedralii][0])+"   "+self.system.name+":"+str(self.dihedrals[dihedralii][1])+"   "+self.system.name+":"+str(self.dihedrals[dihedralii][2])+"   "+self.system.name+":"+str(self.dihedrals[dihedralii][3])])
            writer.writerow(['</beads>'])
            writer.writerow(['</dihedral>'])
            writer.writerow(['</bonded>'])
            writer.writerow(['</topology>'])


    
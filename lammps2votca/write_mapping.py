import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv


class Mapping(object):
    def __init__(self,System=None,Structure=None,Topo=None,filename=None):
        self.filename=filename
        self.Structure=Structure
        self.System=System
        self.mass=self.System.mass
        self.Topo=Topo

    def create_BeadMap(self,Type=None):
        BeadMap_list=[]
        Monomer1=np.array(self.Structure.Beads[Type])
        BeadMap_list.append(Monomer1)
        for monmerii in range(1,self.System.Number_Monomers):
            mapping=np.array(self.Structure.Beads[Type])+len(self.Structure.Monomer_le)+len(self.Structure.Monomer_i)*(monmerii-1)
            BeadMap_list.append(mapping)
        BeadMap=np.array(BeadMap_list)
        return BeadMap

    def create_BondTopo(self,Type=None):
        Bonds=[]
        Beads=self.Structure.Bonds[Type]
        if Beads[0]==Beads[1]:
            for beadii in range(self.System.Number_Monomers-1):
                bond=[Beads[0]+str(beadii+1),Beads[0]+str(beadii+1+1)]
                Bonds.append(bond)
        else:
            for beadii in range(self.System.Number_Monomers):
                bond=[Beads[0]+str(beadii+1),Beads[1]+str(beadii+1)]
                Bonds.append(bond)
        return Bonds

    def create_AngleTopo(self,Type=None):
        Angles=[]
        Beads=self.Structure.Angles[Type]
        if Beads[0]==Beads[1] and Beads[1] ==Beads[2]:
            for beadii in range(self.System.Number_Monomers-2):
                angle=[Beads[0]+str(beadii+1),Beads[0]+str(beadii+1+1),Beads[0]+str(beadii+2+1)]
                Angles.append(angle)
        elif Beads[0]==Beads[1] or Beads[1] ==Beads[2]:
            for beadii in range(self.System.Number_Monomers-1):
                if Beads[0]==Beads[1]:
                    angle=[Beads[0]+str(beadii+1),Beads[0]+str(beadii+1+1),Beads[2]+str(beadii+1+1)]
                    Angles.append(angle)
                else:
                    angle=[Beads[1]+str(beadii+1),Beads[2]+str(beadii+1+1),Beads[0]+str(beadii+1+1)]
                    Angles.append(angle)
        return Angles

    def create_DihedralTopo(self,Type=None):
        Dihedrals=[]
        Beads=self.Structure.Dihedrals[Type]
        if Beads[0]==Beads[1] and Beads[1] ==Beads[2] and Beads[2] ==Beads[3]:
            for beadii in range(self.System.Number_Monomers-3):
                dihedral=[Beads[0]+str(beadii+1),Beads[0]+str(beadii+1+1),Beads[0]+str(beadii+2+1),Beads[0]+str(beadii+3+1)]
                Dihedrals.append(dihedral)
        else:
            for beadii in range(self.System.Number_Monomers-1):
                dihedral=[Beads[0]+str(beadii+1),Beads[1]+str(beadii+1),Beads[2]+str(beadii+1+1),Beads[3]+str(beadii+1+1)]
                Dihedrals.append(dihedral)
        return Dihedrals

    def write(self):
        with open(self.filename,'w') as write_f:
            write_f.write('<cg_molecule>\n')
            write_f.write('<name>'+self.Structure.Name+'</name>\n')
            write_f.write('<ident>'+self.Structure.Name+'</ident>\n')
            write_f.write('<topology>\n')
            write_f.write('<cg_beads>\n')
            atomindex=0
            for beadii in range(1,self.Structure.BeadIndexs+1):
                
                Type=self.Structure.CoarseGrainedBeads[beadii].Type
                BeadMap=self.Structure.CoarseGrainedBeads[beadii].Mapping
                AtomIndex=self.Structure.CoarseGrainedBeads[beadii].IndexList
                write_f.write('<cg_bead>\n')
                write_f.write('<name>'+Type+str(beadii)+'</name>\n')
                write_f.write('<type>'+Type+'</type>\n')
                write_f.write('<mapping>'+BeadMap+'</mapping>\n')
                write_f.write('<beads>\n')
                for atomii in AtomIndex:
                    #print(atomii)
                    write_f.write('1:'+self.Structure.Name+':'+str(atomii+1+atomindex)+"\n")
                    
                atomindex=atomindex+len(AtomIndex)
                write_f.write('</beads>\n')
                write_f.write('</cg_bead>\n')
            write_f.write('</cg_beads>\n')

            write_f.write('<cg_bonded>\n')
            for bondtypeii in self.Structure.BondsTypes:
                Type=bondtypeii
                write_f.write('<bond>\n')
                write_f.write('<name>bond'+Type+'</name>\n')
                write_f.write('<beads>\n')
                BondTopo=self.create_BondTopo(Type=Type)
                for bondii in BondTopo:
                    write_f.write(bondii[0]+' '+bondii[1]+"\n")
                write_f.write('</beads>\n')
                write_f.write('</bond>\n')

            for angletypeii in self.Structure.AnglesTypes:
                Type=angletypeii
                write_f.write('<angle>\n')
                write_f.write('<name>angle'+Type+'</name>\n')
                write_f.write('<beads>\n')
                Topo=self.create_AngleTopo(Type=Type)
                for ii in Topo:
                    write_f.write(ii[0]+' '+ii[1]+' '+ii[2]+"\n")
                write_f.write('</beads>\n')
                write_f.write('</angle>\n')

            for dihedraltypeii in self.Structure.DihedralsTypes:
                Type=dihedraltypeii
                write_f.write('<dihedral>\n')
                write_f.write('<name>dihedral'+Type+'</name>\n')
                write_f.write('<beads>\n')
                Topo=self.create_DihedralTopo(Type=Type)
                for ii in Topo:
                    write_f.write(ii[0]+' '+ii[1]+' '+ii[2]+' '+ii[3]+"\n")
                write_f.write('</beads>\n')
                write_f.write('</dihedral>\n')

            write_f.write('</cg_bonded>\n')
            write_f.write('</topology>\n')
            write_f.write('<maps>\n')
            
            Mappings=[]
            for beadii in range(1,self.Structure.BeadIndexs+1):
                Mapping=self.Structure.CoarseGrainedBeads[beadii].Mapping
                if Mapping not in Mappings:

                    write_f.write('<map>\n')
                    write_f.write('<name>'+Mapping+'</name>\n')
                    write_f.write('<weights>\n')
                    Index=self.Structure.CoarseGrainedBeads[beadii].IndexList
                    for indexii in Index:
                        typeii=self.Topo.atoms[indexii].type
                        write_f.write(str(self.mass[self.Structure.AtomIndex2Name[int(typeii)]])+" ")
                    write_f.write("\n")
                    write_f.write('</weights>\n')
                    write_f.write('</map>\n')
                    Mappings.append(Mapping)
            
            write_f.write('</maps>\n')

            write_f.write('</cg_molecule>\n')

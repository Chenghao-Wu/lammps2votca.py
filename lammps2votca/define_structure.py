import pandas as pd
import numpy as np
import csv


class CoarseGrainedBead(object):
    def __init__(self,Type=None,Mapping=None,IndexList=None):
        self.Type=Type
        self.Mapping=Mapping
        self.IndexList=IndexList

class Structure(object):
    def __init__(self,Name=None):
        self.Name=Name
        self.AtomIndex2Name={}
        self.AtomName2Index={}
        self.Beads={}
        self.Numbers=[]
        self.Types=[]
        self.BondsTypes=[]
        self.AnglesTypes=[]
        self.DihedralsTypes=[]
        self.Bonds={}
        self.Angles={}   
        self.Dihedrals={}
        self.BeadIndexs=0
        self.CoarseGrainedBeads={}

    def define_Atom(self,Index=None,Name=None):
        self.AtomIndex2Name[Index]=Name
        self.AtomName2Index[Name]=Index
    
    def define_Monomer_i(self,Types=None):
        self.Monomer_i=Types

    def define_Monomer_le(self,Types=None):
        self.Monomer_le=Types

    def define_Monomer_re(self,Types=None):
        self.Monomer_re=Types

    def define_Bead(self,Index=None,Type=None,Mapping=None,IndexList=None,Num=None):
        """
        Indexs: List
        """
        CGBEAD=CoarseGrainedBead(Type=Type,Mapping=Mapping,IndexList=IndexList)
        self.CoarseGrainedBeads[Index]=CGBEAD
        self.BeadIndexs=self.BeadIndexs+1
        
    def def_Bond(self,Type=None,Bond=None):
        self.Bonds[Type]=Bond
        self.BondsTypes.append(Type)

    def def_Angle(self,Type=None,Angle=None):
        self.Angles[Type]=Angle
        self.AnglesTypes.append(Type)

    def def_Dihedral(self,Type=None,Dihedral=None):
        self.Dihedrals[Type]=Dihedral
        self.DihedralsTypes.append(Type)
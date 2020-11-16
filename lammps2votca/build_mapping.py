import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv

MoleculeName='test'
ComponentName='polyisoprene'
N_Mols=str(44)
N_beads=str(6)
monomer_le=40+13
monomer_re=40+13
monomer_i=39+13
types=['A','B']
masses=['12 12 12 12 12 1 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1','12 12 12 12 12 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1 12 12 12 12 12 1 1 1 1 1 1 1 1']
#mapping_beads=24
beads_mass=(12.011000*5+8*1.008000)*4


votca_file=open("mapping.xml","w")
with votca_file:
    writer=csv.writer(votca_file,delimiter='\t',
                    quotechar='\t', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['<cg_molecule>'])
    writer.writerow(['<name>'+ComponentName+'</name>'])
    writer.writerow(['<ident>'+ComponentName+'</ident>'])
    writer.writerow(['<topology>'])
    writer.writerow(['<cg_beads>'])
    for beadii in range(int(N_beads)):
        if beadii==0:
            writer.writerow(['<cg_bead>'])
            writer.writerow(['<name>A0</name>'])
            writer.writerow(['<type>A</type>'])
            writer.writerow(['<mapping>A</mapping>'])
            writer.writerow(['<beads>'])
            for atomii in range(monomer_le):
                writer.writerow(['1:'+ComponentName+':'+str((atomii+1))])
            writer.writerow(['</beads>'])
            writer.writerow(['</cg_bead>'])
        elif beadii==int(N_beads)-1:
            writer.writerow(['<cg_bead>'])
            writer.writerow(['<name>A1</name>'])
            writer.writerow(['<type>A</type>'])
            writer.writerow(['<mapping>A</mapping>'])
            writer.writerow(['<beads>'])
            for atomii in range(monomer_re):
                writer.writerow(['1:'+ComponentName+':'+str((atomii+1+monomer_le+monomer_i*(int(N_beads)-2)))])
            writer.writerow(['</beads>'])
            writer.writerow(['</cg_bead>'])
        else:
            writer.writerow(['<cg_bead>'])
            writer.writerow(['<name>B'+str(beadii-1)+'</name>'])
            writer.writerow(['<type>B</type>'])
            writer.writerow(['<mapping>B</mapping>'])
            writer.writerow(['<beads>'])
            for atomii in range(monomer_i):
                writer.writerow(['1:'+ComponentName+':'+str((atomii+1+monomer_le+monomer_i*(beadii-1)))])
            writer.writerow(['</beads>'])
            writer.writerow(['</cg_bead>'])
            
    writer.writerow(['</cg_beads>'])
    writer.writerow(['<cg_bonded>'])
    writer.writerow(['<bond>'])
    writer.writerow(['<name>bond</name>'])
    writer.writerow(['<beads>'])
    
    for bondii in range(int(int(N_beads))-1):
        if bondii == 0:
            writer.writerow(['A'+str(bondii)+" "+"B"+str(bondii)])
        elif bondii == int(int(N_beads))-2:
            writer.writerow(['B'+str(bondii-1)+" "+"A1"])
        else:
            writer.writerow(['B'+str(bondii-1)+" "+"B"+str(bondii)])
    writer.writerow(['</beads>'])
    writer.writerow(['</bond>'])
    writer.writerow(['<angle>'])
    writer.writerow(['<name>angle</name>'])
    writer.writerow(['<beads>'])
    """
    for angleii in range(int(int(N_beads))-2):
        if angleii == 0:
            writer.writerow(['A'+str(angleii)+" "+"B"+str(angleii)+" "+"B"+str(angleii+1)])
        elif angleii == int(int(N_beads))-3:
            writer.writerow(['B'+str(angleii-1)+" "+'B'+str(angleii-0)+" "+"A1"])
        else:
            writer.writerow(['B'+str(angleii-1)+" "+"B"+str(angleii)+" "+"B"+str(angleii+1)])
    """
    writer.writerow(['</beads>'])
    writer.writerow(['</angle>'])
    writer.writerow(['<dihedral>'])
    writer.writerow(['<name>dihedral</name>'])
    writer.writerow(['<beads>'])
    """
    for dihedralii in range(int(int(N_beads))-3):
        if dihedralii == 0:
            writer.writerow(['A'+str(dihedralii)+" "+"B"+str(dihedralii)+" "+"B"+str(dihedralii+1) +" "+"B"+str(dihedralii+2)])
        elif dihedralii == int(int(N_beads))-4:
            writer.writerow(['B'+str(dihedralii-1)+" "+'B'+str(dihedralii)+" "+'B'+str(dihedralii+1)+" "+"A1"])
        else:
            writer.writerow(['B'+str(dihedralii-1)+" "+"B"+str(dihedralii)+" "+"B"+str(dihedralii+1)+" "+"B"+str(dihedralii+2)])
    """
    writer.writerow(['</beads>'])
    writer.writerow(['</dihedral>'])
    writer.writerow(['</cg_bonded>'])
    writer.writerow(['</topology>'])


    writer.writerow(['<maps>'])
    for index,typeii in enumerate(types):
        writer.writerow(['<map>'])
        writer.writerow(['<name>'+typeii+'</name>'])
        writer.writerow(['<weights>'])
        writer.writerow([masses[index]])
        writer.writerow(['</weights>'])
        writer.writerow(['</map>'])
    writer.writerow(['</maps>'])
    writer.writerow(['</cg_molecule>'])
    
votca_CG_file=open("mapping-CG.xml","w")
with votca_CG_file:
    writer=csv.writer(votca_CG_file,delimiter='\t',
                    quotechar='\t', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['<cg_molecule>'])
    writer.writerow(['<name>'+ComponentName+'</name>'])
    writer.writerow(['<ident>'+ComponentName+'</ident>'])
    writer.writerow(['<topology>'])
    writer.writerow(['<cg_beads>'])
    for beadii in range(int(int(N_beads))):
        writer.writerow(['<cg_bead>'])
        writer.writerow(['<name>A'+str(beadii)+'</name>'])
        writer.writerow(['<type>A</type>'])
        writer.writerow(['<mapping>A</mapping>'])
        writer.writerow(['<beads>'])
        writer.writerow(['1:'+ComponentName+':'+str(beadii+1)])
        writer.writerow(['</beads>'])
        writer.writerow(['</cg_bead>'])
    writer.writerow(['</cg_beads>'])
    writer.writerow(['<cg_bonded>'])
    writer.writerow(['<bond>'])
    writer.writerow(['<name>bond</name>'])
    writer.writerow(['<beads>'])
    for bondii in range(int(int(N_beads))-1):
        writer.writerow(['A'+str(bondii)+" "+"A"+str(bondii+1)])
    writer.writerow(['</beads>'])
    writer.writerow(['</bond>'])
    writer.writerow(['<angle>'])
    writer.writerow(['<name>angle</name>'])
    writer.writerow(['<beads>'])
    for angleii in range(int(int(N_beads))-2):
        writer.writerow(['A'+str(angleii)+" "+"A"+str(angleii+1)+" "+"A"+str(angleii+2)])
    writer.writerow(['</beads>'])
    writer.writerow(['</angle>'])
    writer.writerow(['<dihedral>'])
    writer.writerow(['<name>dihedral</name>'])
    writer.writerow(['<beads>'])
    for angleii in range(int(int(N_beads))-3):
        writer.writerow(['A'+str(angleii)+" "+"A"+str(angleii+1)+" "+"A"+str(angleii+2)+" "+"A"+str(angleii+3)])
    writer.writerow(['</beads>'])
    writer.writerow(['</dihedral>'])
    writer.writerow(['</cg_bonded>'])
    writer.writerow(['</topology>'])
    writer.writerow(['<maps>'])
    writer.writerow(['<map>'])
    writer.writerow(['<name>A</name>'])
    writer.writerow(['<weights>'])
    masses=''
    masses+=' '+str(beads_mass)
    writer.writerow([masses])
    writer.writerow(['</weights>'])
    writer.writerow(['</map>'])
    writer.writerow(['</maps>'])
    writer.writerow(['</cg_molecule>'])

votca_file=open("topo-CG.xml","w")
with votca_file:
    writer=csv.writer(votca_file,delimiter='\t',
                    quotechar='\t', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['<topology name=\''+MoleculeName+'\'>'])
    writer.writerow(['<molecules>'])
    writer.writerow(['<clear  />'])
    writer.writerow(['<molecule name=\''+ComponentName+'\' nmols=\''+N_Mols +'\' nbeads=\''+str(int(int(N_beads)))+'\'>'])
    for beadii in range(int(int(N_beads))):
        writer.writerow(['<bead name =\''  + str(beadii+1)+ '\' type=\''+ str(1)+'\' mass=\''+str(beads_mass)+ '\' q=\''+str(0)+'\' />'])   
    writer.writerow(['</molecule>'])
    writer.writerow(['</molecules>'])
    writer.writerow(['<bonded>'])
    writer.writerow(['<bond>'])
    writer.writerow(['<name>bond</name>'])
    writer.writerow(['<beads>'])
    for bondii in range(int(int(N_beads))-1):
        writer.writerow([ComponentName+":"+str(bondii+1)+"   "+ComponentName+":"+str(bondii+2)])
    writer.writerow(['</beads>'])
    writer.writerow(['</bond>'])
    writer.writerow(['<angle>'])
    writer.writerow(['<name>angle</name>'])
    writer.writerow(['<beads>'])
    for angleii in range(int(int(N_beads))-2):
        writer.writerow([ComponentName+":"+str(angleii+1)+"   "+ComponentName+":"+str(angleii+2)+"   "+ComponentName+":"+str(angleii+3)])
    writer.writerow(['</beads>'])
    writer.writerow(['</angle>'])
    writer.writerow(['<dihedral>'])
    writer.writerow(['<name>dihedral</name>'])
    writer.writerow(['<beads>'])
    for angleii in range(int(int(N_beads))-3):
        writer.writerow([ComponentName+":"+str(angleii+1)+"   "+ComponentName+":"+str(angleii+2)+"   "+ComponentName+":"+str(angleii+3)+"   "+ComponentName+":"+str(angleii+4)])
    writer.writerow(['</beads>'])
    writer.writerow(['</dihedral>'])
    writer.writerow(['</bonded>'])
    writer.writerow(['</topology>'])


import sys
sys.path.append('/home/bruce/Dropbox/code/research/votca_scripts/lammps2votca')

import lammps2votca

system=lammps2votca.System(name='polystyrene',Number_Monomers=10,Number_Moles=29)

topo=lammps2votca.Topo(system)
topo.chemfile_read('polystyrene_Mono10.lammpsdata')
topo.output(file_='topo.xml')

Str=lammps2votca.Structure(Name='polystyrene')
Str.define_Atom(Index=1,Name='C')
Str.define_Atom(Index=2,Name='C')
Str.define_Atom(Index=3,Name='C')
Str.define_Atom(Index=4,Name='H')
Str.define_Atom(Index=5,Name='C')
Str.define_Atom(Index=6,Name='H')
Str.define_Atom(Index=7,Name='C')
Str.define_Atom(Index=8,Name='H')

Str.define_Bead(Index=1,Type='A',Mapping='A',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
Str.define_Bead(Index=2,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=3,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=4,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=5,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=6,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=7,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=8,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=9,Type='A',Mapping='B',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Str.define_Bead(Index=10,Type='A',Mapping='A',IndexList=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

Str.def_Bond(Type="AA",Bond=['A','A'])

Str.def_Angle(Type="AAA",Angle=['A','A','A'])

Str.def_Dihedral(Type="AAAA",Dihedral=['A','A','A','A'])

map_=lammps2votca.Mapping(System=system,Structure=Str,Topo=topo,filename="mapping.xml")
map_.write()

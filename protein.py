from Bio.PDB import *

parser = MMCIFParser()
structure = parser.get_structure("myFile","1dg3.cif")
chain = structure[1][1]
chain.get_atoms()
mmcif_dict = MMCIF2Dict("1dg3.cif")
y_list = mmcif_dict["_atom_site.Cartn_y"]
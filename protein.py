from Bio.PDB import *
from matplotlib import pyplot as plt

parser = MMCIFParser()
structure = parser.get_structure("myFile","1dg3.cif")
chain = structure[0]['A']
xdata = []
ydata = []
for atom in chain.get_atoms():
    if atom.get_name() == 'CA':
        v=atom.get_vector()
        xdata.append(v[0])
        ydata.append(v[1])

plt.scatter(xdata,ydata)
#mmcif_dict = MMCIF2Dict("1dg3.cif")
#y_list = mmcif_dict["_atom_site.Cartn_y"]
#print(list)
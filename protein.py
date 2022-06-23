from Bio.PDB import *
from matplotlib import pyplot as plt

# initilization of the parser
parser = MMCIFParser()
structure = parser.get_structure("myFile","1dg3.cif")
# get 1DG3 specific data from the structure
chain = structure[0]['A']
xdata = []
ydata = []
for atom in chain.get_atoms():
    # filter the atoms based on the name
    if atom.get_name() == 'CA':
        # get the coordinates of these atoms
        v=atom.get_vector()
        # add the coordinates to the data to plot graph
        xdata.append(v[0])
        ydata.append(v[1])

#plot the scatter graph using matplotlib
plt.scatter(xdata,ydata)
plt.tight_layout()
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.show()
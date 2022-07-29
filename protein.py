from Bio.PDB import *
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

# initilization of the parser
parser = MMCIFParser()
structure = parser.get_structure("myFile","1dg3.cif")
for chain in structure.get_chains():
    print(chain)
# get 1DG3 specific data from the structure
chain = structure[0]['A']
x_data = []
y_data = []
pca_input = []
for atom in chain.get_atoms():
    # filter the atoms based on the name
    if atom.get_name() == 'CA':
        # get the coordinates of these atoms
        v=atom.get_vector()
        # add the coordinates to the data to plot graph
        x_data.append(v[0])
        y_data.append(v[1])
        xyz=[v[0],v[1],v[2]]
        pca_input.append(xyz)

#plot the scatter graph using matplotlib
plt.scatter(x_data,y_data)
plt.tight_layout()
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.show()

# reduced into 2 dimensions
pca = PCA(n_components=2)
pca_result = pca.fit_transform(pca_input)
# categorize x and y used in graph
pca_x=[]
pca_y=[]
for element in pca_result:
    pca_x.append(element[0])
    pca_y.append(element[1])
# plot the graph
plt.scatter(pca_x,pca_y)
plt.tight_layout()
plt.show()


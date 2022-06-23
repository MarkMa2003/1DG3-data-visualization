# 1DG3 Data Visualization

*For this task, I've used Python with the Biopython, scikit-learn, and matplotlib libraries.*

## Plotting the Cα coordinates on the plane z=0 

In the first part of the task, I used the Biopython to handle data and matplotlib to plot the graph. 

As shown below, I firstly initialize the MMCIFParser that will be used to parse the file. Once I get the structure, I filtered the data to obtain 1dg3 specific chain data given that 1dg3 have single model and chain.
```parser = MMCIFParser()
structure = parser.get_structure("myFile","1dg3.cif")
chain = structure[0]['A']
```

Later, I create the empty arrays that are going to store the data that used in later to plot graph and perform principal component analysis and apply dimensionality reduction, as shown below

```
x_data = []
y_data = []
pca_input = []
```

As in the loop shown below, I filtered the atoms to Cα atoms only. Then, I get the vector of their coordinates using `get_vector()` Once I get their xyz coordinates, firstly, I append the x coordinates and y coordinates into their respective arrays that will be used to plot the graph of part 1. Secondly, I create a array that include all coordinates and add this array into the 2-dimentional array that is used as an argument for the PCA dimentionaility reduction.

```
for atom in chain.get_atoms():
    if atom.get_name() == 'CA':
        v=atom.get_vector()
        x_data.append(v[0])
        y_data.append(v[1])
        xyz=[v[0],v[1],v[2]]
        pca_input.append(xyz)
```

At last of this part, I used matplotlib to plot a scatter graph for this part of task.

```plt.scatter(x_data,y_data)
plt.tight_layout()
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.show()
```

The final graph is shown below:
![xygraph](./pictures/xygraph.png)

## Computing PCA on the Cα coordinates and plotting a graph using the data. 

For this part of the task, I've used scikit-learn to perform PSA dimensionality reduction and matplotlib to plot the graph. At the begining,I set up the PSA to perform the reduction. I set the transformed dimension to 2 as the task describes using `n_components=2` and then used the data we collected in previous code as an argument that will be transformed, and then we get back the transformed data `pca_result`

```
pca = PCA(n_components=2)
pca_result = pca.fit_transform(pca_input)
```
At last, we modify the data using a loop so that it can be take as an argument to the matplotlib as x-axis and y-axis.
```
pca_x=[]
pca_y=[]
for element in pca_result:
    pca_x.append(element[0])
    pca_y.append(element[1])
plt.scatter(pca_x,pca_y)
plt.tight_layout()
plt.show()
```
The final graph is shown below:
![xygraph](./pictures/pcagraph.png)

## Plots comparision and analysis

As what we can see from the 3-D graph, the first plot where z=0 is the corss-section when the z-axis is 0 of the 3-D graph. In comparsion, the second graph is the plot of the cross-section along the plane that most points cluster around it since we performed PCA dimentionality reduction. As a result, the two graphs are very different from each other. 

---
reference: the documentation of [Biopython](https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ), [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA), and [matplotlib](https://matplotlib.org/stable/api/index.html).
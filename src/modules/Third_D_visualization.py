import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

def plot_3d_graph(G):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    pos = nx.spring_layout(G, dim=3, scale=2)

    for node in G.nodes:
        x, y, z = pos[node]
        ax.scatter(x, y, z, s=100)
        ax.text(x, y, z, node)

    for edge in G.edges:
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, color='grey')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


import networkx as nx
import sys
sys.path.append("src/modules") 
import network_visualization as nv
import Third_D_visualization as TD

def _3D_ (pos,G) :
    pos = nx.spring_layout(G, dim=3)
    with open('data/processed/nodes.txt', 'w') as f:
        for node in G.nodes:
            x, y, z = pos[node]
            f.write(f'{x},{y},{z}\n')

        for edge in G.edges:
            x = [pos[edge[0]][0], pos[edge[1]][0]]
            y = [pos[edge[0]][1], pos[edge[1]][1]]
            z = [pos[edge[0]][2], pos[edge[1]][2]]
            f.write(f'{x[0]}, {y[0]}, {z[0]}\n')
            f.write(f'{x[1]}, {y[1]}, {z[1]}\n')
    TD.build(G)
    
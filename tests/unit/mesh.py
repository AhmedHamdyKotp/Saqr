import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx


def make_the_nodes(profession_found):
    G = nx.Graph()
    GN = []
    for profession in profession_found:
        G.add_node(profession, type='profession')

    for profession, urls in profession_found.items():
        for url in urls:
            individual_node = f"{profession}_{url.split('/')[-1]}"
            if len(individual_node) > 10 :
                individual_node = individual_node[:10]
            G.add_node(individual_node, type='individual', profession=profession, url=url)
            G.add_edge(individual_node, profession)  
            GN.append(profession)
    centrality = nx.degree_centrality(G)
    sortion = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

    print("Top 10 nodes by degree centrality:")
    for node, cent in sortion[:10]:
        print(f"{node}: {cent}")
    com = nx.algorithms.community.greedy_modularity_communities(G)
    print(f"Detected {len(com)} communities.")
    node_sizes = [G.degree(node) * 100 for node in G]
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]

    # Create a 3D layout
    pos = nx.spring_layout(G, dim=3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for node in G.nodes:
        x, y, z = pos[node]
        node_size = G.degree(node) * 100  # Calculate node size here
        node_color = 'skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen'
        ax.scatter(x, y, z, s=node_size, c=node_color)

    for edge in G.edges:
        x = [pos[edge[0]][0], pos[edge[1]][0]]
        y = [pos[edge[0]][1], pos[edge[1]][1]]
        z = [pos[edge[0]][2], pos[edge[1]][2]]
        ax.plot(x, y, z, color='gray')

    # plt.show()


    return G

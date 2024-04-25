import networkx as nx
import matplotlib.pyplot as plt

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
    pos = nx.spring_layout(G, k=0.3)
    x = [pos[node][0] for node in G.nodes if G.nodes[node]['type'] == 'profession']
    y = [pos[node][1] for node in G.nodes if G.nodes[node]['type'] == 'profession']
    print("x:", x)
    print("y:", y)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
    plt.show()

    return G

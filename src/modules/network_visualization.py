import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append('algorithms')

import hmap as ht
import heatmap_visualization as hm
import third_D_ as td
def add_nodes(G, profession_found):
    for profession, urls in profession_found.items():
        G.add_node(profession, type='profession')
        for url in urls:
            individual_node = f"{profession}_{url.split('/')[-1]}"[:10]
            G.add_node(individual_node, type='individual', profession=profession, url=url)
            G.add_edge(individual_node, profession)

def print_centrality(G):
    centrality = nx.degree_centrality(G)
    sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    print("Top 10 nodes by degree centrality:")
    for node, cent in sorted_centrality[:10]:
        print(f"{node}: {cent}")

def print_communities(G):
    com = nx.algorithms.community.greedy_modularity_communities(G)
    print(f"Detected {len(com)} communities.")

def draw_graph(G):
    node_sizes = [G.degree(node) * 100 for node in G]
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]
    pos = nx.spring_layout(G, k=0.3)
    heatmap_algorithms(pos,G)
    td._3D_(pos,G)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
    plt.show()
    return pos

    
def make_the_nodes(profession_found):
    G = nx.Graph()
    add_nodes(G, profession_found)
    print_centrality(G)
    print_communities(G)
    draw_graph(G)
    return G

def heatmap_algorithms(pos,G):
    x = []
    y = []
    for node in G.nodes:
        if G.nodes[node]['type'] == 'profession':
            x.append(pos[node][0])
            y.append(pos[node][1])
    ht.getter(x,y)
    hm.getter(x,y)
    hm.start()

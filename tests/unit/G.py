import json
import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append('algorithms')
sys.path.append('src\modules')
import tkinter as tk
import hmap as ht
import heatmap_visualization as hm
import Third_D_visualization as TD

def make_the_nodes():
    with open('data/processed/profession_found.json', 'r') as f:
        profession_found = json.load(f)
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
    com = nx.algorithms.community.greedy_modularity_communities(G)
    G_dict = nx.to_dict_of_dicts(G)

    nx.write_gpickle(G, "graph.gpickle")


    node_sizes = [G.degree(node) * 100 for node in G]
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
    plt.show()
    # TD.plot_3d_graph(G)

    return G

make_the_nodes()
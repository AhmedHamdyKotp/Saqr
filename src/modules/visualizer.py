

import networkx as nx
import matplotlib.pyplot as plt

def make_the_nodes(profession_found):
    G = nx.Graph()
    for profession in profession_found:
        G.add_node(profession, type='profession')

    for profession, urls in profession_found.items():
        for url in urls:
            individual_node = f"{profession}_{url.split('/')[-1]}"
            if len(individual_node) > 10 :
                individual_node = individual_node[:10]
            G.add_node(individual_node, type='individual', profession=profession, url=url)
            G.add_edge(individual_node, profession)  # Connect individual to profession

    for pro_a, urls_a in profession_found.items():
        for pro_b, urls_b in profession_found.items():
            if pro_a != pro_b:
                shared_urls = set(urls_a).intersection(urls_b)
                for url in shared_urls:
                    individual_a = f"{pro_a}_{url.split('/')[-1]}"
                    individual_b = f"{pro_b}_{url.split('/')[-1]}"
                    if len(individual_a) > 10 :
                        individual_a = individual_a[:10]
                    if len(individual_b) > 10 :
                        individual_b = individual_b[:10]                    
                   
                    G.add_edge(individual_a, individual_b)  # Connect individuals sharing URLs

    # Node sizes based on degree
    node_sizes = [G.degree(node) * 100 for node in G]

    # Node colors
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]

    # Position nodes using the spring layout
    pos = nx.spring_layout(G, k=0.3)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
    plt.show()

    return G

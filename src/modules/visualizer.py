

import networkx as nx
import matplotlib.pyplot as plt

def make_the_nodes(profession_found):
    G = nx.Graph()
    for profession in profession_found:
        G.add_node(profession, type='profession')

    for profession, urls in profession_found.items():
        for url in urls:
            individual_node = f"{profession}_{url.split('/')[-1]}"  # Unique identifier for the individual
            G.add_node(individual_node, type='individual', profession=profession, url=url)
            G.add_edge(individual_node, profession)  # Connect individual to profession

    for pro_a, urls_a in profession_found.items():
        for pro_b, urls_b in profession_found.items():
            if pro_a != pro_b:
                shared_urls = set(urls_a).intersection(urls_b)
                for url in shared_urls:
                    individual_a = f"{pro_a}_{url.split('/')[-1]}"
                    individual_b = f"{pro_b}_{url.split('/')[-1]}"
                    G.add_edge(individual_a, individual_b)  # Connect individuals sharing URLs
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]
    pos = nx.spring_layout(G,k=0.3)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=8)
    plt.show()
    
    return G

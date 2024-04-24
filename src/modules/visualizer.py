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
            G.add_edge(individual_node, profession)  # Connect individual to profession
            GN.append(profession)

    # Calculate centrality measures
    centrality = nx.degree_centrality(G)
    sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

    print("Top 10 nodes by degree centrality:")
    for node, cent in sorted_centrality[:10]:
        print(f"{node}: {cent}")

    # Community detection
    communities = nx.algorithms.community.greedy_modularity_communities(G)
    print(f"Detected {len(communities)} communities.")

    node_sizes = [G.degree(node) * 100 for node in G]
    node_colors = ['skyblue' if G.nodes[node]['type'] == 'individual' else 'lightgreen' for node in G]
    pos = nx.spring_layout(G, k=0.3)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=8)
    plt.show()

    return G
